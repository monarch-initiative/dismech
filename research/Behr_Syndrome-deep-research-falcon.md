---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-30T23:22:48.770649'
end_time: '2026-07-30T23:31:24.702628'
duration_seconds: 515.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Behr Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Behr_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Behr Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Behr Syndrome** covering all of the
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
- **Disease Name:** Behr Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Behr Syndrome** covering all of the
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


# Behr Syndrome: Comprehensive Disease-Characteristics Report

**Scope and evidence date.** This report treats “Behr syndrome” in its modern, molecularly resolved sense: a severe, usually childhood-onset **biallelic OPA1-related neuro-ophthalmologic disorder**. Historical use was phenotype-based and can encompass genetically distinct “Behr-like” disorders. Most evidence comes from aggregated disease resources, small case series, individual patients, and OPA1 cellular/animal models—not EHR-scale cohorts or randomized Behr-specific trials.

## Executive summary

Behr syndrome is a very rare Mendelian mitochondrial-neurodegenerative syndrome characterized by early bilateral optic atrophy followed or accompanied by cerebellar ataxia, pyramidal signs/spasticity, peripheral neuropathy, and variably developmental, auditory, gastrointestinal, muscular, and cerebral abnormalities. Current disease-resource evidence maps it to **MONDO:0008858** and strongly associates it with **OPA1**; Open Targets reports an association score of 0.812 and cites genetic evidence including PMID 27604308, 17722006, 28494813, 24970096, 11017079, 27150940, 11017080, 25012220, and 35741767. (OpenTargets Search: Behr syndrome)

The mechanistic core is failure of OPA1-dependent inner-mitochondrial-membrane fusion and crista organization, producing mitochondrial fragmentation, respiratory dysfunction, impaired mtDNA maintenance, disturbed calcium/redox homeostasis, excessive mitophagy or apoptosis, and preferential degeneration of metabolically demanding long-projecting neurons—especially retinal ganglion cells. No approved disease-modifying therapy or Behr-specific treatment trial exists; current care is multidisciplinary and supportive. Trials of the oligonucleotide PYC-001 concern **dominant OPA1 haploinsufficiency** and expressly exclude ADOA-plus phenotypes, so they should not be represented as Behr-syndrome trials. (NCT06970106 chunk 1, NCT06970106 chunk 2, NCT06461286 chunk 1, NCT06461286 chunk 2)

## 1. Disease information

### Definition and nosology

Behr syndrome is a syndromic hereditary optic neuropathy in which childhood optic atrophy occurs with spinocerebellar degeneration, pyramidal-tract dysfunction, and peripheral neuropathy. A current review describes it as childhood-onset optic atrophy with “ataxia and pyramidal signs including spasticity, weakness, and hyperreflexia.” (ojaimi2022mitochondrialfissionand pages 7-8)

**Key identifiers**

- **MONDO:** MONDO:0008858.
- **OMIM/MIM:** **210000**.
- **Causal-gene resource mapping:** OPA1, Ensembl ENSG00000198836; approved name “OPA1 mitochondrial dynamin like GTPase.” (OpenTargets Search: Behr syndrome)
- **MeSH:** no retrieved disease-specific descriptor; broader applicable descriptors include *Optic Atrophies, Hereditary* (D015418), *Optic Atrophy* (D009896), and *Mitochondrial Diseases* (D028361). (NCT06461286 chunk 2)
- **ICD-10/ICD-11:** no uniquely validated Behr-syndrome code was identified. Coding generally falls under hereditary optic atrophy/optic-nerve or mitochondrial disease categories; local coding should not be treated as molecularly specific.
- **Orphanet:** a reliable disease-specific ORPHA number was not recovered from the available evidence and should be curator-verified rather than inferred.

**Synonyms/labels:** Behr’s syndrome; complicated hereditary infantile optic atrophy; complicated optic atrophy; OPA1-related Behr syndrome; Behr-related syndrome; recessive/compound-heterozygous OPA1 optic atrophy. “DOA-plus” overlaps phenotypically but generally refers to multisystem disease from monoallelic OPA1 variants and is not always equivalent.

**Important terminology warning:** **OPA3-related Costeff syndrome**—3-methylglutaconic aciduria type III—is a close differential, not a strict synonym. OPA3 can also cause dominant optic atrophy-cataract-plus disease. Primary literature supporting OPA3 phenotypes includes PMID **15342707**, **22797356**, **24136862**, and **28050599**. (weisschuh2021mutationspectrumof pages 17-18)

## 2. Etiology, causal factors, and risks

### Genetic cause

The established cause is **biallelic germline pathogenic variants in OPA1**, usually compound heterozygous and less commonly homozygous, producing autosomal-recessive disease. By 2011, 14 affected individuals from 13 families carrying compound-heterozygous or homozygous OPA1 variants had been documented. The first molecularly defined case, reported in 2001, carried two heterozygous missense variants in exon 8. (nottia2021mitochondrialdynamicsmolecular pages 8-10)

OPA1 variants across the broader disease spectrum include missense, nonsense, frameshift, splice-altering, and copy-number alleles. In a 755-proband optic-atrophy cohort, 278 probands (36.8%) had putatively pathogenic OPA1 variants; 156 unique variants were found, 78% were null alleles, and c.2708_2711del/p.(Val903Glyfs*3) represented 14% of disease-causing alleles. These are **OPA1-spectrum statistics**, not Behr-specific frequencies. The study classified nine novel variants as pathogenic, 34 as likely pathogenic, and five as VUS. DOI: https://doi.org/10.1371/journal.pone.0253987, published 9 July 2021. (weisschuh2021mutationspectrumof pages 17-18)

A typical recessive genotype combines a severe loss-of-function allele with a hypomorphic missense allele; two severe alleles can cause a much more severe mitochondrial encephalomyopathy, sometimes with cardiomyopathy, lactic acidemia, and death. Variant interpretation must therefore be allele- and phase-specific. Homozygous or compound severe alleles should not automatically be equated with the survivable classic Behr phenotype. (nottia2021mitochondrialdynamicsmolecular pages 8-10)

All established causal variants are constitutional/germline. Somatic mutation is not a recognized Behr mechanism. Population allele frequency must be checked variant-by-variant in gnomAD/TOPMed; no defensible aggregate carrier frequency was found. Pathogenic recessive alleles are expected to be rare, and an allele too frequent for this ultra-rare phenotype requires reassessment.

### Environmental, lifestyle, infectious, and protective factors

No environmental toxin, infection, diet, occupation, smoking pattern, sex, or lifestyle exposure is established as a cause or penetrance determinant. No validated protective genetic allele, dietary factor, or gene-environment interaction has been demonstrated specifically for Behr syndrome. General mitochondrial-health advice—avoid smoking, excessive alcohol, malnutrition, and unnecessary mitochondrial-toxic drugs—is prudent but not proven to alter this disease’s natural history.

Family history, parental consanguinity, and ancestry can increase the prior probability of recessive disease but are not biological causes independent of genotype. No robust founder effect, anticipation, germline-mosaicism rate, or sex bias has been established.

## 3. Phenotypes

The phenotype is highly variable, and Behr-specific percentages are generally unavailable because published cohorts are very small.

- **Bilateral optic atrophy/optic neuropathy**—usually infancy or childhood onset, progressive and irreversible; impaired acuity, color vision, central/centrocecal field loss, and later severe visual disability. Suggested HPO: **HP:0000648**.
- **Ataxia/spinocerebellar degeneration**—childhood or later, generally progressive; dysmetria, dysdiadochokinesia, nystagmus, and gait instability. HPO: **HP:0001251**; dysmetria and nystagmus may be separately encoded.
- **Pyramidal signs**—spasticity, hyperreflexia, weakness, and sometimes extensor plantar responses; progressive mobility limitation. HPO: **HP:0001257** and relevant hyperreflexia terms.
- **Peripheral neuropathy/posterior-column dysfunction**—sensory loss, weakness, areflexic components, pes cavus, and contractures. HPO: **HP:0009830**, **HP:0001761**.
- **Developmental delay/hypotonia**—particularly in severe early-onset disease; delayed motor milestones may precede gait decline. HPO: **HP:0001263**, **HP:0001252**.
- **Hearing impairment**, often sensorineural; HPO: **HP:0000365**.
- **Dysarthria and dysphagia**; HPO: **HP:0001260**, **HP:0002015**.
- **Gastrointestinal dysmotility**—vomiting, constipation, dysphagia, and feeding difficulty.
- **Musculoskeletal manifestations**—pes cavus and severe lower-limb contractures.
- **Severe-variable manifestations**—lactic acidemia, myopathy, cardiomyopathy, developmental encephalopathy, and Leigh-like episodes have occurred in the most severe biallelic disease. (ojaimi2022mitochondrialfissionand pages 7-8, nottia2021mitochondrialdynamicsmolecular pages 8-10)

MRI can show optic-nerve/chiasm atrophy, cerebellar or vermian atrophy (**HP:0001272**), periventricular white-matter abnormalities, and occasionally Leigh-like basal-ganglia hyperintensities with lactate accumulation. (ojaimi2022mitochondrialfissionand pages 7-8, nottia2021mitochondrialdynamicsmolecular pages 8-10)

### Quality-of-life impact

No Behr-specific EQ-5D, SF-36, PROMIS, or utility study was identified. Expected burden is substantial: visual impairment limits reading, education, orientation, and driving; ataxia/spasticity/neuropathy impair walking and self-care; hearing loss and dysarthria impair communication; dysphagia and contractures add aspiration, nutrition, pain, and caregiver burdens. These effects are clinically plausible but have not been quantified with a validated Behr-specific instrument.

## 4. Genetic and molecular information

**OPA1** encodes a ubiquitously expressed dynamin-like GTPase localized to the mitochondrial inner membrane. More than 500 OPA1 variants had been described in a 2024 review; the two principal mechanisms across dominant disease are haploinsufficiency and dominant-negative interference. Splice/deletion null alleles often cause haploinsufficiency, whereas some missense alleles exert stronger functional effects. Compound heterozygosity can shift disease from isolated dominant optic atrophy to early multisystem Behr syndrome. (lee2024hereditaryopticneuropathies pages 5-7)

For a knowledge-base entry, each reported allele should include HGVS transcript, genome build, phase, ClinVar accession, ACMG/AMP classification, gnomAD ancestry-specific frequency, and functional assay. VUS should not be promoted to causal without segregation, transcript, protein, or mitochondrial-function evidence. Deep-intronic splice variants and copy-number changes are diagnostically relevant; RNA/minigene analysis may resolve uncertain splice effects.

No reproducible modifier gene is established. Patient-derived neurons carrying the same OPA1 variant can have different clinical severity, but candidate modifiers remain unresolved. Broader OPA1 work reports altered CpG methylation and downregulation of developmental genes in OPA1-haploinsufficient neural progenitors; this is mechanistic model evidence, not a validated Behr epigenetic biomarker. (dotto2021dominantopticatrophy pages 5-6)

No recurrent disease-defining aneuploidy, translocation, inversion, or large chromosomal syndrome is established. Consequently, karyotyping, FISH, and CMA are not first-line unless the phenotype suggests an independent chromosomal diagnosis.

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupational exposure, lifestyle factor, or infectious agent is known to initiate Behr syndrome. It is not infectious, transmissible, or zoonotic. Evidence for oxidative stress is downstream of inherited mitochondrial dysfunction rather than proof of an environmental etiology. Environmental avoidance recommendations should therefore be labeled precautionary, not disease-preventive.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic trigger:** two functionally damaging OPA1 alleles reduce or qualitatively impair OPA1.
2. **Primary organellar defect:** impaired inner-membrane fusion, cardiolipin-dependent membrane remodeling, and crista-junction organization cause fragmented mitochondria and disordered cristae.
3. **Bioenergetic/quality-control consequences:** destabilized respiratory-chain supercomplexes, reduced oxygen consumption/OXPHOS, impaired mtDNA maintenance or depletion, abnormal calcium handling, ROS stress, and altered autophagy/mitophagy.
4. **Cell-death and connectivity consequences:** cytochrome-c/apoptotic susceptibility, reduced axonal mitochondrial density, defective synaptogenesis, and progressive axonal degeneration.
5. **Tissue selectivity:** retinal ganglion cells and long central/peripheral neurons have high energy demand and long axons, making them particularly vulnerable; degeneration produces optic atrophy, corticospinal signs, neuropathy, and cerebellar dysfunction. OPA1 also regulates cytochrome-c release and apoptosis. (strachan2025novelinvivo pages 1-2, dotto2021dominantopticatrophy pages 10-11, alavi2013dominantopticatrophy pages 1-3, fogazza2018biochemicalcharacterizationand pages 35-38)

Human cellular and muscle observations include fragmented mitochondrial networks, ragged-red fibers, diminished cytochrome-c oxidase staining, reduced complex-IV activity, and mtDNA depletion in severe disease. (nottia2021mitochondrialdynamicsmolecular pages 8-10, ojaimi2022mitochondrialfissionand pages 7-8)

**Suggested GO annotations:** mitochondrial inner membrane fusion (**GO:0007342**), mitochondrial inner membrane (**GO:0005743**), mitochondrial crista, mitochondrial organization, oxidative phosphorylation, respiratory electron transport, mitochondrial DNA maintenance, mitophagy, intrinsic apoptotic signaling, calcium-ion homeostasis, and response to oxidative stress. Exact current GO IDs beyond those shown should be ontology-version checked.

**Suggested cells:** retinal ganglion cell (**CL:0000704**, verify current release), cerebellar neuron/Purkinje cell, corticospinal motor neuron, peripheral sensory neuron, peripheral motor neuron, and skeletal myocyte. Only retinal-ganglion-cell vulnerability is directly and repeatedly demonstrated; other cell assignments partly follow clinical localization.

### Molecular profiling and advanced technologies

Metabolomic work in OPA1-disrupted fibroblasts identified a bioenergetic signature including aspartate deficiency; lipidomics found triacylglycerol accumulation from impaired fatty-acid flux. These findings are not validated clinical biomarkers. iPSC lines have been generated directly from a Behr patient for disease modeling (Hauser et al., *Stem Cell Research*, 2016; DOI https://doi.org/10.1016/j.scr.2016.09.012). Broader OPA1 iPSC neurons exhibit reduced oxygen consumption, complex-I abundance/activity, mitochondrial fragmentation, ROS elevation, impaired axonal mitochondrial distribution, and loss of synaptic contacts. (dotto2021dominantopticatrophy pages 10-11, dotto2021dominantopticatrophy pages 5-6)

No validated Behr-specific single-cell atlas, spatial-transcriptomic signature, plasma proteomic panel, metabolomic diagnostic classifier, or multi-omics prognostic model was identified.

## 7. Anatomical structures affected

**Primary:** bilateral retina—especially retinal ganglion-cell layer—and optic nerves/optic chiasm. **Neurologic:** cerebellum and vermis, corticospinal/pyramidal tracts, posterior columns, peripheral nerves, and variably cerebral white matter/basal ganglia. **Secondary/variable:** skeletal muscle, auditory pathway, gastrointestinal neuromuscular system, and heart in severe biallelic disease. (ojaimi2022mitochondrialfissionand pages 7-8, nottia2021mitochondrialdynamicsmolecular pages 8-10)

Suggested UBERON terms include retina, retinal ganglion-cell layer, optic nerve, optic chiasm, cerebellum, cerebellar vermis, corticospinal tract, spinal-cord posterior column, peripheral nerve, skeletal muscle, and heart. Exact IDs require release-specific verification. Ocular and neurologic involvement is generally bilateral; asymmetry can occur clinically but unilateral disease would be atypical and should prompt reconsideration.

Subcellular localization is predominantly the mitochondrial inner membrane and cristae; downstream abnormalities involve respiratory-chain complexes, mitochondrial nucleoids/mtDNA, and autophagic/lysosomal pathways.

## 8. Temporal development

Onset is usually insidious in infancy or childhood. Optic neuropathy and developmental/motor abnormalities often occur first; gait difficulty commonly becomes prominent in the second decade. Rare adult-onset optic atrophy-ataxia presentations are reported. Disease is chronic and generally progressive, not relapsing-remitting. (ojaimi2022mitochondrialfissionand pages 7-8, nottia2021mitochondrialdynamicsmolecular pages 8-10)

A practical—not formally validated—staging framework is:

- **Early:** reduced visual acuity/color discrimination and optic pallor, sometimes delayed motor development.
- **Intermediate:** gait ataxia, spasticity/hyperreflexia, neuropathy, dysarthria, and hearing impairment.
- **Advanced:** severe visual disability, loss of independent ambulation, contractures, dysphagia, and multisystem complications.

No spontaneous remission pattern is established. The most plausible therapeutic window is before irreversible retinal-ganglion-cell and long-tract axonal loss, but this remains a mechanistic inference rather than a proven Behr intervention window.

## 9. Inheritance and population

Classic molecularly defined OPA1-related Behr syndrome is **autosomal recessive**. Recurrence risk is 25% per pregnancy when both parents are heterozygous carriers, with a 50% carrier probability and 25% probability of inheriting neither familial allele. Expressivity is variable and depends strongly on allele severity. Penetrance cannot be reliably quantified from available cohorts. Anticipation is not expected because repeat expansion is not the mechanism.

No population-based Behr prevalence or incidence was found. The approximately **1 in 30,000**, and in some populations **1 in 12,000**, estimates concern autosomal/dominant optic atrophy broadly—not Behr syndrome. Approximately 20% of autosomal optic atrophy cases have extraocular AOA-plus features, again not a Behr-specific statistic. (strachan2025novelinvivo pages 1-2)

No reliable sex ratio, age distribution, carrier frequency, geographic clustering, or ancestry-specific prevalence is available. Consanguinity can enrich homozygosity in individual families, but its population contribution is unquantified.

## 10. Diagnostics

### Clinical evaluation

Diagnosis begins with bilateral optic atrophy plus neurologic examination for ataxia, pyramidal signs, neuropathy, developmental delay, hearing loss, and bulbar or gastrointestinal dysfunction. Recommended investigations include:

- Best-corrected and low-contrast visual acuity, color testing, fundus examination, static perimetry.
- Spectral-domain OCT of retinal nerve-fiber and ganglion-cell layers.
- Visual evoked potentials; ERG when retinal dystrophy is a concern.
- Brain/orbit MRI for optic nerve/chiasm and cerebellar/white-matter abnormalities.
- Audiology, EMG/nerve-conduction studies, gait assessment, and swallowing evaluation as indicated.
- Blood lactate, CK, metabolic panel, and ECG/echocardiography where systemic disease is suspected; normal results do not exclude Behr syndrome.
- Muscle biopsy and respiratory-chain/mtDNA studies are now second-line, useful when sequencing is inconclusive or a severe mitochondrial phenotype requires functional clarification. Trial protocols illustrate current quantitative ophthalmic endpoints, including ETDRS acuity, perimetry, mfVEP, OCT RNFL/GCL, flavoprotein fluorescence, and retinal-apoptosis imaging. (NCT06970106 chunk 2, NCT06461286 chunk 1, NCT06461286 chunk 2)

### Genetic testing strategy

1. Use a hereditary optic neuropathy/mitochondrial-neurodegeneration panel including **OPA1**, with deletion/duplication detection and adequate intronic splice coverage.
2. If unrevealing or phenotype is complex, use trio WES or WGS; broader genomic testing is preferred when no familial variant is known.
3. Confirm both variants, phase them in parents, apply ACMG/AMP criteria, and perform RNA studies for suspected splice variants.
4. mtDNA sequencing is useful for LHON/NARP/Leigh differentials but is not the primary test for OPA1-related Behr syndrome.
5. CMA, karyotype, FISH, and repeat-expansion testing are phenotype-directed, not routine Behr tests. (lee2024hereditaryopticneuropathies pages 5-7)

There are no universally accepted clinical criteria independent of molecular confirmation. Genetic diagnosis is therefore central.

### Differential diagnosis

Major alternatives are OPA3/Costeff syndrome, dominant OPA1/DOA-plus, SPG7- and AFG3L2-related optic atrophy/spastic ataxia, MFN2 neuropathy, WFS1 spectrum, ACO2 cerebellar-retinal degeneration, SSBP1 mtDNA-maintenance disease, DNAJC30 recessive LHON, mitochondrial LHON/NARP/Leigh syndromes, Friedreich ataxia, complicated hereditary spastic paraplegias, and leukodystrophies. OPA3 disease is favored by 3-methylglutaconic aciduria and its characteristic genetic/ocular spectrum.

No newborn population screening is established. Cascade testing of relatives and targeted familial-variant testing are appropriate after molecular confirmation.

## 11. Outcome and prognosis

The usual course is lifelong and progressive. Vision loss generally does not spontaneously recover in OPA1 disease. Neurologic disability can advance from gait difficulty to loss of independent ambulation, with additional morbidity from contractures, falls, hearing loss, dysphagia, aspiration, and nutritional compromise. (lee2024hereditaryopticneuropathies pages 5-7)

No valid 5- or 10-year survival rate, median life expectancy, mortality rate, or Behr-specific quality-of-life statistic exists. Many patients survive into adulthood, but severe homozygous/biallelic mitochondrial encephalomyopathy can include cardiomyopathy and fatal outcomes. Prognosis likely depends on residual OPA1 function, age at onset, neurologic burden, cardiomyopathy/lactic acidosis, swallowing safety, and rate of visual/motor decline, but no validated prognostic model or biomarker exists. (nottia2021mitochondrialdynamicsmolecular pages 8-10)

## 12. Treatment

### Current real-world management

No FDA/EMA-approved pharmacologic, gene, RNA, or cell therapy exists specifically for Behr syndrome. Management is individualized and multidisciplinary:

- Low-vision rehabilitation, optical/electronic aids, educational accommodations, orientation and mobility training.
- Physical and occupational therapy, gait aids, orthoses, stretching, contracture prevention, and fall prevention.
- Symptomatic antispasticity treatment when benefits exceed weakness/sedation risks.
- Speech-language therapy and augmentative communication.
- Audiology and hearing aids/cochlear-implant assessment.
- Swallow evaluation, diet modification, nutrition support, and gastrostomy when clinically necessary.
- Neuropathic-pain treatment, orthopedic management, cardiology surveillance in severe phenotypes, and psychosocial support.

Suggested MAXO concepts include ophthalmologic examination, OCT, visual-field testing, low-vision therapy, physical therapy, occupational therapy, speech therapy, hearing-aid fitting, dysphagia management, enteral feeding, orthotic treatment, and genetic counseling; exact MAXO IDs should be curator-verified.

Idebenone has only weak, uncontrolled evidence in dominant optic atrophy: a small phase-II study reported a statistically significant but minor visual-acuity recovery after 12 months at 900 mg/day, with major limitations from sample size and lack of a control group. It cannot be considered established Behr treatment. (lee2024hereditaryopticneuropathies pages 5-7)

### Experimental therapy and trials

**NCT06461286 (Sundew)** is a first-in-human phase 1a study of one intravitreal PYC-001 dose in approximately 18 adults with confirmed **OPA1 haploinsufficiency-associated dominant optic atrophy**; it began 31 October 2024 and was active, not recruiting, in the retrieved registry record. PYC-001 is an oligonucleotide therapeutic. Crucially, the protocol excludes ADOA-plus and non-haploinsufficiency mechanisms; therefore Behr patients are not the intended population. Registry URL: https://clinicaltrials.gov/study/NCT06461286. (NCT06461286 chunk 1, NCT06461286 chunk 2)

**NCT06970106 (Myrtle)** is a phase 1b/1–2 open-label dose study of intravitreal peptide-phosphorodiamidate morpholino PYC-001, estimated enrollment 24, with 10–60 µg single/repeat-dose cohorts. It began 30 September 2025 and was recruiting in the retrieved record. Eligibility again requires dominant OPA1 haploinsufficiency and excludes ADOA-plus/confounding variants. Registry URL: https://clinicaltrials.gov/study/NCT06970106. (NCT06970106 chunk 1, NCT06970106 chunk 2)

Gene augmentation, splice correction, CRISPR repair, iPSC-derived retinal-ganglion-cell replacement, antioxidant treatment, and mitophagy/necroptosis modulation remain preclinical. Their major challenge is the allele-specific combination of one severe and one hypomorphic OPA1 allele and the need to reach both retina and systemic nervous tissue.

## 13. Prevention

Primary lifestyle prevention and vaccination are not applicable to this inherited disorder. The principal prevention options are reproductive and molecular:

- Genetic counseling and parental phasing.
- Cascade carrier testing of adult relatives.
- Prenatal diagnosis by CVS/amniocentesis when familial pathogenic variants are known.
- IVF with preimplantation genetic testing for monogenic disease.
- Early targeted testing of at-risk siblings to permit surveillance and rehabilitation before major functional loss.

Tertiary prevention includes fall prevention, contracture management, aspiration/nutrition surveillance, hearing and vision rehabilitation, and monitoring for cardiomyopathy or metabolic decompensation in severe cases. Avoiding tobacco, excessive alcohol, and unnecessary mitochondrial toxins is reasonable general advice but is not proven primary prevention.

## 14. Other species and natural disease

No well-established naturally occurring veterinary disease precisely equivalent to human biallelic OPA1 Behr syndrome was identified. OPA1 is evolutionarily conserved across vertebrates and invertebrate ortholog systems. There is no transmission or zoonotic potential.

OPA3-related natural/model phenotypes should not be merged with OPA1 Behr syndrome. A murine Opa3 missense model reproduces aspects of Costeff syndrome, and zebrafish opa3 models have illuminated metabolic/protective functions, but these model a differential disease mechanism rather than OPA1-related Behr syndrome.

## 15. Model organisms and experimental systems

- **Patient fibroblasts/muscle:** mitochondrial fragmentation, COX/complex-IV defects, mtDNA depletion, and abnormal bioenergetics; directly relevant but limited in modeling retinal and long-axon vulnerability.
- **Patient-derived iPSCs:** an “iPS-OPA1-BEHR” line was generated specifically for complex optic-atrophy/Behr modeling (DOI https://doi.org/10.1016/j.scr.2016.09.012). iPSC neurons enable studies of respiration, ROS, axonal mitochondrial transport, and synaptic degeneration but lack whole-organism natural history. (dotto2021dominantopticatrophy pages 10-11)
- **Mouse:** heterozygous Opa1 models show age-dependent RGC dysfunction/loss, optic-nerve demyelination/axonal degeneration, mitochondrial ultrastructural abnormalities, and increased autophagy/mitophagy. Homozygous knockout is embryonic lethal, limiting recreation of survivable biallelic Behr disease. (dotto2021dominantopticatrophy pages 5-6)
- **Zebrafish:** morpholino depletion causes developmental delay, small eyes, reduced circulation and heart rate, mitochondrial fragmentation, and impaired bioenergetics. A recent CRISPR Opa1 knockout produced visual impairment before RGC degeneration, fragmented axonal mitochondria, disordered cristae, and reduced respiration while early locomotion remained relatively preserved. This temporal ordering supports mitochondrial dysfunction as upstream of neuronal loss. DOI https://doi.org/10.1096/fj.202403271R; accepted 19 March 2025. (strachan2025novelinvivo pages 1-2)
- **Drosophila:** Opa1 deficiency causes reduced survival, visual and cardiac abnormalities, elevated ROS, dysmorphic mitochondria, and age-dependent multisystem disease; useful for genetic and drug screens but anatomically distant from the human optic nerve.
- **C. elegans:** eat-3 loss causes fragmented mitochondria, abnormal cristae, oxidative-stress sensitivity, progressive movement/neural defects, and altered mitophagy; valuable for pathway interrogation, not direct visual-phenotype modeling. (dotto2021dominantopticatrophy pages 5-6)
- **Yeast:** MGM1, the OPA1 ortholog, is useful for functional classification of variants and mtDNA-instability assays but cannot model neuronal selectivity.

The strongest cross-model conclusion is that mitochondrial fragmentation and respiratory/visual dysfunction precede overt RGC loss, identifying mitochondrial maintenance as an upstream therapeutic target. Translation remains uncertain because most models represent haploinsufficiency or complete knockout rather than the compound severe-plus-hypomorphic genotype typical of Behr syndrome.

## Recent developments and expert assessment

The most consequential 2023–2024 developments were improved broad genomic diagnosis for complex hereditary optic neuropathies, increasing use of RNA/functional assays for splice variants, maturation of patient-specific iPSC systems, and entry of an OPA1-directed oligonucleotide into a 2024 first-in-human dominant-optic-atrophy trial. A 2024 expert review nevertheless concluded that treatment studies remain nascent and that present management is largely supportive. The same review emphasizes that compound-heterozygous OPA1 variants cause the early optic-neuropathy, spinocerebellar, peripheral-neuropathy, pyramidal, and developmental phenotype recognized as Behr-related syndrome. DOI https://doi.org/10.3390/jcto2030006, published June 2024. (lee2024hereditaryopticneuropathies pages 5-7)

A useful exact abstract statement from the 2025 model study is: **“mitochondrial disruption and visual impairment precede degeneration of RGCs.”** This supports intervention before irreversible ganglion-cell loss but does not establish clinical efficacy. (strachan2025novelinvivo pages 1-2)

A second key exact summary from the modern clinical literature is that Behr syndrome is characterized by **“childhood-onset optic atrophy combined with ataxia and pyramidal signs including spasticity, weakness, and hyperreflexia.”** (ojaimi2022mitochondrialfissionand pages 7-8)

## Ontology-ready summary

The following artifact provides compact annotations and curation caveats.

| Domain | Evidence-backed finding | Suggested ontology terms/IDs | Evidence caveat |
|---|---|---|---|
| Disease identity | Behr syndrome is a rare Mendelian syndromic optic neuropathy; Open Targets maps it to **MONDO:0008858** and associates it primarily with **OPA1** (OpenTargets Search: Behr syndrome) | MONDO:0008858; OMIM:210000; MeSH/Orphanet/ICD IDs **curator verification needed** | MONDO/OPA1 support is strong, but external identifier crosswalks beyond MONDO/OMIM should be curator-checked |
| Nosology / synonymy | Current literature supports **OPA1-related Behr syndrome / Behr-related syndrome** for biallelic OPA1 disease; this should be **distinguished from OPA3-related Costeff syndrome**, which is a differential diagnosis rather than a true synonym (weisschuh2021mutationspectrumof pages 17-18, lee2024hereditaryopticneuropathies pages 5-7) | Synonym candidate: “OPA1-related Behr syndrome”; Differential diagnosis: OPA3-related Costeff syndrome **(ontology ID curator verification needed)** | Historical literature used “Behr syndrome” broadly; modern molecular classification separates OPA1- from OPA3-related disease |
| Etiology / gene | The principal evidence-backed causal gene is **OPA1** (OPA1 mitochondrial dynamin like GTPase) (OpenTargets Search: Behr syndrome, ojaimi2022mitochondrialfissionand pages 7-8) | HGNC:8156 **curator verification needed**; OPA1 | Evidence in retrieved contexts centers on OPA1; other historical “Behr-like” phenocopies are not excluded globally |
| Inheritance | Reported disease mechanism is **biallelic germline OPA1 pathogenic variants**, consistent with **autosomal recessive** inheritance in classic OPA1-related Behr syndrome (ojaimi2022mitochondrialfissionand pages 7-8, nottia2021mitochondrialdynamicsmolecular pages 8-10, lee2024hereditaryopticneuropathies pages 5-7) | Inheritance: autosomal recessive; Variant origin: germline | Some OPA1 disorders are dominant DOA/DOA+; inheritance must be tied specifically to the Behr syndrome subset |
| Core phenotype | Childhood/early-onset **optic atrophy** is the core presentation (ojaimi2022mitochondrialfissionand pages 7-8, nottia2021mitochondrialdynamicsmolecular pages 8-10) | HPO: HP:0000648 optic atrophy | Frequency not well quantified in retrieved contexts |
| Core phenotype | **Spasticity / pyramidal signs / hyperreflexia** are characteristic neurologic features (ojaimi2022mitochondrialfissionand pages 7-8) | HPO: HP:0001257 spasticity; pyramidal signs **curator verification for exact HPO term** | Literature often groups pyramidal signs broadly; exact HPO mapping may need refinement |
| Core phenotype | **Ataxia / spinocerebellar degeneration** is a recurring major feature (ojaimi2022mitochondrialfissionand pages 7-8, nottia2021mitochondrialdynamicsmolecular pages 8-10, lee2024hereditaryopticneuropathies pages 5-7) | HPO: HP:0001251 ataxia | Cerebellar signs may include dysmetria/dysdiadochokinesis/nystagmus not fully decomposed here |
| Core phenotype | **Peripheral neuropathy** is repeatedly described (nottia2021mitochondrialdynamicsmolecular pages 8-10, lee2024hereditaryopticneuropathies pages 5-7) | HPO: HP:0009830 peripheral neuropathy | Subtype (axonal/sensory-motor) may vary and is not consistently specified in the retrieved contexts |
| Core phenotype | **Developmental delay** / delayed motor development can occur, especially in severe early-onset cases (ojaimi2022mitochondrialfissionand pages 7-8, nottia2021mitochondrialdynamicsmolecular pages 8-10, lee2024hereditaryopticneuropathies pages 5-7) | HPO: HP:0001263 developmental delay | Severity and domain specificity are variably reported |
| Associated phenotype | **Hearing impairment** / sensorineural deafness may occur (ojaimi2022mitochondrialfissionand pages 7-8, nottia2021mitochondrialdynamicsmolecular pages 8-10, lee2024hereditaryopticneuropathies pages 5-7) | HPO: HP:0000365 hearing impairment | Common in broader OPA1 syndromic disease, not necessarily present in all Behr syndrome cases |
| Associated phenotype | **Dysarthria** is reported among neurologic manifestations (ojaimi2022mitochondrialfissionand pages 7-8) | HPO: HP:0001260 dysarthria | Limited frequency data in retrieved contexts |
| Associated phenotype | **Dysphagia** and other gastrointestinal dysmotility features are described (ojaimi2022mitochondrialfissionand pages 7-8, nottia2021mitochondrialdynamicsmolecular pages 8-10) | HPO: HP:0002015 dysphagia | GI findings may be underreported and are not universal |
| Associated phenotype | **Pes cavus** and contractures can occur (ojaimi2022mitochondrialfissionand pages 7-8) | HPO: HP:0001761 pes cavus | Musculoskeletal findings may overlap with neuropathy-related foot deformity |
| Imaging phenotype | Brain MRI may show **cerebellar atrophy**, including vermian atrophy (ojaimi2022mitochondrialfissionand pages 7-8, nottia2021mitochondrialdynamicsmolecular pages 8-10) | HPO: HP:0001272 cerebellar atrophy | Exact HPO for vermian atrophy may be more specific; curator refinement may help |
| Anatomy / tissue | Major affected ocular cell type is the **retinal ganglion cell**; degeneration of RGCs underlies optic neuropathy (strachan2025novelinvivo pages 1-2, alavi2013dominantopticatrophy pages 1-3, fogazza2018biochemicalcharacterizationand pages 35-38) | CL:0000704 retinal ganglion cell **curator verification needed**; UBERON retina/retinal ganglion cell layer **curator verification needed** | Cell ontology ID should be verified before ingestion |
| Anatomy / organ | The **optic nerve** is a primary affected structure; optic nerve/chiasm atrophy is reported (ojaimi2022mitochondrialfissionand pages 7-8, alavi2013dominantopticatrophy pages 1-3) | UBERON optic nerve **curator verification needed** | Chiasmal involvement may merit separate anatomical annotation |
| Anatomy / organ | The **cerebellum** is a major CNS site involved clinically and on MRI (ojaimi2022mitochondrialfissionand pages 7-8) | UBERON cerebellum **curator verification needed** | Vermis-specific annotation may be preferable when supported |
| Anatomy / system | **Corticospinal/pyramidal system** involvement is inferred from spasticity and hyperreflexia (ojaimi2022mitochondrialfissionand pages 7-8) | UBERON corticospinal tract / pyramidal tract **curator verification needed** | Structure-level assignment is phenotype-inferred rather than directly demonstrated in retrieved contexts |
| Anatomy / system | **Peripheral nerve** involvement is supported by neuropathy and contractures (nottia2021mitochondrialdynamicsmolecular pages 8-10, ojaimi2022mitochondrialfissionand pages 7-8) | UBERON peripheral nerve **curator verification needed** | Specific nerves/cell subclasses were not defined in retrieved contexts |
| Molecular location | OPA1 is localized to the **mitochondrial inner membrane** (strachan2025novelinvivo pages 1-2, dotto2021dominantopticatrophy pages 10-11, alavi2013dominantopticatrophy pages 1-3) | GO:0005743 mitochondrial inner membrane | Strongly supported for OPA1 biology, but not unique to Behr syndrome |
| Biological process | A central upstream defect is impaired **mitochondrial inner membrane fusion** due to OPA1 dysfunction (strachan2025novelinvivo pages 1-2, alavi2013dominantopticatrophy pages 1-3) | GO:0007342 mitochondrial inner membrane fusion | GO label/ID should be curator-verified in pipeline if strict ontology versioning is required |
| Cellular component | Abnormal **mitochondrial cristae** organization is repeatedly implicated (strachan2025novelinvivo pages 1-2, dotto2021dominantopticatrophy pages 10-11, fogazza2018biochemicalcharacterizationand pages 35-38) | GO: mitochondrial crista **ID curator verification needed** | Exact GO ID not supplied in retrieved contexts |
| Biological process | Downstream consequences include impaired **oxidative phosphorylation / respiratory function** (strachan2025novelinvivo pages 1-2, dotto2021dominantopticatrophy pages 5-6) | GO: oxidative phosphorylation **ID curator verification needed** | Evidence is strong mechanistically but often derived from broader OPA1/AOA models rather than Behr-only cohorts |
| Biological process | OPA1 dysfunction is linked to defective **mtDNA maintenance / depletion** in severe disease (nottia2021mitochondrialdynamicsmolecular pages 8-10, alavi2013dominantopticatrophy pages 1-3) | GO: mitochondrial DNA maintenance **ID curator verification needed** | mtDNA depletion may be more prominent in severe or specific molecular contexts |
| Biological process | OPA1 participates in regulation of **apoptosis**, including cytochrome c release/cristae remodeling pathways (dotto2021dominantopticatrophy pages 10-11, alavi2013dominantopticatrophy pages 1-3, fogazza2018biochemicalcharacterizationand pages 35-38) | GO: apoptosis **ID curator verification needed** | Much mechanistic evidence comes from OPA1 biology and model systems, not exclusively human Behr tissue |
| Biological process | Increased **mitophagy / autophagy** is a recurrent downstream mechanism in OPA1-deficient models (dotto2021dominantopticatrophy pages 5-6, fogazza2018biochemicalcharacterizationand pages 35-38) | GO: mitophagy **ID curator verification needed** | Model-system evidence stronger than direct human Behr syndrome tissue evidence |
| Diagnostics | Recommended workup in suspected hereditary optic neuropathy includes **next-generation sequencing**, with broader exome/genome testing for complex phenotypes; OPA1 diagnosis is established by identifying pathogenic variants (lee2024hereditaryopticneuropathies pages 5-7, ojaimi2022mitochondrialfissionand pages 7-8) | MAXO: genetic testing **curator verification needed**; assay types: targeted panel / WES / WGS | Diagnostic strategy derives from hereditary optic neuropathy practice, not a Behr-specific guideline |
| Diagnostics | Ophthalmic and functional measures used in OPA1 trials include **BCVA/ETDRS**, visual fields/perimetry, color vision, contrast sensitivity, mfVEP, RNFL and GCL thickness by OCT (NCT06970106 chunk 2, NCT06461286 chunk 1, NCT06461286 chunk 2) | MAXO: ophthalmologic examination; optical coherence tomography; visual field testing; visual evoked potentials **all curator verification needed** | Trial measures are from dominant OPA1 studies but remain relevant for phenotyping syndromic OPA1 disease |
| Management | No approved curative therapy is established; management is largely **supportive** (lee2024hereditaryopticneuropathies pages 5-7) | MAXO: supportive care; rehabilitation; low-vision services **curator verification needed** | Statement reflects broader OPA1/DOA literature, not a dedicated Behr syndrome management guideline |
| Management | Practical supportive interventions may include **multidisciplinary rehabilitation** for gait/spasticity/neuropathy, speech therapy for dysarthria, swallowing support for dysphagia, audiology/hearing aids, and genetic counseling (ojaimi2022mitochondrialfissionand pages 7-8, lee2024hereditaryopticneuropathies pages 5-7) | MAXO: physical therapy; occupational therapy; speech therapy; dysphagia management; hearing aid provision; genetic counseling **all curator verification needed** | These are evidence-informed generic interventions rather than trial-proven Behr-specific therapies |
| Recent development | 2024–2025 OPA1 interventional trials test **PYC-001**, an intravitreal peptide-phosphorodiamidate morpholino oligonucleotide, in **OPA1 haploinsufficiency-associated autosomal dominant optic atrophy**, not specifically Behr syndrome (NCT06970106 chunk 1, NCT06970106 chunk 2, NCT06461286 chunk 1, NCT06461286 chunk 2) | Clinical trials: NCT06461286; NCT06970106 | Important to avoid overgeneralizing these dominant OPA1 trial data to recessive OPA1 Behr syndrome |
| Differential diagnosis | Differential genetic diagnoses for optic atrophy-plus phenotypes include **OPA3**, **WFS1**, **MFN2**, **SPG7**, **AFG3L2**, **ACO2**, and others (weisschuh2021mutationspectrumof pages 17-18, lee2024hereditaryopticneuropathies pages 5-7) | Disease/gene ontology entries **curator verification needed** | Differential list is not exhaustive and depends on presenting phenotype |
| Evidence source | Most information here is **aggregated disease-level literature/review evidence**, supplemented by Open Targets disease-gene association and OPA1 trial registry records, rather than EHR-derived patient aggregation (OpenTargets Search: Behr syndrome, lee2024hereditaryopticneuropathies pages 5-7) | Evidence categories: review, genetic association, clinical trial registry | Primary case-level extraction would still be needed for precise variant-phenotype curation |


*Table: This compact table summarizes ontology-ready facts for OPA1-related Behr syndrome, including identifiers, inheritance, phenotypes, anatomy, mechanisms, diagnostics, and supportive management. It also flags areas needing curator verification and clearly separates Behr syndrome from OPA3/Costeff syndrome.*

## Evidence limitations

Behr syndrome has no large registry-quality natural-history cohort, prevalence study, controlled treatment trial, validated quality-of-life instrument, or standardized diagnostic/management guideline. Numerical data from dominant optic atrophy must not be imported as Behr-specific statistics. Likewise, evidence from OPA1 haploinsufficiency models and trials is mechanistically relevant but not automatically applicable to biallelic systemic disease. Variant-level curation should return to primary case reports and ClinVar/gnomAD records before database ingestion.

References

1. (OpenTargets Search: Behr syndrome): Open Targets Query (Behr syndrome, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (NCT06970106 chunk 1):  Safety of Single and Repeat Dose of PYC-001 Eye Injections in People With Autosomal Dominant Optic Atrophy (Myrtle). PYC Therapeutics. 2025. ClinicalTrials.gov Identifier: NCT06970106

3. (NCT06970106 chunk 2):  Safety of Single and Repeat Dose of PYC-001 Eye Injections in People With Autosomal Dominant Optic Atrophy (Myrtle). PYC Therapeutics. 2025. ClinicalTrials.gov Identifier: NCT06970106

4. (NCT06461286 chunk 1):  SAD of IVT PYC-001 in OPA1 Mutation-Associated Autosomal Dominant Optic Atrophy (Sundew). PYC Therapeutics. 2024. ClinicalTrials.gov Identifier: NCT06461286

5. (NCT06461286 chunk 2):  SAD of IVT PYC-001 in OPA1 Mutation-Associated Autosomal Dominant Optic Atrophy (Sundew). PYC Therapeutics. 2024. ClinicalTrials.gov Identifier: NCT06461286

6. (ojaimi2022mitochondrialfissionand pages 7-8): Mode Al Ojaimi, Azza Salah, and Ayman El-Hattab. Mitochondrial fission and fusion: molecular mechanisms, biological functions, and related disorders. Membranes, 12:893, Sep 2022. URL: https://doi.org/10.3390/membranes12090893, doi:10.3390/membranes12090893. This article has 167 citations.

7. (weisschuh2021mutationspectrumof pages 17-18): Nicole Weisschuh, Simone Schimpf-Linzenbold, Pascale Mazzola, Sinja Kieninger, Ting Xiao, Ulrich Kellner, Teresa Neuhann, Carina Kelbsch, Felix Tonagel, Helmut Wilhelm, Susanne Kohl, and Bernd Wissinger. Mutation spectrum of the opa1 gene in a large cohort of patients with suspected dominant optic atrophy: identification and classification of 48 novel variants. PLoS ONE, 16:e0253987, Jul 2021. URL: https://doi.org/10.1371/journal.pone.0253987, doi:10.1371/journal.pone.0253987. This article has 37 citations and is from a peer-reviewed journal.

8. (nottia2021mitochondrialdynamicsmolecular pages 8-10): Michela Di Nottia, Daniela Verrigni, Alessandra Torraco, Teresa Rizza, Enrico Bertini, and Rosalba Carrozzo. Mitochondrial dynamics: molecular mechanisms, related primary mitochondrial disorders and therapeutic approaches. Genes, 12:247, Feb 2021. URL: https://doi.org/10.3390/genes12020247, doi:10.3390/genes12020247. This article has 57 citations.

9. (lee2024hereditaryopticneuropathies pages 5-7): Samuel K. Lee, Caroline Mura, Nicolas J. Abreu, Janet C. Rucker, Steven L. Galetta, Laura J. Balcer, and Scott N. Grossman. Hereditary optic neuropathies: an updated review. Journal of Clinical &amp; Translational Ophthalmology, 2:64-78, Jun 2024. URL: https://doi.org/10.3390/jcto2030006, doi:10.3390/jcto2030006. This article has 5 citations.

10. (dotto2021dominantopticatrophy pages 5-6): Valentina Del Dotto and Valerio Carelli. Dominant optic atrophy (doa): modeling the kaleidoscopic roles of opa1 in mitochondrial homeostasis. Frontiers in Neurology, Jun 2021. URL: https://doi.org/10.3389/fneur.2021.681326, doi:10.3389/fneur.2021.681326. This article has 23 citations and is from a peer-reviewed journal.

11. (strachan2025novelinvivo pages 1-2): Elin L. Strachan, Eugene T. Dillon, Mairéad Sullivan, Jeffrey C. Glennon, Amandine Peyrel, Jérôme Sarniguet, Kevin Dubois, Benjamin Delprat, Breandán N. Kennedy, and Niamh C. O'Sullivan. Novel in vivo models of autosomal optic atrophy reveal conserved pathological changes in neuronal mitochondrial structure and function. The FASEB Journal, Apr 2025. URL: https://doi.org/10.1096/fj.202403271r, doi:10.1096/fj.202403271r. This article has 1 citations.

12. (dotto2021dominantopticatrophy pages 10-11): Valentina Del Dotto and Valerio Carelli. Dominant optic atrophy (doa): modeling the kaleidoscopic roles of opa1 in mitochondrial homeostasis. Frontiers in Neurology, Jun 2021. URL: https://doi.org/10.3389/fneur.2021.681326, doi:10.3389/fneur.2021.681326. This article has 23 citations and is from a peer-reviewed journal.

13. (alavi2013dominantopticatrophy pages 1-3): Marcel V Alavi and Nico Fuhrmann. Dominant optic atrophy, opa1, and mitochondrial quality control: understanding mitochondrial network dynamics. Molecular Neurodegeneration, 8:32, Sep 2013. URL: https://doi.org/10.1186/1750-1326-8-32, doi:10.1186/1750-1326-8-32. This article has 178 citations and is from a highest quality peer-reviewed journal.

14. (fogazza2018biochemicalcharacterizationand pages 35-38): Mario Fogazza. Biochemical characterization and validation of a novel cellmodel for dominant optic atrophy. ArXiv, Apr 2018. URL: https://doi.org/10.6092/unibo/amsdottorato/8630, doi:10.6092/unibo/amsdottorato/8630. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Behr_Syndrome-deep-research-falcon_artifacts/artifact-00.md)