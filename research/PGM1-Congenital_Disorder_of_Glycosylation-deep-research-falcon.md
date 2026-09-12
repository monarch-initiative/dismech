---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:08:50.223670'
end_time: '2026-08-01T17:17:03.063741'
duration_seconds: 492.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PGM1-Congenital Disorder of Glycosylation
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
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PGM1-Congenital_Disorder_of_Glycosylation-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PGM1-Congenital Disorder of Glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PGM1-Congenital Disorder of Glycosylation** covering all of the
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
- **Disease Name:** PGM1-Congenital Disorder of Glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PGM1-Congenital Disorder of Glycosylation** covering all of the
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


# PGM1-Congenital Disorder of Glycosylation: Disease-Characteristics Report

## Executive summary

PGM1-congenital disorder of glycosylation (PGM1-CDG) is an ultra-rare, autosomal-recessive, treatable disorder of both carbohydrate metabolism and protein glycosylation. Biallelic pathogenic variants in **PGM1** reduce phosphoglucomutase-1 activity, disrupting interconversion of glucose-1-phosphate and glucose-6-phosphate. This impairs glycogen synthesis/mobilization, glycolytic energy supply, UDP-glucose/UDP-galactose production, and N-linked glycosylation. The result is a mixed biochemical CDG-I/CDG-II pattern and a variable phenotype ranging from adult-onset exercise intolerance to congenital craniofacial anomalies, hypoglycemia, hepatopathy, coagulopathy, rhabdomyolysis, endocrine disease, and potentially fatal dilated cardiomyopathy. International experts emphasize early recognition because oral D-galactose improves glycosylation, liver abnormalities, coagulation, hypoglycemia, and some muscle outcomes, although cardiac disease is often treatment-resistant. (altassan2021internationalconsensusguidelines pages 10-12, radenkovic2023novelinsightsinto pages 2-3, altassan2021internationalconsensusguidelines pages 1-3)

The following table summarizes the strongest quantitative evidence.

| Domain | Strongest quantitative finding | Evidence type | Source / date / DOI or NCT |
|---|---|---|---|
| Human cohort phenotypes | Among 57 molecularly confirmed patients, cleft palate occurred in 28, bifid uvula in 25, and Pierre-Robin sequence in 15; cardiac involvement affected 24 patients, including dilated cardiomyopathy in 12; hypoglycemia was reported in 38 patients; cardiac complications caused death in 6 patients (altassan2021internationalconsensusguidelines pages 3-4, altassan2021internationalconsensusguidelines pages 4-6, altassan2021internationalconsensusguidelines pages 6-7) | Human clinical cohort / consensus synthesis | Altassan et al., *J Inherit Metab Dis*, Sep 2021, doi:10.1002/jimd.12286 |
| 2023 five-patient D-galactose outcomes | In 5 treated patients, notable clinical improvement occurred in 4; transferrin glycosylation, liver transaminases, and coagulation factors improved/normalized in 3; CK improved in 2; hypoglycemia resolved in 2; 1 discontinued for urinary frequency/lack of benefit; cardiac function did not improve in 3 with baseline abnormalities (radenkovic2023novelinsightsinto pages 1-2, radenkovic2023novelinsightsinto pages 5-6) | Human case series | Radenkovic et al., *Ther Adv Rare Dis*, Jan 2023, doi:10.1177/26330040221150269 |
| Standard D-galactose management | Recommended dose range 500-2500 mg/kg/day (about 1 g/kg/day typical), divided up to 6 doses, maximum 50 g/day; monitoring every 6 months includes ALT/AST, ATIII, CK, CDT/N-glycans, Gal-1-P, and urine galactitol (boyer2022nutritioninterventionsin pages 30-30, altassan2021internationalconsensusguidelines pages 13-15) | Human management guideline / review | Boyer et al., *Trends Mol Med*, Jun 2022, doi:10.1016/j.molmed.2022.04.003; Altassan et al., Sep 2021, doi:10.1002/jimd.12286 |
| Skeletal muscle mechanism (C2C12) | CRISPR Pgm1-knockout myoblasts/myotubes showed significantly reduced basal respiration, ATP production, and spare respiratory capacity; ^13C6-galactose tracing showed a block in galactose use for energy production, and D-galactose did not rescue the energetic deficit (conte2023invitroskeletal pages 15-16, conte2023invitroskeletal pages 1-2) | In vitro cellular model | Conte et al., *Int J Mol Sci*, May 2023, doi:10.3390/ijms24098247 |
| Constitutive mouse model | Homozygous constitutive knockout produced 0 homozygous live births among 78 pups, indicating embryonic lethality before E9.5; heterozygotes had abnormal serum glycosylation similar to human PGM1-CDG (balakrishnan2019anovelphosphoglucomutase‐deficient pages 1-3) | Animal model | Balakrishnan et al., *J Inherit Metab Dis*, Jun 2019, doi:10.1002/jimd.12110 |
| Cardiac mouse multi-omics | In Pgm2cKO hearts, mitochondrial complex III activity was reduced by 25%; proteomics quantified 4,396 proteins; glycoproteomics identified 1,640 N-glycopeptides and 147 N-glycan compositions; 213 glycopeptides from 71 proteins changed significantly, with 74/213 from laminin subunits and 71/74 downregulated (balakrishnan2023aavbasedgenetherapy pages 13-15, balakrishnan2023aavbasedgenetherapy pages 10-12, balakrishnan2023aavbasedgenetherapy pages 1-3) | Animal multi-omics | Balakrishnan et al., *Transl Res*, Jul 2023, doi:10.1016/j.trsl.2023.01.004 |
| Cardiac gene therapy rescue | AAV9-PGM1 gene replacement prevented and halted progression of dilated cardiomyopathy in the cardiomyocyte-specific knockout mouse model; in the index human comparator case, LVEF fell from 54% at 6 months to 10% by 12 months before transplant (balakrishnan2023aavbasedgenetherapy pages 15-16, balakrishnan2023aavbasedgenetherapy pages 3-4) | Animal therapeutic study with human comparator case | Balakrishnan et al., *Transl Res*, Jul 2023, doi:10.1016/j.trsl.2023.01.004 |
| Clinical trial: ORL-1G | Phase 1/2, single-group pediatric trial; estimated enrollment 5; primary completion Oct 31, 2019; primary outcome was decrease in plasma liver enzymes at 3 months; secondary outcome was transferrin glycosylation improvement by day 30 (NCT03404856 chunk 1) | Interventional trial registry | NCT03404856, Orpha Labs, study start Oct 31, 2017 |
| Clinical trial: AVTX-801 | Phase 2b randomized double-blind placebo-controlled crossover trial; planned enrollment 8 adults; AVTX-801 1.5 g/kg/day (max 50 g/day); estimated start Oct 1, 2026; primary endpoint is proportion with PGM1-CDG-related events during treatment periods (NCT05402332 chunk 1) | Interventional trial registry | NCT05402332, Icahn School of Medicine at Mount Sinai, status verified Mar 2026 |


*Table: This table compiles the most decision-relevant quantitative findings for PGM1-CDG across clinical cohorts, treatment outcomes, mechanistic models, and registered trials. It is useful as a compact evidence map for disease characterization and management planning.*

## 1. Disease information

### Definition and classification

PGM1-CDG is a Mendelian inborn error of metabolism caused by phosphoglucomutase-1 deficiency. It was historically called **glycogen-storage disease type XIV**, **GSD XIV**, or **CDG type It**, but is now classified as PGM1-CDG because abnormal protein glycosylation is integral to the disorder. Two broad presentations are recognized: a congenital/multisystem phenotype and a predominantly myopathic phenotype that may not become evident until adolescence or adulthood. (altassan2021internationalconsensusguidelines pages 3-4, altassan2021internationalconsensusguidelines pages 1-3)

**Key identifiers and names**

- **OMIM phenotype:** 614921.
- **Causal gene:** *PGM1*, chromosome 1p31.3; 11 exons.
- **Synonyms:** PGM1 deficiency; phosphoglucomutase-1 deficiency; glycogen-storage disease XIV/GSD14; CDG-It; phosphoglucomutase-1 congenital disorder of glycosylation.
- **MONDO:** A MONDO identifier was not established in the retrieved primary sources and should be verified directly against the current MONDO release before database ingestion.
- **Orphanet, MeSH, ICD-10/ICD-11:** Dedicated identifiers were not verified in the retrieved evidence. Clinically, it may be coded under broader congenital glycosylation or glycogen-metabolism categories, but such coding should not be treated as disease-specific without terminology-server confirmation.

The evidence summarized here is **aggregated disease-level evidence** from published cohorts, international consensus review, case series, models, and trial registries—not individual EHR extraction. The 2023 report contributes individual-level data from five patients enrolled through a natural-history framework. (radenkovic2023novelinsightsinto pages 1-2, radenkovic2023novelinsightsinto pages 5-6)

## 2. Etiology, risks, protective factors, and gene–environment interaction

### Primary cause

The necessary cause is **biallelic germline pathogenic or likely pathogenic variation in PGM1**, producing autosomal-recessive enzyme deficiency. PGM1 contributes about 90% of phosphoglucomutase activity in most cell types and is broadly expressed, except in erythrocytes. Residual activity in affected fibroblasts or leukocytes is generally undetectable to 20% of control, but residual activity has not shown a reliable severity correlation. (altassan2021internationalconsensusguidelines pages 10-12, altassan2021internationalconsensusguidelines pages 3-4)

Forty-one variants were reported in the consensus synthesis; **c.112A>T** occurred in nine patients and **c.988G>C** in five. Most reported alleles were missense, although other loss-of-function classes are possible. Variant-level ACMG status and gnomAD frequency must be checked individually in current ClinVar/gnomAD records; the available literature does not support assigning one classification or frequency to all alleles. (altassan2021internationalconsensusguidelines pages 10-12)

### Risk and protective factors

- **Genetic risk:** two disease-causing PGM1 alleles; parental consanguinity increases the probability of homozygosity but is not required.
- **Family history:** affected siblings and carrier parents are expected under autosomal-recessive inheritance.
- **Environmental susceptibility:** fasting, illness, vomiting, and strenuous exercise plausibly expose limited glucose mobilization and energy reserve, precipitating hypoglycemia or rhabdomyolysis. These are clinical triggers, not primary causes.
- **Protective/mitigating factors:** regular complex-carbohydrate intake, avoidance of prolonged fasting and excessive alcohol, individualized exercise precautions, and D-galactose therapy reduce metabolic stress or downstream biochemical abnormalities. (boyer2022nutritioninterventionsin pages 30-30, altassan2021internationalconsensusguidelines pages 1-3)
- No validated protective PGM1 allele, modifier gene, toxin, infectious cause, smoking association, or formal gene–environment interaction model has been established.

## 3. Phenotypes

### Core phenotype spectrum

The strongest broad dataset comprised **57 molecularly confirmed patients**. Congenital craniofacial findings included cleft palate in 28/57, bifid uvula in 25/57, and Pierre Robin sequence in 15/57; combined dysmorphic features were reported in approximately 85%. Endocrine involvement was reported in 39 patients, including hypoglycemia in 38. Cardiac involvement occurred in 24, including dilated cardiomyopathy in 12, heart failure in nine, and cardiac arrest in eight. Six reported patients died from cardiac complications. (altassan2021internationalconsensusguidelines pages 3-4, altassan2021internationalconsensusguidelines pages 4-6, altassan2021internationalconsensusguidelines pages 6-7)

Suggested phenotype annotations include:

- **Craniofacial:** cleft palate, bifid uvula, Pierre Robin sequence, micrognathia. Suggested HPO concepts: Cleft palate, Bifid uvula, Pierre Robin sequence, Micrognathia.
- **Metabolic/endocrine:** fasting or illness-associated hypoglycemia, hyperinsulinism in some patients, short stature/growth-hormone–IGF1 abnormalities, occasional hypothyroidism, hypogonadotropic hypogonadism, or adrenal dysfunction. Suggested HPO: Hypoglycemia, Hyperinsulinemic hypoglycemia, Short stature, Growth hormone deficiency, Hypothyroidism, Hypogonadotropic hypogonadism.
- **Hepatic:** chronically or episodically elevated aminotransferases, steatosis, hepatomegaly, cholestasis, and fibrosis. Suggested HPO: Elevated hepatic transaminases, Hepatic steatosis, Hepatomegaly, Cholestasis, Hepatic fibrosis.
- **Muscle:** exercise intolerance, fatigue, weakness, elevated creatine kinase, myopathy, and recurrent exercise- or illness-associated rhabdomyolysis. Suggested HPO: Exercise intolerance, Muscle weakness, Elevated serum creatine kinase, Rhabdomyolysis, Myopathy.
- **Cardiac:** dilated cardiomyopathy, reduced ejection fraction, conduction/ECG abnormalities, ventricular dilation, heart failure, cardiac arrest, and occasional septal or valvular defects. Suggested HPO: Dilated cardiomyopathy, Reduced left ventricular ejection fraction, Cardiac conduction abnormality, Congestive heart failure, Ventricular septal defect, Mitral regurgitation.
- **Hemostatic/vascular:** reduced coagulation or anticoagulation proteins, prolonged coagulation measurements, bleeding or thrombotic concern. Suggested HPO: Abnormality of coagulation, Prolonged prothrombin time, Reduced antithrombin III activity.
- **Neurologic/developmental:** cognitive impairment, intellectual or learning disability, speech/motor delay, balance problems, abnormal movements, and uncommon seizures. Suggested HPO: Global developmental delay, Intellectual disability, Learning disability, Motor delay, Seizure, Abnormality of coordination.
- **Gastrointestinal/nutritional:** feeding difficulty, vomiting, dysphagia, gastroesophageal reflux, constipation, and failure to thrive. Suggested HPO: Feeding difficulties, Recurrent vomiting, Dysphagia, Gastroesophageal reflux, Constipation, Failure to thrive.

The five-patient 2023 series illustrates variability but should not be generalized as population prevalence: onset was congenital in all five; liver abnormalities and muscle involvement occurred in 5/5, hypoglycemia in 4/5, growth delay in 4/5, developmental delay in 4/5, craniofacial anomalies in 5/5, and heterogeneous cardiovascular findings in 5/5. (radenkovic2023novelinsightsinto pages 5-6)

### Severity, progression, and quality of life

Severity ranges from mild isolated adult myopathy to fatal pediatric cardiomyopathy. Hypoglycemia, transaminase elevation, CK elevation, and rhabdomyolysis may fluctuate with fasting, illness, or exertion. Cardiomyopathy may arise in childhood or adulthood and can progress rapidly; reported onset included five cases before age five, two at 5–10 years, and six after age ten, with the oldest onset at 49 years. (altassan2021internationalconsensusguidelines pages 1-3, altassan2021internationalconsensusguidelines pages 6-7)

No disease-specific EQ-5D, SF-36, PROMIS, or validated quality-of-life dataset was identified. Nevertheless, recurrent hypoglycemia, dietary burden, exercise limitation, rhabdomyolysis, cardiac surveillance, cleft-palate care, and possible transplantation are expected to affect education, employment, mobility, and family burden. This is a clinical inference rather than quantified PGM1-CDG QoL evidence.

## 4. Genetic and molecular information

### Gene and protein

*PGM1* encodes cytosolic phosphoglucomutase-1, which reversibly converts glucose-1-phosphate and glucose-6-phosphate. Suggested annotations include HGNC-approved symbol **PGM1**, protein phosphoglucomutase-1, and molecular-function concepts **phosphoglucomutase activity** and **magnesium-ion binding**. The exact HGNC and GO accession numbers should be validated against current ontology releases before automated loading.

The disease mechanism is predominantly **loss of enzymatic function** from germline biallelic variants. The evidence does not support a recurrent somatic mechanism, dominant-negative inheritance, repeat expansion, mitochondrial-DNA cause, or characteristic chromosomal rearrangement. Large deletions could theoretically cause loss of function but are not established as a common mechanism in the retrieved cohort.

### Variants and modifiers

Reported variants are predominantly missense. A severe cardiac example was homozygous **c.1544G>A (p.Arg515Gln)**; the child’s ejection fraction fell from 54% at six months to 10% at 12 months before cardiac transplantation. (balakrishnan2023aavbasedgenetherapy pages 3-4)

No replicated modifier gene or disease-specific epigenetic signature has been established. Transcriptomic and proteomic changes observed in cardiac models are downstream consequences or candidate mechanisms, not proven inherited modifiers. Epigenetic testing is therefore not part of routine diagnosis.

## 5. Environmental, lifestyle, and infectious information

PGM1-CDG is not caused by toxins, radiation, pollution, occupational exposure, smoking, alcohol, or infection. Environmental and behavioral factors matter chiefly as **metabolic stressors**:

- fasting and poor intake can provoke hypoglycemia;
- febrile illness or vomiting can precipitate catabolism;
- intense exercise can precipitate myalgia, CK elevation, or rhabdomyolysis;
- alcohol can worsen hepatic/metabolic risk and is discouraged;
- regular complex-carbohydrate intake may stabilize glucose availability. (boyer2022nutritioninterventionsin pages 30-30)

No pathogen, zoonotic transmission, or vaccine-preventable mechanism applies. Routine immunization remains appropriate as general care, subject to individual clinical status.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic PGM1 loss-of-function variants.
2. **Primary biochemical defect:** reduced conversion between glucose-1-phosphate and glucose-6-phosphate.
3. **Metabolic consequences:** impaired glycogen synthesis and glycogenolysis, reduced access of glycogen-derived carbon to glycolysis, and impaired energetic flexibility during fasting or exercise.
4. **Glycosylation consequences:** reduced UDP-glucose and UDP-galactose supply causes incompletely occupied N-glycosylation sites and truncated, galactose-deficient glycans—a mixed ER-associated type-I and Golgi-associated type-II pattern.
5. **Tissue consequences:** hepatocyte metabolic stress and abnormal secreted proteins; skeletal-muscle energetic failure and rhabdomyolysis; abnormal glycosylation plus energetic/mitochondrial dysfunction in cardiomyocytes; altered coagulation-protein abundance or processing; and developmental craniofacial defects.
6. **Clinical manifestations:** hypoglycemia, hepatopathy, coagulopathy, myopathy, exercise intolerance, and dilated cardiomyopathy. (altassan2021internationalconsensusguidelines pages 10-12, balakrishnan2023aavbasedgenetherapy pages 1-3, balakrishnan2019anovelphosphoglucomutase‐deficient pages 1-3)

Suggested GO biological-process concepts are glycogen biosynthetic process, glycogen catabolic process, glycolytic process, glucose metabolic process, UDP-glucose metabolic process, UDP-galactose metabolic process, protein N-linked glycosylation, mitochondrial ATP synthesis, muscle-cell differentiation, and cardiac-muscle contraction.

### Cell and tissue mechanisms

**Skeletal muscle—cellular evidence.** CRISPR/Cas9 Pgm1-knockout C2C12 cells showed impaired myotube maturation, reduced basal respiration, reduced mitochondrial ATP-production capacity, and reduced spare respiratory capacity. Stable-isotope tracing demonstrated impaired use of galactose for energy production. Galactose did not rescue the energetic defect, explaining why glycosylation correction may not fully resolve myopathy. Suggested CL concepts: skeletal muscle satellite cell/myoblast and skeletal muscle fiber. (conte2023invitroskeletal pages 15-16, conte2023invitroskeletal pages 1-2)

**Heart—animal multi-omics.** Cardiomyocyte-specific knockout caused ventricular dilation, reduced ejection fraction, glycogen accumulation, fibrosis, Z-disk disorganization, swollen mitochondria, a 25% reduction in mitochondrial complex III activity, TCA-metabolite depletion, and lactate accumulation. Of 1,640 detected N-glycopeptides, 213 from 71 proteins changed significantly; 74 involved laminin subunits and 71/74 were reduced. These findings support combined energetic failure and defective extracellular-matrix/sarcolemmal glycosylation. Suggested CL: cardiomyocyte, cardiac fibroblast; GO cellular components: cytosol, glycogen granule, mitochondrion, sarcolemma, extracellular matrix, endoplasmic reticulum, Golgi apparatus. (balakrishnan2023aavbasedgenetherapy pages 13-15, balakrishnan2023aavbasedgenetherapy pages 10-12)

No established PGM1-CDG single-cell atlas, spatial-transcriptomic study, patient-tissue lipidomic signature, or validated disease epigenome was identified. The most mature profiling evidence is bulk cardiac transcriptomics/proteomics/glycoproteomics and tracer metabolomics in cultured cells.

## 7. Anatomical structures affected

**Primary organs and tissues** include liver, skeletal muscle, myocardium/conduction system, endocrine pancreas and counter-regulatory endocrine axes, craniofacial structures, and the hemostatic system. Secondary involvement includes gastrointestinal feeding structures, growth axis, and variably the nervous system.

Suggested anatomical mappings include:

- **Liver**—UBERON liver; hepatocyte CL concept.
- **Skeletal muscle tissue**—UBERON skeletal muscle organ; skeletal muscle fiber/myoblast CL concepts.
- **Heart and left ventricle**—UBERON heart/left ventricle; cardiomyocyte and cardiac fibroblast.
- **Palate and uvula**—UBERON palate/soft palate/uvula.
- **Pancreas/islet beta cell** for hyperinsulinism, although hyperinsulinism is not universal.
- **Blood plasma/hemostatic system** for transferrin and coagulation abnormalities.

No consistent lateralization is described. Cardiomyopathy and metabolic myopathy are systemic rather than unilateral.

## 8. Temporal development

The congenital/multisystem form often begins prenatally or in infancy with cleft palate/Pierre Robin sequence, feeding problems, hypoglycemia, or liver abnormalities. The myopathic form can be insidious and present in adolescence or adulthood with exercise intolerance or recurrent rhabdomyolysis. (altassan2021internationalconsensusguidelines pages 3-4, altassan2021internationalconsensusguidelines pages 1-3)

The course is chronic and lifelong but heterogeneous:

- metabolic and hepatic abnormalities may fluctuate and improve with D-galactose;
- exercise-associated muscle episodes are recurrent/episodic;
- growth and developmental effects accrue during childhood;
- cardiomyopathy can be absent, slowly evolving, or rapidly progressive and fatal.

Critical intervention periods are infancy after metabolic or craniofacial presentation and any time before irreversible cardiomyopathy or organ injury. No formal staging system or spontaneous-remission pattern exists.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two carrier parents, the conventional per-pregnancy risks are 25% affected, 50% carrier, and 25% unaffected/non-carrier. Penetrance for individuals with two genuinely pathogenic alleles appears high, but expressivity is markedly variable. Anticipation is not expected. Germline mosaicism has not been established as a characteristic feature, although low residual recurrence risk can never be categorically excluded in apparently de novo situations.

More than 60 patients had been reported by 2023, while population prevalence and incidence remain unknown. There is no established sex bias, ethnic restriction, endemic region, or robust carrier frequency. No confirmed founder effect was demonstrated by the retrieved evidence. (radenkovic2023novelinsightsinto pages 1-2, altassan2021internationalconsensusguidelines pages 3-4)

## 10. Diagnostics

### Clinical and biochemical testing

PGM1-CDG should be considered in any combination of cleft palate/bifid uvula, hypoglycemia, unexplained aminotransferase elevation, coagulopathy, exercise intolerance/rhabdomyolysis, short stature, or dilated cardiomyopathy.

The characteristic screening finding is a **mixed transferrin glycosylation abnormality**, combining partially missing glycans with truncated, galactose-deficient glycans. Intact transferrin mass spectrometry—MALDI-TOF, ESI-MS, ESI-QTOF, or LC-MS—best demonstrates this mixed pattern. Transferrin isoelectric focusing, HPLC, or capillary electrophoresis may screen for carbohydrate-deficient transferrin, but mass spectrometry better resolves the structural signature. (altassan2021internationalconsensusguidelines pages 10-12)

Additional tests include fasting and illness glucose, insulin during hypoglycemia, AST/ALT, bilirubin, CK, lactate as indicated, PT/INR, antithrombin III and other coagulation factors, endocrine/growth evaluation, ECG, echocardiography, and cardiac MRI when clinically appropriate. Liver imaging can identify steatosis or hepatomegaly; muscle/liver biopsy is generally unnecessary if biochemical and molecular testing are diagnostic.

PGM1 enzyme activity in fibroblasts or leukocytes is usually 0–20% of control. It is supportive but not independently definitive. Mild galactose-1-phosphate elevation may occur even before treatment and is useful for safety monitoring. (altassan2021internationalconsensusguidelines pages 10-12)

### Molecular confirmation

Recommended confirmation is identification of two pathogenic/likely pathogenic PGM1 variants with phase established when possible. Approaches include:

1. targeted PGM1 sequencing plus deletion/duplication analysis when suspicion is high;
2. CDG, hypoglycemia, glycogen-storage, metabolic-myopathy, or cardiomyopathy panels including PGM1;
3. WES or WGS for atypical or unresolved cases.

CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line unless another diagnosis is suspected. RNA sequencing may help resolve splice variants, but it is not routine. (altassan2021internationalconsensusguidelines pages 10-12)

### Differential diagnosis and screening

Differentials include other CDGs, hepatic glycogen-storage diseases, fatty-acid oxidation disorders, disorders of gluconeogenesis, primary hyperinsulinism, metabolic myopathies, fatty-acid oxidation defects causing rhabdomyolysis, and genetic cardiomyopathies. The mixed transferrin pattern plus PGM1 variants distinguishes PGM1-CDG.

There is no established population newborn-screening program. Genomic newborn screening may incidentally detect PGM1 variants, but clinical utility and confirmatory pathways require validation. Cascade testing, carrier testing, prenatal diagnosis, and preimplantation genetic testing are available when familial variants are known. (altassan2021internationalconsensusguidelines pages 13-15)

## 11. Outcomes and prognosis

No reliable five- or ten-year survival curve, population mortality rate, or life-expectancy estimate exists. Prognosis is driven chiefly by cardiac involvement, severity of hypoglycemia, recurrent rhabdomyolysis, and treatment access. In the consensus literature, cardiac complications caused six reported deaths; dilated cardiomyopathy may progress to arrest, heart failure, transplantation, or sudden death. (altassan2021internationalconsensusguidelines pages 4-6, altassan2021internationalconsensusguidelines pages 6-7)

Noncardiac biochemical abnormalities often improve with galactose, supporting meaningful recovery potential for hypoglycemia, liver dysfunction, coagulation abnormalities, and some muscle manifestations. Congenital malformations and established developmental disability do not reverse biochemically. Persistent or progressive cardiomyopathy despite galactose is the major adverse prognostic feature. Formal prognostic models and validated biomarkers predicting cardiac progression are unavailable.

## 12. Treatment

### D-galactose

Oral **D-galactose** is the principal disease-directed treatment. It replenishes UDP-galactose/UDP-glucose pools through the Leloir pathway and improves glycan completion. Suggested chemical annotation: D-galactose, with the current CHEBI identifier to be verified before database loading. Suggested NCIt intervention concepts are dietary supplementation, carbohydrate supplementation, and oral therapy.

A commonly used target is approximately **1 g/kg/day**, with reported ranges of 500–2,500 mg/kg/day, divided into as many as six doses, and a maximum of 50 g/day. Consensus recommendations describe gradual titration, particularly in infants. Dosing must be individualized with metabolic-specialist and dietitian oversight because very high intake may increase galactose-1-phosphate and galactitol. (boyer2022nutritioninterventionsin pages 30-30, altassan2021internationalconsensusguidelines pages 13-15)

The 2023 five-patient series found clinical improvement in four; transferrin glycosylation, transaminases, and coagulation factors improved or normalized in three; CK improved in two; and hypoglycemia resolved in two. One patient stopped treatment because of urinary frequency and absent benefit; another continued to have rhabdomyolysis and tachycardia. Cardiac function did not improve in the three patients with baseline dysfunction. (radenkovic2023novelinsightsinto pages 1-2)

Monitoring should include symptoms and growth, glucose, ALT/AST, CK, coagulation factors including antithrombin III, intact transferrin or N-glycan analysis, serum galactose-1-phosphate, and urine galactitol. Six-month monitoring is suggested once stable, with closer evaluation during initiation or dose changes. (boyer2022nutritioninterventionsin pages 30-30, altassan2021internationalconsensusguidelines pages 13-15)

### Supportive and organ-directed care

- Avoid prolonged fasting; use regular complex carbohydrates and an illness/emergency feeding plan.
- Treat acute hypoglycemia promptly with glucose.
- Individualize exercise; institute hydration and rhabdomyolysis protocols.
- Standard cardiomyopathy therapy and rhythm surveillance; transplantation may be required.
- Manage cleft palate/Pierre Robin sequence through craniofacial, airway, feeding, dental, and speech teams.
- Treat endocrine deficiencies according to standard practice.
- Use PT/OT, speech/feeding therapy, and educational support when indicated.
- Review bleeding and thrombosis risk before surgery; avoid alcohol because of hepatic/metabolic vulnerability. (boyer2022nutritioninterventionsin pages 30-30, altassan2021internationalconsensusguidelines pages 1-3)

No PGM1-specific pharmacogenomic guideline, approved RNA therapy, cell therapy, or genome-editing treatment exists.

### Trials and experimental therapy

**NCT03404856** evaluated oral ORL-1G D-galactose in a Phase 1/2, single-group pediatric study with planned enrollment of five. The primary endpoint was liver-enzyme reduction at three months and the secondary endpoint transferrin-glycosylation improvement by day 30. Its registry information was last verified in January 2019, so its current status and results should not be inferred from the stale “recruiting” record. (NCT03404856 chunk 1)

**NCT05402332** is listed as a planned Phase 2b randomized, double-blind, placebo-controlled crossover study of AVTX-801 at 1.5 g/kg/day, maximum 50 g/day, in eight adults already using galactose. The registry gives an estimated start of October 1, 2026 and was status-verified in March 2026; it is therefore a future/planned study, not 2023–2024 clinical evidence. (NCT05402332 chunk 1)

AAV9-PGM1 gene replacement prevented and halted cardiomyopathy progression in a cardiac conditional-knockout mouse. This is compelling preclinical evidence but not yet evidence of safety or efficacy in humans. (balakrishnan2023aavbasedgenetherapy pages 15-16)

## 13. Prevention

Because the disease is inherited, lifestyle modification cannot prevent occurrence in a person with biallelic pathogenic variants.

- **Primary genetic prevention:** carrier testing, reproductive counseling, prenatal diagnosis, and preimplantation genetic testing for families with known variants.
- **Secondary prevention:** cascade testing of siblings and early biochemical/genetic diagnosis to initiate galactose and surveillance before irreversible complications.
- **Tertiary prevention:** fasting avoidance, illness plans, metabolic monitoring, rhabdomyolysis precautions, coagulation assessment, and regular ECG/echocardiography to reduce secondary injury.

No vaccine, antimicrobial prophylaxis, sanitation measure, toxin avoidance program, or population screening recommendation is disease-specific. Each full sibling should be evaluated promptly because apparently asymptomatic relatives may have mild or late-onset disease.

## 14. Other species and natural disease

No well-established naturally occurring veterinary PGM1-CDG syndrome or breed predisposition was identified. PGM enzymes and central glucose/glycogen pathways are evolutionarily conserved, which supports comparative modeling, but experimentally engineered disease should not be labeled natural animal disease.

There is no transmission, zoonotic potential, or cross-species infectious susceptibility. Relevant experimental taxonomy includes **Mus musculus** (NCBI Taxonomy 10090). The human taxon is **Homo sapiens** (9606). Exact mouse orthology nomenclature is potentially confusing in this literature: some publications refer to the functional mouse ortholog as **Pgm2**, whereas the 2023 C2C12 work uses updated **Pgm1** nomenclature. Database implementation should reconcile symbols against the current MGI/NCBI Gene release. (conte2023invitroskeletal pages 1-2, balakrishnan2019anovelphosphoglucomutase‐deficient pages 1-3)

## 15. Model organisms and experimental systems

### Constitutive mouse model

CRISPR-generated homozygous constitutive knockout caused death before embryonic day 9.5: no homozygous live births occurred among 78 pups. Heterozygotes had reduced enzyme activity and abnormal serum glycosylation resembling human disease. This model demonstrates developmental essentiality but is too severe for postnatal natural-history or treatment studies. (balakrishnan2019anovelphosphoglucomutase‐deficient pages 1-3)

### Cardiac conditional mouse model

A tamoxifen-inducible, cardiomyocyte-specific Pgm2 knockout recapitulates human dilated cardiomyopathy, including ventricular dilation, reduced ejection fraction, glycogen accumulation, fibrosis, Z-disk abnormalities, mitochondrial injury, and altered sarcolemmal glycoproteins. Its principal application is cardiac mechanism and therapy testing. Its limitation is that it does not model congenital craniofacial, hepatic, endocrine, or systemic disease. (balakrishnan2023aavbasedgenetherapy pages 13-15, balakrishnan2023aavbasedgenetherapy pages 1-3)

### Skeletal-muscle cellular model

CRISPR Pgm1-knockout C2C12 myoblasts/myotubes model impaired differentiation, mitochondrial respiration, ATP generation, and metabolic flexibility. They are useful for flux analysis and muscle-directed therapy screening but cannot reproduce whole-body fasting physiology, liver-derived glycoproteins, immune/hemostatic effects, or human cardiac disease. (conte2023invitroskeletal pages 15-16, conte2023invitroskeletal pages 1-2)

### Human pluripotent-stem-cell work

Patient-derived induced pluripotent stem cells have been used for stable-isotope tracing of nucleotide-sugar metabolism. This platform is relevant for tissue differentiation and personalized metabolic studies, but the retrieved evidence does not yet establish a validated organoid or mature multi-organ PGM1-CDG model.

## Recent developments and expert interpretation

The most important 2023 advance was the convergence of clinical and mechanistic evidence showing that galactose-responsive glycosylation abnormalities and galactose-resistant cardiac/muscle energetics are separable therapeutic problems. The 2023 case series documented meaningful but heterogeneous noncardiac responses and persistent cardiac dysfunction. In parallel, skeletal-muscle studies demonstrated failure of galactose to restore mitochondrial ATP production, while cardiac multi-omics implicated mitochondrial dysfunction and hypoglycosylation of laminin/sarcolemmal proteins. AAV9-PGM1 rescue of murine cardiomyopathy provides a rational route toward organ-directed gene replacement. (radenkovic2023novelinsightsinto pages 1-2, conte2023invitroskeletal pages 15-16, balakrishnan2023aavbasedgenetherapy pages 13-15, balakrishnan2023aavbasedgenetherapy pages 15-16)

The consensus expert position remains that early diagnosis and D-galactose treatment are warranted, but treatment should not create false reassurance about cardiac risk. Lifelong cardiac surveillance is necessary even when transferrin glycosylation, liver tests, coagulation, or glucose control improve. (radenkovic2023novelinsightsinto pages 2-3, altassan2021internationalconsensusguidelines pages 13-15)

## Selected exact abstract quotations

- International guideline: **“Most patients present as infants with cleft palate, liver function abnormalities and hypoglycemia, but some patients present in adulthood with isolated muscle involvement.”** (Altassan et al., September 2021; https://doi.org/10.1002/jimd.12286). (altassan2021internationalconsensusguidelines pages 1-3)
- 2023 clinical series: **“D-gal resulted in notable clinical improvement in four patients, though the efficacy of treatment varied between the patients.”** (Radenkovic et al., January 2023; https://doi.org/10.1177/26330040221150269). (radenkovic2023novelinsightsinto pages 1-2)
- 2023 muscle model: **“No difference was found for steady-state levels of nucleotide sugars, while dynamic flux analysis based on 13C6-galactose suggested a block in the use of galactose for energy production in knockout myoblasts.”** (Conte et al., May 2023; https://doi.org/10.3390/ijms24098247). (conte2023invitroskeletal pages 1-2)

## Evidence limitations

PGM1-CDG remains an ultra-rare disorder with small, partly overlapping cohorts. Many published frequencies are counts of reported patients rather than unbiased population estimates. Natural-history, quality-of-life, survival, penetrance, carrier-frequency, modifier-gene, and genotype–phenotype data remain insufficient. D-galactose evidence is based mainly on observational treatment, small case series, biochemical endpoints, and expert consensus rather than large randomized trials. The gene-therapy evidence is preclinical. PMID values and ontology accession numbers not explicitly verified in the retrieved sources have deliberately not been invented; DOI URLs are supplied for source resolution.

References

1. (altassan2021internationalconsensusguidelines pages 10-12): Ruqaiah Altassan, Silvia Radenkovic, Andrew C. Edmondson, Rita Barone, Sandra Brasil, Anna Cechova, David Coman, Sarah Donoghue, Kristina Falkenstein, Vanessa Ferreira, Carlos Ferreira, Agata Fiumara, Rita Francisco, Hudson Freeze, Stephanie Grunewald, Tomas Honzik, Jaak Jaeken, Donna Krasnewich, Christina Lam, Joy Lee, Dirk Lefeber, Dorinda Marques‐da‐Silva, Carlota Pascoal, Dulce Quelhas, Kimiyo M. Raymond, Daisy Rymen, Malgorzata Seroczynska, Mercedes Serrano, Jolanta Sykut‐Cegielska, Christian Thiel, Frederic Tort, Mari‐Anne Vals, Paula Videira, Nicol Voermans, Peter Witters, and Eva Morava. International consensus guidelines for phosphoglucomutase 1 deficiency (<scp>pgm1‐cdg</scp>): diagnosis, follow‐up, and management. Journal of Inherited Metabolic Disease, 44:148-163, Sep 2021. URL: https://doi.org/10.1002/jimd.12286, doi:10.1002/jimd.12286. This article has 86 citations and is from a peer-reviewed journal.

2. (radenkovic2023novelinsightsinto pages 2-3): Silvia Radenkovic, Christin Johnsen, Andreas Schulze, Gurnoor Lail, Laura Guilder, Kaitlin Schwartz, Matthew Schultz, Saadet Mercimek-Andrews, Suzanne Boyer, and Eva Morava. Novel insights into the phenotype and long-term d-gal treatment in pgm1-cdg: a case series. Therapeutic Advances in Rare Disease, Jan 2023. URL: https://doi.org/10.1177/26330040221150269, doi:10.1177/26330040221150269. This article has 11 citations.

3. (altassan2021internationalconsensusguidelines pages 1-3): Ruqaiah Altassan, Silvia Radenkovic, Andrew C. Edmondson, Rita Barone, Sandra Brasil, Anna Cechova, David Coman, Sarah Donoghue, Kristina Falkenstein, Vanessa Ferreira, Carlos Ferreira, Agata Fiumara, Rita Francisco, Hudson Freeze, Stephanie Grunewald, Tomas Honzik, Jaak Jaeken, Donna Krasnewich, Christina Lam, Joy Lee, Dirk Lefeber, Dorinda Marques‐da‐Silva, Carlota Pascoal, Dulce Quelhas, Kimiyo M. Raymond, Daisy Rymen, Malgorzata Seroczynska, Mercedes Serrano, Jolanta Sykut‐Cegielska, Christian Thiel, Frederic Tort, Mari‐Anne Vals, Paula Videira, Nicol Voermans, Peter Witters, and Eva Morava. International consensus guidelines for phosphoglucomutase 1 deficiency (<scp>pgm1‐cdg</scp>): diagnosis, follow‐up, and management. Journal of Inherited Metabolic Disease, 44:148-163, Sep 2021. URL: https://doi.org/10.1002/jimd.12286, doi:10.1002/jimd.12286. This article has 86 citations and is from a peer-reviewed journal.

4. (altassan2021internationalconsensusguidelines pages 3-4): Ruqaiah Altassan, Silvia Radenkovic, Andrew C. Edmondson, Rita Barone, Sandra Brasil, Anna Cechova, David Coman, Sarah Donoghue, Kristina Falkenstein, Vanessa Ferreira, Carlos Ferreira, Agata Fiumara, Rita Francisco, Hudson Freeze, Stephanie Grunewald, Tomas Honzik, Jaak Jaeken, Donna Krasnewich, Christina Lam, Joy Lee, Dirk Lefeber, Dorinda Marques‐da‐Silva, Carlota Pascoal, Dulce Quelhas, Kimiyo M. Raymond, Daisy Rymen, Malgorzata Seroczynska, Mercedes Serrano, Jolanta Sykut‐Cegielska, Christian Thiel, Frederic Tort, Mari‐Anne Vals, Paula Videira, Nicol Voermans, Peter Witters, and Eva Morava. International consensus guidelines for phosphoglucomutase 1 deficiency (<scp>pgm1‐cdg</scp>): diagnosis, follow‐up, and management. Journal of Inherited Metabolic Disease, 44:148-163, Sep 2021. URL: https://doi.org/10.1002/jimd.12286, doi:10.1002/jimd.12286. This article has 86 citations and is from a peer-reviewed journal.

5. (altassan2021internationalconsensusguidelines pages 4-6): Ruqaiah Altassan, Silvia Radenkovic, Andrew C. Edmondson, Rita Barone, Sandra Brasil, Anna Cechova, David Coman, Sarah Donoghue, Kristina Falkenstein, Vanessa Ferreira, Carlos Ferreira, Agata Fiumara, Rita Francisco, Hudson Freeze, Stephanie Grunewald, Tomas Honzik, Jaak Jaeken, Donna Krasnewich, Christina Lam, Joy Lee, Dirk Lefeber, Dorinda Marques‐da‐Silva, Carlota Pascoal, Dulce Quelhas, Kimiyo M. Raymond, Daisy Rymen, Malgorzata Seroczynska, Mercedes Serrano, Jolanta Sykut‐Cegielska, Christian Thiel, Frederic Tort, Mari‐Anne Vals, Paula Videira, Nicol Voermans, Peter Witters, and Eva Morava. International consensus guidelines for phosphoglucomutase 1 deficiency (<scp>pgm1‐cdg</scp>): diagnosis, follow‐up, and management. Journal of Inherited Metabolic Disease, 44:148-163, Sep 2021. URL: https://doi.org/10.1002/jimd.12286, doi:10.1002/jimd.12286. This article has 86 citations and is from a peer-reviewed journal.

6. (altassan2021internationalconsensusguidelines pages 6-7): Ruqaiah Altassan, Silvia Radenkovic, Andrew C. Edmondson, Rita Barone, Sandra Brasil, Anna Cechova, David Coman, Sarah Donoghue, Kristina Falkenstein, Vanessa Ferreira, Carlos Ferreira, Agata Fiumara, Rita Francisco, Hudson Freeze, Stephanie Grunewald, Tomas Honzik, Jaak Jaeken, Donna Krasnewich, Christina Lam, Joy Lee, Dirk Lefeber, Dorinda Marques‐da‐Silva, Carlota Pascoal, Dulce Quelhas, Kimiyo M. Raymond, Daisy Rymen, Malgorzata Seroczynska, Mercedes Serrano, Jolanta Sykut‐Cegielska, Christian Thiel, Frederic Tort, Mari‐Anne Vals, Paula Videira, Nicol Voermans, Peter Witters, and Eva Morava. International consensus guidelines for phosphoglucomutase 1 deficiency (<scp>pgm1‐cdg</scp>): diagnosis, follow‐up, and management. Journal of Inherited Metabolic Disease, 44:148-163, Sep 2021. URL: https://doi.org/10.1002/jimd.12286, doi:10.1002/jimd.12286. This article has 86 citations and is from a peer-reviewed journal.

7. (radenkovic2023novelinsightsinto pages 1-2): Silvia Radenkovic, Christin Johnsen, Andreas Schulze, Gurnoor Lail, Laura Guilder, Kaitlin Schwartz, Matthew Schultz, Saadet Mercimek-Andrews, Suzanne Boyer, and Eva Morava. Novel insights into the phenotype and long-term d-gal treatment in pgm1-cdg: a case series. Therapeutic Advances in Rare Disease, Jan 2023. URL: https://doi.org/10.1177/26330040221150269, doi:10.1177/26330040221150269. This article has 11 citations.

8. (radenkovic2023novelinsightsinto pages 5-6): Silvia Radenkovic, Christin Johnsen, Andreas Schulze, Gurnoor Lail, Laura Guilder, Kaitlin Schwartz, Matthew Schultz, Saadet Mercimek-Andrews, Suzanne Boyer, and Eva Morava. Novel insights into the phenotype and long-term d-gal treatment in pgm1-cdg: a case series. Therapeutic Advances in Rare Disease, Jan 2023. URL: https://doi.org/10.1177/26330040221150269, doi:10.1177/26330040221150269. This article has 11 citations.

9. (boyer2022nutritioninterventionsin pages 30-30): Suzanne W. Boyer, Christin Johnsen, and Eva Morava. Nutrition interventions in congenital disorders of glycosylation. Jun 2022. URL: https://doi.org/10.1016/j.molmed.2022.04.003, doi:10.1016/j.molmed.2022.04.003. This article has 44 citations and is from a domain leading peer-reviewed journal.

10. (altassan2021internationalconsensusguidelines pages 13-15): Ruqaiah Altassan, Silvia Radenkovic, Andrew C. Edmondson, Rita Barone, Sandra Brasil, Anna Cechova, David Coman, Sarah Donoghue, Kristina Falkenstein, Vanessa Ferreira, Carlos Ferreira, Agata Fiumara, Rita Francisco, Hudson Freeze, Stephanie Grunewald, Tomas Honzik, Jaak Jaeken, Donna Krasnewich, Christina Lam, Joy Lee, Dirk Lefeber, Dorinda Marques‐da‐Silva, Carlota Pascoal, Dulce Quelhas, Kimiyo M. Raymond, Daisy Rymen, Malgorzata Seroczynska, Mercedes Serrano, Jolanta Sykut‐Cegielska, Christian Thiel, Frederic Tort, Mari‐Anne Vals, Paula Videira, Nicol Voermans, Peter Witters, and Eva Morava. International consensus guidelines for phosphoglucomutase 1 deficiency (<scp>pgm1‐cdg</scp>): diagnosis, follow‐up, and management. Journal of Inherited Metabolic Disease, 44:148-163, Sep 2021. URL: https://doi.org/10.1002/jimd.12286, doi:10.1002/jimd.12286. This article has 86 citations and is from a peer-reviewed journal.

11. (conte2023invitroskeletal pages 15-16): Federica Conte, Angel Ashikov, Rachel Mijdam, Eline G. P. van de Ven, Monique van Scherpenzeel, Raisa Veizaj, Seyed P. Mahalleh-Yousefi, Merel A. Post, Karin Huijben, Daan M. Panneman, Richard J. T. Rodenburg, Nicol C. Voermans, Alejandro Garanto, Werner J. H. Koopman, Hans J. C. T. Wessels, Marek J. Noga, and Dirk J. Lefeber. In vitro skeletal muscle model of pgm1 deficiency reveals altered energy homeostasis. International Journal of Molecular Sciences, 24:8247, May 2023. URL: https://doi.org/10.3390/ijms24098247, doi:10.3390/ijms24098247. This article has 16 citations.

12. (conte2023invitroskeletal pages 1-2): Federica Conte, Angel Ashikov, Rachel Mijdam, Eline G. P. van de Ven, Monique van Scherpenzeel, Raisa Veizaj, Seyed P. Mahalleh-Yousefi, Merel A. Post, Karin Huijben, Daan M. Panneman, Richard J. T. Rodenburg, Nicol C. Voermans, Alejandro Garanto, Werner J. H. Koopman, Hans J. C. T. Wessels, Marek J. Noga, and Dirk J. Lefeber. In vitro skeletal muscle model of pgm1 deficiency reveals altered energy homeostasis. International Journal of Molecular Sciences, 24:8247, May 2023. URL: https://doi.org/10.3390/ijms24098247, doi:10.3390/ijms24098247. This article has 16 citations.

13. (balakrishnan2019anovelphosphoglucomutase‐deficient pages 1-3): Bijina Balakrishnan, Jan Verheijen, Arielle Lupo, Kimiyo Raymond, Coleman Turgeon, Yueqin Yang, Kandis L. Carter, Kevin J. Whitehead, Tamas Kozicz, Eva Morava, and Kent Lai. A novel phosphoglucomutase‐deficient mouse model reveals aberrant glycosylation and early embryonic lethality. Journal of Inherited Metabolic Disease, 42:1007-998, Jun 2019. URL: https://doi.org/10.1002/jimd.12110, doi:10.1002/jimd.12110. This article has 26 citations and is from a peer-reviewed journal.

14. (balakrishnan2023aavbasedgenetherapy pages 13-15): Bijina Balakrishnan, Ruqaiah Altassan, Rohit Budhraja, Willisa Liou, Arielle Lupo, Sarah Bryant, Anastasiya Mankouski, Silvia Radenkovic, Graeme J. Preston, Akhilesh Pandey, Sihem Boudina, Tamas Kozicz, Eva Morava, and Kent Lai. Aav-based gene therapy prevents and halts the progression of dilated cardiomyopathy in a mouse model of phosphoglucomutase 1 deficiency (pgm1-cdg). Jul 2023. URL: https://doi.org/10.1016/j.trsl.2023.01.004, doi:10.1016/j.trsl.2023.01.004. This article has 27 citations and is from a domain leading peer-reviewed journal.

15. (balakrishnan2023aavbasedgenetherapy pages 10-12): Bijina Balakrishnan, Ruqaiah Altassan, Rohit Budhraja, Willisa Liou, Arielle Lupo, Sarah Bryant, Anastasiya Mankouski, Silvia Radenkovic, Graeme J. Preston, Akhilesh Pandey, Sihem Boudina, Tamas Kozicz, Eva Morava, and Kent Lai. Aav-based gene therapy prevents and halts the progression of dilated cardiomyopathy in a mouse model of phosphoglucomutase 1 deficiency (pgm1-cdg). Jul 2023. URL: https://doi.org/10.1016/j.trsl.2023.01.004, doi:10.1016/j.trsl.2023.01.004. This article has 27 citations and is from a domain leading peer-reviewed journal.

16. (balakrishnan2023aavbasedgenetherapy pages 1-3): Bijina Balakrishnan, Ruqaiah Altassan, Rohit Budhraja, Willisa Liou, Arielle Lupo, Sarah Bryant, Anastasiya Mankouski, Silvia Radenkovic, Graeme J. Preston, Akhilesh Pandey, Sihem Boudina, Tamas Kozicz, Eva Morava, and Kent Lai. Aav-based gene therapy prevents and halts the progression of dilated cardiomyopathy in a mouse model of phosphoglucomutase 1 deficiency (pgm1-cdg). Jul 2023. URL: https://doi.org/10.1016/j.trsl.2023.01.004, doi:10.1016/j.trsl.2023.01.004. This article has 27 citations and is from a domain leading peer-reviewed journal.

17. (balakrishnan2023aavbasedgenetherapy pages 15-16): Bijina Balakrishnan, Ruqaiah Altassan, Rohit Budhraja, Willisa Liou, Arielle Lupo, Sarah Bryant, Anastasiya Mankouski, Silvia Radenkovic, Graeme J. Preston, Akhilesh Pandey, Sihem Boudina, Tamas Kozicz, Eva Morava, and Kent Lai. Aav-based gene therapy prevents and halts the progression of dilated cardiomyopathy in a mouse model of phosphoglucomutase 1 deficiency (pgm1-cdg). Jul 2023. URL: https://doi.org/10.1016/j.trsl.2023.01.004, doi:10.1016/j.trsl.2023.01.004. This article has 27 citations and is from a domain leading peer-reviewed journal.

18. (balakrishnan2023aavbasedgenetherapy pages 3-4): Bijina Balakrishnan, Ruqaiah Altassan, Rohit Budhraja, Willisa Liou, Arielle Lupo, Sarah Bryant, Anastasiya Mankouski, Silvia Radenkovic, Graeme J. Preston, Akhilesh Pandey, Sihem Boudina, Tamas Kozicz, Eva Morava, and Kent Lai. Aav-based gene therapy prevents and halts the progression of dilated cardiomyopathy in a mouse model of phosphoglucomutase 1 deficiency (pgm1-cdg). Jul 2023. URL: https://doi.org/10.1016/j.trsl.2023.01.004, doi:10.1016/j.trsl.2023.01.004. This article has 27 citations and is from a domain leading peer-reviewed journal.

19. (NCT03404856 chunk 1):  Study of ORL-1G (D-galactose) in Patients With Glycogen Storage Disease Type 14. Orpha Labs. 2017. ClinicalTrials.gov Identifier: NCT03404856

20. (NCT05402332 chunk 1): Eva Morava-Kozicz. Evaluating the Efficacy and Safety of D-galactose in PGM1-CDG (AVTX-801). Eva Morava-Kozicz. 2026. ClinicalTrials.gov Identifier: NCT05402332

## Artifacts

- [Edison artifact artifact-00](PGM1-Congenital_Disorder_of_Glycosylation-deep-research-falcon_artifacts/artifact-00.md)