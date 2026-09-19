---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-30T23:41:44.560335'
end_time: '2026-07-30T23:55:35.801042'
duration_seconds: 831.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Arboleda-Tham Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Arboleda-Tham_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Arboleda-Tham Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arboleda-Tham Syndrome** covering all of the
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
- **Disease Name:** Arboleda-Tham Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arboleda-Tham Syndrome** covering all of the
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


# Arboleda–Tham Syndrome (KAT6A Syndrome): Comprehensive Disease-Characteristics Report

## Executive summary

Arboleda–Tham syndrome (ARTHS), more commonly called **KAT6A syndrome**, is a rare autosomal-dominant Mendelian chromatinopathy caused by heterozygous pathogenic variants in **KAT6A**, a lysine acetyltransferase and transcriptional regulator. The defining phenotype is congenital or early-childhood neurodevelopmental impairment—particularly severe expressive speech delay—with variable hypotonia, feeding and gastrointestinal dysfunction, characteristic craniofacial features, eye abnormalities, congenital heart disease, microcephaly, growth impairment, sleep disturbance, behavioral differences, and occasional seizures. Most affected individuals have a de novo protein-truncating variant; late truncations in exons 16–17 tend to produce a more severe phenotype than earlier truncations. The best available cohort contained 76 individuals aged 1–32 years, so population prevalence, adult natural history, life expectancy, and formal quality-of-life outcomes remain poorly defined. (kennedy2019kat6asyndromegenotype–phenotype pages 8-9, kennedy2019kat6asyndromegenotype–phenotype pages 1-2)

The strongest recent mechanistic advance is a 2024 mouse study identifying a **KAT6A→RSPO2→Wnt/β-catenin** pathway in hippocampal CA3 pyramidal neurons. Kat6a deficiency reduced CA3 synaptic structure and plasticity and impaired memory; AAV-mediated restoration of RSPO2 substantially rescued the molecular, synaptic, and behavioral deficits. This is important proof of biological reversibility but not yet a human treatment. (liu2024kat6adeficiencyimpairs pages 8-9, liu2024kat6adeficiencyimpairs pages 1-2)

The following compact table summarizes high-yield knowledge-base annotations; ontology mappings are suggestions and should be validated against the release used by the target database.

| domain | evidence-backed finding | suggested ontology identifiers/terms | evidence type/strength |
|---|---|---|---|
| disease entity | Arboleda-Tham syndrome / KAT6A syndrome; Mendelian chromatinopathy / neurodevelopmental disorder caused by pathogenic KAT6A variants; disease-level resource also represented as “autosomal dominant intellectual disability-craniofacial anomalies-cardiac defects syndrome” (bae2021identificationofa pages 1-2, arboleda2015denovononsense pages 1-2, OpenTargets Search: Arboleda-Tham syndrome-KAT6A) | Suggested: MONDO:0014558; OMIM/MIM: 616268; category: Mendelian disorder | Strong: discovery paper + curated disease-target resource + later case series/cohort |
| causal gene | Causal gene is **KAT6A** (aka MOZ, MYST3), encoding lysine acetyltransferase 6A; gene MIM 601408 (bae2021identificationofa pages 1-2, munueracabeza2022pantothenateandlcarnitine pages 1-2, arboleda2015denovononsense pages 1-2) | Suggested: HGNC gene **KAT6A**; OMIM/MIM: 601408 | Strong: multiple human genetic studies |
| inheritance | Predominantly **autosomal dominant**, usually **de novo** heterozygous variants; one maternally inherited missense/VUS-like situation reported in cohort work, supporting variable expressivity for some missense alleles (bae2021identificationofa pages 1-2, lin2020diagnosisofarboledatham pages 3-4, kennedy2019kat6asyndromegenotype–phenotype pages 2-3, arboleda2015denovononsense pages 1-2) | Suggested: HP:0000006 Autosomal dominant inheritance; HP:0025352 De novo constitutional mutation | Strong for AD/de novo; moderate for broader penetrance/expressivity nuances |
| core neurodevelopment | Global developmental delay / intellectual disability is essentially universal in compiled cohorts (**100%**); speech delay is especially prominent (**99%**) and often the most severe developmental domain (urreizti2020fivenewcases pages 7-8, kennedy2019kat6asyndromegenotype–phenotype pages 8-9, kennedy2019kat6asyndromegenotype–phenotype pages 6-7) | Suggested: HP:0001263 Global developmental delay; HP:0001249 Intellectual disability; HP:0002463 Global developmental delay/variable severity; HP:0000750 Delayed speech and language development | Strong: largest cohort + case series |
| feeding / GI phenotype | Feeding difficulties in infancy are common (**79%**), often with reflux, constipation, and oromotor dysfunction; bowel malrotation/obstruction risk highlighted in management recommendations (urreizti2020fivenewcases pages 7-8, bae2021identificationofa pages 5-6, kennedy2019kat6asyndromegenotype–phenotype pages 6-7) | Suggested: HP:0011968 Feeding difficulties; HP:0002020 Gastroesophageal reflux; HP:0002019 Constipation; MAXO suggested: feeding support / laxative therapy / GI surveillance | Strong for feeding/constipation; moderate for obstruction risk |
| hypotonia | Neonatal hypotonia reported in **74%** and contributes to early motor delay and feeding issues (urreizti2020fivenewcases pages 7-8, lin2020diagnosisofarboledatham pages 3-4) | Suggested: HP:0001290 Generalized hypotonia; HP:0008947 Infantile muscular hypotonia | Strong: cohort-supported |
| craniofacial / ear phenotype | Ear anomalies are frequent (**83%**); characteristic dysmorphism includes bulbous/prominent nose, thin upper lip, low-set ears, epicanthal folds, frontal bossing, long face/midface retrusion in some patients (urreizti2020fivenewcases pages 7-8, bae2021identificationofa pages 5-6, urreizti2020fivenewcases pages 6-7) | Suggested: HP:0000357 Abnormality of the external ear; HP:0000369 Low-set ears; HP:0000426 Prominent nasal bridge; HP:0000219 Thin upper lip vermilion | Moderate-strong: cohort + repeated case reports |
| ophthalmic phenotype | Eye anomalies occur in **72%**; strabismus/visual issues affect over half of the cohort and may risk amblyopia if untreated (urreizti2020fivenewcases pages 7-8, bae2021identificationofa pages 5-6, kennedy2019kat6asyndromegenotype–phenotype pages 6-7) | Suggested: HP:0000478 Abnormality of the eye; HP:0000486 Strabismus; HP:0000505 Visual impairment; MAXO suggested: ophthalmology surveillance | Strong for broad eye involvement; moderate for specific subfeatures |
| microcephaly | Microcephaly reported in **36%** overall; was a prominent feature in the original discovery series (urreizti2020fivenewcases pages 7-8, arboleda2015denovononsense pages 1-2) | Suggested: HP:0000252 Microcephaly | Strong |
| cardiac phenotype | Congenital heart disease occurs in about **50%**, commonly septal defects/PDA/PFO; about half of affected cardiac cases required surgical intervention in the large cohort (bae2021identificationofa pages 5-6, kennedy2019kat6asyndromegenotype–phenotype pages 6-7, lin2020diagnosisofarboledatham pages 3-4) | Suggested: HP:0001627 Abnormality of the cardiovascular system; HP:0001631 Atrial septal defect; HP:0001643 Patent ductus arteriosus; MAXO suggested: echocardiography / cardiology evaluation / cardiac surgery | Strong for frequency and need for baseline cardiac workup |
| seizures / sleep | Seizures reported in **13%** and sleep disturbance in **42%** in compiled cohort data (urreizti2020fivenewcases pages 7-8) | Suggested: HP:0001250 Seizure; HP:0002360 Sleep disturbance | Moderate: cohort-supported but less deeply characterized |
| genotype spectrum | Most variants are truncating; in 52 novel cases, **88% (39/44)** were predicted truncating. Recurrent hotspot truncations occur at aa **1019, 1024, 1129**; recurrent nonsense variants include p.Arg1024* and p.Arg1129* (kennedy2019kat6asyndromegenotype–phenotype pages 1-2, kennedy2019kat6asyndromegenotype–phenotype pages 2-3, arboleda2015denovononsense pages 1-2) | Suggested: SO terms—nonsense_variant, frameshift_variant, splice_donor/acceptor_variant, missense_variant | Strong |
| genotype-phenotype correlation | **Late-truncating variants in exons 16–17** associate with more severe ID/speech problems and more microcephaly, hypotonia, cardiac and GI complications; early truncating variants likely undergo NMD and may have fewer GI symptoms (bae2021identificationofa pages 1-2, bae2021identificationofa pages 5-6, kennedy2019kat6asyndromegenotype–phenotype pages 8-9, liu2024kat6adeficiencyimpairs pages 1-2) | Suggested: exon 16/17 late-truncating subgroup annotation; mechanism note: escape from NMD vs haploinsufficiency | Moderate-strong: cohort-based correlation, still mechanistically incomplete |
| primary anatomy | Main affected systems are **central nervous system**, **heart**, **gastrointestinal tract**, **eye**, craniofacial structures, and growth pathways (bae2021identificationofa pages 1-2, kennedy2019kat6asyndromegenotype–phenotype pages 6-7, liu2024kat6adeficiencyimpairs pages 1-2, arboleda2015denovononsense pages 1-2) | Suggested UBERON: brain, hippocampus, heart, gastrointestinal tract, eye, craniofacial skeleton | Strong at organ-system level |
| cell types | Experimental evidence points especially to **hippocampal CA3 pyramidal excitatory neurons** for cognitive mechanism; patient-derived **dermal fibroblasts** are established disease cell models (munueracabeza2022pantothenateandlcarnitine pages 1-2, liu2024kat6adeficiencyimpairs pages 8-9, liu2024kat6adeficiencyimpairs pages 1-2, arboleda2015denovononsense pages 6-7) | Suggested CL terms: excitatory neuron, pyramidal neuron, fibroblast | Strong for model systems; moderate for direct human tissue causality |
| subcellular / chromatin localization | KAT6A is a chromatin-associated lysine acetyltransferase recruited to **unmethylated CpG islands** via an N-terminal winged-helix DNA-binding domain; affects histone acetylation including H3K9 and H3K23 contexts (weber2023thehistoneacetyltransferase pages 1-2, arboleda2015denovononsense pages 6-7) | Suggested GO CC/BP: nucleus, chromatin, histone acetyltransferase complex, regulation of transcription by RNA polymerase II; histone marks: H3K9ac, H3K23ac/propionylation context | Strong biochemistry/mechanism |
| core mechanism | Best current mechanistic chain: **KAT6A deficiency → reduced transcription of CA3-enriched RSPO2 → impaired Wnt/β-catenin signaling in hippocampal CA3 → reduced dendritic spine density / synaptic plasticity → hippocampus-dependent memory deficits** (liu2024kat6adeficiencyimpairs pages 8-9, liu2024kat6adeficiencyimpairs pages 1-2) | Suggested GO/BP: histone acetylation; positive regulation of Wnt signaling pathway; synaptic plasticity; learning or memory. Suggested pathway label: KAT6A–RSPO2–Wnt axis | Strong preclinical evidence; not yet fully validated in humans |
| additional molecular abnormalities | Patient fibroblasts show altered histone acetylation (decreased H3K9ac, increased H3K18ac in original work), altered p53-related expression, transcriptomic disruption, and mitochondrial/bioenergetic defects with reduced acetylation/deacetylation, CoA-metabolism and antioxidant proteins (munueracabeza2022pantothenateandlcarnitine pages 15-16, arboleda2015denovononsense pages 6-7) | Suggested GO/BP: regulation of apoptotic process, cellular metabolism, mitochondrial function, oxidative stress response | Moderate: human in vitro evidence from small numbers |
| diagnostics | Diagnosis is primarily by **WES/WGS**, especially trio-based testing for de novo variants; WGS and WES both successfully diagnosed infants/children with syndromic developmental delay and dysmorphism (bae2021identificationofa pages 1-2, lin2020diagnosisofarboledatham pages 3-4, lin2020diagnosisofarboledatham pages 1-3, arboleda2015denovononsense pages 1-2) | Suggested testing annotations: trio WES, trio WGS, Sanger confirmation; phenotype-driven genomic testing | Strong |
| supportive management | Current management is **supportive and surveillance-based**: early developmental assessment/intervention, speech-language therapy and communication aids/sign language, cardiology evaluation with ECG/echocardiogram, GI management for reflux/constipation/feeding issues, ophthalmology review, rehabilitation and serial developmental follow-up (bae2021identificationofa pages 5-6, bae2021identificationofa pages 6-7, kennedy2019kat6asyndromegenotype–phenotype pages 6-7) | Suggested MAXO: developmental therapy, speech therapy, augmentative communication, cardiology assessment, ophthalmologic monitoring, GI symptom management, rehabilitation | Moderate-strong: expert cohort recommendations rather than trials |
| experimental interventions | No established disease-specific therapy retrieved. Preclinical/cellular candidates: **pantothenate + L-carnitine** improved histone acetylation, transcriptomic/protein abnormalities and bioenergetics in three patient fibroblast lines; **RSPO2 restoration / Wnt enhancement** rescued synaptic and behavioral phenotypes in mouse CA3 (munueracabeza2022pantothenateandlcarnitine pages 1-2, munueracabeza2022pantothenateandlcarnitine pages 15-16, liu2024kat6adeficiencyimpairs pages 8-9, liu2024kat6adeficiencyimpairs pages 1-2) | Suggested CHEBI/MAXO notes: pantothenate supplementation, L-carnitine supplementation, AAV-mediated RSPO2 restoration, Wnt-pathway enhancement | Weak-moderate for translation: preclinical only |
| model organisms | **Kat6a homozygous knockout mice are embryonic lethal** with developmental/vascular-cardiac and hematopoietic defects; haploinsufficient and neuron-specific mouse models reproduce growth and cognitive phenotypes; AAV rescue supports reversibility of some neural deficits (munueracabeza2022pantothenateandlcarnitine pages 1-2, liu2024kat6adeficiencyimpairs pages 1-2, arboleda2015denovononsense pages 6-7) | Suggested model annotations: mouse knockout, conditional neuronal knockout, AAV rescue model | Strong for disease-mechanism modeling |
| epidemiology / demographics | Largest cohort included **76 patients**, age **1–32 years**, sex roughly balanced (**49% female, 51% male**). True population prevalence/incidence remain undefined; one report estimated pathogenic KAT6A variants in ~**1% of undiagnosed syndromic developmental delay** referrals, which is not a population prevalence estimate (kennedy2019kat6asyndromegenotype–phenotype pages 1-2, bae2021identificationofa pages 5-6, arboleda2015denovononsense pages 1-2) | Suggested epidemiology note: prevalence unknown; ascertainment from case reports/cohorts, not population registry | Moderate for cohort demographics; weak for prevalence |
| evidence gaps | Major gaps: no robust population prevalence/incidence, no disease-specific survival/life-expectancy data, sparse formal QoL studies, limited penetrance estimates, no validated biomarkers for monitoring, no established episignature data in retrieved full texts, no controlled treatment trials, and little evidence for environmental/protective factors or gene-environment interaction (kennedy2019kat6asyndromegenotype–phenotype pages 1-2, kennedy2019kat6asyndromegenotype–phenotype pages 6-7, kennedy2019kat6asyndromegenotype–phenotype pages 9-10) | Suggested annotation: evidence gap / not established / not retrieved | Strong confidence that these are current knowledge gaps based on gathered evidence |


*Table: This table compiles the highest-yield, evidence-backed annotations for Arboleda-Tham/KAT6A syndrome using only the information gathered in the preceding search. It is useful as a compact knowledge-base scaffold spanning identifiers, phenotype frequencies, mechanism, diagnostics, management, and evidence gaps.*

## 1. Disease information

### Definition and identifiers

* **Preferred names:** Arboleda–Tham syndrome; KAT6A syndrome.
* **Alternative names:** autosomal dominant intellectual disability–craniofacial anomalies–cardiac defects syndrome; autosomal dominant mental retardation 32; KAT6A-related neurodevelopmental disorder.
* **MONDO:** **MONDO:0014558**, represented as autosomal dominant intellectual disability–craniofacial anomalies–cardiac defects syndrome.
* **OMIM phenotype:** **616268**.
* **Causal gene:** **KAT6A**, OMIM gene **601408**, also known as **MOZ** and **MYST3**; Ensembl target ENSG00000083168.
* **Chromosomal location:** 8p11.21/8p11 region.
* **ICD-10/ICD-11 and MeSH:** no syndrome-specific code or descriptor was established in the retrieved evidence. Coding generally must use broader congenital-malformation, intellectual-disability, or genetic-syndrome categories. (OpenTargets Search: Arboleda-Tham syndrome-KAT6A, bae2021identificationofa pages 1-2, lin2020diagnosisofarboledatham pages 3-4)

The syndrome was delineated in 2015 after clinical trio-exome sequencing identified de novo heterozygous nonsense variants in four unrelated families. The discovery abstract states: **“Common features among all four probands include primary microcephaly, global developmental delay including profound speech delay, and craniofacial dysmorphism.”** [Arboleda et al., published March 5, 2015; DOI: https://doi.org/10.1016/j.ajhg.2015.01.017]. (arboleda2015denovononsense pages 1-2)

### Evidence provenance

The evidence is principally **aggregated disease-level information derived from individually ascertained patients**, including clinician reports, family surveys, case reports, exome/genome cohorts, and literature review. It is not based on a population registry or systematic extraction from longitudinal electronic health records. The largest study combined 52 new cases with previously published individuals for a total of 76. (kennedy2019kat6asyndromegenotype–phenotype pages 1-2)

## 2. Etiology

### Causal and genetic risk factors

ARTHS is caused by a heterozygous constitutional pathogenic variant in **KAT6A**. Most reported variants are nonsense or frameshift alleles, although splice-site and selected missense variants have also been described. In the 2019 cohort, 39/44 novel variants (88%) were predicted truncating. Recurrent nonsense hotspots at amino-acid positions **1019, 1024, and 1129** accounted for 13/68 (19.1%) pathogenic variants among unrelated individuals. (kennedy2019kat6asyndromegenotype–phenotype pages 8-9, kennedy2019kat6asyndromegenotype–phenotype pages 2-3)

Examples include:

* **NM_006766.5:c.3385C>T, p.Arg1129Ter**, recurrent in the discovery series;
* **c.3070C>T, p.Arg1024Ter**;
* **NM_006766.5:c.3411del, p.Glu1139SerfsTer41**, a de novo exon-17 variant associated with severe delay;
* **c.1312C>T, p.Arg438Ter**, an early truncating variant expected to undergo nonsense-mediated decay;
* **c.3427_3428insTA, p.Ser1143LeufsTer5**;
* **c.1075G>A, p.Gly359Ser**, which experimentally altered splicing rather than acting solely as a missense allele. (bae2021identificationofa pages 1-2, lin2020diagnosisofarboledatham pages 3-4, urreizti2020fivenewcases pages 7-8, arboleda2015denovononsense pages 1-2)

Pathogenic constitutional variants are expected to be absent or extremely rare from population databases because of strong functional constraint and severe early-onset effects. Exact gnomAD/TOPMed frequencies were not available in the retrieved texts and should be obtained variant-by-variant rather than inferred.

### Environmental, infectious, and lifestyle risk factors

No toxin, infection, radiation, diet, smoking, alcohol, occupation, or other lifestyle exposure is known to cause ARTHS. It is not infectious or environmentally acquired. Phenotypic variability may reflect genetic background, epigenetic state, development, clinical ascertainment, and possibly environment, but no reproducible gene–environment interaction has been demonstrated. The 2019 cohort explicitly considered background genetic variation and environmental factors plausible contributors to expressivity, not established causal exposures. (kennedy2019kat6asyndromegenotype–phenotype pages 9-10, arboleda2015denovononsense pages 6-7)

### Protective factors and modifiers

No validated protective allele, modifier gene, diet, or exposure is known. **KAT6B** may provide partial biochemical redundancy in some tissues, but this is mechanistic inference rather than a clinically established modifier. Pantothenate and L-carnitine improved cellular abnormalities in vitro; they have not been shown to prevent disease or improve outcomes in patients. (munueracabeza2022pantothenateandlcarnitine pages 1-2, liu2024kat6adeficiencyimpairs pages 8-9)

## 3. Phenotypes

The most reusable frequencies come from the 76-person cohort and the subsequent synthesis of approximately 80 reported cases. Denominators vary because not every feature was assessed in every patient; percentages should therefore be stored with study provenance rather than treated as population penetrance. (urreizti2020fivenewcases pages 7-8, kennedy2019kat6asyndromegenotype–phenotype pages 1-2)

| Phenotype | Frequency/current characterization | Onset/course and functional impact | Suggested HPO term |
|---|---|---|---|
| Global developmental delay/intellectual disability | Approximately 100%; severity variable | Infancy/early childhood; chronic and lifelong; affects learning, independence, and adaptive function | HP:0001263; HP:0001249 |
| Speech/language delay | Approximately 99%; expressive speech disproportionately severe | May become clearer after infancy; often persistent and a major participation barrier | HP:0000750; consider childhood apraxia/motor-speech annotation when formally diagnosed |
| Neonatal/infantile hypotonia | Approximately 74% | Early onset; may worsen feeding and motor milestone acquisition | HP:0001290 / HP:0008947 |
| Feeding difficulty | Approximately 79% | Usually infancy; oromotor dysfunction, reflux, and poor growth may require tube feeding | HP:0011968 |
| Gastroesophageal reflux/constipation | Common, exact denominator variable | Usually chronic or recurrent; constipation may require long-term treatment | HP:0002020; HP:0002019 |
| Congenital heart disease | About 50%; septal defects and PDA/PFO common | Congenital and generally structurally stable after treatment; about half of cardiac cases required surgery | HP:0001627; HP:0001631; HP:0001643 |
| Eye abnormalities | About 72%; strabismus/visual problems in over half | Childhood; untreated strabismus can lead to permanent amblyopia | HP:0000478; HP:0000486; HP:0000505 |
| External-ear anomalies | About 83% | Congenital, usually nonprogressive | HP:0000357; HP:0000369 |
| Microcephaly | About 36% overall | Congenital or postnatal; severity variable | HP:0000252 |
| Characteristic face | Broad/bulbous nasal tip or prominent bridge, thin/tented upper lip, low-set ears, epicanthi, short philtrum, frontal bossing or midface retrusion | Congenital; facial gestalt may evolve with age | HP:0000426; HP:0000219; HP:0000286 |
| Sleep disturbance | About 42% | Childhood; potentially chronic/fluctuating and burdensome to families | HP:0002360 |
| Seizures | About 13% | Variable onset and type; not a universal defining feature | HP:0001250 |
| Behavioral/autistic features | Autism reported at approximately 25% in one synthesis; stereotypies and other behavioral differences vary | Childhood; effects on education and social function vary | HP:0000729; HP:0000717 |
| Skeletal abnormalities | Scoliosis, kyphosis, torticollis, syndactyly, pes planus, genu valgum; craniosynostosis around 10% in one synthesis | Congenital or developing with growth; may affect mobility or require surgery | Feature-specific HPO terms |
| Genitourinary findings | Cryptorchidism in some males; inguinal hernia reported | Congenital | HP:0000028; HP:0000023 |
| Recurrent infections | Reported in case series, frequency uncertain | Episodic; immune mechanism not established | HP:0002719 |

These estimates are supported by the five-case/literature synthesis reporting developmental delay/ID 100%, speech delay 99%, feeding difficulty 79%, neonatal hypotonia 74%, ear anomalies 83%, eye anomalies 72%, microcephaly 36%, seizures 13%, and sleep disturbance 42%. (urreizti2020fivenewcases pages 7-8) Congenital heart disease occurs in approximately half, and feeding difficulties were estimated at 78.7% in another review. (bae2021identificationofa pages 5-6, kennedy2019kat6asyndromegenotype–phenotype pages 6-7)

### Quality of life

No validated ARTHS-specific EQ-5D, SF-36, PROMIS, or caregiver-burden dataset was identified. The major inferred burdens are impaired communication, intellectual and adaptive limitations, feeding support, constipation, visual disability, sleep disruption, mobility problems, and repeated specialty care. Communication aids and early speech therapy are therefore clinically important even in the absence of controlled quality-of-life trials. (bae2021identificationofa pages 6-7, kennedy2019kat6asyndromegenotype–phenotype pages 6-7)

## 4. Genetic and molecular information

### Gene and protein

**KAT6A** encodes a roughly 250-kDa MYST-family lysine acetyltransferase. Important regions include an N-terminal NEMM/winged-helix region, a double PHD finger, the catalytic histone-acetyltransferase domain, and long acidic and serine/methionine-rich C-terminal regions. KAT6A operates in multiprotein chromatin complexes with BRPF-family scaffolds, ING4/ING5, and MEAF6/EAF6-associated components. It modifies histone and non-histone substrates, including p53. (arboleda2015denovononsense pages 6-7, weber2023thehistoneacetyltransferase pages 1-2)

### Variant classes and consequences

* **Early truncating variants, exons 1–15:** commonly expected to trigger nonsense-mediated mRNA decay and produce haploinsufficiency.
* **Late truncating variants, exons 16–17:** may escape nonsense-mediated decay, leaving truncated proteins with altered C-terminal regulatory functions. The cohort association with greater severity raises dominant-negative or altered-function possibilities, but these mechanisms are not fully proven in patients.
* **Canonical splice variants:** pathogenic when demonstrated to disrupt splicing.
* **Missense variants:** require cautious evaluation. De novo status, absence from population databases, domain/residue conservation, phenotype concordance, functional evidence, and an ARTHS-compatible methylation signature can strengthen classification. A maternally inherited p.Ser371Tyr allele was classified as a VUS in the 2019 study. (kennedy2019kat6asyndromegenotype–phenotype pages 8-9, kennedy2019kat6asyndromegenotype–phenotype pages 2-3, liu2024kat6adeficiencyimpairs pages 1-2)

Variants causing the developmental syndrome are **germline/constitutional**, not somatic. Somatic KAT6A rearrangements or fusions are relevant to leukemia but are a separate disease mechanism and should not be conflated with ARTHS.

### Genotype–phenotype relationship

Late truncations in exons 16–17 correlate with more severe intellectual disability, speech impairment, microcephaly, neonatal hypotonia, cardiac anomalies, and gastrointestinal complications. Early truncations may have fewer gastrointestinal manifestations. This is a group-level association, not a deterministic prognostic rule. (bae2021identificationofa pages 1-2, bae2021identificationofa pages 5-6, kennedy2019kat6asyndromegenotype–phenotype pages 8-9)

### Epigenetics and chromosomal abnormalities

The syndrome is itself an epigenetic-regulator disorder. Patient fibroblasts showed reduced H3K9 acetylation and increased H3K18 acetylation in the original study, with altered p53-pathway expression. A later cellular study also found reduced histone-H3 acetylation, broad transcriptomic disturbance, and mitochondrial/bioenergetic abnormalities. (munueracabeza2022pantothenateandlcarnitine pages 15-16, arboleda2015denovononsense pages 6-7)

A 2023 publication reported sensitive and specific blood DNA-methylation episignatures for KAT6A/KAT6B variants, suggesting a future adjunct for VUS interpretation; however, the full study was not retrievable in this search, so assay performance should be verified directly before database entry or clinical use [Vos et al., *Epigenomics*, May 2023; DOI: https://doi.org/10.2217/epi-2023-0079].

No recurrent pathogenic aneuploidy, translocation, inversion, or syndrome-defining copy-number alteration is established as the usual cause. Deletions disrupting KAT6A could theoretically cause haploinsufficiency, but larger 8p alterations may produce blended phenotypes.

## 5. Environmental information

No environmental toxin, radiation exposure, pollutant, occupational factor, lifestyle behavior, or infectious agent is known to initiate ARTHS. Standard healthy diet, activity, vaccination, and avoidance of tobacco exposure remain appropriate general health measures but are not disease-specific prevention. Nutrient-dependent acetyl-CoA and mitochondrial biology may influence cellular acetylation, yet no clinical evidence establishes diet as a modifier of penetrance or severity. (munueracabeza2022pantothenateandlcarnitine pages 1-2, munueracabeza2022pantothenateandlcarnitine pages 15-16)

## 6. Mechanism and pathophysiology

### Upstream molecular lesion

A pathogenic KAT6A allele reduces the amount of functional enzyme or yields a C-terminally truncated dysfunctional protein. KAT6A normally binds chromatin and catalyzes lysine acetylation, helping establish transcriptionally competent chromatin. A 2023 biochemical study showed that an N-terminal winged-helix domain directly recognizes unmethylated CpG motifs and recruits KAT6A to CpG islands genome-wide. Mutating essential DNA-binding residues abolished CpG-island enrichment; a winged-helix mutant also exerted a dominant-negative effect on H3K9 acetylation. (weber2023thehistoneacetyltransferase pages 1-2)

### Downstream chromatin and cellular effects

The original patient-fibroblast study found altered H3K9/H3K18 acetylation and differential expression of 30 p53-pathway genes, enriched for apoptosis, transcriptional regulation, and metabolism. The authors concluded that KAT6A variants alter global acetylation and p53-mediated pathways. (arboleda2015denovononsense pages 6-7)

Fibroblasts from three patients subsequently showed reduced H3 acetylation and reduced proteins involved in acetylation/deacetylation, CoA metabolism, mitochondrial function, and antioxidant defense, including SIRT1, SIRT3, NAMPT, PANK2, mitochondrial respiratory-chain proteins, SOD1/SOD2, and GPX4. These findings support secondary mitochondrial and redox dysfunction, but fibroblasts are a surrogate model and do not establish that every abnormality occurs in human neurons or heart tissue. (munueracabeza2022pantothenateandlcarnitine pages 1-2, munueracabeza2022pantothenateandlcarnitine pages 15-16)

### KAT6A–RSPO2–Wnt causal chain in the brain

The best-defined neural mechanism is:

**KAT6A haploinsufficiency → reduced H3K23 acetylation at the Rspo2 promoter and reduced Rspo2 transcription → diminished RSPO2-dependent canonical Wnt/β-catenin signaling → reduced dendritic-spine density, excitatory transmission, and long-term potentiation in CA3 pyramidal neurons → impaired hippocampus-dependent learning and memory.**

Single-nucleus RNA sequencing and chromatin analysis identified **Rspo2** as the robust CA3-enriched transcriptional target. Excitatory-neuron Rspo2 deletion phenocopied Kat6a loss, whereas AAV-RSPO2 delivery restored β-catenin, synaptic physiology, dendritic spines, and much of the learning/memory phenotype. CA1 synaptic function was comparatively spared. (liu2024kat6adeficiencyimpairs pages 8-9, liu2024kat6adeficiencyimpairs pages 1-2)

Direct abstract quote: **“Deletion of Rspo2 in excitatory neurons impairs memory formation, and restoring RSPO2 expression in CA3 neurons rescues the deficits in Wnt signaling and learning-associated behaviors in Kat6a mutant mice.”** [Liu et al., *Science Advances*, May 17, 2024; DOI: https://doi.org/10.1126/sciadv.adm9326]. (liu2024kat6adeficiencyimpairs pages 1-2)

### Suggested ontologies

* **GO biological process:** histone acetylation; chromatin organization; regulation of transcription by RNA polymerase II; canonical Wnt signaling; synaptic plasticity; learning or memory; stem-cell maintenance; embryonic organ development.
* **GO cellular component:** nucleus; chromatin; histone acetyltransferase complex; neuronal dendrite; excitatory synapse.
* **Cell Ontology:** fibroblast; excitatory neuron; pyramidal neuron; hippocampal CA3 pyramidal neuron where an exact release-specific term exists; hematopoietic stem cell; neural-crest-derived craniofacial cell as a proposed developmental annotation.

### Omics and advanced technologies

Human fibroblast RNA-seq demonstrated transcriptomic disturbance; the 2024 mouse study integrated single-nucleus RNA-seq with chromatin analysis. No validated human disease-specific proteomic, metabolomic, lipidomic, spatial-transcriptomic, organoid, or large iPSC atlas was identified. No published therapeutic CRISPR screen was retrieved. (munueracabeza2022pantothenateandlcarnitine pages 1-2, liu2024kat6adeficiencyimpairs pages 1-2, arboleda2015denovononsense pages 6-7)

## 7. Anatomical structures affected

* **Primary nervous-system involvement:** developing brain and neural circuits governing cognition, speech, language, motor planning, tone, sleep, and behavior. The strongest mechanistic localization is hippocampal CA3, not evidence that disease is restricted to CA3.
* **Cardiovascular:** atrial/ventricular septa, ductus arteriosus, and other congenital cardiac structures.
* **Gastrointestinal/oromotor:** oral and pharyngeal feeding apparatus, esophagus, bowel motility, and occasionally intestinal rotation/obstruction.
* **Craniofacial:** skull, palate, midface, nose, lips, jaw, and external ears.
* **Eye:** extraocular alignment and visual system; ptosis and structural ocular abnormalities occur variably.
* **Musculoskeletal:** spine, feet, joints, and cranial sutures in a subset.
* **Genitourinary:** testes/inguinal region in some males.
* **Hematopoietic/immune system:** major defects occur in complete mouse knockouts; recurrent infection and an isolated 2023 marrow-failure report warrant awareness, but routine human hematopoietic failure is not established. (lin2020diagnosisofarboledatham pages 3-4, urreizti2020fivenewcases pages 7-8, kennedy2019kat6asyndromegenotype–phenotype pages 6-7, arboleda2015denovononsense pages 6-7)

Suggested UBERON annotations include brain, hippocampus, CA3 field of hippocampus, heart, gastrointestinal tract, eye, palate, craniofacial skeleton, spinal column, and testis. Relevant subcellular annotations are nucleus, chromatin, nucleosome, and histone-acetyltransferase complex. No consistent lateralization is known.

## 8. Temporal development

ARTHS begins prenatally through disturbed embryonic gene regulation, although the neurodevelopmental phenotype often becomes clinically apparent in infancy. Congenital manifestations can include craniofacial differences, heart defects, palate abnormalities, hypotonia, feeding difficulty, growth restriction, and microcephaly. Developmental and especially expressive-language delays become clearer over the first years; an infant diagnosed at two months developed evident expressive-language delay by eight months. (bae2021identificationofa pages 1-2, bae2021identificationofa pages 6-7)

The disorder is chronic and lifelong. It has no accepted staging system, relapsing-remitting pattern, or spontaneous remission phenotype. Congenital structural abnormalities are generally stable or surgically corrected, while development continues slowly with variable gains. Constipation, sleep problems, orthopedic abnormalities, and communication disability may remain chronic. One individual had progressive cerebellar atrophy, but progressive neurodegeneration is not established as the typical course. (urreizti2020fivenewcases pages 7-8)

Early childhood is the principal intervention window for feeding safety, communication, motor development, vision, and cardiac assessment. Early genomic diagnosis therefore has practical value even without disease-modifying therapy. (bae2021identificationofa pages 6-7, kennedy2019kat6asyndromegenotype–phenotype pages 6-7)

## 9. Inheritance and population

Inheritance is autosomal dominant and usually de novo. For an affected individual with a constitutional pathogenic variant, the theoretical transmission risk is 50% per pregnancy, although reproductive fitness and individual circumstances vary. Parents testing negative in blood usually have a low recurrence risk, but parental germline or low-level somatic mosaicism cannot be excluded; no syndrome-specific mosaic recurrence rate is available.

Penetrance appears high for truncating pathogenic variants ascertained clinically, while expressivity is markedly variable. Missense alleles require greater caution because incomplete penetrance, alternate molecular effects, or misclassification may occur. Genetic anticipation is not expected because ARTHS is not a repeat-expansion disorder. Consanguinity is not etiologically relevant to a predominantly de novo dominant condition. No founder variant, carrier frequency, or population-specific enrichment is established. (kennedy2019kat6asyndromegenotype–phenotype pages 8-9, kennedy2019kat6asyndromegenotype–phenotype pages 2-3, kennedy2019kat6asyndromegenotype–phenotype pages 9-10)

The largest cohort included 76 individuals aged 1–32 years and was sex-balanced: 49% female and 51% male. Cases have been reported across multiple ancestries and regions; no geographic or ethnic predilection is established. Approximately 400–500 diagnosed patients had been cited by 2023–2024 mechanistic publications, but this is a reported-case count, not prevalence. A discovery-center estimate of 3/298, approximately 1%, among developmental-delay exomes reflects highly selected referral ascertainment and must not be interpreted as population prevalence. (kennedy2019kat6asyndromegenotype–phenotype pages 1-2, liu2024kat6adeficiencyimpairs pages 1-2, arboleda2015denovononsense pages 6-7, weber2023thehistoneacetyltransferase pages 1-2)

Population prevalence, birth incidence, and carrier frequency remain unknown.

## 10. Diagnostics

### Clinical recognition

Clinical suspicion should arise with global developmental delay—especially profound expressive speech delay—plus hypotonia, feeding/GI problems, a broad or bulbous nose with thin upper lip, low-set ears, eye findings, microcephaly, or congenital heart disease. No purely clinical diagnostic criteria are sufficiently specific; molecular confirmation is required.

### Recommended genetic approach

1. **Trio WES or WGS** is the preferred broad approach for an undiagnosed syndromic neurodevelopmental disorder. WES identified the original de novo variants; WGS diagnosed a severe case within four weeks and may detect structural, noncoding, or coverage-limited variants missed by exome sequencing. (lin2020diagnosisofarboledatham pages 1-3, arboleda2015denovononsense pages 1-2)
2. **Neurodevelopmental/intellectual-disability or congenital-anomaly panels** should include KAT6A and detect single-nucleotide variants and indels, with validated exon-level copy-number analysis.
3. **Single-gene sequencing** is suitable when the phenotype is strongly suggestive or for familial testing.
4. Confirm the variant and parental status by an orthogonal method such as Sanger sequencing where appropriate.
5. Interpret variants using ACMG/AMP criteria, population frequency, predicted loss of function, exon position/NMD, de novo status, phenotype, splicing assays, and functional or methylation evidence.
6. **CMA** remains useful when a copy-number disorder is suspected or sequencing is nondiagnostic. Routine karyotype/FISH, mitochondrial DNA testing, and repeat-expansion testing are not first-line ARTHS tests.

RNA sequencing can resolve suspected splice variants, while blood DNA-methylation profiling may support classification of uncertain KAT6A/KAT6B variants. Neither replaces primary DNA testing.

### Baseline and surveillance evaluations

Recommended evaluations include developmental and speech-language assessment; feeding/swallowing and nutrition review; growth and head circumference; ECG and echocardiogram; ophthalmology; hearing; neurologic assessment with EEG when seizures are suspected; GI review for reflux, constipation, malrotation, or obstruction; musculoskeletal examination; and renal/genitourinary assessment guided by findings. Brain MRI is clinically indicated for seizures, abnormal neurologic progression, unusual head growth, or focal findings, not as a diagnostic biomarker. (bae2021identificationofa pages 5-6, kennedy2019kat6asyndromegenotype–phenotype pages 6-7)

### Differential diagnosis

Important differentials include KAT6B-related Say–Barber–Biesecker–Young–Simpson/genitopatellar syndromes, BRPF1-related intellectual developmental disorder with dysmorphic facies and ptosis, Wiedemann–Steiner syndrome, Kabuki syndrome, Coffin–Siris spectrum, Cornelia de Lange spectrum, Rubinstein–Taybi syndrome, CDK13-related disorder, and other monogenic chromatinopathies. Distinction generally requires genomic testing because ID, speech delay, hypotonia, feeding problems, heart defects, and dysmorphism overlap.

Population newborn screening is unavailable. Cascade testing is appropriate after a molecular diagnosis; prenatal diagnosis and preimplantation genetic testing are technically possible when the familial variant is known.

## 11. Outcome and prognosis

No reliable 5- or 10-year survival rate, disease-specific mortality rate, or life-expectancy estimate exists. The 2019 cohort included adults up to age 32, showing survival into adulthood, but adult ascertainment is limited. (kennedy2019kat6asyndromegenotype–phenotype pages 1-2)

Morbidity is dominated by communication and intellectual disability, delayed motor and adaptive skills, feeding/GI problems, visual impairment, sleep disturbance, and congenital anomalies. Developmental skills may improve with therapy, but full recovery from the underlying neurodevelopmental disorder is not expected. Prognostic factors supported at group level include variant position—late truncations generally confer greater severity—and the burden of congenital heart, GI, feeding, neurologic, or orthopedic complications. Individual prediction remains imprecise because expressivity varies even among people with the same variant. (kennedy2019kat6asyndromegenotype–phenotype pages 8-9, arboleda2015denovononsense pages 6-7)

There is no validated circulating, imaging, electrophysiologic, or molecular prognostic biomarker. DNA methylation signatures are diagnostic/classification candidates rather than proven outcome biomarkers.

## 12. Treatment

### Current clinical management

There is no approved disease-modifying pharmacotherapy, gene therapy, RNA therapy, or cell therapy. Care is multidisciplinary and phenotype-directed:

* early intervention, special education, neuropsychology, and behavioral support;
* intensive speech-language therapy, with sign language, picture systems, or speech-generating devices introduced early rather than waiting for speech to emerge;
* physical and occupational therapy for hypotonia, coordination, mobility, and adaptive skills;
* swallow/feeding therapy, nutritional support, reflux treatment, and enteral feeding when required;
* constipation therapy and urgent evaluation of bilious vomiting or obstructive symptoms;
* standard cardiology and cardiac-surgical care;
* ophthalmologic treatment of strabismus, refractive error, ptosis, and amblyopia risk;
* standard antiseizure therapy when epilepsy is confirmed;
* sleep assessment and treatment of specific contributors;
* orthopedic, craniofacial, dental, hearing, and genitourinary care as indicated. (bae2021identificationofa pages 5-6, bae2021identificationofa pages 6-7, kennedy2019kat6asyndromegenotype–phenotype pages 6-7)

Suggested MAXO annotations include genetic counseling, exome/genome sequencing, echocardiography, electrocardiography, ophthalmologic examination, developmental assessment, speech therapy, augmentative and alternative communication, physical therapy, occupational therapy, feeding therapy, enteral nutrition, laxative therapy, antiseizure pharmacotherapy, and corrective cardiac or craniofacial surgery.

### Experimental strategies

Patient fibroblasts treated with **pantothenate and L-carnitine** showed increased histone acetylation, partial normalization of protein and transcriptomic patterns, and significantly improved bioenergetics. Direct abstract quote: **“Pantothenate and L-carnitine treatment increased histone acetylation and partially corrected protein and transcriptomic expression patterns in mutant KAT6A cells.”** [Munuera-Cabeza et al., published December 2022; DOI: https://doi.org/10.3390/genes13122300]. This was an in-vitro study of three patient cell lines, not a clinical trial; efficacy, dosing, safety, and developmental benefit in patients are unknown. (munueracabeza2022pantothenateandlcarnitine pages 1-2, munueracabeza2022pantothenateandlcarnitine pages 15-16)

Enhancing RSPO2/Wnt signaling rescued cognitive and synaptic deficits in mice, identifying a target rather than a ready treatment. Systemic Wnt activation has substantial developmental and oncogenic risks, and human translation will require tissue-specific delivery and extensive safety work. (liu2024kat6adeficiencyimpairs pages 8-9)

No disease-specific interventional ClinicalTrials.gov study was retrieved. There are therefore no evidence-based response rates, adverse-event profiles, combination regimens, or pharmacogenomic prescribing recommendations for ARTHS.

## 13. Prevention

Primary prevention by lifestyle modification or vaccination is not possible for a usually de novo genetic disorder. The principal preventive actions are reproductive and complication-focused:

* preconception and postdiagnostic genetic counseling;
* parental testing, with discussion of residual germline-mosaicism risk;
* prenatal diagnosis or PGT-M when a pathogenic familial variant is known;
* early molecular diagnosis and developmental intervention;
* baseline cardiac and eye assessment to prevent avoidable cardiac morbidity and amblyopia;
* feeding/swallowing assessment to reduce malnutrition and aspiration risk;
* proactive constipation treatment and recognition of bowel obstruction;
* seizure, sleep, orthopedic, and hearing surveillance according to symptoms.

No population carrier-screening or newborn-screening program is indicated by current evidence. Public-health sanitation, vector control, environmental remediation, vaccines, and antimicrobial prophylaxis are not disease-specific measures.

## 14. Other species and natural disease

No naturally occurring veterinary syndrome clearly orthologous to human ARTHS was identified, and there is no zoonotic or cross-species transmission. Relevant orthologues include mouse **Kat6a** and zebrafish **kat6a**; exact NCBI Gene and Taxon identifiers should be populated from current NCBI records. Standard taxonomy identifiers are *Homo sapiens* Taxon 9606, *Mus musculus* Taxon 10090, and *Danio rerio* Taxon 7955.

KAT6A’s chromatin, embryonic-development, hematopoietic, cardiac, craniofacial, and neural functions are evolutionarily conserved. Animal phenotypes are experimental genetic models rather than evidence of a recognized spontaneous livestock, companion-animal, or wildlife disease. (arboleda2015denovononsense pages 6-7, weber2023thehistoneacetyltransferase pages 1-2)

## 15. Model organisms and experimental systems

### Mouse models

* **Constitutive homozygous Kat6a loss:** embryonic or perinatal lethal, with vascular/cardiac, gastrointestinal, skeletal, thymic/splenic, neural-stem-cell, and hematopoietic defects. This model demonstrates essential developmental functions but is more severe than the usual human heterozygous syndrome. (arboleda2015denovononsense pages 6-7)
* **Kat6a+/− early-truncation model:** approximately 50% hippocampal Kat6a expression, reduced body weight, and learning/memory abnormalities, modeling human haploinsufficiency.
* **Excitatory-neuron conditional knockout:** reproduces CA3-specific synaptic and memory deficits without requiring whole-organism loss.
* **Rspo2 conditional knockout and AAV-RSPO2 rescue:** establish pathway causality and demonstrate that selected postnatal neural deficits can be reversed in mice. (liu2024kat6adeficiencyimpairs pages 8-9, liu2024kat6adeficiencyimpairs pages 1-2)

Limitations include species differences, simplified alleles, incomplete modeling of late-truncating human variants, and inability of behavioral assays to reproduce human speech, language, congenital anomalies, and psychosocial outcomes.

### Cellular and biochemical models

Patient dermal fibroblasts reproduce altered histone acetylation, p53-related transcription, mitochondrial dysfunction, and treatment-responsive molecular phenotypes. Their accessibility is an advantage, but they do not fully model developing neurons, cardiomyocytes, cranial neural crest, or gastrointestinal tissues. Recombinant-domain, DNA-binding, chromatin-immunoprecipitation, and genome-wide occupancy assays established direct KAT6A recruitment to unmethylated CpG islands. (munueracabeza2022pantothenateandlcarnitine pages 1-2, arboleda2015denovononsense pages 6-7, weber2023thehistoneacetyltransferase pages 1-2)

No mature ARTHS-specific iPSC-neuron, cerebral-organoid, or patient-derived cardiac-organoid platform was identified in the retrieved literature; these are logical priorities for variant-specific therapeutic testing.

## Recent developments, 2023–2024

1. **Chromatin targeting:** KAT6A was shown to bind unmethylated CpG islands directly through an N-terminal winged-helix domain, clarifying how the enzyme reaches genomic targets [published online December 20, 2022; journal issue 2023; DOI: https://doi.org/10.1093/nar/gkac1188]. (weber2023thehistoneacetyltransferase pages 1-2)
2. **DNA-methylation diagnostics:** a 2023 study reported KAT6A/KAT6B episignatures as sensitive and specific biomarkers for variant detection/classification; direct review is needed for exact validation metrics [DOI: https://doi.org/10.2217/epi-2023-0079].
3. **Brain mechanism and rescue:** the 2024 Science Advances study localized a major cognitive mechanism to CA3 KAT6A–RSPO2–Wnt signaling and achieved AAV-RSPO2 rescue [DOI: https://doi.org/10.1126/sciadv.adm9326]. (liu2024kat6adeficiencyimpairs pages 8-9, liu2024kat6adeficiencyimpairs pages 1-2)
4. **Phenotypic expansion:** 2024 reports added prenatal/fetal observations, including fetal hepatic calcification, and additional Asian cases, but these remain isolated observations rather than established screening markers [DOIs: https://doi.org/10.1016/j.ejmg.2023.104906 and https://doi.org/10.1002/mgg3.2420].
5. **Clinical implementation:** multidisciplinary chromatinopathy clinics increasingly integrate genomic sequencing, DNA-methylation profiling, anticipatory surveillance, and structured neurodevelopmental care; however, controlled ARTHS treatment trials remain absent.

## Evidence assessment and major gaps

The gene–disease relationship and core phenotype are strongly supported by repeated de novo variants, recurrence, variant enrichment, and consistent human phenotypes. Genotype–phenotype correlation is moderately strong but subject to ascertainment and incomplete standardized testing. Cellular acetylation and metabolic abnormalities have direct human in-vitro support but small sample sizes. The CA3 RSPO2/Wnt mechanism has unusually strong preclinical causal evidence—including conditional genetics and rescue—but has not been demonstrated in human brain tissue or clinical intervention.

Priority gaps are population prevalence, adult natural history, formal adaptive and quality-of-life trajectories, penetrance of nontruncating variants, systematic immune/hematologic surveillance data, human neuronal and organoid models, validated longitudinal biomarkers, and controlled therapeutic trials. Consequently, experimental supplements or pathway-directed interventions should not be represented as established therapy.

References

1. (kennedy2019kat6asyndromegenotype–phenotype pages 8-9): Joanna Kennedy, David Goudie, Edward Blair, Kate Chandler, Shelagh Joss, Victoria McKay, Andrew Green, Ruth Armstrong, Melissa Lees, Benjamin Kamien, Bruce Hopper, Tiong Yang Tan, Patrick Yap, Zornitza Stark, Nobuhiko Okamoto, Noriko Miyake, Naomichi Matsumoto, Ellen Macnamara, Jennifer L. Murphy, Elizabeth McCormick, Hakon Hakonarson, Marni J. Falk, Dong Li, Patrick Blackburn, Eric Klee, Dusica Babovic-Vuksanovic, Susan Schelley, Louanne Hudgins, Sarina Kant, Bertrand Isidor, Benjamin Cogne, Kimberley Bradbury, Mark Williams, Chirag Patel, Helen Heussler, Celia Duff-Farrier, Phillis Lakeman, Ingrid Scurr, Usha Kini, Mariet Elting, Margot Reijnders, Janneke Schuurs-Hoeijmakers, Mohamed Wafik, Anne Blomhoff, Claudia A.L. Ruivenkamp, Esther Nibbeling, Alexander J.M. Dingemans, Emilie D. Douine, Stanley F. Nelson, Maja Hempel, Tatjana Bierhals, Davor Lessel, Jessika Johannsen, Valerie A. Arboleda, and Ruth Newbury-Ecob. Kat6a syndrome: genotype–phenotype correlation in 76 patients with pathogenic kat6a variants. Genetics in Medicine, 21:850-860, Apr 2019. URL: https://doi.org/10.1038/s41436-018-0259-2, doi:10.1038/s41436-018-0259-2. This article has 134 citations and is from a highest quality peer-reviewed journal.

2. (kennedy2019kat6asyndromegenotype–phenotype pages 1-2): Joanna Kennedy, David Goudie, Edward Blair, Kate Chandler, Shelagh Joss, Victoria McKay, Andrew Green, Ruth Armstrong, Melissa Lees, Benjamin Kamien, Bruce Hopper, Tiong Yang Tan, Patrick Yap, Zornitza Stark, Nobuhiko Okamoto, Noriko Miyake, Naomichi Matsumoto, Ellen Macnamara, Jennifer L. Murphy, Elizabeth McCormick, Hakon Hakonarson, Marni J. Falk, Dong Li, Patrick Blackburn, Eric Klee, Dusica Babovic-Vuksanovic, Susan Schelley, Louanne Hudgins, Sarina Kant, Bertrand Isidor, Benjamin Cogne, Kimberley Bradbury, Mark Williams, Chirag Patel, Helen Heussler, Celia Duff-Farrier, Phillis Lakeman, Ingrid Scurr, Usha Kini, Mariet Elting, Margot Reijnders, Janneke Schuurs-Hoeijmakers, Mohamed Wafik, Anne Blomhoff, Claudia A.L. Ruivenkamp, Esther Nibbeling, Alexander J.M. Dingemans, Emilie D. Douine, Stanley F. Nelson, Maja Hempel, Tatjana Bierhals, Davor Lessel, Jessika Johannsen, Valerie A. Arboleda, and Ruth Newbury-Ecob. Kat6a syndrome: genotype–phenotype correlation in 76 patients with pathogenic kat6a variants. Genetics in Medicine, 21:850-860, Apr 2019. URL: https://doi.org/10.1038/s41436-018-0259-2, doi:10.1038/s41436-018-0259-2. This article has 134 citations and is from a highest quality peer-reviewed journal.

3. (liu2024kat6adeficiencyimpairs pages 8-9): Yongqing Liu, Minghua Fan, Junhua Yang, Ljubica Mihaljević, Kevin Hong Chen, Yingzhi Ye, Shuying Sun, and Zhaozhu Qiu. Kat6a deficiency impairs cognitive functions through suppressing rspo2/wnt signaling in hippocampal ca3. Science Advances, May 2024. URL: https://doi.org/10.1126/sciadv.adm9326, doi:10.1126/sciadv.adm9326. This article has 20 citations and is from a highest quality peer-reviewed journal.

4. (liu2024kat6adeficiencyimpairs pages 1-2): Yongqing Liu, Minghua Fan, Junhua Yang, Ljubica Mihaljević, Kevin Hong Chen, Yingzhi Ye, Shuying Sun, and Zhaozhu Qiu. Kat6a deficiency impairs cognitive functions through suppressing rspo2/wnt signaling in hippocampal ca3. Science Advances, May 2024. URL: https://doi.org/10.1126/sciadv.adm9326, doi:10.1126/sciadv.adm9326. This article has 20 citations and is from a highest quality peer-reviewed journal.

5. (bae2021identificationofa pages 1-2): Soyoung Bae, Aram Yang, Jinsup Kim, Hyun Ju Lee, and Hyun Kyung Park. Identification of a novel kat6a variant in an infant presenting with facial dysmorphism and developmental delay: a case report and literature review. BMC Medical Genomics, Dec 2021. URL: https://doi.org/10.1186/s12920-021-01148-x, doi:10.1186/s12920-021-01148-x. This article has 22 citations and is from a peer-reviewed journal.

6. (arboleda2015denovononsense pages 1-2): Valerie A. Arboleda, Hane Lee, Naghmeh Dorrani, Neda Zadeh, Mary Willis, Colleen Forsyth Macmurdo, Melanie A. Manning, Andrea Kwan, Louanne Hudgins, Florian Barthelemy, M. Carrie Miceli, Fabiola Quintero-Rivera, Sibel Kantarci, Samuel P. Strom, Joshua L. Deignan, Wayne W. Grody, Eric Vilain, and Stanley F. Nelson. De novo nonsense mutations in kat6a, a lysine acetyl-transferase gene, cause a syndrome including microcephaly and global developmental delay. American journal of human genetics, 96 3:498-506, Mar 2015. URL: https://doi.org/10.1016/j.ajhg.2015.01.017, doi:10.1016/j.ajhg.2015.01.017. This article has 172 citations and is from a highest quality peer-reviewed journal.

7. (OpenTargets Search: Arboleda-Tham syndrome-KAT6A): Open Targets Query (Arboleda-Tham syndrome-KAT6A, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (munueracabeza2022pantothenateandlcarnitine pages 1-2): Manuel Munuera-Cabeza, Mónica Álvarez-Córdoba, Juan Suárez-Rivero, Suleva Povea-Cabello, Irene Villalón-García, Marta Talaverón-Rey, Alejandra Suárez-Carrillo, Diana Reche-López, Paula Cilleros-Holgado, Rocío Piñero-Pérez, and José Sánchez-Alcázar. Pantothenate and l-carnitine supplementation improves pathological alterations in cellular models of kat6a syndrome. Genes, 13:2300, Dec 2022. URL: https://doi.org/10.3390/genes13122300, doi:10.3390/genes13122300. This article has 6 citations.

9. (lin2020diagnosisofarboledatham pages 3-4): Yung-Feng Lin, Tzu-Ching Lin, Ralph Kirby, Hui-Ying Weng, Yen-Ming Liu, Dau-Ming Niu, Shih-Feng Tsai, and Chia-Feng Yang. Diagnosis of arboleda-tham syndrome by whole genome sequencing in an asian boy with severe developmental delay. Molecular Genetics and Metabolism Reports, 25:100686, Dec 2020. URL: https://doi.org/10.1016/j.ymgmr.2020.100686, doi:10.1016/j.ymgmr.2020.100686. This article has 22 citations.

10. (kennedy2019kat6asyndromegenotype–phenotype pages 2-3): Joanna Kennedy, David Goudie, Edward Blair, Kate Chandler, Shelagh Joss, Victoria McKay, Andrew Green, Ruth Armstrong, Melissa Lees, Benjamin Kamien, Bruce Hopper, Tiong Yang Tan, Patrick Yap, Zornitza Stark, Nobuhiko Okamoto, Noriko Miyake, Naomichi Matsumoto, Ellen Macnamara, Jennifer L. Murphy, Elizabeth McCormick, Hakon Hakonarson, Marni J. Falk, Dong Li, Patrick Blackburn, Eric Klee, Dusica Babovic-Vuksanovic, Susan Schelley, Louanne Hudgins, Sarina Kant, Bertrand Isidor, Benjamin Cogne, Kimberley Bradbury, Mark Williams, Chirag Patel, Helen Heussler, Celia Duff-Farrier, Phillis Lakeman, Ingrid Scurr, Usha Kini, Mariet Elting, Margot Reijnders, Janneke Schuurs-Hoeijmakers, Mohamed Wafik, Anne Blomhoff, Claudia A.L. Ruivenkamp, Esther Nibbeling, Alexander J.M. Dingemans, Emilie D. Douine, Stanley F. Nelson, Maja Hempel, Tatjana Bierhals, Davor Lessel, Jessika Johannsen, Valerie A. Arboleda, and Ruth Newbury-Ecob. Kat6a syndrome: genotype–phenotype correlation in 76 patients with pathogenic kat6a variants. Genetics in Medicine, 21:850-860, Apr 2019. URL: https://doi.org/10.1038/s41436-018-0259-2, doi:10.1038/s41436-018-0259-2. This article has 134 citations and is from a highest quality peer-reviewed journal.

11. (urreizti2020fivenewcases pages 7-8): Roser Urreizti, Estrella Lopez-Martin, Antonio Martinez-Monseny, Montse Pujadas, Laura Castilla-Vallmanya, Luis Alberto Pérez-Jurado, Mercedes Serrano, Daniel Natera-de Benito, Beatriz Martínez-Delgado, Manuel Posada-de-la-Paz, Javier Alonso, Purificación Marin-Reina, Mar O’Callaghan, Daniel Grinberg, Eva Bermejo-Sánchez, and Susanna Balcells. Five new cases of syndromic intellectual disability due to kat6a mutations: widening the molecular and clinical spectrum. Orphanet Journal of Rare Diseases, Feb 2020. URL: https://doi.org/10.1186/s13023-020-1317-9, doi:10.1186/s13023-020-1317-9. This article has 48 citations and is from a peer-reviewed journal.

12. (kennedy2019kat6asyndromegenotype–phenotype pages 6-7): Joanna Kennedy, David Goudie, Edward Blair, Kate Chandler, Shelagh Joss, Victoria McKay, Andrew Green, Ruth Armstrong, Melissa Lees, Benjamin Kamien, Bruce Hopper, Tiong Yang Tan, Patrick Yap, Zornitza Stark, Nobuhiko Okamoto, Noriko Miyake, Naomichi Matsumoto, Ellen Macnamara, Jennifer L. Murphy, Elizabeth McCormick, Hakon Hakonarson, Marni J. Falk, Dong Li, Patrick Blackburn, Eric Klee, Dusica Babovic-Vuksanovic, Susan Schelley, Louanne Hudgins, Sarina Kant, Bertrand Isidor, Benjamin Cogne, Kimberley Bradbury, Mark Williams, Chirag Patel, Helen Heussler, Celia Duff-Farrier, Phillis Lakeman, Ingrid Scurr, Usha Kini, Mariet Elting, Margot Reijnders, Janneke Schuurs-Hoeijmakers, Mohamed Wafik, Anne Blomhoff, Claudia A.L. Ruivenkamp, Esther Nibbeling, Alexander J.M. Dingemans, Emilie D. Douine, Stanley F. Nelson, Maja Hempel, Tatjana Bierhals, Davor Lessel, Jessika Johannsen, Valerie A. Arboleda, and Ruth Newbury-Ecob. Kat6a syndrome: genotype–phenotype correlation in 76 patients with pathogenic kat6a variants. Genetics in Medicine, 21:850-860, Apr 2019. URL: https://doi.org/10.1038/s41436-018-0259-2, doi:10.1038/s41436-018-0259-2. This article has 134 citations and is from a highest quality peer-reviewed journal.

13. (bae2021identificationofa pages 5-6): Soyoung Bae, Aram Yang, Jinsup Kim, Hyun Ju Lee, and Hyun Kyung Park. Identification of a novel kat6a variant in an infant presenting with facial dysmorphism and developmental delay: a case report and literature review. BMC Medical Genomics, Dec 2021. URL: https://doi.org/10.1186/s12920-021-01148-x, doi:10.1186/s12920-021-01148-x. This article has 22 citations and is from a peer-reviewed journal.

14. (urreizti2020fivenewcases pages 6-7): Roser Urreizti, Estrella Lopez-Martin, Antonio Martinez-Monseny, Montse Pujadas, Laura Castilla-Vallmanya, Luis Alberto Pérez-Jurado, Mercedes Serrano, Daniel Natera-de Benito, Beatriz Martínez-Delgado, Manuel Posada-de-la-Paz, Javier Alonso, Purificación Marin-Reina, Mar O’Callaghan, Daniel Grinberg, Eva Bermejo-Sánchez, and Susanna Balcells. Five new cases of syndromic intellectual disability due to kat6a mutations: widening the molecular and clinical spectrum. Orphanet Journal of Rare Diseases, Feb 2020. URL: https://doi.org/10.1186/s13023-020-1317-9, doi:10.1186/s13023-020-1317-9. This article has 48 citations and is from a peer-reviewed journal.

15. (arboleda2015denovononsense pages 6-7): Valerie A. Arboleda, Hane Lee, Naghmeh Dorrani, Neda Zadeh, Mary Willis, Colleen Forsyth Macmurdo, Melanie A. Manning, Andrea Kwan, Louanne Hudgins, Florian Barthelemy, M. Carrie Miceli, Fabiola Quintero-Rivera, Sibel Kantarci, Samuel P. Strom, Joshua L. Deignan, Wayne W. Grody, Eric Vilain, and Stanley F. Nelson. De novo nonsense mutations in kat6a, a lysine acetyl-transferase gene, cause a syndrome including microcephaly and global developmental delay. American journal of human genetics, 96 3:498-506, Mar 2015. URL: https://doi.org/10.1016/j.ajhg.2015.01.017, doi:10.1016/j.ajhg.2015.01.017. This article has 172 citations and is from a highest quality peer-reviewed journal.

16. (weber2023thehistoneacetyltransferase pages 1-2): Lisa Marie Weber, Yulin Jia, Bastian Stielow, Stephen S Gisselbrecht, Yinghua Cao, Yanpeng Ren, Iris Rohner, Jessica King, Elisabeth Rothman, Sabrina Fischer, Clara Simon, Ignasi Forné, Andrea Nist, Thorsten Stiewe, Martha L Bulyk, Zhanxin Wang, and Robert Liefke. The histone acetyltransferase kat6a is recruited to unmethylated cpg islands via a dna binding winged helix domain. Nucleic Acids Research, 51:574-594, Dec 2023. URL: https://doi.org/10.1093/nar/gkac1188, doi:10.1093/nar/gkac1188. This article has 44 citations and is from a highest quality peer-reviewed journal.

17. (munueracabeza2022pantothenateandlcarnitine pages 15-16): Manuel Munuera-Cabeza, Mónica Álvarez-Córdoba, Juan Suárez-Rivero, Suleva Povea-Cabello, Irene Villalón-García, Marta Talaverón-Rey, Alejandra Suárez-Carrillo, Diana Reche-López, Paula Cilleros-Holgado, Rocío Piñero-Pérez, and José Sánchez-Alcázar. Pantothenate and l-carnitine supplementation improves pathological alterations in cellular models of kat6a syndrome. Genes, 13:2300, Dec 2022. URL: https://doi.org/10.3390/genes13122300, doi:10.3390/genes13122300. This article has 6 citations.

18. (lin2020diagnosisofarboledatham pages 1-3): Yung-Feng Lin, Tzu-Ching Lin, Ralph Kirby, Hui-Ying Weng, Yen-Ming Liu, Dau-Ming Niu, Shih-Feng Tsai, and Chia-Feng Yang. Diagnosis of arboleda-tham syndrome by whole genome sequencing in an asian boy with severe developmental delay. Molecular Genetics and Metabolism Reports, 25:100686, Dec 2020. URL: https://doi.org/10.1016/j.ymgmr.2020.100686, doi:10.1016/j.ymgmr.2020.100686. This article has 22 citations.

19. (bae2021identificationofa pages 6-7): Soyoung Bae, Aram Yang, Jinsup Kim, Hyun Ju Lee, and Hyun Kyung Park. Identification of a novel kat6a variant in an infant presenting with facial dysmorphism and developmental delay: a case report and literature review. BMC Medical Genomics, Dec 2021. URL: https://doi.org/10.1186/s12920-021-01148-x, doi:10.1186/s12920-021-01148-x. This article has 22 citations and is from a peer-reviewed journal.

20. (kennedy2019kat6asyndromegenotype–phenotype pages 9-10): Joanna Kennedy, David Goudie, Edward Blair, Kate Chandler, Shelagh Joss, Victoria McKay, Andrew Green, Ruth Armstrong, Melissa Lees, Benjamin Kamien, Bruce Hopper, Tiong Yang Tan, Patrick Yap, Zornitza Stark, Nobuhiko Okamoto, Noriko Miyake, Naomichi Matsumoto, Ellen Macnamara, Jennifer L. Murphy, Elizabeth McCormick, Hakon Hakonarson, Marni J. Falk, Dong Li, Patrick Blackburn, Eric Klee, Dusica Babovic-Vuksanovic, Susan Schelley, Louanne Hudgins, Sarina Kant, Bertrand Isidor, Benjamin Cogne, Kimberley Bradbury, Mark Williams, Chirag Patel, Helen Heussler, Celia Duff-Farrier, Phillis Lakeman, Ingrid Scurr, Usha Kini, Mariet Elting, Margot Reijnders, Janneke Schuurs-Hoeijmakers, Mohamed Wafik, Anne Blomhoff, Claudia A.L. Ruivenkamp, Esther Nibbeling, Alexander J.M. Dingemans, Emilie D. Douine, Stanley F. Nelson, Maja Hempel, Tatjana Bierhals, Davor Lessel, Jessika Johannsen, Valerie A. Arboleda, and Ruth Newbury-Ecob. Kat6a syndrome: genotype–phenotype correlation in 76 patients with pathogenic kat6a variants. Genetics in Medicine, 21:850-860, Apr 2019. URL: https://doi.org/10.1038/s41436-018-0259-2, doi:10.1038/s41436-018-0259-2. This article has 134 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Arboleda-Tham_Syndrome-deep-research-falcon_artifacts/artifact-00.md)