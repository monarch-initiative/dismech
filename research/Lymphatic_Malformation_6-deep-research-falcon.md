---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-18T09:21:46.449097'
end_time: '2026-08-18T09:32:14.266439'
duration_seconds: 627.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lymphatic malformation 6
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 8
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Lymphatic_Malformation_6-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lymphatic malformation 6
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lymphatic malformation 6** covering all of the
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
- **Disease Name:** Lymphatic malformation 6
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lymphatic malformation 6** covering all of the
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


# Lymphatic Malformation 6: Comprehensive Disease-Characteristics Report

## Executive summary

**Lymphatic malformation 6 (LM6)** is a rare Mendelian disorder of lymphatic development caused principally by **biallelic loss-of-function variants in PIEZO1**, which encodes a mechanically activated, calcium-permeable cation channel. It is best understood clinically as **PIEZO1-related generalized lymphatic dysplasia (GLD)**. The characteristic spectrum comprises prenatal nonimmune hydrops fetalis, pleural or pericardial effusions, chylothorax, ascites, pulmonary or intestinal lymphangiectasia, and congenital or later-onset generalized lymphedema. Disease severity is highly variable, ranging from fetal death to transient prenatal edema followed by childhood- or adult-onset lymphatic disease. Founding human studies were published independently in September 2015 by Fotiou et al. and Lukacs et al. (PMIDs indexed for the disease association include **26333996** and **26387913**). (OpenTargets Search: lymphatic malformation 6, iyer2020lymphaticvalvesand pages 15-17, fotiou2015novelmutationsin pages 1-2)

The strongest recent mechanistic advance is the 2024 demonstration that PIEZO1 activation in lymphatic endothelial cells induces **ANGPT2 exocytosis, ADAM17-mediated TIE1 shedding, TIE/PI3K/AKT activation, and FOXO1 nuclear export**. This complements earlier evidence that PIEZO1 controls lymphatic-valve morphogenesis, lymphatic sprouting, and vessel maintenance. No approved PIEZO1-directed treatment exists; small-molecule PIEZO1 agonism with Yoda1 remains preclinical. (du2024themechanosensorychannel pages 1-2, choi2022piezo1regulatedmechanotransductioncontrols pages 1-3, ludlow2023smallmoleculefunctionalrescue pages 14-16)

The following table summarizes the principal evidence and ontology-ready annotations.

| Domain | Key finding | Evidence type | Quantitative detail | Source / date / DOI / PMID | Knowledge-base ontology suggestions |
|---|---|---|---|---|---|
| Disease identity / gene | Lymphatic malformation 6 is linked to **PIEZO1**; disease-target association databases map LM6 to **MONDO:0014797** and PIEZO1 as the only strong associated target | Curated disease-resource + human genetics | OpenTargets evidence size: **5** literature-backed links for PIEZO1–LM6 association | OpenTargets disease-target association for “lymphatic malformation 6” (MONDO_0014797) (OpenTargets Search: lymphatic malformation 6) | MONDO:0014797; HGNC:13866 **PIEZO1**; NCIT: C129043 *Lymphatic Malformation* |
| Founding human cohort | **Autosomal recessive generalized lymphatic dysplasia (GLD)** due to homozygous/compound-heterozygous PIEZO1 variants; frequent **non-immune hydrops fetalis (NIHF)** and childhood facial/four-limb lymphedema | Human clinical / human genetics | **6 families**, **10 PIEZO1 variants** reported; high incidence of NIHF; onset of facial and four-limb lymphedema in childhood | Fotiou et al., **2015-09**, *Nature Communications*, DOI: https://doi.org/10.1038/ncomms9085 (PMID not available in context) (fotiou2015novelmutationsin pages 1-2) | HP:0001789 Lymphedema; HP:0001561 Hydrops fetalis; HP:0000978 Facial edema; HP:0002202 Pleural effusion; HP:0001744 Ascites; HP:0001733 Lymphangiectasia |
| Founding human cohort details | GLD phenotype includes widespread edema with systemic lymphatic involvement: intestinal/pulmonary lymphangiectasia, pleural/chylous/pericardial effusions; some prenatal demise, some postnatal hydrops resolution followed by later lymphedema | Human clinical | **5 patients across 4 families** highlighted; hydrops in at least **2 families**; one in utero demise at **34 weeks**; postnatal lymphedema onset reported around **6–9 years** in survivors | Fotiou et al., **2015-09**, DOI: https://doi.org/10.1038/ncomms9085 (fotiou2015novelmutationsin pages 2-3) | HP:0003573 Congenital onset; HP:0001789 Lymphedema; HP:0010318 Chylothorax; HP:0001698 Pericardial effusion; UBERON:0005409 lymphatic vessel |
| Variant classes / function | Disease-associated PIEZO1 variants include **nonsense, splice-site, and missense** alleles with segregation in affected families; evidence supports **loss of protein** and/or **loss of function** | Human genetics + in vitro / ex vivo functional | Examples in context include nonsense variants **p.E1630X, p.E755X, p.Q2228X** and splice variant **c.3796+1G>A**; reduced/absent protein on Western blot; subtle RBC abnormalities noted | Fotiou et al., **2015-09**, DOI: https://doi.org/10.1038/ncomms9085 (fotiou2015novelmutationsin pages 1-2, fotiou2015novelmutationsin pages 2-3) | SO:0001587 nonsense_variant; SO:0001629 splice_donor_variant; GO:0006816 calcium ion transport; GO:0008308 voltage-gated ion channel activity |
| Independent founding family | Biallelic PIEZO1 mutations identified in **2 siblings** with persistent congenital lymphedema; affected alleles showed markedly reduced channel activity | Human clinical + human genetics + heterologous functional assay | **2 affected siblings**; one splice/truncating allele plus one missense allele; channel function “greatly attenuated” | Lukacs et al., **2015-09**, *Nature Communications*, DOI: https://doi.org/10.1038/ncomms9329 (PMID not available in context) (iyer2020lymphaticvalvesand pages 15-17) | HP:0001789 Lymphedema; HP:0003577 Congenital onset; MONDO:0014797; GO:0005262 calcium channel activity |
| Recent human variant interpretation | Four novel GLD-associated missense variants can reach the cell surface as full-length protein but still show **reduced or abolished mechanical channel function**, supporting pathogenic LOF mechanisms beyond absent trafficking | Human genetics + in vitro | Variants in context: **E829V, G1978D, I2270T, R2335Q**; all rare/ultra-rare, with no homozygotes in gnomAD noted in context | Ludlow et al., **2023-08**, *medRxiv* preprint, DOI: https://doi.org/10.1101/2023.08.01.23292554 (ludlow2023smallmoleculefunctionalrescue pages 41-45, ludlow2023smallmoleculefunctionalrescue pages 5-8) | SO:0001583 missense_variant; GO:0005516 mechanosensitive ion channel activity; ECO:0001565 cell-based functional assay evidence |
| Recent families / phenotype expansion | Additional PIEZO1-GLD families show antenatal NIHF, polyhydramnios, congenital limb edema, chylothoraces and ascites; one family showed **adult-onset bilateral chylothoraces in the 30s** before later lymphedema | Human clinical | **3 families** in context (GLD07-09); GLD09 hydrothoraces detected at **19 weeks gestation**; pseudo-dominant appearance in one consanguineous family due to homozygous **I2270T** | Ludlow et al., **2023-08**, DOI: https://doi.org/10.1101/2023.08.01.23292554 (ludlow2023smallmoleculefunctionalrescue pages 8-10, ludlow2023smallmoleculefunctionalrescue pages 14-16) | HP:0001561 Hydrops fetalis; HP:0002023 Polyhydramnios; HP:0002202 Pleural effusion; HP:0010318 Chylothorax; HP:0001744 Ascites; HP:0001789 Lymphedema |
| Preclinical rescue | **Yoda1** and analogues rescued function of some GLD-associated PIEZO1 missense channels in vitro; this is **preclinical**, not an approved genotype-specific therapy | In vitro / preclinical | Missense variants showed **~65–90% reduction** in Ca2+ signaling vs WT in context; Yoda1 restored mechanically evoked responses in rescue assays | Ludlow et al., **2023-08**, DOI: https://doi.org/10.1101/2023.08.01.23292554 (preprint) (ludlow2023smallmoleculefunctionalrescue pages 8-10, ludlow2023smallmoleculefunctionalrescue pages 14-16) | CHEBI: not established here for Yoda1; NCIT suggestion: *Experimental Therapeutic Procedure*; GO:0051480 regulation of cytosolic calcium ion concentration |
| Valve-development mechanism | PIEZO1 is required for **lymphatic valve formation**; loss in endothelial/lymphatic endothelium reduces valve number and causes pleural effusion/postnatal lethality in mouse models | Mouse + cultured LECs | Endothelial-specific knockout mice showed **dramatic reduction** in lymphatic valves; pleural effusion and postnatal death reported | Nonomura et al., **2018-11**, *PNAS*, DOI: https://doi.org/10.1073/pnas.1817070115 (PMID not available in context) (iyer2020lymphaticvalvesand pages 15-17) | GO:0001946 lymphangiogenesis; GO:0035239 tube morphogenesis; CL:0000115 endothelial cell; CL lymphatic endothelial cell; UBERON:0005409 lymphatic vessel |
| Valve development and maintenance | PIEZO1 senses **oscillating shear stress** and drives the genetic program for **lymphatic valve development and maintenance**; adult deletion causes valve degeneration | Mouse + in vitro LECs | Newborn endothelial or lymphatic-specific deletion inhibited valve formation; adult deletion caused “substantial” valve degeneration | Choi et al., **2019-05**, *JCI Insight*, DOI: https://doi.org/10.1172/jci.insight.125068 (choi2019piezo1incorporatesmechanical pages 2-4, choi2019piezo1incorporatesmechanical pages 1-2) | GO:0034405 response to fluid shear stress; GO:0001946 lymphangiogenesis; HP:0002564 Lymphatic vessel abnormality |
| Sprouting / regression mechanism | PIEZO1 acts upstream of **ORAI1** in flow-activated lymphatic expansion; deletion causes sprouting defects and adult lymphatic regression; activation enhances regeneration | Mouse + in vitro LECs | Lymphatic-specific conditional KO phenocopied sprouting defects; postnatal deletion induced regression; **Yoda1** suppressed postsurgical lymphedema in mice | Choi et al., **2022-07**, *Circulation Research*, DOI: https://doi.org/10.1161/circresaha.121.320565 (choi2022piezo1regulatedmechanotransductioncontrols pages 10-12, choi2022piezo1regulatedmechanotransductioncontrols pages 1-3) | GO:0001946 lymphangiogenesis; GO:0035556 intracellular signal transduction; NCIT: Preclinical Study |
| 2024 pathway advance | PIEZO1 functions **upstream of ANGPT2/TIE/PI3K/AKT/FOXO1 signaling** in lymphatic endothelial cells, linking mechanosensation to transcriptional regulation relevant to lymphedema biology | Mouse + in vitro LECs | PIEZO1 activation triggered **rapid ANGPT2 exocytosis**, **TIE1 ectodomain shedding by ADAM17**, increased **TIE/PI3K/AKT**, and **FOXO1 nuclear export** | Du et al., **2024-05**, *J Clin Invest*, DOI: https://doi.org/10.1172/jci176577 (du2024themechanosensorychannel pages 1-2) | GO:0034405 response to fluid shear stress; GO:0014068 positive regulation of phosphatidylinositol 3-kinase signaling; GO:0001525 angiogenesis/lymphatic vascular development; CL:0000115 endothelial cell |
| Current understanding of pathophysiology | Consensus model: biallelic PIEZO1 LOF impairs lymphatic endothelial mechanosensation, disrupting valve morphogenesis, sprouting, and maintenance, producing fetal effusions/hydrops and later systemic lymphedema | Synthesis of human + in vitro + mouse evidence | Supported across **2015–2024** human genetics and mechanistic studies | Supported by Fotiou 2015, Lukacs 2015, Nonomura 2018, Choi 2019/2022, Du 2024 (du2024themechanosensorychannel pages 1-2, choi2019piezo1incorporatesmechanical pages 2-4, choi2022piezo1regulatedmechanotransductioncontrols pages 10-12, iyer2020lymphaticvalvesand pages 15-17, fotiou2015novelmutationsin pages 1-2) | MONDO:0014797; GO:0001946 lymphangiogenesis; GO:0034405 response to fluid shear stress; CL: lymphatic endothelial cell |
| Diagnostics | Most specific diagnostic evidence is **molecular**: exome sequencing/NGS identifying **biallelic PIEZO1 variants**, supported by segregation and functional testing when missense/VUS alleles are found | Human clinical / molecular diagnostics | WES identified causative variants in founding families and sibling pair; lymphoscintigraphy reported in Fotiou cohort; RBC film abnormalities can be supportive but nonspecific | Fotiou et al., **2015-09**; Lukacs et al., **2015-09** (fotiou2015novelmutationsin pages 2-3, iyer2020lymphaticvalvesand pages 15-17) | NCIT: Whole Exome Sequencing; HP:0001789; LOINC/NCIT suggestions for lymphoscintigraphy not disease-specific |
| Prognosis / natural history | Prenatal course can include NIHF and fetal demise; in survivors, edema may partially/fully resolve postnatally then recur as persistent or childhood-onset lymphedema with systemic complications | Human clinical | Context notes fetal demise, postnatal hydrops resolution, onset around **6–9 years** in some survivors, and adult presentations in later families | Fotiou 2015; Ludlow 2023 (fotiou2015novelmutationsin pages 2-3, ludlow2023smallmoleculefunctionalrescue pages 8-10, cheng2025piezo1variantimplications pages 3-4) | HP:0003573 Congenital onset; HP:0001789 Lymphedema; HP:0002202 Pleural effusion |
| Epidemiology | Disease-specific prevalence/incidence for LM6 is **not established** in retrieved sources; generalized lymphatic dysplasia is rare | Human clinical / review-level statement | No robust population rate found for LM6; one preprint excerpt mentioned GLD approx. **1 in 6000**, but this appears to refer broadly and should be treated cautiously | Ludlow et al., **2023-08** preprint (context summary only) (ludlow2023smallmoleculefunctionalrescue pages 5-8) | MONDO:0014797; Orphan disease coding pending confirmation |
| Clinical treatment evidence | No approved **PIEZO1-genotype-specific** therapy was found in retrieved evidence; management in published human LM6 reports is largely supportive and complication-directed | Human clinical + evidence gap | No controlled LM6 treatment trial identified in retrieved sources | Evidence gap across retrieved LM6 literature (fotiou2015novelmutationsin pages 1-2, ludlow2023smallmoleculefunctionalrescue pages 8-10, fotiou2015novelmutationsin pages 2-3) | NCIT: Supportive Care; NCIT: Lymphedema Therapy |
| Generic lymphatic-malformation trials | Active LM/vascular-anomaly trials exist for **sirolimus/rapamycin** and **alpelisib**, but these are **not PIEZO1-genotype-specific** and should not be interpreted as LM6-targeted evidence | Clinical trials, non-genotype-specific | Examples: **NCT06673290** recruiting, n=150; **NCT03243019** recruiting, n=28; **NCT06239480** active-not-recruiting, n=51; **NCT05948943** recruiting, n=232; **NCT00975819** completed, n=61 | ClinicalTrials.gov results retrieved in tool output (current statuses as returned) (OpenTargets Search: lymphatic malformation 6) | NCIT: Sirolimus; NCIT: Alpelisib; NCIT: Clinical Trial; note: not specific to MONDO:0014797 |
| Prevention / environment | No evidence supports environmental, infectious, lifestyle, or protective factors as causal for LM6; prevention is primarily **genetic counseling/reproductive risk management** in affected families | Human genetics / evidence gap | Autosomal recessive inheritance implies **25% recurrence risk** for carrier-couple pregnancies, though exact counseling numbers were not directly quoted in retrieved contexts | Inference from AR inheritance established by Fotiou/Lukacs (iyer2020lymphaticvalvesand pages 15-17, fotiou2015novelmutationsin pages 1-2) | NCIT: Genetic Counseling; HP/GO not applicable |
| Model systems | Best-supported disease models are **endothelial or lymphatic-specific Piezo1 knockout mice** and cultured lymphatic endothelial cells; these recapitulate valve/sprouting defects and enable pathway dissection | Mouse + in vitro | Multiple conditional models: Tie2Cre, Lyve1Cre, Prox1-CreERT2, Cdh5(PAC)-CreERT2 reported in context | Nonomura 2018; Choi 2019; Choi 2022; Du 2024 (du2024themechanosensorychannel pages 1-2, choi2019piezo1incorporatesmechanical pages 2-4, choi2022piezo1regulatedmechanotransductioncontrols pages 10-12, iyer2020lymphaticvalvesand pages 15-17) | CL: lymphatic endothelial cell; GO:0001946 lymphangiogenesis; NCIT: Disease Model |


*Table: This compact table organizes the key human, in vitro, mouse, and trial evidence for PIEZO1-related lymphatic malformation 6. It highlights the founding 2015 cohorts, recent mechanistic advances, and the important distinction between preclinical Yoda1 rescue and non-genotype-specific lymphatic-malformation trials.*

## 1. Disease information

### Definition and identifiers

- **Preferred name:** Lymphatic malformation 6.
- **Core clinical designation:** PIEZO1-related generalized lymphatic dysplasia.
- **MONDO:** **MONDO:0014797**.
- **OMIM:** **616843**.
- **Causal gene:** **PIEZO1**, Ensembl **ENSG00000103335**; approved name *piezo type mechanosensitive ion channel component 1 (Er blood group)*. OpenTargets identifies PIEZO1 as the sole associated target, supported by five evidence records and multiple disease-defining publications. (OpenTargets Search: lymphatic malformation 6)
- **Common synonyms:** generalized lymphatic dysplasia with nonimmune hydrops fetalis; PIEZO1-related generalized lymphatic dysplasia; congenital lymphatic dysplasia; hereditary lymphedema due to PIEZO1 deficiency; Fotiou generalized lymphatic dysplasia.
- **Classification:** congenital primary lymphatic anomaly; autosomal-recessive Mendelian disease.

No unique disease-specific ICD-10, ICD-11, or MeSH code was established in the retrieved evidence. Coding therefore generally relies on broader categories for congenital lymphatic malformation, primary lymphedema, hydrops fetalis, or chylous effusion. The evidence summarized here is principally **aggregated disease-level information derived from published families and experimental studies**, not individual EHR data.

### Defining abstract quotations

Fotiou et al. defined GLD as “**a rare form of primary lymphoedema characterized by a uniform, widespread lymphoedema affecting all segments of the body, with systemic involvement such as intestinal and/or pulmonary lymphangiectasia, pleural effusions, chylothoraces and/or pericardial effusions**.” They further reported “**homozygous and compound heterozygous mutations in PIEZO1, resulting in an autosomal recessive form of GLD with a high incidence of non-immune hydrops fetalis**.” Published September 2015; DOI: https://doi.org/10.1038/ncomms9085; PMID **26333996**. (OpenTargets Search: lymphatic malformation 6, fotiou2015novelmutationsin pages 1-2)

Lukacs et al. reported: “**Through whole-exome sequencing, we identify biallelic mutations in PIEZO1 … in a pair of siblings affected with persistent lymphoedema caused by congenital lymphatic dysplasia**.” Published September 2015; DOI: https://doi.org/10.1038/ncomms9329; PMID **26387913**. (OpenTargets Search: lymphatic malformation 6, iyer2020lymphaticvalvesand pages 15-17)

## 2. Etiology

### Causal factors and genetic risk

The established cause is **biallelic pathogenic or likely pathogenic PIEZO1 variation**, usually homozygous or compound heterozygous, producing absent protein, defective membrane trafficking, or impaired mechanically activated channel function. Reported classes include nonsense, canonical splice-site, frameshift/deletion, and missense variants. Ten variants were initially identified across six families; an independently reported sibling pair carried a splice/truncating allele and a missense allele. (iyer2020lymphaticvalvesand pages 15-17, fotiou2015novelmutationsin pages 1-2, cheng2025piezo1variantimplications pages 3-4)

Important genotype distinction:

1. **Biallelic PIEZO1 loss of function** causes LM6/GLD.
2. **Heterozygous PIEZO1 gain-of-function variants** more commonly cause autosomal-dominant dehydrated hereditary stomatocytosis, sometimes accompanied by perinatal edema or hydrops. These allelic disorders should not be conflated. (iyer2020lymphaticvalvesand pages 15-17, ludlow2023smallmoleculefunctionalrescue pages 5-8)

Family history, parental consanguinity, and carriage of a pathogenic allele in each parent increase reproductive risk. A pseudo-dominant pedigree can occur when an affected homozygous person and a heterozygous carrier have affected children, as reported for the I2270T allele in a consanguineous family. (ludlow2023smallmoleculefunctionalrescue pages 8-10, ludlow2023smallmoleculefunctionalrescue pages 14-16)

### Environmental, infectious, and lifestyle factors

No reproducible toxin, radiation, infectious, dietary, smoking, alcohol, occupational, or other environmental cause has been demonstrated. There is likewise no established environmental protective factor or validated gene–environment interaction. Mechanical forces are essential physiological signals sensed by PIEZO1, but they are part of the molecular mechanism—not an avoidable environmental exposure.

No genetic protective allele has been validated for LM6. Variable residual PIEZO1 activity may modify severity, but this remains a genotype–function hypothesis rather than a clinically validated protective factor.

## 3. Phenotypes

The phenotype is multisystemic and markedly variable. Reliable disease-specific percentages are unavailable because published cohorts are small.

- **Nonimmune hydrops fetalis — HP:0001561:** prenatal sign, often detected in the second or third trimester; ranges from transient to lethal. One founding-family fetus died at 34 weeks, whereas hydrops resolved after birth in some survivors. (fotiou2015novelmutationsin pages 1-2, fotiou2015novelmutationsin pages 2-3)
- **Pleural effusion — HP:0002202; chylothorax — HP:0010318:** prenatal, neonatal, childhood, or adult manifestation; may be bilateral and persistent. In a recent family, bilateral hydrothoraces were detected at 19 weeks; another patient developed bilateral chylothoraces in the third decade. (ludlow2023smallmoleculefunctionalrescue pages 8-10, ludlow2023smallmoleculefunctionalrescue pages 41-45)
- **Pericardial effusion — HP:0001698:** systemic lymphatic manifestation; CT documentation accompanied bilateral chylothorax in one recent proband. (ludlow2023smallmoleculefunctionalrescue pages 41-45)
- **Ascites — HP:0001744:** prenatal or postnatal fluid accumulation resulting from defective lymphatic drainage. (ludlow2023smallmoleculefunctionalrescue pages 8-10, ludlow2023smallmoleculefunctionalrescue pages 5-8)
- **Generalized/peripheral lymphedema — HP:0001789:** congenital or delayed onset, affecting all four limbs, face, and sometimes genitalia. Some founding-cohort survivors developed edema around 6–9 years, whereas recent families expand onset into adulthood. (ludlow2023smallmoleculefunctionalrescue pages 8-10, fotiou2015novelmutationsin pages 2-3, ludlow2023smallmoleculefunctionalrescue pages 5-8)
- **Facial edema/facial dysmorphism — suggested HP:0000978:** secondary to chronic lymphatic swelling; may impair appearance, oral function, and psychosocial well-being. (fotiou2015novelmutationsin pages 1-2)
- **Lymphangiectasia — HP:0001733:** intestinal or pulmonary; may lead to respiratory morbidity, protein loss, nutritional problems, and recurrent effusions. (choi2022piezo1regulatedmechanotransductioncontrols pages 10-12, fotiou2015novelmutationsin pages 1-2)
- **Polyhydramnios — HP:0002023:** reported in antenatally affected pregnancies. (ludlow2023smallmoleculefunctionalrescue pages 8-10)
- **Recurrent cellulitis:** two founding-cohort patients had severe recurrent facial cellulitis, a complication of chronic edema and impaired local barrier/immune function. (fotiou2015novelmutationsin pages 2-3)
- **Subtle erythrocyte abnormalities:** stomatocytes or spherocytes were reported in some affected people and carriers, but these are inconsistent and are not diagnostic of LM6. (fotiou2015novelmutationsin pages 2-3)

Quality-of-life studies specific to LM6 were not retrieved. Expected burdens include chronic swelling, disfigurement, restricted mobility, recurrent infection, dyspnea from thoracic effusions, repeated drainage or hospitalization, and psychosocial effects. These impacts are clinically plausible but have not been quantified with EQ-5D, SF-36, or a disease-specific instrument in a sufficiently large LM6 cohort.

## 4. Genetic and molecular information

**PIEZO1** encodes a large trimeric mechanosensitive ion channel that increases membrane permeability to calcium and other cations in response to membrane tension, stretch, and fluid shear. Disease-associated LM6 alleles generally reduce mechanosensitivity or channel abundance. (du2024themechanosensorychannel pages 1-2, iyer2020lymphaticvalvesand pages 15-17)

Reported variants in retrieved studies include truncating alleles **p.E755X, p.E1630X, and p.Q2228X**, splice donor **c.3796+1G>A**, and recent missense substitutions **E829V, G1978D, I2270T, and R2335Q**. The 2015 study also documented another splice-site allele, c.1669+1G>A. Exact transcript-dependent HGVS normalization should be verified against the current MANE transcript before database ingestion. (fotiou2015novelmutationsin pages 1-2, fotiou2015novelmutationsin pages 2-3, ludlow2023smallmoleculefunctionalrescue pages 41-45)

The early variants segregated with disease; most were absent from dbSNP, 1000 Genomes, and 900 controls, while two had reported minor-allele frequencies of approximately 0.0002. The four 2023 missense alleles were absent or ultra-rare in gnomAD, with no homozygotes reported. (fotiou2015novelmutationsin pages 1-2, ludlow2023smallmoleculefunctionalrescue pages 41-45)

Functional consequences include exon skipping or intron retention, premature truncation, reduced/absent protein, impaired surface trafficking, and channels that reach the membrane but have markedly reduced mechanosensitivity. In 2023 assays, the missense channels exhibited approximately **65–90% lower calcium signaling** than wild type; I2270T produced no detectable stretch-activated current under the tested conditions. Yoda1 restored activity in several mutant channels. (ludlow2023smallmoleculefunctionalrescue pages 8-10, ludlow2023smallmoleculefunctionalrescue pages 14-16)

No validated modifier gene, disease-specific methylation signature, recurrent chromosomal abnormality, or somatic mosaic mechanism has been established. The disorder is primarily a **germline single-gene disease**.

## 5. Environmental information

Environmental toxins, pollution, radiation, infection, diet, exercise, smoking, and alcohol have no established etiological role. Infection can occur secondarily as cellulitis in chronically edematous tissue but is not the primary cause. Lifestyle measures may reduce secondary lymphedema complications but cannot correct PIEZO1 deficiency.

## 6. Mechanism and pathophysiology

### Causal chain

**Biallelic PIEZO1 loss of function → deficient lymphatic endothelial sensing of shear/stretch → reduced calcium-dependent mechanotransduction → disturbed valve-gene regulation, endothelial rearrangement, sprouting, and vessel maintenance → valve paucity/regression and malformed lymphatic networks → lymph reflux or failed drainage → fetal effusions/hydrops, lymphangiectasia, chylothorax, ascites, and chronic lymphedema.** Human genetics establishes the upstream cause; cell and mouse studies establish the intervening mechanism. (du2024themechanosensorychannel pages 1-2, choi2019piezo1incorporatesmechanical pages 2-4, choi2022piezo1regulatedmechanotransductioncontrols pages 1-3, iyer2020lymphaticvalvesand pages 15-17, fotiou2015novelmutationsin pages 1-2)

### Principal pathways

1. **Valve morphogenesis:** Piezo1 detects oscillatory shear stress in lymphatic endothelial cells. Conditional deletion suppresses valve formation in newborn mice; adult deletion causes substantial valve degeneration. Knockdown prevents flow-induced expression of valve genes, whereas overexpression or Yoda1 activation promotes valve-gene expression. (choi2019piezo1incorporatesmechanical pages 2-4, choi2019piezo1incorporatesmechanical pages 1-2)
2. **Cytoskeletal and junctional remodeling:** endothelial Piezo1 knockout impairs valve-leaflet protrusion, collective migration, actin polymerization, and remodeling of VE-cadherin-positive junctions. Knockout mice have markedly fewer lymphatic valves, pleural effusions, and postnatal death. (iyer2020lymphaticvalvesand pages 15-17)
3. **PIEZO1–ORAI1–KLF2/DTX/NOTCH axis:** flow-activated PIEZO1 lies upstream of ORAI1-dependent calcium signaling and regulates KLF2, DTX1, DTX3L, and NOTCH1. Loss causes embryonic sprouting defects and adult lymphatic regression; Dtx3L expression can rescue aspects of the knockout phenotype. (choi2022piezo1regulatedmechanotransductioncontrols pages 10-12, choi2022piezo1regulatedmechanotransductioncontrols pages 1-3)
4. **2024 ANGPT2/TIE/PI3K/AKT/FOXO1 advance:** PIEZO1 activation triggers ANGPT2 exocytosis, ADAM17-dependent TIE1 ectodomain shedding, increased TIE/PI3K/AKT signaling, and FOXO1 nuclear export. It regulates lymphedema-associated valve genes including FOXC2, GATA2, GJA4, and ITGA9. Published May 2024; DOI: https://doi.org/10.1172/JCI176577. (du2024themechanosensorychannel pages 1-2)

Suggested annotations include **GO:0034405 response to fluid shear stress**, **GO:0001946 lymphangiogenesis**, calcium-ion transport/signaling, actin-cytoskeleton organization, cell–cell junction organization, and PI3K/AKT signaling. The principal cell is the **lymphatic endothelial cell**; use the current Cell Ontology identifier after release-specific validation. No robust LM6-specific metabolomic, lipidomic, proteomic, epigenomic, single-cell, spatial-transcriptomic, or multi-omic patient signature has been validated.

## 7. Anatomical structures affected

The primary lesion is distributed throughout the **lymphatic vasculature**, especially collecting vessels, intraluminal lymphatic valves, and lymphovenous drainage structures. Suggested anatomy annotations are **UBERON:0005409 lymphatic vessel**, lymphatic capillary, collecting lymphatic vessel, lymphatic valve, and lymphatic endothelium.

Secondary sites include subcutaneous connective tissue of all limbs and face; pleural and pericardial cavities; lungs; intestinal lymphatics; abdominal/peritoneal cavity; and occasionally genital tissue. Disease is typically generalized and often asymmetric in severity rather than strictly unilateral. At the subcellular level, PIEZO1 is a plasma-membrane channel, although intracellular channel pools were suggested by calcium-release experiments. (ludlow2023smallmoleculefunctionalrescue pages 8-10, ludlow2023smallmoleculefunctionalrescue pages 5-8)

## 8. Temporal development

Onset may be antenatal, congenital, childhood, or—less commonly—adult. Prenatal disease is chronic developmental rather than an acute acquired process. Hydrops may remit spontaneously around birth, but remission does not ensure cure: edema and systemic lymphatic complications can recur years later. Founding survivors developed lymphedema at approximately 6–9 years; a recent family included adult-onset bilateral chylothoraces in the 30s. (ludlow2023smallmoleculefunctionalrescue pages 8-10, fotiou2015novelmutationsin pages 2-3, cheng2025piezo1variantimplications pages 3-4)

There is no validated staging system. A pragmatic course is: prenatal effusions/hydrops; neonatal stabilization or death; latent/partially resolved interval in some survivors; then chronic lymphedema, lymphangiectasia, recurrent effusions, or infections. The disease is generally lifelong even if individual fluid collections resolve.

## 9. Inheritance and population

Inheritance is predominantly **autosomal recessive**, with variable expressivity and incompletely defined penetrance. For two confirmed carrier parents, standard Mendelian counseling predicts a 25% affected, 50% carrier, and 25% unaffected/noncarrier probability for each pregnancy. Pseudo-dominant inheritance can occur in consanguineous pedigrees. Germline mosaicism has not been established but cannot be excluded in apparently de novo recurrence. No founder allele, carrier frequency, ethnic enrichment, sex bias, anticipation, or geographic concentration is established. (fotiou2015novelmutationsin pages 1-2, ludlow2023smallmoleculefunctionalrescue pages 14-16)

Disease-specific prevalence and incidence are unknown. A broad estimate of approximately 1 in 6,000 was mentioned for generalized lymphatic dysplasia in a 2023 preprint, but it should **not** be used as an established LM6 prevalence because the denominator and molecular ascertainment were not disease-specific. (ludlow2023smallmoleculefunctionalrescue pages 5-8)

## 10. Diagnostics

### Clinical and imaging assessment

Prenatal ultrasound should evaluate skin edema, ascites, pleural/pericardial effusions, hydrothorax, placental edema, and polyhydramnios. Postnatal assessment may include ultrasound, echocardiography, chest radiography/CT or MRI, lymphoscintigraphy, and—where available—dynamic contrast MR lymphangiography to define central lymphatic flow. Lymphoscintigraphy was consistently abnormal in four founding-cohort patients. (fotiou2015novelmutationsin pages 2-3)

Laboratory evaluation is mainly directed toward complications: CBC and blood film; hemolysis indices where stomatocytosis is suspected; albumin, total protein, immunoglobulins and lymphocyte counts for intestinal lymph loss; electrolytes; and pleural-fluid triglycerides/chylomicrons for chylothorax. No validated circulating LM6 biomarker exists.

### Genetic testing algorithm

1. Confirm a generalized congenital lymphatic phenotype and exclude immune, cardiac, chromosomal, infectious, hematologic, and structural causes of hydrops.
2. Use a **primary-lymphedema/generalized lymphatic-anomaly panel** that includes PIEZO1 and relevant differential genes such as PIEZO2, EPHB4, RASA1, ANGPT2, TIE1, FLT4, CCBE1, FAT4, ADAMTS3, FOXC2, GATA2, PTPN14, and PIK3CA.
3. If negative, perform trio WES or WGS; WGS is useful for deep intronic, structural, and poorly captured variants.
4. Confirm candidate PIEZO1 variants by segregation analysis. For missense VUS, functional channel assays may be decisive because surface-localized protein can still lack mechanical activity. (iyer2020lymphaticvalvesand pages 15-17, ludlow2023smallmoleculefunctionalrescue pages 8-10, ludlow2023smallmoleculefunctionalrescue pages 41-45)

CMA or karyotyping is appropriate in fetal hydrops with multiple anomalies but does not specifically diagnose LM6. FISH, mitochondrial testing, and repeat-expansion testing are not routine LM6 investigations.

Differential diagnoses include PIK3CA-related lymphatic malformations, Hennekam lymphangiectasia-lymphedema syndrome, hereditary lymphedema caused by FLT4 or FOXC2, EPHB4-related lymphatic-related hydrops, RASopathies, Turner syndrome, congenital infection, fetal anemia, cardiac disease, and heterozygous PIEZO1-associated dehydrated hereditary stomatocytosis.

## 11. Outcome and prognosis

Prognosis is variable. Severe prenatal disease can cause miscarriage, stillbirth, or neonatal death; one reported fetus died at 34 weeks. Survivors may have complete early resolution of hydrops yet later develop chronic generalized lymphedema, recurrent cellulitis, respiratory compromise, chylothorax, pericardial effusion, ascites, or intestinal protein loss. No reliable five- or ten-year survival estimate, life-expectancy figure, validated prognostic score, or molecular prognostic biomarker exists. (fotiou2015novelmutationsin pages 1-2, fotiou2015novelmutationsin pages 2-3, cheng2025piezo1variantimplications pages 3-4)

Residual channel function, extent of thoracic/intestinal involvement, persistence of prenatal effusions, and ability to control chyle loss are plausible prognostic factors, but they have not been validated in a sufficiently large prospective cohort.

## 12. Treatment

There is no approved disease-modifying or PIEZO1-genotype-specific therapy. Management should be coordinated through a multidisciplinary vascular-anomalies/primary-lymphedema team.

- **Lymphedema care:** compression garments or bandaging, skin care, exercise, manual lymphatic drainage where appropriate, weight optimization, rapid treatment of cellulitis, and physical/occupational therapy.
- **Effusions and chylothorax:** respiratory support, drainage when clinically required, nutritional management with low long-chain-fat/high-medium-chain-triglyceride feeding or parenteral nutrition, and individualized lymphatic interventional procedures.
- **Surgery/intervention:** pleurodesis, thoracic-duct or abnormal-channel embolization, lymphovenous procedures, or debulking may be considered according to anatomy and severity; no LM6-specific response rate is established.
- **Sirolimus/rapamycin:** used for complicated lymphatic anomalies generally, but no controlled evidence establishes efficacy specifically for biallelic PIEZO1 LM6.
- **Alpelisib:** appropriate only for proven PIK3CA-driven disease; it is not mechanistically indicated solely by a PIEZO1 diagnosis.

Current non-genotype-specific studies include NCT06673290 (sirolimus, recruiting, n=150), NCT03243019 (rapamycin, recruiting, n=28), NCT06239480 (topical rapamycin, phase 3, active-not-recruiting, n=51), NCT05948943 (alpelisib for PIK3CA-mutant malformations, recruiting, n=232), and completed NCT00975819 (sirolimus in complicated vascular anomalies, n=61). None should be represented as an LM6-specific trial. (OpenTargets Search: lymphatic malformation 6)

### Experimental PIEZO1 agonism

Yoda1 accelerated valve formation, promoted lymphatic sprouting, reduced postsurgical lymphedema in mice, and rescued several mechanically insensitive human mutant channels in vitro. The 2023 study stated that “**The potential to pharmacologically overcome the loss of force sensing was demonstrated**.” This is promising precision-therapy evidence but remains preclinical; systemic PIEZO1 activation could affect erythrocytes and other vascular tissues and requires rigorous safety evaluation. DOI: https://doi.org/10.1101/2023.08.01.23292554. (choi2022piezo1regulatedmechanotransductioncontrols pages 1-3, ludlow2023smallmoleculefunctionalrescue pages 14-16, ludlow2023smallmoleculefunctionalrescue pages 5-8)

Suggested NCIT annotations include Genetic Counseling, Supportive Care, Lymphedema Therapy, Compression Therapy, Sirolimus, Alpelisib, Pleurodesis, and Clinical Trial; exact NCIT identifiers should be release-validated.

## 13. Prevention

No primary lifestyle or environmental prevention exists. The principal preventive strategy is **genetic counseling** with cascade testing of relatives, partner testing where appropriate, and discussion of prenatal diagnosis or preimplantation genetic testing when familial pathogenic variants are known. Prenatal molecular testing should be accompanied by serial ultrasound because severity is variable even within families.

Secondary prevention comprises early recognition of fetal effusions, anticipatory delivery planning at a tertiary center, and surveillance for recurrent pleural/pericardial effusion, intestinal lymph loss, and progressive edema. Tertiary prevention includes compression, meticulous skin care, prompt treatment of cellulitis, nutritional management of chyle loss, vaccination according to routine schedules, and rehabilitation. No vaccine or prophylactic medication prevents LM6 itself.

## 14. Other species and natural disease

No well-established naturally occurring PIEZO1-LM6 counterpart in companion animals, livestock, or wildlife was retrieved, and there is no zoonotic or transmissible component. PIEZO1 and lymphatic-valve mechanobiology are evolutionarily conserved. Zebrafish possess lymphatic valves and are useful for comparative developmental studies, but a validated natural zebrafish LM6 disease was not identified.

## 15. Model organisms

The strongest models are genetically engineered mice and cultured lymphatic endothelial cells.

- **Tie2Cre;Piezo1 conditional knockout mice:** endothelial loss causes pleural effusion, marked lymphatic-valve reduction, and postnatal death.
- **Lyve1Cre;Piezo1 knockout mice:** lymphatic/endothelial targeting confirms a valve requirement.
- **Prox1-CreERT2 and Cdh5(PAC)-CreERT2 models:** temporally controlled deletion demonstrates requirements in neonatal valve formation and adult valve maintenance.
- **Lymphatic-specific embryonic/adult deletion models:** reproduce sprouting defects, reduced branching, delayed valve formation, and adult vessel regression.
- **Cultured human or mouse lymphatic endothelial cells:** support shear-stress, calcium imaging, patch-clamp, trafficking, RNA-expression, and ANGPT2/TIE/FOXO1 pathway studies.
- **Heterologous expression systems:** determine whether individual human missense variants alter surface localization, mechanically activated current, calcium influx, or Yoda1 responsiveness. (du2024themechanosensorychannel pages 1-2, choi2019piezo1incorporatesmechanical pages 2-4, choi2022piezo1regulatedmechanotransductioncontrols pages 10-12, iyer2020lymphaticvalvesand pages 15-17, ludlow2023smallmoleculefunctionalrescue pages 8-10)

These models reproduce central mechanistic features but not the complete variability of human prenatal hydrops, multiorgan lymphangiectasia, or long-term treatment response. Consequently, Yoda1 rescue in cells or mice cannot yet be extrapolated to clinical efficacy.

## Evidence limitations and curation recommendations

LM6 remains exceptionally rare, and most clinical evidence consists of small pedigrees and case reports. Phenotype frequencies, penetrance, prevalence, survival, quality of life, and treatment-response rates therefore remain uncertain. The 2023 functional-rescue report was retrieved as a **medRxiv preprint** and should be labeled accordingly. Ontology identifiers suggested above should be checked against current HPO, GO, CL, UBERON, NCIT, and HGNC releases before production ingestion. Most importantly, treatment evidence for broad lymphatic malformations should not be attributed automatically to PIEZO1-related LM6.

References

1. (OpenTargets Search: lymphatic malformation 6): Open Targets Query (lymphatic malformation 6, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (iyer2020lymphaticvalvesand pages 15-17): Drishya Iyer, Melanie Jannaway, Ying Yang, and Joshua P. Scallan. Lymphatic valves and lymph flow in cancer-related lymphedema. Cancers, 12:2297, Aug 2020. URL: https://doi.org/10.3390/cancers12082297, doi:10.3390/cancers12082297. This article has 50 citations.

3. (fotiou2015novelmutationsin pages 1-2): Elisavet Fotiou, Silvia Martin-Almedina, Michael A. Simpson, Shin Lin, Kristiana Gordon, Glen Brice, Giles Atton, Iona Jeffery, David C. Rees, Cyril Mignot, Julie Vogt, Tessa Homfray, Michael P. Snyder, Stanley G. Rockson, Steve Jeffery, Peter S. Mortimer, Sahar Mansour, and Pia Ostergaard. Novel mutations in piezo1 cause an autosomal recessive generalized lymphatic dysplasia with non-immune hydrops fetalis. Nature Communications, Sep 2015. URL: https://doi.org/10.1038/ncomms9085, doi:10.1038/ncomms9085. This article has 380 citations and is from a highest quality peer-reviewed journal.

4. (du2024themechanosensorychannel pages 1-2): Jing Du, Pan Liu, Yalu Zhou, Sol Misener, Isha Sharma, Phoebe Leeaw, Benjamin R. Thomson, Jing Jin, and Susan E. Quaggin. The mechanosensory channel piezo1 functions upstream of angiopoietin/tie/foxo1 signaling in lymphatic development. The Journal of Clinical Investigation, May 2024. URL: https://doi.org/10.1172/jci176577, doi:10.1172/jci176577. This article has 33 citations.

5. (choi2022piezo1regulatedmechanotransductioncontrols pages 1-3): Dongwon Choi, Eunkyung Park, Roy P. Yu, Michael N. Cooper, Il-Taeg Cho, Joshua Choi, James Yu, Luping Zhao, Ji-Eun Irene Yum, Jin Suh Yu, Brandon Nakashima, Sunju Lee, Young Jin Seong, Wan Jiao, Chester J. Koh, Peter Baluk, Donald M. McDonald, Sindhu Saraswathy, Jong Y. Lee, Noo Li Jeon, Zhenqian Zhang, Alex S. Huang, Bin Zhou, Alex K. Wong, and Young-Kwon Hong. Piezo1-regulated mechanotransduction controls flow-activated lymphatic expansion. Circulation Research, Jul 2022. URL: https://doi.org/10.1161/circresaha.121.320565, doi:10.1161/circresaha.121.320565. This article has 115 citations and is from a highest quality peer-reviewed journal.

6. (ludlow2023smallmoleculefunctionalrescue pages 14-16): Melanie J Ludlow, Oleksandr V Povstyan, Deborah M Linley, Silvia Martin-Almedina, Charlotte Revill, Kevin Cuthbertson, Katie A Smith, Emily Fay, Elisavet Fotiou, Andrew Bush, Claire Hogg, Tobias Linden, Natalie B Tan, Susan M White, Esther Dempsey, Sahar Mansour, Gregory Parsonage, Antreas C Kalli, Richard Foster, Pia Ostergaard, and David J Beech. Small-molecule functional rescue of piezo1 channel variants associated with generalised lymphatic dysplasia. MedRxiv, Aug 2023. URL: https://doi.org/10.1101/2023.08.01.23292554, doi:10.1101/2023.08.01.23292554. This article has 5 citations.

7. (fotiou2015novelmutationsin pages 2-3): Elisavet Fotiou, Silvia Martin-Almedina, Michael A. Simpson, Shin Lin, Kristiana Gordon, Glen Brice, Giles Atton, Iona Jeffery, David C. Rees, Cyril Mignot, Julie Vogt, Tessa Homfray, Michael P. Snyder, Stanley G. Rockson, Steve Jeffery, Peter S. Mortimer, Sahar Mansour, and Pia Ostergaard. Novel mutations in piezo1 cause an autosomal recessive generalized lymphatic dysplasia with non-immune hydrops fetalis. Nature Communications, Sep 2015. URL: https://doi.org/10.1038/ncomms9085, doi:10.1038/ncomms9085. This article has 380 citations and is from a highest quality peer-reviewed journal.

8. (ludlow2023smallmoleculefunctionalrescue pages 41-45): Melanie J Ludlow, Oleksandr V Povstyan, Deborah M Linley, Silvia Martin-Almedina, Charlotte Revill, Kevin Cuthbertson, Katie A Smith, Emily Fay, Elisavet Fotiou, Andrew Bush, Claire Hogg, Tobias Linden, Natalie B Tan, Susan M White, Esther Dempsey, Sahar Mansour, Gregory Parsonage, Antreas C Kalli, Richard Foster, Pia Ostergaard, and David J Beech. Small-molecule functional rescue of piezo1 channel variants associated with generalised lymphatic dysplasia. MedRxiv, Aug 2023. URL: https://doi.org/10.1101/2023.08.01.23292554, doi:10.1101/2023.08.01.23292554. This article has 5 citations.

9. (ludlow2023smallmoleculefunctionalrescue pages 5-8): Melanie J Ludlow, Oleksandr V Povstyan, Deborah M Linley, Silvia Martin-Almedina, Charlotte Revill, Kevin Cuthbertson, Katie A Smith, Emily Fay, Elisavet Fotiou, Andrew Bush, Claire Hogg, Tobias Linden, Natalie B Tan, Susan M White, Esther Dempsey, Sahar Mansour, Gregory Parsonage, Antreas C Kalli, Richard Foster, Pia Ostergaard, and David J Beech. Small-molecule functional rescue of piezo1 channel variants associated with generalised lymphatic dysplasia. MedRxiv, Aug 2023. URL: https://doi.org/10.1101/2023.08.01.23292554, doi:10.1101/2023.08.01.23292554. This article has 5 citations.

10. (ludlow2023smallmoleculefunctionalrescue pages 8-10): Melanie J Ludlow, Oleksandr V Povstyan, Deborah M Linley, Silvia Martin-Almedina, Charlotte Revill, Kevin Cuthbertson, Katie A Smith, Emily Fay, Elisavet Fotiou, Andrew Bush, Claire Hogg, Tobias Linden, Natalie B Tan, Susan M White, Esther Dempsey, Sahar Mansour, Gregory Parsonage, Antreas C Kalli, Richard Foster, Pia Ostergaard, and David J Beech. Small-molecule functional rescue of piezo1 channel variants associated with generalised lymphatic dysplasia. MedRxiv, Aug 2023. URL: https://doi.org/10.1101/2023.08.01.23292554, doi:10.1101/2023.08.01.23292554. This article has 5 citations.

11. (choi2019piezo1incorporatesmechanical pages 2-4): Dongwon Choi, Eunkyung Park, Eunson Jung, Boksik Cha, Somin Lee, James Yu, Paul M. Kim, Sunju Lee, Yeo Jin Hong, Chester J. Koh, Chang-Won Cho, Yifan Wu, Noo Li Jeon, Alex K. Wong, Laura Shin, S. Ram Kumar, Ivan Bermejo-Moreno, R. Sathish Srinivasan, Il-Taeg Cho, and Young-Kwon Hong. Piezo1 incorporates mechanical force signals into the genetic program that governs lymphatic valve development and maintenance. JCI insight, May 2019. URL: https://doi.org/10.1172/jci.insight.125068, doi:10.1172/jci.insight.125068. This article has 180 citations and is from a domain leading peer-reviewed journal.

12. (choi2019piezo1incorporatesmechanical pages 1-2): Dongwon Choi, Eunkyung Park, Eunson Jung, Boksik Cha, Somin Lee, James Yu, Paul M. Kim, Sunju Lee, Yeo Jin Hong, Chester J. Koh, Chang-Won Cho, Yifan Wu, Noo Li Jeon, Alex K. Wong, Laura Shin, S. Ram Kumar, Ivan Bermejo-Moreno, R. Sathish Srinivasan, Il-Taeg Cho, and Young-Kwon Hong. Piezo1 incorporates mechanical force signals into the genetic program that governs lymphatic valve development and maintenance. JCI insight, May 2019. URL: https://doi.org/10.1172/jci.insight.125068, doi:10.1172/jci.insight.125068. This article has 180 citations and is from a domain leading peer-reviewed journal.

13. (choi2022piezo1regulatedmechanotransductioncontrols pages 10-12): Dongwon Choi, Eunkyung Park, Roy P. Yu, Michael N. Cooper, Il-Taeg Cho, Joshua Choi, James Yu, Luping Zhao, Ji-Eun Irene Yum, Jin Suh Yu, Brandon Nakashima, Sunju Lee, Young Jin Seong, Wan Jiao, Chester J. Koh, Peter Baluk, Donald M. McDonald, Sindhu Saraswathy, Jong Y. Lee, Noo Li Jeon, Zhenqian Zhang, Alex S. Huang, Bin Zhou, Alex K. Wong, and Young-Kwon Hong. Piezo1-regulated mechanotransduction controls flow-activated lymphatic expansion. Circulation Research, Jul 2022. URL: https://doi.org/10.1161/circresaha.121.320565, doi:10.1161/circresaha.121.320565. This article has 115 citations and is from a highest quality peer-reviewed journal.

14. (cheng2025piezo1variantimplications pages 3-4): Chew W. Cheng, Sophie L. Earle, Oleksandr V. Povstyan, Chloe Randall, Katie A. Smith, Marjolaine Debant, Fraser L. Macrae, Daniel G. Beech, Anna McGrane, Fiona Bartoli, Eulashini Chuntharpursat-Bon, Richard M. Cubbon, Kathryn J. Griffin, Marc A. Bailey, Antreas C. Kalli, Lara C. Morley, Klaus K. Witte, and David J. Beech. Piezo1 variant implications for biological understanding and human health. Open Biology, Jul 2025. URL: https://doi.org/10.1098/rsob.240345, doi:10.1098/rsob.240345. This article has 11 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Lymphatic_Malformation_6-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.