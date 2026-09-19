---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T01:22:52.750320'
end_time: '2026-07-31T01:32:24.507734'
duration_seconds: 571.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Shashi X-Linked Intellectual Disability Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Shashi_X-Linked_Intellectual_Disability_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Shashi X-Linked Intellectual Disability Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Shashi X-Linked Intellectual Disability Syndrome** covering all of the
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
- **Disease Name:** Shashi X-Linked Intellectual Disability Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Shashi X-Linked Intellectual Disability Syndrome** covering all of the
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


# Shashi X-Linked Intellectual Disability Syndrome

## Executive summary

Shashi X-linked intellectual disability syndrome (Shashi-XLID) is an ultra-rare Mendelian neurodevelopmental disorder associated with a hemizygous, 23-base-pair coding deletion in **RBMX**, which encodes the nuclear RNA-binding protein hnRNP G. The defining family contained seven affected males. The historical clinical phenotype comprises intellectual disability, short stature, obesity, and hypogonadism, but patient-level frequencies, standardized developmental assessments, longitudinal outcomes, and population prevalence have not been published adequately in the retrievable literature. Open Targets maps the disorder to **MONDO:0010277** and links it to RBMX using evidence citing PMIDs **10677307** and **25256757**. (OpenTargets Search: Shashi X-linked intellectual disability syndrome, cai2021deletionofrbmx pages 1-4)

The strongest disease-specific mechanistic evidence comes from a 2021 human isogenic iPSC study. The RBMX deletion removes the C-terminal RGG/RG motif, disrupting PRMT5-dependent arginine methylation, RBMX–SRSF1 complex formation, and MDM4 exon-6 splicing. Reduced MDM4 protein releases p53 activity, increases apoptosis, and impairs glutamatergic neuronal differentiation. No disease-modifying treatment, validated biomarker, natural-history registry, or Shashi-specific clinical trial was identified. (cai2021deletionofrbmx pages 1-4, cai2021deletionofrbmx pages 9-11)

A central caveat is nomenclature: **Shashi-XLID is not Shashi–Pena syndrome**, an unrelated ASXL2 disorder, and should not be conflated with **Gustavson syndrome**, another RBMX-associated XLID caused by a different in-frame deletion and apparently distinct domain-specific mechanism. (johansson2024gustavsonsyndromeis pages 7-8)

## 1. Disease information

### Definition and identifiers

- **Preferred name:** syndromic X-linked intellectual disability, Shashi type.
- **Synonyms:** Shashi syndrome; Shashi-XLID; Shashi X-linked intellectual disability syndrome; Shashi X-linked mental retardation syndrome; MRXSS.
- **MONDO:** **MONDO:0010277**.
- **Causal gene:** **RBMX**, RNA binding motif protein X-linked; Ensembl **ENSG00000147274**.
- **Foundational literature:** original clinical report, PMID **10677307**; genetic association report, PMID **25256757**; mechanistic study, Cai et al., published **13 July 2021**, DOI [10.1016/j.celrep.2021.109337](https://doi.org/10.1016/j.celrep.2021.109337).
- **OMIM/Orphanet:** an exact disease-entry number was not securely recoverable from the available evidence and should be verified directly before database ingestion.
- **ICD-10/ICD-11 and MeSH:** no syndrome-specific code or descriptor was identified. Coding would ordinarily use broader intellectual-disability, developmental-disorder, obesity, short-stature, or hypogonadism categories as clinically appropriate. (OpenTargets Search: Shashi X-linked intellectual disability syndrome, cai2021deletionofrbmx pages 15-16, cai2021deletionofrbmx pages 1-4)

The knowledge base is derived principally from an individual pedigree and experimental disease models, subsequently summarized in aggregated disease resources. It is not based on EHR-scale cohorts, claims databases, surveillance registries, or population studies. The initial pedigree comprised **seven affected males**. (cai2021deletionofrbmx pages 1-4)

### Key abstract quotation

Cai et al. state: “Transcriptomic analysis of isogenic Shashi-XLID human-induced pluripotent stem cells (hiPSCs) generated using CRISPR-Cas9 reveals a dysregulation of MDM4 splicing and aberrant p53 upregulation.” They conclude that their findings suggest “the loss of function of the RBMX RGG/RG motif is the cause of Shashi-XLID syndrome.” (cai2021deletionofrbmx pages 1-4)

## 2. Etiology

### Causal and genetic risk factors

The established cause is a germline X-chromosomal RBMX lesion. The reported **23-bp deletion lies in the last coding exon**, causes a frameshift and predicted premature termination codon, and removes the terminal **38 amino acids**, including the C-terminal RGG/RG motif. It is therefore best interpreted mechanistically as a domain-specific partial loss-of-function allele rather than assuming complete absence of RBMX. The precise HGVS expression was not available in the retrieved full text and should be copied from the original variant report or ClinVar rather than reconstructed. (cai2021deletionofrbmx pages 4-6, cai2021deletionofrbmx pages 1-4)

The disorder follows X-linked inheritance: hemizygous males are expected to be at greatest risk, while the phenotype in heterozygous females may depend on X-chromosome inactivation. However, penetrance, carrier manifestations, X-inactivation measurements, germline-mosaicism risk, and recurrence estimates specific to this family were not available in the retrieved evidence.

No susceptibility loci, confirmed modifier genes, founder allele, anticipation, or consanguinity effect has been established. **RBMXL1**, a functional RBMX retrocopy, is a plausible biological modifier because it shares RNA/protein partners and can compensate experimentally for RBMX deficiency, but this has not been clinically validated for the original Shashi family. Later mouse and cellular work found that RBMXL1 can rescue RBMX-dependent neurogenesis and splicing defects. (tilliole2025rbmxfunctionalretrocopy pages 11-14, tilliole2025rbmxfunctionalretrocopy pages 8-11)

### Environmental, infectious, lifestyle, and protective factors

No toxin, infection, diet, activity pattern, substance exposure, parental age effect, or other environmental factor is known to cause Shashi-XLID. Smoking, alcohol, occupational exposure, pollution, and infectious agents are not etiologic categories for this monogenic syndrome. No genetic or environmental protective factor has been demonstrated clinically. Supportive developmental environments may improve function but do not prevent inheritance of the causal allele.

A disease-specific gene–environment interaction has not been reported. General prenatal or postnatal insults could modify neurodevelopment independently, but that proposition should not be entered as a Shashi-specific association.

## 3. Phenotypes

The human clinical evidence is too small and incompletely quantified to support reliable prevalence percentages. The original phenotype is generally summarized as intellectual disability, short stature, obesity, and hypogonadism. Accordingly, frequency labels should be recorded as **reported/characteristic, exact frequency unknown**, rather than “frequent” or “obligate.” (OpenTargets Search: Shashi X-linked intellectual disability syndrome, cai2021deletionofrbmx pages 1-4)

| Phenotype | Type and likely timing | Severity/course | Suggested HPO term | Evidence limitation |
|---|---|---|---|---|
| Intellectual disability/developmental impairment | Neurodevelopmental symptom; childhood onset | Lifelong; severity insufficiently quantified for the original family | **HP:0001249** Intellectual disability; consider HP:0012758 Neurodevelopmental delay | Defining feature, but standardized scores unavailable |
| Short stature | Growth sign emerging in childhood | Degree and progression unknown | **HP:0004322** Short stature | Frequency and endocrine work-up unavailable |
| Obesity | Metabolic/physical manifestation | Timing and trajectory unknown | **HP:0001513** Obesity | No BMI distribution, hyperphagia, or metabolic data found |
| Hypogonadism | Endocrine/reproductive sign, often apparent around puberty | Type and severity unknown | **HP:0000135** Hypogonadism | No hormonal, fertility, or genital measurements found |

The primary quality-of-life burden is expected to arise from cognitive/developmental disability, educational dependence, communication limitations, and possible endocrine or metabolic complications. No EQ-5D, SF-36, PROMIS, caregiver-burden, adaptive-behavior, or disease-specific quality-of-life study exists in the retrieved evidence.

Microcephaly, corpus-callosum abnormalities, seizures, progressive spasticity, arthrogryposis, eye anomalies, and early mortality occur in the wider spectrum of recently described RBMX-related disorders, but should **not automatically be assigned to classic Shashi syndrome**. These features were prominent in other RBMX genotypes and particularly in Gustavson syndrome or later expanded cohorts. (tilliole2025rbmxfunctionalretrocopy pages 11-14, johansson2024gustavsonsyndromeis pages 7-8, tilliole2025rbmxfunctionalretrocopy pages 14-17)

## 4. Genetic and molecular information

### Gene and protein

**RBMX** encodes hnRNP G, a predominantly nuclear RNA-binding and splicing-regulatory protein. Its N-terminal RNA-recognition motif binds RNA, while low-complexity C-terminal regions mediate interactions and higher-order assemblies. RBMX participates in pre-mRNA splicing, maintenance of genome stability, DNA-damage responses, and repression of cryptic splice sites. The Shashi deletion specifically removes the C-terminal RGG/RG region. (cai2021deletionofrbmx pages 1-4, tilliole2025rbmxfunctionalretrocopy pages 1-4)

### Variant interpretation

- **Gene:** RBMX.
- **Origin:** germline, inherited in an X-linked pedigree.
- **Class:** 23-bp deletion; frameshift with premature stop; C-terminal truncation.
- **Functional consequence:** loss of the last 38 amino acids and RGG/RG motif; defective arginine methylation-dependent splicing complex formation.
- **Clinical classification:** the family segregation and functional evidence strongly support pathogenicity, but the exact current ClinVar assertion and ACMG evidence codes should be confirmed against the live record before ingestion.
- **Population frequency:** not reported in the retrieved evidence. Because the disorder is ultra-rare and the allele segregated with a severe X-linked phenotype, absence or extreme rarity in population databases is expected but should not be asserted without a current gnomAD query.
- **Somatic status:** not a somatic cancer mutation in this disease.

RBMX’s C-terminal residues R369 and R373 were identified as methylated in cells, and the minimal PRMT5-methylated region was mapped to residues 366–391. This directly overlaps the region removed by the Shashi-associated truncation. (cai2021deletionofrbmx pages 4-6)

### Epigenetics and chromosomal abnormalities

The relevant regulatory event is **post-translational arginine methylation**, not a proven syndrome-specific DNA-methylation episignature. No Shashi-specific blood DNA methylation signature, histone profile, chromatin-accessibility assay, or epigenomic diagnostic test has been validated.

The causal lesion is a small coding deletion rather than an aneuploidy, translocation, inversion, or large copy-number variant. No recurrent gross chromosomal abnormality is established.

## 5. Environmental information

Environmental toxicants, radiation, pollution, lifestyle behavior, and infectious agents have no established causal role. There is no zoonotic, contagious, inflammatory-trigger, or exposure-mediated component. Environmental surveillance and infectious-disease prevention are therefore not disease-specific interventions, although ordinary preventive health care remains important.

## 6. Mechanism and pathophysiology

### Disease-specific causal chain

1. **Upstream genetic lesion:** the terminal RBMX deletion removes its C-terminal RGG/RG motif.
2. **Post-translational defect:** the deleted region normally contains PRMT5-methylated arginines, notably R369 and R373.
3. **Nuclear-complex defect:** methylated RBMX normally assembles with the splicing factor SRSF1 in higher-order nuclear structures. Deletion of the motif or PRMT5 depletion disrupts these assemblies.
4. **Splicing defect:** SRSF1 association with MDM4 pre-mRNA decreases, promoting MDM4 exon-6 exclusion and lowering full-length MDM4 protein.
5. **Signaling defect:** MDM4 ordinarily restrains p53. Reduced MDM4 therefore causes inappropriate p53 stabilization and activation.
6. **Cellular outcome:** p53 targets such as CDKN1A, BBC3, BAX, and other cell-cycle/apoptosis genes rise, producing excessive apoptosis and altered neurodevelopmental transcription.
7. **Tissue outcome:** neural progenitors and differentiating cortical neurons exhibit abnormal morphology, altered splicing, and markedly impaired maturation into VGLUT1-positive glutamatergic neurons.
8. **Clinical outcome:** disrupted cortical neurogenesis provides a biologically coherent explanation for developmental impairment and intellectual disability. (cai2021deletionofrbmx pages 4-6, cai2021deletionofrbmx pages 9-11, cai2021deletionofrbmx pages 1-4)

Quantitatively, nuclear p53-positive cells rose from **8.67% in control iPSCs to 19.74% and 19.93%** in two edited RBMX-DRGG lines. Cleaved-caspase-3-positive area increased from **2.9%** to **4.8% and 6.06%**. RNA sequencing identified **847 upregulated and 1,067 downregulated genes** in mutant iPSCs at an absolute fold-change threshold above 1.5. (cai2021deletionofrbmx pages 4-6)

In NPCs, more than 90% of cells expressed SOX1, SOX2, or PAX6 after induction, demonstrating that early NPC specification remained possible. Nevertheless, mutant NPCs had **258 downregulated genes, 15 upregulated genes, and 111 significant alternative-splicing changes**. Downregulated neurodevelopmental genes included FOXG1, TBR1, EMX1, and SLC17A7. After cortical differentiation, only approximately **3%** of mutant neurons were VGLUT1-positive versus **15%** of controls; the GABAergic fraction was not significantly different. (cai2021deletionofrbmx pages 9-11)

Physical disruption of nuclear assemblies reduced RBMX-foci size by **43.8%**, intensity by **62.48%**, RBMX–SRSF1 colocalization by **25%**, and SRSF1 association with MDM4 RNA by **50%**. These experiments support a mechanistic role for methylation-regulated higher-order assembly, although the exact biophysical classification of these puncta in vivo remains an active question. (cai2021deletionofrbmx pages 9-11)

### Other RBMX biology and recent research

A 2024 eLife study showed that RBMX-family proteins repress cryptic splice sites within unusually long exons, particularly in genome-stability genes. This broadens the mechanistic framework but is not direct proof that ultra-long-exon missplicing causes classic Shashi syndrome. DOI [10.7554/eLife.89705](https://doi.org/10.7554/eLife.89705), published May 2024.

A 2024 review emphasized that hnRNP proteins, although widely expressed, are increasingly implicated in intellectual disability, epilepsy, microcephaly, ALS, and dementia because of their crucial CNS functions. DOI [10.3389/fnmol.2024.1411639](https://doi.org/10.3389/fnmol.2024.1411639), published July 2024. These sources support authoritative expert consensus that tissue-selective neurodevelopmental vulnerability can arise from ubiquitous RNA-processing proteins.

A 2025 preprint—outside the requested 2023–2024 priority window and not yet equivalent to peer-reviewed evidence—proposed domain-dependent loss- and gain-of-function mechanisms across nine RBMX-associated families and showed functional compensation by RBMXL1. It also implicated abnormal ATRX exitron splicing. These findings are important emerging evidence but should not overwrite the established Shashi-specific PRMT5–MDM4–p53 mechanism until peer reviewed. (tilliole2025rbmxfunctionalretrocopy pages 11-14, tilliole2025rbmxfunctionalretrocopy pages 14-17, tilliole2025rbmxfunctionalretrocopy pages 1-4)

### Suggested GO and CL annotations

- **GO biological process:** mRNA splicing via spliceosome (**GO:0000398**); regulation of mRNA splicing (**GO:0048024**); neuron differentiation (**GO:0030182**); CNS development (**GO:0007417**); forebrain development (**GO:0030900**); apoptotic process (**GO:0006915**); intrinsic apoptotic signaling by p53 (**GO:0072332**); protein arginine methylation (**GO:0018216**).
- **GO molecular function:** RNA binding (**GO:0003723**).
- **GO cellular component:** nucleus (**GO:0005634**); nuclear speck (**GO:0016607**), with the caveat that RBMX puncta were experimentally described as membraneless nuclear structures.
- **Cell Ontology:** neural progenitor cell (**CL:0011115**); glutamatergic neuron (**CL:0000679**); cortical neuron, where a locally validated exact descendant term should be selected.

No disease-specific metabolomics, lipidomics, proteomics biomarker, spatial-transcriptomic atlas, or clinical single-cell dataset was found. Transcriptomics and splicing analysis are the principal available molecular profiles.

## 7. Anatomical structures affected

The primary system is the **central nervous system**, especially developing forebrain/cerebral cortex. Experimental effects occur in neural progenitors and differentiating cortical glutamatergic neurons. Suggested anatomy terms are brain (**UBERON:0000955**), cerebral cortex (**UBERON:0000956**), forebrain, and central nervous system. At the subcellular level, the nucleus and splicing-associated nuclear puncta are implicated. (cai2021deletionofrbmx pages 9-11, cai2021deletionofrbmx pages 1-4)

Secondary endocrine/metabolic involvement is suggested clinically by short stature, obesity, and hypogonadism, but specific hypothalamic, pituitary, gonadal, adipose, or skeletal pathology has not been demonstrated. No lateralization is expected or reported.

## 8. Temporal development

The syndrome is congenital in genetic origin and developmental in expression. Intellectual/developmental manifestations would ordinarily become evident in infancy or childhood, while short stature and obesity may evolve during growth and hypogonadism may become clearer around puberty. Exact onset ages are unavailable.

The course is presumed chronic and lifelong rather than episodic or relapsing. No formal disease stages, remission pattern, progression rate, or critical therapeutic window has been defined. Mechanistically, prenatal and early postnatal corticogenesis are plausible periods of greatest vulnerability because RBMX dysfunction alters NPC differentiation and cortical-neuron maturation, but this inference has not been tested clinically.

## 9. Inheritance and population

Shashi-XLID is X-linked and was delineated in a family with seven affected males. Hemizygous males are therefore the principal recognized affected group. Female penetrance, skewed X-inactivation, carrier phenotype, male-to-female ratio in an independent cohort, and age distribution cannot be calculated. (cai2021deletionofrbmx pages 1-4)

No prevalence, incidence, carrier frequency, founder effect, ethnic enrichment, or geographic distribution has been established. It should be represented as **ultra-rare; prevalence unknown**, not assigned a numerical rate. Genetic anticipation is not expected for a small deletion and has not been reported. Germline mosaicism remains a general counseling possibility but has not been documented specifically.

## 10. Diagnostics

### Clinical recognition and testing strategy

The phenotype is not sufficiently specific for diagnosis without molecular confirmation. Evaluation should include developmental history and examination, growth trajectory, BMI, pubertal/genital assessment, and a three-generation pedigree emphasizing affected males and maternal-line transmission.

A reasonable genetic workflow is:

1. **Neurodevelopmental/XLID multigene panel or WES**, ensuring adequate RBMX coverage and indel calling.
2. **Trio or family segregation testing** whenever possible.
3. **WGS** when exome/panel testing is negative but suspicion remains, particularly to detect noncoding or structural lesions.
4. **RBMX single-gene sequencing** for targeted familial testing or a highly suggestive pedigree.
5. **Deletion/duplication analysis or CMA** if a larger X-chromosome copy-number lesion is suspected; conventional CMA may not detect a 23-bp deletion.
6. **Sanger confirmation** of a candidate small indel and testing of at-risk relatives.

Karyotyping and FISH are low-yield for a small coding deletion. Mitochondrial sequencing and repeat-expansion assays are not disease-specific tests. RNA sequencing could demonstrate abnormal splicing in research settings, but no validated clinical MDM4-splicing assay exists. There is no diagnostic blood protein, metabolite, imaging, EEG, biopsy, or epigenetic biomarker. (cai2021deletionofrbmx pages 4-6, cai2021deletionofrbmx pages 1-4)

### Differential diagnosis

- Other monogenic syndromic XLID conditions.
- Prader–Willi and other syndromic-obesity disorders when obesity and hypogonadism dominate.
- Endocrine causes of short stature/hypogonadism.
- **Gustavson syndrome**, caused by RBMX c.484_486del, p.(Pro162del), which has profound ID, brain abnormalities, epilepsy, sensory deficits, and early death and is mechanistically distinct.
- Other recently recognized RBMX-related neurodevelopmental disorders.
- **Shashi–Pena syndrome (ASXL2)** must be excluded as a nomenclaturally similar but genetically unrelated condition. (johansson2024gustavsonsyndromeis pages 7-8)

No newborn or population screening program exists. Cascade testing is appropriate after a molecular diagnosis.

## 11. Outcome and prognosis

No survival curve, life-expectancy estimate, disease-specific mortality rate, hospitalization rate, or validated prognostic biomarker is available. Classic Shashi syndrome should not be assigned the early mortality reported in Gustavson syndrome. (johansson2024gustavsonsyndromeis pages 7-8)

Long-term morbidity likely centers on intellectual/developmental disability and possible growth, weight, and reproductive-endocrine complications. Recovery of the underlying neurodevelopmental disorder is not expected, although developmental skills and adaptive function may improve with individualized intervention. Neither genotype–phenotype predictors nor treatment-response predictors are validated.

## 12. Treatment

There is no approved disease-modifying pharmacotherapy, gene therapy, RNA therapy, cell therapy, or genotype-specific drug. No relevant Shashi-specific interventional clinical trial was identified.

Current care should be individualized and supportive:

- developmental and neuropsychological assessment;
- early-intervention services and special education;
- speech/language, occupational, and physical therapy as indicated;
- behavioral and communication support;
- nutritional and weight-management services;
- pediatric endocrinology for growth, pubertal development, and hypogonadism;
- symptom-directed seizure, sleep, gastrointestinal, orthopedic, or psychiatric treatment if such problems occur in an individual;
- social-work and caregiver support.

Suggested MAXO mappings include molecular genetic testing, genetic counseling, developmental assessment, speech therapy, occupational therapy, physical therapy, nutritional management, and endocrine evaluation; exact MAXO identifiers should be validated against the current ontology release.

The PRMT5 inhibitor EPZ015666 reproduced mutant phenotypes—p53 activation, apoptosis, and reduced FOXG1/TBR1—in control neuronal cultures. It is therefore a **mechanistic probe and potential hazard, not a proposed treatment**. Conversely, suppressing p53 or correcting MDM4 splicing may be experimentally testable rescue strategies, but neither has clinical efficacy or safety evidence in Shashi syndrome. (cai2021deletionofrbmx pages 9-11)

## 13. Prevention

Primary prevention by lifestyle modification, vaccine, or medication is not applicable to the inherited molecular lesion. Relevant reproductive options after identifying the familial variant include genetic counseling, carrier testing, prenatal diagnosis, and preimplantation genetic testing where legally and ethically available.

Secondary prevention consists of early molecular diagnosis and prompt developmental/endocrine assessment. Tertiary prevention includes therapies and surveillance intended to limit disability, obesity-related complications, contractures, communication barriers, and psychosocial burden. There is no disease-specific immunization, chemoprophylaxis, or public-health environmental intervention.

## 14. Other species and natural disease

No naturally occurring veterinary counterpart, breed predisposition, animal-to-human transmission, or zoonotic potential was identified. RBMX orthologs are evolutionarily conserved across vertebrates, supporting comparative developmental studies but not establishing naturally occurring animal disease.

Experimental depletion of RBMX orthologs impairs brain and somite development in zebrafish and neural/muscle development in *Xenopus laevis*. RBMX knockdown in rat hippocampal neurons reduces dendritic-spine density. These are induced functional models rather than spontaneous Shashi syndrome. (cai2021deletionofrbmx pages 15-16, cai2021deletionofrbmx pages 1-4, tilliole2025rbmxfunctionalretrocopy pages 1-4)

## 15. Model organisms and experimental systems

### Human cellular disease model

The strongest model uses CRISPR-Cas9-engineered male human iPSCs with C-terminal RBMX truncations designed to recapitulate the Shashi deletion. These cells were differentiated into SOX1/SOX2/PAX6-positive NPCs and cortical neurons. The system reproduces MDM4 missplicing, p53 activation, excessive apoptosis, altered neurodevelopmental transcription, and impaired glutamatergic maturation. Its principal limitation is that the edited lines were isogenic models rather than multiple independent patient-derived lines; they also cannot model whole-organism endocrine manifestations or long-term cognition. (cai2021deletionofrbmx pages 4-6, cai2021deletionofrbmx pages 9-11, cai2021deletionofrbmx pages 1-4)

### Vertebrate models

- **Zebrafish:** rbmx depletion causes brain, eye, muscle, and somite developmental abnormalities; useful for embryonic development and rescue studies, but not shown to reproduce the human metabolic/endocrine syndrome.
- **Xenopus:** Rbmx is necessary for neural and muscle development.
- **Rat primary hippocampal neurons:** knockdown reduces dendritic-spine density, providing a synaptic model.
- **Mouse:** later Rbmx-knockout work found only mild neuroanatomical changes—approximately **9.3% lower total brain area** and **15.1% smaller corpus-callosum genu**—probably because mouse Rbmxl1 retrocopies compensate. Combined Rbmx/Rbmxl1 knockdown increased abnormal cortical-cell delamination by **38–44%**, and human RBMX or RBMXL1 rescued the phenotype. This work is valuable but was reported in a 2025 preprint and is not classic Shashi-allele knock-in evidence. (tilliole2025rbmxfunctionalretrocopy pages 11-14, tilliole2025rbmxfunctionalretrocopy pages 8-11, tilliole2025rbmxfunctionalretrocopy pages 49-52, tilliole2025rbmxfunctionalretrocopy pages 1-4)

No validated Shashi-specific organoid, conditional knock-in, adult behavioral, or therapeutic-rescue model was identified.

## Evidence-and-ontology summary

| domain | disease-specific finding | quantitative evidence / frequency | suggested ontology terms | evidence level and source date |
|---|---|---|---|---|
| Nosology | Syndromic X-linked intellectual disability, Shashi type; causal gene RBMX | MONDO MONDO:0010277; disease-target association to RBMX supported by literature and ClinVar-linked evidence | MONDO:0010277; Gene: RBMX | Curated disease ontology and genetics evidence; Open Targets context citing PMIDs 10677307 and 25256757; accessed in current tool session (OpenTargets Search: Shashi X-linked intellectual disability syndrome) |
| Disease definition | RBMX-associated X-linked intellectual disability syndrome originally described in a pedigree with affected males | Original pedigree reported 7 affected males; aggregated disease-level knowledge remains sparse | MONDO:0010277; HPO: Intellectual disability HP:0001249 | Human clinical genetics and pedigree-level evidence; 2015 genetic association summarized in 2021 Cell Reports intro (cai2021deletionofrbmx pages 1-4) |
| Inheritance | X-linked inheritance | Male-limited affected pedigree; exact penetrance not reported | MONDO:0010277; inheritance ontology not specified here | Human pedigree evidence; original family summarized 2021 (cai2021deletionofrbmx pages 1-4) |
| Core phenotype | Intellectual disability is the defining clinical feature | Frequency in original pedigree not fully enumerated in retrieved text; syndrome-level feature established | HPO: HP:0001249 | Human clinical and pedigree evidence; 2000 and 2015 source lineage via curated association and 2021 summary (OpenTargets Search: Shashi X-linked intellectual disability syndrome, cai2021deletionofrbmx pages 1-4) |
| Core phenotype | Short stature reported in original syndrome descriptions | Frequency not reported in retrieved evidence | HPO: Short stature HP:0004322 | Human clinical report lineage; evidence indirect in retrieved corpus and sparsely quantified (OpenTargets Search: Shashi X-linked intellectual disability syndrome) |
| Core phenotype | Obesity reported in original syndrome descriptions | Frequency not reported in retrieved evidence | HPO: Obesity HP:0001513 | Human clinical report lineage; evidence indirect in retrieved corpus and sparsely quantified (OpenTargets Search: Shashi X-linked intellectual disability syndrome) |
| Core phenotype | Hypogonadism or genital phenotype reported in original syndrome descriptions | Frequency not reported in retrieved evidence | HPO: Hypogonadism HP:0000135; genital abnormality term uncertain or not specified from retrieved text | Human clinical report lineage; evidence indirect in retrieved corpus and sparsely quantified (OpenTargets Search: Shashi X-linked intellectual disability syndrome) |
| Molecular lesion | 23-bp deletion in the last exon of RBMX predicted to cause frameshift and premature stop, deleting the C-terminal RGG or RG motif | Size 23 bp; truncates last 38 aa encompassing RGG or RG motif | Gene: RBMX; GO: RNA binding GO:0003723; protein region: C-terminal RGG or RG motif | Human genetic evidence and disease-model recapitulation; 2021 peer-reviewed mechanistic study summarizing 2015 family variant (cai2021deletionofrbmx pages 4-6, cai2021deletionofrbmx pages 1-4) |
| Protein and mechanism | RBMX C-terminal RGG or RG motif is methylated by PRMT5 | In vivo methylated arginines identified at R369 and R373; minimal PRMT5-methylated region aa 366-391 | GO: protein arginine methylation GO:0018216; GO: mRNA splicing via spliceosome GO:0000398 | In vitro and cellular mechanistic evidence; 2021 (cai2021deletionofrbmx pages 4-6) |
| Mechanism | PRMT5-RBMX methylation promotes RBMX-SRSF1 higher-order complexes that support MDM4 exon 6 inclusion | 1,6-hexanediol reduced RBMX foci size by 43.8 percent, intensity by 62.48 percent, RBMX-SRSF1 colocalization by 25 percent, and SRSF1 binding to MDM4 RNA by 50 percent | GO: regulation of mRNA splicing GO:0048024; GO: nuclear speck GO:0016607; CL: neural progenitor cell CL:0011115 | Cellular mechanistic evidence in U2OS and neuronal systems; 2021 (cai2021deletionofrbmx pages 9-11) |
| Mechanism | Loss of RBMX RGG or RG function causes MDM4 missplicing, reduced MDM4 protein, p53 pathway activation, and apoptosis | In patient-modeled iPSCs, nuclear p53-positive cells: 8.67 percent control vs 19.74 percent DRGG1 vs 19.93 percent DRGG2; cleaved caspase-3 area: 2.9 percent control vs 4.8 percent DRGG1 vs 6.06 percent DRGG2 | GO: apoptotic process GO:0006915; GO: regulation of transcription by p53 class mediator GO:1901796; GO: alternative mRNA splicing via spliceosome GO:0000380 | Human iPSC disease model; 2021 (cai2021deletionofrbmx pages 4-6, cai2021deletionofrbmx pages 1-4) |
| Transcriptomics | Shashi-XLID iPSCs show broad transcriptional dysregulation with p53 signature enrichment | 847 upregulated and 1067 downregulated genes in DRGG1 iPSCs with fold change threshold greater than 1.5 | GO: intrinsic apoptotic signaling pathway by p53 class mediator GO:0072332; GO: neuron differentiation GO:0030182 | Human CRISPR-engineered iPSC model; 2021 (cai2021deletionofrbmx pages 4-6) |
| NPC phenotype | Neural progenitor cells differentiate efficiently but show developmental transcriptional defects | NPC induction efficiency greater than 90 percent SOX1 positive, SOX2 positive, and PAX6 positive; 258 downregulated and 15 upregulated genes in DRGG1 NPCs; 111 significant splicing events in DRGG NPCs | CL: neural progenitor cell CL:0011115; GO: central nervous system development GO:0007417; GO: neuron differentiation GO:0030182 | Human iPSC-derived NPC model; 2021 (cai2021deletionofrbmx pages 9-11) |
| Neuronal phenotype | Impaired glutamatergic neurogenesis in cortical-neuron differentiation | 3 percent VGLUT1 positive neurons in RBMX-DRGG cultures vs 15 percent in controls; GABAergic difference not significant in reported experiment | GO: glutamatergic synaptic transmission GO:0035249; CL: glutamatergic neuron CL:0000679; UBERON: cerebral cortex UBERON:0000956; HPO neurodevelopmental term broad or unspecified | Human iPSC-derived cortical neuron model; 2021 (cai2021deletionofrbmx pages 9-11) |
| Additional neuronal readouts | Neurogenesis regulators are reduced and apoptosis rises after neuronal differentiation | Downregulated FOXG1, TBR1, and SLC17A7; increased CDKN1A and BAX in 14-day neurons; increased cleaved caspase-3 or 7 activity | GO: forebrain development GO:0030900; GO: neuron fate commitment GO:0048663; CL: cortical neuron term uncertain or not specified | Human iPSC-derived neuronal model; 2021 (cai2021deletionofrbmx pages 9-11) |
| Affected anatomy | Primary system is central nervous system and cerebral cortex; subcellular involvement includes nucleus and splicing-related compartments | Quantitative anatomy not available for Shashi patients in retrieved evidence | UBERON: brain UBERON:0000955; UBERON: cerebral cortex UBERON:0000956; GO cellular component nucleus GO:0005634; GO cellular component nuclear speck GO:0016607 | Mechanistic and model-based inference anchored to disease models; 2021 (cai2021deletionofrbmx pages 9-11, cai2021deletionofrbmx pages 1-4) |
| Comparative RBMX disorders | Gustavson syndrome is also RBMX-related but clinically more severe and mechanistically distinct, so it should not be conflated with Shashi syndrome | Comparative statement only; not a Shashi frequency estimate | Differential diagnosis note; MONDO term not specified here | Human comparative genetics; 2024 peer-reviewed study (johansson2024gustavsonsyndromeis pages 7-8) |
| Diagnostics | Most direct diagnostic approach is molecular testing of RBMX, especially sequencing methods capable of detecting small coding deletions; phenotype alone is insufficiently specific | No validated biomarker beyond genetic diagnosis found; no disease-specific biochemical assay found | MAXO: genetic testing term uncertain or not specified; HPO-guided neurodevelopmental gene panel or exome sequencing concept | Clinical genetics practice inference from causal variant architecture and mechanistic confirmation (OpenTargets Search: Shashi X-linked intellectual disability syndrome, cai2021deletionofrbmx pages 1-4) |
| Genetic testing modalities | Single-gene RBMX analysis, XLID or neurodevelopmental gene panels, WES, and WGS are reasonable; CMA and karyotype may miss small exon-level indels unless rearrangement is suspected | No performance statistics reported for Shashi specifically in retrieved evidence | MAXO: molecular genetic testing term uncertain or not specified | Evidence-informed inference based on lesion type and published disease-model recapitulation; no disease-specific guideline located (cai2021deletionofrbmx pages 4-6, cai2021deletionofrbmx pages 1-4) |
| Treatment and management | No disease-specific molecular therapy established; management is supportive and multidisciplinary | No disease-specific response-rate data found | MAXO: supportive care term uncertain or not specified; speech therapy, occupational therapy, and physical therapy terms uncertain or not specified | Evidence gap plus standard rare neurodevelopmental care inference; no relevant disease-specific trials found in tool search (OpenTargets Search: Shashi X-linked intellectual disability syndrome) |
| Prevention and counseling | Genetic counseling, cascade testing in families, and reproductive counseling are relevant because of X-linked inheritance | No carrier-frequency or founder-effect data found | MAXO: genetic counseling term uncertain or not specified | Human genetics implication from pedigree structure; disease-specific epidemiology sparse (OpenTargets Search: Shashi X-linked intellectual disability syndrome, cai2021deletionofrbmx pages 1-4) |
| Clinical trials | No Shashi syndrome-specific interventional trials identified | 0 relevant disease-specific trials found in current search | MAXO not applicable | Clinical trials search in current session; no relevant registered study returned (OpenTargets Search: Shashi X-linked intellectual disability syndrome) |
| Epidemiology | Ultra-rare Mendelian disorder with evidence based on a small number of reported families and patients | Prevalence, incidence, sex ratio beyond X-linked expectation, and life expectancy not reported in retrieved evidence | MONDO:0010277 | Evidence gap; current knowledge largely from individual patients, pedigrees, and disease-level curation (OpenTargets Search: Shashi X-linked intellectual disability syndrome, cai2021deletionofrbmx pages 1-4) |


*Table: This table compacts the key disease-specific evidence and ontology suggestions for RBMX-related Shashi X-linked intellectual disability syndrome. It highlights what is directly supported by available evidence, where quantitative model data exist, and where frequencies or ontology IDs remain uncertain.*

## Major evidence gaps and curation recommendations

1. Verify the exact OMIM/Orphanet entries and syndrome-specific HGVS nomenclature directly from live primary databases.
2. Do not calculate phenotype frequencies from the seven-male family unless patient-level tables are recovered.
3. Record prevalence, incidence, penetrance, female expressivity, life expectancy, and carrier frequency as unknown.
4. Keep classic Shashi syndrome separate from Shashi–Pena syndrome, Gustavson syndrome, and the broader emerging RBMX-related neurodevelopmental spectrum.
5. Mark mechanistic evidence as primarily human **in vitro** disease-model evidence; mark zebrafish, Xenopus, rat, and mouse observations separately.
6. Treat RBMXL1 compensation and ATRX-splicing mechanisms as emerging later evidence, not yet a replacement for the peer-reviewed Shashi-specific MDM4–p53 model.
7. Do not present PRMT5 inhibition as therapy: experimentally, it phenocopies the disease-associated defect. (cai2021deletionofrbmx pages 9-11, johansson2024gustavsonsyndromeis pages 7-8, tilliole2025rbmxfunctionalretrocopy pages 11-14)

Overall, current understanding supports Shashi-XLID as an RBMX domain-specific spliceopathy in which disruption of methylation-dependent RNA-processing complexes activates p53 during neuronal differentiation. Clinical knowledge remains substantially less mature than molecular knowledge, making natural-history collection, standardized phenotyping, female-carrier assessment, and variant-resolved functional studies the highest priorities.

References

1. (OpenTargets Search: Shashi X-linked intellectual disability syndrome): Open Targets Query (Shashi X-linked intellectual disability syndrome, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (cai2021deletionofrbmx pages 1-4): Ting Cai, Jessica K. Cinkornpumin, Zhenbao Yu, Oscar D. Villarreal, William A. Pastor, and Stéphane Richard. Deletion of rbmx rgg/rg motif in shashi-xlid syndrome leads to aberrant p53 activation and neuronal differentiation defects. Cell reports, 36 2:109337, Jul 2021. URL: https://doi.org/10.1016/j.celrep.2021.109337, doi:10.1016/j.celrep.2021.109337. This article has 42 citations and is from a highest quality peer-reviewed journal.

3. (cai2021deletionofrbmx pages 9-11): Ting Cai, Jessica K. Cinkornpumin, Zhenbao Yu, Oscar D. Villarreal, William A. Pastor, and Stéphane Richard. Deletion of rbmx rgg/rg motif in shashi-xlid syndrome leads to aberrant p53 activation and neuronal differentiation defects. Cell reports, 36 2:109337, Jul 2021. URL: https://doi.org/10.1016/j.celrep.2021.109337, doi:10.1016/j.celrep.2021.109337. This article has 42 citations and is from a highest quality peer-reviewed journal.

4. (johansson2024gustavsonsyndromeis pages 7-8): Josefin Johansson, Sarah Lidéus, Carina Frykholm, Cecilia Gunnarsson, Filip Mihalic, Sanna Gudmundsson, Sara Ekvall, Anna-Maja Molin, Mai Pham, Mauno Vihinen, Kristina Lagerstedt-Robinson, Ann Nordgren, Per Jemth, Adam Ameur, Göran Annerén, Maria Wilbe, and Marie-Louise Bondeson. Gustavson syndrome is caused by an in-frame deletion in rbmx associated with potentially disturbed sh3 domain interactions. European Journal of Human Genetics, 32:333-341, Jun 2024. URL: https://doi.org/10.1038/s41431-023-01392-y, doi:10.1038/s41431-023-01392-y. This article has 17 citations and is from a domain leading peer-reviewed journal.

5. (cai2021deletionofrbmx pages 15-16): Ting Cai, Jessica K. Cinkornpumin, Zhenbao Yu, Oscar D. Villarreal, William A. Pastor, and Stéphane Richard. Deletion of rbmx rgg/rg motif in shashi-xlid syndrome leads to aberrant p53 activation and neuronal differentiation defects. Cell reports, 36 2:109337, Jul 2021. URL: https://doi.org/10.1016/j.celrep.2021.109337, doi:10.1016/j.celrep.2021.109337. This article has 42 citations and is from a highest quality peer-reviewed journal.

6. (cai2021deletionofrbmx pages 4-6): Ting Cai, Jessica K. Cinkornpumin, Zhenbao Yu, Oscar D. Villarreal, William A. Pastor, and Stéphane Richard. Deletion of rbmx rgg/rg motif in shashi-xlid syndrome leads to aberrant p53 activation and neuronal differentiation defects. Cell reports, 36 2:109337, Jul 2021. URL: https://doi.org/10.1016/j.celrep.2021.109337, doi:10.1016/j.celrep.2021.109337. This article has 42 citations and is from a highest quality peer-reviewed journal.

7. (tilliole2025rbmxfunctionalretrocopy pages 11-14): Pierre Tilliole, Carolin Mattausch, Peggy Tilly, Elsa Leitão, Lucile Boutaud, Daphné Lehalle, Isabelle An, Emanuela Argilli, Sharon Aufox, Bert Callewaert, Perrine Charles, Jessica K. Cinkornpumin, Thomas Courtin, Marco Dalla Vecchia, Erica E. Davis, Boyan Ivanov Dimitrov, William Dobyns, Ekaterina Epifanova, Erwan Grandgirard, Matthieu Jung, Sarah Jurgensmeyer Langas, Sabine Kaya, Boris Keren, Tahir N. Khan, Elodie Lejeune, Mingfeng Li, Yannick Marie, Bastien Morlet, Caroline Nava, William A. Pastor, Damien Plassard, Carlos E. Prada, Agnès Rastetter, Noémie Schwaller, Nenad Sestan, Elliott Sherr, Suzanna L. Temple, Jude-Felix Tenywa, Sylvia Tielens, Arie van Haeringen, Helen Whitley, Laurent Nguyen, Laura Steenpaß, Muriel Rhinn, Stephan C. Collins, Delphine Héron, Valerie Cormier-Daire, Tania Attie-Bitach, Binnaz Yalcin, Christel Depienne, and Juliette D. Godin. Rbmx functional retrocopy safeguards brain development. MedRxiv, Oct 2025. URL: https://doi.org/10.1101/2025.10.17.25337589, doi:10.1101/2025.10.17.25337589. This article has 1 citations.

8. (tilliole2025rbmxfunctionalretrocopy pages 8-11): Pierre Tilliole, Carolin Mattausch, Peggy Tilly, Elsa Leitão, Lucile Boutaud, Daphné Lehalle, Isabelle An, Emanuela Argilli, Sharon Aufox, Bert Callewaert, Perrine Charles, Jessica K. Cinkornpumin, Thomas Courtin, Marco Dalla Vecchia, Erica E. Davis, Boyan Ivanov Dimitrov, William Dobyns, Ekaterina Epifanova, Erwan Grandgirard, Matthieu Jung, Sarah Jurgensmeyer Langas, Sabine Kaya, Boris Keren, Tahir N. Khan, Elodie Lejeune, Mingfeng Li, Yannick Marie, Bastien Morlet, Caroline Nava, William A. Pastor, Damien Plassard, Carlos E. Prada, Agnès Rastetter, Noémie Schwaller, Nenad Sestan, Elliott Sherr, Suzanna L. Temple, Jude-Felix Tenywa, Sylvia Tielens, Arie van Haeringen, Helen Whitley, Laurent Nguyen, Laura Steenpaß, Muriel Rhinn, Stephan C. Collins, Delphine Héron, Valerie Cormier-Daire, Tania Attie-Bitach, Binnaz Yalcin, Christel Depienne, and Juliette D. Godin. Rbmx functional retrocopy safeguards brain development. MedRxiv, Oct 2025. URL: https://doi.org/10.1101/2025.10.17.25337589, doi:10.1101/2025.10.17.25337589. This article has 1 citations.

9. (tilliole2025rbmxfunctionalretrocopy pages 14-17): Pierre Tilliole, Carolin Mattausch, Peggy Tilly, Elsa Leitão, Lucile Boutaud, Daphné Lehalle, Isabelle An, Emanuela Argilli, Sharon Aufox, Bert Callewaert, Perrine Charles, Jessica K. Cinkornpumin, Thomas Courtin, Marco Dalla Vecchia, Erica E. Davis, Boyan Ivanov Dimitrov, William Dobyns, Ekaterina Epifanova, Erwan Grandgirard, Matthieu Jung, Sarah Jurgensmeyer Langas, Sabine Kaya, Boris Keren, Tahir N. Khan, Elodie Lejeune, Mingfeng Li, Yannick Marie, Bastien Morlet, Caroline Nava, William A. Pastor, Damien Plassard, Carlos E. Prada, Agnès Rastetter, Noémie Schwaller, Nenad Sestan, Elliott Sherr, Suzanna L. Temple, Jude-Felix Tenywa, Sylvia Tielens, Arie van Haeringen, Helen Whitley, Laurent Nguyen, Laura Steenpaß, Muriel Rhinn, Stephan C. Collins, Delphine Héron, Valerie Cormier-Daire, Tania Attie-Bitach, Binnaz Yalcin, Christel Depienne, and Juliette D. Godin. Rbmx functional retrocopy safeguards brain development. MedRxiv, Oct 2025. URL: https://doi.org/10.1101/2025.10.17.25337589, doi:10.1101/2025.10.17.25337589. This article has 1 citations.

10. (tilliole2025rbmxfunctionalretrocopy pages 1-4): Pierre Tilliole, Carolin Mattausch, Peggy Tilly, Elsa Leitão, Lucile Boutaud, Daphné Lehalle, Isabelle An, Emanuela Argilli, Sharon Aufox, Bert Callewaert, Perrine Charles, Jessica K. Cinkornpumin, Thomas Courtin, Marco Dalla Vecchia, Erica E. Davis, Boyan Ivanov Dimitrov, William Dobyns, Ekaterina Epifanova, Erwan Grandgirard, Matthieu Jung, Sarah Jurgensmeyer Langas, Sabine Kaya, Boris Keren, Tahir N. Khan, Elodie Lejeune, Mingfeng Li, Yannick Marie, Bastien Morlet, Caroline Nava, William A. Pastor, Damien Plassard, Carlos E. Prada, Agnès Rastetter, Noémie Schwaller, Nenad Sestan, Elliott Sherr, Suzanna L. Temple, Jude-Felix Tenywa, Sylvia Tielens, Arie van Haeringen, Helen Whitley, Laurent Nguyen, Laura Steenpaß, Muriel Rhinn, Stephan C. Collins, Delphine Héron, Valerie Cormier-Daire, Tania Attie-Bitach, Binnaz Yalcin, Christel Depienne, and Juliette D. Godin. Rbmx functional retrocopy safeguards brain development. MedRxiv, Oct 2025. URL: https://doi.org/10.1101/2025.10.17.25337589, doi:10.1101/2025.10.17.25337589. This article has 1 citations.

11. (tilliole2025rbmxfunctionalretrocopy pages 49-52): Pierre Tilliole, Carolin Mattausch, Peggy Tilly, Elsa Leitão, Lucile Boutaud, Daphné Lehalle, Isabelle An, Emanuela Argilli, Sharon Aufox, Bert Callewaert, Perrine Charles, Jessica K. Cinkornpumin, Thomas Courtin, Marco Dalla Vecchia, Erica E. Davis, Boyan Ivanov Dimitrov, William Dobyns, Ekaterina Epifanova, Erwan Grandgirard, Matthieu Jung, Sarah Jurgensmeyer Langas, Sabine Kaya, Boris Keren, Tahir N. Khan, Elodie Lejeune, Mingfeng Li, Yannick Marie, Bastien Morlet, Caroline Nava, William A. Pastor, Damien Plassard, Carlos E. Prada, Agnès Rastetter, Noémie Schwaller, Nenad Sestan, Elliott Sherr, Suzanna L. Temple, Jude-Felix Tenywa, Sylvia Tielens, Arie van Haeringen, Helen Whitley, Laurent Nguyen, Laura Steenpaß, Muriel Rhinn, Stephan C. Collins, Delphine Héron, Valerie Cormier-Daire, Tania Attie-Bitach, Binnaz Yalcin, Christel Depienne, and Juliette D. Godin. Rbmx functional retrocopy safeguards brain development. MedRxiv, Oct 2025. URL: https://doi.org/10.1101/2025.10.17.25337589, doi:10.1101/2025.10.17.25337589. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Shashi_X-Linked_Intellectual_Disability_Syndrome-deep-research-falcon_artifacts/artifact-00.md)