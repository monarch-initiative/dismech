---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-22T11:11:12.665946'
end_time: '2026-06-22T11:24:42.262239'
duration_seconds: 809.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Uterine Leiomyoma
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 46
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Uterine_Leiomyoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Uterine_Leiomyoma-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Uterine_Leiomyoma-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Uterine Leiomyoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Uterine Leiomyoma** covering all of the
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
- **Disease Name:** Uterine Leiomyoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Uterine Leiomyoma** covering all of the
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


# COMPREHENSIVE RESEARCH REPORT ON UTERINE LEIOMYOMA

## Disease Characteristics Knowledge Base Entry

---

## 1. DISEASE INFORMATION

### Overview and Definition

Uterine leiomyomas (also known as uterine fibroids or myomas) are the most common benign gynecological tumors affecting women of reproductive age (alali2023theetiopathogenesisof pages 1-2, bulun2025uterinefibroids pages 1-5). These tumors originate from the myometrial smooth muscle cells of the uterus and are characterized by monoclonal proliferation, excessive accumulation of extracellular matrix (ECM), and hormone-dependent growth (bulun2025uterinefibroids pages 1-5, ishikawa2023risingstarsrole pages 1-3). The lifetime prevalence reaches 30–70% in the general population, with incidence rates as high as 70–80% by menopause (alali2023theetiopathogenesisof pages 1-2, koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2, larrain2024newinsightsinto pages 1-3). Black women experience disproportionately higher rates, with prevalence exceeding 80% by age 50 compared to approximately 70% in White women (buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2).

### Key Identifiers

While specific OMIM numbers and comprehensive ontology identifiers were not fully detailed in the retrieved recent literature, uterine fibroids are classified using ICD-10 codes D25-D26.9 and D28.2 (zhang2025globalregionaland pages 1-2). The International Federation of Gynecology and Obstetrics (FIGO) classification system stratifies fibroids based on anatomical location into types 0–8 and hybrid categories (micic2024currentlyavailabletreatment pages 1-2).

### Common Synonyms

- Uterine leiomyomas
- Uterine fibroids  
- Myomas
- Leiomyomas

### Data Source

The information is derived from aggregated disease-level resources including recent systematic reviews, epidemiological studies using Global Burden of Disease (GBD) data, molecular profiling studies, and large-scale genome-wide association studies (GWAS) published between 2023 and 2026 (alali2023theetiopathogenesisof pages 1-2, bulun2025uterinefibroids pages 1-5, tang2025theglobalburden pages 1-2, zhang2025globalregionaland pages 1-2, buyukcelebi2024integratingleiomyomagenetics pages 1-2).

---

## 2. ETIOLOGY

### Disease Causal Factors

#### Genetic Factors

Uterine leiomyomas have complex genetic architecture combining somatic driver mutations and heritable susceptibility:

**Somatic Mutations (Tumor-Intrinsic):**
- **MED12 mutations** (exon 2) are the most common somatic driver, present in 50–80% of fibroids (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, ishikawa2023risingstarsrole pages 1-3). These heterozygous, gain-of-function mutations disrupt the CDK8 kinase module of the Mediator complex, affecting chromatin landscape, enhancer engagement, genomic stability, and responsiveness to progesterone (bulun2025uterinefibroids pages 1-5, ishikawa2023risingstarsrole pages 1-3).

- **HMGA2/HMGA1 overexpression and rearrangements** occur in approximately 10% of fibroids, defining a distinct molecular subtype with characteristic histopathologic features (bulun2025uterinefibroids pages 1-5, dundr2022uterinecellularleiomyomas pages 1-2).

- **FH (Fumarate Hydratase) deficiency** characterizes FH-deficient leiomyomas and is associated with hereditary leiomyomatosis and renal cell cancer (HLRCC) syndrome (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, boos2025therolesof pages 1-2).

- **COL4A5/COL4A6 deletions**, **SRCAP complex mutations** (causing H2A.Z deposition defects), and **chromosome 1p deletions** represent additional recurrent molecular subtypes (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2, dundr2022uterinecellularleiomyomas pages 1-2).

A detailed summary of genetic alterations is provided in the genetic mutations table below.

| Gene Name / Alteration | Mutation Type | Frequency / Prevalence | Molecular Effects | Clinical Associations | Key References |
|---|---|---:|---|---|---|
| **MED12** | Recurrent **somatic** exon 2 point mutations; typically heterozygous, gain-of-function–like driver alterations disrupting Mediator kinase module signaling | ~50–80% of uterine fibroids; ~70% in several recent summaries; 77% in a large review | Disrupts MED12-dependent activation of **CDK8/CDK19** within the Mediator complex; associated with altered chromatin landscape, enhancer engagement, genomic instability, progesterone responsiveness, and dysregulated **WNT/β-catenin**, hedgehog, sex steroid, and **TGF-β** signaling; transcriptomic enrichment for ECM/collagen pathways | Most common driver; often multiple tumors rather than solitary lesions; commonly seen even in small tumors; more frequent in Black women in some series; mutant tumors can differ in size/location and may show mutation-status–dependent response to GnRH agonists and ulipristal acetate | (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, ishikawa2023risingstarsrole pages 1-3) |
| **HMGA2 / HMGA1** | **Somatic** overexpression and chromosomal rearrangements/fusions involving HMGA2/1 | ~10% of fibroids in recent overview; in cellular leiomyoma, HMGA2 overexpression was 36.5% and rearrangement 13.2% | Alters chromatin architecture and transcriptional programs; defines a molecular subtype distinct from MED12-mutant tumors | Associated with distinct histopathologic phenotypes; important subtype in usual leiomyoma and especially enriched in some variants such as cellular leiomyoma | (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2, dundr2022uterinecellularleiomyomas pages 1-2) |
| **FH** | **Somatic or germline-related** loss-of-function / deficiency; part of FH-deficient leiomyoma spectrum and HLRCC-related disease | Less common than MED12/HMGA2 in unselected fibroids; recognized recurrent subtype | Fumarate hydratase deficiency rewires metabolism and contributes to a distinct molecular subtype of leiomyoma | Seen in FH-deficient leiomyomas and in hereditary leiomyomatosis and renal cell cancer (HLRCC); clinically relevant for identifying syndromic disease | (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, boos2025therolesof pages 1-2) |
| **COL4A5 / COL4A6** | Recurrent **somatic deletions / structural alterations** affecting collagen IV genes | Recurrent but uncommon relative to MED12; listed among frequently observed genetic alterations | Likely alters basement-membrane / ECM-related biology and contributes to subtype-specific tumor development | Included among recognized uterine fibroid driver alterations; may overlap with syndromic/structural subtypes rather than classic MED12 tumors | (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2, chuang2023differentialexpressionof pages 1-2) |
| **SRCAP complex genes** (e.g., **YEATS4, ZNHIT1**, other complex members) | **Inactivating somatic mutations** causing defective H2A.Z loading / chromatin remodeling abnormalities | Recently identified recurrent but uncommon subtype | Produces **H2A.Z deposition defects** and epigenetic dysregulation; supports a chromatin-based pathogenesis distinct from MED12 and HMGA2 | Emerging molecular class of leiomyoma; potentially useful for future subtype-based diagnostics and therapy development | (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2) |
| **Chromosome 1p deletion** | Recurrent **somatic copy-number loss** | 19.3% in a cellular leiomyoma series | Copy-number loss likely alters dosage of tumor-relevant genes on 1p; appears mutually exclusive with some other driver classes in variant tumors | Particularly reported in **cellular leiomyoma**; useful in variant classification and differential pathology | (dundr2022uterinecellularleiomyomas pages 1-2) |
| **24 GWAS risk loci / heritable susceptibility variants** (multiple genes including **GREB1, MCM8** and broader target-gene sets) | **Germline susceptibility SNPs** / risk loci from population genetics | 24 uterine-fibroid–associated risk loci identified in a 2024 integrative analysis; 394 potential target genes, 168 differentially expressed in tumors | Heritable risk variants map largely to noncoding regulatory regions and influence gene regulation through chromatin contacts, eQTL effects, and cell-type–specific regulatory programs | Explains familial aggregation and racial/population risk differences; points to causal cell types and potential preventive/targeted strategies rather than a single monogenic cause | (buyukcelebi2024integratingleiomyomagenetics pages 1-2) |
| **Non-coding RNA dysregulation linked to driver status** (e.g., miR-21, miR-29, miR-200; H19, MIAT, XIST) | Secondary molecular alterations influenced by driver mutations, race/ethnicity, and hormones rather than classic coding mutations | Commonly dysregulated across fibroids; not a single frequency estimate | Regulates ECM production, proliferation, apoptosis, and inflammation; expression is influenced by **MED12** mutation status and ovarian steroids | Potential biomarker and non-hormonal therapeutic layer; may help explain phenotypic heterogeneity and racial disparities | (boos2025therolesof pages 1-2) |


*Table: This table summarizes the principal genetic and molecular alterations implicated in uterine leiomyoma, emphasizing recurrent somatic drivers, inherited susceptibility loci, and their clinical relevance. It is useful for quickly comparing major subtypes, frequencies, and mechanistic consequences across the current evidence base.*

**Heritable Susceptibility:**
A 2024 integrative GWAS meta-analysis identified 24 uterine fibroid-associated risk loci potentially targeting 394 genes, of which 168 are differentially expressed in fibroid tumors (buyukcelebi2024integratingleiomyomagenetics pages 1-2). This heritable component explains familial aggregation, with first-degree relatives showing 2.5-fold elevated risk and higher concordance in monozygotic versus dizygotic twins (buyukcelebi2024integratingleiomyomagenetics pages 1-2).

#### Hormonal Factors

Estrogen and progesterone are essential for fibroid development and growth (bulun2025uterinefibroids pages 1-5, ishikawa2023risingstarsrole pages 1-3, boos2025therolesof pages 1-2). Fibroids overexpress estrogen and progesterone receptors, and their growth is associated with ovulatory cycles and the first trimester of pregnancy (bulun2025uterinefibroids pages 1-5). Progesterone, via its nuclear receptor PGR, is particularly critical: it activates paracrine WNT signaling and production of growth factors that support fibroid stem cell proliferation (bulun2025uterinefibroids pages 1-5, larrain2024newinsightsinto pages 1-3). Fibroids rarely develop before menarche and often regress after menopause, underscoring steroid hormone dependence (alali2023theetiopathogenesisof pages 1-2, ishikawa2023risingstarsrole pages 1-3).

#### Mechanistic Factors

Uterine leiomyomas arise from clonal expansion of a single mutated myometrial stem cell or transformed myometrial cell acquiring stem-like features (tumor-initiating cell, TIC) (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3). This initial genetic insult (e.g., MED12 mutation) transforms the cell, but additional factors—including hormonal signaling, paracrine interactions with surrounding differentiated cells, and ECM remodeling—are required for tumor progression (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3).

### Risk Factors

A comprehensive summary of risk and protective factors is presented in the table below.

| Factor Type | Specific Factor | Category | Strength of Association | Population-Specific Effects | Key Evidence |
|---|---|---|---|---|---|
| Risk | Advanced reproductive age | Reproductive | Consistently reported risk factor; incidence and symptom burden increase through reproductive years, especially ages 35–50 | Burden concentrated in women aged 40–69 globally; common in reproductive-age women (tang2025theglobalburden pages 1-2, micic2024currentlyavailabletreatment pages 1-2) | Listed as a risk factor in reviews; fibroids are most commonly found in women aged 35–50, and global burden is concentrated in ages 40–69 (koltsova2023aviewon pages 1-2, tang2025theglobalburden pages 1-2, micic2024currentlyavailabletreatment pages 1-2) |
| Risk | Black/African ancestry | Genetic / population | Strong and repeatedly reported association | By age 50, prevalence reaches >80% in Black women vs ~70% overall/White women; disproportionate incidence and severity (buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2, boos2025therolesof pages 1-2) | Reviews and genomic studies report substantially higher prevalence and burden in Black women (buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2, boos2025therolesof pages 1-2) |
| Risk | Latin American ethnicity | Population | Reported association, but less extensively quantified than Black ancestry | Mentioned as increased-risk population in review literature | Identified among risk factors in heterogeneity-focused review (koltsova2023aviewon pages 1-2) |
| Risk | Family history of uterine leiomyoma | Genetic | Moderate-to-strong; familial aggregation repeatedly reported | First-degree relatives have elevated risk; reflects heritable susceptibility | Review identifies family history as a risk factor; GWAS/integrative genetics supports heritable contribution and multiple susceptibility loci (koltsova2023aviewon pages 1-2, buyukcelebi2024integratingleiomyomagenetics pages 1-2) |
| Risk | Germline/heritable susceptibility loci | Genetic | Strong biologic evidence for susceptibility, but effect sizes vary by locus | May contribute to racial/population differences in risk | Integrative 2024 analysis identified 24 UF-associated risk loci and 394 candidate target genes, supporting inherited susceptibility (buyukcelebi2024integratingleiomyomagenetics pages 1-2) |
| Risk | MED12-associated predisposition to specific tumor biology | Genetic / molecular | Strong for tumor subtype biology rather than disease initiation alone | MED12-mutant tumors are more frequent in Black women in some series and often multiple | MED12 mutations are the dominant driver in many tumors and are associated with distinct biology and multiplicity (bulun2025uterinefibroids pages 1-5, ishikawa2023risingstarsrole pages 1-3) |
| Risk | Early menarche | Reproductive | Consistently reported risk factor | No specific population restriction given, but may interact with lifetime hormonal exposure | Included as a risk factor in multiple reviews and diagnostic overview (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Risk | Late menopause | Reproductive | Reported risk factor, likely reflecting prolonged estrogen/progesterone exposure | Not specifically stratified | Included in etiopathogenesis overview figure/discussion (alali2023theetiopathogenesisof pages 1-2) |
| Risk | Nulliparity / low parity | Reproductive | Consistently reported risk factor | Protective effect of multiparity implies higher risk in nulliparous women | Nulliparity or absence of parity is reported as a risk factor; several reviews note multiparity as protective (buyukcelebi2024integratingleiomyomagenetics pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Protective | Multiparity / parity | Reproductive | Consistently reported protective factor | Not population-specific, though effect may vary with reproductive history | Multiparity/parity reported as protective in reviews and diagnostic narrative (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2) |
| Risk | Obesity / high BMI | Lifestyle / metabolic | Strong and consistently reported | Important in many populations; cited in epidemiologic and mechanistic reviews | Obesity repeatedly listed among major risk factors and linked to symptomatic disease burden (alali2023theetiopathogenesisof pages 1-2, koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2, micic2024currentlyavailabletreatment pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Risk | Diabetes | Metabolic | Reported association | Not specifically stratified | Included among factors involved in incidence/development in clinician-friendly review (larrain2024newinsightsinto pages 1-3) |
| Risk | Arterial hypertension | Metabolic / vascular | Repeatedly reported association | Not specifically stratified | Identified as a risk factor in heterogeneity/risk-factor review and clinician review (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Risk | Chronic inflammation | Environmental / biologic | Reported association with plausible mechanistic support | Not specifically stratified | Listed as a risk factor in review of UL genesis; inflammation also emphasized mechanistically in fibroid biology (koltsova2023aviewon pages 1-2, boos2025therolesof pages 1-2) |
| Risk | Sexually transmitted infections | Infectious | Reported association, evidence less mature than hormonal/metabolic factors | Not specifically stratified | Identified as a possible risk factor in review of risk/protective factors (koltsova2023aviewon pages 1-2) |
| Risk | Exposure to xenoestrogens in early ontogenesis | Environmental | Biologically plausible and reported in review literature | Suggests early-life vulnerability window | Reported as a risk factor in review of UL genesis (koltsova2023aviewon pages 1-2) |
| Risk | Diethylstilbestrol (DES) exposure | Environmental | Reported association | Not specifically stratified | Included among environmental contributors in clinician-friendly molecular review (larrain2024newinsightsinto pages 1-3) |
| Risk | Air pollution | Environmental | Reported association | Not specifically stratified | Mentioned among factors potentially involved in incidence/development (larrain2024newinsightsinto pages 1-3) |
| Risk | Alcohol consumption | Lifestyle | Repeatedly reported risk factor | Not specifically stratified | Alcohol listed as a risk factor in heterogeneity review and clinician-friendly review (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Risk | Caffeine | Lifestyle | Reported in one review/figure; likely weaker evidence than alcohol/obesity | Not specifically stratified | Included in etiopathogenesis figure as a potential risk factor (alali2023theetiopathogenesisof pages 1-2) |
| Risk | Chronic stress | Lifestyle / psychosocial | Reported association | Not specifically stratified | Listed in diagnostic review as a risk factor (centini2024tailoringthediagnostic pages 1-2) |
| Risk | Vitamin D deficiency | Environmental / nutritional | Repeatedly reported association with supportive mechanistic rationale | Not specifically stratified; may be relevant in populations with higher deficiency prevalence | Vitamin D deficiency is listed among known factors influencing fibroid development in recent reviews (alali2023theetiopathogenesisof pages 1-2, micic2024currentlyavailabletreatment pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Protective | Adequate vitamin D status | Nutritional | Implied protective factor from repeated deficiency-risk association; preclinical support exists | Not specifically stratified | Since deficiency is repeatedly associated with risk, adequate status is plausibly protective; some model literature supports anti-fibroid effects (micic2024currentlyavailabletreatment pages 1-2, wu2026preclinicalresearchplatform pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Risk | High-fat diet / adverse dietary factors | Lifestyle / nutritional | Reported association | Not specifically stratified | High-fat diet and dietary factors are mentioned as contributing to incidence/development (larrain2024newinsightsinto pages 1-3) |
| Protective | Oral contraceptive use / combined oral contraceptives | Reproductive / hormonal | Reported protective factor in review literature, though literature historically mixed | Not specifically stratified | Oral contraceptive intake and combined oral contraceptives are listed among possible protective factors in recent reviews (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2) |
| Protective | Smoking | Lifestyle | Reported as a possible protective factor in reviews, but likely outweighed by broader health harms | Not population-specific; not a recommended prevention strategy | Smoking is listed among possible protective factors in one recent review even though it is not clinically recommended (koltsova2023aviewon pages 1-2) |
| Risk | Hormonal milieu: higher estradiol and progesterone exposure | Hormonal / mechanistic | Strong mechanistic support | Relevant across reproductive-age populations; explains premenopausal predominance | Risk/severity associated with serum estradiol and progesterone; tumors are steroid-dependent and rarely develop before menarche (buyukcelebi2024integratingleiomyomagenetics pages 1-2, ishikawa2023risingstarsrole pages 1-3) |
| Protective | Postmenopausal state / menopause-associated regression | Reproductive / hormonal | Strong observational pattern | Applies broadly; many fibroids regress after menopause | Fibroids frequently regress after menopause, supporting reduced ovarian steroid exposure as protective against persistence/growth (alali2023theetiopathogenesisof pages 1-2, ishikawa2023risingstarsrole pages 1-3) |
| Risk | Reproductive delay / postponed childbearing | Reproductive | Epidemiologically plausible; discussed in population-burden review | Relevant in regions with delayed childbearing patterns | Population review links changing reproductive patterns, including postponed childbearing, to increasing prevalence (zhang2025globalregionaland pages 1-2) |


*Table: This table summarizes reported risk and protective factors for uterine leiomyoma across recent reviews and epidemiologic/genetic studies. It organizes the factors by category, indicates the qualitative strength of association, and notes population-specific patterns where available.*

**Genetic Risk Factors:**
- Family history of fibroids (koltsova2023aviewon pages 1-2, buyukcelebi2024integratingleiomyomagenetics pages 1-2)
- Black/African ancestry (highest risk and severity) (buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2, boos2025therolesof pages 1-2)
- Latin American ethnicity (koltsova2023aviewon pages 1-2)
- Multiple GWAS-identified susceptibility loci (buyukcelebi2024integratingleiomyomagenetics pages 1-2)

**Environmental and Lifestyle Risk Factors:**
- Early menarche, nulliparity, late menopause (alali2023theetiopathogenesisof pages 1-2, koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2, larrain2024newinsightsinto pages 1-3)
- Obesity and high BMI (alali2023theetiopathogenesisof pages 1-2, koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2, micic2024currentlyavailabletreatment pages 1-2, larrain2024newinsightsinto pages 1-3)
- Diabetes and arterial hypertension (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3)
- Vitamin D deficiency (alali2023theetiopathogenesisof pages 1-2, micic2024currentlyavailabletreatment pages 1-2, larrain2024newinsightsinto pages 1-3)
- Alcohol consumption, high-fat diet (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3)
- Chronic stress and chronic inflammation (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2)
- Exposure to xenoestrogens (e.g., diethylstilbestrol, DES), air pollution (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3)
- Sexually transmitted infections (koltsova2023aviewon pages 1-2)

**Advanced Age:**
Reproductive age 35–50 years represents peak incidence (koltsova2023aviewon pages 1-2, tang2025theglobalburden pages 1-2, micic2024currentlyavailabletreatment pages 1-2).

### Protective Factors

**Genetic Protective Factors:**
Although specific protective genetic variants are not well-defined, the presence of certain alleles at GWAS loci may modulate risk (buyukcelebi2024integratingleiomyomagenetics pages 1-2).

**Environmental/Lifestyle Protective Factors:**
- Multiparity/parity (consistently protective) (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2)
- Combined oral contraceptive use (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2)
- Adequate vitamin D status (implied by deficiency being a risk factor) (micic2024currentlyavailabletreatment pages 1-2, wu2026preclinicalresearchplatform pages 1-2, larrain2024newinsightsinto pages 1-3)
- Postmenopausal state (fibroids often regress after menopause) (alali2023theetiopathogenesisof pages 1-2, ishikawa2023risingstarsrole pages 1-3)
- Smoking (paradoxically listed as protective in some reviews, though not clinically recommended) (koltsova2023aviewon pages 1-2)

### Gene-Environment Interactions

MED12 mutation status, race/ethnicity, and ovarian steroid hormones influence the expression of non-coding RNAs (ncRNAs) such as miRNAs, lncRNAs, and circRNAs, which regulate ECM production, cell proliferation, apoptosis, and inflammation in fibroids (boos2025therolesof pages 1-2). This represents a complex gene-environment interaction where genetic drivers (MED12 mutations), population ancestry, and hormonal milieu converge to shape tumor biology and phenotypic heterogeneity (chuang2023differentialexpressionof pages 1-2, boos2025therolesof pages 1-2).

---

## 3. PHENOTYPES

### Clinical Presentations

Approximately 70–80% of women with fibroids remain asymptomatic, with clinical manifestations occurring in 20–30% of cases (alali2023theetiopathogenesisof pages 1-2, centini2024tailoringthediagnostic pages 1-2). Symptomatic presentations vary widely depending on fibroid size, number, and location.

**Common Symptoms and Signs:**

1. **Abnormal Uterine Bleeding (AUB) and Heavy Menstrual Bleeding (HMB)**
   - **Type:** Symptom
   - **Characteristics:** Most common symptom; classified as AUB-L (AUB-Leiomyoma) by FIGO (vannuccini2024themodernmanagement pages 1-5). Heavy menstrual bleeding interferes with physical, social, emotional, and material quality of life (vannuccini2024themodernmanagement pages 1-5). Submucosal fibroids particularly cause bleeding (centini2024tailoringthediagnostic pages 1-2).
   - **Age of Onset:** Reproductive age, especially 35–50 years
   - **Severity:** Variable from mild to severe anemia-inducing
   - **Progression:** Can worsen over time if untreated
   - **Frequency:** Approximately 30% of women with fibroids; AUB/HMB is a major determinant of stress and reduced quality of life (vannuccini2024themodernmanagement pages 1-5)
   - **HPO Term Suggestion:** HP:0000132 (Menorrhagia), HP:0001892 (Abnormal bleeding tendency)

2. **Pelvic Pain and Dysmenorrhea**
   - **Type:** Symptom
   - **Characteristics:** Pelvic heaviness, pressure, pain, and dysmenorrhea (alali2023theetiopathogenesisof pages 1-2, centini2024tailoringthediagnostic pages 1-2)
   - **Severity:** Mild to severe
   - **HPO Term Suggestion:** HP:0000131 (Dysmenorrhea), HP:0100602 (Pelvic pain)

3. **Pelvic Pressure and Bulk Symptoms**
   - **Type:** Physical manifestation
   - **Characteristics:** Pressure on adjacent organs causing constipation, urinary dysfunction, and abdominal distension (alali2023theetiopathogenesisof pages 1-2, centini2024tailoringthediagnostic pages 1-2)
   - **Severity:** Depends on fibroid size and location
   - **HPO Term Suggestion:** HP:0100594 (Urinary dysfunction), HP:0002019 (Constipation)

4. **Iron Deficiency and Iron Deficiency Anemia (IDA)**
   - **Type:** Laboratory abnormality
   - **Characteristics:** Consequence of chronic blood loss from HMB (vannuccini2024themodernmanagement pages 1-5)
   - **Severity:** Variable; can be severe and symptomatic
   - **HPO Term Suggestion:** HP:0001891 (Iron deficiency anemia)

5. **Reproductive Dysfunction**
   - **Type:** Clinical manifestation
   - **Characteristics:** Infertility, recurrent pregnancy loss, preterm labor, defective embryo implantation, obstruction of labor (alali2023theetiopathogenesisof pages 1-2, buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2)
   - **Frequency:** Variable; associated with fibroid location and size
   - **HPO Term Suggestion:** HP:0000789 (Infertility), HP:0200067 (Recurrent spontaneous abortion), HP:0001622 (Preterm birth)

### Quality of Life Impact

Symptomatic uterine fibroids profoundly reduce quality of life (QoL) and decrease labor productivity (ishikawa2023risingstarsrole pages 1-3, vannuccini2024themodernmanagement pages 1-5). Women with HMB as the primary complaint experience significantly higher direct healthcare costs and perceived stress (vannuccini2024themodernmanagement pages 1-5). The disease impacts physical, social, emotional, and material well-being (vannuccini2024themodernmanagement pages 1-5). Annual costs in the United States range from $5.9 billion to $34.4 billion (buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2).

---

## 4. GENETIC/MOLECULAR INFORMATION

### Causal Genes and Pathogenic Variants

The comprehensive genetic mutations table summarizes causal genes and variants:

| Gene Name / Alteration | Mutation Type | Frequency / Prevalence | Molecular Effects | Clinical Associations | Key References |
|---|---|---:|---|---|---|
| **MED12** | Recurrent **somatic** exon 2 point mutations; typically heterozygous, gain-of-function–like driver alterations disrupting Mediator kinase module signaling | ~50–80% of uterine fibroids; ~70% in several recent summaries; 77% in a large review | Disrupts MED12-dependent activation of **CDK8/CDK19** within the Mediator complex; associated with altered chromatin landscape, enhancer engagement, genomic instability, progesterone responsiveness, and dysregulated **WNT/β-catenin**, hedgehog, sex steroid, and **TGF-β** signaling; transcriptomic enrichment for ECM/collagen pathways | Most common driver; often multiple tumors rather than solitary lesions; commonly seen even in small tumors; more frequent in Black women in some series; mutant tumors can differ in size/location and may show mutation-status–dependent response to GnRH agonists and ulipristal acetate | (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, ishikawa2023risingstarsrole pages 1-3) |
| **HMGA2 / HMGA1** | **Somatic** overexpression and chromosomal rearrangements/fusions involving HMGA2/1 | ~10% of fibroids in recent overview; in cellular leiomyoma, HMGA2 overexpression was 36.5% and rearrangement 13.2% | Alters chromatin architecture and transcriptional programs; defines a molecular subtype distinct from MED12-mutant tumors | Associated with distinct histopathologic phenotypes; important subtype in usual leiomyoma and especially enriched in some variants such as cellular leiomyoma | (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2, dundr2022uterinecellularleiomyomas pages 1-2) |
| **FH** | **Somatic or germline-related** loss-of-function / deficiency; part of FH-deficient leiomyoma spectrum and HLRCC-related disease | Less common than MED12/HMGA2 in unselected fibroids; recognized recurrent subtype | Fumarate hydratase deficiency rewires metabolism and contributes to a distinct molecular subtype of leiomyoma | Seen in FH-deficient leiomyomas and in hereditary leiomyomatosis and renal cell cancer (HLRCC); clinically relevant for identifying syndromic disease | (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, boos2025therolesof pages 1-2) |
| **COL4A5 / COL4A6** | Recurrent **somatic deletions / structural alterations** affecting collagen IV genes | Recurrent but uncommon relative to MED12; listed among frequently observed genetic alterations | Likely alters basement-membrane / ECM-related biology and contributes to subtype-specific tumor development | Included among recognized uterine fibroid driver alterations; may overlap with syndromic/structural subtypes rather than classic MED12 tumors | (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2, chuang2023differentialexpressionof pages 1-2) |
| **SRCAP complex genes** (e.g., **YEATS4, ZNHIT1**, other complex members) | **Inactivating somatic mutations** causing defective H2A.Z loading / chromatin remodeling abnormalities | Recently identified recurrent but uncommon subtype | Produces **H2A.Z deposition defects** and epigenetic dysregulation; supports a chromatin-based pathogenesis distinct from MED12 and HMGA2 | Emerging molecular class of leiomyoma; potentially useful for future subtype-based diagnostics and therapy development | (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2) |
| **Chromosome 1p deletion** | Recurrent **somatic copy-number loss** | 19.3% in a cellular leiomyoma series | Copy-number loss likely alters dosage of tumor-relevant genes on 1p; appears mutually exclusive with some other driver classes in variant tumors | Particularly reported in **cellular leiomyoma**; useful in variant classification and differential pathology | (dundr2022uterinecellularleiomyomas pages 1-2) |
| **24 GWAS risk loci / heritable susceptibility variants** (multiple genes including **GREB1, MCM8** and broader target-gene sets) | **Germline susceptibility SNPs** / risk loci from population genetics | 24 uterine-fibroid–associated risk loci identified in a 2024 integrative analysis; 394 potential target genes, 168 differentially expressed in tumors | Heritable risk variants map largely to noncoding regulatory regions and influence gene regulation through chromatin contacts, eQTL effects, and cell-type–specific regulatory programs | Explains familial aggregation and racial/population risk differences; points to causal cell types and potential preventive/targeted strategies rather than a single monogenic cause | (buyukcelebi2024integratingleiomyomagenetics pages 1-2) |
| **Non-coding RNA dysregulation linked to driver status** (e.g., miR-21, miR-29, miR-200; H19, MIAT, XIST) | Secondary molecular alterations influenced by driver mutations, race/ethnicity, and hormones rather than classic coding mutations | Commonly dysregulated across fibroids; not a single frequency estimate | Regulates ECM production, proliferation, apoptosis, and inflammation; expression is influenced by **MED12** mutation status and ovarian steroids | Potential biomarker and non-hormonal therapeutic layer; may help explain phenotypic heterogeneity and racial disparities | (boos2025therolesof pages 1-2) |


*Table: This table summarizes the principal genetic and molecular alterations implicated in uterine leiomyoma, emphasizing recurrent somatic drivers, inherited susceptibility loci, and their clinical relevance. It is useful for quickly comparing major subtypes, frequencies, and mechanistic consequences across the current evidence base.*

**MED12 (Mediator Complex Subunit 12):**
- **OMIM/HGNC:** MED12 gene located on chromosome Xq13.1
- **Variant Type:** Somatic exon 2 point mutations (typically codon 44 region); gain-of-function, driver mutations
- **Frequency:** 50–80% of fibroids (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, ishikawa2023risingstarsrole pages 1-3, boos2025therolesof pages 1-2)
- **Functional Consequences:** Disrupts CDK8/CDK19 kinase module activity; impairs Mediator kinase function; dysregulates WNT/β-catenin, TGF-β, hedgehog, and sex steroid signaling; alters chromatin landscape and enhancer-promoter interactions; increases genomic instability; enhances progesterone responsiveness (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, ishikawa2023risingstarsrole pages 1-3)
- **Clinical Associations:** More frequent in Black women; commonly observed in small tumors; associated with multiple rather than solitary fibroids; mutation-dependent response to GnRH agonists and ulipristal acetate (ishikawa2023risingstarsrole pages 1-3)

**HMGA2/HMGA1 (High Mobility Group AT-hook 2/1):**
- **Variant Type:** Somatic chromosomal rearrangements, fusions, and overexpression
- **Frequency:** ~10% overall; higher in cellular leiomyoma variants (bulun2025uterinefibroids pages 1-5, dundr2022uterinecellularleiomyomas pages 1-2)
- **Functional Consequences:** Alters chromatin architecture and transcriptional programs; defines distinct molecular subtype
- **Clinical Associations:** Distinct histopathologic phenotype; enriched in cellular leiomyoma (dundr2022uterinecellularleiomyomas pages 1-2)

**FH (Fumarate Hydratase):**
- **Variant Type:** Somatic or germline loss-of-function mutations
- **Functional Consequences:** Metabolic reprogramming; distinct molecular subtype
- **Clinical Associations:** FH-deficient leiomyomas; hereditary leiomyomatosis and renal cell cancer (HLRCC) syndrome (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2)

**COL4A5/COL4A6 (Collagen Type IV Alpha 5/6):**
- **Variant Type:** Somatic deletions and structural alterations
- **Functional Consequences:** Altered basement membrane/ECM biology (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2)

**SRCAP Complex Genes (YEATS4, ZNHIT1):**
- **Variant Type:** Inactivating somatic mutations
- **Functional Consequences:** Defective H2A.Z histone variant loading; chromatin remodeling abnormalities; epigenetic dysregulation (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2)

**Chromosome 1p Deletion:**
- **Variant Type:** Recurrent somatic copy-number loss
- **Frequency:** 19.3% in cellular leiomyoma series (dundr2022uterinecellularleiomyomas pages 1-2)

### Modifier Genes

The 24 GWAS-identified risk loci implicate 394 candidate genes, of which 168 are differentially expressed in tumors (buyukcelebi2024integratingleiomyomagenetics pages 1-2). These likely represent modifier loci influencing susceptibility, tumor multiplicity, and phenotypic variability.

### Epigenetic Information

**DNA Methylation:**
MED12-mutant fibroids exhibit distinct DNA methylomes compared to wild-type tumors (ishikawa2023risingstarsrole pages 1-3). Aberrant DNA methylation patterns contribute to altered gene expression profiles regulating ECM organization, cell proliferation, and steroid hormone responsiveness (chuang2023differentialexpressionof pages 1-2, ishikawa2023risingstarsrole pages 1-3).

**Histone Modifications:**
SRCAP complex mutations result in deficient H2A.Z deposition, causing chromatin-based pathogenesis distinct from MED12/HMGA2 subtypes (bulun2025uterinefibroids pages 1-5). Alterations in histone modifications affect enhancer-promoter interactions and gene regulatory programs (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2).

**Non-Coding RNAs:**
Dysregulated miRNAs (miR-21, miR-29, miR-200), lncRNAs (H19, MIAT, XIST), and circRNAs act as epigenetic regulators controlling ECM production, cell proliferation, apoptosis, and inflammation (boos2025therolesof pages 1-2). Expression is influenced by MED12 mutation status, race/ethnicity, and ovarian steroids (boos2025therolesof pages 1-2).

### Chromosomal Abnormalities

- Chromosome 1p deletions (dundr2022uterinecellularleiomyomas pages 1-2)
- HMGA2 chromosomal rearrangements and fusions (bulun2025uterinefibroids pages 1-5, dundr2022uterinecellularleiomyomas pages 1-2)
- COL4A5/COL4A6 deletions (bulun2025uterinefibroids pages 1-5)

### Allele Frequency and Origin

Somatic mutations (MED12, HMGA2, FH) are tumor-specific and not present in germline DNA (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, ishikawa2023risingstarsrole pages 1-3). Allele frequencies in population databases for germline GWAS risk variants vary by locus and population ancestry (buyukcelebi2024integratingleiomyomagenetics pages 1-2). FH germline mutations in HLRCC syndrome represent an exception where inherited pathogenic variants predispose to multiple fibroids and renal cell carcinoma (bulun2025uterinefibroids pages 1-5).

---

## 5. ENVIRONMENTAL INFORMATION

### Environmental Factors

- Xenoestrogen exposure in early life (koltsova2023aviewon pages 1-2)
- Diethylstilbestrol (DES) exposure (larrain2024newinsightsinto pages 1-3)
- Air pollution (larrain2024newinsightsinto pages 1-3)

### Lifestyle Factors

- Smoking (paradoxically protective but not recommended) (koltsova2023aviewon pages 1-2)
- Diet: High-fat diet increases risk; adequate vitamin D may be protective (micic2024currentlyavailabletreatment pages 1-2, wu2026preclinicalresearchplatform pages 1-2, larrain2024newinsightsinto pages 1-3)
- Alcohol consumption (risk factor) (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3)
- Obesity and physical activity patterns (alali2023theetiopathogenesisof pages 1-2, koltsova2023aviewon pages 1-2)
- Chronic stress (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2)

### Infectious Agents

Sexually transmitted infections are reported as potential risk factors, though the mechanism is less well-defined than hormonal/metabolic factors (koltsova2023aviewon pages 1-2).

---

## 6. MECHANISM / PATHOPHYSIOLOGY

### Molecular Pathways

**WNT/β-Catenin Signaling:**
Progesterone stimulates secretion of WNT ligands from mature myometrial and leiomyoma cells, inducing nuclear translocation of β-catenin in fibroid stem cells, promoting proliferation and ECM accumulation (larrain2024newinsightsinto pages 1-3). MED12 mutations enhance WNT/β-catenin pathway activation (ishikawa2023risingstarsrole pages 1-3, larrain2024newinsightsinto pages 1-3).

**TGF-β Signaling:**
Dysregulated TGF-β signaling promotes ECM production (particularly fibronectin and collagen), cell proliferation, and fibrosis (chuang2023differentialexpressionof pages 1-2, larrain2024newinsightsinto pages 1-3). TGF-β3 is upregulated via WNT signaling (larrain2024newinsightsinto pages 1-3).

**Progesterone and Estrogen Signaling:**
Progesterone (via PGR) is essential for fibroid growth, acting through paracrine mechanisms on stem cells (bulun2025uterinefibroids pages 1-5, larrain2024newinsightsinto pages 1-3). Estrogen enables progesterone action (bulun2025uterinefibroids pages 1-5). DNA methylation regulates PGR expression and responsiveness (bulun2025uterinefibroids pages 1-5).

**Hedgehog Pathway:**
Dysregulated in MED12-mutant fibroids (chuang2023differentialexpressionof pages 1-2).

**AKT/PI3K and Oxidative Stress:**
AKT activation and oxidative stress pathways contribute to fibroid pathogenesis (bulun2025uterinefibroids pages 1-5).

### Cellular Processes

- **Cell Proliferation:** Driven by stem cell expansion and paracrine growth factor signaling (bulun2025uterinefibroids pages 1-5, larrain2024newinsightsinto pages 1-3)
- **Apoptosis Dysregulation:** Reduced apoptosis contributes to tumor persistence (boos2025therolesof pages 1-2)
- **Inflammation:** Upregulation of pro-inflammatory cytokines (TNF-α, IL-6, IFN-γ) drives DNA damage, epigenetic alterations, and tumorigenesis (boos2025therolesof pages 1-2)
- **ECM Remodeling:** Excessive deposition of collagen, fibronectin, and proteoglycans creates fibroid bulk; ECM organization genes are upregulated, especially in MED12-mutant tumors (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, ishikawa2023risingstarsrole pages 1-3)
- **Cell Cycle Dysregulation:** Aberrant expression of cell cycle regulators (boos2025therolesof pages 1-2)

**Gene Ontology (GO) Terms:**
- GO:0030198 (extracellular matrix organization)
- GO:0008283 (cell proliferation)
- GO:0006915 (apoptotic process)
- GO:0006954 (inflammatory response)
- GO:0007049 (cell cycle)

### Protein Dysfunction

**MED12 Protein:**
Mutant MED12 disrupts CDK8/CDK19 stimulatory activity and alters chromatin-associated transcriptional regulation (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, ishikawa2023risingstarsrole pages 1-3).

**HMGA2 Protein:**
Overexpressed HMGA2 alters chromatin structure and transcriptional programs (bulun2025uterinefibroids pages 1-5).

**Fumarate Hydratase (FH):**
Loss of FH activity causes metabolic reprogramming (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2).

### Metabolic Changes

FH-deficient leiomyomas exhibit rewired metabolism due to fumarate hydratase loss (bulun2025uterinefibroids pages 1-5). Oxidative stress and altered energy metabolism are implicated in pathogenesis (bulun2025uterinefibroids pages 1-5).

### Immune System Involvement

Chronic inflammation with upregulation of pro-inflammatory cytokines (TNF-α, IL-6, IFN-γ) is a hallmark of fibroid pathogenesis (boos2025therolesof pages 1-2). Inflammatory pathways drive DNA damage and epigenetic changes, promoting tumorigenesis (boos2025therolesof pages 1-2).

### Tissue Damage Mechanisms

- Ischemia/hypoxia within tumor microenvironment (ishikawa2023risingstarsrole pages 1-3, larrain2024newinsightsinto pages 1-3)
- Fibrosis from excessive ECM deposition (bulun2025uterinefibroids pages 1-5, ishikawa2023risingstarsrole pages 1-3)
- Vascular abnormalities and angiogenesis dysregulation (vannuccini2024themodernmanagement pages 1-5)

### Molecular Profiling

**Transcriptomics:**
MED12-mutant tumors show 394 genes differentially expressed compared to matched myometrium, predominantly involved in ECM regulation (chuang2023differentialexpressionof pages 1-2). Distinct transcriptomic profiles differentiate MED12-mutant from wild-type fibroids (chuang2023differentialexpressionof pages 1-2, ishikawa2023risingstarsrole pages 1-3).

**Epigenomics:**
Distinct DNA methylomes and histone modification patterns characterize molecular subtypes (bulun2025uterinefibroids pages 1-5, ishikawa2023risingstarsrole pages 1-3).

**Single-Cell Transcriptomics:**
Integrative single-cell analysis reveals causal cell types with aberrant target gene expression linked to GWAS risk loci (buyukcelebi2024integratingleiomyomagenetics pages 1-2).

**Cell Types Involved:**
- Myometrial smooth muscle stem cells (tumor-initiating cells)
- Differentiated smooth muscle cells
- Tumor-associated fibroblasts
- Vascular smooth muscle cells
- Myofibroblasts

**Cell Ontology (CL) Terms:**
- CL:0000192 (smooth muscle cell)
- CL:0000057 (fibroblast)
- CL:0002548 (fibroblast of the uterus)

---

## 7. ANATOMICAL STRUCTURES AFFECTED

### Organ Level

**Primary Organ:**
- Uterus (specifically myometrium) (UBERON:0000995 uterus)

**Secondary Organ Involvement:**
- Endometrium (affected by submucosal fibroids causing bleeding) (UBERON:0001295 endometrium)
- Bladder (pressure symptoms) (UBERON:0001255 urinary bladder)
- Rectum (constipation) (UBERON:0001052 rectum)
- Reproductive tract complications (fallopian tube compression, cervical distortion)

**Body Systems Involved:**
- Female reproductive system
- Urinary system (secondary bulk effects)
- Gastrointestinal system (secondary bulk effects)
- Hematologic system (anemia from bleeding)

### Tissue and Cell Level

**Tissue Types:**
- Smooth muscle tissue (myometrium)
- Connective tissue (excessive ECM)

**Cell Populations:**
- Myometrial smooth muscle stem cells (CL:0000192)
- Differentiated smooth muscle cells (CL:0000192)
- Fibroblasts (CL:0000057, CL:0002548)
- Vascular smooth muscle cells
- Myofibroblasts
- Telocytes (interstitial cells forming contacts with smooth muscle and stem cells) (koltsova2023aviewon pages 1-2)

### Subcellular Level

**Cellular Compartments:**
- Nucleus (transcriptional dysregulation, chromatin remodeling) (GO:0005634 nucleus)
- Cytoplasm (signaling pathway activation)
- Extracellular matrix (excessive deposition) (GO:0031012 extracellular matrix)
- Chromatin (altered landscape in MED12-mutant tumors) (GO:0000785 chromatin)

### Localization

**FIGO Classification by Anatomical Site:**
- Type 0: Pedunculated intracavitary
- Type 1: <50% intramural
- Type 2: ≥50% intramural
- Type 3: 100% intramural; contacts endometrium
- Type 4: Intramural
- Type 5: Subserosal ≥50% intramural
- Type 6: Subserosal <50% intramural
- Type 7: Subserosal pedunculated
- Type 8: Other (cervical, parasitic)
- Hybrid: Submucous and subserous (micic2024currentlyavailabletreatment pages 1-2)

**Lateralization:**
Typically bilateral distribution within the uterus, though individual fibroids can be unilateral or asymmetric (alali2023theetiopathogenesisof pages 1-2).

---

## 8. TEMPORAL DEVELOPMENT

### Onset

**Age of Onset:**
- Rarely develop before menarche (ishikawa2023risingstarsrole pages 1-3)
- Most commonly diagnosed in reproductive age women, especially 35–50 years (koltsova2023aviewon pages 1-2, tang2025theglobalburden pages 1-2, micic2024currentlyavailabletreatment pages 1-2)
- Prevalence increases with age through reproductive years

**Onset Pattern:**
- Insidious and gradual; often asymptomatic initially (alali2023theetiopathogenesisof pages 1-2, centini2024tailoringthediagnostic pages 1-2)

### Progression

**Disease Course:**
- Variable growth rates; some fibroids grow rapidly, others remain stable or regress (larrain2024newinsightsinto pages 1-3)
- Multiple tumors within the same uterus are not clonally related and grow independently (larrain2024newinsightsinto pages 1-3)
- Progression influenced by hormonal milieu, mutation status, and patient-specific factors

**Disease Duration:**
- Chronic, lifelong presence through reproductive years
- Often regress after menopause due to decreased ovarian steroid production (alali2023theetiopathogenesisof pages 1-2, ishikawa2023risingstarsrole pages 1-3)

### Patterns

**Remission:**
- Spontaneous regression common after menopause (alali2023theetiopathogenesisof pages 1-2, ishikawa2023risingstarsrole pages 1-3)
- Treatment-induced shrinkage with GnRH agonists/antagonists, but rebound growth after discontinuation (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5)

**Critical Periods:**
- Reproductive years with ovulatory cycles (high estrogen/progesterone exposure)
- Pregnancy (first trimester growth stimulus) (bulun2025uterinefibroids pages 1-5)
- Menopause (regression window)

---

## 9. INHERITANCE AND POPULATION

### Epidemiology

**Prevalence:**
- Lifetime prevalence: 30–70% (alali2023theetiopathogenesisof pages 1-2, koltsova2023aviewon pages 1-2)
- By age 50: >70% overall, >80% in Black women (buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2)
- In 2021, age-standardized prevalence rate (ASPR): 2,841.07 per 100,000 (tang2025theglobalburden pages 1-2)

**Incidence:**
- Age-standardized incidence rate (ASIR) in 2021: 250.93 per 100,000 (tang2025theglobalburden pages 1-2)
- Incidence increasing globally from 1990 to 2021 (tang2025theglobalburden pages 1-2, zhang2025globalregionaland pages 1-2)

### Inheritance (for Genetic Etiology)

**Inheritance Pattern:**
- Multifactorial and polygenic susceptibility for sporadic fibroids (buyukcelebi2024integratingleiomyomagenetics pages 1-2)
- Autosomal dominant for HLRCC syndrome (germline FH mutations) (bulun2025uterinefibroids pages 1-5)

**Penetrance:**
- Variable and incomplete for heritable susceptibility loci (buyukcelebi2024integratingleiomyomagenetics pages 1-2)
- High penetrance for HLRCC-related fibroids (bulun2025uterinefibroids pages 1-5)

**Expressivity:**
- Variable; influenced by hormonal exposure, lifestyle, and modifier genes (buyukcelebi2024integratingleiomyomagenetics pages 1-2)

**Family History:**
- First-degree relatives have 2.5-fold elevated risk (buyukcelebi2024integratingleiomyomagenetics pages 1-2)

### Population Demographics

**Affected Populations:**
- Black/African-American women: highest prevalence and severity (>80% by age 50) (buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2, boos2025therolesof pages 1-2)
- Latin American women: elevated risk (koltsova2023aviewon pages 1-2)
- All racial/ethnic groups affected, but significant disparities exist

**Geographic Distribution:**
- Global distribution with higher burden in higher SDI (Socio-Demographic Index) regions for uterine fibroids, though lower SDI regions have higher burden for some gynecologic conditions (tang2025theglobalburden pages 1-2)
- Increasing incidence in countries like Brazil, India, and Georgia (zhang2025globalregionaland pages 1-2)

**Sex Ratio:**
- Female-only disease

**Age Distribution:**
- Peak ages 40–69 years globally for symptomatic burden (tang2025theglobalburden pages 1-2)
- Most commonly diagnosed 35–50 years (koltsova2023aviewon pages 1-2, micic2024currentlyavailabletreatment pages 1-2)

---

## 10. DIAGNOSTICS

### Clinical Tests

**Laboratory Tests:**
- Complete blood count (CBC) to assess anemia from HMB (vannuccini2024themodernmanagement pages 1-5)
- Iron studies (ferritin, serum iron, TIBC) for iron deficiency evaluation (vannuccini2024themodernmanagement pages 1-5)
- Hormone levels (estradiol, progesterone) if clinically indicated (buyukcelebi2024integratingleiomyomagenetics pages 1-2)

**Biomarkers:**
- No widely established serum biomarkers for routine diagnosis
- Emerging multi-omics biomarkers under investigation (vannuccini2024themodernmanagement pages 1-5)

**Imaging Studies:**
- **Transvaginal Ultrasound (TVS):** First-line imaging; detects presence, size, number, and location of fibroids (centini2024tailoringthediagnostic pages 1-2)
- **Sonohysterography:** Enhanced visualization of intracavitary lesions (centini2024tailoringthediagnostic pages 1-2)
- **Magnetic Resonance Imaging (MRI):** Gold standard for detailed anatomical characterization, differential diagnosis, and treatment planning; particularly useful for HIFU treatment planning and predicting regrowth (centini2024tailoringthediagnostic pages 1-2, vannuccini2024themodernmanagement pages 1-5)
- **Contrast-Enhanced MRI (CE-MRI):** Predicts residual fibroid regrowth post-HIFU; signal intensity ratios on CE-MRI correlate with long-term re-intervention rates (vannuccini2024themodernmanagement pages 1-5)

**MRI Radiomics:**
AI-based radiomics models combining T2-weighted MRI features with clinical parameters predict HIFU ablation efficacy and non-perfusion volume ratio (NPVR) (vannuccini2024themodernmanagement pages 1-5).

**Artificial Intelligence and Machine Learning:**
Deep learning models improve fibroid segmentation, diagnosis, and differentiation from malignancy using ultrasound and MRI images (vannuccini2024themodernmanagement pages 1-5).

**Functional Tests:**
Not routinely applicable

**Biopsy and Pathology:**
- Histopathological examination after surgical removal confirms diagnosis
- Immunohistochemistry: High expression of smooth muscle markers (calponin, desmin, SMA, caldesmon, transgelin, SMMHC, smoothelin); co-expression of endometrial stromal markers (CD10, IFITM1) in some variants (dundr2022uterinecellularleiomyomas pages 1-2)
- Molecular classification by mutation status (MED12, HMGA2, FH) increasingly relevant (ishikawa2023risingstarsrole pages 1-3, dundr2022uterinecellularleiomyomas pages 1-2)

### Genetic Testing

**Overview:**
Genetic testing is not routinely performed for sporadic fibroids but may be indicated in specific clinical scenarios.

**Single Gene Testing:**
- **FH gene testing** for suspected HLRCC syndrome (family history of renal cell carcinoma, early-onset multiple fibroids) (bulun2025uterinefibroids pages 1-5)

**Gene Panels:**
Not standard for uterine fibroids

**Chromosomal Microarray:**
Not routinely indicated

**Whole Exome/Genome Sequencing:**
Research tool; not routine clinical practice

**Somatic Mutation Testing:**
- MED12 mutation testing on tumor tissue can inform prognosis and potential treatment response (e.g., GnRH agonist/antagonist or ulipristal acetate response) (ishikawa2023risingstarsrole pages 1-3)
- HMGA2, FH, COL4A5/6, SRCAP complex mutations for molecular subtyping in research or specialized clinical settings (bulun2025uterinefibroids pages 1-5, dundr2022uterinecellularleiomyomas pages 1-2)

### Clinical Criteria

**Diagnostic Pathway:**
- Clinical suspicion based on symptoms (AUB, pelvic pain, bulk symptoms)
- Pelvic examination
- Transvaginal ultrasound (first-line imaging) (centini2024tailoringthediagnostic pages 1-2)
- Diagnostic hysteroscopy for intrauterine assessment if needed (centini2024tailoringthediagnostic pages 1-2)
- MRI when necessary for detailed characterization and treatment planning (centini2024tailoringthediagnostic pages 1-2)

**Differential Diagnosis:**
- Adenomyosis (can coexist)
- Endometrial stromal tumors (ESN, LG-ESS): differentiated by immunohistochemistry (IFITM1, CD10 patterns) and molecular testing (dundr2022uterinecellularleiomyomas pages 1-2)
- Leiomyosarcoma (LMS): requires histopathology; molecular profiling may assist (dundr2022uterinecellularleiomyomas pages 1-2)
- Smooth tumors of unknown malignant potential (STUMPs) (centini2024tailoringthediagnostic pages 1-2)

---

## 11. OUTCOME/PROGNOSIS

### Survival and Mortality

Uterine leiomyomas are benign tumors with very low risk of malignant transformation to leiomyosarcoma (bulun2025uterinefibroids pages 1-5). They are not typically associated with mortality unless severe anemia or surgical complications occur. Life expectancy is not significantly impacted by fibroids alone.

### Morbidity and Function

**Morbidity:**
- Significant morbidity from HMB, anemia, chronic pain, bulk symptoms, and reproductive dysfunction (alali2023theetiopathogenesisof pages 1-2, buyukcelebi2024integratingleiomyomagenetics pages 1-2, vannuccini2024themodernmanagement pages 1-5)
- Heavy menstrual bleeding is a leading cause of iron deficiency anemia in reproductive-age women (vannuccini2024themodernmanagement pages 1-5)

**Quality of Life:**
- Reduced quality of life in ~25–30% of affected women (bulun2025uterinefibroids pages 1-5, ishikawa2023risingstarsrole pages 1-3, vannuccini2024themodernmanagement pages 1-5)
- Decreased labor productivity (ishikawa2023risingstarsrole pages 1-3)
- Impaired physical, social, emotional, and material well-being (vannuccini2024themodernmanagement pages 1-5)

### Disease Course

**Complications:**
- Iron deficiency anemia (vannuccini2024themodernmanagement pages 1-5)
- Infertility, recurrent pregnancy loss, preterm labor (alali2023theetiopathogenesisof pages 1-2, buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2)
- Urinary incontinence, constipation (alali2023theetiopathogenesisof pages 1-2)
- Post-surgical complications (adhesions, bleeding, infection)
- Recurrence after myomectomy (micic2024currentlyavailabletreatment pages 1-2)

**Recovery Potential:**
- Fibroids often regress spontaneously after menopause (alali2023theetiopathogenesisof pages 1-2, ishikawa2023risingstarsrole pages 1-3)
- Surgical removal (myomectomy, hysterectomy) provides definitive symptom relief (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5)
- Medical treatments provide temporary symptom control but not cure; rebound growth after discontinuation (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5)

### Prognostic Factors

- MED12 mutation status may predict response to hormonal therapies (ishikawa2023risingstarsrole pages 1-3)
- Fibroid size, number, and location influence symptom burden and treatment outcomes
- MRI-based radiomics predict HIFU treatment success and fibroid regrowth (vannuccini2024themodernmanagement pages 1-5)

---

## 12. TREATMENT

A comprehensive treatment options table is provided below.

| Treatment Category | Specific Treatment Options | Mechanism of Action | Indications / Patient Selection | Clinical Efficacy | Side Effects / Limitations | MAXO term suggestion |
|---|---|---|---|---|---|---|
| Non-hormonal medical therapy | Tranexamic acid | Antifibrinolytic; reduces menstrual blood loss by inhibiting plasminogen activation | Symptomatic heavy menstrual bleeding (HMB) when uterine preservation desired; useful as symptom-control therapy rather than tumor-directed treatment (vannuccini2024themodernmanagement pages 1-5) | Improves fibroid-related abnormal uterine bleeding/heavy menstrual bleeding; does not shrink fibroids (vannuccini2024themodernmanagement pages 1-5) | No effect on fibroid size; symptomatic only; thrombotic-risk considerations in selected patients (vannuccini2024themodernmanagement pages 1-5) | MAXO: antifibrinolytic therapy |
| Non-hormonal medical therapy | NSAIDs | Reduce prostaglandin-mediated bleeding and pain | Mild-to-moderate bleeding and dysmenorrhea; patients seeking short-term symptom relief (vannuccini2024themodernmanagement pages 1-5) | Can reduce pain and some bleeding symptoms, but generally less effective than targeted hormonal suppression for fibroid burden (vannuccini2024themodernmanagement pages 1-5) | Symptomatic only; gastrointestinal/renal adverse effects; no fibroid shrinkage (vannuccini2024themodernmanagement pages 1-5) | MAXO: nonsteroidal anti-inflammatory drug therapy |
| Hormonal medical therapy | Combined oral contraceptives | Suppress ovulation/endometrial proliferation; reduce menstrual bleeding | Women with bleeding symptoms who desire non-surgical management and contraception (centini2024tailoringthediagnostic pages 1-2, micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Helpful for bleeding control; primarily symptom management rather than definitive fibroid treatment (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Limited effect on fibroid size; estrogen-containing therapy may not suit all patients (vannuccini2024themodernmanagement pages 1-5) | MAXO: hormonal therapy |
| Hormonal medical therapy | Progestogens | Endometrial suppression and bleeding control | Selected patients with abnormal uterine bleeding; often short-term or individualized use (micic2024currentlyavailabletreatment pages 1-2) | May improve bleeding; evidence for fibroid shrinkage is limited (micic2024currentlyavailabletreatment pages 1-2) | Restricted efficacy for bulk symptoms/size reduction; hormone-related adverse effects (micic2024currentlyavailabletreatment pages 1-2) | MAXO: progestogen therapy |
| Hormonal medical therapy | Levonorgestrel intrauterine system (LNG-IUS) | Local progestin effect on endometrium, reducing bleeding | Bleeding-predominant symptoms, especially when uterine cavity distortion is not prohibitive (vannuccini2024themodernmanagement pages 1-5) | Effective for HMB control in selected women; not a fibroid-eliminating therapy (vannuccini2024themodernmanagement pages 1-5) | Expulsion/placement difficulty with cavity distortion; limited effect on bulk symptoms or tumor size (vannuccini2024themodernmanagement pages 1-5) | MAXO: intrauterine hormone delivery |
| Hormonal medical therapy | GnRH agonists | Initial pituitary stimulation followed by downregulation, causing hypoestrogenism/hypoprogesteronism | Preoperative bridge therapy, short-term bleeding control, temporary fibroid shrinkage, anemia optimization before surgery (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Well-established temporary reduction in bleeding and fibroid size; useful as bridge to surgery (bulun2025uterinefibroids pages 1-5, micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Menopausal symptoms, bone loss with prolonged use, rebound growth after discontinuation (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | MAXO: gonadotropin-releasing hormone agonist therapy |
| Hormonal medical therapy | Oral GnRH antagonists | Direct pituitary GnRH blockade suppressing ovarian steroid production | Symptomatic fibroids with HMB; uterus-sparing medical management; useful when a reversible oral option is preferred (vannuccini2024themodernmanagement pages 1-5) | Effective modern option for reducing bleeding and improving symptoms; part of contemporary conservative management (vannuccini2024themodernmanagement pages 1-5) | Hypoestrogenic adverse effects; may require add-back strategies; treatment effect is not curative (vannuccini2024themodernmanagement pages 1-5) | MAXO: gonadotropin-releasing hormone antagonist therapy |
| Hormonal medical therapy | Selective progesterone receptor modulators (SPRMs), e.g. ulipristal acetate | Modulate progesterone receptor signaling, reducing bleeding and fibroid growth | Historically used for intermittent long-term bleeding and size control in selected women (micic2024currentlyavailabletreatment pages 1-2, ishikawa2023risingstarsrole pages 1-3, vannuccini2024themodernmanagement pages 1-5) | Good results reported for bleeding control and fibroid size reduction; response may vary with MED12 status (micic2024currentlyavailabletreatment pages 1-2, ishikawa2023risingstarsrole pages 1-3) | Regulatory/safety limitations in many regions, including liver toxicity concerns; access restricted (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | MAXO: selective progesterone receptor modulator therapy |
| Hormonal medical therapy | Aromatase inhibitors | Lower local/systemic estrogen synthesis | Selected refractory cases or off-label individualized management (vannuccini2024themodernmanagement pages 1-5) | May improve symptoms in some patients; evidence base narrower than GnRH-based approaches (vannuccini2024themodernmanagement pages 1-5) | Hypoestrogenic effects; not standard first-line treatment (vannuccini2024themodernmanagement pages 1-5) | MAXO: aromatase inhibitor therapy |
| Surgical therapy | Myomectomy (hysteroscopic, laparoscopic, open/laparotomic, mini-laparotomic, robotic) | Physical removal of fibroids with uterine preservation | Symptomatic patients desiring fertility preservation or uterine conservation; approach depends on number, size, and location of myomas (micic2024currentlyavailabletreatment pages 1-2, centini2024tailoringthediagnostic pages 1-2) | Effective symptom relief while preserving uterus; review data showed comparable average pregnancy rates between minimally invasive and open approaches (~29.7% vs ~28.5%) (micic2024currentlyavailabletreatment pages 1-2) | Recurrence risk persists; operative bleeding/adhesions; more invasive than medical/radiologic options (micic2024currentlyavailabletreatment pages 1-2) | MAXO: myomectomy |
| Surgical therapy | Hysterectomy | Definitive removal of uterus, eliminating fibroids | Women with severe symptoms, no fertility desire, recurrent disease, or failure of conservative options; often considered definitive therapy (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Most definitive symptom control; fibroid recurrence eliminated because uterus removed (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Loss of fertility; surgical morbidity; longer recovery than some minimally invasive approaches (micic2024currentlyavailabletreatment pages 1-2) | MAXO: hysterectomy |
| Minimally invasive / interventional | Uterine artery embolization (UAE) / uterine artery occlusion | Devascularization leading to ischemic shrinkage of fibroids | Symptomatic women seeking uterus-sparing, non-excisional treatment; generally not first choice when future fertility is a major goal (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Improves bleeding and bulk symptoms in many patients; accepted radiologic option in modern care pathways (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Post-embolization pain, reintervention/recurrence risk, uncertain reproductive implications relative to myomectomy (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | MAXO: uterine artery embolization |
| Minimally invasive / interventional | High-intensity focused ultrasound (HIFU) / MR-guided focused ultrasound | Thermal ablation of fibroid tissue | Selected women with accessible fibroid anatomy seeking noninvasive uterus-sparing treatment (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Can reduce symptoms and fibroid volume; post-treatment MRI parameters can predict regrowth/reintervention risk (vannuccini2024themodernmanagement pages 1-5) | Not suitable for all fibroid locations/sizes; residual fibroid regrowth can occur; access/expertise dependent (vannuccini2024themodernmanagement pages 1-5) | MAXO: focused ultrasound ablation |
| Minimally invasive / interventional | Radiofrequency ablation / myolysis | Thermal destruction of fibroid tissue | Symptomatic fibroids in patients preferring minimally invasive, uterus-preserving treatment (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Effective symptom-directed minimally invasive option in selected patients (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Long-term recurrence and fertility data less extensive than for myomectomy; anatomy-dependent feasibility (micic2024currentlyavailabletreatment pages 1-2) | MAXO: radiofrequency ablation |
| Minimally invasive / interventional | Endometrial ablation | Destruction of endometrium to reduce bleeding | Bleeding-predominant symptoms in carefully selected women not seeking fertility; not a tumor-directed therapy (micic2024currentlyavailabletreatment pages 1-2) | May reduce bleeding symptoms but does not treat intramural/subserosal tumor burden (micic2024currentlyavailabletreatment pages 1-2) | Not appropriate for future fertility; limited if cavity distortion is substantial (micic2024currentlyavailabletreatment pages 1-2) | MAXO: endometrial ablation |
| Supportive care | Iron replacement therapy | Repletes iron stores in iron deficiency/iron deficiency anemia from chronic bleeding | Women with fibroid-related HMB, iron deficiency, or anemia before/after surgery and during medical management (vannuccini2024themodernmanagement pages 1-5) | Improves consequences of chronic blood loss and perioperative readiness; important adjunct rather than fibroid-directed therapy (vannuccini2024themodernmanagement pages 1-5) | Does not treat underlying fibroids; oral GI intolerance or IV infusion logistics may limit use (vannuccini2024themodernmanagement pages 1-5) | MAXO: iron supplementation |
| Experimental / emerging | Vitamin D | Proposed antiproliferative/anti-fibrotic effects; deficiency is a reported risk factor | Investigational or adjunctive setting; biologic rationale strengthened by epidemiologic association with deficiency (micic2024currentlyavailabletreatment pages 1-2, wu2026preclinicalresearchplatform pages 1-2) | Promising preclinical and prior xenograft evidence noted in model reviews, but not established standard clinical therapy (wu2026preclinicalresearchplatform pages 1-2) | Insufficient evidence for routine standalone treatment of symptomatic leiomyoma (wu2026preclinicalresearchplatform pages 1-2) | MAXO: vitamin supplementation |
| Experimental / emerging | Targeted/precision approaches linked to molecular subtype (e.g., MED12-informed response prediction) | Treatment selection based on tumor driver biology and pathway dependence | Future personalized management, particularly for mutation-stratified hormonal response (ishikawa2023risingstarsrole pages 1-3) | Emerging evidence suggests MED12 status may influence response to GnRH agonists and ulipristal acetate (ishikawa2023risingstarsrole pages 1-3) | Not yet routine clinical standard; requires broader validation and accessible molecular testing (ishikawa2023risingstarsrole pages 1-3) | MAXO: precision medicine intervention |
| Experimental / emerging | Novel agents under investigation | Various pathways including progesterone signaling, ECM remodeling, and other molecular targets | Patients with unmet need for fertility-preserving, long-term, non-surgical options (micic2024currentlyavailabletreatment pages 1-2, bulun2025uterinefibroids pages 1-5) | Reviews describe multiple promising investigational therapies, but few are yet approved specifically for fibroids (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Evidence still evolving; many therapies remain investigational or regionally unavailable (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | MAXO: investigational pharmacotherapy |


*Table: This table summarizes current and emerging treatment options for uterine leiomyoma, including mechanisms, appropriate patient selection, expected efficacy, limitations, and suggested MAXO-aligned intervention labels. It is useful for comparing conservative, surgical, and interventional management strategies in one view.*

### Pharmacotherapy

**Non-Hormonal:**
- Tranexamic acid (antifibrinolytic for HMB) (vannuccini2024themodernmanagement pages 1-5) [MAXO: antifibrinolytic therapy]
- NSAIDs (symptom control for pain and bleeding) (vannuccini2024themodernmanagement pages 1-5) [MAXO: nonsteroidal anti-inflammatory drug therapy]

**Hormonal:**
- Combined oral contraceptives (centini2024tailoringthediagnostic pages 1-2, micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) [MAXO: hormonal therapy]
- Progestogens (micic2024currentlyavailabletreatment pages 1-2) [MAXO: progestogen therapy]
- Levonorgestrel intrauterine system (LNG-IUS) (vannuccini2024themodernmanagement pages 1-5) [MAXO: intrauterine hormone delivery]
- GnRH agonists (preoperative bridge, temporary shrinkage) (bulun2025uterinefibroids pages 1-5, micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) [MAXO: gonadotropin-releasing hormone agonist therapy]
- Oral GnRH antagonists (modern option for symptom and size control) (vannuccini2024themodernmanagement pages 1-5) [MAXO: gonadotropin-releasing hormone antagonist therapy]
- Selective progesterone receptor modulators (SPRMs, e.g., ulipristal acetate): historically effective but limited by safety concerns (micic2024currentlyavailabletreatment pages 1-2, ishikawa2023risingstarsrole pages 1-3, vannuccini2024themodernmanagement pages 1-5) [MAXO: selective progesterone receptor modulator therapy]
- Aromatase inhibitors (off-label) (vannuccini2024themodernmanagement pages 1-5) [MAXO: aromatase inhibitor therapy]

**Pharmacogenomics:**
MED12 mutation status influences response to GnRH agonists and ulipristal acetate, suggesting potential for mutation-guided therapy (ishikawa2023risingstarsrole pages 1-3).

### Advanced Therapeutics

**Experimental:**
- Vitamin D supplementation (promising preclinical/xenograft evidence but not standard therapy) (micic2024currentlyavailabletreatment pages 1-2, wu2026preclinicalresearchplatform pages 1-2)
- Catechol-O-methyltransferase inhibitors (evaluated in Eker rat models) (wu2026preclinicalresearchplatform pages 1-2)
- Hedgehog pathway inhibitors (GLI inhibitors like Gant61 show efficacy in xenograft models) (wu2026preclinicalresearchplatform pages 1-2)
- Novel targeted therapies based on molecular subtype (under investigation) (bulun2025uterinefibroids pages 1-5, micic2024currentlyavailabletreatment pages 1-2, ishikawa2023risingstarsrole pages 1-3)

### Surgical and Interventional

**Surgical:**
- **Myomectomy** (hysteroscopic, laparoscopic, open, robotic): Fertility-preserving fibroid removal (micic2024currentlyavailabletreatment pages 1-2) [MAXO: myomectomy]
- **Hysterectomy**: Definitive treatment, loss of fertility (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) [MAXO: hysterectomy]

**Minimally Invasive/Interventional:**
- **Uterine artery embolization (UAE)**: Devascularization (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) [MAXO: uterine artery embolization]
- **High-intensity focused ultrasound (HIFU)**: Thermal ablation (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) [MAXO: focused ultrasound ablation]
- **Radiofrequency ablation**: Thermal destruction (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) [MAXO: radiofrequency ablation]
- **Endometrial ablation**: For bleeding control (micic2024currentlyavailabletreatment pages 1-2) [MAXO: endometrial ablation]

### Supportive and Rehabilitative

- **Iron replacement therapy**: For iron deficiency anemia (vannuccini2024themodernmanagement pages 1-5) [MAXO: iron supplementation]

### Treatment Outcomes

**Response Rates:**
- GnRH agonists/antagonists: Effective temporary shrinkage and symptom control; rebound after discontinuation (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5)
- Myomectomy: Effective symptom relief; pregnancy rates comparable between minimally invasive and open approaches (~29.7% vs ~28.5%) (micic2024currentlyavailabletreatment pages 1-2)
- Hysterectomy: Most definitive; eliminates recurrence (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5)
- UAE and HIFU: Improve symptoms in many patients; reintervention rates variable (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5)

**Side Effects:**
- GnRH agonists/antagonists: Menopausal symptoms, bone loss with prolonged use (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5)
- SPRMs: Liver toxicity concerns (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5)
- Surgical: Bleeding, adhesions, infection, longer recovery for open surgery (micic2024currentlyavailabletreatment pages 1-2)

### Treatment Strategy

- Individualized based on symptoms, fibroid characteristics, fertility desire, and patient preference (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5)
- Shared decision-making emphasizing short- and long-term treatment goals (centini2024tailoringthediagnostic pages 1-2, vannuccini2024themodernmanagement pages 1-5)
- Medical therapy often used as bridge to surgery or for patients preferring conservative management (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5)
- Personalized/precision approaches incorporating MED12 mutation status for response prediction are emerging (ishikawa2023risingstarsrole pages 1-3)

---

## 13. PREVENTION

### Prevention Levels

**Primary Prevention:**
- Lifestyle modifications: Maintain healthy body weight, adequate vitamin D, balanced diet (micic2024currentlyavailabletreatment pages 1-2, larrain2024newinsightsinto pages 1-3)
- Avoid excessive alcohol consumption (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3)
- Reduce exposure to xenoestrogens and environmental pollutants (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3)
- Multiparity may be protective (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2)

**Secondary Prevention:**
- Early detection via routine pelvic exams and ultrasound in asymptomatic women at high risk (family history, Black ancestry) (buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2)
- Prompt treatment of symptomatic fibroids to prevent complications like anemia and reproductive dysfunction

**Tertiary Prevention:**
- Medical management to prevent symptom progression and complications (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5)
- Iron supplementation to prevent anemia in women with HMB (vannuccini2024themodernmanagement pages 1-5)

### Immunization

Not applicable

### Screening and Early Detection

**Screening Programs:**
- No population-based screening recommended for asymptomatic women
- Opportunistic detection during routine gynecological ultrasound

**Genetic Screening:**
- Genetic counseling and FH gene testing for families with HLRCC syndrome (bulun2025uterinefibroids pages 1-5)

**Risk Stratification:**
- Family history, race/ethnicity, reproductive history, and GWAS risk scores may identify high-risk individuals (buyukcelebi2024integratingleiomyomagenetics pages 1-2)

### Behavioral Interventions

- Weight management and healthy diet (micic2024currentlyavailabletreatment pages 1-2, larrain2024newinsightsinto pages 1-3)
- Stress reduction (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2)

### Counseling

Genetic counseling for HLRCC syndrome families (bulun2025uterinefibroids pages 1-5)

### Public Health

- Health education on modifiable risk factors
- Reduce environmental xenoestrogen exposure (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3)

---

## 14. OTHER SPECIES / NATURAL DISEASE

### Taxonomy

- Eker rats (*Rattus norvegicus*) with Tsc2 germline mutation spontaneously develop uterine smooth muscle tumors (wu2026preclinicalresearchplatform pages 1-2)
- Japanese quail spontaneously develop leiomyomas (wu2026preclinicalresearchplatform pages 1-2)
- Miniature pet pigs (*Sus scrofa*) documented with spontaneous leiomyomas (wu2026preclinicalresearchplatform pages 1-2)

**NCBI Taxon IDs:**
- *Rattus norvegicus*: NCBITaxon:10116
- *Sus scrofa*: NCBITaxon:9823
- *Coturnix japonica* (Japanese quail): NCBITaxon:93934

### Natural Disease

**Eker Rats:**
Approximately 65% of female Eker rats develop uterine smooth muscle tumors by 12–16 months of age due to germline Tsc2 mutation (wu2026preclinicalresearchplatform pages 1-2). Histomorphology and hormone-dependence are highly similar to human fibroids (wu2026preclinicalresearchplatform pages 1-2).

**Japanese Quail and Miniature Pigs:**
Also exhibit spontaneous leiomyomas, though less extensively characterized (wu2026preclinicalresearchplatform pages 1-2).

### Comparative Biology

Eker rat tumors recapitulate key features of human fibroids, including estrogen/progesterone-dependent growth, ECM-rich composition, and similar histology (wu2026preclinicalresearchplatform pages 1-2). However, Eker rats develop concurrent renal and hepatic tumors, complicating model interpretation (wu2026preclinicalresearchplatform pages 1-2).

---

## 15. MODEL ORGANISMS

### Model Types

**Spontaneous Animal Models:**
- **Eker Rats:** Germline Tsc2 mutation; spontaneous tumor development by 12–16 months; widely used for etiology and drug validation studies (wu2026preclinicalresearchplatform pages 1-2)
- **Japanese Quail and Miniature Pigs:** Spontaneous models, less commonly used (wu2026preclinicalresearchplatform pages 1-2)

**Genetically Modified Animal Models:**
- **Conditional MED12-mutant mouse model:** Engineered MED12 exon 2 mutation in uterus; develops leiomyoma-like tumors; confirms MED12 gain-of-function role (bulun2025uterinefibroids pages 1-5, wu2026preclinicalresearchplatform pages 1-2)

**Hormone-Induced Animal Models:**
- Combined estrogen-progesterone induction in mice/rats (wu2026preclinicalresearchplatform pages 1-2)
- Sequential induction (estrogen followed by progesterone) mimics natural hormonal cycles (wu2026preclinicalresearchplatform pages 1-2)
- Concurrent induction promotes hormone receptor expression (wu2026preclinicalresearchplatform pages 1-2)
- Multi-factor composite models integrating chronic stress and epinephrine intervention to simulate "Qi Stagnation and Blood Stasis" syndrome in integrated medicine research (wu2026preclinicalresearchplatform pages 1-2)

**Xenograft Animal Models:**
- Patient-derived xenografts (PDX) in immunodeficient mice (e.g., SCID, NSG mice) (wu2026preclinicalresearchplatform pages 1-2)
- Maintain human fibroid architecture, hormone-responsiveness, and genetic background (wu2026preclinicalresearchplatform pages 1-2)
- Useful for drug testing and mechanistic studies (wu2026preclinicalresearchplatform pages 1-2)

**Organotypic/Ex Vivo Models:**
- Organotypic culture of fibroid tissue slices on alginate scaffolds; maintains morphological integrity, steroid receptor expression, and driver mutations for up to 7 days (wu2026preclinicalresearchplatform pages 1-2)
- Allows encapsulation of drug-loaded microspheres for preclinical testing (wu2026preclinicalresearchplatform pages 1-2)

### Genetic Models

- Conditional MED12-mutant mice (bulun2025uterinefibroids pages 1-5, wu2026preclinicalresearchplatform pages 1-2)
- Eker rats (Tsc2 mutation) (wu2026preclinicalresearchplatform pages 1-2)

### Model Characteristics

**Phenotype Recapitulation:**
- Eker rats: High similarity in histology, ECM deposition, and hormone-dependence; useful for mTOR pathway studies (wu2026preclinicalresearchplatform pages 1-2)
- MED12-mutant mice: Confirm gain-of-function mutation role and leiomyoma pathogenesis (bulun2025uterinefibroids pages 1-5, wu2026preclinicalresearchplatform pages 1-2)
- Xenografts: Best preserve human tumor heterogeneity and genetic background (wu2026preclinicalresearchplatform pages 1-2)

**Model Limitations:**
- Eker rats: Long establishment time (12–16 months), concurrent tumors (renal, hepatic), high cost (wu2026preclinicalresearchplatform pages 1-2)
- Hormone-induced models: May not fully replicate spontaneous human disease complexity; reproducibility variable (wu2026preclinicalresearchplatform pages 1-2)
- Xenografts: Require immunodeficient hosts; do not capture immune interactions (wu2026preclinicalresearchplatform pages 1-2)

### Applications

- Etiology and mechanism research (wu2026preclinicalresearchplatform pages 1-2)
- Drug efficacy and safety testing (wu2026preclinicalresearchplatform pages 1-2)
- Evaluation of novel therapies (vitamin D, hedgehog inhibitors, hormonal agents) (wu2026preclinicalresearchplatform pages 1-2)

### Resources

- Mouse models: MGI, IMPC, KOMP repositories
- Rat models: RGD
- Xenograft protocols and cell lines available through specialized research centers

---

## SUMMARY TABLES

### Key Genetic Mutations in Uterine Leiomyoma
| Gene Name / Alteration | Mutation Type | Frequency / Prevalence | Molecular Effects | Clinical Associations | Key References |
|---|---|---:|---|---|---|
| **MED12** | Recurrent **somatic** exon 2 point mutations; typically heterozygous, gain-of-function–like driver alterations disrupting Mediator kinase module signaling | ~50–80% of uterine fibroids; ~70% in several recent summaries; 77% in a large review | Disrupts MED12-dependent activation of **CDK8/CDK19** within the Mediator complex; associated with altered chromatin landscape, enhancer engagement, genomic instability, progesterone responsiveness, and dysregulated **WNT/β-catenin**, hedgehog, sex steroid, and **TGF-β** signaling; transcriptomic enrichment for ECM/collagen pathways | Most common driver; often multiple tumors rather than solitary lesions; commonly seen even in small tumors; more frequent in Black women in some series; mutant tumors can differ in size/location and may show mutation-status–dependent response to GnRH agonists and ulipristal acetate | (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, ishikawa2023risingstarsrole pages 1-3) |
| **HMGA2 / HMGA1** | **Somatic** overexpression and chromosomal rearrangements/fusions involving HMGA2/1 | ~10% of fibroids in recent overview; in cellular leiomyoma, HMGA2 overexpression was 36.5% and rearrangement 13.2% | Alters chromatin architecture and transcriptional programs; defines a molecular subtype distinct from MED12-mutant tumors | Associated with distinct histopathologic phenotypes; important subtype in usual leiomyoma and especially enriched in some variants such as cellular leiomyoma | (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2, dundr2022uterinecellularleiomyomas pages 1-2) |
| **FH** | **Somatic or germline-related** loss-of-function / deficiency; part of FH-deficient leiomyoma spectrum and HLRCC-related disease | Less common than MED12/HMGA2 in unselected fibroids; recognized recurrent subtype | Fumarate hydratase deficiency rewires metabolism and contributes to a distinct molecular subtype of leiomyoma | Seen in FH-deficient leiomyomas and in hereditary leiomyomatosis and renal cell cancer (HLRCC); clinically relevant for identifying syndromic disease | (bulun2025uterinefibroids pages 1-5, chuang2023differentialexpressionof pages 1-2, boos2025therolesof pages 1-2) |
| **COL4A5 / COL4A6** | Recurrent **somatic deletions / structural alterations** affecting collagen IV genes | Recurrent but uncommon relative to MED12; listed among frequently observed genetic alterations | Likely alters basement-membrane / ECM-related biology and contributes to subtype-specific tumor development | Included among recognized uterine fibroid driver alterations; may overlap with syndromic/structural subtypes rather than classic MED12 tumors | (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2, chuang2023differentialexpressionof pages 1-2) |
| **SRCAP complex genes** (e.g., **YEATS4, ZNHIT1**, other complex members) | **Inactivating somatic mutations** causing defective H2A.Z loading / chromatin remodeling abnormalities | Recently identified recurrent but uncommon subtype | Produces **H2A.Z deposition defects** and epigenetic dysregulation; supports a chromatin-based pathogenesis distinct from MED12 and HMGA2 | Emerging molecular class of leiomyoma; potentially useful for future subtype-based diagnostics and therapy development | (bulun2025uterinefibroids pages 1-5, buyukcelebi2024integratingleiomyomagenetics pages 1-2) |
| **Chromosome 1p deletion** | Recurrent **somatic copy-number loss** | 19.3% in a cellular leiomyoma series | Copy-number loss likely alters dosage of tumor-relevant genes on 1p; appears mutually exclusive with some other driver classes in variant tumors | Particularly reported in **cellular leiomyoma**; useful in variant classification and differential pathology | (dundr2022uterinecellularleiomyomas pages 1-2) |
| **24 GWAS risk loci / heritable susceptibility variants** (multiple genes including **GREB1, MCM8** and broader target-gene sets) | **Germline susceptibility SNPs** / risk loci from population genetics | 24 uterine-fibroid–associated risk loci identified in a 2024 integrative analysis; 394 potential target genes, 168 differentially expressed in tumors | Heritable risk variants map largely to noncoding regulatory regions and influence gene regulation through chromatin contacts, eQTL effects, and cell-type–specific regulatory programs | Explains familial aggregation and racial/population risk differences; points to causal cell types and potential preventive/targeted strategies rather than a single monogenic cause | (buyukcelebi2024integratingleiomyomagenetics pages 1-2) |
| **Non-coding RNA dysregulation linked to driver status** (e.g., miR-21, miR-29, miR-200; H19, MIAT, XIST) | Secondary molecular alterations influenced by driver mutations, race/ethnicity, and hormones rather than classic coding mutations | Commonly dysregulated across fibroids; not a single frequency estimate | Regulates ECM production, proliferation, apoptosis, and inflammation; expression is influenced by **MED12** mutation status and ovarian steroids | Potential biomarker and non-hormonal therapeutic layer; may help explain phenotypic heterogeneity and racial disparities | (boos2025therolesof pages 1-2) |


*Table: This table summarizes the principal genetic and molecular alterations implicated in uterine leiomyoma, emphasizing recurrent somatic drivers, inherited susceptibility loci, and their clinical relevance. It is useful for quickly comparing major subtypes, frequencies, and mechanistic consequences across the current evidence base.*

### Treatment Options for Uterine Leiomyoma
| Treatment Category | Specific Treatment Options | Mechanism of Action | Indications / Patient Selection | Clinical Efficacy | Side Effects / Limitations | MAXO term suggestion |
|---|---|---|---|---|---|---|
| Non-hormonal medical therapy | Tranexamic acid | Antifibrinolytic; reduces menstrual blood loss by inhibiting plasminogen activation | Symptomatic heavy menstrual bleeding (HMB) when uterine preservation desired; useful as symptom-control therapy rather than tumor-directed treatment (vannuccini2024themodernmanagement pages 1-5) | Improves fibroid-related abnormal uterine bleeding/heavy menstrual bleeding; does not shrink fibroids (vannuccini2024themodernmanagement pages 1-5) | No effect on fibroid size; symptomatic only; thrombotic-risk considerations in selected patients (vannuccini2024themodernmanagement pages 1-5) | MAXO: antifibrinolytic therapy |
| Non-hormonal medical therapy | NSAIDs | Reduce prostaglandin-mediated bleeding and pain | Mild-to-moderate bleeding and dysmenorrhea; patients seeking short-term symptom relief (vannuccini2024themodernmanagement pages 1-5) | Can reduce pain and some bleeding symptoms, but generally less effective than targeted hormonal suppression for fibroid burden (vannuccini2024themodernmanagement pages 1-5) | Symptomatic only; gastrointestinal/renal adverse effects; no fibroid shrinkage (vannuccini2024themodernmanagement pages 1-5) | MAXO: nonsteroidal anti-inflammatory drug therapy |
| Hormonal medical therapy | Combined oral contraceptives | Suppress ovulation/endometrial proliferation; reduce menstrual bleeding | Women with bleeding symptoms who desire non-surgical management and contraception (centini2024tailoringthediagnostic pages 1-2, micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Helpful for bleeding control; primarily symptom management rather than definitive fibroid treatment (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Limited effect on fibroid size; estrogen-containing therapy may not suit all patients (vannuccini2024themodernmanagement pages 1-5) | MAXO: hormonal therapy |
| Hormonal medical therapy | Progestogens | Endometrial suppression and bleeding control | Selected patients with abnormal uterine bleeding; often short-term or individualized use (micic2024currentlyavailabletreatment pages 1-2) | May improve bleeding; evidence for fibroid shrinkage is limited (micic2024currentlyavailabletreatment pages 1-2) | Restricted efficacy for bulk symptoms/size reduction; hormone-related adverse effects (micic2024currentlyavailabletreatment pages 1-2) | MAXO: progestogen therapy |
| Hormonal medical therapy | Levonorgestrel intrauterine system (LNG-IUS) | Local progestin effect on endometrium, reducing bleeding | Bleeding-predominant symptoms, especially when uterine cavity distortion is not prohibitive (vannuccini2024themodernmanagement pages 1-5) | Effective for HMB control in selected women; not a fibroid-eliminating therapy (vannuccini2024themodernmanagement pages 1-5) | Expulsion/placement difficulty with cavity distortion; limited effect on bulk symptoms or tumor size (vannuccini2024themodernmanagement pages 1-5) | MAXO: intrauterine hormone delivery |
| Hormonal medical therapy | GnRH agonists | Initial pituitary stimulation followed by downregulation, causing hypoestrogenism/hypoprogesteronism | Preoperative bridge therapy, short-term bleeding control, temporary fibroid shrinkage, anemia optimization before surgery (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Well-established temporary reduction in bleeding and fibroid size; useful as bridge to surgery (bulun2025uterinefibroids pages 1-5, micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Menopausal symptoms, bone loss with prolonged use, rebound growth after discontinuation (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | MAXO: gonadotropin-releasing hormone agonist therapy |
| Hormonal medical therapy | Oral GnRH antagonists | Direct pituitary GnRH blockade suppressing ovarian steroid production | Symptomatic fibroids with HMB; uterus-sparing medical management; useful when a reversible oral option is preferred (vannuccini2024themodernmanagement pages 1-5) | Effective modern option for reducing bleeding and improving symptoms; part of contemporary conservative management (vannuccini2024themodernmanagement pages 1-5) | Hypoestrogenic adverse effects; may require add-back strategies; treatment effect is not curative (vannuccini2024themodernmanagement pages 1-5) | MAXO: gonadotropin-releasing hormone antagonist therapy |
| Hormonal medical therapy | Selective progesterone receptor modulators (SPRMs), e.g. ulipristal acetate | Modulate progesterone receptor signaling, reducing bleeding and fibroid growth | Historically used for intermittent long-term bleeding and size control in selected women (micic2024currentlyavailabletreatment pages 1-2, ishikawa2023risingstarsrole pages 1-3, vannuccini2024themodernmanagement pages 1-5) | Good results reported for bleeding control and fibroid size reduction; response may vary with MED12 status (micic2024currentlyavailabletreatment pages 1-2, ishikawa2023risingstarsrole pages 1-3) | Regulatory/safety limitations in many regions, including liver toxicity concerns; access restricted (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | MAXO: selective progesterone receptor modulator therapy |
| Hormonal medical therapy | Aromatase inhibitors | Lower local/systemic estrogen synthesis | Selected refractory cases or off-label individualized management (vannuccini2024themodernmanagement pages 1-5) | May improve symptoms in some patients; evidence base narrower than GnRH-based approaches (vannuccini2024themodernmanagement pages 1-5) | Hypoestrogenic effects; not standard first-line treatment (vannuccini2024themodernmanagement pages 1-5) | MAXO: aromatase inhibitor therapy |
| Surgical therapy | Myomectomy (hysteroscopic, laparoscopic, open/laparotomic, mini-laparotomic, robotic) | Physical removal of fibroids with uterine preservation | Symptomatic patients desiring fertility preservation or uterine conservation; approach depends on number, size, and location of myomas (micic2024currentlyavailabletreatment pages 1-2, centini2024tailoringthediagnostic pages 1-2) | Effective symptom relief while preserving uterus; review data showed comparable average pregnancy rates between minimally invasive and open approaches (~29.7% vs ~28.5%) (micic2024currentlyavailabletreatment pages 1-2) | Recurrence risk persists; operative bleeding/adhesions; more invasive than medical/radiologic options (micic2024currentlyavailabletreatment pages 1-2) | MAXO: myomectomy |
| Surgical therapy | Hysterectomy | Definitive removal of uterus, eliminating fibroids | Women with severe symptoms, no fertility desire, recurrent disease, or failure of conservative options; often considered definitive therapy (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Most definitive symptom control; fibroid recurrence eliminated because uterus removed (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Loss of fertility; surgical morbidity; longer recovery than some minimally invasive approaches (micic2024currentlyavailabletreatment pages 1-2) | MAXO: hysterectomy |
| Minimally invasive / interventional | Uterine artery embolization (UAE) / uterine artery occlusion | Devascularization leading to ischemic shrinkage of fibroids | Symptomatic women seeking uterus-sparing, non-excisional treatment; generally not first choice when future fertility is a major goal (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Improves bleeding and bulk symptoms in many patients; accepted radiologic option in modern care pathways (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Post-embolization pain, reintervention/recurrence risk, uncertain reproductive implications relative to myomectomy (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | MAXO: uterine artery embolization |
| Minimally invasive / interventional | High-intensity focused ultrasound (HIFU) / MR-guided focused ultrasound | Thermal ablation of fibroid tissue | Selected women with accessible fibroid anatomy seeking noninvasive uterus-sparing treatment (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Can reduce symptoms and fibroid volume; post-treatment MRI parameters can predict regrowth/reintervention risk (vannuccini2024themodernmanagement pages 1-5) | Not suitable for all fibroid locations/sizes; residual fibroid regrowth can occur; access/expertise dependent (vannuccini2024themodernmanagement pages 1-5) | MAXO: focused ultrasound ablation |
| Minimally invasive / interventional | Radiofrequency ablation / myolysis | Thermal destruction of fibroid tissue | Symptomatic fibroids in patients preferring minimally invasive, uterus-preserving treatment (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Effective symptom-directed minimally invasive option in selected patients (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Long-term recurrence and fertility data less extensive than for myomectomy; anatomy-dependent feasibility (micic2024currentlyavailabletreatment pages 1-2) | MAXO: radiofrequency ablation |
| Minimally invasive / interventional | Endometrial ablation | Destruction of endometrium to reduce bleeding | Bleeding-predominant symptoms in carefully selected women not seeking fertility; not a tumor-directed therapy (micic2024currentlyavailabletreatment pages 1-2) | May reduce bleeding symptoms but does not treat intramural/subserosal tumor burden (micic2024currentlyavailabletreatment pages 1-2) | Not appropriate for future fertility; limited if cavity distortion is substantial (micic2024currentlyavailabletreatment pages 1-2) | MAXO: endometrial ablation |
| Supportive care | Iron replacement therapy | Repletes iron stores in iron deficiency/iron deficiency anemia from chronic bleeding | Women with fibroid-related HMB, iron deficiency, or anemia before/after surgery and during medical management (vannuccini2024themodernmanagement pages 1-5) | Improves consequences of chronic blood loss and perioperative readiness; important adjunct rather than fibroid-directed therapy (vannuccini2024themodernmanagement pages 1-5) | Does not treat underlying fibroids; oral GI intolerance or IV infusion logistics may limit use (vannuccini2024themodernmanagement pages 1-5) | MAXO: iron supplementation |
| Experimental / emerging | Vitamin D | Proposed antiproliferative/anti-fibrotic effects; deficiency is a reported risk factor | Investigational or adjunctive setting; biologic rationale strengthened by epidemiologic association with deficiency (micic2024currentlyavailabletreatment pages 1-2, wu2026preclinicalresearchplatform pages 1-2) | Promising preclinical and prior xenograft evidence noted in model reviews, but not established standard clinical therapy (wu2026preclinicalresearchplatform pages 1-2) | Insufficient evidence for routine standalone treatment of symptomatic leiomyoma (wu2026preclinicalresearchplatform pages 1-2) | MAXO: vitamin supplementation |
| Experimental / emerging | Targeted/precision approaches linked to molecular subtype (e.g., MED12-informed response prediction) | Treatment selection based on tumor driver biology and pathway dependence | Future personalized management, particularly for mutation-stratified hormonal response (ishikawa2023risingstarsrole pages 1-3) | Emerging evidence suggests MED12 status may influence response to GnRH agonists and ulipristal acetate (ishikawa2023risingstarsrole pages 1-3) | Not yet routine clinical standard; requires broader validation and accessible molecular testing (ishikawa2023risingstarsrole pages 1-3) | MAXO: precision medicine intervention |
| Experimental / emerging | Novel agents under investigation | Various pathways including progesterone signaling, ECM remodeling, and other molecular targets | Patients with unmet need for fertility-preserving, long-term, non-surgical options (micic2024currentlyavailabletreatment pages 1-2, bulun2025uterinefibroids pages 1-5) | Reviews describe multiple promising investigational therapies, but few are yet approved specifically for fibroids (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | Evidence still evolving; many therapies remain investigational or regionally unavailable (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5) | MAXO: investigational pharmacotherapy |


*Table: This table summarizes current and emerging treatment options for uterine leiomyoma, including mechanisms, appropriate patient selection, expected efficacy, limitations, and suggested MAXO-aligned intervention labels. It is useful for comparing conservative, surgical, and interventional management strategies in one view.*

### Risk and Protective Factors for Uterine Leiomyoma
| Factor Type | Specific Factor | Category | Strength of Association | Population-Specific Effects | Key Evidence |
|---|---|---|---|---|---|
| Risk | Advanced reproductive age | Reproductive | Consistently reported risk factor; incidence and symptom burden increase through reproductive years, especially ages 35–50 | Burden concentrated in women aged 40–69 globally; common in reproductive-age women (tang2025theglobalburden pages 1-2, micic2024currentlyavailabletreatment pages 1-2) | Listed as a risk factor in reviews; fibroids are most commonly found in women aged 35–50, and global burden is concentrated in ages 40–69 (koltsova2023aviewon pages 1-2, tang2025theglobalburden pages 1-2, micic2024currentlyavailabletreatment pages 1-2) |
| Risk | Black/African ancestry | Genetic / population | Strong and repeatedly reported association | By age 50, prevalence reaches >80% in Black women vs ~70% overall/White women; disproportionate incidence and severity (buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2, boos2025therolesof pages 1-2) | Reviews and genomic studies report substantially higher prevalence and burden in Black women (buyukcelebi2024integratingleiomyomagenetics pages 1-2, centini2024tailoringthediagnostic pages 1-2, boos2025therolesof pages 1-2) |
| Risk | Latin American ethnicity | Population | Reported association, but less extensively quantified than Black ancestry | Mentioned as increased-risk population in review literature | Identified among risk factors in heterogeneity-focused review (koltsova2023aviewon pages 1-2) |
| Risk | Family history of uterine leiomyoma | Genetic | Moderate-to-strong; familial aggregation repeatedly reported | First-degree relatives have elevated risk; reflects heritable susceptibility | Review identifies family history as a risk factor; GWAS/integrative genetics supports heritable contribution and multiple susceptibility loci (koltsova2023aviewon pages 1-2, buyukcelebi2024integratingleiomyomagenetics pages 1-2) |
| Risk | Germline/heritable susceptibility loci | Genetic | Strong biologic evidence for susceptibility, but effect sizes vary by locus | May contribute to racial/population differences in risk | Integrative 2024 analysis identified 24 UF-associated risk loci and 394 candidate target genes, supporting inherited susceptibility (buyukcelebi2024integratingleiomyomagenetics pages 1-2) |
| Risk | MED12-associated predisposition to specific tumor biology | Genetic / molecular | Strong for tumor subtype biology rather than disease initiation alone | MED12-mutant tumors are more frequent in Black women in some series and often multiple | MED12 mutations are the dominant driver in many tumors and are associated with distinct biology and multiplicity (bulun2025uterinefibroids pages 1-5, ishikawa2023risingstarsrole pages 1-3) |
| Risk | Early menarche | Reproductive | Consistently reported risk factor | No specific population restriction given, but may interact with lifetime hormonal exposure | Included as a risk factor in multiple reviews and diagnostic overview (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Risk | Late menopause | Reproductive | Reported risk factor, likely reflecting prolonged estrogen/progesterone exposure | Not specifically stratified | Included in etiopathogenesis overview figure/discussion (alali2023theetiopathogenesisof pages 1-2) |
| Risk | Nulliparity / low parity | Reproductive | Consistently reported risk factor | Protective effect of multiparity implies higher risk in nulliparous women | Nulliparity or absence of parity is reported as a risk factor; several reviews note multiparity as protective (buyukcelebi2024integratingleiomyomagenetics pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Protective | Multiparity / parity | Reproductive | Consistently reported protective factor | Not population-specific, though effect may vary with reproductive history | Multiparity/parity reported as protective in reviews and diagnostic narrative (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2) |
| Risk | Obesity / high BMI | Lifestyle / metabolic | Strong and consistently reported | Important in many populations; cited in epidemiologic and mechanistic reviews | Obesity repeatedly listed among major risk factors and linked to symptomatic disease burden (alali2023theetiopathogenesisof pages 1-2, koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2, micic2024currentlyavailabletreatment pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Risk | Diabetes | Metabolic | Reported association | Not specifically stratified | Included among factors involved in incidence/development in clinician-friendly review (larrain2024newinsightsinto pages 1-3) |
| Risk | Arterial hypertension | Metabolic / vascular | Repeatedly reported association | Not specifically stratified | Identified as a risk factor in heterogeneity/risk-factor review and clinician review (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Risk | Chronic inflammation | Environmental / biologic | Reported association with plausible mechanistic support | Not specifically stratified | Listed as a risk factor in review of UL genesis; inflammation also emphasized mechanistically in fibroid biology (koltsova2023aviewon pages 1-2, boos2025therolesof pages 1-2) |
| Risk | Sexually transmitted infections | Infectious | Reported association, evidence less mature than hormonal/metabolic factors | Not specifically stratified | Identified as a possible risk factor in review of risk/protective factors (koltsova2023aviewon pages 1-2) |
| Risk | Exposure to xenoestrogens in early ontogenesis | Environmental | Biologically plausible and reported in review literature | Suggests early-life vulnerability window | Reported as a risk factor in review of UL genesis (koltsova2023aviewon pages 1-2) |
| Risk | Diethylstilbestrol (DES) exposure | Environmental | Reported association | Not specifically stratified | Included among environmental contributors in clinician-friendly molecular review (larrain2024newinsightsinto pages 1-3) |
| Risk | Air pollution | Environmental | Reported association | Not specifically stratified | Mentioned among factors potentially involved in incidence/development (larrain2024newinsightsinto pages 1-3) |
| Risk | Alcohol consumption | Lifestyle | Repeatedly reported risk factor | Not specifically stratified | Alcohol listed as a risk factor in heterogeneity review and clinician-friendly review (koltsova2023aviewon pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Risk | Caffeine | Lifestyle | Reported in one review/figure; likely weaker evidence than alcohol/obesity | Not specifically stratified | Included in etiopathogenesis figure as a potential risk factor (alali2023theetiopathogenesisof pages 1-2) |
| Risk | Chronic stress | Lifestyle / psychosocial | Reported association | Not specifically stratified | Listed in diagnostic review as a risk factor (centini2024tailoringthediagnostic pages 1-2) |
| Risk | Vitamin D deficiency | Environmental / nutritional | Repeatedly reported association with supportive mechanistic rationale | Not specifically stratified; may be relevant in populations with higher deficiency prevalence | Vitamin D deficiency is listed among known factors influencing fibroid development in recent reviews (alali2023theetiopathogenesisof pages 1-2, micic2024currentlyavailabletreatment pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Protective | Adequate vitamin D status | Nutritional | Implied protective factor from repeated deficiency-risk association; preclinical support exists | Not specifically stratified | Since deficiency is repeatedly associated with risk, adequate status is plausibly protective; some model literature supports anti-fibroid effects (micic2024currentlyavailabletreatment pages 1-2, wu2026preclinicalresearchplatform pages 1-2, larrain2024newinsightsinto pages 1-3) |
| Risk | High-fat diet / adverse dietary factors | Lifestyle / nutritional | Reported association | Not specifically stratified | High-fat diet and dietary factors are mentioned as contributing to incidence/development (larrain2024newinsightsinto pages 1-3) |
| Protective | Oral contraceptive use / combined oral contraceptives | Reproductive / hormonal | Reported protective factor in review literature, though literature historically mixed | Not specifically stratified | Oral contraceptive intake and combined oral contraceptives are listed among possible protective factors in recent reviews (koltsova2023aviewon pages 1-2, centini2024tailoringthediagnostic pages 1-2) |
| Protective | Smoking | Lifestyle | Reported as a possible protective factor in reviews, but likely outweighed by broader health harms | Not population-specific; not a recommended prevention strategy | Smoking is listed among possible protective factors in one recent review even though it is not clinically recommended (koltsova2023aviewon pages 1-2) |
| Risk | Hormonal milieu: higher estradiol and progesterone exposure | Hormonal / mechanistic | Strong mechanistic support | Relevant across reproductive-age populations; explains premenopausal predominance | Risk/severity associated with serum estradiol and progesterone; tumors are steroid-dependent and rarely develop before menarche (buyukcelebi2024integratingleiomyomagenetics pages 1-2, ishikawa2023risingstarsrole pages 1-3) |
| Protective | Postmenopausal state / menopause-associated regression | Reproductive / hormonal | Strong observational pattern | Applies broadly; many fibroids regress after menopause | Fibroids frequently regress after menopause, supporting reduced ovarian steroid exposure as protective against persistence/growth (alali2023theetiopathogenesisof pages 1-2, ishikawa2023risingstarsrole pages 1-3) |
| Risk | Reproductive delay / postponed childbearing | Reproductive | Epidemiologically plausible; discussed in population-burden review | Relevant in regions with delayed childbearing patterns | Population review links changing reproductive patterns, including postponed childbearing, to increasing prevalence (zhang2025globalregionaland pages 1-2) |


*Table: This table summarizes reported risk and protective factors for uterine leiomyoma across recent reviews and epidemiologic/genetic studies. It organizes the factors by category, indicates the qualitative strength of association, and notes population-specific patterns where available.*

---

## CONCLUSION

Uterine leiomyomas are the most common benign gynecological tumors, affecting up to 70–80% of women by menopause, with disproportionate burden in Black women. The disease has complex etiology involving somatic driver mutations (MED12 most common at 50–80%, followed by HMGA2, FH, and others), heritable susceptibility loci (24 GWAS risk loci identified), hormonal dependence on estrogen and progesterone, and environmental/lifestyle risk factors including obesity, early menarche, nulliparity, and vitamin D deficiency (alali2023theetiopathogenesisof pages 1-2, bulun2025uterinefibroids pages 1-5, koltsova2023aviewon pages 1-2, buyukcelebi2024integratingleiomyomagenetics pages 1-2, ishikawa2023risingstarsrole pages 1-3).

Approximately 20–30% of women with fibroids experience symptoms including heavy menstrual bleeding (leading to iron deficiency anemia), pelvic pain, bulk symptoms, and reproductive dysfunction, significantly impairing quality of life (alali2023theetiopathogenesisof pages 1-2, centini2024tailoringthediagnostic pages 1-2, vannuccini2024themodernmanagement pages 1-5). Diagnosis relies primarily on transvaginal ultrasound, with MRI for detailed characterization and treatment planning (centini2024tailoringthediagnostic pages 1-2, vannuccini2024themodernmanagement pages 1-5). Emerging AI-based radiomics and molecular subtyping (MED12 mutation status) may enable personalized treatment approaches (ishikawa2023risingstarsrole pages 1-3, vannuccini2024themodernmanagement pages 1-5).

Treatment is individualized based on symptoms, fibroid characteristics, fertility desire, and patient preference. Options range from medical management (GnRH agonists/antagonists, SPRMs, NSAIDs, tranexamic acid) to surgical interventions (myomectomy, hysterectomy) and minimally invasive procedures (UAE, HIFU, radiofrequency ablation) (micic2024currentlyavailabletreatment pages 1-2, vannuccini2024themodernmanagement pages 1-5). Novel therapies targeting molecular pathways and mutation-specific responses are under investigation (bulun2025uterinefibroids pages 1-5, micic2024currentlyavailabletreatment pages 1-2, ishikawa2023risingstarsrole pages 1-3).

Animal models including Eker rats, conditional MED12-mutant mice, hormone-induced models, and patient-derived xenografts facilitate mechanistic research and drug development (wu2026preclinicalresearchplatform pages 1-2). Future directions emphasize precision medicine leveraging molecular subtyping, multi-omics biomarkers, and non-hormonal targeted therapies to improve outcomes for this highly prevalent and morbid condition (buyukcelebi2024integratingleiomyomagenetics pages 1-2, ishikawa2023risingstarsrole pages 1-3, vannuccini2024themodernmanagement pages 1-5, boos2025therolesof pages 1-2).

References

1. (alali2023theetiopathogenesisof pages 1-2): Ola M. Alali and Mikhail I. Churnosov. The etiopathogenesis of uterine leiomyomas: a review. Gynecology, 25:22-30, Apr 2023. URL: https://doi.org/10.26442/20795696.2023.1.201827, doi:10.26442/20795696.2023.1.201827. This article has 14 citations.

2. (bulun2025uterinefibroids pages 1-5): Serdar E. Bulun, Ping Yin, JianJun Wei, Azna Zuberi, Takashi Iizuka, Takuma Suzuki, Priyanka Saini, Jyoti Goad, J. Brandon Parker, Mazhar Adli, Thomas Boyer, Debabrata Chakravarti, and Aleksandar Rajkovic. Uterine fibroids. Oct 2025. URL: https://doi.org/10.1152/physrev.00010.2024, doi:10.1152/physrev.00010.2024. This article has 44 citations and is from a highest quality peer-reviewed journal.

3. (ishikawa2023risingstarsrole pages 1-3): Hiroshi Ishikawa, Tatsuya Kobayashi, Meika Kaneko, Yoshiko Saito, Makio Shozu, and Kaori Koga. Rising stars: role of med12 mutation in the pathogenesis of uterine fibroids. Journal of Molecular Endocrinology, Sep 2023. URL: https://doi.org/10.1530/jme-23-0039, doi:10.1530/jme-23-0039. This article has 20 citations and is from a peer-reviewed journal.

4. (koltsova2023aviewon pages 1-2): Alla Koltsova, Olga Efimova, and Anna Pendina. A view on uterine leiomyoma genesis through the prism of genetic, epigenetic and cellular heterogeneity. International Journal of Molecular Sciences, 24:5752, Mar 2023. URL: https://doi.org/10.3390/ijms24065752, doi:10.3390/ijms24065752. This article has 41 citations.

5. (centini2024tailoringthediagnostic pages 1-2): Gabriele Centini, Alberto Cannoni, Alessandro Ginetti, Irene Colombi, Matteo Giorgi, Giorgia Schettini, Francesco Giuseppe Martire, Lucia Lazzeri, and Errico Zupi. Tailoring the diagnostic pathway for medical and surgical treatment of uterine fibroids: a narrative review. Sep 2024. URL: https://doi.org/10.3390/diagnostics14182046, doi:10.3390/diagnostics14182046. This article has 28 citations.

6. (larrain2024newinsightsinto pages 1-3): Demetrio Larraín and Jaime Prado. New insights into molecular pathogenesis of uterine fibroids: from the lab to a clinician-friendly review. Soft Tissue Sarcoma and Leiomyoma - Diagnosis, Management, and New Perspectives, Jan 2024. URL: https://doi.org/10.5772/intechopen.1002969, doi:10.5772/intechopen.1002969. This article has 5 citations.

7. (buyukcelebi2024integratingleiomyomagenetics pages 1-2): Kadir Buyukcelebi, Alexander J. Duval, Fatih Abdula, Hoda Elkafas, Fidan Seker-Polat, and Mazhar Adli. Integrating leiomyoma genetics, epigenomics, and single-cell transcriptomics reveals causal genetic variants, genes, and cell types. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45382-0, doi:10.1038/s41467-024-45382-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

8. (zhang2025globalregionaland pages 1-2): Zihan Zhang, Hongxin Huang, Kuanlie Jiang, Weixia Liu, Yan Xuan, and Wei Lu. Global, regional and national uterine fibroid burdens from 1990 to 2021 and projections until 2050: results from the gbd study. BMC Women's Health, Sep 2025. URL: https://doi.org/10.1186/s12905-025-03974-y, doi:10.1186/s12905-025-03974-y. This article has 6 citations.

9. (micic2024currentlyavailabletreatment pages 1-2): Jelena Micić, Maja Macura, Mladen Andjić, Katarina Ivanović, Jelena Dotlić, Dušan D. Micić, Vladimir Arsenijević, Jelena Stojnić, Jovan Bila, Sandra Babić, Una Šljivančanin, Danka Mostić Stanišić, and Milan Dokić. Currently available treatment modalities for uterine fibroids. Medicina, 60:868, May 2024. URL: https://doi.org/10.3390/medicina60060868, doi:10.3390/medicina60060868. This article has 79 citations.

10. (tang2025theglobalburden pages 1-2): Wei-Zhen Tang, Qin-Yu Cai, Kang-Jin Huang, Wei-Ze Xu, Jia-Zheng Li, Yun-Ren Pan, Hong-Yu Xu, Yi-Fan Zhao, Ting-He Sheng, Zhi-Mou Li, Tai-Hang Liu, and Ying-Bo Li. The global burden of polycystic ovary syndrome, endometriosis, uterine fibroids, cervical cancer, uterine cancer, and ovarian cancer from 1990 to 2021. BMC Public Health, May 2025. URL: https://doi.org/10.1186/s12889-025-22881-3, doi:10.1186/s12889-025-22881-3. This article has 39 citations and is from a peer-reviewed journal.

11. (chuang2023differentialexpressionof pages 1-2): Tsai-Der Chuang, Jianjun Gao, Derek Quintanilla, Hayden McSwiggin, Drake Boos, Wei Yan, and Omid Khorram. Differential expression of med12-associated coding rna transcripts in uterine leiomyomas. International Journal of Molecular Sciences, 24:3742, Feb 2023. URL: https://doi.org/10.3390/ijms24043742, doi:10.3390/ijms24043742. This article has 18 citations.

12. (dundr2022uterinecellularleiomyomas pages 1-2): Pavel Dundr, Mária Gregová, Jan Hojný, Eva Krkavcová, Romana Michálková, Kristýna Němejcová, Michaela Bártů, Nikola Hájková, Jan Laco, Michal Mára, Adéla Richtárová, Tomáš Zima, and Ivana Stružinská. Uterine cellular leiomyomas are characterized by common hmga2 aberrations, followed by chromosome 1p deletion and med12 mutation: morphological, molecular, and immunohistochemical study of 52 cases. Virchows Archiv, 480:281-291, Oct 2022. URL: https://doi.org/10.1007/s00428-021-03217-z, doi:10.1007/s00428-021-03217-z. This article has 27 citations and is from a peer-reviewed journal.

13. (boos2025therolesof pages 1-2): Drake Boos, Tsai-Der Chuang, and Omid Khorram. The roles of non-coding rnas in the pathogenesis of uterine fibroids. Cells, 14:1290, Aug 2025. URL: https://doi.org/10.3390/cells14161290, doi:10.3390/cells14161290. This article has 7 citations.

14. (wu2026preclinicalresearchplatform pages 1-2): Dan Wu, Jian Luo, Li‐Yu Lin, Tingting Gu, and Zhehui You. Preclinical research platform for uterine leiomyoma: construction optimization and selection of animal models. Frontiers in Veterinary Science, Feb 2026. URL: https://doi.org/10.3389/fvets.2026.1772750, doi:10.3389/fvets.2026.1772750. This article has 1 citations and is from a peer-reviewed journal.

15. (vannuccini2024themodernmanagement pages 1-5): Silvia Vannuccini, Felice Petraglia, Francisco Carmona, Joaquim Calaf, and Charles Chapron. The modern management of uterine fibroids-related abnormal uterine bleeding. Fertility and Sterility, 122:20-30, Jul 2024. URL: https://doi.org/10.1016/j.fertnstert.2024.04.041, doi:10.1016/j.fertnstert.2024.04.041. This article has 103 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Uterine_Leiomyoma-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Uterine_Leiomyoma-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Uterine_Leiomyoma-deep-research-falcon_artifacts/artifact-02.md)