---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T07:13:49.792440'
end_time: '2026-08-20T07:29:12.966846'
duration_seconds: 923.17
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Hydrocephalus
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 6
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Congenital_Hydrocephalus-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Hydrocephalus
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Congenital Hydrocephalus** covering all of the
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
- **Disease Name:** Congenital Hydrocephalus
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Congenital Hydrocephalus** covering all of the
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


# Congenital Hydrocephalus: Disease Characteristics Research Report

## Executive summary

Congenital hydrocephalus (CH) is a heterogeneous developmental disorder in which impaired cerebrospinal-fluid (CSF) production–flow–absorption homeostasis causes prenatal or neonatal ventricular enlargement, often with raised intracranial pressure and secondary injury to the developing brain. It is not a single molecular disease: causes include monogenic and chromosomal disorders, aqueductal or hindbrain malformations, neural-tube defects, hemorrhage, and congenital infection. A useful current model therefore combines **developmental brain dysgenesis** with the traditional **CSF-dynamics disorder** concept. A 2024 review states that CH “results from an imbalance in production, flow, or absorption of cerebrospinal fluid.” (aragon2024geneticetiologiesand pages 1-2)

The most defensible aggregate identifier is **MONDO:0016349**. The strongest established monogenic associations are **L1CAM** and **AP1S2** (X-linked) and **MPDZ** and **CCDC88C** (autosomal recessive), while newer human evidence supports a broader architecture including **SMARCC1, TRIM71, WDR81, FOXJ1, PTCH1, LDB1, CLASP1, DNMBP**, and **FSD1L**. Genetic factors may contribute to as many as 40% of cases, although older stringent estimates assigned a specific molecular diagnosis to fewer than 5%, reflecting case selection and rapidly changing sequencing knowledge rather than a contradiction. (OpenTargets Search: congenital hydrocephalus, liu2024congenitalhydrocephalusa pages 3-5, liu2024congenitalhydrocephalusa pages 1-3)

Definitive treatment remains surgical—usually ventriculoperitoneal shunting or, in selected infants, endoscopic third ventriculostomy with choroid-plexus cauterization (ETV/CPC). These procedures control CSF and intracranial pressure but generally do not reverse the initiating developmental defect. No disease-modifying drug, gene therapy, or RNA therapy is approved for CH. (aragon2024geneticetiologiesand pages 1-2, warf2023endoscopicthirdventriculostomy pages 1-2)

## 1. Disease information

### Definition and scope

CH denotes hydrocephalus beginning prenatally or present at birth/early infancy. Excess ventricular CSF produces ventriculomegaly; if pressure rises, surrounding white matter and cortex are stretched or compressed, cerebral perfusion may fall, and progressive neurological injury can follow. “Congenital ventriculomegaly” is related but not fully synonymous: ventriculomegaly is an imaging phenotype and may be mild, stable, or non-hypertensive, whereas hydrocephalus implies pathological CSF dynamics and usually progressive ventricular distension or clinical consequences. (aragon2024geneticetiologiesand pages 1-2, zhang2024areviewof pages 1-2, isaacs2018agespecificglobalepidemiology pages 2-4)

### Identifiers and synonyms

- **MONDO:** MONDO:0016349, congenital hydrocephalus. Subtypes include MONDO:0010611, X-linked hydrocephalus with stenosis of the aqueduct of Sylvius; MONDO:0014085, nonsyndromic autosomal-recessive hydrocephalus 2; MONDO:0017116, congenital communicating hydrocephalus; and MONDO:0054794, congenital hydrocephalus 3 with brain anomalies. (OpenTargets Search: congenital hydrocephalus)
- **MeSH:** Hydrocephalus, **D006849**; congenital forms are generally indexed with congenital-abnormality qualifiers rather than a uniquely specific MeSH disease record. (NCT06664372 chunk 1)
- **ICD-10-CM:** **Q03.-**, congenital hydrocephalus; Q03.0 malformations of aqueduct of Sylvius, Q03.1 atresia of foramina of Magendie and Luschka, Q03.8 other congenital hydrocephalus, Q03.9 unspecified.
- **ICD-11:** congenital hydrocephalus is represented among structural developmental anomalies of the nervous system; the exact extension code should be validated against the current national ICD-11 implementation.
- **OMIM:** best represented by etiologic subtypes rather than one universal record—classically L1CAM-related X-linked hydrocephalus/HSAS, MPDZ-related nonsyndromic hydrocephalus, CCDC88C-related hydrocephalus, and WDR81-related congenital hydrocephalus with brain anomalies.
- **Synonyms:** congenital/infantile hydrocephalus, hydrocephalus present at birth, congenital communicating or obstructive hydrocephalus, and—less precisely—congenital ventriculomegaly. “Aqueductal stenosis” is a mechanism/subtype, not a synonym for all CH.

This report synthesizes **aggregated disease-level resources, systematic reviews, cohorts, trials, and model studies**. It does not use individual EHR-level patient data.

## 2. Etiology

### Causal factors

1. **Genetic/developmental:** pathogenic variation affecting neuronal adhesion and axon development (L1CAM), vesicle trafficking (AP1S2), epithelial polarity and junctions (MPDZ), Wnt/ciliary orientation (CCDC88C), chromatin regulation and neural progenitors (SMARCC1), RNA regulation/neurogenesis (TRIM71), ciliogenesis (FOXJ1), and broader cortical or hindbrain development. (deng2025geneticandmolecular pages 15-15, liu2024congenitalhydrocephalusa pages 3-5, deng2025geneticandmolecular pages 4-5)
2. **Structural:** cerebral-aqueduct stenosis, fourth-ventricular outlet obstruction, Dandy–Walker spectrum, Chiari II/myelomeningocele, craniosynostosis, intracranial cysts, and tumors. Aqueductal stenosis accounts for much nonsyndromic obstructive CH. (zhang2024areviewof pages 1-2, liu2024congenitalhydrocephalusa pages 3-5)
3. **Hemorrhagic:** fetal or neonatal intraventricular hemorrhage can obstruct CSF pathways and impair absorption; in preterm infants, posthemorrhagic hydrocephalus is especially important but is not always classified as strictly congenital. (newland2024understandingandmodeling pages 2-4, warf2023endoscopicthirdventriculostomy pages 1-2)
4. **Infectious:** congenital infections and neonatal meningitis can produce inflammation, ependymal injury, fibrosis, and obstruction. Globally, infection is a major pediatric cause, especially in resource-limited settings. (newland2024understandingandmodeling pages 2-4, dewan2019globalhydrocephalusepidemiology pages 1-2)
5. **CSF-secretory/transport defects:** altered choroid-plexus NKCC1 and other ion transporters can increase or dysregulate CSF secretion; pure CSF overproduction is less common than obstruction or developmental dysgenesis. (zhang2024areviewof pages 1-2, deng2025geneticandmolecular pages 5-6, liu2024congenitalhydrocephalusa pages 1-3)

### Risk factors

**Genetic risks** include a pathogenic family variant, affected male relatives in L1CAM/AP1S2 families, parental consanguinity for recessive disease, and parental germline mosaicism or a de novo dominant variant. The recurrence risk is therefore cause-specific: approximately 50% of sons of a heterozygous mother may inherit an X-linked variant; recessive carrier couples have a 25% affected-pregnancy risk; and a proven de novo variant usually carries low—but non-zero—recurrence risk because of germline mosaicism.

**Environmental/obstetric risks** supported at the hydrocephalus or associated-malformation level include maternal/fetal infection, prematurity and intraventricular hemorrhage, neural-tube defects, poorly controlled pregestational diabetes, obesity, teratogenic exposures, and inadequate folate for neural-tube-defect-associated cases. These factors should not be interpreted as explaining most isolated CH. The higher burden in low- and middle-income countries reflects more neural-tube defects and postinfectious disease, high birth rates, and reduced access to prenatal and neurosurgical care. (dewan2019globalhydrocephalusepidemiology pages 1-2)

### Protective factors and gene–environment interaction

There is no validated protective human allele for CH. Prevention is largely **cause-specific**: periconceptional folic acid prevents many neural-tube defects and thereby some secondary Chiari II/myelomeningocele-associated hydrocephalus; vaccination and infection prevention reduce congenital and neonatal infectious causes; optimized maternal diabetes control reduces congenital-malformation risk; and safe obstetric/neonatal care reduces prematurity-associated hemorrhage. Population surveillance, however, did not find folate-fortification status significantly associated with hydrocephalus incidence as a whole, emphasizing that folate is not a general CH preventive therapy. (isaacs2018agespecificglobalepidemiology pages 1-2)

Proposed gene–environment mechanisms include folate-dependent methylation interacting with developmental susceptibility, and inflammatory injury interacting with ciliary/ependymal reserve. These remain incompletely established in humans; most mechanistic evidence comes from animal studies. (deng2025geneticandmolecular pages 5-6)

## 3. Phenotypes

The phenotype is highly variable by etiology, timing, pressure, associated malformations, and access to treatment.

- **Ventriculomegaly/hydrocephalus** (HP:0002119/HP:0000238): prenatal or neonatal; mild to severe; stable in some mild ventriculomegaly but generally progressive when active hydrocephalus is untreated.
- **Macrocephaly and accelerated head growth** (HP:0000256), widened sutures and **bulging fontanelle** (HP:0000239): typical infant signs because the skull remains compliant.
- **Raised intracranial pressure** (HP:0002516): irritability, poor feeding, vomiting, sleepiness, “sun-setting” eyes, apnea or bradycardia, and progressive neurological decline. Severity can fluctuate with shunt function.
- **Aqueductal stenosis** (HP:0002625): common obstructive imaging phenotype, particularly in L1CAM-related disease.
- **Corpus-callosum dysgenesis** (HP:0001273), cortical malformation, enlarged ventricles, reduced white matter, or hindbrain malformation: congenital and usually stable structural abnormalities, although their functional consequences evolve with development.
- **Developmental delay** (HP:0001263), intellectual disability (HP:0001249), speech/language impairment, and learning disability: variable, often lifelong; major determinants of education, independence, and caregiver burden.
- **Motor impairment:** hypotonia or spasticity (HP:0001257), abnormal gait (HP:0001288), poor coordination, and cerebral-palsy-like disability.
- **Seizures** (HP:0001250), visual dysfunction and endocrine/hypothalamic sequelae occur in subsets, driven more by associated brain injury or malformation than ventricular size alone.

Pediatric morbidity documented across studies includes seizures, developmental delay, psychomotor impairment, and gait difficulty. Frequencies cannot be assigned reliably across “CH” because cohorts differ sharply in cause and severity; phenotype frequencies should be stored by molecular or structural subtype whenever possible. Untreated disease can progress to severe disability or death, whereas early successful pressure control may stabilize or improve pressure-related manifestations. (isaacs2018agespecificglobalepidemiology pages 9-13, isaacs2018agespecificglobalepidemiology pages 2-4)

Quality-of-life effects include repeated emergency assessments and operations, cognitive and motor disability, school limitations, caregiver stress, and substantial cost. U.S. pediatric inpatient hydrocephalus care has been estimated at about **$2 billion annually**. No single CH-specific QoL instrument is universally accepted; Hydrocephalus Outcome Questionnaire, PedsQL, PROMIS pediatric domains, caregiver-burden measures, and functional/developmental testing are more informative than ventricular size alone. (isaacs2018agespecificglobalepidemiology pages 9-13)

## 4. Genetic and molecular information

### Established and emerging genes

The conservative established set comprises **L1CAM, AP1S2, MPDZ, and CCDC88C**. Recent disease-resource evidence also strongly associates **WDR81, SMARCC1, TRIM71**, and additional candidates. L1CAM variants may explain approximately **5–15%** of CH, especially males with aqueductal stenosis and L1-spectrum findings. (OpenTargets Search: congenital hydrocephalus, liu2024congenitalhydrocephalusa pages 3-5)

- **L1CAM:** X-linked; missense, nonsense, frameshift, splice and deletion variants. Loss of neuronal cell-adhesion signaling disrupts axon guidance, corticospinal-tract and callosal development; severe loss-of-function variants often produce hydrocephalus, adducted thumbs, spasticity and intellectual disability.
- **AP1S2:** X-linked loss-of-function; abnormal adaptor-protein-mediated vesicle trafficking; syndromic intellectual disability with hydrocephalus in some individuals.
- **MPDZ:** autosomal recessive, generally biallelic loss-of-function; disrupts apical junctions/polarity in neuroepithelium and ependyma, causing communicating or obstructive hydrocephalus.
- **CCDC88C:** autosomal recessive; biallelic variants perturb Wnt signaling and ciliary orientation/CSF flow.
- **WDR81:** recessive; congenital hydrocephalus with brain anomalies and variable cerebellar/neurodevelopmental disease.
- **SMARCC1:** dominant/de novo and familial variants with incomplete penetrance; altered BAF/SWI–SNF chromatin remodeling in neural progenitors and ependymal development.
- **TRIM71:** predominantly dominant/de novo human evidence; perturbs RNA regulation and neural-progenitor fate.
- **FOXJ1:** heterozygous loss-of-function can impair multiciliated ependymal differentiation and produce communicating hydrocephalus, sometimes with motile-ciliopathy features.
- Other phenotype-dependent genes include **PTCH1, SHH, CRB2, EML1, PIK3CA, PTEN, MTOR, FMN2, FXYD2, ZEB1, SBF2, GNAI2, CC2D2A, DNAH5, IFT172**, and **VANGL2**. Many cause broader syndromes in which hydrocephalus is one feature. (liu2024congenitalhydrocephalusa pages 15-16, liu2024congenitalhydrocephalusa pages 3-5, liu2024congenitalhydrocephalusa pages 5-6)

Open Targets’ current CH association set contains 11 targets, led by L1CAM, MPDZ, WDR81, CCDC88C, SMARCC1 and TRIM71; this is useful for prioritization but is not equivalent to a clinically curated definitive-gene list. (OpenTargets Search: congenital hydrocephalus)

### Variant interpretation

Most causal variants are **germline**. Somatic mosaic activating variants in PI3K–AKT–mTOR pathway genes may cause segmental brain overgrowth with ventriculomegaly/hydrocephalus. Variant classes include loss-of-function, deleterious missense, splice-altering variants, exon/gene deletions, copy-number variants and chromosomal rearrangements. Population frequency should be checked in ancestry-matched gnomAD data; a credible severe dominant or X-linked variant is normally absent or extremely rare, while recessive carrier alleles can be present at low frequency. Exact frequency and ACMG classification must be recorded per variant and transcript—there is no disease-wide allele frequency.

**VUSs must not be used alone** for prenatal prognosis, pregnancy decisions, or cascade testing. Segregation, phenotype concordance, ClinVar/ClinGen evidence, RNA studies, and functional assays should be pursued. Penetrance is gene- and variant-specific; incomplete penetrance is particularly documented for SMARCC1. Expressivity is often broad. Anticipation is not characteristic. Germline mosaicism is relevant after apparently de novo disease. Consanguinity increases recessive disease yield; no universal carrier frequency or single founder variant applies globally. (deng2025geneticandmolecular pages 15-15, liu2024congenitalhydrocephalusa pages 15-16)

### Chromosomal and epigenetic abnormalities

Aneuploidies, pathogenic CNVs and rearrangements may present with ventriculomegaly plus multiple anomalies, justifying chromosomal microarray as a first-line prenatal test. Epigenetic evidence is strongest for altered chromatin regulation through SMARCC1 and experimental folate/methylation effects; a reproducible CH-specific methylation signature suitable for clinical diagnosis has not been established. (liu2024congenitalhydrocephalusa pages 15-16, deng2025geneticandmolecular pages 5-6)

## 5. Environmental information

Relevant non-genetic contributors are fetal/neonatal hemorrhage, intrauterine or neonatal infection, neural-tube defects, teratogenic medication/exposure, and structural obstruction. Smoking, alcohol, pollution, occupational exposure and radiation are not established specific causes of isolated CH, although they may increase general adverse-pregnancy or malformation risk. Evidence should therefore be annotated as **associated**, not causal, unless a specific fetal infection, hemorrhage, or teratogenic syndrome is demonstrated.

Potential infectious agents include cytomegalovirus, toxoplasma, rubella and other congenital infections, and neonatal bacterial meningitis. Mechanistically, infection causes ependymal/choroid-plexus inflammation, debris and fibrosis, impaired absorption, or aqueductal obstruction. The resulting condition may be congenital or early acquired depending on timing.

## 6. Mechanism and pathophysiology

### Integrated causal chain

**Upstream developmental trigger**—pathogenic variant, malformation, hemorrhage, or infection—can cause one or more of the following:

1. **Ciliogenesis/motility failure:** FOXJ1, DNAH5, WDR16/WDR78 and related defects impair coordinated beating of ependymal multicilia → abnormal local CSF movement and altered ventricular-wall signaling → ventricular enlargement. Suggested GO: cilium movement (GO:0003341), cilium assembly, CSF circulation. (liu2024congenitalhydrocephalusa pages 3-5, liu2024congenitalhydrocephalusa pages 5-6, liu2024congenitalhydrocephalusa pages 1-3)
2. **Neuroepithelial junction/polarity failure:** MPDZ, CCDC88C, NAPA and related defects disrupt adherens/tight junctions and planar polarity → ventricular-zone denudation, abnormal aqueduct development or closure → obstructed flow. Suggested GO: cell–cell junction organization (GO:0045216), epithelial cell polarity, vesicle-mediated transport. (liu2024congenitalhydrocephalusa pages 6-8, deng2025geneticandmolecular pages 4-5)
3. **Disordered neurogenesis/chromatin/RNA regulation:** SMARCC1, TRIM71, PTCH1/SHH, PTEN–PI3K–mTOR and other pathways alter neural-progenitor proliferation, differentiation and brain architecture → dysplastic cortex, aqueduct or posterior fossa plus secondary CSF obstruction. Suggested GO: neurogenesis (GO:0022008), neural precursor proliferation, chromatin remodeling.
4. **Choroid-plexus transport dysregulation:** altered NKCC1, Na+/K+-ATPase, bicarbonate/chloride transport, TRPV4 or SGK1 signaling → excessive or mistimed ion/water secretion → increased ventricular CSF load. The choroid plexus produces an estimated **80–90%** of CSF. Suggested GO: ion transport (GO:0006811), transepithelial transport and water homeostasis. (deng2025geneticandmolecular pages 5-6, liu2024congenitalhydrocephalusa pages 1-3)
5. **Subcommissural organ–Reissner fiber abnormalities:** defective SCO-spondin/Reissner-fiber formation alters aqueduct patency and CSF protein homeostasis; evidence is strongest in zebrafish and rodents. (liu2024congenitalhydrocephalusa pages 6-8, deng2025geneticandmolecular pages 5-6)
6. **Inflammation/hemorrhage:** blood products or pathogens activate macrophages/microglia, NF-κB, cytokine, TGF-β and related pathways → ependymal/ciliary injury, fibrosis and impaired CSF absorption/flow. Suggested GO: inflammatory response (GO:0006954), glial activation, response to oxidative stress. (deng2025geneticandmolecular pages 15-15)

The common downstream chain is **ventricular CSF accumulation → ventricular wall stretch and raised pressure → reduced cerebral perfusion and white-matter compression → axonal/myelin injury, gliosis, inflammation and sometimes apoptosis → motor, cognitive, visual and seizure phenotypes**. (zhang2024areviewof pages 1-2, deng2025geneticandmolecular pages 4-5, NCT06693752 chunk 1)

Principal cell types are multiciliated **ependymal cells**, **choroid-plexus epithelial cells**, radial glia/neural stem and progenitor cells, neurons, oligodendrocyte-lineage cells, astrocytes, microglia/macrophages and vascular endothelium. Relevant subcellular structures include motile cilia/axoneme, basal bodies, apical junction complexes, endosomes/lysosomes, nucleus/chromatin and ion-transporter-rich apical membranes.

### Molecular profiling and advanced technology

Human CH-specific single-cell, spatial transcriptomic, proteomic, metabolomic and lipidomic reference datasets remain sparse. Rat expression studies report altered **Cck, Nfix, Lgals3, Gsta1, Xdh**, reduced **Ptpn20**, and elevated phosphorylated NKCC1, but these are model-derived biomarkers, not validated clinical diagnostics. (deng2025geneticandmolecular pages 4-5, deng2025geneticandmolecular pages 5-6)

Current functional genomics relies heavily on CRISPR/knockout mice and zebrafish, morpholino knockdown, fetal/neonatal MRI, CSF proteomics, and patient-specific sequencing. Organoids and iPSC-derived neuroepithelial/choroid-plexus systems are promising for variant testing and drug screening, but no organoid assay is standard of care.

## 7. Anatomical structures affected

The primary organ is the **central nervous system**, especially the ventricular system, cerebral aqueduct, foramina/outlets of the fourth ventricle, subarachnoid spaces and CSF-absorption pathways. Directly affected tissues include ependyma, choroid plexus, periventricular white matter, germinal matrix/ventricular zone, cortex, corpus callosum, optic pathways and, in syndromic disease, cerebellum and brainstem. Disease is typically bilateral/central rather than lateralized; asymmetry may occur with a focal obstruction or unilateral ventriculomegaly.

Suggested UBERON concepts are brain ventricular system, lateral/third/fourth ventricle, cerebral aqueduct, choroid plexus, ependyma, cerebral cortex, corpus callosum, cerebellum and subarachnoid space. Secondary extracranial involvement is syndrome-specific—for example kidney cysts in ciliopathies, skeletal/limb findings in L1 syndrome or neural-tube defects, and craniofacial abnormalities in craniosynostosis. (newland2024understandingandmodeling pages 2-4, liu2024congenitalhydrocephalusa pages 1-3)

The following curation table consolidates phenotype, anatomy, cell, mechanism, gene and intervention annotations.

| domain | key item | suggested ontology term/identifier | evidence/interpretation |
|---|---|---|---|
| disease | Congenital hydrocephalus | MONDO:0016349 | Congenital/pediatric hydrocephalus entity used in Open Targets; defined as abnormal CSF accumulation beginning prenatally or at birth, with major genetic and structural heterogeneity (OpenTargets Search: congenital hydrocephalus, aragon2024geneticetiologiesand pages 1-2, zhang2024areviewof pages 1-2, liu2024congenitalhydrocephalusa pages 1-3) |
| phenotype | Hydrocephalus | HPO: HP:0000238 | Core phenotype; excess CSF with ventricular enlargement and potential elevated intracranial pressure (aragon2024geneticetiologiesand pages 1-2, zhang2024areviewof pages 1-2) |
| phenotype | Ventriculomegaly | HPO: HP:0002119 | Common imaging phenotype in fetal/neonatal diagnosis; often detected prenatally by ultrasound/MRI (aragon2024geneticetiologiesand pages 1-2, zhang2024areviewof pages 1-2) |
| phenotype | Macrocephaly | HPO: HP:0000256 | Common clinical manifestation in infant hydrocephalus; head circumference monitoring is standard clinical follow-up (NCT06310213 chunk 1) |
| phenotype | Bulging fontanelle | HPO: HP:0000239 | Practical bedside sign of raised intracranial pressure in infants; relevant to hydrocephalus monitoring (NCT06310213 chunk 1) |
| phenotype | Increased intracranial pressure | HPO: HP:0002516 | Downstream physiologic consequence of ventricular enlargement; a major treatment target and monitoring endpoint (zhang2024areviewof pages 1-2, NCT06693752 chunk 1, NCT06693752 chunk 2) |
| phenotype | Aqueductal stenosis | HPO: HP:0002625 | Major obstructive mechanism; especially associated with L1CAM-related/X-linked forms and non-syndromic CH (liu2024congenitalhydrocephalusa pages 3-5, deng2025geneticandmolecular pages 4-5) |
| phenotype | Developmental delay | HPO: HP:0001263 | Frequent long-term neurodevelopmental outcome in pediatric hydrocephalus cohorts (isaacs2018agespecificglobalepidemiology pages 9-13) |
| phenotype | Intellectual disability | HPO: HP:0001249 | Reported in monogenic forms including L1 syndrome; severity variable (newland2024understandingandmodeling pages 2-4, deng2025geneticandmolecular pages 4-5) |
| phenotype | Seizures | HPO: HP:0001250 | Important neurologic comorbidity/morbidity in pediatric hydrocephalus (isaacs2018agespecificglobalepidemiology pages 9-13) |
| phenotype | Spasticity / gait abnormality | HPO: HP:0001257; HP:0001288 | Motor impairment and gait difficulty are recognized morbidity features in affected children (isaacs2018agespecificglobalepidemiology pages 9-13) |
| phenotype | Corpus callosum abnormalities | HPO: HP:0001273 | Corpus callosum malformations are prominent in some genetic cases, particularly L1CAM-related disease (newland2024understandingandmodeling pages 2-4) |
| anatomy | Brain ventricular system | UBERON: brain ventricular system (verify exact ID in target ontology) | Primary anatomic compartment enlarged in disease (zhang2024areviewof pages 1-2) |
| anatomy | Lateral ventricle | UBERON: lateral ventricle (verify exact ID in target ontology) | Frequently measured on prenatal/postnatal imaging and targeted in shunt catheter placement (zhang2024areviewof pages 1-2, NCT06664372 chunk 1) |
| anatomy | Third ventricle | UBERON: third ventricle (verify exact ID in target ontology) | Relevant to obstructive hydrocephalus and ETV procedure (zhang2024areviewof pages 1-2, warf2023endoscopicthirdventriculostomy pages 1-2) |
| anatomy | Fourth ventricle | UBERON: fourth ventricle (verify exact ID in target ontology) | Included in ventricular system anatomy affected by CSF flow abnormalities (zhang2024areviewof pages 1-2) |
| anatomy | Cerebral aqueduct | UBERON: cerebral aqueduct (verify exact ID in target ontology) | Critical site for aqueductal stenosis/obstruction (liu2024congenitalhydrocephalusa pages 3-5, deng2025geneticandmolecular pages 4-5) |
| anatomy | Choroid plexus | UBERON: choroid plexus (verify exact ID in target ontology) | Major CSF-producing tissue; implicated in secretion, barrier, and surgical cauterization strategies (liu2024congenitalhydrocephalusa pages 1-3, NCT06693752 chunk 1, NCT06664372 chunk 1) |
| anatomy | Ependyma | UBERON: ependyma (verify exact ID in target ontology) | Ventricular lining central to ciliary motility and barrier/junction defects (zhang2024areviewof pages 1-2, liu2024congenitalhydrocephalusa pages 3-5) |
| anatomy | Cerebral cortex | UBERON: cerebral cortex (verify exact ID in target ontology) | Affected secondarily by compression and developmentally in some genetic forms (zhang2024areviewof pages 1-2, liu2024congenitalhydrocephalusa pages 6-8) |
| anatomy | Corpus callosum | UBERON: corpus callosum (verify exact ID in target ontology) | Malformation documented in monogenic disease presentations (newland2024understandingandmodeling pages 2-4) |
| cell type | Ependymal cell | CL: ependymal cell (verify exact ID in target ontology) | Key motile-cilia-bearing cell type regulating CSF movement; repeatedly implicated in CH (zhang2024areviewof pages 1-2, liu2024congenitalhydrocephalusa pages 3-5, liu2024congenitalhydrocephalusa pages 5-6) |
| cell type | Choroid plexus epithelial cell | CL: choroid plexus epithelial cell (verify exact ID in target ontology) | Core CSF-secretory/barrier cell; transporter dysregulation implicated mechanistically (zhang2024areviewof pages 1-2, deng2025geneticandmolecular pages 5-6, NCT06693752 chunk 1) |
| cell type | Neural stem/progenitor cell | CL: neural stem cell / neural progenitor cell (verify exact ID in target ontology) | Junctional and neurogenic defects in ventricular zone progenitors linked to aqueductal and cortical abnormalities (liu2024congenitalhydrocephalusa pages 6-8, liu2024congenitalhydrocephalusa pages 3-5) |
| cell type | Neuron | CL: neuron (verify exact ID in target ontology) | Downstream injury/developmental disruption contributes to cognitive and motor phenotypes (newland2024understandingandmodeling pages 2-4, liu2024congenitalhydrocephalusa pages 6-8) |
| cell type | Astrocyte | CL: astrocyte (verify exact ID in target ontology) | Glial activation reported in animal mechanistic cascades downstream of obstruction (deng2025geneticandmolecular pages 4-5) |
| cell type | Microglia | CL: microglial cell (verify exact ID in target ontology) | Inflammatory signaling is increasingly implicated in hydrocephalus pathobiology (deng2025geneticandmolecular pages 15-15) |
| mechanism | Cilium movement | GO:0003341 | Strongest recurring upstream mechanism; motile cilia defects impair CSF propulsion (liu2024congenitalhydrocephalusa pages 3-5, liu2024congenitalhydrocephalusa pages 5-6, liu2024congenitalhydrocephalusa pages 1-3) |
| mechanism | CSF circulation | GO: cerebrospinal fluid circulation (verify exact ID in target ontology) | Central disease process linking cilia, obstruction, and transporter dysfunction to ventricular dilation (zhang2024areviewof pages 1-2, liu2024congenitalhydrocephalusa pages 1-3) |
| mechanism | Ion transport | GO:0006811 | Choroid plexus ion transporters regulate CSF secretion; NKCC-related dysregulation highlighted in models (zhang2024areviewof pages 1-2, deng2025geneticandmolecular pages 5-6, liu2024congenitalhydrocephalusa pages 1-3) |
| mechanism | Cell-cell junction organization | GO:0045216 | Apical/junctional defects in ventricular zone and ependyma contribute to aqueductal stenosis and barrier dysfunction (liu2024congenitalhydrocephalusa pages 6-8, liu2024congenitalhydrocephalusa pages 3-5) |
| mechanism | Neurogenesis | GO:0022008 | Developmental pathway implicated through TRIM71, SMARCC1 and other neurodevelopmental genes (liu2024congenitalhydrocephalusa pages 6-8, liu2024congenitalhydrocephalusa pages 3-5) |
| mechanism | Inflammatory response | GO:0006954 | Neuroinflammatory signaling is a recognized contributor/modifier in hydrocephalus biology (deng2025geneticandmolecular pages 15-15) |
| mechanism | Apoptosis | GO:0006915 | Included among proposed molecular pathways contributing to tissue injury and ventricular pathology (liu2024congenitalhydrocephalusa pages 1-3) |
| gene / inheritance | L1CAM | HGNC: L1CAM; X-linked inheritance | Established CH gene; classic X-linked aqueductal stenosis/L1 syndrome; accounts for a notable fraction of congenital cases (liu2024congenitalhydrocephalusa pages 3-5, deng2025geneticandmolecular pages 4-5, OpenTargets Search: congenital hydrocephalus) |
| gene / inheritance | AP1S2 | HGNC: AP1S2; X-linked inheritance | Established X-linked CH-associated gene with vesicle trafficking role (liu2024congenitalhydrocephalusa pages 3-5, deng2025geneticandmolecular pages 4-5, liu2024congenitalhydrocephalusa pages 1-3) |
| gene / inheritance | MPDZ | HGNC: MPDZ; autosomal recessive inheritance | Established recessive CH gene; linked to planar polarity/junctional integrity and aqueduct/ependymal pathology (liu2024congenitalhydrocephalusa pages 3-5, deng2025geneticandmolecular pages 4-5, OpenTargets Search: congenital hydrocephalus) |
| gene / inheritance | CCDC88C | HGNC: CCDC88C; autosomal recessive inheritance | Established recessive CH gene; associated with cilia orientation/CSF flow abnormalities (liu2024congenitalhydrocephalusa pages 3-5, deng2025geneticandmolecular pages 4-5, OpenTargets Search: congenital hydrocephalus) |
| gene / inheritance | FOXJ1 | HGNC: FOXJ1; expanded evidence / candidate dominant mechanism | Strong mechanistic/candidate evidence for communicating hydrocephalus through impaired ependymal differentiation/ciliogenesis (liu2024congenitalhydrocephalusa pages 3-5, deng2025geneticandmolecular pages 15-15) |
| gene / inheritance | SMARCC1 | HGNC: SMARCC1; expanded evidence / autosomal dominant with incomplete penetrance reported | Increasing evidence linking chromatin remodeling and neural progenitor defects to CH (liu2024congenitalhydrocephalusa pages 15-16, liu2024congenitalhydrocephalusa pages 3-5, deng2025geneticandmolecular pages 15-15) |
| gene / inheritance | TRIM71 | HGNC: TRIM71; expanded evidence / candidate | Neurodevelopmental candidate implicated in communicating CH and neural progenitor biology (liu2024congenitalhydrocephalusa pages 3-5, OpenTargets Search: congenital hydrocephalus) |
| intervention | Ventriculoperitoneal shunt | NCIT-style: Ventriculoperitoneal Shunt Procedure (verify in NCIT) | Global standard surgical treatment; failure/revision remains common (aragon2024geneticetiologiesand pages 1-2, navaei2018controlledtrialto pages 1-2, NCT06664372 chunk 1) |
| intervention | Endoscopic third ventriculostomy | NCIT-style: Endoscopic Third Ventriculostomy (verify in NCIT) | Standard option for selected obstructive cases; can avoid shunt dependence in some infants (zhang2024areviewof pages 1-2, warf2023endoscopicthirdventriculostomy pages 1-2, navaei2018controlledtrialto pages 1-2) |
| intervention | Choroid plexus cauterization | NCIT-style: Choroid Plexus Cauterization (verify in NCIT) | Used with ETV in infant hydrocephalus; long-term shunt freedom reported in selected cohorts (warf2023endoscopicthirdventriculostomy pages 1-2, navaei2018controlledtrialto pages 1-2) |
| intervention | Physical therapy | NCIT-style: Physical Therapy (verify in NCIT) | Supportive rehabilitation for motor impairment/spasticity/gait dysfunction; ontology-ready supportive care term (isaacs2018agespecificglobalepidemiology pages 9-13) |
| intervention | Occupational therapy | NCIT-style: Occupational Therapy (verify in NCIT) | Supportive rehabilitation for developmental and functional deficits; commonly relevant in pediatric neurodisability (isaacs2018agespecificglobalepidemiology pages 9-13) |
| intervention | Speech therapy | NCIT-style: Speech Therapy (verify in NCIT) | Supportive rehabilitation for neurodevelopmental sequelae when language/communication are affected (isaacs2018agespecificglobalepidemiology pages 9-13) |


*Table: This compact ontology-ready table maps congenital hydrocephalus to suggested disease, phenotype, anatomy, cell type, mechanism, gene, and intervention terms. It is designed to support knowledge-base curation while flagging ontology IDs that should be verified in the target terminology.*

## 8. Temporal development

Onset is prenatal or neonatal. Ventriculomegaly may be detected at the second-trimester anatomy scan and characterized further by serial ultrasound and fetal MRI. Course ranges from stable mild isolated ventriculomegaly to rapidly progressive macrocephaly and neurological decompensation.

A practical chronology is: **prenatal ventricular enlargement → neonatal monitoring for head growth and pressure signs → temporizing CSF drainage when needed → definitive diversion → lifelong surveillance for developmental sequelae and treatment failure**. There is no formal stage system. “Compensated/arrested” hydrocephalus can remain clinically stable, but shunt-dependent disease is chronic and lifelong. Apparent remission usually reflects successful diversion or stable compensation, not elimination of the developmental cause.

Fetal and early postnatal brain development constitute the critical vulnerability window: prolonged pressure and white-matter distortion may cause irreversible injury, while overly early ETV/CPC is less successful because infant CSF absorption pathways are immature. In a 2023 cohort, corrected age below 2.5 months predicted reoperation or conversion to shunting. (warf2023endoscopicthirdventriculostomy pages 1-2)

## 9. Inheritance and population

### Epidemiology

A 78-study global meta-analysis found congenital-hydrocephalus incidences of **145/100,000 births in Africa**, **316/100,000 in Latin America**, and **68/100,000 in the United States/Canada**. Incidence was **123/100,000** (95% CI 98–152) in low-/middle-income countries versus **79/100,000** (95% CI 68–90) in high-income countries. Nearly **400,000 new pediatric hydrocephalus cases** were projected annually, with three quarters in Africa, Latin America and Southeast Asia. (dewan2019globalhydrocephalusepidemiology pages 1-2)

A separate 52-study meta-analysis covering 171,558,651 people estimated pediatric prevalence at **88/100,000** (95% CI 72–107) and birth-diagnosed incidence at **81/100,000** (95% CI 69–96). Isolated congenital hydrocephalus incidence was estimated at **49.5/100,000**, rising to **81.2/100,000** when spina-bifida-associated cases were included. (isaacs2018agespecificglobalepidemiology pages 9-13, isaacs2018agespecificglobalepidemiology pages 1-2)

These estimates are more reliable than the broader “approximately 1 in 500 births” figure quoted in a 2024 molecular review, because definitions, ascertainment and inclusion of acquired pediatric disease vary. (liu2024congenitalhydrocephalusa pages 1-3)

### Population genetics

Inheritance may be X-linked, autosomal recessive, autosomal dominant/de novo, mosaic, chromosomal, or multifactorial. Male excess is expected in L1CAM/AP1S2 disease and was present in one infant trial (66% male), but there is no universal sex ratio for all CH. (navaei2018controlledtrialto pages 1-2)

No robust evidence supports anticipation. Penetrance and expressivity are variant-specific; SMARCC1 can show incomplete penetrance, whereas severe biallelic loss-of-function disorders are often highly penetrant. Founder effects and carrier frequencies exist for individual variants/populations but cannot be generalized. Consanguinity increases homozygous recessive disease and should prompt trio exome/genome analysis plus homozygosity-aware interpretation.

## 10. Diagnostics

### Clinical and imaging diagnosis

Prenatal ultrasound is first-line: atrial width, ventricular progression, head size, neural-tube defect, posterior fossa and other anomalies are assessed. Fetal MRI better defines aqueduct, corpus callosum, cortical development, hemorrhage and associated malformations. After birth, serial head circumference, fontanelle tension, eye findings, feeding, alertness and neurodevelopment are integrated with transfontanelle ultrasound; MRI is preferred for anatomy and CSF-flow assessment, while CT is reserved for urgent situations where speed outweighs ionizing-radiation risk. (zhang2024areviewof pages 1-2, NCT06310213 chunk 1)

There is no diagnostic blood, urine, enzyme or CSF biomarker specific for CH. ICP measurement, shunt tap/EVD data, ophthalmic examination and CSF studies are used selectively. EEG is indicated for suspected seizures, not routine diagnosis. Biopsy is not generally appropriate.

### Genetic testing strategy

1. Detailed prenatal/postnatal phenotype and three-generation pedigree.
2. **Chromosomal microarray** after structural anomalies/ventriculomegaly; karyotype when aneuploidy or balanced rearrangement is suspected.
3. **Targeted testing** for a recognizable subtype—for example L1CAM sequencing plus deletion/duplication analysis in an affected male with aqueductal stenosis/adducted thumbs.
4. A hydrocephalus/brain-malformation panel or preferably **trio WES/WGS** when CMA is nondiagnostic. WGS offers more complete structural, intronic, repeat and mosaic-variant detection; WES remains widely available and useful.
5. Reanalysis as gene–disease knowledge evolves; parental segregation and recurrence-risk counseling.

A small fetal-CNS-anomaly series reported prenatal exome diagnostic yield of **53% (10/19)** and clinical impact in **63%**, illustrating utility but not a CH-specific expected yield. A 2024 scoping review emphasized causes from secondary insults to germline pathogenic variants and the need to combine molecular testing with phenotype. (aragon2024geneticetiologiesand pages 1-2)

RNA sequencing may resolve splice variants, but appropriate fetal/brain tissue is rarely available. Proteomics, metabolomics, methylation testing, liquid biopsy, mitochondrial testing and repeat-expansion assays are not routine unless another syndrome is suspected.

### Differential diagnosis and screening

Differentiate active hydrocephalus from ex-vacuo ventriculomegaly due to tissue loss, benign enlargement of subarachnoid spaces, isolated stable mild ventriculomegaly, hydranencephaly, porencephaly, intracranial cysts, megalencephaly, and acquired posthemorrhagic/postinfectious hydrocephalus. No universal newborn biochemical screen exists. Prenatal ultrasound is the principal population screen; carrier, cascade, prenatal and preimplantation testing are appropriate after identification of a familial pathogenic variant.

## 11. Outcome and prognosis

Outcome depends more on etiology, associated brain malformations/injury, infection, prematurity, treatment timing and complications than on ventricular size alone. Untreated-hydrocephalus mortality has been reported across a very wide **20–87%** range, reflecting heterogeneous settings and historical cohorts; this should not be used as an individualized estimate. (isaacs2018agespecificglobalepidemiology pages 9-13)

Long-term morbidity includes intellectual/developmental disability, epilepsy, cerebral palsy/spasticity, visual impairment, endocrine dysfunction, chronic headache and repeated operations. A trial registry summarizes long-term disability in up to **78%**, but this is background rather than a peer-reviewed subtype-specific estimate. (NCT06693752 chunk 1)

Major complications are shunt obstruction, infection, disconnection, migration, overdrainage/subdural collection and underdrainage; ETV can close, especially early after treatment. Prognostic indicators include severe associated malformation, infection, prematurity/hemorrhage, very young age at ETV/CPC, prior CSF diversion, severe preoperative ventriculomegaly and intraoperative bleeding. In the 2023 infant cohort, FOHR >0.613 predicted conversion after ETV/CPC. (warf2023endoscopicthirdventriculostomy pages 1-2)

There is no validated molecular prognostic biomarker applicable across CH. Genotype improves counseling—for example severe L1CAM loss-of-function disease generally carries greater neurodevelopmental risk—but within-gene variability remains substantial.

## 12. Treatment

### Standard surgical treatment

- **Ventriculoperitoneal shunt (VPS):** most widely used treatment; diverts ventricular CSF to the peritoneum. Suggested NCIT term: Ventriculoperitoneal Shunt Procedure. It is effective but creates lifelong device dependence and revision risk. A current congenital trial cites revision in **30–40%** of cases. (NCT06664372 chunk 1)
- **ETV:** fenestrates the third-ventricular floor to bypass obstruction; most appropriate for selected obstructive anatomy.
- **ETV/CPC:** adds cauterization to reduce CSF production and can avoid a permanent shunt in selected infants. In 348 infants, estimated long-term shunt freedom was **59% through 11 years**; approximately 80% of children treated at ≥2.5 months avoided a shunt, whereas only 26.9% of those <2.5 months with prior diversion remained shunt-free. (warf2023endoscopicthirdventriculostomy pages 1-2)
- In a randomized trial of 49 infants with obstructive hydrocephalus, 36-month success was **88.5% for VPS** and **68.2% for ETV/CPC**, without a statistically significant difference. (navaei2018controlledtrialto pages 1-2)
- **Temporary measures:** ventricular reservoir taps, ventriculosubgaleal shunt, external ventricular drainage or serial lumbar puncture in selected premature/posthemorrhagic infants.

Antibiotic-impregnated catheters and standardized infection-prevention bundles reduce shunt infection in pediatric practice. Acute shunt malfunction or infection is a neurosurgical emergency.

### Pharmacological, advanced and supportive therapy

No drug reliably eliminates hydrocephalus or replaces diversion. Acetazolamide, furosemide and osmotic agents are not definitive chronic therapy and can cause electrolyte, renal and systemic toxicity. Antiseizure medication, analgesia and antibiotics treat complications rather than CH itself. No established CH pharmacogenomic guideline exists.

Preclinical targets include NKCC1, TRPV4, SGK1, inflammatory pathways, aquaporins and PI3K–AKT–mTOR signaling, but none is approved as disease-modifying CH therapy. Gene replacement, CRISPR, ASO, siRNA, stem-cell and immunotherapy approaches remain experimental/preclinical.

Physical, occupational, speech/feeding, vision and educational therapies should begin early and be individualized. Management commonly requires neurosurgery, neurology, developmental pediatrics, rehabilitation, ophthalmology, genetics and social support.

### Emerging applications and trials

- **NCT06310213**, first posted 15 March 2024: modified smart soft contact lens for non-invasive ICP monitoring; enrolling by invitation, 25 infants, with comparison against clinical assessment, EVD readings and pre/post-shunt measurements. It is an unapproved investigational device. (NCT06310213 chunk 1)
- **NCT06664372**, first posted 29 October 2024: transfontanelle ultrasound-guided frontal VPS catheter placement in 30 children, intended to reduce proximal obstruction; listed as not yet recruiting in the retrieved record. (NCT06664372 chunk 1)
- **NCT06693752**, first posted 18 November 2024: Phase 2 pilot of Lumason contrast-enhanced brain ultrasound, 20 infants, assessing safety, perfusion and correlation with ICP/ischemia; the retrieved record lists recruitment beginning in 2026. (NCT06693752 chunk 1, NCT06693752 chunk 2)

These trials improve diagnosis or surgical precision; none tests a curative molecular therapy.

## 13. Prevention

**Primary prevention:** periconceptional folic acid and food fortification for neural-tube-defect prevention; rubella and other recommended maternal vaccination before pregnancy; avoidance of teratogens; infection prevention and prompt maternal treatment; optimized diabetes and nutritional care; and prevention of prematurity where possible. These measures prevent only attributable subsets, not most monogenic CH.

**Secondary prevention:** prenatal ultrasound/MRI, diagnostic CMA/WES/WGS, serial monitoring of fetal ventricles and infant head growth, and rapid referral to fetal medicine, genetics and pediatric neurosurgery. Fetal closure of myelomeningocele can reduce subsequent hindbrain herniation and shunt requirement in appropriately selected pregnancies, but fetal ventricular shunting for isolated hydrocephalus remains investigational/high risk.

**Tertiary prevention:** reliable follow-up, caregiver education about malfunction/infection, infection-prevention bundles, accurate catheter placement, developmental surveillance, seizure/vision management, and early rehabilitation.

For a known pathogenic variant, genetic counseling should address inheritance, penetrance, germline mosaicism, carrier/cascade testing, chorionic-villus or amniotic-fluid diagnosis, and PGT-M. Population-wide carrier screening is not currently justified because of extreme locus heterogeneity.

## 14. Other species and natural disease

Naturally occurring internal hydrocephalus occurs in mammals and birds. In dogs (**Canis lupus familiaris**, NCBI Taxon 9615), it is a common brain malformation, especially in toy and brachycephalic breeds such as Chihuahua; restricted cranial capacity and craniovertebral/Chiari-like abnormalities can impair CSF flow. VPS is used clinically in selected dogs. In cats (**Felis catus**, Taxon 9685), congenital hydrocephalus is uncommon, with a suspected recessive form in Siamese cats. Ruminant congenital hydrocephalus is often caused by teratogenic viruses; avian and large-felid acquired disease can accompany vitamin-A deficiency. These conditions are non-zoonotic. (schmidt2019hydrocephalusinanimals pages 2-4)

A naturally occurring autosomal-recessive syndrome in mixed-breed Oriental cats is caused by homozygous **GDF7 c.221_227delGCCGCGC (p.Arg74Profs)**. It produces ventriculomegaly, interhemispheric cysts, commissural malformation, hippocampal hypoplasia and mild ataxia. The variant segregated in 43 genotyped cats and was absent from 192 unaffected cats, supporting breeder testing and comparative developmental biology. (yu2020adeletionin pages 1-3)

Veterinary disease is valuable because it occurs in a naturally sized, genetically diverse brain, but heterogeneous husbandry, limited pathology, cost-dependent ascertainment and species-specific skull anatomy constrain translation.

## 15. Model organisms

- **Mouse (Mus musculus; Taxon 10090):** L1cam, Foxj1, Smarcc1, Ccdc39, Ccdc88c, Mpdz, Napa/hyh, Hydin/hy3, Rnd3, Msx1 and other knockout/knock-in models reproduce ventriculomegaly, aqueductal obstruction, ciliary defects, ependymal denudation or neurodevelopmental abnormalities. The hyh Napa model is recessive and highly penetrant; aqueduct obstruction is evident by postnatal day 1 with later myelin degeneration and glial activation. (deng2025geneticandmolecular pages 4-5, newland2024understandingandmodeling pages 7-8)
- **Rat (Rattus norvegicus; Taxon 10116):** H-Tx models aqueductal stenosis; Wpk/Tmem67−/− models communicating hydrocephalus plus polycystic kidneys and dies at 18–21 days; LEW/Jms shows neonatal, male-biased inherited hydrocephalus. Rat size facilitates shunts, imaging, ICP monitoring and pharmacology. (newland2024understandingandmodeling pages 7-8)
- **Zebrafish (Danio rerio; Taxon 7955):** transparent embryos and rapid CRISPR/morpholino studies permit live analysis and chemical screening. Models involving wdr16, nphp7, l1camb, ccdc88c, Reissner-fiber genes and ion transport reproduce ventricular dilation or ciliary-flow abnormalities. Limitations include substantial differences in ventricular anatomy, CSF physiology and duplicated genes. (liu2024congenitalhydrocephalusa pages 6-8, deng2025geneticandmolecular pages 5-6, liu2024congenitalhydrocephalusa pages 5-6)
- **Induced models:** kaolin creates inflammatory obstructive hydrocephalus; intraventricular blood models posthemorrhagic disease; 6-aminonicotinamide produces Dandy–Walker-like cerebellar hypoplasia and ventriculomegaly within 72 hours. These are useful for downstream pressure/inflammation and device studies but do not model a congenital human genotype. (newland2024understandingandmodeling pages 5-7)
- **Cellular systems:** primary choroid-plexus epithelial cultures, ependymal differentiation cultures, organoids and iPSC-derived neuroepithelia support transporter, barrier, ciliary and variant-functional studies. They lack whole-brain pressure, absorption and biomechanical interactions.

A recurrent expert conclusion is that no single model captures CH’s genetic, developmental, biomechanical and inflammatory dimensions; replication across human genetics, cell systems and at least two vertebrate models is preferable before therapeutic translation. (liu2024congenitalhydrocephalusa pages 5-6, newland2024understandingandmodeling pages 16-17)

## Evidence interpretation and knowledge gaps

The strongest evidence comprises global epidemiological meta-analyses, human gene–disease associations, molecularly diagnosed families and infant surgical cohorts. Mechanistic detail is disproportionately model-derived. Current priorities are large ancestry-diverse trio-WGS cohorts, standardized prenatal/postnatal phenotyping, long-read and mosaic-variant detection, human single-cell/spatial atlases of ventricular interfaces, validated pressure/perfusion biomarkers, and trials that measure neurodevelopment rather than ventricular size alone.

Important negative findings for database curation are: no universal biochemical biomarker; no established protective allele; no approved pharmacologic, gene, RNA or cell therapy; no single penetrance, carrier-frequency or sex-ratio estimate; no disease-wide molecular prognosis; and no evidence that folate prevents isolated monogenic hydrocephalus. The 2024 literature’s most important conceptual advance is the shift from treating CH solely as “plumbing failure” toward a developmental disorder involving neural progenitors, ependyma, cilia, choroid plexus and brain–CSF interfaces. (aragon2024geneticetiologiesand pages 1-2, liu2024congenitalhydrocephalusa pages 3-5, liu2024congenitalhydrocephalusa pages 1-3)

References

1. (aragon2024geneticetiologiesand pages 1-2): Caroline Aragón, D'aviyan Robinson, Megan Kocher, Katie Barrick, Lihsia Chen, and Heather Zierhut. Genetic etiologies and diagnostic methods for congenital ventriculomegaly and hydrocephalus: a scoping review. Birth Defects Research, Dec 2024. URL: https://doi.org/10.1002/bdr2.2287, doi:10.1002/bdr2.2287. This article has 4 citations and is from a peer-reviewed journal.

2. (OpenTargets Search: congenital hydrocephalus): Open Targets Query (congenital hydrocephalus, 16 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (liu2024congenitalhydrocephalusa pages 3-5): Xiu-Yun Liu, Xin Song, Marek Czosnyka, Chiara Robba, Zofia Czosnyka, Jennifer Lee Summers, Hui-Jie Yu, Guo-Yi Gao, Peter Smielewski, Fang Guo, Mei-Jun Pang, and Dong Ming. Congenital hydrocephalus: a review of recent advances in genetic etiology and molecular mechanisms. Military Medical Research, Aug 2024. URL: https://doi.org/10.1186/s40779-024-00560-5, doi:10.1186/s40779-024-00560-5. This article has 19 citations and is from a peer-reviewed journal.

4. (liu2024congenitalhydrocephalusa pages 1-3): Xiu-Yun Liu, Xin Song, Marek Czosnyka, Chiara Robba, Zofia Czosnyka, Jennifer Lee Summers, Hui-Jie Yu, Guo-Yi Gao, Peter Smielewski, Fang Guo, Mei-Jun Pang, and Dong Ming. Congenital hydrocephalus: a review of recent advances in genetic etiology and molecular mechanisms. Military Medical Research, Aug 2024. URL: https://doi.org/10.1186/s40779-024-00560-5, doi:10.1186/s40779-024-00560-5. This article has 19 citations and is from a peer-reviewed journal.

5. (warf2023endoscopicthirdventriculostomy pages 1-2): Benjamin C. Warf, Daniel S. Weber, Emily L. Day, Coleman P. Riordan, Steven J. Staffa, Lissa C. Baird, Katie P. Fehnel, and Scellig S. D. Stone. Endoscopic third ventriculostomy with choroid plexus cauterization: predictors of long-term success and comparison with shunt placement for primary treatment of infant hydrocephalus. Journal of Neurosurgery: Pediatrics, 32:201-213, Aug 2023. URL: https://doi.org/10.3171/2023.4.peds2310, doi:10.3171/2023.4.peds2310. This article has 37 citations and is from a peer-reviewed journal.

6. (zhang2024areviewof pages 1-2): Mingzhao Zhang, Xiangjun Hu, and Lifeng Wang. A review of cerebrospinal fluid circulation and the pathogenesis of congenital hydrocephalus. Neurochemical Research, 49:1123-1136, Feb 2024. URL: https://doi.org/10.1007/s11064-024-04113-z, doi:10.1007/s11064-024-04113-z. This article has 23 citations and is from a peer-reviewed journal.

7. (isaacs2018agespecificglobalepidemiology pages 2-4): Albert M. Isaacs, Jay Riva-Cambrin, Daniel Yavin, Aaron Hockley, Tamara M. Pringsheim, Nathalie Jette, Brendan Cord Lethebe, Mark Lowerison, Jarred Dronyk, and Mark G. Hamilton. Age-specific global epidemiology of hydrocephalus: systematic review, metanalysis and global birth surveillance. PLoS ONE, 13:e0204926, Oct 2018. URL: https://doi.org/10.1371/journal.pone.0204926, doi:10.1371/journal.pone.0204926. This article has 339 citations and is from a peer-reviewed journal.

8. (NCT06664372 chunk 1): Omar Salah Mohamed Omran. Insertion of Frontal Ventricular Catheter of VP Shunt in Congenital Hydrocephalus Guided by Trans Fontanelle Ultrasound. Assiut University. 2024. ClinicalTrials.gov Identifier: NCT06664372

9. (deng2025geneticandmolecular pages 15-15): Xuehai Deng, Yiqian Chen, Qiyue Duan, Jianlin Ding, Zhong Wang, Junchi Wang, Xinlong Chen, Liangxue Zhou, and Long Zhao. Genetic and molecular mechanisms of hydrocephalus. Frontiers in Molecular Neuroscience, Jan 2025. URL: https://doi.org/10.3389/fnmol.2024.1512455, doi:10.3389/fnmol.2024.1512455. This article has 7 citations.

10. (deng2025geneticandmolecular pages 4-5): Xuehai Deng, Yiqian Chen, Qiyue Duan, Jianlin Ding, Zhong Wang, Junchi Wang, Xinlong Chen, Liangxue Zhou, and Long Zhao. Genetic and molecular mechanisms of hydrocephalus. Frontiers in Molecular Neuroscience, Jan 2025. URL: https://doi.org/10.3389/fnmol.2024.1512455, doi:10.3389/fnmol.2024.1512455. This article has 7 citations.

11. (newland2024understandingandmodeling pages 2-4): Verayna Newland, Lauren L. Jantzie, and Bonnie L. Blazer-Yost. Understanding and modeling the pathophysiology of hydrocephalus: in search of better treatment options. Physiologia, 4:182-201, Apr 2024. URL: https://doi.org/10.3390/physiologia4020010, doi:10.3390/physiologia4020010. This article has 10 citations.

12. (dewan2019globalhydrocephalusepidemiology pages 1-2): Michael C. Dewan, Abbas Rattani, Rania Mekary, Laurence J. Glancz, Ismaeel Yunusa, Ronnie E. Baticulon, Graham Fieggen, John C. Wellons, Kee B. Park, and Benjamin C. Warf. Global hydrocephalus epidemiology and incidence: systematic review and meta-analysis. Journal of neurosurgery, 130:1-15, Apr 2019. URL: https://doi.org/10.3171/2017.10.jns17439, doi:10.3171/2017.10.jns17439. This article has 542 citations and is from a domain leading peer-reviewed journal.

13. (deng2025geneticandmolecular pages 5-6): Xuehai Deng, Yiqian Chen, Qiyue Duan, Jianlin Ding, Zhong Wang, Junchi Wang, Xinlong Chen, Liangxue Zhou, and Long Zhao. Genetic and molecular mechanisms of hydrocephalus. Frontiers in Molecular Neuroscience, Jan 2025. URL: https://doi.org/10.3389/fnmol.2024.1512455, doi:10.3389/fnmol.2024.1512455. This article has 7 citations.

14. (isaacs2018agespecificglobalepidemiology pages 1-2): Albert M. Isaacs, Jay Riva-Cambrin, Daniel Yavin, Aaron Hockley, Tamara M. Pringsheim, Nathalie Jette, Brendan Cord Lethebe, Mark Lowerison, Jarred Dronyk, and Mark G. Hamilton. Age-specific global epidemiology of hydrocephalus: systematic review, metanalysis and global birth surveillance. PLoS ONE, 13:e0204926, Oct 2018. URL: https://doi.org/10.1371/journal.pone.0204926, doi:10.1371/journal.pone.0204926. This article has 339 citations and is from a peer-reviewed journal.

15. (isaacs2018agespecificglobalepidemiology pages 9-13): Albert M. Isaacs, Jay Riva-Cambrin, Daniel Yavin, Aaron Hockley, Tamara M. Pringsheim, Nathalie Jette, Brendan Cord Lethebe, Mark Lowerison, Jarred Dronyk, and Mark G. Hamilton. Age-specific global epidemiology of hydrocephalus: systematic review, metanalysis and global birth surveillance. PLoS ONE, 13:e0204926, Oct 2018. URL: https://doi.org/10.1371/journal.pone.0204926, doi:10.1371/journal.pone.0204926. This article has 339 citations and is from a peer-reviewed journal.

16. (liu2024congenitalhydrocephalusa pages 15-16): Xiu-Yun Liu, Xin Song, Marek Czosnyka, Chiara Robba, Zofia Czosnyka, Jennifer Lee Summers, Hui-Jie Yu, Guo-Yi Gao, Peter Smielewski, Fang Guo, Mei-Jun Pang, and Dong Ming. Congenital hydrocephalus: a review of recent advances in genetic etiology and molecular mechanisms. Military Medical Research, Aug 2024. URL: https://doi.org/10.1186/s40779-024-00560-5, doi:10.1186/s40779-024-00560-5. This article has 19 citations and is from a peer-reviewed journal.

17. (liu2024congenitalhydrocephalusa pages 5-6): Xiu-Yun Liu, Xin Song, Marek Czosnyka, Chiara Robba, Zofia Czosnyka, Jennifer Lee Summers, Hui-Jie Yu, Guo-Yi Gao, Peter Smielewski, Fang Guo, Mei-Jun Pang, and Dong Ming. Congenital hydrocephalus: a review of recent advances in genetic etiology and molecular mechanisms. Military Medical Research, Aug 2024. URL: https://doi.org/10.1186/s40779-024-00560-5, doi:10.1186/s40779-024-00560-5. This article has 19 citations and is from a peer-reviewed journal.

18. (liu2024congenitalhydrocephalusa pages 6-8): Xiu-Yun Liu, Xin Song, Marek Czosnyka, Chiara Robba, Zofia Czosnyka, Jennifer Lee Summers, Hui-Jie Yu, Guo-Yi Gao, Peter Smielewski, Fang Guo, Mei-Jun Pang, and Dong Ming. Congenital hydrocephalus: a review of recent advances in genetic etiology and molecular mechanisms. Military Medical Research, Aug 2024. URL: https://doi.org/10.1186/s40779-024-00560-5, doi:10.1186/s40779-024-00560-5. This article has 19 citations and is from a peer-reviewed journal.

19. (NCT06693752 chunk 1): Misun Hwang, MD. CEUS Evaluation of Hydrocephalus in Neonates and Infants. Children's Hospital of Philadelphia. 2026. ClinicalTrials.gov Identifier: NCT06693752

20. (NCT06310213 chunk 1): Jignesh Tailor. Non-Invasive Pressure Monitor for Neonates & Infants at Risk of Developing Hydrocephalus. Indiana University. 2025. ClinicalTrials.gov Identifier: NCT06310213

21. (NCT06693752 chunk 2): Misun Hwang, MD. CEUS Evaluation of Hydrocephalus in Neonates and Infants. Children's Hospital of Philadelphia. 2026. ClinicalTrials.gov Identifier: NCT06693752

22. (navaei2018controlledtrialto pages 1-2): Amir Navaei, Sara Hanaei, Zohreh Habibi, Morteza Jouibari, Vahid Heidari, Soheil Naderi, and Farideh Nejat. Controlled trial to compare therapeutic efficacy of endoscopic third ventriculostomy plus choroid plexus cauterization with ventriculoperitoneal shunt in infants with obstructive hydrocephalus. Asian Journal of Neurosurgery, 13:1042-1047, Dec 2018. URL: https://doi.org/10.4103/ajns.ajns\_63\_17, doi:10.4103/ajns.ajns\_63\_17. This article has 20 citations.

23. (schmidt2019hydrocephalusinanimals pages 2-4): Martin Schmidt and Nele Ondreka. Hydrocephalus in animals. Pediatric Hydrocephalus, pages 53-95, Jan 2019. URL: https://doi.org/10.1007/978-3-319-27250-4\_36, doi:10.1007/978-3-319-27250-4\_36. This article has 59 citations.

24. (yu2020adeletionin pages 1-3): Yoshihiko Yu, Erica K. Creighton, Reuben M. Buckley, and Leslie A. Lyons. A deletion in gdf7 is associated with a heritable forebrain commissural malformation concurrent with ventriculomegaly and interhemispheric cysts in cats. Genes, 11:672, Jun 2020. URL: https://doi.org/10.3390/genes11060672, doi:10.3390/genes11060672. This article has 8 citations.

25. (newland2024understandingandmodeling pages 7-8): Verayna Newland, Lauren L. Jantzie, and Bonnie L. Blazer-Yost. Understanding and modeling the pathophysiology of hydrocephalus: in search of better treatment options. Physiologia, 4:182-201, Apr 2024. URL: https://doi.org/10.3390/physiologia4020010, doi:10.3390/physiologia4020010. This article has 10 citations.

26. (newland2024understandingandmodeling pages 5-7): Verayna Newland, Lauren L. Jantzie, and Bonnie L. Blazer-Yost. Understanding and modeling the pathophysiology of hydrocephalus: in search of better treatment options. Physiologia, 4:182-201, Apr 2024. URL: https://doi.org/10.3390/physiologia4020010, doi:10.3390/physiologia4020010. This article has 10 citations.

27. (newland2024understandingandmodeling pages 16-17): Verayna Newland, Lauren L. Jantzie, and Bonnie L. Blazer-Yost. Understanding and modeling the pathophysiology of hydrocephalus: in search of better treatment options. Physiologia, 4:182-201, Apr 2024. URL: https://doi.org/10.3390/physiologia4020010, doi:10.3390/physiologia4020010. This article has 10 citations.

## Artifacts

- [Edison artifact artifact-00](Congenital_Hydrocephalus-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.