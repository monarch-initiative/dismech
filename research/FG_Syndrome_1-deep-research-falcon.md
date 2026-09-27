---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:39:43.876323'
end_time: '2026-07-31T00:47:23.141431'
duration_seconds: 459.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: FG Syndrome 1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: FG_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FG Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FG Syndrome 1** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
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
- **Disease Name:** FG Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FG Syndrome 1** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# FG Syndrome 1: Disease-Characteristics Research Report

## Executive summary and scope

**FG syndrome 1 (FGS1)** is the molecularly defined, X-linked multiple-congenital-anomaly/neurodevelopmental disorder classically called **Opitz–Kaveggia syndrome**, caused by the recurrent germline **MED12 c.2881C>T (p.Arg961Trp; p.R961W)** variant. It must be distinguished from the older, phenotype-based label “FG syndrome,” which includes genetically heterogeneous and MED12-negative cases. Only about 3% of patients historically assigned a clinical FG-syndrome diagnosis were found to carry p.Arg961Trp in one diagnostic series. The principal evidence base remains a small cohort—23 molecularly confirmed males from 10 families—so frequencies below are descriptive, not population estimates. (clark2009fgsyndromean pages 1-2, clark2009fgsyndromean pages 7-7, clark2009fgsyndromean pages 4-6)

No substantial FGS1-specific clinical or therapeutic advances were identified from 2023–2024. Recent work on MED12 has primarily refined the wider allelic spectrum and mechanisms of Mediator-complex dysfunction rather than changing FGS1 diagnosis or care. The most relevant modern synthesis is van de Plassche and de Brouwer, published April 2021, DOI: [10.3390/genes12050663](https://doi.org/10.3390/genes12050663). Its abstract states: **“Missense variants in MED12 cause FG syndrome, Lujan-Fryns syndrome, and Ohdo syndrome, as well as non-syndromic intellectual disability (ID) in hemizygous males.”** This statement concerns the broader MED12 spectrum; the classic FGS1 diagnosis is specifically anchored to p.Arg961Trp. (graham2013med12relateddisorders pages 1-2, plassche2021med12related(neuro)developmentaldisorders pages 7-10)

| domain | finding/statistic | evidence type | interpretation/limitation |
|---|---|---|---|
| Molecular definition | FG syndrome 1 / Opitz-Kaveggia syndrome is the molecularly confirmed MED12-associated disorder caused by recurrent MED12 c.2881C>T (p.Arg961Trp, p.R961W) (clark2009fgsyndromean pages 7-7, graham2013med12relateddisorders pages 1-2) | Human clinical genetics + review | Important to distinguish from broader “FG syndrome” phenotypes that are genetically heterogeneous and often MED12-negative (clark2009fgsyndromean pages 7-7, graham2013med12relateddisorders pages 2-3) |
| Molecularly confirmed cohort | 23 affected males from 10 families with MED12 p.Arg961Trp; broader paper also discusses 30 live-born affected males in 10 families and compares 48 clinically diagnosed but mutation-negative cases (clark2009fgsyndromean pages 6-7, clark2009fgsyndromean pages 1-2) | Human cohort/case series | Denominators vary by analysis subset and by availability of records; avoid mixing molecularly confirmed cases with historical phenotypic FG cases (clark2009fgsyndromean pages 6-7, clark2009fgsyndromean pages 1-2) |
| Inheritance | X-linked disorder affecting males; heterozygous females reported as clinically unaffected and intellectually normal in the core cohort (clark2009fgsyndromean pages 6-7, clark2009fgsyndromean pages 4-6) | Human pedigree/cohort | Evidence supports male-limited expression in known families, but formal penetrance estimates are not established (clark2009fgsyndromean pages 6-7) |
| Core early phenotype | Infantile hypotonia and constipation in 23/23 affected males (clark2009fgsyndromean pages 6-7) | Human cohort/case series | Strongest recurring early clinical features; useful for recognition but not specific outside the syndromic context (clark2009fgsyndromean pages 4-6, clark2009fgsyndromean pages 6-7) |
| Neuroanatomy | Corpus callosum agenesis/hypoplasia in 13/13 imaged individuals (clark2009fgsyndromean pages 6-7) | Human imaging within cohort | High frequency among imaged patients, but denominator is only those who underwent neuroimaging (clark2009fgsyndromean pages 6-7) |
| Gastrointestinal/anorectal anomalies | Anal anomaly (fistula/stenosis/atresia) in 11/19 (clark2009fgsyndromean pages 6-7) | Human cohort/case series | Denominator reflects patients with evaluable data; severe constipation can also occur without a major structural anal defect (graham2013med12relateddisorders pages 2-3, clark2009fgsyndromean pages 6-7) |
| Cardiac anomalies | Congenital cardiac anomaly in 11/18 (clark2009fgsyndromean pages 6-7) | Human cohort/case series | Substantial but not universal; supports baseline cardiology evaluation in suspected cases (clark2009fgsyndromean pages 4-6, clark2009fgsyndromean pages 6-7) |
| Craniofacial features | Small ears in 12/13 where specifically measured/supported (clark2009fgsyndromean pages 2-3) | Human cohort/case series | One of the more discriminating facial findings, but facial gestalt remains composite rather than single-feature based (clark2009fgsyndromean pages 6-7, clark2009fgsyndromean pages 4-6) |
| Head size | Macrocephaly reported with denominator variation: 15/18 in one summary, 7/18 absolute macrocephaly in another analysis (clark2009fgsyndromean pages 2-3, clark2009fgsyndromean pages 6-7) | Human cohort/case series | Variation likely reflects different definitions/ascertainment (absolute vs relative macrocephaly, age-specific data); should be reported with denominator and wording preserved (clark2009fgsyndromean pages 6-7, clark2009fgsyndromean pages 2-3) |
| Diagnostic performance | Historical clinical algorithm for targeted MED12 p.Arg961Trp testing showed 100% sensitivity and 90% specificity (clark2009fgsyndromean pages 1-2) | Human diagnostic study | Useful as historical triage, but modern practice generally prioritizes sequencing-based diagnosis; performance derived from limited retrospective cohorts (clark2009fgsyndromean pages 7-7, clark2009fgsyndromean pages 1-2) |
| Mechanism: immediate-early genes | In patient EBV-immortalized lymphoblastoid cells, MED12 p.Arg961Trp dysregulated immediate-early genes, with JUN downregulation and FOS upregulation; promoter Pol II/MED12 recruitment paralleled expression changes (donnio2017med12relatedxliddisorders pages 10-14) | Human patient-cell functional study | Mechanistic evidence is from lymphoblastoid cells, so tissue relevance to brain/gut/heart phenotypes is inferential rather than directly demonstrated (donnio2017med12relatedxliddisorders pages 10-14) |
| Mechanism: SHH/GLI3 | In patient lymphoblast cell lines, MED12-related XLID variants including FG-associated p.Arg961Trp showed elevated GLI3-dependent SHH target-gene transcripts such as CREB5, BMP4, and NEUROG2 (srivastava2019dysregulationsofsonic pages 1-2) | Human patient-cell functional study | Supports pathway-selective transcriptional dysregulation; does not fully explain organ-specific manifestations or phenotypic variability (plassche2021med12related(neuro)developmentaldisorders pages 7-10, srivastava2019dysregulationsofsonic pages 1-2) |
| Mechanistic synthesis | Expert review concludes p.Arg961Trp causes selective MED12 pathway dysfunction affecting enhancer/transcriptional control rather than complete loss of MED12 function (plassche2021med12related(neuro)developmentaldisorders pages 7-10, plassche2021med12related(neuro)developmentaldisorders pages 6-7) | Expert review/mechanistic synthesis | Current model integrates REST/IEG/SHH findings, but no unified causal chain has been proven across all affected tissues (plassche2021med12related(neuro)developmentaldisorders pages 7-10, plassche2021med12related(neuro)developmentaldisorders pages 6-7) |
| Prognosis/natural history | Early deaths/deceased male infants occurred in many families, but after infancy prognosis improves; some affected males were functioning well in the 5th-6th decades and hypotonia may improve with age (clark2009fgsyndromean pages 6-7) | Human natural history within cohort | Mortality is concentrated early; long-term adult survival is clearly possible, but formal survival curves are unavailable (clark2009fgsyndromean pages 6-7) |
| Treatment landscape | No disease-modifying therapy, validated biomarker-directed treatment, or FG syndrome 1-specific interventional clinical trial was identified; management is supportive and multidisciplinary (graham2013med12relateddisorders pages 2-3, clark2009fgsyndromean pages 6-7) | Review + cohort-based expert management | Current care targets complications and development rather than MED12-specific molecular correction; evidence base is largely expert opinion and case-series practice (graham2013med12relateddisorders pages 2-3) |


*Table: This table summarizes the most actionable evidence for molecularly confirmed FG syndrome 1, including defining variant, cohort size, major phenotype frequencies, mechanism, diagnostic performance, prognosis, and treatment gaps. It is useful for separating MED12 p.Arg961Trp-associated disease from the broader heterogeneous FG phenotype.*

## 1. Disease information

### Definition and history

FGS1 is a congenital, lifelong Mendelian disorder characterized by developmental delay/intellectual disability, congenital hypotonia, severe constipation or anorectal abnormalities, characteristic craniofacial morphology and behavior, and variable brain, cardiac, skeletal, ocular, and genitourinary anomalies. Opitz and Kaveggia originally described five affected males—three brothers and two male first cousins—in 1974. The causal recurrent MED12 variant was established in 2007. (clark2009fgsyndromean pages 1-2, graham2013med12relateddisorders pages 1-2)

### Identifiers and synonyms

- **OMIM:** **305450**, FG syndrome 1/Opitz–Kaveggia syndrome.
- **Causal gene:** **MED12**, OMIM **300188**, Xq13.
- **Synonyms:** FG syndrome type 1; FGS1; Opitz–Kaveggia syndrome; FG syndrome, MED12-related.
- **MONDO:** A dedicated current MONDO identifier could not be verified from the retrieved primary literature; a knowledge-base ingest should resolve the live MONDO release rather than infer an identifier.
- **Orphanet:** A current subtype-specific number was not verified in the retrieved evidence.
- **ICD-10/ICD-11 and MeSH:** No specific FGS1 code was established. Cases are generally represented under broader congenital-malformation, syndromic intellectual-disability, or rare genetic-disease categories.

The evidence summarized here is **aggregated disease-level literature**, mostly pedigrees, dysmorphology examinations, records, imaging, and patient-derived cell experiments—not individual EHR data.

## 2. Etiology

### Cause and genetic risk

FGS1 is caused by the germline hemizygous **MED12 NM_005120.3:c.2881C>T, p.(Arg961Trp)** missense variant in affected males. It is an X-linked disorder: transmission through heterozygous females produces at-risk sons, while male-to-male transmission does not occur. No environmental, infectious, lifestyle, occupational, or toxic cause has been demonstrated. (clark2009fgsyndromean pages 6-7, clark2009fgsyndromean pages 7-7, graham2013med12relateddisorders pages 1-2)

The core cohort found clinically unaffected, intellectually normal heterozygous females. This supports sex-dependent expression, probably influenced by X-inactivation, but does not establish a numerical penetrance estimate for every carrier population. Expressivity among affected males is variable, particularly for congenital malformations and intellectual severity. No validated modifier gene, protective allele, founder haplotype, anticipation, or reproducible germline-mosaicism rate has been defined. (clark2009fgsyndromean pages 6-7)

### Protective factors and gene–environment interaction

No genetic or environmental factor is known to prevent expression in a hemizygous male. No reproducible gene–environment interaction has been reported. Good nutrition, early therapy, constipation control, and treatment of cardiac or feeding complications can reduce secondary morbidity but are not etiologic protection.

## 3. Phenotypes

The best quantitative data derive from incompletely assessed subsets of 23 confirmed males; denominators therefore vary. (clark2009fgsyndromean pages 4-6, clark2009fgsyndromean pages 6-7)

| Phenotype | Type, onset, frequency/course | Suggested HPO term |
|---|---|---|
| Developmental delay/intellectual disability | Neurodevelopmental sign; childhood recognition; borderline to severe, most tested IQ values below 70; lifelong | HP:0001263; HP:0001249 |
| Congenital hypotonia | Sign; neonatal; 23/23 in the main cohort; often improves with age | HP:0008936 |
| Feeding difficulty | Symptom; neonatal/infancy; frequent and sometimes requires nasogastric or gastrostomy feeding | HP:0011968 |
| Constipation/GI dysmotility | Symptom; infancy onward; reported in all 23; chronic and sometimes severe | HP:0002019; HP:0012450 |
| Anal stenosis, atresia, or fistula | Congenital malformation; 11/19 evaluable | HP:0002025; HP:0004378; HP:0010447 |
| Corpus-callosum agenesis/hypoplasia | Imaging/anatomic sign; congenital; 13/13 imaged | HP:0001274; HP:0002079 |
| Congenital heart defect | Malformation; congenital; 11/18 evaluable, including septal defects | HP:0001627; HP:0001631; HP:0001629 |
| Macrocephaly/relative macrocephaly | Physical sign; infancy/childhood; ascertainment varies—15/18 in one summary but 7/18 for absolute macrocephaly in another analysis | HP:0000256; HP:0011451 |
| Characteristic face | Long/narrow face, tall or prominent forehead, frontal hair upsweep, puffy eyelids, open mouth, small low-set ears | HP:0000276; HP:0011220; HP:0000286; HP:0000194; HP:0000369 |
| Small ears | Physical sign; congenital; 12/13 in one measured subset | HP:0008551 |
| Hand/skeletal findings | Broad thumbs, fetal pads, syndactyly, pectus or vertebral/rib anomalies, contractures, hip dysplasia, limited elbow supination; variable | HP:0011304; HP:0001212; HP:0001159; HP:0001371 |
| Ocular abnormalities | Clinical sign; approximately 10 patients in the principal series; optic-nerve hypoplasia reported | HP:0001098; HP:0000609 |
| Speech/language impairment | Developmental/behavioral; articulation, syntax, pragmatics and intonation affected; often functionally important | HP:0000750; HP:0002465 |
| Behavioral phenotype | Affable/eager-to-please, talkative; hyperactivity, short attention span, anxiety, frustration, and insistence on sameness may coexist | HP:0000752; HP:0000736; HP:0000729 |

Characteristic facies, affable behavior, and infantile hypotonia/feeding difficulty/constipation were each reported in all 13 subjects in one deeply characterized subset; congenital anomalies occurred in 11/13. These figures are vulnerable to referral and publication bias. (clark2009fgsyndromean pages 2-3, clark2009fgsyndromean pages 3-4)

Quality-of-life studies using EQ-5D, SF-36, PROMIS, or an FGS1-specific instrument were not found. Major burdens are communication impairment, dependence in daily living, chronic bowel dysfunction, anxiety with transitions, mobility limitations, feeding problems, sleep disturbance, and consequences of congenital anomalies. Socialization may be a relative strength. (graham2013med12relateddisorders pages 2-3)

## 4. Genetic and molecular information

- **Gene:** MED12, mediator complex subunit 12; Xq13; HGNC symbol **MED12**.
- **Defining FGS1 variant:** c.2881C>T, p.Arg961Trp, missense; germline and hemizygous in affected males.
- **Population frequency:** No numerical gnomAD frequency was established in the retrieved evidence. Its recurrence in affected pedigrees, segregation, rarity, and functional evidence support pathogenicity; a current clinical report should query the live gnomAD and ClinVar releases.
- **Functional class:** Not simple whole-gene loss of function. Evidence favors a **pathway-selective altered-function/hypomorphic transcriptional-regulatory defect**. Complete MED12 loss has broader and often developmentally severe consequences. (plassche2021med12related(neuro)developmentaldisorders pages 7-10, plassche2021med12related(neuro)developmentaldisorders pages 6-7)

Other MED12 variants cause **different allelic disorders**, including Lujan syndrome—classically p.Asn1007Ser—X-linked Ohdo syndrome and broader male or female neurodevelopmental phenotypes. Protein-truncating MED12 variants in females can cause Hardikar syndrome or other severe syndromic presentations and should not automatically be called FGS1. (graham2013med12relateddisorders pages 1-2, plassche2021med12related(neuro)developmentaldisorders pages 7-10)

No validated FGS1 modifier gene or disease-specific epigenetic signature is known. Large deletions, duplications, translocations, aneuploidy, repeat expansions, mitochondrial variants, and somatic MED12 mutations are **not** the defining cause of FGS1.

## 5. Environmental information

Environmental toxins, radiation, pollution, diet, smoking, alcohol, exercise, occupational exposures, and infectious agents have no established causal role. Environmental care affects complications: inadequate hydration or mobility can worsen constipation, and poorly structured transitions may exacerbate anxiety and behavior. These are management interactions, not demonstrated etiologic gene–environment effects. FGS1 is neither infectious nor zoonotic.

## 6. Mechanism and pathophysiology

### Upstream molecular defect

MED12 is part of the Mediator kinase module and helps couple transcription factors and regulatory signals to RNA polymerase II. p.Arg961Trp does not appear to abolish all MED12 functions; it selectively impairs recruitment or response at particular regulatory complexes. MED12 loss can reduce super-enhancer capacity by approximately 50% and disturb enhancer–promoter interactions, although these broader loss experiments are not equivalent to FGS1. (plassche2021med12related(neuro)developmentaldisorders pages 7-10, plassche2021med12related(neuro)developmentaldisorders pages 6-7)

### Supported pathway effects

1. **Immediate-early genes and Pol II recruitment—human patient cells.** In EBV-immortalized lymphoblastoid cells from p.Arg961Trp patients, **JUN was downregulated and FOS upregulated**. Chromatin immunoprecipitation showed that MED12 and RNA polymerase II promoter recruitment tracked these changes; impaired TCF4 recruitment was observed at JUN, while altered ELK-factor occupancy occurred at FOS. This supports stimulus-responsive transcriptional dysregulation. DOI: [10.1093/hmg/ddx099](https://doi.org/10.1093/hmg/ddx099), published June 2017. (donnio2017med12relatedxliddisorders pages 10-14)

2. **SHH–GLI3 signaling—patient cells and rescue experiments.** MED12 normally constrains GLI3-dependent Sonic Hedgehog transcription. Patient lymphoblast lines carrying MED12 XLID variants, including p.Arg961Trp, had increased transcripts of GLI3-regulated targets including **CREB5, BMP4, and NEUROG2**. p.Arg961Trp failed to restore normal SHH inhibition in a MED12-null experimental setting and showed reduced CDK8 recruitment at GLI3 sites while retaining recruitment at unrelated PPARγ targets. DOI: [10.1002/mgg3.569](https://doi.org/10.1002/mgg3.569), published February 2019. (srivastava2019dysregulationsofsonic pages 8-9, plassche2021med12related(neuro)developmentaldisorders pages 7-10, srivastava2019dysregulationsofsonic pages 1-2)

3. **REST/neural-gene repression.** Experimental rescue studies indicate that p.Arg961Trp fails to restore REST-mediated silencing while retaining β-catenin rescue capacity. Unscheduled derepression of neural genes could disrupt neuronal differentiation. This effect appears kinase-independent and therefore differs mechanistically from the CDK8-dependent SHH defect. (plassche2021med12related(neuro)developmentaldisorders pages 6-7)

### Proposed causal chain

**Germline MED12 p.Arg961Trp → selective disruption of signal-responsive Mediator assembly/recruitment → altered Pol II occupancy, immediate-early-gene expression, REST repression, and SHH/GLI3 developmental transcription → abnormal neurodevelopment and morphogenesis → intellectual disability, hypotonia, corpus-callosum, craniofacial, anorectal, cardiac, and skeletal phenotypes.** The downstream organ links are biologically plausible but not proven directly in fetal human brain, enteric nervous system, heart, or anorectal tissue.

Suggested annotations include **GO:0016592 mediator complex; GO:0006357 regulation of transcription by RNA polymerase II; GO:0007224 smoothened signaling pathway; GO:0045664 regulation of neuron differentiation; GO:0007417 central nervous system development; GO:0060536 cartilage morphogenesis**. Candidate cell types—not demonstrated selective targets—include neural progenitor cell (**CL:0011020**), neuron (**CL:0000540**), enteric neuron (**CL:0007011**), cardiomyocyte (**CL:0000746**), and chondrocyte (**CL:0000138**).

No FGS1-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or multi-omic human-tissue dataset was identified. No characteristic immune, inflammatory, metabolic, mitochondrial, aggregation, fibrosis, or tissue-necrosis mechanism has been demonstrated.

## 7. Anatomical structures affected

- **Nervous system:** cerebral commissures, especially corpus callosum; pituitary/sella and optic nerve can be abnormal. Suggested UBERON: **UBERON:0002336 corpus callosum**, **UBERON:0000007 pituitary gland**, **UBERON:0000966 retina**, **UBERON:0001908 optic nerve**.
- **Digestive/anorectal system:** anus, distal bowel, and functional intestinal motility; UBERON: **UBERON:0001245 anus**, **UBERON:0000160 intestine**, **UBERON:0001988 rectum**.
- **Cardiovascular:** congenital structural heart disease; **UBERON:0000948 heart**.
- **Musculoskeletal:** skull, vertebrae/ribs, chest wall, joints, hips, hands/thumbs; **UBERON:0003129 skull**, **UBERON:0002416 vertebral column**, **UBERON:0001464 hand**.
- **Craniofacial and ear structures:** face and external ear; **UBERON:0001456 face**, **UBERON:0003102 external ear**.

The relevant subcellular site is principally the **nucleus** and chromatin-associated Mediator/transcription machinery: **GO:0005634 nucleus**, **GO:0000785 chromatin**, **GO:0016592 mediator complex**. No characteristic lateralization has been reported. (clark2009fgsyndromean pages 4-6, clark2009fgsyndromean pages 6-7)

## 8. Temporal development

FGS1 begins prenatally as a developmental disorder. Hypotonia, feeding problems, constipation, dysmorphism, cardiac disease, and anorectal malformations may be apparent neonatally; developmental and behavioral differences emerge during infancy and childhood. Facial recognition may be easiest in early childhood. (clark2009fgsyndromean pages 4-6, clark2009fgsyndromean pages 6-7)

The course is chronic and lifelong, not episodic or relapsing-remitting. Congenital malformations are structurally stable unless corrected; hypotonia often improves with age, while intellectual, speech, and adaptive limitations persist. No formal stages, progression rate, remission pattern, or validated critical therapeutic window has been defined, although early feeding, cardiac, bowel, developmental, speech, and vision intervention is clinically important. Some children achieve walking only in later childhood, while surviving adults can function into their fifth or sixth decades. (clark2009fgsyndromean pages 6-7, clark2009fgsyndromean pages 3-4)

## 9. Inheritance and population

Inheritance is **X-linked**. A heterozygous carrier has a 50% probability of transmitting the variant in each pregnancy; a son inheriting it is expected to be affected, whereas a daughter inheriting it is generally an asymptomatic carrier based on the core pedigrees. An affected male transmits the variant to all daughters and no sons, assuming reproductive fitness. This is standard X-linked counseling and should be individualized for maternal mosaicism and X-inactivation.

Formal incidence, prevalence per 100,000, carrier frequency, ethnic enrichment, geographic concentration, and sex ratio from a registry are unavailable. FGS1 is ultra-rare and reported across unrelated families. The clinical cohort consists almost entirely of males because of X-linked hemizygous expression. No founder effect, consanguinity association, anticipation, or population-specific risk has been established. Early family histories often included deceased male infants, miscarriages, or X-linked intellectual disability. (clark2009fgsyndromean pages 6-7, clark2009fgsyndromean pages 1-2)

## 10. Diagnostics

### Recommended approach

Diagnosis requires a compatible phenotype plus identification of a pathogenic MED12 variant, with **p.Arg961Trp defining classic FGS1**. Modern testing should use an intellectual-disability/congenital-anomaly panel containing MED12 or exome/genome sequencing, with confirmation and segregation testing. Targeted testing for c.2881C>T is efficient where the classic phenotype or familial variant is known. A historical phenotype algorithm achieved **100% sensitivity and approximately 90% specificity** and reduced targeted testing by 74%, but it was derived from small retrospective cohorts and should not replace contemporary sequencing. (clark2009fgsyndromean pages 1-2, clark2009fgsyndromean pages 2-3)

WES/WGS is useful for atypical cases and for detecting alternative diagnoses. Copy-number analysis should be considered when sequencing is negative or the phenotype suggests a genomic disorder. Karyotyping, FISH, mitochondrial sequencing, repeat-expansion tests, biopsy, metabolomics, and liquid biopsy are not routine FGS1 tests.

### Baseline clinical evaluation

Recommended assessments include developmental and neurologic examination; brain MRI with attention to the corpus callosum; echocardiography and ECG; formal ophthalmology; hearing evaluation; feeding/swallow and nutritional assessment; gastrointestinal/anorectal examination; renal/genitourinary evaluation when indicated; and orthopedic review. Routine blood or urine chemistry has no diagnostic biomarker. (clark2009fgsyndromean pages 4-6, clark2009fgsyndromean pages 6-7)

### Differential diagnosis

Important differentials include Lujan syndrome and X-linked Ohdo syndrome caused by other MED12 variants; broader MED12-related neurodevelopmental disorders; FLNA-, UPF3B-, and BRWD3-associated X-linked intellectual disability; Xq28 duplication syndromes; fragile X syndrome; Mowat–Wilson syndrome; Coffin–Siris spectrum; and other syndromic causes of hypotonia, constipation, macrocephaly, callosal abnormality, and anal or cardiac malformations. A MED12-negative patient with nonspecific “FG-like” findings should not automatically retain an FGS1 label. (clark2009fgsyndromean pages 7-7, graham2013med12relateddisorders pages 2-3, graham2013med12relateddisorders pages 1-2)

There is no population newborn screen. Cascade testing of relatives is appropriate after molecular confirmation.

## 11. Outcome and prognosis

Early mortality occurred in 8 of the 10 reported families, although the literature does not provide a reliable disease-specific mortality rate or survival curve. Congenital cardiac, respiratory, feeding, and gastrointestinal complications likely contribute, but causes cannot be assigned uniformly. Among survivors beyond infancy, mortality did not appear markedly elevated in the small series, and three males were reportedly functioning into their fifth or sixth decades. (clark2009fgsyndromean pages 6-7)

Long-term morbidity includes intellectual and speech disability, chronic constipation, anxiety/behavioral dysregulation, sleep disturbance, orthopedic problems, and residual consequences of congenital anomalies. Recovery from the underlying disorder is not expected, but hypotonia, mobility, communication, comfort, and participation may improve. No validated molecular prognostic biomarker or FGS1-specific quality-of-life statistic exists.

## 12. Treatment

There is **no disease-modifying, gene, RNA, cell, targeted, or approved MED12-directed therapy** for FGS1. No FGS1-specific interventional clinical trial or treatment-response rate was identified. Care is individualized and multidisciplinary. (graham2013med12relateddisorders pages 2-3, clark2009fgsyndromean pages 6-7)

- Feeding therapy, nutritional support, and gastrostomy when required — suggested **MAXO:0001006 nutritional therapy**, **MAXO:0001175 gastrostomy**.
- Aggressive constipation management, reflux treatment, and evaluation for structural anorectal disease; surgery where indicated — **MAXO:0000088 surgical procedure**, **MAXO:0000011 therapeutic procedure**.
- Cardiology surveillance and repair of significant congenital defects — **MAXO:0000487 echocardiography**, surgical-procedure terms as appropriate.
- Physical and occupational therapy for hypotonia, mobility, contractures, and adaptive skills — **MAXO:0000015 physical therapy**, **MAXO:0000017 occupational therapy**.
- Early, sustained speech-language and augmentative-communication support — **MAXO:0000018 speech therapy**.
- Structured routines, advance warnings for transitions, educational support, and behavioral/psychological treatment for anxiety, attention problems, or sleep disturbance.
- Ophthalmic, hearing, orthopedic, neurologic, dental, and genitourinary treatment according to findings.

Reported real-world interventions include tube feeding, gastrostomy, fundoplication, congenital-heart surgery, orthopedic management, and developmental therapies. Pharmacotherapy is symptom-directed; no FGS1 pharmacogenomic guidance or evidence-based combination regimen exists. (graham2013med12relateddisorders pages 2-3, clark2009fgsyndromean pages 3-4)

## 13. Prevention

The inherited molecular defect cannot be prevented by diet, vaccination, lifestyle change, or environmental avoidance. Primary reproductive prevention options after identification of a familial variant include genetic counseling, carrier testing, preimplantation genetic testing, chorionic-villus sampling, amniocentesis, and use of donor gametes. Secondary prevention consists of early molecular diagnosis and prompt detection of cardiac, feeding, bowel, visual, hearing, and developmental complications. Tertiary prevention includes bowel regimens, nutrition, rehabilitation, communication support, safety planning, and surveillance for known congenital anomalies. No vaccine, preventive medication, public-health exposure intervention, or population screening program is applicable.

## 14. Other species and natural disease

MED12 is evolutionarily conserved in vertebrates, but no naturally occurring veterinary disorder established as an exact orthologue of human MED12 p.Arg961Trp FGS1 was identified. Consequently, no breed, VBO term, animal incidence, veterinary transmission, or zoonotic potential applies. Orthologues include **Med12** in mouse (*Mus musculus*, NCBI Taxonomy **10090**) and med12 in zebrafish (*Danio rerio*, Taxonomy **7955**); exact live NCBI Gene IDs should be resolved during database ingestion.

## 15. Model organisms and experimental systems

The strongest FGS1-specific functional evidence comes from **patient-derived EBV-immortalized lymphoblastoid cells**, promoter ChIP/qPCR, and MED12-null/rescue cellular experiments. These models demonstrate altered JUN/FOS regulation, Pol II/MED12 recruitment, REST silencing, and SHH/GLI3 target expression. Their major limitation is that lymphoblasts do not model developing cortical neurons, enteric neurons, cardiomyocytes, or anorectal mesenchyme. (plassche2021med12related(neuro)developmentaldisorders pages 7-10, plassche2021med12related(neuro)developmentaldisorders pages 6-7, srivastava2019dysregulationsofsonic pages 1-2, donnio2017med12relatedxliddisorders pages 10-14)

Conditional and reduced-expression Med12 mouse models establish that MED12 is essential for embryogenesis and tissue development, but constitutive loss is often embryonic lethal and is not equivalent to the selective p.Arg961Trp disorder. A validated knock-in model shown to reproduce the complete human FGS1 phenotype was not identified in the retrieved evidence. No established FGS1 zebrafish, Drosophila, C. elegans, organoid, or patient-iPSC neuronal model with comprehensive phenotypic validation was found. Experts have proposed isogenic induced-neuron models to distinguish pathogenic MED12-specific expression signatures, underscoring that this remains a research need rather than a clinical assay. (plassche2021med12related(neuro)developmentaldisorders pages 7-10, plassche2021med12related(neuro)developmentaldisorders pages 6-7)

## Evidence limitations and current expert assessment

The defining clinical dataset is small, familial, retrospective, and enriched for recognizable severe cases. Frequencies should therefore retain their original denominators and should not be interpreted as penetrance estimates. Mechanistic studies consistently indicate **selective transcriptional-network dysfunction**, but most were performed in lymphoblastoid or engineered cells rather than affected fetal tissues. As of the searched 2023–2024 literature, no prospective natural-history registry, standardized patient-reported outcome, validated biomarker, disease-modifying therapy, or FGS1-specific intervention trial was evident. The immediate priorities are longitudinal natural-history collection, modern variant curation, patient-derived neural and enteric models, and tissue-relevant multi-omic analysis.

### Principal sources

1. Clark RD et al. *FG syndrome, an X-linked multiple congenital anomaly syndrome: the clinical phenotype and an algorithm for diagnostic testing.* **Genetics in Medicine**, published November 2009. DOI: [10.1097/GIM.0b013e3181bd3d90](https://doi.org/10.1097/gim.0b013e3181bd3d90). (clark2009fgsyndromean pages 6-7, clark2009fgsyndromean pages 1-2)
2. Graham JM, Schwartz CE. *MED12 related disorders.* **American Journal of Medical Genetics Part A**, published November 2013. DOI: [10.1002/ajmg.a.36183](https://doi.org/10.1002/ajmg.a.36183). (graham2013med12relateddisorders pages 2-3, graham2013med12relateddisorders pages 1-2)
3. Donnio LM et al. *MED12-related XLID disorders are dose-dependent of immediate early genes (IEGs) expression.* **Human Molecular Genetics**, published June 2017. DOI: [10.1093/hmg/ddx099](https://doi.org/10.1093/hmg/ddx099). (donnio2017med12relatedxliddisorders pages 10-14)
4. Srivastava S et al. *Dysregulations of sonic hedgehog signaling in MED12-related X-linked intellectual disability disorders.* **Molecular Genetics & Genomic Medicine**, published February 2019. DOI: [10.1002/mgg3.569](https://doi.org/10.1002/mgg3.569). (srivastava2019dysregulationsofsonic pages 8-9, srivastava2019dysregulationsofsonic pages 1-2)
5. van de Plassche SR, de Brouwer APM. *MED12-Related (Neuro)Developmental Disorders: A Question of Causality.* **Genes**, published April 2021. DOI: [10.3390/genes12050663](https://doi.org/10.3390/genes12050663). (plassche2021med12related(neuro)developmentaldisorders pages 7-10, plassche2021med12related(neuro)developmentaldisorders pages 6-7)

References

1. (clark2009fgsyndromean pages 1-2): Robin Dawn Clark, John M. Graham, Michael J. Friez, Joe J. Hoo, Kenneth Lyons Jones, Carole McKeown, John B. Moeschler, F. Lucy Raymond, R. Curtis Rogers, Charles E. Schwartz, Agatino Battaglia, Michael J. Lyons, and Roger E. Stevenson. Fg syndrome, an x-linked multiple congenital anomaly syndrome: the clinical phenotype and an algorithm for diagnostic testing. Genetics in Medicine, 11:769-775, Nov 2009. URL: https://doi.org/10.1097/gim.0b013e3181bd3d90, doi:10.1097/gim.0b013e3181bd3d90. This article has 49 citations and is from a highest quality peer-reviewed journal.

2. (clark2009fgsyndromean pages 7-7): Robin Dawn Clark, John M. Graham, Michael J. Friez, Joe J. Hoo, Kenneth Lyons Jones, Carole McKeown, John B. Moeschler, F. Lucy Raymond, R. Curtis Rogers, Charles E. Schwartz, Agatino Battaglia, Michael J. Lyons, and Roger E. Stevenson. Fg syndrome, an x-linked multiple congenital anomaly syndrome: the clinical phenotype and an algorithm for diagnostic testing. Genetics in Medicine, 11:769-775, Nov 2009. URL: https://doi.org/10.1097/gim.0b013e3181bd3d90, doi:10.1097/gim.0b013e3181bd3d90. This article has 49 citations and is from a highest quality peer-reviewed journal.

3. (clark2009fgsyndromean pages 4-6): Robin Dawn Clark, John M. Graham, Michael J. Friez, Joe J. Hoo, Kenneth Lyons Jones, Carole McKeown, John B. Moeschler, F. Lucy Raymond, R. Curtis Rogers, Charles E. Schwartz, Agatino Battaglia, Michael J. Lyons, and Roger E. Stevenson. Fg syndrome, an x-linked multiple congenital anomaly syndrome: the clinical phenotype and an algorithm for diagnostic testing. Genetics in Medicine, 11:769-775, Nov 2009. URL: https://doi.org/10.1097/gim.0b013e3181bd3d90, doi:10.1097/gim.0b013e3181bd3d90. This article has 49 citations and is from a highest quality peer-reviewed journal.

4. (graham2013med12relateddisorders pages 1-2): John M. Graham and Charles E. Schwartz. Med12 related disorders. American Journal of Medical Genetics Part A, 161:2734-2740, Nov 2013. URL: https://doi.org/10.1002/ajmg.a.36183, doi:10.1002/ajmg.a.36183. This article has 97 citations.

5. (plassche2021med12related(neuro)developmentaldisorders pages 7-10): Stijn R. van de Plassche and Arjan P. M. de Brouwer. Med12-related (neuro)developmental disorders: a question of causality. Genes, 12 5:663, Apr 2021. URL: https://doi.org/10.3390/genes12050663, doi:10.3390/genes12050663. This article has 28 citations.

6. (graham2013med12relateddisorders pages 2-3): John M. Graham and Charles E. Schwartz. Med12 related disorders. American Journal of Medical Genetics Part A, 161:2734-2740, Nov 2013. URL: https://doi.org/10.1002/ajmg.a.36183, doi:10.1002/ajmg.a.36183. This article has 97 citations.

7. (clark2009fgsyndromean pages 6-7): Robin Dawn Clark, John M. Graham, Michael J. Friez, Joe J. Hoo, Kenneth Lyons Jones, Carole McKeown, John B. Moeschler, F. Lucy Raymond, R. Curtis Rogers, Charles E. Schwartz, Agatino Battaglia, Michael J. Lyons, and Roger E. Stevenson. Fg syndrome, an x-linked multiple congenital anomaly syndrome: the clinical phenotype and an algorithm for diagnostic testing. Genetics in Medicine, 11:769-775, Nov 2009. URL: https://doi.org/10.1097/gim.0b013e3181bd3d90, doi:10.1097/gim.0b013e3181bd3d90. This article has 49 citations and is from a highest quality peer-reviewed journal.

8. (clark2009fgsyndromean pages 2-3): Robin Dawn Clark, John M. Graham, Michael J. Friez, Joe J. Hoo, Kenneth Lyons Jones, Carole McKeown, John B. Moeschler, F. Lucy Raymond, R. Curtis Rogers, Charles E. Schwartz, Agatino Battaglia, Michael J. Lyons, and Roger E. Stevenson. Fg syndrome, an x-linked multiple congenital anomaly syndrome: the clinical phenotype and an algorithm for diagnostic testing. Genetics in Medicine, 11:769-775, Nov 2009. URL: https://doi.org/10.1097/gim.0b013e3181bd3d90, doi:10.1097/gim.0b013e3181bd3d90. This article has 49 citations and is from a highest quality peer-reviewed journal.

9. (donnio2017med12relatedxliddisorders pages 10-14): Lise-Marie Donnio, Baptiste Bidon, Satoru Hashimoto, Melanie May, Alexey Epanchintsev, Colm Ryan, William Allen, Anna Hackett, Jozef Gecz, Cindy Skinner, Roger E. Stevenson, Arjan P.M. de Brouwer, Charles Coutton, Christine Francannet, Pierre-Simon Jouk, Charles E. Schwartz, and Jean-Marc Egly. Med12-related xlid disorders are dose-dependent of immediate early genes (iegs) expression. Human Molecular Genetics, 26:2062–2075, Jun 2017. URL: https://doi.org/10.1093/hmg/ddx099, doi:10.1093/hmg/ddx099. This article has 33 citations and is from a domain leading peer-reviewed journal.

10. (srivastava2019dysregulationsofsonic pages 1-2): Siddharth Srivastava, Tejasvi Niranjan, Melanie M. May, Patrick Tarpey, William Allen, Anna Hackett, Pierre‐Simon Jouk, Lucy Raymond, Slyvain Briault, Cindy Skinner, Annick Toutain, Jozef Gecz, William Heath, Roger E. Stevenson, Charles E. Schwartz, and Tao Wang. Dysregulations of sonic hedgehog signaling in med12‐related x‐linked intellectual disability disorders. Molecular Genetics & Genomic Medicine, Feb 2019. URL: https://doi.org/10.1002/mgg3.569, doi:10.1002/mgg3.569. This article has 21 citations and is from a peer-reviewed journal.

11. (plassche2021med12related(neuro)developmentaldisorders pages 6-7): Stijn R. van de Plassche and Arjan P. M. de Brouwer. Med12-related (neuro)developmental disorders: a question of causality. Genes, 12 5:663, Apr 2021. URL: https://doi.org/10.3390/genes12050663, doi:10.3390/genes12050663. This article has 28 citations.

12. (clark2009fgsyndromean pages 3-4): Robin Dawn Clark, John M. Graham, Michael J. Friez, Joe J. Hoo, Kenneth Lyons Jones, Carole McKeown, John B. Moeschler, F. Lucy Raymond, R. Curtis Rogers, Charles E. Schwartz, Agatino Battaglia, Michael J. Lyons, and Roger E. Stevenson. Fg syndrome, an x-linked multiple congenital anomaly syndrome: the clinical phenotype and an algorithm for diagnostic testing. Genetics in Medicine, 11:769-775, Nov 2009. URL: https://doi.org/10.1097/gim.0b013e3181bd3d90, doi:10.1097/gim.0b013e3181bd3d90. This article has 49 citations and is from a highest quality peer-reviewed journal.

13. (srivastava2019dysregulationsofsonic pages 8-9): Siddharth Srivastava, Tejasvi Niranjan, Melanie M. May, Patrick Tarpey, William Allen, Anna Hackett, Pierre‐Simon Jouk, Lucy Raymond, Slyvain Briault, Cindy Skinner, Annick Toutain, Jozef Gecz, William Heath, Roger E. Stevenson, Charles E. Schwartz, and Tao Wang. Dysregulations of sonic hedgehog signaling in med12‐related x‐linked intellectual disability disorders. Molecular Genetics & Genomic Medicine, Feb 2019. URL: https://doi.org/10.1002/mgg3.569, doi:10.1002/mgg3.569. This article has 21 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](FG_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md)