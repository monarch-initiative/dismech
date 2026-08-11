---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-03T16:39:00.459713'
end_time: '2026-06-03T17:00:44.444553'
duration_seconds: 1303.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Branchiooculofacial Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Branchiooculofacial_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Branchiooculofacial Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Branchiooculofacial Syndrome** covering all of the
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
- **Disease Name:** Branchiooculofacial Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Branchiooculofacial Syndrome** covering all of the
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


## Comprehensive Research Report: Branchiooculofacial Syndrome (BOFS)

### Target Disease
- **Disease name:** Branchio-oculo-facial syndrome (BOFS) / Branchiooculofacial syndrome / BOF syndrome (sato2018noveltfap2amutation pages 1-3, haldemanenglert2025branchiooculofacialsyndrome pages 1-4)
- **Category:** Genetic congenital developmental disorder (min2020aheterozygousnovel pages 1-2, haldemanenglert2025branchiooculofacialsyndrome pages 4-7)
- **MONDO ID:** Not retrievable from the available full-text evidence in this run; should be added by linking to MONDO via OMIM 113620 in ontology resources.

---

## 1. Disease Information

### 1.1 Overview / definition (current understanding)
BOFS is a rare, multisystem congenital craniofacial developmental disorder classically involving **branchial cutaneous defects**, **ocular anomalies**, and **craniofacial anomalies (especially clefting)** (milunsky2008tfap2amutationsresult pages 1-2, min2020aheterozygousnovel pages 1-2). Recent curated summary text notes that **“Most individuals with branchiooculofacial syndrome (BOFS) can be diagnosed in infancy on the basis of their clinical features.”** (haldemanenglert2025branchiooculofacialsyndrome pages 4-7).

A concise definition from a molecularly confirmed family report states BOFS is **“a rare autosomal dominant disorder characterized by craniofacial, ocular, and ectodermal anomalies”** (Human Genome Variation 2018-05; URL https://doi.org/10.1038/s41439-018-0004-z) (sato2018noveltfap2amutation pages 1-3).

### 1.2 Key identifiers
- **OMIM (disease):** **113620** (milunsky2008tfap2amutationsresult pages 1-2, sato2018noveltfap2amutation pages 1-3, reiber2010additionalclinicaland pages 1-2)
- **OMIM (gene):** **TFAP2A = 107580** (sato2018noveltfap2amutation pages 1-3, haldemanenglert2025branchiooculofacialsyndrome pages 1-4)
- **Gene locus:** TFAP2A at **6p24.3** (curated summary) (haldemanenglert2025branchiooculofacialsyndrome pages 11-14). Older primary papers also report mapping as 6p21.3 (reiber2010additionalclinicaland pages 1-2).
- **Orphanet / ICD-10 / ICD-11 / MeSH:** Not present in the retrieved full-text excerpts; these require direct lookup in Orphanet/ICD/MeSH resources.

### 1.3 Synonyms / alternative names
- Branchio-oculo-facial syndrome (BOFS)
- Branchiooculofacial syndrome
- BOF syndrome (haldemanenglert2025branchiooculofacialsyndrome pages 1-4)

### 1.4 Evidence source type
The BOFS knowledge here is derived mainly from **aggregated disease-level resources** (GeneReviews-style summary excerpts), **cohort studies**, and **case reports**, rather than EHR-derived cohorts (haldemanenglert2025branchiooculofacialsyndrome pages 1-4, milunsky2011genotype–phenotypeanalysisof pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** heterozygous pathogenic variants affecting **TFAP2A** (autosomal dominant), including coding variants, deletions/duplications, mosaicism, and regulatory structural variants that disrupt TFAP2A enhancer contacts (milunsky2008tfap2amutationsresult pages 1-2, milunsky2011genotype–phenotypeanalysisof pages 1-2, shi2023structuralvariantsinvolved pages 1-2).

Direct human genetic evidence for causality includes discovery of a **3.2 Mb deletion** including TFAP2A and multiple **de novo TFAP2A missense variants** in BOFS patients (AJHG 2008-05; URL https://doi.org/10.1016/j.ajhg.2008.03.005) (milunsky2008tfap2amutationsresult pages 1-2).

### 2.2 Risk factors
- **Genetic risk:** having a TFAP2A pathogenic variant (autosomal dominant transmission). Approximately **40%–50%** of diagnosed individuals have an affected parent and **50%–60%** have **de novo** TFAP2A pathogenic variants (haldemanenglert2025branchiooculofacialsyndrome pages 11-14).
- **Environmental risk factors:** none were identified in the retrieved evidence; BOFS is primarily genetic (haldemanenglert2025branchiooculofacialsyndrome pages 1-4, min2020aheterozygousnovel pages 1-2).

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the available evidence.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved texts.

---

## 3. Phenotypes

### 3.1 Core phenotype domains
BOFS is defined by three major domains: **branchial defects**, **ocular anomalies**, and **craniofacial anomalies (notably cleft lip/microform cleft)** (stoetzel2009confirmationoftfap2a pages 1-2, min2020aheterozygousnovel pages 1-2).

### 3.2 Phenotype frequencies (recent aggregated estimates)
A curated summary incorporating a large ophthalmic review (172 individuals) reports approximate frequencies:
- **Cervical cutaneous defects:** ~**90%**
- **Infra-/supra-auricular defects:** ~**60%**
- **Cleft lip / microform cleft lip (with or without cleft palate):** **99%** (no isolated cleft palate reported)
- **Hearing loss:** ~**70%**
- **Renal structural anomalies:** ~**35%**
- **Thymic anomalies:** ~**35%**
- **Ocular findings (172-case review):** nasolacrimal duct stenosis **57%**, coloboma **46%**, anophthalmia/microphthalmia **37%**, cataract **16%**, strabismus **14%**, myopia **12%** (haldemanenglert2025branchiooculofacialsyndrome pages 4-7).

Additional tabulated frequencies from older clinical compilation include:
- **Ectodermal anomalies:** **37/62 (60%)**
- **Dental anomalies:** **23/55 (42%)**
- **Prematurely gray hair:** **20/53 (38%)**
- **Malformed middle/inner ear:** **10/27 (37%)**
- **Kidney anomaly:** **17/48 (35%)**
- **Growth retardation:** **18/62 (29%)**
- **Congenital heart disease:** **3/37 (8%)**
- **Intellectual disability/mental retardation:** **8/56 (14%)** (lugli2015earlydiagnosisof pages 4-4).

### 3.3 Onset, severity, progression
- **Typical onset:** congenital; often clinically diagnosable in infancy (haldemanenglert2025branchiooculofacialsyndrome pages 4-7, min2020aheterozygousnovel pages 1-2).
- **Severity:** highly variable, including “non-classical” ocular-predominant presentations (ng2019tfap2amutationin pages 4-4).
- **Course:** generally lifelong congenital anomalies; progression is not a defining feature, but functional outcomes depend on vision/hearing and craniofacial complications (thomeer2010clinicalpresentationand pages 4-6, haldemanenglert2025branchiooculofacialsyndrome pages 9-11).

### 3.4 Quality-of-life (QoL) impacts
Direct QoL instrument data (EQ-5D/SF-36) were not identified. However, the functional burden is implied by frequent **visual and hearing handicaps** and by explicit psychosocial surveillance recommendations: **“Monitor for signs of low self-esteem & other psychologic issues.”** (haldemanenglert2025branchiooculofacialsyndrome pages 11-14, milunsky2011genotype–phenotypeanalysisof pages 7-7).

### 3.5 Suggested HPO terms (examples)
Representative HPO mappings (non-exhaustive; based on described phenotypes in retrieved evidence):
- Branchial/cutaneous: **Branchial fistula** (HP:0009795); **Cervical sinus** (HP:0009796); **Aplasia cutis congenita** (if present); **Ectopic thymus** (no single canonical HP term; map via “Thymus hypoplasia/abnormality” as appropriate) (thomeer2010clinicalpresentationand pages 4-6, lugli2015earlydiagnosisof pages 1-3).
- Craniofacial: **Cleft lip** (HP:0000204); **Cleft palate** (HP:0000175); **Broad nasal bridge** (HP:0000431); **Hypertelorism** (HP:0000316); **Telecanthus** (HP:0000506); **Dolichocephaly** (HP:0000268) (haldemanenglert2025branchiooculofacialsyndrome pages 4-7, min2020aheterozygousnovel pages 1-2).
- Ocular: **Microphthalmia** (HP:0000568); **Anophthalmia** (HP:0000528); **Coloboma** (HP:0000589); **Congenital cataract** (HP:0000519); **Strabismus** (HP:0000486); **Nasolacrimal duct obstruction** (HP:0000579) (haldemanenglert2025branchiooculofacialsyndrome pages 4-7, min2020aheterozygousnovel pages 1-2).
- Auditory/temporal bone: **Hearing impairment** (HP:0000365); **Conductive hearing impairment** (HP:0000405); **Sensorineural hearing impairment** (HP:0000407); **Abnormality of the ossicles** (HP:0000380) (thomeer2010clinicalpresentationand pages 4-6).
- Renal: **Renal agenesis** (HP:0000104); **Multicystic dysplastic kidney** (HP:0000003); **Vesicoureteral reflux** (HP:0000076) (milunsky2011genotype–phenotypeanalysisof pages 9-10).
- Ectodermal: **Premature graying of hair** (HP:0002216); **Dental anomalies** (HP:0000164); **Nail dystrophy** (HP:0002164) (lugli2015earlydiagnosisof pages 4-4).

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene(s)
- **TFAP2A** (Transcription Factor AP-2 Alpha), OMIM **107580**; BOFS OMIM **113620** (sato2018noveltfap2amutation pages 1-3, haldemanenglert2025branchiooculofacialsyndrome pages 1-4).

### 4.2 Inheritance, penetrance, expressivity
- **Autosomal dominant** (haldemanenglert2025branchiooculofacialsyndrome pages 1-4, haldemanenglert2025branchiooculofacialsyndrome pages 11-14).
- **De novo rate:** approximately **50%–60%** de novo TFAP2A pathogenic variants; ~40%–50% inherited from an affected parent (haldemanenglert2025branchiooculofacialsyndrome pages 11-14).
- **Penetrance:** described as **almost complete**, with significant **intrafamilial variability** (haldemanenglert2025branchiooculofacialsyndrome pages 11-14, haldemanenglert2025branchiooculofacialsyndrome pages 4-7).
- **Mosaicism:** parental somatic/germline mosaicism is specifically highlighted as a recurrence-risk consideration (haldemanenglert2025branchiooculofacialsyndrome pages 11-14).

### 4.3 Pathogenic variant spectrum (by class)
Reported pathogenic mechanisms include:
- **Missense** (dominant class; hotspot in exons 4–5) (milunsky2011genotype–phenotypeanalysisof pages 1-2, milunsky2011genotype–phenotypeanalysisof pages 6-7)
- **Nonsense** (example: c.912C>A, p.Cys304*) (Front Pediatr 2020-07; URL https://doi.org/10.3389/fped.2020.00380) (min2020aheterozygousnovel pages 1-2)
- **Frameshift / small indels** (reported in curated summary) (haldemanenglert2025branchiooculofacialsyndrome pages 4-7)
- **Splice-altering variants** (including predicted creation of a new splice acceptor in one report) (reiber2010additionalclinicaland pages 3-5)
- **Large deletions/CNVs** including a 3.2 Mb deletion encompassing TFAP2A (milunsky2008tfap2amutationsresult pages 1-2, milunsky2011genotype–phenotypeanalysisof pages 1-2)
- **Regulatory structural variants**: an inversion disconnecting TFAP2A from enhancers (cited as causative) (shi2023structuralvariantsinvolved pages 1-2)

### 4.4 Hotspots and recurrent variants
A large cohort identified a strong hotspot in conserved exons 4–5 with multiple recurrent amino acid substitutions, including **R254** changes, **R237** changes, **E242K**, **G251E**, **R255G**, and **A256V** (milunsky2011genotype–phenotypeanalysisof pages 6-7). A separate study also reports **c.763A>G (p.Arg255Gly)** as a probable mutational hotspot (reiber2010additionalclinicaland pages 1-2).

### 4.5 Allele frequency / population data
Population allele frequencies (e.g., gnomAD) and ClinVar aggregate counts were not available in the retrieved full-text excerpts and cannot be reliably reported here.

---

## 5. Environmental Information
No environmental, lifestyle, or infectious contributors have been reported in the retrieved sources; BOFS is best supported as a genetic developmental disorder (haldemanenglert2025branchiooculofacialsyndrome pages 1-4, min2020aheterozygousnovel pages 1-2).

---

## 6. Mechanism / Pathophysiology

### 6.1 Current mechanistic model (integrating human genetics + developmental biology)
**Upstream trigger:** heterozygous TFAP2A loss-of-function or impaired regulation (coding variant, deletion, mosaicism, or enhancer disconnection) (milunsky2008tfap2amutationsresult pages 1-2, shi2023structuralvariantsinvolved pages 1-2).

**Molecular role of TFAP2A:** TFAP2A is a **retinoic acid–responsive** AP-2 family transcription factor, expressed in **premigratory and migratory neural crest cells**, regulating gene expression during embryogenesis of the **eye, ear, face, limbs, body wall, and neural tube**; it is also “required for early morphogenesis of the lens” (haldemanenglert2025branchiooculofacialsyndrome pages 11-14).

**Downstream developmental disruption:** 2024 mechanistic work shows TFAP2 paralogs regulate cranial neural crest midfacial development partly by **directly activating ALX transcription factor genes** (Alx1/Alx3/Alx4) (Development 2024-01; URL https://doi.org/10.1242/dev.202095). Loss of TFAP2 function reduces Alx transcripts and dysregulates broader midface gene regulatory network components; these changes are linked to midfacial clefts and craniofacial skeletal abnormalities in mouse and zebrafish models (nguyen2024tfap2paralogsregulate pages 1-3, nguyen2024tfap2paralogsregulate pages 7-9).

**Regulatory SV mechanism:** A high-quality 2023 structural variation paper explicitly notes that **“an inversion disconnecting TFAP2A from its enhancers causes branchiooculofacial syndrome,”** supporting that disrupted long-range enhancer–promoter regulation can phenocopy coding loss-of-function in BOFS (Nature Communications 2023-12; URL https://doi.org/10.1038/s41467-023-44034-z) (shi2023structuralvariantsinvolved pages 1-2).

### 6.2 Suggested ontology terms
**GO Biological Process (examples):**
- Neural crest cell development / differentiation / migration
- Craniofacial morphogenesis
- Eye development; lens morphogenesis
- Regulation of transcription (DNA-templated)

**Cell Ontology (CL) (examples):**
- **Cranial neural crest cell** (CNCC)

**UBERON (examples):**
- **Pharyngeal arch** derivatives (first and second pharyngeal arches)
- **Eye**, **lens**, **inner ear**, **midface**

Evidence types: human genetic causality (milunsky2008tfap2amutationsresult pages 1-2); animal model mechanistic pathway mapping (mouse + zebrafish) (nguyen2024tfap2paralogsregulate pages 1-3, nguyen2024tfap2paralogsregulate pages 7-9).

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary systems:
- **Craniofacial/orofacial** (cleft lip ± cleft palate; characteristic facial morphology) (haldemanenglert2025branchiooculofacialsyndrome pages 4-7, min2020aheterozygousnovel pages 1-2)
- **Ocular** (microphthalmia/anophthalmia, coloboma, cataract, strabismus, nasolacrimal duct obstruction) (haldemanenglert2025branchiooculofacialsyndrome pages 4-7)
- **Auditory/temporal bone** (hearing loss; middle/inner ear malformations; external canal anomalies) (thomeer2010clinicalpresentationand pages 4-6, lugli2015earlydiagnosisof pages 4-4)
Secondary/variable:
- **Renal** anomalies (~35%) (milunsky2011genotype–phenotypeanalysisof pages 9-10, haldemanenglert2025branchiooculofacialsyndrome pages 4-7)
- **Thymic** anomalies (~35%) (haldemanenglert2025branchiooculofacialsyndrome pages 4-7)
- **Ectodermal** appendages (hair, teeth, nails) (lugli2015earlydiagnosisof pages 4-4)

---

## 8. Temporal Development

- **Onset:** congenital; diagnosis often made in infancy (haldemanenglert2025branchiooculofacialsyndrome pages 4-7, min2020aheterozygousnovel pages 1-2).
- **Progression:** primarily structural/developmental anomalies; long-term course depends on corrective surgeries and sensory impairment management. No staging system is established in retrieved sources.

---

## 9. Inheritance and Population

### 9.1 Inheritance
- Autosomal dominant; 50% recurrence risk to offspring of an affected individual (haldemanenglert2025branchiooculofacialsyndrome pages 11-14).

### 9.2 Epidemiology
Robust prevalence/incidence statistics were not found in the retrieved evidence. Case-count statements indicate rarity, with older and newer summaries noting roughly **~50 cases in older literature** and **<150 well-described cases** in later reports/curated summaries (reiber2010additionalclinicaland pages 1-2, min2020aheterozygousnovel pages 1-2).

---

## 10. Diagnostics

### 10.1 Clinical diagnostic concept
Clinical diagnosis may be made by recognizing the triad of branchial, ocular, and craniofacial features; atypical presentations exist and motivate molecular confirmation (min2020aheterozygousnovel pages 1-2, lugli2015earlydiagnosisof pages 1-3).

### 10.2 Genetic testing (recommended approach)
A curated diagnostic workflow recommends:
1) **TFAP2A sequence analysis first**, and
2) if negative, **gene-targeted deletion/duplication analysis** to detect exon- or whole-gene CNVs (haldemanenglert2025branchiooculofacialsyndrome pages 1-4).

Testing options include single-gene testing, multigene panels, and exome/genome sequencing (haldemanenglert2025branchiooculofacialsyndrome pages 1-4).

### 10.3 Recent diagnostic yield / real-world implementation (2024 priority)
In an **EJHG 2024** study of individuals with **orofacial clefts plus microphthalmia/anophthalmia/coloboma (OC+MAC)**, WES provided a conclusive diagnosis in **6/17 (35.29%)**, including a **TFAP2A/BOFS** diagnosis, while CMA detected **no pathogenic/likely pathogenic CNVs** (Publication date: 2024-11; URL https://doi.org/10.1038/s41431-023-01488-5) (tacla2024molecularinvestigationin pages 1-2).

---

## 11. Outcome / Prognosis

- **Life expectancy/survival:** not reported in the retrieved evidence.
- **Morbidity drivers:** visual impairment, hearing loss, and complications of craniofacial anomalies (e.g., cleft-related feeding/speech issues; branchial sinus complications) (thomeer2010clinicalpresentationand pages 4-6, haldemanenglert2025branchiooculofacialsyndrome pages 9-11).
- **Neurodevelopment:** typically normal; intellectual disability is uncommon but reported (~14% in an older compilation) (lugli2015earlydiagnosisof pages 4-4, haldemanenglert2025branchiooculofacialsyndrome pages 4-7).
- **Cancer risk:** evidence is limited. One cohort excerpt notes a single affected individual with **medulloblastoma**, without establishing a clear predisposition; curated text states “The role of cancer surveillance is not established.” (milunsky2011genotype–phenotypeanalysisof pages 7-9, haldemanenglert2025branchiooculofacialsyndrome pages 9-11).

---

## 12. Treatment

No disease-modifying pharmacologic therapy is established in the retrieved evidence; management is supportive and surgical.

### 12.1 Surgical / interventional and supportive care
A curated summary recommends that affected children be managed by a **multispecialty craniofacial team** and notes interventions including:
- **Nasolacrimal duct surgery** for stenosis/atresia
- **Cleft lip repair** by experienced pediatric plastic surgeons
- **Orbital conformer** for anophthalmia/severe microphthalmia
- Standard-of-care management for hearing loss, renal malformations, dental manifestations, congenital heart defects (haldemanenglert2025branchiooculofacialsyndrome pages 1-4, haldemanenglert2025branchiooculofacialsyndrome pages 9-11).

A detailed otologic case series documents real-world implementation for conductive hearing loss: CT temporal bone imaging; canal/middle ear surgeries; and **bone-anchored hearing aid (BAHA)** implantation with postoperative audiometric improvement (thomeer2010clinicalpresentationand pages 4-6).

### 12.2 Suggested MAXO terms (examples)
- Cleft lip repair (surgical repair)
- Nasolacrimal duct surgery
- Hearing amplification / bone-anchored hearing device placement
- Multidisciplinary craniofacial care
- Genetic counseling

---

## 13. Prevention

BOFS prevention is primarily genetic and surveillance-based:
- **Primary prevention / reproductive options:** prenatal and preimplantation genetic testing once a familial TFAP2A pathogenic variant is identified (haldemanenglert2025branchiooculofacialsyndrome pages 11-14, haldemanenglert2025branchiooculofacialsyndrome pages 1-4).
- **Secondary prevention:** evaluation of at-risk relatives and surveillance to detect treatable complications (hearing, vision, renal) (haldemanenglert2025branchiooculofacialsyndrome pages 11-14, haldemanenglert2025branchiooculofacialsyndrome pages 9-11).
- **Tertiary prevention:** timely surgical correction and supportive therapies to minimize disability (thomeer2010clinicalpresentationand pages 4-6, haldemanenglert2025branchiooculofacialsyndrome pages 1-4).

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary BOFS analogs were identified in the retrieved evidence.

---

## 15. Model Organisms
Recent mechanistic work uses **mouse and zebrafish** models to study TFAP2 function in cranial neural crest and midfacial development, demonstrating clefting and dysregulated **ALX** pathway activity after Tfap2 perturbation (nguyen2024tfap2paralogsregulate pages 1-3, nguyen2024tfap2paralogsregulate pages 7-9).

---

## Expert synthesis / analysis (authoritative interpretation)
1) **BOFS is best conceptualized as a neural-crest–related developmental disorder (neurocristopathy)** driven by haploinsufficiency or functional impairment of TFAP2A, with broad effects on gene regulatory networks controlling facial, ocular, and ear morphogenesis (haldemanenglert2025branchiooculofacialsyndrome pages 11-14, nguyen2024tfap2paralogsregulate pages 1-3).
2) **Variant interpretation and test selection must explicitly account for both coding and non-coding mechanisms.** In addition to recurrent missense hotspots (exons 4–5), large deletions and enhancer-disconnecting inversions can cause BOFS; therefore, negative sequencing should prompt CNV/structural variant evaluation when suspicion remains high (milunsky2011genotype–phenotypeanalysisof pages 6-7, milunsky2008tfap2amutationsresult pages 1-2, shi2023structuralvariantsinvolved pages 1-2).
3) **Real-world practice increasingly relies on exome sequencing and integrated craniofacial care**, supported by a 2024 cohort demonstrating meaningful WES diagnostic yield in complex cranio-ocular phenotypes that included BOFS (tacla2024molecularinvestigationin pages 1-2) and by detailed otologic management examples showing benefit of advanced hearing interventions (thomeer2010clinicalpresentationand pages 4-6).

---

## Summary Table (for knowledge base ingestion)
| Category | Key data |
|---|---|
| Identifiers | **Disease:** Branchio-oculo-facial syndrome (BOFS), OMIM **113620**; **Gene:** **TFAP2A** (OMIM **107580**), locus **6p24.3** in recent GeneReviews-style summary; older papers also reported mapping as 6p21.3. Synonym: branchiooculofacial syndrome / BOF syndrome (haldemanenglert2025branchiooculofacialsyndrome pages 11-14, sato2018noveltfap2amutation pages 1-3, reiber2010additionalclinicaland pages 1-2) |
| Inheritance / de novo / penetrance | **Autosomal dominant**; ~**40%–50%** have an affected parent and ~**50%–60%** are due to **de novo TFAP2A** variants; penetrance described as **almost complete** with marked **intra-/interfamilial variable expressivity**; parental somatic/germline mosaicism is a recurrence-risk consideration (haldemanenglert2025branchiooculofacialsyndrome pages 11-14) |
| Hallmark phenotypes | Typical diagnosis is **congenital/infancy**. Major domains: **branchial cutaneous defects**, **ocular anomalies**, and **craniofacial/cleft phenotype**. Frequencies from aggregated BOFS summaries: cervical cutaneous defects **~90%**, infra-/supra-auricular defects **~60%**, cleft lip / microform cleft with or without cleft palate **~99%**, hearing loss **~70%**, renal structural anomalies **~35%**, thymic anomalies **~35%**, premature graying/poliosis **~35%**. Ocular frequencies from 172-case review summarized in GeneReviews: nasolacrimal duct stenosis **57%**, coloboma **46%**, anophthalmia/microphthalmia **37%**, cataract **16%**, strabismus **14%**, myopia **12%** (haldemanenglert2025branchiooculofacialsyndrome pages 4-7) |
| Additional phenotype statistics | From older BOFS tabulation: ectodermal anomalies **37/62 (60%)**; dental anomalies **23/55 (42%)**; nail anomalies **8/61 (13%)**; prematurely gray hair **20/53 (38%)**; malformed middle/inner ear **10/27 (37%)**; kidney anomaly **17/48 (35%)**; growth retardation **18/62 (29%)**; congenital heart disease **3/37 (8%)**; intellectual disability/mental retardation **8/56 (14%)**. Psychomotor development is usually normal despite sensory handicaps; developmental delay/autism are uncommon (lugli2015earlydiagnosisof pages 4-4, haldemanenglert2025branchiooculofacialsyndrome pages 4-7, milunsky2011genotype–phenotypeanalysisof pages 7-7) |
| Genetic mechanisms | BOFS is caused by **heterozygous TFAP2A** alterations. Pathogenic mechanisms include **missense SNVs** (dominant mechanism in most families), **nonsense** variants, **splice-altering** variants, **small indels/frameshifts**, **whole-/multi-exon deletions**, and **mosaicism**. A historical cohort found missense variants in **27/30 families (90%)** and one **3.2 Mb deletion** including TFAP2A; no clear genotype-phenotype correlation established (milunsky2011genotype–phenotypeanalysisof pages 1-2, haldemanenglert2025branchiooculofacialsyndrome pages 4-7) |
| Recurrent variants / hotspots | Strong hotspot in **exons 4–5** (DNA-binding/basic region), with recurrent amino-acid substitutions including **R254G/W/P (6)**, **R237G/P (3)**, **E242K (3)**, **G251E (2)**, **R255G (2)**, **A256V (3)**; recurrent **c.763A>G (p.Arg255Gly)** reported as probable hotspot. Other reported BOFS variants include **p.Arg236Pro**, **p.Leu269Pro**, **p.Glu296Lys**, **p.Cys304\***, and family-specific missense/nonsense changes. Variant clustering supports prioritizing exons 4–6 in review, but broader testing remains necessary (milunsky2011genotype–phenotypeanalysisof pages 6-7, reiber2010additionalclinicaland pages 3-5, milunsky2008tfap2amutationsresult pages 1-2, min2020aheterozygousnovel pages 1-2, thomeer2010clinicalpresentationand pages 4-6, sato2018noveltfap2amutation pages 1-3) |
| Structural/regulatory mechanisms | Structural/regulatory disruption is relevant: a 2023 Nature Communications paper cites prior evidence that **“an inversion disconnecting TFAP2A from its enhancers causes branchiooculofacial syndrome.”** This supports enhancer-domain disruption as a bona fide disease mechanism in addition to coding variants (shi2023structuralvariantsinvolved pages 1-2) |
| Mechanistic understanding | TFAP2A encodes AP-2α, a transcription factor active in **premigratory and migratory neural crest cells** and important for embryogenesis of the **eye, ear, face, limbs, body wall, and neural tube**. 2024 developmental work showed TFAP2 paralogs regulate midfacial development partly via a conserved **ALX** pathway: **Alx1/3/4** transcript levels fall with Tfap2 loss, and ChIP-seq supports direct positive regulation of ALX loci (nguyen2024tfap2paralogsregulate pages 1-3, haldemanenglert2025branchiooculofacialsyndrome pages 11-14) |
| Diagnostic workflow | Recommended order: **TFAP2A sequence analysis first**; if negative, perform **gene-targeted deletion/duplication analysis** because sequencing may miss exon- or whole-gene CNVs. Acceptable strategies include **single-gene testing**, **multigene craniofacial/ocular panels**, and **exome/genome sequencing**. Sequence analysis detects the **vast majority (>95%)** of pathogenic variants in the GeneReviews-style summary; del/dup testing accounts for a minority (**<5%**) but is still important (haldemanenglert2025branchiooculofacialsyndrome pages 1-4, haldemanenglert2025branchiooculofacialsyndrome pages 4-7) |
| Diagnostic yield evidence (recent) | In a **2024** cohort of **17** individuals with **orofacial cleft + microphthalmia/anophthalmia/coloboma (OC+MAC)**, **WES** gave a conclusive diagnosis in **6/17 (35.29%)**, including a **TFAP2A/BOFS** diagnosis; **CMA** detected **no pathogenic/likely pathogenic CNVs** in that cohort. Authors concluded **WES was the most effective molecular approach** for OC+MAC (tacla2024molecularinvestigationin pages 1-2) |
| Real-world management | Multidisciplinary craniofacial care is recommended: pediatric plastic surgery/cleft team, ENT/audiology, ophthalmology, nephrology as indicated, speech-language therapy, dental care, and psychosocial support. Interventions include **nasolacrimal duct surgery**, **cleft lip repair**, possible repair/reconstruction of branchial defects/pinnae, **orbital conformer** for anophthalmia/severe microphthalmia, and standard treatment of hearing, renal, cardiac, and dental problems (haldemanenglert2025branchiooculofacialsyndrome pages 1-4, haldemanenglert2025branchiooculofacialsyndrome pages 7-9, haldemanenglert2025branchiooculofacialsyndrome pages 9-11) |
| Real-world hearing interventions | Case-level implementation includes full audiologic workup, **CT temporal bone imaging**, canal surgery, tympanotomy/ossicular procedures, myringoplasty, meatoplasty, and **bone-anchored hearing aid (BAHA)** placement with postoperative audiometric improvement; aggressive hearing evaluation is advised because conductive, sensorineural, and mixed hearing loss all occur (thomeer2010clinicalpresentationand pages 4-6, milunsky2011genotype–phenotypeanalysisof pages 9-10) |


*Table: This table condenses the main disease-knowledge-base fields for Branchio-oculo-facial syndrome, including identifiers, phenotype frequencies, TFAP2A variant mechanisms, testing workflow, and practical management points. It emphasizes recent diagnostic and mechanistic evidence while anchoring claims to primary BOFS literature and curated summaries.*

---

## Key References (publication dates and URLs)
(These are the most central sources used in this report; additional sources are embedded in citations above.)
- Milunsky JM et al. *Am J Hum Genet.* **2008-05**. “TFAP2A mutations result in branchio-oculo-facial syndrome.” https://doi.org/10.1016/j.ajhg.2008.03.005 (milunsky2008tfap2amutationsresult pages 1-2)
- Milunsky JM et al. *Am J Med Genet A.* **2011-01**. “Genotype–phenotype analysis of the branchio-oculo-facial syndrome.” https://doi.org/10.1002/ajmg.a.33783 (milunsky2011genotype–phenotypeanalysisof pages 1-2, milunsky2011genotype–phenotypeanalysisof pages 9-10)
- Tacla MA et al. *Eur J Hum Genet.* **2024-11**. “Molecular investigation in individuals with orofacial clefts and microphthalmia-anophthalmia-coloboma spectrum.” https://doi.org/10.1038/s41431-023-01488-5 (tacla2024molecularinvestigationin pages 1-2)
- Nguyen TT et al. *Development.* **2024-01**. “TFAP2 paralogs regulate midfacial development in part through a conserved ALX genetic pathway.” https://doi.org/10.1242/dev.202095 (nguyen2024tfap2paralogsregulate pages 1-3, nguyen2024tfap2paralogsregulate pages 7-9)
- Shi J et al. *Nat Commun.* **2023-12**. “Structural variants involved in high-altitude adaptation…” (includes BOFS regulatory SV statement). https://doi.org/10.1038/s41467-023-44034-z (shi2023structuralvariantsinvolved pages 1-2)
- Thomeer HGXM et al. *Ann Otol Rhinol Laryngol.* **2010-12**. “Clinical Presentation…hearing impairment…” https://doi.org/10.1177/000348941011901204 (thomeer2010clinicalpresentationand pages 4-6)


References

1. (sato2018noveltfap2amutation pages 1-3): Taisuke Sato, Osamu Samura, Noriko Kato, Kosuke Taniguchi, Ken Takahashi, Yuki Ito, Hiroaki Aoki, Masahisa Kobayashi, Ohsuke Migita, Aikou Okamoto, and Kenichiro Hata. Novel tfap2a mutation in a japanese family with branchio-oculo-facial syndrome. Human Genome Variation, May 2018. URL: https://doi.org/10.1038/s41439-018-0004-z, doi:10.1038/s41439-018-0004-z. This article has 19 citations.

2. (haldemanenglert2025branchiooculofacialsyndrome pages 1-4): CR Haldeman-Englert and AE Lin. Branchiooculofacial syndrome. Unknown journal, 2025.

3. (min2020aheterozygousnovel pages 1-2): Jie Min, Bing Mao, Yong Wang, Xuelian He, Shuyang Gao, and Hairong Wang. A heterozygous novel mutation in tfap2a gene causes atypical branchio-oculo-facial syndrome with isolated coloboma of choroid: a case report. Frontiers in Pediatrics, Jul 2020. URL: https://doi.org/10.3389/fped.2020.00380, doi:10.3389/fped.2020.00380. This article has 8 citations.

4. (haldemanenglert2025branchiooculofacialsyndrome pages 4-7): CR Haldeman-Englert and AE Lin. Branchiooculofacial syndrome. Unknown journal, 2025.

5. (milunsky2008tfap2amutationsresult pages 1-2): Jeff M. Milunsky, Tom A. Maher, Geping Zhao, Amy E. Roberts, Heather J. Stalker, Roberto T. Zori, Michelle N. Burch, Michele Clemens, John B. Mulliken, Rosemarie Smith, and Angela E. Lin. Tfap2a mutations result in branchio-oculo-facial syndrome. American journal of human genetics, 82 5:1171-7, May 2008. URL: https://doi.org/10.1016/j.ajhg.2008.03.005, doi:10.1016/j.ajhg.2008.03.005. This article has 258 citations and is from a highest quality peer-reviewed journal.

6. (reiber2010additionalclinicaland pages 1-2): Judith Reiber, Yves Sznajer, Elena Guillén Posteguillo, Dietmar Müller, Stanislas Lyonnet, Clarisse Baumann, and Walter Just. Additional clinical and molecular analyses of tfap2a in patients with the branchio‐oculo‐facial syndrome. American Journal of Medical Genetics Part A, 152A:994-999, Apr 2010. URL: https://doi.org/10.1002/ajmg.a.33331, doi:10.1002/ajmg.a.33331. This article has 31 citations.

7. (haldemanenglert2025branchiooculofacialsyndrome pages 11-14): CR Haldeman-Englert and AE Lin. Branchiooculofacial syndrome. Unknown journal, 2025.

8. (milunsky2011genotype–phenotypeanalysisof pages 1-2): Jeff M. Milunsky, Tom M. Maher, Geping Zhao, Zhenyuan Wang, John B. Mulliken, David Chitayat, Michele Clemens, Heather J. Stalker, Mislen Bauer, Michele Burch, Sébastien Chénier, Michael L. Cunningham, Arlene V. Drack, Sandra Janssens, Audrey Karlea, Regan Klatt, Usha Kini, Ophir Klein, Augusta M. Lachmeijer, Andre Megarbane, Nancy J. Mendelsohn, Wendy S. Meschino, Geert R. Mortier, Sandhya Parkash, C. Renai Ray, Angharad Roberts, Amy Roberts, Willie Reardon, Rhonda E. Schnur, Rosemarie Smith, Miranda Splitt, Kamer Tezcan, Margo L. Whiteford, Derek A. Wong, Roberto Zori, and Angela E. Lin. Genotype–phenotype analysis of the branchio‐oculo‐facial syndrome. American Journal of Medical Genetics Part A, 155:22-32, Jan 2011. URL: https://doi.org/10.1002/ajmg.a.33783, doi:10.1002/ajmg.a.33783. This article has 81 citations.

9. (shi2023structuralvariantsinvolved pages 1-2): Jinlong Shi, Zhilong Jia, Jinxiu Sun, Xiaoreng Wang, Xiaojing Zhao, Chenghui Zhao, Fan Liang, Xinyu Song, Jiawei Guan, Xue Jia, Jing Yang, Qi Chen, Kang Yu, Qian Jia, Jing Wu, Depeng Wang, Yuhui Xiao, Xiaoman Xu, Yinzhe Liu, Shijing Wu, Qin Zhong, Jue Wu, Saijia Cui, Xiaochen Bo, Zhenzhou Wu, Minsung Park, Manolis Kellis, and Kunlun He. Structural variants involved in high-altitude adaptation detected using single-molecule long-read sequencing. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-44034-z, doi:10.1038/s41467-023-44034-z. This article has 41 citations and is from a highest quality peer-reviewed journal.

10. (stoetzel2009confirmationoftfap2a pages 1-2): C. Stoetzel, S. Riehm, V. B. Greene, V. Pelletier, J. Vigneron, Bruno Leheup, Vincent Marion, Sophie Hellé, Jean-Marc Danse, C. Thibault, Luc Moulinier, F. Veillon, and Hélène Dollfus. Confirmation of tfap2a gene involvement in branchio‐oculo‐facial syndrome (bofs) and report of temporal bone anomalies. American Journal of Medical Genetics Part A, 149A:2141-2146, Oct 2009. URL: https://doi.org/10.1002/ajmg.a.33015, doi:10.1002/ajmg.a.33015. This article has 44 citations.

11. (lugli2015earlydiagnosisof pages 4-4): Licia Lugli, Walter Just, Elisabetta Genovese, Silvia Palma, Fabrizio Ferrari, and Antonio Percesepe. Early diagnosis of branchio-oculo-facial syndrome in a patient with inner ear malformation and mild ocular involvement. Clinical Dysmorphology, 24:17–20, Jan 2015. URL: https://doi.org/10.1097/mcd.0000000000000061, doi:10.1097/mcd.0000000000000061. This article has 1 citations and is from a peer-reviewed journal.

12. (ng2019tfap2amutationin pages 4-4): Pamela Si-Min Ng, Shazia Khan, Jiin Ying Lim, Jasmine Chew-Yin Goh, Grace Xiulin Lin, Heming Wei, Ene Choo Tan, and Saumya Shekhar Jamuar. Tfap2a mutation in a child and mother with predominantly ocular anomalies: non-classical presentation of branchio-oculo-facial syndrome. Clinical Dysmorphology, 28:215-218, Oct 2019. URL: https://doi.org/10.1097/mcd.0000000000000290, doi:10.1097/mcd.0000000000000290. This article has 2 citations and is from a peer-reviewed journal.

13. (thomeer2010clinicalpresentationand pages 4-6): Henricus G. X. M. Thomeer, Tom T. H. Crins, Erik J. Kamsteeg, Wendy Buijsman, Johannes R. M. Cruysberg, Nine V. A. M. Knoers, and W. R. J. Cremers. Clinical presentation and the presence of hearing impairment in branchio-oculo-facial syndrome: a new mutation in the tfap2a gene. Annals of Otology, Rhinology & Laryngology, 119:806-814, Dec 2010. URL: https://doi.org/10.1177/000348941011901204, doi:10.1177/000348941011901204. This article has 12 citations.

14. (haldemanenglert2025branchiooculofacialsyndrome pages 9-11): CR Haldeman-Englert and AE Lin. Branchiooculofacial syndrome. Unknown journal, 2025.

15. (milunsky2011genotype–phenotypeanalysisof pages 7-7): Jeff M. Milunsky, Tom M. Maher, Geping Zhao, Zhenyuan Wang, John B. Mulliken, David Chitayat, Michele Clemens, Heather J. Stalker, Mislen Bauer, Michele Burch, Sébastien Chénier, Michael L. Cunningham, Arlene V. Drack, Sandra Janssens, Audrey Karlea, Regan Klatt, Usha Kini, Ophir Klein, Augusta M. Lachmeijer, Andre Megarbane, Nancy J. Mendelsohn, Wendy S. Meschino, Geert R. Mortier, Sandhya Parkash, C. Renai Ray, Angharad Roberts, Amy Roberts, Willie Reardon, Rhonda E. Schnur, Rosemarie Smith, Miranda Splitt, Kamer Tezcan, Margo L. Whiteford, Derek A. Wong, Roberto Zori, and Angela E. Lin. Genotype–phenotype analysis of the branchio‐oculo‐facial syndrome. American Journal of Medical Genetics Part A, 155:22-32, Jan 2011. URL: https://doi.org/10.1002/ajmg.a.33783, doi:10.1002/ajmg.a.33783. This article has 81 citations.

16. (lugli2015earlydiagnosisof pages 1-3): Licia Lugli, Walter Just, Elisabetta Genovese, Silvia Palma, Fabrizio Ferrari, and Antonio Percesepe. Early diagnosis of branchio-oculo-facial syndrome in a patient with inner ear malformation and mild ocular involvement. Clinical Dysmorphology, 24:17–20, Jan 2015. URL: https://doi.org/10.1097/mcd.0000000000000061, doi:10.1097/mcd.0000000000000061. This article has 1 citations and is from a peer-reviewed journal.

17. (milunsky2011genotype–phenotypeanalysisof pages 9-10): Jeff M. Milunsky, Tom M. Maher, Geping Zhao, Zhenyuan Wang, John B. Mulliken, David Chitayat, Michele Clemens, Heather J. Stalker, Mislen Bauer, Michele Burch, Sébastien Chénier, Michael L. Cunningham, Arlene V. Drack, Sandra Janssens, Audrey Karlea, Regan Klatt, Usha Kini, Ophir Klein, Augusta M. Lachmeijer, Andre Megarbane, Nancy J. Mendelsohn, Wendy S. Meschino, Geert R. Mortier, Sandhya Parkash, C. Renai Ray, Angharad Roberts, Amy Roberts, Willie Reardon, Rhonda E. Schnur, Rosemarie Smith, Miranda Splitt, Kamer Tezcan, Margo L. Whiteford, Derek A. Wong, Roberto Zori, and Angela E. Lin. Genotype–phenotype analysis of the branchio‐oculo‐facial syndrome. American Journal of Medical Genetics Part A, 155:22-32, Jan 2011. URL: https://doi.org/10.1002/ajmg.a.33783, doi:10.1002/ajmg.a.33783. This article has 81 citations.

18. (milunsky2011genotype–phenotypeanalysisof pages 6-7): Jeff M. Milunsky, Tom M. Maher, Geping Zhao, Zhenyuan Wang, John B. Mulliken, David Chitayat, Michele Clemens, Heather J. Stalker, Mislen Bauer, Michele Burch, Sébastien Chénier, Michael L. Cunningham, Arlene V. Drack, Sandra Janssens, Audrey Karlea, Regan Klatt, Usha Kini, Ophir Klein, Augusta M. Lachmeijer, Andre Megarbane, Nancy J. Mendelsohn, Wendy S. Meschino, Geert R. Mortier, Sandhya Parkash, C. Renai Ray, Angharad Roberts, Amy Roberts, Willie Reardon, Rhonda E. Schnur, Rosemarie Smith, Miranda Splitt, Kamer Tezcan, Margo L. Whiteford, Derek A. Wong, Roberto Zori, and Angela E. Lin. Genotype–phenotype analysis of the branchio‐oculo‐facial syndrome. American Journal of Medical Genetics Part A, 155:22-32, Jan 2011. URL: https://doi.org/10.1002/ajmg.a.33783, doi:10.1002/ajmg.a.33783. This article has 81 citations.

19. (reiber2010additionalclinicaland pages 3-5): Judith Reiber, Yves Sznajer, Elena Guillén Posteguillo, Dietmar Müller, Stanislas Lyonnet, Clarisse Baumann, and Walter Just. Additional clinical and molecular analyses of tfap2a in patients with the branchio‐oculo‐facial syndrome. American Journal of Medical Genetics Part A, 152A:994-999, Apr 2010. URL: https://doi.org/10.1002/ajmg.a.33331, doi:10.1002/ajmg.a.33331. This article has 31 citations.

20. (nguyen2024tfap2paralogsregulate pages 1-3): Timothy T. Nguyen, Jennyfer M. Mitchell, Michaela D. Kiel, Colin P. Kenny, Hong Li, Kenneth L. Jones, Robert A. Cornell, Trevor J. Williams, James T. Nichols, and Eric Van Otterloo. Tfap2 paralogs regulate midfacial development in part through a conserved alx genetic pathway. Development, Jan 2024. URL: https://doi.org/10.1242/dev.202095, doi:10.1242/dev.202095. This article has 17 citations and is from a domain leading peer-reviewed journal.

21. (nguyen2024tfap2paralogsregulate pages 7-9): Timothy T. Nguyen, Jennyfer M. Mitchell, Michaela D. Kiel, Colin P. Kenny, Hong Li, Kenneth L. Jones, Robert A. Cornell, Trevor J. Williams, James T. Nichols, and Eric Van Otterloo. Tfap2 paralogs regulate midfacial development in part through a conserved alx genetic pathway. Development, Jan 2024. URL: https://doi.org/10.1242/dev.202095, doi:10.1242/dev.202095. This article has 17 citations and is from a domain leading peer-reviewed journal.

22. (tacla2024molecularinvestigationin pages 1-2): Milena Atique Tacla, Matheus de Mello Copelli, Eleonore Pairet, Isabella Lopes Monlleó, Erlane Marques Ribeiro, Elaine Lustosa Mendes, Raphaël Helaers, Tarsis Paiva Vieira, Miikka Vikkula, and Vera Lúcia Gil-da-Silva-Lopes. Molecular investigation in individuals with orofacial clefts and microphthalmia-anophthalmia-coloboma spectrum. European journal of human genetics : EJHG, 32:1257-1266, Nov 2024. URL: https://doi.org/10.1038/s41431-023-01488-5, doi:10.1038/s41431-023-01488-5. This article has 5 citations.

23. (milunsky2011genotype–phenotypeanalysisof pages 7-9): Jeff M. Milunsky, Tom M. Maher, Geping Zhao, Zhenyuan Wang, John B. Mulliken, David Chitayat, Michele Clemens, Heather J. Stalker, Mislen Bauer, Michele Burch, Sébastien Chénier, Michael L. Cunningham, Arlene V. Drack, Sandra Janssens, Audrey Karlea, Regan Klatt, Usha Kini, Ophir Klein, Augusta M. Lachmeijer, Andre Megarbane, Nancy J. Mendelsohn, Wendy S. Meschino, Geert R. Mortier, Sandhya Parkash, C. Renai Ray, Angharad Roberts, Amy Roberts, Willie Reardon, Rhonda E. Schnur, Rosemarie Smith, Miranda Splitt, Kamer Tezcan, Margo L. Whiteford, Derek A. Wong, Roberto Zori, and Angela E. Lin. Genotype–phenotype analysis of the branchio‐oculo‐facial syndrome. American Journal of Medical Genetics Part A, 155:22-32, Jan 2011. URL: https://doi.org/10.1002/ajmg.a.33783, doi:10.1002/ajmg.a.33783. This article has 81 citations.

24. (haldemanenglert2025branchiooculofacialsyndrome pages 7-9): CR Haldeman-Englert and AE Lin. Branchiooculofacial syndrome. Unknown journal, 2025.

## Artifacts

- [Edison artifact artifact-00](Branchiooculofacial_Syndrome-deep-research-falcon_artifacts/artifact-00.md)