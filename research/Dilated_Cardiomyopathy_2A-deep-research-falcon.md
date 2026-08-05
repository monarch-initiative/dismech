---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-02T16:41:13.440077'
end_time: '2026-08-02T16:55:30.717974'
duration_seconds: 857.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dilated Cardiomyopathy 2A
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dilated_Cardiomyopathy_2A-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 2A
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 2A** covering all of the
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
- **Disease Name:** Dilated Cardiomyopathy 2A
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 2A** covering all of the
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


# Dilated Cardiomyopathy 2A (DCM2A): Disease Characteristics Report

## Executive summary and evidence boundary

Dilated cardiomyopathy 2A (DCM2A; also written **CMD2A**) is an exceptionally rare, usually neonatal or infantile, autosomal-recessive cardiomyopathy caused by **biallelic loss-of-function variants in TNNI3**, which encodes cardiac troponin I (cTnI). It should not be conflated with dominant hypertrophic, restrictive, or dilated cardiomyopathies caused by heterozygous TNNI3 alleles, or with disease involving the separate kinase gene **TNNI3K**. The strongest disease-specific synthesis available in the retrieved literature is Sorrentino et al., published March 2023, DOI [10.3390/genes14030748](https://doi.org/10.3390/genes14030748). It summarized only 20 individuals with biallelic TNNI3 variants; 16 had DCM, sometimes overlapping left-ventricular noncompaction (LVNC). Consequently, most frequencies and prognosis estimates remain imprecise, and treatment recommendations are necessarily extrapolated from pediatric/genetic DCM practice. (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 1-2)

| Topic | DCM2A-specific summary | General DCM context / extrapolation | Suggested ontology terms / identifiers | Key citations |
|---|---|---|---|---|
| Definition / scope | Dilated cardiomyopathy 2A (DCM2A; historically CMD2A) is a rare **autosomal recessive** cardiomyopathy caused by **biallelic TNNI3 loss-of-function** variants, usually presenting as severe neonatal/infantile dilated cardiomyopathy; broader heterozygous TNNI3-associated cardiomyopathies are a different entity. | Broader DCM is genetically heterogeneous and includes monogenic, oligogenic, and acquired forms. | **OMIM:** 611880; suggested disease terms: dilated cardiomyopathy, infantile-onset cardiomyopathy | (sorrentino2023homozygoustnni3mutations pages 2-4, newman2024dilatedcardiomyopathya pages 1-2) |
| Causal gene and inheritance | **TNNI3** (cardiac troponin I) is the established causal gene for DCM2A when variants are **biallelic** and loss-of-function; inheritance is **autosomal recessive**. Consanguinity is reported in some families but is not required. | In general DCM, pathogenic variants are found in many genes; pediatric cases often have higher genetic diagnostic yield than adult cases. | **Gene:** TNNI3; suggested HGNC symbol: TNNI3; inheritance: AR | (sorrentino2023homozygoustnni3mutations pages 5-8, sorrentino2023homozygoustnni3mutations pages 2-4, eldemire2024geneticsofdilated pages 1-3) |
| Hallmark phenotype / onset | Hallmark presentation is **early severe systolic dysfunction with LV dilation**, often in the first months of life, with low LVEF, heart failure symptoms (dyspnea, feeding difficulty), and occasional LV noncompaction overlap. Disease course is usually rapidly progressive. | General pediatric DCM can present across childhood, but infancy is a particularly vulnerable period. | **HPO:** Dilated cardiomyopathy HP:0001644; Left ventricular systolic dysfunction HP:0005162; Heart failure HP:0001635; Dyspnea HP:0002094; Feeding difficulties HP:0011968; Left ventricular noncompaction HP:0006677 | (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 4-5, sorrentino2023homozygoustnni3mutations pages 5-8) |
| Strongest disease-specific statistics | In the 2023 disease-focused review/case series, **20 documented biallelic TNNI3 cases** were summarized, of which **16/20 had DCM phenotype**; onset was consistently early and outcomes were typically severe, often requiring transplant soon after diagnosis. | By contrast, general genetic DCM is much more common and genetically diverse; up to ~40% of idiopathic/familial DCM has an identifiable genetic basis. | Evidence type: human case reports / case series | (sorrentino2023homozygoustnni3mutations pages 8-9, newman2024dilatedcardiomyopathya pages 1-2, eldemire2024geneticsofdilated pages 1-3) |
| Recurrent variants and frequencies | Recurrent DCM2A-associated variants include **p.Arg69Alafs\*8** and **p.Arg98\***. Reported carrier frequencies in population data summarized in the 2023 review were approximately **1/26,222** for p.Arg69Alafs\*8 and **1/17,750** for p.Arg98\*; healthy heterozygous carrier frequency overall was summarized as **48/100,000**. In two 2023 patients, homozygous **c.292C>T (p.Arg98\*)** caused severe infantile DCM. | Heterozygous TNNI3 variants more commonly relate to hypertrophic/restrictive cardiomyopathy and do not define DCM2A. | Variant classes: nonsense, frameshift, splice-altering / null | (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 4-5, sorrentino2023homozygoustnni3mutations pages 1-2) |
| Mechanism / pathophysiology | Core mechanism is **loss of cTnI function** due to biallelic TNNI3 null variants, often through **nonsense-mediated decay** with markedly reduced or absent TNNI3 mRNA/protein in myocardium; compensatory upregulation of fetal **TNNI1** has been reported. Expected downstream effect is impaired sarcomeric thin-filament inhibition and abnormal excitation-contraction coupling leading to contractile failure, ventricular dilation, and heart failure. | General DCM literature supports sarcomeric dysfunction, calcium-handling abnormalities, remodeling, fibrosis, and arrhythmia susceptibility as common downstream pathways. | **GO:** sarcomere organization GO:0045214; cardiac muscle contraction GO:0060048; regulation of cardiac muscle contraction by calcium ion signaling GO:0010882; **CL:** cardiomyocyte CL:0002494; **UBERON:** heart UBERON:0000948, left ventricle UBERON:0002084 | (sorrentino2023homozygoustnni3mutations pages 5-8, sorrentino2023homozygoustnni3mutations pages 8-9, newman2024dilatedcardiomyopathya pages 1-2) |
| Diagnosis | Most disease-specific diagnoses have been made by **echocardiography plus molecular testing**. Practical approach: infant/pediatric cardiomyopathy work-up with ECG, echocardiography, family history, and **multigene panel / WES**, interpreted with genetic counseling; test the most clearly affected proband first, then cascade test relatives if a familial variant is found. | This diagnostic strategy is extrapolated from pediatric/genetic DCM practice, where genetic testing is recommended and informative for prognosis and family screening. | Suggested tests: echocardiography, ECG, cardiac MRI when feasible, multigene cardiomyopathy panel, WES/WGS as needed | (sorrentino2023homozygoustnni3mutations pages 4-5, arnautu2024riskassessmentand pages 11-12, eldemire2024geneticsofdilated pages 1-3) |
| Treatment / prognosis | No approved **TNNI3-specific** therapy was identified. Reported DCM2A patients were managed with advanced heart-failure care; severe infant cases often required **ECMO/VAD bridge** and **heart transplantation**, with favorable post-transplant short-term outcomes in the two 2023 cases. Overall prognosis appears poor without advanced support because progression is often rapid. | Extrapolated standard DCM/HFrEF care includes beta-blocker, ARNI/ACEi/ARB, MRA, and SGLT2 inhibitor when age/clinical status allow; refractory pediatric cases may need mechanical support/transplant. | **NCIT suggestions:** Heart Transplantation, Ventricular Assist Device, Extracorporeal Membrane Oxygenation, Genetic Counseling | (sorrentino2023homozygoustnni3mutations pages 4-5, arnautu2024riskassessmentand pages 21-23, mestroni2014geneticcausesof pages 6-8) |
| Prevention / risk modification | No primary prevention exists for genetically affected homozygotes beyond reproductive counseling and at-risk family identification. Secondary prevention is **cascade screening** of relatives and early cardiac surveillance in genetically at-risk family members. | General DCM counseling includes avoiding cardiotoxic exposures and recognizing that pregnancy, alcohol, chemotherapy, and other triggers can worsen some genetic DCMs, though this has not been shown specifically for DCM2A. | Suggested counseling terms: cascade screening, reproductive counseling, family screening | (arnautu2024riskassessmentand pages 11-12, mestroni2014geneticcausesof pages 6-8, bondue2018complexroadsfrom pages 19-22) |
| Major evidence gaps | Very small number of published patients; phenotype frequencies remain imprecise; penetrance estimates for heterozygous relatives are uncertain; no confidently retrieved MONDO/Orphanet ID; no disease-specific biomarker, natural-history registry, or approved targeted therapy identified; no well-validated DCM2A-specific animal model was retrieved, and **TNNI3K** studies must not be confused with **TNNI3** disease biology. | General DCM research is rapidly evolving, but its findings cannot be assumed to apply directly to recessive TNNI3-null infantile disease. | Curation note: do **not** infer TNNI3K knockout data as DCM2A evidence | (qu2022knockoutofcardiac pages 7-7, sorrentino2023homozygoustnni3mutations pages 8-9, arnautu2024riskassessmentand pages 11-12) |


*Table: This table compacts the highest-yield knowledge-base facts for Dilated Cardiomyopathy 2A, separating subtype-specific evidence from broader dilated cardiomyopathy context. It is useful for rapid curation of identifiers, phenotype, mechanism, diagnosis, and current evidence gaps.*

## 1. Disease information

### Definition

DCM2A is a primary genetic myocardial disease characterized by ventricular—usually left-ventricular—dilation, severe systolic dysfunction, and rapidly progressive heart failure after biallelic TNNI3 loss of function. Cardiac troponin I is the inhibitory subunit of the thin-filament troponin complex and is essential for calcium-regulated cardiac contraction and relaxation. (sorrentino2023homozygoustnni3mutations pages 5-8, sorrentino2023homozygoustnni3mutations pages 2-4)

### Identifiers and synonyms

- **OMIM:** **611880**, Cardiomyopathy, dilated, 2A.
- **Common names:** DCM2A, CMD2A, cardiomyopathy dilated 2A, autosomal-recessive TNNI3-related dilated cardiomyopathy, recessive cardiac troponin-I cardiomyopathy.
- **MONDO:** a unique DCM2A-specific MONDO identifier was not confidently recoverable; map provisionally to the relevant MONDO dilated-cardiomyopathy concept while retaining OMIM:611880 as the subtype identifier.
- **Orphanet:** no confidently verified subtype-specific identifier was found.
- **ICD-10-CM:** I42.0, dilated cardiomyopathy; no gene-specific code.
- **ICD-11:** use the dilated-cardiomyopathy category with genetic etiology annotation; no dedicated DCM2A code was verified.
- **MeSH:** Cardiomyopathy, Dilated.

The evidence is mainly **aggregated disease-level literature assembled from individual case reports and small families**, not population EHR cohorts. The 2023 report combined two new patients with previously published cases. (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 4-5, sorrentino2023homozygoustnni3mutations pages 2-4)

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Primary causal factor

The established cause is a **germline biallelic pathogenic TNNI3 genotype**, especially nonsense, frameshift, or splice-disrupting alleles that abolish cTnI expression. Autosomal-recessive segregation was first supported by affected siblings of consanguineous parents; subsequent unrelated families consolidated the association. (sorrentino2023homozygoustnni3mutations pages 5-8, sorrentino2023homozygoustnni3mutations pages 2-4)

### Genetic risk factors

- Having two pathogenic TNNI3 alleles is the principal risk factor.
- Parental consanguinity increases the chance that a rare allele is inherited homozygously, but DCM2A also occurs in nonconsanguineous families.
- Recurrent alleles include **p.Arg69Alafs*8** and **p.Arg98***. In the 2023 synthesis, p.Arg69Alafs* occurred in 9 of 16 families; estimated carrier frequencies were approximately 1/26,222 and 1/17,750, respectively. Aggregate healthy heterozygous carriage was estimated at 48/100,000. These are carrier—not disease-prevalence—figures. (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 4-5)
- No validated modifier gene or polygenic score specific to DCM2A has been established.

### Environmental and protective factors

No environmental exposure is known to cause DCM2A, and no genetic protective allele has been validated. Avoiding alcohol excess, cocaine/amphetamines, cardiotoxic chemotherapy, smoking, obesity, and uncontrolled hypertension is prudent in genetic DCM generally, but evidence is not TNNI3-null-specific. Pregnancy, viral myocarditis, alcohol, and anthracyclines can interact with susceptibility alleles in broader DCM; equivalent gene–environment interaction data for DCM2A are absent. (arnautu2024riskassessmentand pages 21-23, mestroni2014geneticcausesof pages 6-8, bondue2018complexroadsfrom pages 19-22)

## 3. Phenotypes

### Core disease-specific phenotype

| Manifestation | Type and suggested HPO term | Characteristics |
|---|---|---|
| Dilated cardiomyopathy | Sign/imaging; **HP:0001644** | Present in 16/20 reported biallelic cases in the 2023 synthesis; predominantly neonatal/infantile, severe, progressive. |
| LV dilation/cardiomegaly | Imaging/sign; **HP:0001711** (abnormal LV morphology), **HP:0001640** (cardiomegaly) | Often marked at presentation. |
| LV systolic dysfunction/low EF | Functional abnormality; **HP:0005162** | Two 2023 infants had LVEF 25%; typically refractory. |
| Congestive heart failure | Clinical syndrome; **HP:0001635** | Rapid progression; advanced mechanical support or transplantation is common. |
| Dyspnea/tachypnea | Symptom; **HP:0002094**, **HP:0002789** | Common presenting manifestation in infancy. |
| Feeding difficulty/poor intake | Symptom; **HP:0011968** | Reported in an infant at six months. |
| Mitral/tricuspid regurgitation | Imaging/sign; **HP:0001653**, **HP:0005180** | Functional regurgitation may accompany chamber dilation. |
| LV noncompaction overlap | Imaging; **HP:0006677** | Reported in a minority; exact frequency is uncertain. |
| Cardiogenic shock | Acute sign; **HP:0030149** | Severe cases may require ECMO/VAD. |

The reviewed homozygous null genotypes showed relatively little variability and generally severe outcomes. Missense alleles with residual activity may have slower or atypical courses, including restrictive phenotypes; they should not automatically be grouped with null-allele DCM2A. (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 4-5)

### Illustrative human cases

A seven-month-old child had dyspnea, LV dilation, and LVEF 25%, then required ECMO and ventricular assistance; an ischemic stroke complicated support, followed by transplantation and post-transplant LVEF 61%. A second child presented at six months with feeding difficulty, dyspnea, severe left-sided dilation, LVEF 25%, and mitral/tricuspid insufficiency; transplantation at eight months produced a favorable early outcome. Both reports involved homozygous **c.292C>T (p.Arg98*)**. (sorrentino2023homozygoustnni3mutations pages 4-5)

### Quality of life

No DCM2A-specific EQ-5D, SF-36, PedsQL, or PROMIS study exists. Severe heart failure is expected to impair feeding, growth, activity, sleep, and caregiver/family functioning, while hospitalization, mechanical support, and transplantation impose major burdens. These effects are clinically evident but have not been quantified in this subtype.

## 4. Genetic and molecular information

### Causal gene

- **Gene:** TNNI3, troponin I3, cardiac type.
- **Protein:** cardiac troponin I, the inhibitory component of the troponin complex.
- **Disease mechanism:** biallelic loss of function.
- **Origin:** constitutional/germline, not somatic.

### Pathogenic variants

The strongest DCM2A variants are rare biallelic null alleles: nonsense, frameshift, and splice-altering variants. In affected myocardium, premature-termination variants can undergo nonsense-mediated decay, producing markedly reduced TNNI3 RNA and complete absence of cTnI protein. The fetal slow-skeletal isoform **TNNI1** may be compensatorily increased but does not prevent severe disease. (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 5-8)

Important reported alleles include:

- **c.292C>T, p.Arg98***: nonsense; homozygous in severe infantile DCM. It was present heterozygously in gnomAD at approximately 1/9,187 among non-Finnish Europeans in the cited analysis; heterozygosity alone is insufficient to establish DCM2A. (sorrentino2023homozygoustnni3mutations pages 4-5)
- **p.Arg69Alafs*8**: recurrent frameshift/null allele; approximate allele/carrier frequency 1/26,222 in the 2023 synthesis. (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 5-8)
- **p.Ala2Val**: homozygous in the first reported recessive family, although the precise residual function and classification require variant-level reassessment under current ACMG/AMP criteria. (sorrentino2023homozygoustnni3mutations pages 5-8)

A variant should be classified with ACMG/AMP criteria using segregation, phenotype specificity, population frequency, predicted transcript effect, myocardial/RNA functional evidence, and ClinVar expert assertions where available. A VUS must not be used for predictive testing or reproductive decision-making as though pathogenic.

### Other molecular categories

No recurrent DCM2A-specific chromosomal rearrangement, aneuploidy, somatic mechanism, DNA-methylation signature, or validated modifier gene has been demonstrated. Copy-number analysis remains relevant if sequencing detects only one pathogenic allele. Large deletions affecting TNNI3 would be biologically plausible but were not established as a common mechanism in the retrieved evidence.

## 5. Environmental and lifestyle information

DCM2A is genetic rather than infectious, toxic, occupational, or radiation-induced. No pathogen is causally implicated. Standard management should nevertheless exclude potentially reversible contributors such as myocarditis, endocrine/metabolic disease, nutritional deficiency, tachyarrhythmia, and toxic exposure. For genetically susceptible DCM generally, limiting alcohol and avoiding cocaine, amphetamines, and unnecessary cardiotoxic drugs is recommended; moderate, clinician-directed physical activity is preferable to inactivity, but exercise must be individualized in advanced pediatric heart failure. (arnautu2024riskassessmentand pages 21-23, mestroni2014geneticcausesof pages 6-8)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** two damaging TNNI3 alleles.
2. **Transcript/protein defect:** nonsense-mediated decay or unstable/truncated transcript causes absent or markedly reduced cTnI.
3. **Sarcomeric defect:** the troponin complex loses normal inhibition of actin–myosin interaction at low cytosolic calcium and normal modulation of thin-filament activation.
4. **Cellular dysfunction:** abnormal calcium–myofilament coupling, impaired relaxation/contractile reserve, inefficient force production, and cardiomyocyte stress.
5. **Tissue remodeling:** chamber dilation, reduced systolic performance, neurohormonal activation, secondary valvular regurgitation, and potentially fibrosis/arrhythmia.
6. **Clinical endpoint:** severe infantile heart failure, cardiogenic shock, mechanical-support dependence, transplantation, or death. (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 5-8, sorrentino2023homozygoustnni3mutations pages 2-4)

The first two steps are directly supported in DCM2A myocardium; detailed calcium, metabolic, immune, and fibrosis pathways are largely inferred from troponin biology and general DCM. It would be inappropriate to assign a specific Wnt, MAPK, mTOR, or PI3K–AKT driver to human DCM2A without direct evidence.

### Cells, tissues, and ontology suggestions

- **Primary cell:** cardiac muscle cell/cardiomyocyte, **CL:0000746** (cardiac muscle cell; ontology releases may also expose more specific ventricular cardiomyocyte descendants).
- **GO biological processes:** cardiac muscle contraction **GO:0060048**; regulation of cardiac muscle contraction **GO:0055117**; sarcomere organization **GO:0045214**; muscle filament sliding **GO:0030049**; calcium-mediated signaling **GO:0019722**; regulation of heart contraction **GO:0008016**.
- **GO cellular components:** sarcomere **GO:0030017**; myofibril **GO:0030016**; troponin complex **GO:0005861**; thin filament **GO:0005865**.

### Molecular profiling and advanced technologies

Disease-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or integrated multi-omic studies were not found. Direct myocardial assays showing absent TNNI3 and increased TNNI1 are the most relevant expression/protein observations. RNA sequencing can be diagnostically valuable for suspected splice variants, but it is not a routine validated biomarker. No DCM2A-specific CRISPR screen was identified. (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 5-8)

## 7. Anatomical structures affected

- **Primary organ:** heart, **UBERON:0000948**.
- **Primary chamber:** left ventricle, **UBERON:0002084**; biventricular disease can develop.
- **Tissue:** myocardium **UBERON:0002349**, particularly ventricular myocardium.
- **Cell:** ventricular cardiomyocyte/cardiac muscle cell.
- **Subcellular site:** sarcomere, myofibril, thin filament, troponin complex.
- **Secondary organs:** lungs through pulmonary congestion/hypertension; liver, kidneys, and brain through advanced low-output failure or treatment complications. The reported ischemic stroke occurred during advanced support and is not necessarily a primary DCM2A phenotype. (sorrentino2023homozygoustnni3mutations pages 4-5)
- **Lateralization:** not applicable; myocardial disease is not unilateral, although LV dysfunction predominates.

## 8. Temporal development

Onset is usually congenital, neonatal, or in the first year of life; six- and seven-month presentations are documented. The course is chronic but often rapidly progressive rather than episodic. A useful clinical staging model is: genotype-positive/presymptomatic → subtle chamber or functional abnormality → overt DCM with reduced EF → advanced/refractory heart failure → VAD/transplantation or death. Homozygous null cases commonly reach advanced stages shortly after recognition. Durable spontaneous remission has not been demonstrated; improvement after transplantation reflects organ replacement rather than correction of the genotype. (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 4-5, sorrentino2023homozygoustnni3mutations pages 1-2)

The critical intervention window is therefore before or at the earliest sign of ventricular dysfunction in an at-risk sibling. Serial surveillance should not wait for symptoms.

## 9. Inheritance and population

### Inheritance

DCM2A is **autosomal recessive**. For two confirmed heterozygous parents, each pregnancy has a 25% probability of an affected child, 50% probability of a heterozygous carrier, and 25% probability of inheriting neither familial allele. Penetrance appears high for biallelic null genotypes but cannot be quantified reliably from the small, ascertainment-biased literature. Expressivity is severe and relatively consistent for null alleles, but residual-function alleles can produce variable DCM, LVNC, or restrictive phenotypes. Anticipation is not expected. Germline mosaicism has not been established but cannot be excluded after an apparently de novo result. Consanguinity is relevant but not necessary. (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 4-5, sorrentino2023homozygoustnni3mutations pages 5-8)

### Epidemiology

No population prevalence or incidence is available for DCM2A. Only approximately 20 biallelic cases had been summarized by 2023, so it qualifies as ultra-rare. Variant carrier frequencies must not be converted into disease prevalence without accounting for allelic heterogeneity and penetrance. (sorrentino2023homozygoustnni3mutations pages 8-9)

For context only, general DCM prevalence estimates range widely, from 36.5 per 100,000 in older epidemiology to over 0.4% in newer imaging-based estimates; incidence near 7 per 100,000/year has been cited. These figures do **not** describe DCM2A. General pediatric DCM has a higher incidence in infancy, and one 2024 genetics review reported a molecular diagnosis in 54% of pediatric versus 27% of adult DCM. (newman2024dilatedcardiomyopathya pages 1-2, mestroni2014geneticcausesof pages 1-3, eldemire2024geneticsofdilated pages 1-3)

No reproducible ethnic, geographic, or sex enrichment has been established for DCM2A. Reported families include European and North African ancestry, reflecting case ascertainment rather than prevalence.

## 10. Diagnostics

### Clinical evaluation

1. **Echocardiography:** chamber dimensions, fractional shortening/LVEF, valvular regurgitation, RV function, and LVNC morphology.
2. **ECG and ambulatory monitoring:** conduction disease, atrial/ventricular arrhythmia, and repolarization abnormalities.
3. **Cardiac MRI:** ventricular volumes/function, LVNC, edema, and late-gadolinium enhancement when feasible and safe.
4. **Laboratory assessment:** BNP/NT-proBNP and troponin for severity/injury; CBC, electrolytes, renal/liver/thyroid testing, creatine kinase, lactate, acylcarnitines, and other metabolic testing guided by age and presentation. No laboratory biomarker is specific to DCM2A.
5. **Endomyocardial biopsy:** not required for routine genetic diagnosis; consider only when myocarditis, storage disease, infiltrative disease, or an actionable histological diagnosis remains plausible.

### Genetic testing algorithm

A comprehensive cardiomyopathy panel including **TNNI3** is generally the first-line molecular test. Ensure reliable coverage of coding exons, splice boundaries, and copy-number changes. Trio WES is especially useful in severe infantile disease; WGS can detect deep-intronic and structural variants missed by panels/WES. If one allele or a suspected splice variant remains unresolved, RNA analysis from an informative tissue may help. Karyotype, FISH, chromosomal microarray, mitochondrial sequencing, and repeat-expansion testing are not first-line for isolated DCM2A but may be appropriate for syndromic presentations. A negative test does not exclude hereditary DCM. (eldemire2024geneticsofdilated pages 1-3, arnautu2024riskassessmentand pages 11-12)

The most affected individual should be tested first, followed by targeted parental segregation and cascade testing. In a national pediatric DCM cohort, 38/107 tested children (36%) had a pathogenic/likely pathogenic variant, and variant-positive children had a higher death/transplant risk (HR 2.8, 95% CI 1.3–5.8); these are general pediatric DCM data supporting routine genetic evaluation, not TNNI3-specific estimates. (eldemire2024geneticsofdilated pages 1-3)

### Differential diagnosis

Exclude myocarditis; anomalous coronary origin; congenital structural disease; tachycardia-induced cardiomyopathy; metabolic/mitochondrial disorders; Barth syndrome; carnitine deficiency; neuromuscular disease; sepsis; endocrine disease; toxic cardiomyopathy; and other monogenic DCM. Dominant TNNI3-associated hypertrophic/restrictive cardiomyopathy differs by genotype, ventricular morphology, and inheritance.

### Screening

There is no newborn biochemical screen. Siblings and other at-risk relatives require genetic counseling, targeted testing for known familial alleles, and phenotype screening with history, examination, ECG, and echocardiography. Prenatal diagnosis and preimplantation genetic testing are technically possible once both familial pathogenic variants are established.

## 11. Outcome and prognosis

Disease-specific prognosis is unfavorable for biallelic null genotypes. Early onset, severely depressed EF, escalation to inotropes/ECMO/VAD, and inability to recover ventricular function indicate high transplant/death risk. In the two 2023 patients, transplantation produced favorable early cardiac outcomes, but no DCM2A-specific five- or ten-year survival estimate exists. (sorrentino2023homozygoustnni3mutations pages 8-9, sorrentino2023homozygoustnni3mutations pages 4-5)

General pediatric DCM should not substitute for subtype-specific prognosis, although it provides context: a 2024 review cited 94% five-year survival but a 38% transplantation rate in genetically characterized pediatric disease. Broader nonischemic DCM cohorts have reported major cardiac events in about 50% over 12 years and death/transplant/VAD in 17% over eight years. (newman2024dilatedcardiomyopathya pages 1-2, eldemire2024geneticsofdilated pages 1-3)

Major morbidities include recurrent hospitalization, growth and feeding impairment, arrhythmia, thromboembolism, secondary valve regurgitation, pulmonary hypertension, end-organ dysfunction, and complications of mechanical support/transplantation. No validated DCM2A-specific prognostic biomarker exists; phenotype severity and trajectory currently dominate risk assessment.

## 12. Treatment

### Current treatment

There is no approved therapy that restores TNNI3 in DCM2A. Management should occur in a pediatric advanced-heart-failure and inherited-cardiomyopathy center.

- **Congestion:** loop diuretics; NCIT concept suggestion: Diuretic Therapy.
- **Chronic systolic failure:** age-appropriate ACE inhibitor/ARB or ARNI, evidence-based beta-blocker, mineralocorticoid-receptor antagonist, and—in selected older pediatric patients under specialist protocols—an SGLT2 inhibitor. The four-class regimen is established principally in adult HFrEF; pediatric dosing and evidence differ. (arnautu2024riskassessmentand pages 21-23, mestroni2014geneticcausesof pages 6-8)
- **Acute decompensation:** oxygen/ventilation, inotropes, vasopressors, and intensive monitoring as indicated.
- **Mechanical support:** ECMO and ventricular-assist devices as rescue or bridge to transplant; both were clinically relevant in reported DCM2A. Suggested NCIT terms: Extracorporeal Membrane Oxygenation; Ventricular Assist Device. (sorrentino2023homozygoustnni3mutations pages 4-5)
- **Transplantation:** definitive therapy for refractory end-stage disease; suggested NCIT term: Heart Transplantation.
- **Arrhythmia/device therapy:** individualized Holter surveillance, antiarrhythmics, pacing, or ICD based on phenotype. Unlike LMNA/FLNC/PLN disease, no TNNI3-specific threshold supports prophylactic ICD implantation. (arnautu2024riskassessmentand pages 21-23)
- **Supportive care:** nutrition, vaccination, psychosocial support, physical/occupational therapy for deconditioning, and transplant rehabilitation.

### Experimental and precision therapy

No DCM2A-specific interventional clinical trial was found. AAV-mediated TNNI3 replacement, transcript rescue, and genome editing are biologically plausible but remain preclinical concepts. The principal challenges are cardiac delivery, dose control, immune responses, developmental timing, and avoiding abnormal troponin stoichiometry. Genotype currently informs diagnosis, recurrence risk, family screening, and urgency—not selection of an approved TNNI3-targeted drug.

Pharmacogenomic associations involving ADRB1, GRK5, ACE, and AGTR1 have been described in broader DCM/HFrEF, but routine use to guide DCM2A therapy lacks clinical validity. (arnautu2024riskassessmentand pages 21-23)

## 13. Prevention

- **Primary prevention:** the genotype cannot be prevented after conception. Preconception counseling, carrier testing of partners in relevant families, IVF with preimplantation genetic testing, donor gametes, prenatal diagnosis, or natural conception with informed testing are reproductive options.
- **Secondary prevention:** early cascade testing and scheduled ECG/echocardiography can detect presymptomatic disease and permit earlier therapy. This is the most actionable prevention strategy. (arnautu2024riskassessmentand pages 11-12)
- **Tertiary prevention:** guideline-directed heart-failure care, vaccination, nutrition, arrhythmia/thromboembolism assessment, avoidance of cardiotoxins, and timely referral for mechanical support/transplantation.
- **Immunization:** no disease-specific vaccine; routine respiratory vaccination is valuable in medically fragile heart-failure patients.
- **Public health:** no population-wide newborn or carrier-screening program is justified by current evidence. Real-world genetic testing remains underused: only 827/101,919 newly diagnosed DCM patients (0.8%) in a large US EHR/claims study had documented testing within six months, underscoring an implementation gap, though the cohort was not DCM2A-specific. (arnautu2024riskassessmentand pages 11-12)

## 14. Other species and natural disease

No convincing naturally occurring TNNI3-biallelic DCM2A counterpart was identified in dogs, cats, livestock, or wildlife, and there is no zoonotic or transmissible component. Orthologs are present across vertebrates, reflecting conservation of cardiac thin-filament regulation, but orthology alone does not establish a natural veterinary disease.

A major curation warning is that **TNNI3K** encodes cardiac troponin-I-interacting kinase, not cardiac troponin I. Cardiac-specific Tnni3k-knockout mice develop age-progressive dysfunction, dilation, hypertrophy, fibrosis, and apoptosis involving p38 MAPK, but this is not a DCM2A model and should not be annotated as TNNI3 evidence. (qu2022knockoutofcardiac pages 7-7)

## 15. Model organisms and experimental systems

No well-validated model reproducing human biallelic TNNI3-null DCM2A was identified in the retrieved literature. Relevant platforms for future work include:

- **Knock-in/knockout mice:** suitable for chamber remodeling, hemodynamics, arrhythmia, and AAV replacement, but complete loss may cause developmental lethality and murine calcium/heart-rate physiology limits translation.
- **Zebrafish:** rapid CRISPR modeling and live cardiac imaging are advantages; duplicated genes and two-chamber physiology are limitations.
- **Patient-derived or isogenic hiPSC cardiomyocytes:** appropriate for sarcomere assembly, calcium transients, contractility, transcript rescue, and drug screening. Immaturity and fetal TNNI1 expression can obscure a disease whose biology depends on the developmental TNNI1-to-TNNI3 switch.
- **Engineered heart tissue/organoids:** can quantify force and test gene replacement in a three-dimensional context, but do not reproduce whole-organ loading, immunity, conduction, or systemic failure.

Models of heterozygous TNNI3 missense cardiomyopathy can clarify troponin biology but cannot be assumed to model biallelic null disease. Likewise, TNNI3K models are non-equivalent. (sorrentino2023homozygoustnni3mutations pages 5-8, qu2022knockoutofcardiac pages 7-7)

## Recent developments and authoritative interpretation

The key 2023 advance was consolidation of the claim that **biallelic TNNI3 null variants cause a severe neonatal/infantile DCM**, supported by two additional unrelated patients and a systematic review. The authors’ abstract states that “an increasing amount of evidence has validated the hypothesis that biallelic TNNI3 null mutations cause a severe form of neonatal dilated cardiomyopathy.” (sorrentino2023homozygoustnni3mutations pages 1-2)

Current 2024 genetic-DCM reviews emphasize that genetic testing is now integral to pediatric diagnosis, prognosis, and cascade screening, while warning that more than 200 genes have been associated with DCM but evidence is limited for many. For DCM2A, the causal claim is strongest when the phenotype is severe and early, variants are genuinely biallelic and loss-of-function, segregation is compatible, and population frequency is sufficiently low. (newman2024dilatedcardiomyopathya pages 1-2, eldemire2024geneticsofdilated pages 1-3, arnautu2024riskassessmentand pages 11-12)

The expert interpretation is therefore conservative: DCM2A is a credible but ultra-rare recessive troponinopathy with a compelling loss-of-function mechanism and severe natural history. Its immediate real-world applications are molecular diagnosis, rapid family testing, reproductive counseling, intensive presymptomatic surveillance, and early advanced-heart-failure referral. Disease-specific epidemiology, longitudinal quality-of-life data, multi-omics, validated models, and targeted therapy remain major unmet needs.

References

1. (sorrentino2023homozygoustnni3mutations pages 8-9): Ugo Sorrentino, Ilaria Gabbiato, Chiara Canciani, Davide Calosci, Chiara Rigon, Daniela Zuccarello, and Matteo Cassina. Homozygous tnni3 mutations and severe early onset dilated cardiomyopathy: patient report and review of the literature. Genes, 14:748, Mar 2023. URL: https://doi.org/10.3390/genes14030748, doi:10.3390/genes14030748. This article has 19 citations.

2. (sorrentino2023homozygoustnni3mutations pages 1-2): Ugo Sorrentino, Ilaria Gabbiato, Chiara Canciani, Davide Calosci, Chiara Rigon, Daniela Zuccarello, and Matteo Cassina. Homozygous tnni3 mutations and severe early onset dilated cardiomyopathy: patient report and review of the literature. Genes, 14:748, Mar 2023. URL: https://doi.org/10.3390/genes14030748, doi:10.3390/genes14030748. This article has 19 citations.

3. (sorrentino2023homozygoustnni3mutations pages 2-4): Ugo Sorrentino, Ilaria Gabbiato, Chiara Canciani, Davide Calosci, Chiara Rigon, Daniela Zuccarello, and Matteo Cassina. Homozygous tnni3 mutations and severe early onset dilated cardiomyopathy: patient report and review of the literature. Genes, 14:748, Mar 2023. URL: https://doi.org/10.3390/genes14030748, doi:10.3390/genes14030748. This article has 19 citations.

4. (newman2024dilatedcardiomyopathya pages 1-2): Noah A. Newman and Michael A. Burke. Dilated cardiomyopathy: a genetic journey from past to future. International Journal of Molecular Sciences, 25:11460, Oct 2024. URL: https://doi.org/10.3390/ijms252111460, doi:10.3390/ijms252111460. This article has 27 citations.

5. (sorrentino2023homozygoustnni3mutations pages 5-8): Ugo Sorrentino, Ilaria Gabbiato, Chiara Canciani, Davide Calosci, Chiara Rigon, Daniela Zuccarello, and Matteo Cassina. Homozygous tnni3 mutations and severe early onset dilated cardiomyopathy: patient report and review of the literature. Genes, 14:748, Mar 2023. URL: https://doi.org/10.3390/genes14030748, doi:10.3390/genes14030748. This article has 19 citations.

6. (eldemire2024geneticsofdilated pages 1-3): Ramone Eldemire, Luisa Mestroni, and Matthew R.G. Taylor. Genetics of dilated cardiomyopathy. Jan 2024. URL: https://doi.org/10.1146/annurev-med-052422-020535, doi:10.1146/annurev-med-052422-020535. This article has 79 citations and is from a domain leading peer-reviewed journal.

7. (sorrentino2023homozygoustnni3mutations pages 4-5): Ugo Sorrentino, Ilaria Gabbiato, Chiara Canciani, Davide Calosci, Chiara Rigon, Daniela Zuccarello, and Matteo Cassina. Homozygous tnni3 mutations and severe early onset dilated cardiomyopathy: patient report and review of the literature. Genes, 14:748, Mar 2023. URL: https://doi.org/10.3390/genes14030748, doi:10.3390/genes14030748. This article has 19 citations.

8. (arnautu2024riskassessmentand pages 11-12): Diana-Aurora Arnautu, Dragos Cozma, Ioan-Radu Lala, Sergiu-Florin Arnautu, Mirela-Cleopatra Tomescu, and Minodora Andor. Risk assessment and personalized treatment options in inherited dilated cardiomyopathies: a narrative review. Biomedicines, 12:1643, Jul 2024. URL: https://doi.org/10.3390/biomedicines12081643, doi:10.3390/biomedicines12081643. This article has 8 citations.

9. (arnautu2024riskassessmentand pages 21-23): Diana-Aurora Arnautu, Dragos Cozma, Ioan-Radu Lala, Sergiu-Florin Arnautu, Mirela-Cleopatra Tomescu, and Minodora Andor. Risk assessment and personalized treatment options in inherited dilated cardiomyopathies: a narrative review. Biomedicines, 12:1643, Jul 2024. URL: https://doi.org/10.3390/biomedicines12081643, doi:10.3390/biomedicines12081643. This article has 8 citations.

10. (mestroni2014geneticcausesof pages 6-8): Luisa Mestroni, Francesca Brun, Anita Spezzacatene, Gianfranco Sinagra, and Matthew R.G. Taylor. Genetic causes of dilated cardiomyopathy. Progress in pediatric cardiology, 37 1-2:13-18, Dec 2014. URL: https://doi.org/10.1016/j.ppedcard.2014.10.003, doi:10.1016/j.ppedcard.2014.10.003. This article has 143 citations and is from a peer-reviewed journal.

11. (bondue2018complexroadsfrom pages 19-22): Antoine Bondue, Eloisa Arbustini, Anna Bianco, Michele Ciccarelli, Dana Dawson, Matteo De Rosa, Nazha Hamdani, Denise Hilfiker-Kleiner, Benjamin Meder, Adelino F Leite-Moreira, Thomas Thum, Carlo G Tocchetti, Gilda Varricchi, Jolanda Van der Velden, Roddy Walsh, and Stephane Heymans. Complex roads from genotype to phenotype in dilated cardiomyopathy: scientific update from the working group of myocardial function of the european society of cardiology. Cardiovascular Research, 114:1287–1303, Aug 2018. URL: https://doi.org/10.1093/cvr/cvy122, doi:10.1093/cvr/cvy122. This article has 138 citations and is from a domain leading peer-reviewed journal.

12. (qu2022knockoutofcardiac pages 7-7): Hui-Lin Qu, Yue Zhang, Wei Zhang, Yaxin Zhu, and Rui-xia Xu. Knockout of cardiac troponin <scp>i‐interacting</scp> kinase leads to cardiac dysfunction and remodelling. Jul 2022. URL: https://doi.org/10.1111/1440-1681.13699, doi:10.1111/1440-1681.13699. This article has 3 citations and is from a peer-reviewed journal.

13. (mestroni2014geneticcausesof pages 1-3): Luisa Mestroni, Francesca Brun, Anita Spezzacatene, Gianfranco Sinagra, and Matthew R.G. Taylor. Genetic causes of dilated cardiomyopathy. Progress in pediatric cardiology, 37 1-2:13-18, Dec 2014. URL: https://doi.org/10.1016/j.ppedcard.2014.10.003, doi:10.1016/j.ppedcard.2014.10.003. This article has 143 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Dilated_Cardiomyopathy_2A-deep-research-falcon_artifacts/artifact-00.md)