---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T16:48:02.407615'
end_time: '2026-07-31T16:57:07.855104'
duration_seconds: 545.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CTNNB1 Neurodevelopmental Disorder
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CTNNB1_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CTNNB1 Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CTNNB1 Neurodevelopmental Disorder** covering all of the
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
- **Disease Name:** CTNNB1 Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CTNNB1 Neurodevelopmental Disorder** covering all of the
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


# CTNNB1 Neurodevelopmental Disorder: Disease-Characteristics Report

## Executive summary and evidence scope

CTNNB1 neurodevelopmental disorder (CTNNB1-NDD) is a rare, usually de novo autosomal-dominant developmental disorder caused predominantly by heterozygous loss-of-function variants in **CTNNB1**, which encodes β-catenin. The characteristic phenotype combines global developmental delay/intellectual disability, severe expressive-language impairment, axial hypotonia evolving into lower-limb dystonia or spasticity, abnormal gait, acquired or congenital microcephaly, behavioral abnormalities, and visual disease. It is frequently mistaken for cerebral palsy. The best large human anchor is the 2022 international characterization of 404 affected individuals (PMID **36083290**); recent primary reports continue to expand the variant spectrum, while 2024 research refined the recognizable movement-disorder phenotype (PMID **39067319**). Prospective natural-history and first-in-human treatment programs are now underway. (NCT07614126 chunk 1, NCT07614126 chunk 2, lainscek2025ctnnb1syndromemouse pages 1-2, lainscek2025ctnnb1syndromemouse pages 12-13)

Evidence below is labeled as **human clinical**, **registry**, **model organism**, or **mechanistic/in vitro**. Most disease-level information is aggregated from cohorts, case series, systematic reviews, ClinGen/OpenTargets-style resources, and trial registries—not individual EHR records. Important limitations are ascertainment bias, historically small cohorts, heterogeneous ages, and limited longitudinal follow-up.

| Domain | Curated finding | Suggested ontology/identifier | Best evidence and date | Evidence gaps/caveats |
|---|---|---|---|---|
| Disease identity | Rare monogenic neurodevelopmental syndrome caused by CTNNB1 variation; commonly described as CTNNB1 syndrome / CTNNB1 neurodevelopmental syndrome / neurodevelopmental disorder with spastic diplegia and visual defects (NEDSDV) | MONDO:0100571; OMIM/MIM #615075; MeSH term used in trial browse: Neurodevelopmental Disorders | OpenTargets disease-target association for “CTNNB1-related neurodevelopmental disorder and/or vitreoretinopathy”; clinical-trial disease descriptions; 2025-2026 registry entries (OpenTargets Search: CTNNB1 neurodevelopmental disorder-CTNNB1, NCT07167732 chunk 1, NCT07270549 chunk 1) | Naming is still heterogeneous across papers and trials; some legacy reports use MRD19 or emphasize vitreoretinopathy/visual defects rather than the broader syndrome |
| Evidence source type | Knowledge derives mainly from aggregated disease resources, published case reports/case series/systematic review, and prospective/retrospective observational registries rather than EHR-only datasets | Evidence type labels: primary human, review, registry, model organism | 24-patient cohort, 2-patient case series, systematic review, and interventional/observational registrations (yan2022geneticandclinical pages 1-2, ji2023wholeexomesequencing pages 1-3, ji2023wholeexomesequencing pages 5-6, NCT07167732 chunk 1, NCT04812119 chunk 1) | No large population-based EHR study identified in the available evidence |
| Causal gene | CTNNB1 encodes β-catenin, a 781-aa armadillo-family protein with 12 armadillo repeats | Gene: CTNNB1; approved symbol CTNNB1; target ENSG00000168036 | Mouse-model synthesis and OpenTargets association, 2025 and current database record (lainscek2025ctnnb1syndromemouse pages 1-2, lainscek2025ctnnb1syndromemouse pages 2-4, OpenTargets Search: CTNNB1 neurodevelopmental disorder-CTNNB1) | HGNC ID not explicitly available in current context, so not asserted |
| Molecular mechanism | Predominant disease mechanism is heterozygous loss of function / haploinsufficiency affecting canonical Wnt/β-catenin signaling and cadherin-mediated cell adhesion; some variants may act via dominant-negative or gain-of-function effects and are excluded from current gene-replacement trial eligibility | Mechanism labels: haploinsufficiency; canonical Wnt signaling; cell-cell adhesion | Human cohort/case evidence and trial criteria, 2022-2026 (yan2022geneticandclinical pages 1-2, ji2023wholeexomesequencing pages 5-6, NCT07270549 chunk 2, lainscek2025ctnnb1syndromemouse pages 1-2) | Functional classification is variant-specific; only a subset of variants has direct functional evidence |
| Inheritance | Autosomal dominant, usually de novo | Autosomal dominant | 2022 Chinese cohort and 2025 mouse-model review (yan2022geneticandclinical pages 1-2, lainscek2025ctnnb1syndromemouse pages 2-4) | Rare familial recurrence/sibling recurrence can occur; penetrance estimates not well quantified in available evidence |
| Prevalence | Estimated prevalence 2.6-3.2 per 100,000 births | Prevalence estimate (label only) | 2025 peer-reviewed mouse-model review summarizing human epidemiology (lainscek2025ctnnb1syndromemouse pages 1-2) | Estimate appears review-derived rather than from a formal population registry in the provided evidence |
| Core quantitative phenotypes | In 24 mainland Chinese patients: developmental delay/intellectual disability 100%, motor delay 100%, speech impairment 100%, dystonia 87.5%, microcephaly 69.6%, visual defects 79.2%, behavioral abnormalities 83.3%, strabismus 62.5%, sleep disturbance 70.8% | HPO term labels: developmental delay; intellectual disability; motor delay; speech impairment; dystonia; microcephaly; visual impairment/strabismus; behavioral abnormality; sleep disturbance | Primary human cohort, 2022 (yan2022geneticandclinical pages 1-2, yan2022geneticandclinical pages 2-4) | Frequencies vary across ancestries, ascertainment strategies, and age distribution |
| Additional phenotype detail | Systematic review concluded a broad spectrum from normal to severe, with facial dysmorphism, motor disability, language/cognitive impairment, and autistic-like/aggressive behaviors common; C-terminal-region variants (exons 13-15) may trend milder | HPO labels: facial dysmorphism; autism spectrum traits; aggressive behavior | Systematic review, 2022 (ji2023wholeexomesequencing pages 5-6) | Genotype-phenotype correlation remains imperfect and not sufficiently predictive for individual prognosis |
| Onset / course | Typically early childhood/congenital neurodevelopmental presentation; motor features may be difficult to detect before age 1 year; available data do not suggest cognitive decline, but robust longitudinal data remain limited | Onset label: pediatric; chronic lifelong disorder | Levodopa pilot background and natural history rationale, 2025-2026 registry entries (NCT07614126 chunk 1, NCT07167732 chunk 1) | Natural history remains incompletely defined; formal longitudinal outcomes are still being collected |
| Anatomy affected | Central nervous system predominates; retina/visual system commonly involved; movement system/gait frequently impaired | UBERON/CL/GO labels only: brain, cerebral cortex, hippocampus, midbrain dopamine neurons, retina | Human cohorts and mouse models, 2022-2025 (yan2022geneticandclinical pages 1-2, lainscek2025ctnnb1syndromemouse pages 1-2, lainscek2025ctnnb1syndromemouse pages 8-10) | Cardiac involvement is being surveyed but frequency is not established in available evidence |
| Diagnostic approach | Genotype-first diagnosis: molecular confirmation of a pathogenic/likely pathogenic heterozygous CTNNB1 variant, commonly by exome sequencing; parental testing used to show de novo status; phenotyping often includes MRI, EEG, ophthalmology/OCT, motor/cognitive/behavioral testing | Diagnostic labels only: WES, WGS, gene panel, EEG, MRI, OCT | 23/24 patients diagnosed by exome in Chinese cohort; Dragonfly natural history assessments; case reports from WES, 2022-2026 (yan2022geneticandclinical pages 2-4, NCT07167732 chunk 1, ji2023wholeexomesequencing pages 1-3) | No universally adopted disease-specific clinical diagnostic criteria identified; biomarker assays remain investigational |
| Differential diagnosis | Often overlaps clinically with cerebral palsy/genetic cerebral palsy, especially because of dystonic/spastic gait and early motor delay | Differential label: cerebral palsy | 2025-2026 trial descriptions and 2025 review (NCT07614126 chunk 1, lainscek2025ctnnb1syndromemouse pages 1-2) | Differential diagnosis list is broader in practice, but detailed comparative data were not available in the provided evidence |
| Established management | No curative standard therapy; management is supportive and multidisciplinary, emphasizing symptom management, physiotherapy/rehabilitation, developmental therapies, vision care, and monitoring of sleep/behavior/motor complications | NCIT labels only: supportive care; physical therapy; occupational therapy; speech therapy | Mouse-model review and Dragonfly protocol, 2025-2026 (lainscek2025ctnnb1syndromemouse pages 1-2, NCT07167732 chunk 1) | No evidence-based disease-specific treatment algorithm or response-rate meta-analysis available in current evidence |
| Quality of life / family impact | Family and patient quality of life are recognized outcomes and are being prospectively measured in ongoing studies | PedsQL Family Impact Module; PedsQL Core Module | Dragonfly natural history study and AAV9 trial outcome measures, 2025-2026 (NCT07167732 chunk 1, NCT07270549 chunk 2) | Published disease-specific QoL results were not available in the provided evidence |
| Natural history study | Dragonfly: international prospective longitudinal observational study of CTNNB1 neurodevelopmental syndrome; estimated enrollment 250; annual visits over 5 years; assesses neurology, motor/cognition, communication, behavior, vision, sleep, gait actimetry, EEG, MRI/OCT, blood biomarkers | NCT07167732 | ClinicalTrials.gov registry, first posted 2025-09-11; recruiting; study started 2024-06-14 (NCT07167732 chunk 1) | Registry details may update; no results yet |
| Genotype-phenotype registry study | Completed cross-sectional observational study enrolling 100 participants to capture genotype/phenotype correlations and natural-course information | NCT04812119 | ClinicalTrials.gov registry, completed 2022-11-01 (NCT04812119 chunk 1, NCT04812119 chunk 2) | Results not included in current context |
| Hyperekplexia study | Completed observational cohort examining prevalence/clinical features of exaggerated startle/hyperekplexia in CTNNB1 syndrome; actual enrollment 10 | NCT05168969 | ClinicalTrials.gov registry, completed 2022-12-10; updated 2023-04-25 (NCT05168969 chunk 1) | No posted results available in current evidence |
| Levodopa pilot | Prospective pilot of L-dopa/carbidopa for CTNNB1-related NDD in children with dystonia; estimated enrollment 7; primary endpoint GMFM-88 change at 6 months; secondary endpoints include cognition, Vineland, QoL, CGI, safety | NCT07614126; Drug label: Levodopa/carbidopa | ClinicalTrials.gov registry, first posted 2026-05-29; recruiting (NCT07614126 chunk 1, NCT07614126 chunk 2) | Very small, uncontrolled study; efficacy remains unproven |
| Gene-replacement trial | GAIN-CTNNB1 / Urbagen: first-in-human phase I/II open-label AAV9-based CTNNB1 gene addition therapy, single bilateral intracerebroventricular administration, pediatric participants, estimated enrollment 12; prophylactic sirolimus and methylprednisolone/prednisolone | NCT07270549; Biological: Urbagen gene addition therapy; AAV9/hCTNNB1 vector | ClinicalTrials.gov registry, first posted 2025-12-08; recruiting; orphan-drug note in registry (NCT07270549 chunk 1, NCT07270549 chunk 2) | No human efficacy/safety results yet; trial excludes predicted gain-of-function/dominant-negative variants |
| Model organisms | Extensive mouse models recapitulate embryonic lethality, cortical/hippocampal defects, reduced dendritic branching, autism-like behaviors, motor deficits, seizure phenotypes, hypothalamic abnormalities, and retinal exudative vitreoretinopathy features | Model labels only: mouse; retinal-specific model; conditional knockout; gain-of-function model | Peer-reviewed model synthesis, 2025 (lainscek2025ctnnb1syndromemouse pages 4-5, lainscek2025ctnnb1syndromemouse pages 7-8, lainscek2025ctnnb1syndromemouse pages 8-10, lainscek2025ctnnb1syndromemouse pages 2-4) | Mouse evidence is strongest in current context; zebrafish/cellular models are mentioned less directly and not richly detailed here |
| Pathophysiology chain | Reduced functional β-catenin disrupts destruction-complex-regulated Wnt transcription and cadherin-linked adhesion, impairing progenitor proliferation/survival, dendritic development, synaptic organization, and possibly dopaminergic neurogenesis, producing developmental, motor, cognitive, and visual phenotypes | GO labels only: canonical Wnt signaling pathway; cell adhesion; neuron projection development; synapse organization | Mechanistic synthesis from review and trial background with cited foundational PMIDs, 2025-2026 (lainscek2025ctnnb1syndromemouse pages 1-2, lainscek2025ctnnb1syndromemouse pages 4-5, NCT07614126 chunk 1, NCT07614126 chunk 2) | Human biomarker validation is limited; much mechanistic detail comes from model systems |
| Large cohort anchor | A 2022 Genet Med study of 404 individuals is referenced as a major phenotypic/genotypic characterization dataset | PMID 36083290 | Referenced in trial bibliography and mouse-model review, publication 2022-11 (NCT07614126 chunk 2, lainscek2025ctnnb1syndromemouse pages 12-13) | Full cohort details were not directly extractable from current context, so only anchored, not over-interpreted |
| Unavailable / not established | No robust incidence estimate, no validated protective factors, no confirmed environmental causes, no established gene-environment interaction, no disease-specific biochemical diagnostic biomarker, no survival/life-expectancy estimate, no standard prevention beyond genetic counseling and reproductive testing | “Not established in available evidence” | Across available cohorts, reviews, and trial registries (yan2022geneticandclinical pages 1-2, NCT07167732 chunk 1, lainscek2025ctnnb1syndromemouse pages 1-2) | Absence here reflects limits of available evidence/context, not proof of true absence in the wider literature |


*Table: This table condenses the most actionable disease-knowledge-base facts for CTNNB1 neurodevelopmental disorder, including identifiers, mechanism, quantitative phenotypes, diagnosis, management, and active clinical studies. It also flags where evidence remains preliminary or unavailable.*

## 1. Disease information

### Definition, identifiers, and synonyms

CTNNB1-NDD is a Mendelian neurodevelopmental syndrome associated with impaired β-catenin dosage and function. Recommended identifiers are:

- **MONDO:** **MONDO:0100571**, “CTNNB1-related neurodevelopmental disorder and/or vitreoretinopathy.”
- **OMIM/MIM:** **615075**, *Neurodevelopmental disorder with spastic diplegia and visual defects* (NEDSDV).
- **Causal target:** CTNNB1, Ensembl **ENSG00000168036**.
- **Common names:** CTNNB1 syndrome; CTNNB1 neurodevelopmental syndrome; CTNNB1-related neurodevelopmental disorder; NEDSDV; β-catenin-related neurodevelopmental disorder; historically, mental retardation type 19/MRD19.
- **Orphanet, ICD-10/ICD-11, and MeSH:** no disease-specific code was verified in the retrieved evidence. Coding ordinarily uses broader intellectual-disability, developmental-disorder, movement-disorder, or congenital-genetic categories. “Neurodevelopmental Disorders” is the relevant broad MeSH concept. (ji2023wholeexomesequencing pages 5-6, NCT05168969 chunk 1, OpenTargets Search: CTNNB1 neurodevelopmental disorder-CTNNB1, lainscek2025ctnnb1syndromemouse pages 2-4)

The disease should be distinguished from **somatic activating CTNNB1 mutations in cancer** and from activating germline alleles causing other developmental phenotypes. CTNNB1-NDD is primarily a constitutional haploinsufficiency disorder.

## 2. Etiology, risk, protection, and environment

### Causal factors

The primary cause is a **germline heterozygous pathogenic CTNNB1 variant**, usually arising de novo. Nonsense, frameshift, canonical splice, exon-level deletion, and larger deletion variants that reduce functional β-catenin are the principal classes. Two 2023 cases carried novel de novo truncating variants **c.1586dupA (p.Gln530Alafs*42)** and **c.257dup (p.Tyr86*)**. The clinical mechanism was classified as loss of function/haploinsufficiency. (ji2023wholeexomesequencing pages 3-5, ji2023wholeexomesequencing pages 1-3, ji2023wholeexomesequencing pages 5-6)

Exceptional missense or truncating alleles may have dominant-negative or gain-of-function consequences. This distinction is clinically important: the current gene-addition trial excludes variants predicted to produce gain of function, including p.Gly575Arg, or specified dominant-negative effects. Variant interpretation must therefore integrate location, predicted transcript consequence, population frequency, segregation, and, where available, functional data rather than assuming every CTNNB1 variant causes haploinsufficiency. (NCT07270549 chunk 2)

### Risk and protective factors

- **Genetic risk:** a pathogenic constitutional CTNNB1 allele is sufficient; inheritance is autosomal dominant. Most affected individuals have no family history.
- **Environmental, infectious, occupational, or lifestyle risks:** none are established as causes or modifiers of this Mendelian syndrome.
- **Protective alleles, diet, exercise, or prophylactic exposures:** none have been validated.
- **Gene–environment interaction:** no reproducible disease-specific interaction has been demonstrated.
- **Sex:** both sexes are affected; no established sex-specific penetrance was identified. The 24-person Chinese cohort included 14 males and 10 females, which is insufficient to infer a true sex bias. (yan2022geneticandclinical pages 1-2, yan2022geneticandclinical pages 2-4)

## 3. Phenotypes

### Quantitative human evidence

In a primary cohort of 24 mainland Chinese patients aged 0.6–11 years, developmental delay/intellectual disability, motor delay, and speech impairment were each reported in **100%**; dystonia in **87.5%**; visual defects in **79.2%**; behavioral abnormalities in **83.3%**; microcephaly in approximately **70%**; strabismus in **62.5%**; and sleep disturbance in approximately **71%**. Anxiety occurred in 33.3%, repetitive behavior in 33.3%, and formally reported autism spectrum disorder in 12.5%. Frequencies should not be generalized uncritically because ascertainment, age, and phenotype definitions differ among cohorts. (yan2022geneticandclinical pages 4-6, yan2022geneticandclinical pages 1-2, yan2022geneticandclinical pages 2-4)

| Phenotype | Typical characteristics and course | Suggested HPO term |
|---|---|---|
| Global developmental delay / intellectual disability | Evident in infancy or early childhood; severity variable, commonly moderate–severe; chronic, without established neurodegenerative decline | Global developmental delay; Intellectual disability |
| Speech/language impairment | Expressive language disproportionately impaired; speech may be minimal or absent; major effect on autonomy and social participation | Delayed speech and language development; Absent speech |
| Motor delay | Delayed sitting, standing, and walking; some remain nonambulatory | Motor delay; Delayed walking |
| Axial hypotonia | Often early; may coexist with later distal hypertonia | Muscular hypotonia; Truncal hypotonia |
| Dystonia/spastic diplegia | Lower limbs often more affected, especially distally; gait may be tiptoe, broad-based, unstable, or absent | Dystonia; Lower-limb spasticity; Spastic diplegia |
| Microcephaly | Congenital or postnatal; variable | Microcephaly; Postnatal microcephaly |
| Visual disease | Strabismus, refractive error, cortical/functional visual impairment, and occasionally familial exudative vitreoretinopathy or retinal detachment | Strabismus; Visual impairment; Exudative vitreoretinopathy |
| Behavioral/neuropsychiatric findings | Autistic traits, repetitive behavior, anxiety, hyperactivity, impulsivity, aggression or mood abnormalities; variable | Autistic behavior; Anxiety; Hyperactivity; Repetitive behavior |
| Sleep disturbance | Common in cohort data and relevant to family burden | Sleep disturbance |
| Craniofacial features | Wide nasal bridge, bulbous nose, long philtrum, thin upper lip, long eyelashes, or prominent ears; not individually diagnostic | Abnormal facial shape; Broad nasal bridge; Long philtrum; Thin upper lip |
| Hyperekplexia | Rare exaggerated startle phenotype with stiff falls and injury risk | Exaggerated startle response; Hyperekplexia |

The motor disorder is clinically complex and may be labeled “spasticity” when dystonia predominates. A 2024 movement-disorder paper specifically characterized this recognizable phenomenology (published September 2024; PMID **39067319**). Registry investigators note that motor signs may be difficult to recognize before one year of age and that available cross-sectional evidence does not suggest cognitive decline. (NCT05168969 chunk 1, NCT07614126 chunk 1, NCT07614126 chunk 2)

### Quality of life

Motor dependence, limited communication, visual dysfunction, behavioral symptoms, sleep disturbance, feeding limitations, and caregiver burden affect daily functioning. Published CTNNB1-specific EQ-5D or SF-36 estimates were not retrieved. The Dragonfly natural-history study and Urbagen trial now use PedsQL Core and Family Impact modules; the levodopa pilot uses CP-CHILD. These are outcome-measure plans, not evidence of treatment benefit. (NCT07167732 chunk 1, NCT07614126 chunk 1, NCT07270549 chunk 2)

## 4. Genetic and molecular information

**Gene:** **CTNNB1**, encoding the 781-amino-acid β-catenin protein. β-catenin contains 12 armadillo repeats that bind more than 20 partners, including cadherins and TCF/LEF transcription factors. The gene is dosage-sensitive, and biallelic/complete loss is incompatible with normal embryogenesis in animal models. (lainscek2025ctnnb1syndromemouse pages 1-2, lainscek2025ctnnb1syndromemouse pages 2-4)

### Variant interpretation

- **Pathogenic/likely pathogenic:** truncating, splice-disrupting, or deletion alleles supported by de novo occurrence, absence/rarity in population databases, and a haploinsufficiency mechanism.
- **VUS:** should not establish diagnosis without adequate ACMG/AMP evidence.
- **Population frequency:** disease-causing de novo alleles are expected to be absent or extremely rare in gnomAD; exact allele frequencies must be queried per variant.
- **Origin:** predominantly germline de novo; parental testing is needed. Somatic CTNNB1 variants are important in oncology but represent a separate context.
- **Structural changes:** exon/gene deletions and larger 3p deletions encompassing CTNNB1 can produce an overlapping but potentially broader phenotype.
- **Modifier genes:** none are clinically validated.
- **Disease-specific episignature:** not established. Dragonfly is prospectively studying DNA methylation and RNA expression, but these are investigational biomarkers. (yan2022geneticandclinical pages 1-2, ji2023wholeexomesequencing pages 3-5, NCT07167732 chunk 1)

A systematic review found broad genotype–phenotype variability and suggested that variants in the C-terminal region, particularly exons 13–15, may be associated with milder neurodevelopmental phenotypes and relatively prominent eye disease. This is a probabilistic cohort-level observation, not a reliable individual prognostic rule. Its abstract states that CTNNB1 syndrome “encompasses a wide spectrum of clinical features, ranging from normal to severe” (published October 19, 2022; PMID **36293418**; DOI **10.3390/ijms232012564**). (ji2023wholeexomesequencing pages 5-6, NCT07614126 chunk 2)

## 5. Environmental information

No toxin, radiation exposure, pollution, occupation, smoking, alcohol, diet, exercise pattern, or infectious agent is known to cause CTNNB1-NDD. These may affect general health or rehabilitation but are not established etiologic factors. The disorder is not transmissible or zoonotic. Environmental prevention and vaccination are therefore not disease-specific.

## 6. Mechanism and pathophysiology

### Upstream molecular defect

In the absence of Wnt ligand, β-catenin is phosphorylated and degraded through the AXIN–APC–CK1–GSK3β destruction complex. Wnt receptor activation inhibits this destruction process, permitting β-catenin accumulation, nuclear entry, and TCF/LEF-dependent transcription of programs controlling proliferation and differentiation. Separately, membrane-associated β-catenin binds cadherins and α-catenin at adherens junctions. These signaling and adhesion pools support tissue architecture, neurite development, dendritic morphology, synapse organization, and plasticity. (lainscek2025ctnnb1syndromemouse pages 1-2, lainscek2025ctnnb1syndromemouse pages 2-4)

### Causal chain

**Pathogenic CTNNB1 loss-of-function allele → reduced functional β-catenin → impaired canonical Wnt transcription and cadherin-associated adhesion → abnormal neural-progenitor proliferation/survival and differentiation, dendritic branching, synaptic organization, circuit maturation, and retinal vascular development → microcephaly, intellectual/language disability, dystonia/spastic gait, behavioral abnormalities, and visual disease.** Midbrain-model data additionally suggest impaired dopaminergic neurogenesis, providing the rationale—but not proof—for levodopa treatment. (NCT07614126 chunk 1, lainscek2025ctnnb1syndromemouse pages 1-2, lainscek2025ctnnb1syndromemouse pages 4-5, lainscek2025ctnnb1syndromemouse pages 8-10)

In conditional mouse models, β-catenin loss caused reduced progenitor proliferation and a reported approximately **300% increase in neural-progenitor apoptosis** during embryonic development. Other models show reduced hippocampal dendritic branching, altered inhibitory/parvalbumin circuitry, social and repetitive behavioral abnormalities, memory changes, motor deficits, seizures, retinal vascular disease, and major brain-patterning defects. Conversely, stabilized β-catenin expands neural precursors and can produce enlarged brains, demonstrating that dosage and developmental timing are critical. (lainscek2025ctnnb1syndromemouse pages 4-5, lainscek2025ctnnb1syndromemouse pages 7-8, lainscek2025ctnnb1syndromemouse pages 8-10)

### Suggested ontology annotations

- **GO biological process:** canonical Wnt signaling pathway; cell–cell adhesion; neural precursor-cell proliferation; neuron differentiation; dendrite morphogenesis; neuron projection development; synapse organization; midbrain dopaminergic-neuron differentiation; retinal blood-vessel development.
- **GO cellular component:** nucleus; cytoplasm; plasma membrane; adherens junction; postsynaptic density/synapse.
- **Cell Ontology labels:** neural stem cell; radial glial cell; neural progenitor cell; cortical neuron; parvalbumin-positive interneuron; hippocampal neuron; midbrain dopaminergic neuron; retinal endothelial cell.
- **Molecular profiling:** no validated clinical transcriptomic, proteomic, metabolomic, or lipidomic signature exists. DNA methylation, RNA, serum β-catenin, neurofilament, and zinc are exploratory Dragonfly measures. (NCT07167732 chunk 1, lainscek2025ctnnb1syndromemouse pages 7-8)

## 7. Anatomical structures affected

The **central nervous system** is primary: cerebral cortex, corticospinal/motor circuits, hippocampus, basal-ganglia/movement networks, and potentially midbrain dopamine systems. The **visual system** is also directly involved, including ocular alignment, retina and retinal vasculature. Musculoskeletal deformities, contractures, flat feet, and spinal abnormalities are generally downstream of altered tone and motor function. Cardiovascular findings have been reported, but their frequency and causal specificity remain insufficiently defined. (yan2022geneticandclinical pages 4-6, NCT07614126 chunk 1, lainscek2025ctnnb1syndromemouse pages 1-2, lainscek2025ctnnb1syndromemouse pages 8-10)

Suggested terms include **UBERON labels** brain, cerebral cortex, hippocampus, midbrain, spinal cord, retina, retinal vasculature, lower limb and skeletal muscle. Lateralization is not characteristic; motor and visual effects are commonly bilateral, although strabismus or retinal severity can be asymmetric.

## 8. Temporal development

The biological defect is present from conception and acts during embryonic neurodevelopment. Clinical recognition is usually in infancy or early childhood through hypotonia and delayed milestones. Hypertonia, dystonia, abnormal gait, behavioral differences, and microcephaly may become clearer with age. The condition is chronic and lifelong; it has no accepted staging system or remission pattern. Available cross-sectional data do not indicate a primary degenerative cognitive course, but progressive lower-limb motor limitation may reflect increasing dystonia/spasticity, growth, orthopedic complications, or contracture. Robust estimates of progression rate and adult outcomes are not yet available. (NCT05168969 chunk 1, NCT07167732 chunk 1, NCT07614126 chunk 1)

The principal intervention window is presumed to be early neurodevelopment, but the degree of postnatal reversibility is unknown. The ongoing five-year Dragonfly study is designed to resolve milestone acquisition, motor change, communication, cognition, behavior, vision, sleep, EEG, MRI, and biomarker trajectories. (NCT07167732 chunk 1)

## 9. Inheritance and population

Inheritance is **autosomal dominant**, with most pathogenic variants occurring **de novo**. Penetrance for clearly pathogenic loss-of-function variants appears high, while expressivity is markedly variable. Genetic anticipation is not expected because the disorder is not a repeat-expansion disease. Founder effects, consanguinity, carrier frequency, and population-specific susceptibility have not been established. A sibling pair in the Chinese series illustrates that recurrence can occur; parental germline mosaicism should therefore be discussed even when blood testing is negative. (yan2022geneticandclinical pages 1-2, yan2022geneticandclinical pages 2-4)

A recent review estimated prevalence at **2.6–3.2 per 100,000 births**. Incidence, regional variation, and ancestry-specific prevalence remain uncertain, and underdiagnosis is likely because affected children are often classified as cerebral palsy. No convincing ethnic or geographic restriction has emerged. (lainscek2025ctnnb1syndromemouse pages 1-2)

## 10. Diagnostics

### Recommended approach

1. Recognize the combination of developmental/language delay, early hypotonia, dystonic or spastic lower-limb motor disorder, microcephaly, visual abnormalities, and behavioral traits.
2. Perform **trio exome sequencing**, genome sequencing, or a comprehensive neurodevelopmental/cerebral-palsy gene panel that includes CTNNB1. Exome sequencing diagnosed 23 of 24 individuals in one cohort. Ensure copy-number calling or add chromosomal microarray if deletion is suspected.
3. Confirm a candidate variant by an orthogonal method when required and test both parents to determine de novo status/mosaicism.
4. Apply ACMG/AMP classification; do not use a VUS as a definitive diagnosis.
5. Baseline phenotyping: neurological and developmental examination, gross/fine motor and communication assessment, ophthalmology with retinal examination and OCT where feasible, hearing, growth/head circumference, sleep/behavior and feeding review, and orthopedic evaluation. MRI, EEG, echocardiography, or additional testing should be driven by phenotype and planned therapy. (ji2023wholeexomesequencing pages 1-3, yan2022geneticandclinical pages 2-4, NCT07167732 chunk 1, NCT07270549 chunk 2)

There is no diagnostic blood chemistry, enzyme assay, biopsy, metabolite, liquid biopsy, or validated molecular biomarker. RNA sequencing can clarify suspected splice variants; WGS is useful when WES/panel testing is negative or structural/noncoding variation is suspected. Karyotyping, FISH, mitochondrial testing, and repeat-expansion assays are not first-line unless another diagnosis is suspected.

### Differential diagnosis

The major practical differential is **cerebral palsy**, particularly spastic or dyskinetic forms. CTNNB1 testing is important when the history lacks a sufficient acquired perinatal brain insult, MRI is nondiagnostic, dysmorphism/microcephaly/visual disease is present, or the phenotype is familial or atypical. Other genetic differentials include hereditary spastic paraplegias, DDX3X-, GNAO1-, KIF1A-, ATL1-, SPAST-, TCF4-, and Wnt-pathway-related NDDs, Angelman syndrome, Rett syndrome, and other causes of syndromic developmental delay. There are no stand-alone clinical diagnostic criteria; molecular confirmation is central. (NCT07614126 chunk 1, lainscek2025ctnnb1syndromemouse pages 1-2)

Population newborn screening is not available. Cascade testing is appropriate if a parent is found to carry the variant or mosaicism is suspected.

## 11. Outcome and prognosis

Life expectancy, mortality rates, and five- or ten-year survival have not been quantified. There is presently no evidence that uncomplicated CTNNB1-NDD intrinsically shortens lifespan, but adult natural-history data are sparse. Morbidity is dominated by communication disability, impaired mobility, falls, contractures, visual dysfunction, intellectual disability, behavioral/sleep problems, and dependence in activities of daily living. Hyperekplexia can cause sudden stiff falls and recurrent injury. (NCT05168969 chunk 1, NCT07167732 chunk 1)

Functional improvement is possible through maturation, learning, augmentative communication and rehabilitation; the 2023 case report described motor improvement with rehabilitation, but it did not establish a response rate. No validated molecular prognostic biomarker exists. Variant mechanism and location may influence severity, but individual prediction remains unreliable. (ji2023wholeexomesequencing pages 3-5, ji2023wholeexomesequencing pages 5-6)

## 12. Treatment and current implementation

### Current standard care

No approved disease-modifying therapy exists. Management is individualized and multidisciplinary:

- early physical and occupational therapy; gait training, orthoses and mobility devices;
- speech-language therapy and augmentative/alternative communication;
- management of dystonia/spasticity using standard pediatric movement-disorder approaches, with attention to whether dystonia rather than pyramidal spasticity is dominant;
- ophthalmologic and retinal surveillance; refractive correction and treatment of strabismus or retinal disease;
- developmental, educational, behavioral, sleep, feeding, dental and orthopedic care;
- antiseizure treatment only when epilepsy is present;
- family psychosocial support and care coordination. (NCT07167732 chunk 1, NCT04812119 chunk 2, lainscek2025ctnnb1syndromemouse pages 1-2)

Suggested **NCIT intervention labels** are Physical Therapy, Occupational Therapy, Speech Therapy, Assistive Communication, Orthotic Device, Ophthalmologic Examination, Behavioral Therapy, Supportive Care and Genetic Counseling. No CTNNB1-specific pharmacogenomic guidance or validated combination algorithm is available.

### Experimental therapies and trials

- **Dragonfly natural-history study, NCT07167732:** international, prospective, five-year observational study; began June 14, 2024 and is currently registered as recruiting, with estimated enrollment **250**. It measures motor, cognitive, communication, behavioral, visual, sleep, EEG/MRI/OCT, actimetry, quality-of-life, methylation, RNA, β-catenin, neurofilament and zinc outcomes. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT07167732. (NCT07167732 chunk 1)
- **Gen-Phe CTNNB1, NCT04812119:** completed cross-sectional genotype–phenotype study with **100** participants. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT04812119. (NCT04812119 chunk 1, NCT04812119 chunk 2)
- **Hyperekplexia study, NCT05168969:** completed prospective observational questionnaire study, actual enrollment **10**; no results were available in the retrieved record. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT05168969. (NCT05168969 chunk 1)
- **Levodopa/carbidopa pilot, NCT07614126:** open-label single-group study in seven children with dystonia, assessing GMFM-88 at six months plus cognition, adaptive behavior, quality of life and safety. The rationale is model-based dopaminergic deficiency plus anecdotal improvement in three patients; efficacy remains unproven. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT07614126. (NCT07614126 chunk 1, NCT07614126 chunk 2)
- **GAIN-CTNNB1/Urbagen, NCT07270549:** first-in-human phase I/II open-label trial, estimated **12** children aged 2–12 years. Urbagen is a single-stranded **AAV9/hCTNNB1** gene-addition vector under a CBh promoter, delivered once by bilateral intracerebroventricular infusion, with sirolimus and corticosteroid immunosuppression. Outcomes include five-year safety plus motor, dystonia, spasticity, cognition, communication, behavior, sleep, seizures and PedsQL. No human efficacy or safety results are yet available. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT07270549. (NCT07270549 chunk 1, NCT07270549 chunk 2)

The emergence of gene replacement is the principal translational development after 2024. Expert interpretation should remain cautious: β-catenin is dosage-sensitive and oncogenically relevant, so tissue targeting, expression level, developmental timing, immunogenicity, durability, and long-term tumor surveillance are central safety questions. The trial’s exclusion of gain-of-function/dominant-negative alleles reflects the need for mechanism-specific precision medicine. (NCT07270549 chunk 2, lainscek2025ctnnb1syndromemouse pages 7-8)

## 13. Prevention

There is no lifestyle, vaccine, environmental, or medication-based primary prevention. **Genetic counseling** is the key preventive intervention. For a confirmed de novo variant with negative parental blood tests, recurrence risk is low but not zero because germline mosaicism is possible. If a parent carries the variant, each pregnancy has a 50% transmission risk, subject to variant penetrance and expressivity. Options include prenatal diagnosis by chorionic-villus sampling or amniocentesis and preimplantation genetic testing for monogenic disease. Secondary prevention consists of prompt molecular diagnosis and early developmental, motor, communication and visual intervention. Tertiary prevention targets contractures, falls, retinal complications, feeding problems, sleep disruption and caregiver burden.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart, breed predisposition, zoonotic transmission, or cross-species infectious susceptibility was identified. CTNNB1 is evolutionarily conserved, and β-catenin’s Wnt-signaling and adherens-junction functions are conserved across vertebrates. Other-species evidence is therefore predominantly experimentally induced rather than natural disease. Relevant taxa include **human, NCBI Taxon 9606** and **mouse, NCBI Taxon 10090**. Exact ortholog NCBI Gene IDs and VBO terms should be obtained directly from NCBI/Alliance for database ingestion rather than inferred here.

## 15. Model organisms

Mouse is the best-developed model. At least 36 engineered Ctnnb1 alleles have been summarized, including constitutive, conditional tissue-specific, truncating, point-mutant, and stabilized/gain-of-function alleles. Complete loss is embryonic lethal, so conditional models are essential. Brain-specific models reproduce abnormal cortical and hippocampal development, reduced progenitor proliferation, increased apoptosis, reduced dendritic branching, motor/cognitive deficits, altered social behavior and repetitive behavior. Parvalbumin-interneuron deletion produces autism-like traits and memory abnormalities; retinal-specific loss reproduces exudative vitreoretinopathy; stabilized β-catenin or APC loss models reveal the consequences of excessive signaling, including precursor expansion and seizure phenotypes. (lainscek2025ctnnb1syndromemouse pages 4-5, lainscek2025ctnnb1syndromemouse pages 7-8, lainscek2025ctnnb1syndromemouse pages 8-10, lainscek2025ctnnb1syndromemouse pages 2-4)

These models support mechanism discovery and testing of small molecules or gene replacement, but limitations are substantial: embryonic lethality with complete loss, species-specific cortical and behavioral development, variable Cre timing and cell targeting, and imperfect correspondence between engineered homozygous/tissue-specific alleles and human heterozygous germline disease. Patient-derived iPSC neurons and cerebral organoids, single-cell transcriptomics, spatial profiling, proteomics and CRISPR rescue would be valuable, but mature CTNNB1-NDD-specific datasets were not established in the retrieved evidence.

## Key primary and authoritative references

1. **Kayumi S et al.** “Genomic and phenotypic characterization of 404 individuals with neurodevelopmental disorders caused by CTNNB1 variants.” *Genetics in Medicine*. Published November 2022. PMID **36083290**; DOI **10.1016/j.gim.2022.08.006**. This is the principal large human cohort cited by current trial and model literature. (NCT07614126 chunk 2, lainscek2025ctnnb1syndromemouse pages 12-13)
2. **Yan D et al.** “Genetic and clinical characteristics of 24 mainland Chinese patients with CTNNB1 loss-of-function variants.” *Molecular Genetics & Genomic Medicine*. Published September 2022. DOI **10.1002/mgg3.2067**. The abstract directly defines NEDSDV as “a rare autosomal dominant syndrome” caused by heterozygous germline loss-of-function variants. (yan2022geneticandclinical pages 4-6, yan2022geneticandclinical pages 1-2)
3. **Miroševič Š et al.** “Correlation between Phenotype and Genotype in CTNNB1 Syndrome: A Systematic Review of the Literature.” *International Journal of Molecular Sciences*. Published October 19, 2022. PMID **36293418**; DOI **10.3390/ijms232012564**. (ji2023wholeexomesequencing pages 5-6, NCT07614126 chunk 2)
4. **Ji Y et al.** “Whole Exome Sequencing Identified two Novel Truncation Mutations in the CTNNB1 Gene…” *Child Neurology Open*. Published 2023. DOI **10.1177/2329048X231184184**. Its abstract reports two unrelated children with “neurodevelopmental disorder, abnormal facial features, speech impairments, microcephaly, and dystonia.” (ji2023wholeexomesequencing pages 3-5, ji2023wholeexomesequencing pages 1-3)
5. **Tucci V et al.** “Dominant beta-catenin mutations cause intellectual disability with recognizable syndromic features.” *Journal of Clinical Investigation*. Published April 2014. PMID **24614104**; DOI **10.1172/JCI70372**. Landmark human and model evidence. (NCT07614126 chunk 2)
6. **Garone G et al.** “Movement disorder phenotype in CTNNB1-syndrome: A complex but recognizable phenomenology.” *Parkinsonism & Related Disorders*. Published September 2024. PMID **39067319**; DOI **10.1016/j.parkreldis.2024.107057**. (NCT07614126 chunk 2)
7. **Lainšček D et al.** “CTNNB1 syndrome mouse models.” *Mammalian Genome*. Published January 2025. DOI **10.1007/s00335-025-10105-3**. This current synthesis estimates prevalence at 2.6–3.2 per 100,000 births and reviews loss- and gain-of-function models. (lainscek2025ctnnb1syndromemouse pages 1-2, lainscek2025ctnnb1syndromemouse pages 2-4)

## Major knowledge gaps

Validated incidence, adult natural history, life expectancy, standardized clinical criteria, disease-specific biomarkers, quantitative quality-of-life burden, robust variant-level prognosis, protective factors, modifier genes, epigenetic signatures, human single-cell/spatial datasets, and controlled treatment-response rates remain unavailable or preliminary. The Dragonfly cohort and early interventional studies are designed to address several of these gaps, but registry plans must not be interpreted as completed evidence of benefit. (NCT07167732 chunk 1, NCT07614126 chunk 1, NCT07270549 chunk 1)

References

1. (NCT07614126 chunk 1):  Study of L-dopa Treatment in Patients With a Neurodevelopmental Disorder (CTNNB1 Gene). University Hospital, Montpellier. 2026. ClinicalTrials.gov Identifier: NCT07614126

2. (NCT07614126 chunk 2):  Study of L-dopa Treatment in Patients With a Neurodevelopmental Disorder (CTNNB1 Gene). University Hospital, Montpellier. 2026. ClinicalTrials.gov Identifier: NCT07614126

3. (lainscek2025ctnnb1syndromemouse pages 1-2): Duško Lainšček, Vida Forstnerič, and Špela Miroševič. Ctnnb1 syndrome mouse models. Mammalian Genome, 36:390-402, Jan 2025. URL: https://doi.org/10.1007/s00335-025-10105-3, doi:10.1007/s00335-025-10105-3. This article has 5 citations and is from a peer-reviewed journal.

4. (lainscek2025ctnnb1syndromemouse pages 12-13): Duško Lainšček, Vida Forstnerič, and Špela Miroševič. Ctnnb1 syndrome mouse models. Mammalian Genome, 36:390-402, Jan 2025. URL: https://doi.org/10.1007/s00335-025-10105-3, doi:10.1007/s00335-025-10105-3. This article has 5 citations and is from a peer-reviewed journal.

5. (OpenTargets Search: CTNNB1 neurodevelopmental disorder-CTNNB1): Open Targets Query (CTNNB1 neurodevelopmental disorder-CTNNB1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (NCT07167732 chunk 1): Damjan Osredkar. CTNNB1 Neurodevelopmental Syndrome - Natural History Study. University Medical Centre Ljubljana. 2024. ClinicalTrials.gov Identifier: NCT07167732

7. (NCT07270549 chunk 1): Damjan Osredkar. Gene Replacement Therapy for Treatment of Paediatric Patients With CTNNB1 Neurodevelopmental Syndrome. CTNNB1 Foundation. 2025. ClinicalTrials.gov Identifier: NCT07270549

8. (yan2022geneticandclinical pages 1-2): Dan Yan, Yu Sun, Na Xu, Yongguo Yu, and Yongkun Zhan. Genetic and clinical characteristics of 24 mainland chinese patients with ctnnb1 loss‐of‐function variants. Molecular Genetics & Genomic Medicine, Sep 2022. URL: https://doi.org/10.1002/mgg3.2067, doi:10.1002/mgg3.2067. This article has 16 citations and is from a peer-reviewed journal.

9. (ji2023wholeexomesequencing pages 1-3): Yongchun Ji, Qin Xia, Hewei Zhang, Hongliang Huo, Xujun Cao, Weiwei Wang, and Qin Gu. Whole exome sequencing identified two novel truncation mutations in the ctnnb1 gene associated with neurodevelopmental disorder, language dysfunction, and microcephaly in chinese children. Child Neurology Open, Jan 2023. URL: https://doi.org/10.1177/2329048x231184184, doi:10.1177/2329048x231184184. This article has 5 citations and is from a peer-reviewed journal.

10. (ji2023wholeexomesequencing pages 5-6): Yongchun Ji, Qin Xia, Hewei Zhang, Hongliang Huo, Xujun Cao, Weiwei Wang, and Qin Gu. Whole exome sequencing identified two novel truncation mutations in the ctnnb1 gene associated with neurodevelopmental disorder, language dysfunction, and microcephaly in chinese children. Child Neurology Open, Jan 2023. URL: https://doi.org/10.1177/2329048x231184184, doi:10.1177/2329048x231184184. This article has 5 citations and is from a peer-reviewed journal.

11. (NCT04812119 chunk 1): Damjan Osredkar. Genotype-phenotype Correlations in Children and Adults With CTNNB1 Mutation. University Medical Centre Ljubljana. 2021. ClinicalTrials.gov Identifier: NCT04812119

12. (lainscek2025ctnnb1syndromemouse pages 2-4): Duško Lainšček, Vida Forstnerič, and Špela Miroševič. Ctnnb1 syndrome mouse models. Mammalian Genome, 36:390-402, Jan 2025. URL: https://doi.org/10.1007/s00335-025-10105-3, doi:10.1007/s00335-025-10105-3. This article has 5 citations and is from a peer-reviewed journal.

13. (NCT07270549 chunk 2): Damjan Osredkar. Gene Replacement Therapy for Treatment of Paediatric Patients With CTNNB1 Neurodevelopmental Syndrome. CTNNB1 Foundation. 2025. ClinicalTrials.gov Identifier: NCT07270549

14. (yan2022geneticandclinical pages 2-4): Dan Yan, Yu Sun, Na Xu, Yongguo Yu, and Yongkun Zhan. Genetic and clinical characteristics of 24 mainland chinese patients with ctnnb1 loss‐of‐function variants. Molecular Genetics & Genomic Medicine, Sep 2022. URL: https://doi.org/10.1002/mgg3.2067, doi:10.1002/mgg3.2067. This article has 16 citations and is from a peer-reviewed journal.

15. (lainscek2025ctnnb1syndromemouse pages 8-10): Duško Lainšček, Vida Forstnerič, and Špela Miroševič. Ctnnb1 syndrome mouse models. Mammalian Genome, 36:390-402, Jan 2025. URL: https://doi.org/10.1007/s00335-025-10105-3, doi:10.1007/s00335-025-10105-3. This article has 5 citations and is from a peer-reviewed journal.

16. (NCT04812119 chunk 2): Damjan Osredkar. Genotype-phenotype Correlations in Children and Adults With CTNNB1 Mutation. University Medical Centre Ljubljana. 2021. ClinicalTrials.gov Identifier: NCT04812119

17. (NCT05168969 chunk 1):  Hyperekplexia in Patients With CTNNB1 Mutation. Centre Hospitalier Universitaire de Saint Etienne. 2022. ClinicalTrials.gov Identifier: NCT05168969

18. (lainscek2025ctnnb1syndromemouse pages 4-5): Duško Lainšček, Vida Forstnerič, and Špela Miroševič. Ctnnb1 syndrome mouse models. Mammalian Genome, 36:390-402, Jan 2025. URL: https://doi.org/10.1007/s00335-025-10105-3, doi:10.1007/s00335-025-10105-3. This article has 5 citations and is from a peer-reviewed journal.

19. (lainscek2025ctnnb1syndromemouse pages 7-8): Duško Lainšček, Vida Forstnerič, and Špela Miroševič. Ctnnb1 syndrome mouse models. Mammalian Genome, 36:390-402, Jan 2025. URL: https://doi.org/10.1007/s00335-025-10105-3, doi:10.1007/s00335-025-10105-3. This article has 5 citations and is from a peer-reviewed journal.

20. (ji2023wholeexomesequencing pages 3-5): Yongchun Ji, Qin Xia, Hewei Zhang, Hongliang Huo, Xujun Cao, Weiwei Wang, and Qin Gu. Whole exome sequencing identified two novel truncation mutations in the ctnnb1 gene associated with neurodevelopmental disorder, language dysfunction, and microcephaly in chinese children. Child Neurology Open, Jan 2023. URL: https://doi.org/10.1177/2329048x231184184, doi:10.1177/2329048x231184184. This article has 5 citations and is from a peer-reviewed journal.

21. (yan2022geneticandclinical pages 4-6): Dan Yan, Yu Sun, Na Xu, Yongguo Yu, and Yongkun Zhan. Genetic and clinical characteristics of 24 mainland chinese patients with ctnnb1 loss‐of‐function variants. Molecular Genetics & Genomic Medicine, Sep 2022. URL: https://doi.org/10.1002/mgg3.2067, doi:10.1002/mgg3.2067. This article has 16 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CTNNB1_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md)