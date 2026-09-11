---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:06:57.739869'
end_time: '2026-08-01T17:14:47.116071'
duration_seconds: 469.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Epithelioid Hemangioendothelioma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Epithelioid_Hemangioendothelioma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Epithelioid Hemangioendothelioma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Epithelioid Hemangioendothelioma** covering all of the
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
- **Disease Name:** Epithelioid Hemangioendothelioma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Epithelioid Hemangioendothelioma** covering all of the
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


# Epithelioid Hemangioendothelioma: Comprehensive Disease-Characteristics Report

**Evidence scope.** This synthesis prioritizes molecularly confirmed human disease, expert-center registry/consensus material, and primary mechanistic studies, especially 2022–2024. Older numerical estimates are retained when newer prospective data are unavailable. Most information is aggregated disease-level evidence rather than patient-level EHR data. The prospective EURACAN registry begun in December 2023 is designed to remedy major natural-history and treatment-evidence gaps across 21 expert centers in 10 countries. (NCT06408441 chunk 1)

| Domain | Key facts | Ontology / coding suggestions |
|---|---|---|
| Identity / classification | Epithelioid hemangioendothelioma (EHE) is an ultra-rare malignant vascular sarcoma / soft-tissue tumor of endothelial lineage; often described as a translocation-associated, YAP/TAZ-driven cancer with highly variable clinical behavior (stacchiotti2024gdf15predictsepithelioid pages 1-2, seavey2022unravelingthebiology pages 2-4, lamar2018epithelioidhemangioendotheliomaas pages 1-3) | MONDO: epithelioid hemangioendothelioma = MONDO:0015523 (from available disease-target context; verify locally). MeSH / ICD / OMIM / Orphanet: verify locally. NCIT: verify locally. |
| Epidemiology | Estimated prevalence is less than 1 per 1,000,000; EHE accounts for <1% of vascular tumors. Median/typical age at presentation is around 35-40 years, with broad reported range from 8-90 years. Female predominance has been reported (~1.5:1) (seavey2022unravelingthebiology pages 2-4, lamar2018epithelioidhemangioendotheliomaas pages 1-3) | Rare cancer category; disease-level aggregated literature and registry data, not individual EHR-derived. |
| Main sites | Most frequent sites include liver, lung, bone, and soft tissue; one review summarized liver 21%, bone 14%, lung 12%. Multifocal liver disease is a common presentation; tumors can arise in many organs/tissues (lamar2018epithelioidhemangioendotheliomaas pages 5-7, lamar2018epithelioidhemangioendotheliomaas pages 1-3) | UBERON suggestions: liver (UBERON:0002107), lung (UBERON:0002048), bone tissue (UBERON:0002481), soft tissue = verify locally. Cell type: endothelial cell (CL:0000115). |
| Defining alterations | Approx. 90% harbor WWTR1(TAZ)::CAMTA1 fusion; the remaining ~10% harbor YAP1::TFE3 fusion. In one synthesis, >90% carried WWTR1::CAMTA1 and ~45% of WWTR1::CAMTA1-positive tumors had no other genetic alterations. Secondary alterations reported in ~50% include CDKN2A/B, RB, APC, ATRX, XRCC2, FANCA (stacchiotti2024gdf15predictsepithelioid pages 1-2, seavey2022unravelingthebiology pages 2-4) | HGNC genes: WWTR1, CAMTA1, YAP1, TFE3, CDKN2A, CDKN2B, RB1, APC, ATRX, XRCC2, FANCA. Structural variant class: gene fusion / chromosomal translocation. |
| Mechanism | Fusion oncoproteins preserve TEAD-binding function and drive constitutive Hippo-pathway effector activity, producing TEAD-dependent transcription, altered chromatin regulation via the ATAC histone acetyltransferase complex, and oncogenic programs promoting proliferation, survival, migration, anchorage-independent growth, and metastasis. TAZ-CAMTA1 also signals through CTGF, integrin αIIbβ3, and Ras-MAPK; MEK inhibition suppresses fusion-driven growth. CAMTA1 contributes a nuclear-localization function that helps evade normal Hippo cytoplasmic restraint (lamar2018epithelioidhemangioendotheliomaas pages 3-5, seavey2022unravelingthebiology pages 7-8, stacchiotti2024gdf15predictsepithelioid pages 1-2) | GO suggestions: Hippo signaling (verify locally), regulation of transcription by RNA polymerase II (GO:0006357), chromatin organization (GO:0006325), cell proliferation (GO:0008283), cell migration (GO:0016477), anoikis / apoptotic process = verify locally. CL: endothelial cell (CL:0000115). |
| Diagnostic hallmarks | Diagnosis integrates morphology, endothelial differentiation, and molecular testing. WWTR1::CAMTA1 is pathognomonic/standard molecular marker; CAMTA1 immunohistochemistry can be a useful surrogate marker. YAP1::TFE3 defines a distinct subset, but TFE3 immunohistochemistry is not fully specific. Histology typically shows epithelioid endothelial cells in a prominent fibrous/myxohyaline stroma (ong2021genefusionsin pages 13-13, lamar2018epithelioidhemangioendotheliomaas pages 5-7, seavey2022unravelingthebiology pages 2-4) | Diagnostic workflow: histopathology + endothelial immunophenotype + fusion confirmation by RNA sequencing/FISH/targeted molecular assay (verify locally for assay standards). HPO / SNOMED / LOINC coding: verify locally. |
| Prognosis | Clinical course is markedly heterogeneous, from indolent disease lasting years to rapidly fatal progression within months. Review-level survival figures include median overall survival ~75 months and 1-, 3-, 5-year survival of 83.4%, 55.7%, and 41.1%, respectively. Worse outcomes are associated with pleural/peritoneal disease; isolated soft-tissue disease has more favorable 5-year survival (~87%), compared with liver (~65%) and lung (~45%). Tumor size >3 cm and >3 mitoses/HPF were associated with worse 5-year survival (59% vs 100% in one review synthesis) (lamar2018epithelioidhemangioendotheliomaas pages 3-5, seavey2022unravelingthebiology pages 2-4, lamar2018epithelioidhemangioendotheliomaas pages 1-3) | Prognostic factor concepts: pleural effusion / serosal involvement, tumor size, mitotic activity. HPO suggestions: pleural effusion (HP:0002202), ascites (HP:0001541), pain (HP:0012531), weight loss (HP:0001824). |
| Treatment | For localized disease, surgery is the mainstay and can be curative for solitary lesions. Conventional chemotherapy is generally considered less effective in EHE than in angiosarcoma. Targeted/systemic approaches under study or use include sirolimus, trametinib, pazopanib, sorafenib, eribulin, and local ablative/interventional strategies in selected hepatic disease. In preclinical comparison, sirolimus showed greater antitumor activity than doxorubicin; in older case-series summaries, sirolimus showed prolonged benefit in a subset of patients (stacchiotti2024gdf15predictsepithelioid pages 1-2, stacchiotti2024gdf15predictsepithelioid pages 9-9, lamar2018epithelioidhemangioendotheliomaas pages 5-7, lamar2018epithelioidhemangioendotheliomaas pages 7-8) | NCIT intervention suggestions: Surgical Resection, Sirolimus, Trametinib, Pazopanib, Sorafenib, Eribulin, Doxorubicin, Liver Transplantation, Ablation (verify locally for exact NCIT IDs). Clinical trials: trametinib NCT03148275; eribulin NCT03331250; nab-sirolimus NCT07104331; albumin-bound sirolimus NCT07684287 (NCT03148275 chunk 3). |
| Emerging biomarker | Circulating GDF-15 is a 2024 candidate biomarker of aggressiveness and treatment monitoring. In two cohorts, GDF-15 was significantly higher in EHE than controls (P<0.001 in both), highest in higher-risk disease (P=0.006 retrospective; P=0.002 prospective), and correlated with aggressiveness. Example longitudinal values rose from 6,792 to 11,475 pg/mL with progression and fell to 4,064 pg/mL with sirolimus-induced stability (stacchiotti2024gdf15predictsepithelioid pages 11-12) | CHEBI / protein identifier coding: GDF-15 verify locally. Biomarker type: circulating protein biomarker. |
| Models | Strong model evidence now exists: (1) genetically engineered conditional Wwtr1-Camta1 mouse models showing that the fusion is sufficient to drive bona fide EHE; (2) Tet-Off overexpression mouse systems generating postnatal lesions; (3) NIH3T3 transformed-cell and xenograft models for mechanistic work; (4) 2024 patient-derived xenograft and matched cell line retaining WWTR1::CAMTA1 and tumor genomic/transcriptomic features (seavey2022unravelingthebiology pages 7-8, stacchiotti2024gdf15predictsepithelioid pages 1-2) | Evidence types: in vitro, xenograft, genetically engineered mouse, patient-derived xenograft. Model organism: mouse (NCBI Taxon:10090). |
| Prevention | No established primary prevention, population screening, or protective-factor evidence is currently supported. EHE is largely fusion-driven, usually somatic, with no validated inherited predisposition pattern or confirmed environmental cause in the cited evidence. Prevention emphasis is therefore tertiary: expert pathology review, accurate fusion testing, surveillance of known disease, and management of complications (stacchiotti2024gdf15predictsepithelioid pages 1-2, lamar2018epithelioidhemangioendotheliomaas pages 1-3) | Prevention coding: verify locally. Genetic counseling may be considered case-by-case, but routine hereditary screening is not evidence-based from available sources. |


*Table: This table condenses the highest-yield disease characteristics of epithelioid hemangioendothelioma for knowledge-base use, including defining fusions, mechanism, prognosis, treatment, and emerging biomarker evidence. It highlights exact reported percentages and flags ontology or coding elements that should be verified locally before database ingestion.*

## 1. Disease information

### Definition

Epithelioid hemangioendothelioma (EHE) is an ultra-rare, translocation-associated malignant vascular sarcoma showing endothelial differentiation. It can arise almost anywhere, but liver, lung, bone, and soft tissue are especially frequent. Its behavior ranges from prolonged radiographic stability or spontaneous regression to rapidly fatal metastatic disease. (stacchiotti2024gdf15predictsepithelioid pages 1-2, NCT06408441 chunk 1)

### Identifiers and terminology

- **MONDO:** **MONDO:0015523**.
- **Common names:** epithelioid hemangioendothelioma; epithelioid haemangioendothelioma; EHE; hepatic EHE/HEHE; pulmonary EHE/PEH when site-qualified.
- **Historical term:** intravascular bronchioloalveolar tumor, formerly used for pulmonary EHE.
- **MeSH:** *Hemangioendothelioma, Epithelioid*; exact current identifier should be verified against the release used by the knowledge base.
- **Orphanet, OMIM, ICD-10/ICD-11:** release-specific codes were not reliably present in the retrieved primary literature and should be resolved directly against current terminology services. EHE is a somatic neoplasm, not a classic Mendelian phenotype; an OMIM disease entry should not be assumed.
- **Coding caution:** ICD-10-CM often cannot represent EHE histology independently of anatomical site. Cancer-registry coding should combine topography with the applicable ICD-O morphology code after verification against the current ICD-O release.

Open Targets recognizes EHE as MONDO:0015523 but returned no disease-specific target associations; angiosarcoma associations must not be transferred to EHE because these are biologically distinct entities. (OpenTargets Search: epithelioid hemangioendothelioma)

## 2. Etiology, risk, and protective factors

### Causal lesion

EHE is principally caused by an acquired **somatic structural rearrangement**, not by inherited pathogenic variation:

1. Approximately 90% of tumors harbor **WWTR1::CAMTA1**, generated classically by **t(1;3)(p36;q25)**.
2. A minority historically classified as EHE harbor **YAP1::TFE3**. Some contemporary experts recommend calling these *YAP1::TFE3-fused hemangioendothelioma* because their morphology and biology differ from classic WWTR1::CAMTA1-positive EHE. (stacchiotti2024gdf15predictsepithelioid pages 1-2, ma2022thetazcamta1fusion pages 1-2)

The reported proportions vary with classification and assay—approximately 80–>90% for WWTR1::CAMTA1 and roughly 10–12% for YAP1::TFE3—so frequencies should be interpreted in the context of diagnostic criteria. (ong2021genefusionsin pages 8-10, stacchiotti2024gdf15predictsepithelioid pages 1-2)

### Risk and protective factors

No validated inherited susceptibility allele, founder mutation, carrier state, family-history effect, infectious trigger, occupational exposure, toxin, smoking/alcohol association, dietary determinant, or protective lifestyle factor has been established. The recognized arsenic, vinyl chloride, thorium dioxide, radiation, and chronic-lymphedema risks for **angiosarcoma** should not be attributed to EHE. No reproducible gene–environment interaction is known. Accordingly, penetrance, anticipation, germline mosaicism, consanguinity, and carrier frequency are not applicable to the usual somatic EHE mechanism.

## 3. Phenotypes and quality-of-life effects

EHE usually begins in adulthood, around the mid-30s to 40 years, but the reported range extends from childhood to advanced age (approximately 8–90 years). About 25–33% of patients may be asymptomatic and diagnosed incidentally. (seavey2022unravelingthebiology pages 2-4, lamar2018epithelioidhemangioendotheliomaas pages 1-3)

| Phenotype | Type, course, and impact | Suggested HPO term |
|---|---|---|
| Pain, including tumor or bone pain | Symptom; site-dependent, variable; can impair mobility, sleep, and work and may trigger systemic treatment | Pain, HP:0012531; Bone pain, HP:0002653 |
| Weight loss/anorexia/fatigue | Constitutional symptoms; associated systemic deterioration is concerning for aggressive disease | Weight loss, HP:0001824; Feeding/appetite abnormality and Fatigue—verify release |
| Cough, dyspnea, chest pain | Pulmonary/pleural manifestations; severity ranges from mild to respiratory compromise | Cough, HP:0012735; Dyspnea, HP:0002094; Chest pain, HP:0100749 |
| Pleural or peritoneal effusion/ascites | Clinical/imaging sign; progressive serosal disease is a major adverse feature | Pleural effusion, HP:0002202; Ascites, HP:0001541 |
| Hepatomegaly/right-upper-quadrant discomfort | Hepatic manifestation; may remain indolent or progress to portal/hepatic dysfunction | Hepatomegaly, HP:0002240; Abdominal pain, HP:0002027 |
| Pathologic fracture or impaired mobility | Bone disease; uncommon overall but potentially severe | Pathologic fracture, HP:0002756; Abnormality of mobility—verify release |
| Anemia | Laboratory abnormality; prospectively unvalidated but retrospectively associated with worse advanced disease | Anemia, HP:0001903 |
| Multifocal/metastatic lesions | Imaging/pathologic phenotype rather than symptom; lung, liver, and bone are common compartments | Neoplasm/metastatic disease terms should be drawn from NCIT/SNOMED rather than forced into HPO |

The NCI trametinib study formally incorporated PROMIS global health, pain intensity, pain interference, and pain behavior, reflecting clinically important quality-of-life burdens. However, disease-specific validated EHE quality-of-life norms remain limited. (NCT03148275 chunk 1)

## 4. Genetic and molecular information

### Principal alterations

- **WWTR1** encodes TAZ, a Hippo-pathway transcriptional coactivator; **CAMTA1** supplies nuclear localization and transcription/chromatin-regulatory functions. The fusion is a somatic, activating structural variant rather than a conventional ACMG germline SNV. It is therefore best classified as an **oncogenic/pathogenic somatic fusion** rather than assigned a germline ACMG category.
- **YAP1::TFE3** is another activating somatic fusion involving the YAP Hippo effector.
- Population allele frequency in gnomAD/1000 Genomes is not meaningful for tumor-specific chromosomal fusions; they are expected to be absent from normal-population germline datasets.
- Secondary alterations occur in about half of tumors in some series and include **CDKN2A/CDKN2B, RB1, APC, ATRX, XRCC2,** and **FANCA**. Approximately 45% of WWTR1::CAMTA1-positive tumors in one synthesis had no other detected alteration, underscoring the fusion’s sufficiency. (seavey2022unravelingthebiology pages 7-8, stacchiotti2024gdf15predictsepithelioid pages 1-2)

No clinically validated modifier gene is established. Loss of cell-cycle restraints such as CDKN2A is biologically plausible as a progression event, but currently does not define routine genotype-guided care.

### Epigenetic/chromatin biology

Both fusion proteins recruit the **Ada2a-containing histone acetyltransferase (ATAC) complex**, including YEATS2 and ZZZ3, while hyperactivating TEAD-dependent transcription. This is functional chromatin dysregulation rather than a validated diagnostic DNA-methylation signature. ATAC-complex depletion inhibits anchorage-independent growth in fusion-transformed cells, making the complex a candidate therapeutic vulnerability. (seavey2022unravelingthebiology pages 7-8, stacchiotti2024gdf15predictsepithelioid pages 1-2)

## 5. Environmental and infectious information

No specific environmental, lifestyle, occupational, radiation, medication, or infectious cause has been demonstrated for EHE. Apparent hormonal or female-sex associations remain descriptive and do not establish causation. No pathogen is implicated, and the disease is neither communicable nor zoonotic.

## 6. Mechanism and pathophysiology

### Causal chain

**Somatic rearrangement → fusion transcriptional coactivator → constitutive nuclear YAP/TAZ-like activity → TEAD-dependent transcription plus ATAC-mediated chromatin remodeling → survival, proliferation, migration, anoikis resistance, fibromyxoid-stroma production, and metastatic competence → organ-specific nodules, pain, effusions, and organ dysfunction.**

Mechanistically, TAZ–CAMTA1 retains the TAZ TEAD-binding region, loses normal C-terminal regulatory elements, and gains CAMTA1-mediated nuclear localization. Consequently, normal Hippo/LATS phosphorylation does not efficiently impose cytoplasmic restraint. (lamar2018epithelioidhemangioendotheliomaas pages 3-5, ma2022thetazcamta1fusion pages 1-2)

A second experimentally supported branch is:

**TAZ–CAMTA1 → CTGF induction → CTGF binding integrin αIIbβ3 → RAS–MAPK activation → anchorage-independent growth and xenograft expansion.** CTGF knockdown or MEK inhibition with PD0325901/trametinib suppressed growth in transformed NIH3T3 cultures and xenografts. This provided the rationale for phase II trametinib trial NCT03148275. The article’s abstract states: **“CTGF and the Ras-MAPK signaling cascade are essential for TC-mediated tumorigenesis.”** (PMID **35443056**; published April 2022; DOI: https://doi.org/10.1158/1078-0432.CCR-22-0421). (ma2022thetazcamta1fusion pages 1-2)

### mTOR and GDF-15

The 2024 study identified tumor-derived **GDF-15** as a candidate aggressiveness biomarker. Sirolimus inhibited 4E-BP1 phosphorylation, reduced ATF4/ATF5, and lowered GDF-15 expression/release. In two human cohorts, GDF-15 was higher in EHE than controls (both **P<0.001**), highest in higher-risk disease (**P=0.006** retrospective; **P=0.002** prospective), and correlated with aggressiveness. In one longitudinal example, levels rose from **6,792 to 11,475 pg/mL** during progression and fell to **4,064 pg/mL** with sirolimus-associated stability. This remains a candidate—not yet validated or regulatory-qualified—biomarker. (stacchiotti2024gdf15predictsepithelioid pages 9-9, stacchiotti2024gdf15predictsepithelioid pages 11-12)

The 2024 abstract states: **“This study identifies GDF-15 as a novel biomarker of EHE aggressiveness”** and reports “markedly higher antitumor activity” for sirolimus than doxorubicin in experimental models (published September 2024; DOI: https://doi.org/10.1158/1078-0432.CCR-23-3991). (stacchiotti2024gdf15predictsepithelioid pages 1-2)

### Molecular-profile and ontology suggestions

- **GO biological processes:** Hippo signaling; regulation of transcription by RNA polymerase II (GO:0006357); chromatin organization (GO:0006325); histone acetylation (GO:0016573); cell proliferation (GO:0008283); cell migration (GO:0016477); MAPK cascade (GO:0000165); angiogenesis (GO:0001525); apoptotic signaling/anoikis—verify current term.
- **Cell Ontology:** endothelial cell (CL:0000115); vascular endothelial cell and organ-specific endothelial subtypes should be added when supported by specimen location.
- **GO cellular components:** nucleus (GO:0005634), chromatin (GO:0000785), transcription-regulator complex (GO:0005667).
- Robust EHE metabolomic, lipidomic, spatial-transcriptomic, and single-cell atlases are not yet established. Current multi-omic evidence is primarily bulk genomic/transcriptomic and proteomic/chromatin-interaction work.

## 7. Anatomy

Primary or multifocal disease most often affects **liver (UBERON:0002107), lung (UBERON:0002048), bone tissue (UBERON:0002481), and soft/connective tissue**. Pleura, peritoneum, mediastinum, skin, central nervous system, head and neck, and other viscera can also be involved. One literature synthesis reported liver 21%, bone 14%, and lung 12%, but these estimates are referral- and classification-sensitive. (lamar2018epithelioidhemangioendotheliomaas pages 1-3)

EHE arises from endothelial-lineage cells within connective/vascular tissue. At the subcellular level, the defining dysfunction is nuclear localization of fusion coactivators and altered chromatin/transcriptional complexes. Disease may be unifocal, multifocal within one organ/compartment, or systemic; there is no characteristic lateralization. (NCT06408441 chunk 1)

## 8. Temporal development and natural history

Onset is generally insidious. There is no universal AJCC stage system specific to EHE; practical grouping is **localized/unifocal**, **locoregional or multifocal single-compartment**, and **systemic metastatic** disease. The disease may remain stable untreated, slowly progress over years, spontaneously regress rarely, or become rapidly fatal. (NCT06408441 chunk 1)

Because a radiographic change can be slow and conventional therapy has toxicity, experts often use an initial observation interval for asymptomatic advanced disease. Symptomatic deterioration, objective progression, anemia, or new serosal involvement/effusion constitutes an important window to reconsider systemic therapy. Prospective validation is ongoing in EURACAN’s registry, which mandates six-monthly updates when no event occurs. (NCT06408441 chunk 1)

## 9. Inheritance and population epidemiology

The best recent disease-specific estimate cited by the EURACAN registry is an incidence of **0.038 per 100,000 person-years**—approximately 0.38 per million/year. Prevalence has been described as below one per million, although estimates are uncertain because of historical misclassification and long survival in indolent cases. (wiegand2021malignantvasculartumors pages 7-9, NCT06408441 chunk 1)

Typical age is approximately 35–40 years, with a wide 8–90-year range. A female predominance around **1.5:1** has been reported, although site-specific cohorts differ. No reproducible ethnic, geographic, or founder distribution is established. (seavey2022unravelingthebiology pages 2-4, lamar2018epithelioidhemangioendotheliomaas pages 1-3)

EHE is not ordinarily inherited: no autosomal-dominant, recessive, X-linked, mitochondrial, or polygenic pattern is established. Thus penetrance, carrier frequency, prenatal diagnosis, cascade testing, and preimplantation testing are generally not applicable.

## 10. Diagnostics

### Recommended workflow

1. **Imaging and staging:** contrast-enhanced CT of chest/abdomen/pelvis; liver MRI for hepatic disease; MRI for soft-tissue/bone disease; targeted bone imaging or PET/CT when clinically indicated. Pulmonary EHE often presents as multiple nodules and/or pleural thickening. Hepatic EHE commonly presents as multifocal peripheral nodules, sometimes calcified, with peripheral enhancement and the radiologic “lollipop sign.” MRI generally shows low/intermediate T1 and high T2 signal with enhancement. (lamar2018epithelioidhemangioendotheliomaas pages 3-5, wiegand2021malignantvasculartumors pages 7-9)
2. **Core biopsy/excision reviewed by an expert sarcoma pathologist.** Histology typically shows cords, strands, or nests of epithelioid endothelial cells in dense myxohyaline stroma; intracytoplasmic lumina/vacuoles may represent primitive vascular differentiation. (seavey2022unravelingthebiology pages 2-4)
3. **Immunohistochemistry:** CD31/PECAM1 and ERG are strong endothelial markers; CD34 and FLI1 are commonly supportive. Nuclear CAMTA1 is a useful surrogate for WWTR1::CAMTA1. TFE3 staining is insufficiently specific and should be molecularly verified. (lamar2018epithelioidhemangioendotheliomaas pages 3-5, wiegand2021malignantvasculartumors pages 7-9, ong2021genefusionsin pages 8-10)
4. **Molecular confirmation:** fusion FISH, targeted RNA sequencing, anchored multiplex RNA assay, RT-PCR when breakpoints/transcripts are covered, or whole-transcriptome sequencing. A negative CAMTA1/FISH assay in morphologically convincing disease should prompt an RNA-based fusion assay rather than automatically excluding EHE. (seavey2022unravelingthebiology pages 2-4)

The NCI trametinib trial required histologically confirmed disease and tissue for fusion FISH, illustrating real-world integration of molecular confirmation into prospective research. (NCT03148275 chunk 2)

### Differential diagnosis

Important alternatives are epithelioid angiosarcoma, epithelioid hemangioma, pseudomyogenic hemangioendothelioma, metastatic carcinoma, melanoma, myoepithelial neoplasm, and other epithelioid sarcomas. Marked atypia, destructive vasoformation, brisk mitoses, and necrosis favor angiosarcoma; keratins alone cannot establish carcinoma because vascular tumors may show focal epithelial-marker expression. Fusion confirmation is decisive in difficult cases. (lamar2018epithelioidhemangioendotheliomaas pages 3-5, seavey2022unravelingthebiology pages 2-4)

Routine blood tests are nonspecific; CBC, liver/renal function, inflammatory indices, hemoglobin, and fibrinogen are useful for burden, safety, and longitudinal assessment. GDF-15, CTGF, CRP, and ESR remain investigational. There is no population, newborn, carrier, or hereditary-family screening program. Liquid biopsy, WES/WGS, CMA, karyotyping, mitochondrial testing, and repeat-expansion testing are not routine first-line diagnostics; RNA-based fusion detection is generally more directly informative.

## 11. Outcome and prognosis

Clinical outcome is heterogeneous. Review-level estimates include median overall survival around **75 months** and 1-, 3-, and 5-year survival of **83.4%, 55.7%, and 41.1%**, respectively; these pooled historical figures should not be treated as individualized predictions. Reported 5-year survival differs by compartment—approximately **87%** for isolated soft tissue, **65%** with liver involvement, and **45%** with lung involvement. (lamar2018epithelioidhemangioendotheliomaas pages 3-5, lamar2018epithelioidhemangioendotheliomaas pages 5-7, seavey2022unravelingthebiology pages 2-4)

In one risk synthesis, tumors >3 cm and >3 mitoses per high-power field were associated with 5-year survival of 59%, versus 100% without those features. Recurrence after treatment was approximately 15%, and regional metastasis 20–30%, although estimates vary by site and cohort. (lamar2018epithelioidhemangioendotheliomaas pages 3-5)

The most clinically persuasive adverse pattern is **serosal/pleural or peritoneal involvement, especially effusion**, systemic symptom deterioration, and anemia; prospective confirmation remains pending. Other reported adverse associations include older age, male sex, pulmonary or multiorgan disease, larger size, and higher mitotic activity. (wiegand2021malignantvasculartumors pages 7-9, NCT06408441 chunk 1)

Morbidity includes chronic pain, dyspnea, effusions, impaired mobility/fracture, liver dysfunction, repeated imaging and procedures, treatment toxicity, and uncertainty from an unpredictable course. Recovery is plausible after complete local treatment, but disseminated disease is usually chronic and requires long-term surveillance.

## 12. Treatment and real-world implementation

### Strategy

- **Localized resectable disease:** complete surgery is preferred; expected cure is approximately **70–80%** in the EURACAN protocol summary. There is no proven routine adjuvant systemic therapy or radiotherapy. (NCT06408441 chunk 1)
- **Asymptomatic stable advanced disease:** active surveillance is often preferred to avoid overtreatment.
- **Progressive, symptomatic, organ-threatening, or serosa-involving disease:** systemic treatment and/or site-directed intervention should be decided by a multidisciplinary sarcoma center.
- **Hepatic disease:** resection, transplantation, ablation, or embolization may be considered in selected patients; extrahepatic disease does not automatically preclude transplantation in all historical series, but selection is highly specialized. (lamar2018epithelioidhemangioendotheliomaas pages 5-7)
- **Radiotherapy:** may provide local control or palliation in selected unresectable, painful, or osseous lesions; evidence is retrospective.

### Systemic therapies

**Sirolimus/other mTOR inhibition.** Sirolimus has the strongest recurrent disease-specific activity signal and is often regarded by experts as a preferred systemic option for progressive EHE, particularly without severe serosal effusion. It is off-label in many jurisdictions. The 2024 PDX study found an in-vitro IC50 of **0.03 ± 0.03 μmol/L** for sirolimus versus **0.10 ± 0.04 μmol/L** for doxorubicin and superior experimental antitumor activity; this comparison is preclinical and cannot establish clinical superiority. (stacchiotti2024gdf15predictsepithelioid pages 9-9, stacchiotti2024gdf15predictsepithelioid pages 1-2)

**Trametinib.** The mechanistic rationale is CTGF–RAS–MAPK dependence. NCT03148275/SARC033 was a completed, single-arm phase II trial of oral trametinib in **44** patients with unresectable/metastatic EHE; primary outcome was RECIST 1.1 response, with PFS, OS, toxicity, PROMIS measures, CTGF, inflammatory markers, fusion status, and MAPK activity assessed. Registry results were first posted November 26, 2024; because exact efficacy values were not captured in the retrieved evidence, they are not inferred here. (NCT03148275 chunk 1, NCT03148275 chunk 2)

**Conventional chemotherapy.** Anthracycline-based and other cytotoxic regimens generally show marginal activity and are not interchangeable with angiosarcoma treatment. Doxorubicin, taxanes, carboplatin, and other sarcoma regimens may still be considered in exceptional rapidly progressive cases, but expectations should be modest. (lamar2018epithelioidhemangioendotheliomaas pages 7-8, NCT06408441 chunk 1)

**Antiangiogenic/targeted agents.** Pazopanib and sorafenib have produced prolonged stable disease or occasional responses in reports and small series, but no universally accepted standard exists. Immunotherapy, gene therapy, RNA therapy, CAR-T/cell therapy, and fusion-directed editing remain experimental without established efficacy.

**Eribulin.** NCT03331250 is a pilot, open-label phase II study of 13 total angiosarcoma/EHE participants, with no more than five EHE patients planned. Eribulin inhibits microtubule function; disease-specific conclusions are necessarily limited by the tiny EHE subgroup. (NCT03331250 chunk 1)

**Current research infrastructure.** The prospective EURACAN registry (NCT06408441) began enrolling molecularly confirmed new cases in December 2023, targeting 100 participants and longitudinally recording symptoms, pain, blood tests, serosal disease, imaging, surveillance, and treatment outcomes. (NCT06408441 chunk 1)

Suggested **NCIT intervention concepts** include Surgical Resection, Active Surveillance, Liver Transplantation, Radiation Therapy, Ablation, Sirolimus, Trametinib, Pazopanib, Sorafenib, Eribulin, and Doxorubicin; exact NCIT identifiers should be resolved against the current thesaurus. Pharmacogenomic dosing rules specific to EHE are not established.

## 13. Prevention

There is no evidence-based primary prevention because no modifiable cause is known. No vaccine, prophylactic drug, population screening test, hereditary cascade program, or validated high-risk population exists. Secondary prevention is therefore limited to prompt expert evaluation of suspicious lesions and accurate fusion testing. Tertiary prevention includes surveillance, early management of effusions and organ compromise, pain control, fracture prevention/rehabilitation for bone disease, nutrition support, and avoidance of unnecessary toxic treatment in stable disease.

## 14. Natural disease in other species

Naturally occurring vascular tumors called hemangioendothelioma have been described in veterinary pathology, but the retrieved evidence does not establish a spontaneous nonhuman disease molecularly homologous to human WWTR1::CAMTA1 EHE. No breed association, VBO term, cross-species transmission, or zoonotic potential is established. Orthologous **Wwtr1, Camta1, Yap1,** and **Tfe3** genes are conserved, but conservation alone does not prove natural EHE equivalence.

## 15. Model organisms and experimental systems

1. **Conditional knock-in mouse (Mus musculus; NCBI Taxon 10090):** Wwtr1-Camta1 expressed from the endogenous locus after Cre activation produces tumors clinically, histologically, immunohistochemically, genetically, and transcriptionally resembling human EHE. No other tumor type was observed, demonstrating fusion sufficiency and tissue specificity. The abstract states that the tumors were **“indistinguishable from human EHE clinically, histologically, immunohistochemically, and genetically.”** (published March 2021; DOI: https://doi.org/10.1101/gad.348220.120). (seavey2022unravelingthebiology pages 7-8)
2. **Tet-Off mouse:** postnatal fusion expression creates hyperplastic pulmonary lesions; doxycycline re-administration causes involution, supporting continued oncogene dependence. Embryonic expression is lethal, limiting developmental modeling. (seavey2022unravelingthebiology pages 7-8)
3. **NIH3T3/TAZ-CAMTA1 cells and xenografts:** reproduce anchorage-independent growth and enabled identification of CTGF–integrin αIIbβ3–RAS–MAPK signaling and trametinib sensitivity. Limitation: fibroblast-derived transformed cells are not native human EHE endothelium. (ma2022thetazcamta1fusion pages 1-2)
4. **2024 EHE PDX and paired cell line:** derived from aggressive WWTR1::CAMTA1-positive disease and retained original histomorphology plus genomic/transcriptomic profiles. This model enabled sirolimus–doxorubicin comparison and GDF-15 studies. Limitation: one aggressive donor cannot represent the full clinical spectrum. (stacchiotti2024gdf15predictsepithelioid pages 1-2)

No mature zebrafish, Drosophila, organoid, or iPSC model was supported by the retrieved evidence. The mouse and PDX systems are currently the most disease-faithful preclinical resources.

## Expert interpretation and evidence gaps

EHE should be treated as a **fusion-defined YAP/TAZ-driven sarcoma**, not as a low-grade angiosarcoma. Molecular confirmation is central because morphology and clinical tempo overlap with benign vascular tumors, carcinoma, and aggressive angiosarcoma. Surgery can cure localized disease; observation is often appropriate for stable asymptomatic metastatic disease; and mTOR inhibition currently has the strongest recurring disease-specific clinical signal, while MEK and direct YAP/TAZ–TEAD or chromatin-complex inhibition remain rational investigational strategies. (stacchiotti2024gdf15predictsepithelioid pages 1-2, NCT06408441 chunk 1, ma2022thetazcamta1fusion pages 1-2)

The most important unresolved issues are prospective natural-history stratification, validated response criteria for very slow-growing disease, treatment efficacy in serosal/effusion-positive EHE, validation of GDF-15 and CTGF, and molecular distinction of YAP1::TFE3 tumors. The EURACAN registry directly addresses several of these gaps, but its completion is projected for 2033. (NCT06408441 chunk 1)

References

1. (NCT06408441 chunk 1): Annalisa Trama. The Epithelioid Hemangioendothelioma Registry of the European Reference Network on Rare Adult Solid Cancers (EURACAN). Fondazione IRCCS Istituto Nazionale dei Tumori, Milano. 2023. ClinicalTrials.gov Identifier: NCT06408441

2. (stacchiotti2024gdf15predictsepithelioid pages 1-2): Silvia Stacchiotti, Silvia Martini, Sandro Pasquali, Anna M. Frezza, Alessia Beretta, Stefano Percio, Mara Lecchi, Monica Tortoreto, Marta Barisella, Paola Collini, Gian Paolo Dagrada, Alessandra Merlini, Paul H. Huang, Andrew Jenks, Robin L. Jones, William D. Tap, Matilde Ingrosso, Carlo Morosi, Silvia Brich, Claudia Giani, Paolo Verderio, Paolo G. Casali, Hugh Leonard, Alessandro Gronchi, Valentina Zuco, and Nadia Zaffaroni. Gdf-15 predicts epithelioid hemangioendothelioma aggressiveness and is downregulated by sirolimus through atf4/atf5 suppression. Sep 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-3991, doi:10.1158/1078-0432.ccr-23-3991. This article has 13 citations and is from a highest quality peer-reviewed journal.

3. (seavey2022unravelingthebiology pages 2-4): Caleb Seavey, Ajaybabu Pobbati, and Brian Rubin. Unraveling the biology of epithelioid hemangioendothelioma, a taz–camta1 fusion driven sarcoma. Cancers, 14:2980, Jun 2022. URL: https://doi.org/10.3390/cancers14122980, doi:10.3390/cancers14122980. This article has 22 citations.

4. (lamar2018epithelioidhemangioendotheliomaas pages 1-3): John M. Lamar, Vijeyaluxmy Motilal Nehru, and Guy Weinberg. Epithelioid hemangioendothelioma as a model of yap/taz-driven cancer: insights from a rare fusion sarcoma. Cancers, 10:229, Jul 2018. URL: https://doi.org/10.3390/cancers10070229, doi:10.3390/cancers10070229. This article has 47 citations.

5. (lamar2018epithelioidhemangioendotheliomaas pages 5-7): John M. Lamar, Vijeyaluxmy Motilal Nehru, and Guy Weinberg. Epithelioid hemangioendothelioma as a model of yap/taz-driven cancer: insights from a rare fusion sarcoma. Cancers, 10:229, Jul 2018. URL: https://doi.org/10.3390/cancers10070229, doi:10.3390/cancers10070229. This article has 47 citations.

6. (lamar2018epithelioidhemangioendotheliomaas pages 3-5): John M. Lamar, Vijeyaluxmy Motilal Nehru, and Guy Weinberg. Epithelioid hemangioendothelioma as a model of yap/taz-driven cancer: insights from a rare fusion sarcoma. Cancers, 10:229, Jul 2018. URL: https://doi.org/10.3390/cancers10070229, doi:10.3390/cancers10070229. This article has 47 citations.

7. (seavey2022unravelingthebiology pages 7-8): Caleb Seavey, Ajaybabu Pobbati, and Brian Rubin. Unraveling the biology of epithelioid hemangioendothelioma, a taz–camta1 fusion driven sarcoma. Cancers, 14:2980, Jun 2022. URL: https://doi.org/10.3390/cancers14122980, doi:10.3390/cancers14122980. This article has 22 citations.

8. (ong2021genefusionsin pages 13-13): Sheena L. M. Ong, Karoly Szuhai, and Judith V.M.G. Bovée. Gene fusions in vascular tumors and their underlying molecular mechanisms. Expert Review of Molecular Diagnostics, 21:897-909, Aug 2021. URL: https://doi.org/10.1080/14737159.2021.1950533, doi:10.1080/14737159.2021.1950533. This article has 14 citations and is from a peer-reviewed journal.

9. (stacchiotti2024gdf15predictsepithelioid pages 9-9): Silvia Stacchiotti, Silvia Martini, Sandro Pasquali, Anna M. Frezza, Alessia Beretta, Stefano Percio, Mara Lecchi, Monica Tortoreto, Marta Barisella, Paola Collini, Gian Paolo Dagrada, Alessandra Merlini, Paul H. Huang, Andrew Jenks, Robin L. Jones, William D. Tap, Matilde Ingrosso, Carlo Morosi, Silvia Brich, Claudia Giani, Paolo Verderio, Paolo G. Casali, Hugh Leonard, Alessandro Gronchi, Valentina Zuco, and Nadia Zaffaroni. Gdf-15 predicts epithelioid hemangioendothelioma aggressiveness and is downregulated by sirolimus through atf4/atf5 suppression. Sep 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-3991, doi:10.1158/1078-0432.ccr-23-3991. This article has 13 citations and is from a highest quality peer-reviewed journal.

10. (lamar2018epithelioidhemangioendotheliomaas pages 7-8): John M. Lamar, Vijeyaluxmy Motilal Nehru, and Guy Weinberg. Epithelioid hemangioendothelioma as a model of yap/taz-driven cancer: insights from a rare fusion sarcoma. Cancers, 10:229, Jul 2018. URL: https://doi.org/10.3390/cancers10070229, doi:10.3390/cancers10070229. This article has 47 citations.

11. (NCT03148275 chunk 3):  Trametinib in Treating Patients With Epithelioid Hemangioendothelioma That is Metastatic, Locally Advanced, or Cannot Be Removed by Surgery. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT03148275

12. (stacchiotti2024gdf15predictsepithelioid pages 11-12): Silvia Stacchiotti, Silvia Martini, Sandro Pasquali, Anna M. Frezza, Alessia Beretta, Stefano Percio, Mara Lecchi, Monica Tortoreto, Marta Barisella, Paola Collini, Gian Paolo Dagrada, Alessandra Merlini, Paul H. Huang, Andrew Jenks, Robin L. Jones, William D. Tap, Matilde Ingrosso, Carlo Morosi, Silvia Brich, Claudia Giani, Paolo Verderio, Paolo G. Casali, Hugh Leonard, Alessandro Gronchi, Valentina Zuco, and Nadia Zaffaroni. Gdf-15 predicts epithelioid hemangioendothelioma aggressiveness and is downregulated by sirolimus through atf4/atf5 suppression. Sep 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-3991, doi:10.1158/1078-0432.ccr-23-3991. This article has 13 citations and is from a highest quality peer-reviewed journal.

13. (OpenTargets Search: epithelioid hemangioendothelioma): Open Targets Query (epithelioid hemangioendothelioma, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

14. (ma2022thetazcamta1fusion pages 1-2): Shuang Ma, Ryan Kanai, Ajaybabu V. Pobbati, Shuo Li, Kepeng Che, Caleb N. Seavey, Andrea Hallett, Ashley Burtscher, John M. Lamar, and Brian P. Rubin. The taz-camta1 fusion protein promotes tumorigenesis via connective tissue growth factor and ras–mapk signaling in epithelioid hemangioendothelioma. Clinical Cancer Research, 28:3116-3126, Apr 2022. URL: https://doi.org/10.1158/1078-0432.ccr-22-0421, doi:10.1158/1078-0432.ccr-22-0421. This article has 37 citations and is from a highest quality peer-reviewed journal.

15. (ong2021genefusionsin pages 8-10): Sheena L. M. Ong, Karoly Szuhai, and Judith V.M.G. Bovée. Gene fusions in vascular tumors and their underlying molecular mechanisms. Expert Review of Molecular Diagnostics, 21:897-909, Aug 2021. URL: https://doi.org/10.1080/14737159.2021.1950533, doi:10.1080/14737159.2021.1950533. This article has 14 citations and is from a peer-reviewed journal.

16. (NCT03148275 chunk 1):  Trametinib in Treating Patients With Epithelioid Hemangioendothelioma That is Metastatic, Locally Advanced, or Cannot Be Removed by Surgery. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT03148275

17. (wiegand2021malignantvasculartumors pages 7-9): Susanne Wiegand, Andreas Dietz, and Gunnar Wichmann. Malignant vascular tumors of the head and neck—which type of therapy works best? Cancers, 13:6201, Dec 2021. URL: https://doi.org/10.3390/cancers13246201, doi:10.3390/cancers13246201. This article has 16 citations.

18. (NCT03148275 chunk 2):  Trametinib in Treating Patients With Epithelioid Hemangioendothelioma That is Metastatic, Locally Advanced, or Cannot Be Removed by Surgery. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT03148275

19. (NCT03331250 chunk 1): Gregory Cote. Eribulin in Angiosarcoma and Epithelioid Hemangioendothelioma (EHE). Massachusetts General Hospital. 2018. ClinicalTrials.gov Identifier: NCT03331250

## Artifacts

- [Edison artifact artifact-00](Epithelioid_Hemangioendothelioma-deep-research-falcon_artifacts/artifact-00.md)