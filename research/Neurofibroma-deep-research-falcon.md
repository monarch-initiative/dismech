---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T09:05:21.609644'
end_time: '2026-06-30T09:35:29.859157'
duration_seconds: 1808.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurofibroma
  mondo_id: ''
  category: Neoplastic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 62
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Neurofibroma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Neurofibroma-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Neurofibroma-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurofibroma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Neurofibroma** covering all of the
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
- **Disease Name:** Neurofibroma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Neurofibroma** covering all of the
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


# Comprehensive Research Report: Neurofibroma

## 1. Disease Information

### Overview
Neurofibroma is a benign peripheral nerve sheath tumor (PNST) composed predominantly of Schwann cells, fibroblasts, perineurial-like cells, mast cells, and extracellular matrix, arising in the context of neurofibromatosis type 1 (NF1), the most common tumor predisposition syndrome (sur2022neurofibromatosisinchildren pages 1-2, mo2022neurofibrominandsuppression pages 1-3). NF1 is an autosomal dominant neurocutaneous disorder caused by germline pathogenic variants in the *NF1* gene on chromosome 17q11.2, which encodes neurofibromin, a tumor suppressor protein functioning as a negative regulator of RAS signaling (kitsera2026moleculargeneticsand pages 2-3, anastasaki2022rasandbeyond pages 2-3). Neurofibromas represent the hallmark neoplastic manifestation of NF1 and include several histopathologically and clinically distinct subtypes: cutaneous neurofibromas (cNF), plexiform neurofibromas (pNF), subcutaneous neurofibromas, and diffuse neurofibromas (sur2022neurofibromatosisinchildren pages 2-4, yu2025emergingmechanismand pages 2-4, imataka2025neurofibromatosistype1 pages 4-5).

### Key Identifiers
The following table summarizes key disease identifiers and characteristics:

| Disease name | MONDO ID | OMIM | Orphanet | ICD-10 / ICD-11 | MeSH | Common synonyms | Inheritance pattern | Prevalence | Incidence | Causal gene | Chromosome location | Protein product | Key pathway |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Neurofibroma | MONDO:0016755 | Not established for neurofibroma as a standalone entity; commonly contextualized within NF1 | Not established for isolated neurofibroma in the gathered evidence | ICD-10: D36.1 (benign neoplasm of peripheral nerves and autonomic nervous system); ICD-11: peripheral nerve sheath benign neoplasm category, exact code not established here | MeSH term used for neurofibroma exists, but identifier not established in gathered evidence | Peripheral nerve sheath tumor; cutaneous neurofibroma; dermal neurofibroma; plexiform neurofibroma; diffuse neurofibroma | Usually occurs in the setting of NF1, which is autosomal dominant with many de novo cases; tumor formation follows a somatic second-hit mechanism in NF1-deficient Schwann lineage cells (sur2022neurofibromatosisinchildren pages 1-2, anastasaki2022rasandbeyond pages 2-3) | NF1 pooled prevalence: 1 in 3,164 (95% CI 1 in 2,132-1 in 4,712); nearly all adults with NF1 develop cutaneous neurofibromas, and 30-50% develop plexiform neurofibromas (lee2023incidenceandprevalence pages 1-2, yu2025emergingmechanismand pages 2-4) | NF1 pooled birth incidence: 1 in 2,662 (95% CI 1 in 1,968-1 in 3,601) (lee2023incidenceandprevalence pages 1-2, lee2023incidenceandprevalence pages 2-4) | NF1 (neurofibromin 1) (kitsera2026moleculargeneticsand pages 2-3, mo2022neurofibrominandsuppression pages 1-3, anastasaki2022rasandbeyond pages 2-3) | 17q11.2 (sur2022neurofibromatosisinchildren pages 1-2, hussain2024roleoflong pages 3-5) | Neurofibromin, a ~2818 aa RAS-GTPase-activating tumor suppressor (kitsera2026moleculargeneticsand pages 2-3, mo2022neurofibrominandsuppression pages 1-3, anastasaki2022rasandbeyond pages 2-3) | RAS/MAPK is the core dysregulated pathway; PI3K/AKT/mTOR is also activated downstream of NF1 loss (kitsera2026moleculargeneticsand pages 2-3, anastasaki2022rasandbeyond pages 2-3, lu2025neurofibromatosistype1 pages 2-4, OpenTargets Search: neurofibroma) |


*Table: This table summarizes key disease identifiers and high-yield characteristics for neurofibroma, emphasizing its close relationship to NF1-associated tumor biology. It is useful as a compact reference for ontology mapping, epidemiology, and molecular annotation.*

- **MONDO ID:** MONDO:0016755 (neurofibroma); MONDO:0018975 (neurofibromatosis type 1) (OpenTargets Search: neurofibroma)
- **OMIM:** 162200 (Neurofibromatosis type 1)
- **ICD-10:** D36.1 (Benign neoplasm of peripheral nerves and autonomic nervous system)
- **MeSH:** D009455 (Neurofibroma)
- **Synonyms:** Peripheral nerve sheath tumor, dermal neurofibroma, cutaneous neurofibroma, plexiform neurofibroma, von Recklinghausen disease-associated tumor

---

## 2. Etiology

### Disease Causal Factors
Neurofibroma formation is driven by biallelic inactivation of the *NF1* tumor suppressor gene following a classic Knudson two-hit model. Patients inherit one germline loss-of-function *NF1* variant, and tumor initiation requires somatic loss of the remaining wild-type allele (loss of heterozygosity) in Schwann cell lineage progenitors (anastasaki2022rasandbeyond pages 2-3, lu2025neurofibromatosistype1 pages 2-4). Over 3,000 pathogenic *NF1* variants have been documented, with more than 80% producing truncated, non-functional neurofibromin protein (lu2025neurofibromatosistype1 pages 2-4).

### Genetic Risk Factors
- **Causal gene:** *NF1* (neurofibromin 1), chromosome 17q11.2 (kitsera2026moleculargeneticsand pages 2-3, hussain2024roleoflong pages 3-5)
- **Variant types:** Nonsense, frameshift, splice-site, missense mutations, intragenic deletions, whole-gene (microdeletion) deletions (kitsera2026moleculargeneticsand pages 2-3, hussain2024roleoflong pages 3-5)
- **17q11.2 microdeletion syndrome:** Large deletions encompassing the *NF1* gene and flanking regions (5–10% of cases), associated with more severe phenotypes including earlier plexiform neurofibroma development and developmental delay (kitsera2026moleculargeneticsand pages 2-3, hussain2024roleoflong pages 3-5, peduto2023neurofibromatosistype1 pages 11-13)
- **De novo mutations:** Approximately 50% of cases arise from de novo *NF1* mutations (sur2022neurofibromatosisinchildren pages 1-2)
- **Modifier genes:** *SPRED1* has been identified as an NF1-related pathway gene with association scores in OpenTargets (OpenTargets Search: neurofibroma)

### Environmental Risk Factors
Radiation exposure is a recognized risk factor for malignant transformation (MPNST development) but is not considered a primary risk factor for benign neurofibroma formation (yao2023malignantperipheralnerve pages 2-4). Nerve injury may serve as a trigger for neurofibroma development, as demonstrated in animal models where sciatic nerve injury induced plexiform neurofibroma formation in NPcis mice (plante2024revisitingthenpcis pages 8-11, plante2024revisitingthenpcis pages 1-2).

---

## 3. Phenotypes

### Clinical Manifestations of NF1 (with HPO term suggestions)
NF1 presents with multisystem manifestations that appear in an age-dependent manner (lalvani2024neurofibromatosistype1 pages 1-2, imataka2025neurofibromatosistype1 pages 2-4).

**Cutaneous/Pigmentary Features:**
- **Café-au-lait macules (CALMs):** Present in ~85–95% of patients, appearing at birth or in early infancy as flat tan-brown hyperpigmented lesions (≥6 spots of ≥5 mm pre-pubertal or ≥15 mm post-pubertal). HPO: HP:0007565 (lalvani2024neurofibromatosistype1 pages 1-2, almuqbil2024epidemiologyandoutcomes pages 1-2, almuqbil2024epidemiologyandoutcomes pages 5-7)
- **Axillary/inguinal freckling (Crowe sign):** Present in ~34.8% of patients, typically developing after age 5. HPO: HP:0001067 (almuqbil2024epidemiologyandoutcomes pages 5-7, peduto2023neurofibromatosistype1 pages 2-4)

**Ophthalmologic Features:**
- **Iris Lisch nodules:** Melanocytic hamartomas present in ~36.4% of patients at a median age of 12 years. HPO: HP:0009737 (almuqbil2024epidemiologyandoutcomes pages 1-2, almuqbil2024epidemiologyandoutcomes pages 5-7)
- **Optic pathway gliomas:** Found in ~36.4% in one multicenter study, typically diagnosed within the first decade of life. HPO: HP:0009734 (almuqbil2024epidemiologyandoutcomes pages 1-2)

**Tumor Features:**
- **Cutaneous neurofibromas:** Skin tumors originating from cutaneous nerves, forming small rubbery nodules, affecting nearly all adult NF1 patients (>90%). HPO: HP:0001067 (yu2025emergingmechanismand pages 2-4, imataka2025neurofibromatosistype1 pages 4-5)
- **Plexiform neurofibromas:** Complex tumors arising from large internal nerve plexuses, occurring in 30–60% of NF1 patients, often congenital, with ~15% risk of malignant transformation. HPO: HP:0009732 (yu2025emergingmechanismand pages 2-4, imataka2025neurofibromatosistype1 pages 4-5, busciglio2025thepathogenesisof pages 1-2)

**Skeletal Abnormalities:**
- Dystrophic scoliosis (up to 30%), sphenoid wing dysplasia, tibial bowing, pseudoarthrosis. HPO: HP:0002650 (scoliosis), HP:0009736 (tibial pseudoarthrosis) (almuqbil2024epidemiologyandoutcomes pages 2-4, imataka2025neurofibromatosistype1 pages 2-4, imataka2025neurofibromatosistype1 pages 4-5)

**Neurodevelopmental Features:**
- Cognitive deficits in approximately 70% of children, including learning disabilities (20.9%), communication disorders (33.8%), ADHD (4.9%), and intellectual disability (10.5%). HPO: HP:0001328 (specific learning disability), HP:0007018 (attention deficit) (almuqbil2024epidemiologyandoutcomes pages 1-2, almuqbil2024epidemiologyandoutcomes pages 5-7, sur2022neurofibromatosisinchildren pages 2-4)

**Cardiovascular Features:**
- Cardiovascular abnormalities in 9.8%, including hypertension, congenital heart defects, and moyamoya syndrome (almuqbil2024epidemiologyandoutcomes pages 1-2, imataka2025neurofibromatosistype1 pages 4-5)

### Quality of Life Impact
NF1 imposes significant quality-of-life burden. In a Chinese cohort study, pediatric NF1 patients had EQ-5D-Y utility scores of 0.880 ± 0.13 (VAS 75.38 ± 20.67), while adult patients had EQ-5D-5L utility scores of 0.843 ± 0.17 (VAS 72.32 ± 23.49). Over 50% of both groups reported problems with pain/discomfort, and 42.9–74.3% reported anxiety/depression (liang2024longtermdistressthroughout pages 1-2, liang2024longtermdistressthroughout pages 4-5). Pain occurs at young ages in 41% of patients requiring medication (sur2022neurofibromatosisinchildren pages 2-4).

---

## 4. Genetic/Molecular Information

### Causal Gene: *NF1* (Neurofibromin 1)
- **HGNC:** HGNC:7765
- **Ensembl:** ENSG00000196712
- **Chromosome:** 17q11.2
- **Protein:** Neurofibromin, a 2,818-amino acid protein with RAS-GTPase-activating protein (RAS-GAP) activity (kitsera2026moleculargeneticsand pages 2-3, mo2022neurofibrominandsuppression pages 1-3, lu2025neurofibromatosistype1 pages 2-4)

### Pathogenic Variants
The *NF1* gene is one of the largest in the human genome (~350 kb, 60 exons). Pathogenic variants span the entire gene, with over 3,000 documented mutations (lu2025neurofibromatosistype1 pages 2-4):
- **90–95%** are intragenic mutations (nonsense, frameshift, splice-site, missense) (peduto2023neurofibromatosistype1 pages 11-13)
- **5–10%** involve large deletions (17q11.2 microdeletion syndrome) associated with more severe phenotypes (hussain2024roleoflong pages 3-5, peduto2023neurofibromatosistype1 pages 11-13)
- Mutation types include small/large insertions, deletions, chromosome rearrangements, stop mutations, splicing mutations, and amino acid substitutions (hussain2024roleoflong pages 3-5)
- **Functional consequence:** Loss of function (>80% produce truncated protein) (lu2025neurofibromatosistype1 pages 2-4)
- **Somatic vs germline:** Germline heterozygous mutation plus somatic second hit (biallelic inactivation) required for tumor formation (anastasaki2022rasandbeyond pages 2-3, lu2025neurofibromatosistype1 pages 2-4)

### Genotype-Phenotype Correlations
Five key genotype-phenotype correlations have been identified (peduto2023neurofibromatosistype1 pages 11-13):
- 17q11.2 microdeletion syndrome → more severe disease, earlier tumor onset
- Missense variants at codons 844–848 (GRD) → severe phenotype with early tumor development (kitsera2026moleculargeneticsand pages 2-3)
- Mutations in the CSRD domain → increased optic glioma risk (mo2022neurofibrominandsuppression pages 1-3, mo2022neurofibrominandsuppression pages 19-21)
- p.Met992del → milder phenotype
- p.Arg1809 substitutions → Noonan-like features (peduto2023neurofibromatosistype1 pages 11-13)

### Malignant Transformation: Neurofibroma-to-MPNST Continuum
Malignant transformation follows a stepwise molecular cascade (busciglio2025thepathogenesisof pages 2-4, busciglio2025thepathogenesisof pages 1-2, busciglio2025thepathogenesisof pages 4-6):
1. **Biallelic NF1 inactivation** → constitutive RAS activation → benign neurofibroma
2. **CDKN2A/B loss** → ANNUBP (atypical neurofibromatous neoplasm of uncertain biological potential)
3. **PRC2 disruption** (SUZ12, EED, or EZH2 mutations/deletions) → H3K27me3 loss → high-grade MPNST

PRC2 inactivation occurs in 70–90% of MPNSTs and represents a defining molecular event, causing global epigenetic dysregulation and enhancer reprogramming (yao2023malignantperipheralnerve pages 2-4, busciglio2025thepathogenesisof pages 6-7). This leads to Schwann cell dedifferentiation, chromosomal instability, and immune-depleted microenvironments (busciglio2025thepathogenesisof pages 14-14, busciglio2025thepathogenesisof pages 10-12).

### Epigenetic Information
DNA methylation profiling has emerged as a diagnostic tool for MPNST classification, with distinct methylation clusters corresponding to H3K27me3 status (busciglio2025thepathogenesisof pages 14-14, busciglio2025thepathogenesisof pages 10-12). LncRNAs including ANRIL and H19 show dysregulated expression in NF, influencing RAS/MAPK and JAK/STAT signaling pathways (hussain2024roleoflong pages 3-5).

---

## 5. Mechanism / Pathophysiology

### Molecular Pathways
Loss of neurofibromin function leads to constitutive activation of multiple oncogenic signaling cascades (kitsera2026moleculargeneticsand pages 2-3, anastasaki2022rasandbeyond pages 2-3, lu2025neurofibromatosistype1 pages 2-4):
- **RAS/RAF/MEK/ERK (MAPK) pathway** – primary proliferative signal; GO: GO:0000165 (MAPK cascade)
- **PI3K/AKT/mTOR pathway** – survival and growth signaling
- **cAMP pathway** – modulates differentiation and growth
- **RAS-Rac1 pathway** – cytoskeletal regulation and cell migration

Neurofibromin normally converts active RAS-GTP to inactive RAS-GDP through its GAP-related domain (GRD), restraining downstream signaling (kitsera2026moleculargeneticsand pages 2-3, anastasaki2022rasandbeyond pages 2-3).

### Cellular Processes
- **Cell of origin:** NF1-deficient Schwann cell precursors (SOX10+) from the neural crest lineage; CL: CL:0002573 (Schwann cell precursor) (mo2025humanizedneurofibromamodel pages 1-2)
- NF1 loss impairs Schwann cell differentiation, inducing a persistent stem-like state that expands the progenitor pool required for tumor initiation (mo2025humanizedneurofibromamodel pages 1-2)
- A glial-to-mesenchymal transition occurs during malignant transformation, with SOX9 identified as a marker of this transition (busciglio2025thepathogenesisof pages 10-12)

### Tumor Microenvironment
Single-cell RNA sequencing has revealed the remarkable complexity of the neurofibroma tumor microenvironment (TME):
- **Schwann cells** represent only ~4–10% of tumor cells in pNF, while **immune and stromal cells comprise ~90% of human plexiform neurofibromas** (kershner2022multiplenf1schwann pages 1-2, mclean2023singlecellrnasequencing pages 5-6)
- Five distinct SC populations have been identified, including a novel SC progenitor-like (SCP-like) population (kershner2022multiplenf1schwann pages 1-2)
- **Macrophages** (Iba1+CD11b+F4/80+) comprise ~30% of pNF cells with M2-polarized phenotype promoting immunosuppression (kershner2022multiplenf1schwann pages 1-2, mclean2023singlecellrnasequencing pages 11-13)
- **Fibroblasts** form the collagen-rich matrix (CD34+), with six distinct populations identified, comprising over 70% of analyzed cells in porcine models (mclean2023singlecellrnasequencing pages 14-15, mclean2023singlecellrnasequencing pages 5-6)
- **Key cell-cell communication pathways:** PROS1-AXL, FGF-FGFR, MIF-CD74, NF-κB, PTN-PTPRZ1, NRXN1-NLGN1, and collagen/laminin-integrin interactions (kershner2022multiplenf1schwann pages 1-2, swanson2025singlecellanalysisof pages 12-15)
- **Immunosuppressive features:** IDO1+/PD-L1+ dendritic cells, M2 macrophages expressing IL-10 and ARG1, and Schwann cell-derived IL-34 promoting CSF1R-mediated M2 polarization (mclean2023singlecellrnasequencing pages 11-13, mclean2023singlecellrnasequencing pages 14-15)

### Molecular Profiling
Single-nuclei RNA-sequencing integrated with spatial transcriptomics has identified distinct cellular subpopulations with remarkable inter-sample homogeneity, with the predominant fraction being fibroblast subtypes and NRXN1/NLGN1 receptor-ligand cross-talk predicted between fibroblasts and non-myelinated Schwann cells (swanson2025singlecellanalysisof pages 25-27, swanson2025singlecellanalysisof pages 12-15).

---

## 6. Anatomical Structures Affected

### Organ Level
- **Primary:** Peripheral nervous system (peripheral nerves, nerve plexuses); UBERON: UBERON:0000010 (peripheral nervous system)
- **Secondary:** Skin (cutaneous neurofibromas), bone, eye, brain, cardiovascular system
- **Body systems:** Nervous, integumentary, skeletal, cardiovascular, endocrine (lalvani2024neurofibromatosistype1 pages 1-2, imataka2025neurofibromatosistype1 pages 2-4)

### Tissue and Cell Level
- **Schwann cells** (CL: CL:0002573) – neoplastic driver cells
- **Fibroblasts** (CL: CL:0000057) – major stromal component
- **Macrophages** (CL: CL:0000235) – M2-polarized, immunosuppressive
- **Mast cells** (CL: CL:0000097) – present at low abundance
- **Endothelial cells, pericytes, T cells** – TME components (kershner2022multiplenf1schwann pages 1-2, mclean2023singlecellrnasequencing pages 5-6)

### Localization
- Cutaneous neurofibromas: dermal layer, associated with cutaneous nerves (UBERON: UBERON:0002067, skin of body)
- Plexiform neurofibromas: deep nerve plexuses (brachial, lumbosacral, paraspinal); UBERON: UBERON:0001030 (nerve plexus)
- Subcutaneous neurofibromas: trunk, arms, face (yu2025emergingmechanismand pages 2-4, imataka2025neurofibromatosistype1 pages 4-5)

---

## 7. Temporal Development

### Onset
- NF1 has 100% penetrance with age-dependent manifestation (imataka2025neurofibromatosistype1 pages 2-4)
- CALMs appear at birth/infancy; freckling after age 5; Lisch nodules by adolescence
- **Plexiform neurofibromas:** Many diagnosed before age 5, suggesting congenital origin (yu2025emergingmechanismand pages 2-4)
- **Cutaneous neurofibromas:** Typically emerge during puberty and increase throughout life (yu2025emergingmechanismand pages 2-4, imataka2025neurofibromatosistype1 pages 4-5)
- Median age at NF1 diagnosis: 11 years (almuqbil2024epidemiologyandoutcomes pages 1-2)

### Progression
- Benign neurofibromas are generally slow-growing and clinically stable
- Plexiform neurofibromas carry 8–15% lifetime risk of malignant transformation to MPNST (imataka2025neurofibromatosistype1 pages 4-5, busciglio2025thepathogenesisof pages 1-2)
- MPNST represents the most common cause of death in NF1 patients, with high recurrence rates (30–70%) after surgical resection and resistance to chemotherapy (busciglio2025thepathogenesisof pages 1-2)

### Prognosis
- Benign neurofibromas: generally good prognosis; significant morbidity from pain, disfigurement, and neurological deficits
- MPNST: poor prognosis with median survival of 11 months and 5-year survival rate as low as 6.8% for radiation-induced cases (yao2023malignantperipheralnerve pages 2-4)
- High-grade PRC2/CDKN2A-deficient MPNSTs show significantly poorer survival (p = 0.0024) (busciglio2025thepathogenesisof pages 14-14)

---

## 8. Inheritance and Population

### Epidemiology
A 2023 systematic review and meta-analysis of 12 studies reported (lee2023incidenceandprevalence pages 1-2, lee2023incidenceandprevalence pages 2-4, lee2023incidenceandprevalence pages 4-7):
- **Pooled NF1 prevalence:** 1 in 3,164 (95% CI: 1 in 2,132–1 in 4,712)
- **Pooled NF1 birth incidence:** 1 in 2,662 (95% CI: 1 in 1,968–1 in 3,601)
- Screening studies identified higher prevalence (1 in 2,020) compared to medical record-based studies (1 in 4,329), suggesting significant under-recognition

### Inheritance
- **Pattern:** Autosomal dominant (sur2022neurofibromatosisinchildren pages 1-2)
- **Penetrance:** 100% (complete) by adulthood (imataka2025neurofibromatosistype1 pages 2-4)
- **Expressivity:** Highly variable, even within families carrying identical mutations (lalvani2024neurofibromatosistype1 pages 1-2)
- **De novo mutations:** ~50% of cases (sur2022neurofibromatosisinchildren pages 1-2)
- **Sex ratio:** No gender predilection reported (sur2022neurofibromatosisinchildren pages 2-4)

---

## 9. Diagnostics

### Clinical Criteria
The 2021 revised NIH diagnostic criteria for NF1 require ≥2 of the following (almuqbil2024epidemiologyandoutcomes pages 1-2, almuqbil2024epidemiologyandoutcomes pages 2-4, imataka2025neurofibromatosistype1 pages 2-4):
- ≥6 CALMs (≥5 mm pre-pubertal, ≥15 mm post-pubertal)
- ≥2 neurofibromas of any type or one plexiform neurofibroma
- Axillary or inguinal freckling
- Optic pathway glioma
- ≥2 Lisch nodules or ≥2 choroidal abnormalities
- Distinctive osseous lesion (sphenoid dysplasia, tibial bowing/pseudoarthrosis)
- Heterozygous pathogenic *NF1* variant
- First-degree relative with NF1

### Genetic Testing
Molecular analysis of the *NF1* gene is fundamental for confirming diagnosis, especially in cases with atypical or incomplete clinical features, and for distinguishing from Legius syndrome (*SPRED1* mutations) (peduto2023neurofibromatosistype1 pages 2-4). Sequencing approaches include next-generation sequencing panels, whole-exome, or whole-genome sequencing. Differential diagnosis includes Legius syndrome and other RASopathies (peduto2023neurofibromatosistype1 pages 2-4).

### Imaging
Volumetric MRI is the standard for assessment of plexiform neurofibromas, used for both initial evaluation and monitoring treatment response (≥20% volume decrease defines partial response) (armstrong2023treatmentdecisionsand pages 2-4).

### Biomarkers for Malignant Transformation
Circulating tumor DNA (ctDNA) analyses reveal distinctive copy number variations and methylation patterns that can detect malignant transformation (busciglio2025thepathogenesisof pages 1-2). H3K27me3 loss by immunohistochemistry is a highly sensitive marker for MPNST pathogenesis (yao2023malignantperipheralnerve pages 2-4). A 50-protein plasma panel has been identified that accurately distinguishes MPNST from premalignant tumors (from single-cell TME profiling-informed proteomic studies) (OpenTargets Search: neurofibroma).

---

## 10. Treatment

### Current Treatment Landscape
The following table summarizes the therapeutic landscape for neurofibroma:

| Therapy | Class / mechanism | Main indication in neurofibroma | Key clinical results | FDA approval status | Notable adverse effects / limitations |
|---|---|---|---|---|---|
| Selumetinib | MEK1/2 inhibitor; suppresses RAF-MEK-ERK signaling downstream of NF1 loss | Symptomatic, inoperable NF1-associated plexiform neurofibromas (PN), primarily pediatric | Phase II: 68% confirmed partial response (34/50), median best tumor volume reduction 27.9%; Phase I/II long-term follow-up: 70% overall confirmed partial response with durable pain improvement; systematic review cites ~68-71% partial response (armstrong2023treatmentdecisionsand pages 2-4, souza2022clinicaltrialstargeting pages 5-6, souza2022clinicaltrialstargeting pages 9-10, imataka2025neurofibromatosistype1 pages 9-11) | FDA approved in 2020 for pediatric patients with symptomatic, inoperable NF1-PN; also supported by approval-linked Open Targets evidence for MAP2K1/MAP2K2 (souza2022clinicaltrialstargeting pages 5-6, armstrong2023treatmentdecisionsand pages 2-4, OpenTargets Search: neurofibroma) | Rash, vomiting, diarrhea, nausea, fatigue; grade 3 adverse events reported; cardiomyopathy and ocular toxicity require monitoring; prolonged therapy often needed because tumors may regrow after discontinuation (imataka2025neurofibromatosistype1 pages 12-13, imataka2025neurofibromatosistype1 pages 9-11) |
| Mirdametinib | MEK inhibitor | NF1-associated plexiform neurofibromas, including symptomatic/inoperable disease | Partial response reported in 42-50% of patients, with improvements in pain and functioning in trial summaries/reviews (armstrong2023treatmentdecisionsand pages 6-7, souza2022clinicaltrialstargeting pages 6-7, souza2022clinicaltrialstargeting pages 9-10) | FDA approved in 2024 for NF1 with symptomatic plexiform neurofibromas according to current treatment reviews and user-specified latest landscape; active studies ongoing (armstrong2023treatmentdecisionsand pages 6-7, souza2022clinicaltrialstargeting pages 6-7) | Acneiform rash very common (~94.7% in one study summary), nausea, diarrhea; some patients required dose reductions; class toxicities similar to other MEK inhibitors (armstrong2023treatmentdecisionsand pages 6-7, souza2022clinicaltrialstargeting pages 6-7) |
| Trametinib | MEK inhibitor | Investigational treatment for NF1-associated plexiform neurofibromas, including pediatric populations | Studied in children aged 1-17 years; efficacy signal noted in reviews, but no pivotal response rate as established as selumetinib in the cited evidence (armstrong2023treatmentdecisionsand pages 6-7, armstrong2023treatmentdecisionsand pages 2-4) | Not FDA approved specifically for neurofibroma / NF1-PN in cited evidence | Dermatologic and gastrointestinal class toxicities expected; long-term comparative efficacy remains uncertain (armstrong2023treatmentdecisionsand pages 6-7, imataka2025neurofibromatosistype1 pages 7-9) |
| Binimetinib | MEK inhibitor | Investigational therapy for NF1-associated plexiform neurofibromas | Included in ongoing/previous clinical development programs for NF1-PN; no definitive response rate provided in the gathered evidence excerpt (souza2022clinicaltrialstargeting pages 5-6, armstrong2023treatmentdecisionsand pages 2-4) | Not FDA approved specifically for neurofibroma / NF1-PN in cited evidence | MEK inhibitor class toxicities likely, including rash and gastrointestinal events; evidence still emerging (souza2022clinicaltrialstargeting pages 5-6, imataka2025neurofibromatosistype1 pages 7-9) |
| Cabozantinib | Multikinase tyrosine kinase inhibitor | Unresectable, progressive, or symptomatic NF1-associated plexiform neurofibromas, especially adolescents/adults | Partial response in 42% of patients; associated with pain reduction in reported studies/reviews (armstrong2023treatmentdecisionsand pages 6-7, souza2022clinicaltrialstargeting pages 6-7, souza2022clinicaltrialstargeting pages 9-10) | Not FDA approved specifically for neurofibroma / NF1-PN in cited evidence | Fatigue, gastrointestinal effects, hypothyroidism, dermatologic toxicities; used investigationally (armstrong2023treatmentdecisionsand pages 6-7) |
| NFX-179 topical gel | Topical, metabolically labile MEK inhibitor | Cutaneous neurofibromas (cNF) in NF1 | Phase 2a: dose-dependent MEK inhibition with 47% reduction in p-ERK at 0.5%; 20% of treated cNFs had >=50% volume reduction vs 6% with vehicle after 28 days (OpenTargets Search: neurofibroma) | Not FDA approved in cited evidence | No local or systemic toxicities observed during short treatment period; systemic levels remained <1 ng/mL; durability still under study (OpenTargets Search: neurofibroma) |
| Imatinib | Tyrosine kinase inhibitor | Investigational treatment for plexiform neurofibromas | Reported median tumor volume reduction of 26.5% in review summaries; explored before MEK inhibitors became standard (imataka2025neurofibromatosistype1 pages 7-9, imataka2025neurofibromatosistype1 pages 9-11) | Not FDA approved specifically for neurofibroma / NF1-PN in cited evidence | Limited efficacy compared with MEK inhibitors; off-target toxicities typical of TKIs; not current standard of care (imataka2025neurofibromatosistype1 pages 7-9) |
| Surgical resection / debulking | Operative removal of tumor; potentially curative if complete excision feasible | Symptomatic cutaneous or plexiform neurofibromas causing pain, neurologic deficit, disfigurement, airway compromise, or orthopedic complications | Remains standard and only potentially curative local option, but many PN are unresectable; regrowth after surgery ranges ~20-68% depending on extent of resection (armstrong2023treatmentdecisionsand pages 6-7, armstrong2023treatmentdecisionsand pages 2-4) | Standard clinical practice, not an FDA-regulated drug approval question | Risks include bleeding, neurologic injury, incomplete resection, recurrence/regrowth, and anatomic inaccessibility (armstrong2023treatmentdecisionsand pages 6-7, armstrong2023treatmentdecisionsand pages 2-4, imataka2025neurofibromatosistype1 pages 7-9) |
| Gene therapy approaches | Experimental gene restoration / editing strategies, including AAV-based NF1 restoration concepts | Future disease-modifying therapy for NF1-associated neurofibromas and related tumors | Preclinical/early translational only in gathered evidence; recent reviews highlight AAV-based gene therapy, gene-targeted approaches, and humanized/iPSC models to enable testing (lu2025neurofibromatosistype1 pages 2-4, mo2025humanizedneurofibromamodel pages 1-2) | No FDA-approved gene therapy for neurofibroma in cited evidence | Major limitations include delivery of the large NF1 gene, durability, tumor heterogeneity, and need for robust preclinical validation (lu2025neurofibromatosistype1 pages 2-4, mo2025humanizedneurofibromamodel pages 1-2) |


*Table: This table summarizes current and emerging treatments for neurofibroma, especially NF1-associated plexiform and cutaneous neurofibromas. It highlights mechanisms, indications, response rates, approval status, and key safety considerations to support knowledge base curation and comparative review.*

### Pharmacotherapy
**Selumetinib** (KOSELUGO®) is the first FDA-approved medical therapy for NF1-associated symptomatic, inoperable plexiform neurofibromas in pediatric patients aged ≥2 years. The pivotal SPRINT trial demonstrated a 68% confirmed partial response rate (34/50 patients) with median tumor volume reduction of 27.9% from baseline (armstrong2023treatmentdecisionsand pages 2-4). Long-term follow-up showed durable responses: 70% overall confirmed partial response with sustained pain improvement beyond 5 years of treatment (imataka2025neurofibromatosistype1 pages 9-11). Quality of life improved in 70% and pain reduced in 85% of patients with baseline pain (imataka2025neurofibromatosistype1 pages 9-11). The standard dosage is 25 mg/m² orally twice daily (imataka2025neurofibromatosistype1 pages 9-11).

**Mirdametinib** achieved 42–50% partial response rates with significant improvements in pain and functioning (armstrong2023treatmentdecisionsand pages 6-7, souza2022clinicaltrialstargeting pages 6-7).

**NFX-179 Topical Gel**, a metabolically labile MEK inhibitor for cutaneous neurofibromas, demonstrated dose-dependent MEK inhibition with a 47% decrease in p-ERK levels in a phase 2a trial, with excellent safety and no systemic toxicity (OpenTargets Search: neurofibroma).

### Drug Targets (OpenTargets)
OpenTargets analysis identified the following validated drug targets for neurofibroma (MONDO:0016755) with association scores (OpenTargets Search: neurofibroma):
- **NF1** (neurofibromin 1) – score 0.699
- **MAP2K1** (MEK1) – score 0.535 (clinical stage: APPROVAL)
- **MAP2K2** (MEK2) – score 0.532 (clinical stage: APPROVAL)
- **SPRED1** – score 0.480 (NF1-related pathway)

### Surgical and Interventional
Surgical resection remains the only potentially curative option but is limited by incomplete resectability, with regrowth rates of 20–68% depending on extent of resection (armstrong2023treatmentdecisionsand pages 6-7, armstrong2023treatmentdecisionsand pages 2-4). MAXO term: MAXO:0000004 (surgical procedure).

### Experimental Therapies and Clinical Trials
The following table summarizes active recruiting clinical trials:

| NCT number | Brief study title | Phase | Intervention type | Target enrollment | Status |
|---|---|---|---|---:|---|
| NCT05199376 | Percutaneous cryotherapy for plexiform/unresectable neurofibromas in NF1 | N/A | Interventional; cryotherapy | 30 | Recruiting (OpenTargets Search: neurofibroma) |
| NCT07407803 | TQ-B3234 capsules for symptomatic, non-surgical NF1-associated plexiform neurofibromas | Phase 3 | Interventional; small-molecule drug | 177 | Recruiting (OpenTargets Search: neurofibroma) |
| NCT07102394 | IMLYGIC for cutaneous neurofibromas in adults with NF1 | Phase 1 | Interventional; oncolytic viral therapy | 10 | Recruiting (OpenTargets Search: neurofibroma) |
| NCT05331105 | HL-085 in adults with NF1 and inoperable plexiform neurofibromas | Phase 2 | Interventional; small-molecule drug | 70 | Recruiting (OpenTargets Search: neurofibroma) |
| NCT06188741 | Selumetinib for prevention of plexiform neurofibroma growth in NF1 | Phase 2 | Interventional; MEK inhibitor | 200 | Recruiting (OpenTargets Search: neurofibroma) |
| NCT06159166 | Mirdametinib monotherapy in adults with NF1 and cutaneous neurofibromas | Phase 1/2 | Interventional; MEK inhibitor | 24 | Recruiting (OpenTargets Search: neurofibroma) |
| NCT06961565 | PAS-004 in adults with NF1 and plexiform neurofibromas | Phase 1 | Interventional; investigational drug | 56 | Recruiting (OpenTargets Search: neurofibroma) |
| NCT06515860 | NF1 Tumor Early Detection Study | Observational | Observational; early detection/biomarker study | 1000 | Recruiting (OpenTargets Search: neurofibroma) |


*Table: This table summarizes active/recruiting neurofibroma-related clinical studies identified in the search, highlighting trial phase, intervention type, enrollment, and current status. It is useful for quickly surveying the present translational and therapeutic pipeline in NF1-associated neurofibroma.*

Emerging therapeutic strategies under investigation include AAV-based gene therapy for NF1 restoration, oncolytic herpes simplex virus (oHSV) therapy, CAR-T cell therapy targeting NF1-associated tumors, and combination strategies such as MEK + PAK inhibition for treatment-resistant tumors (lu2025neurofibromatosistype1 pages 2-4). Prolonged MEK inhibition induces compensatory phosphorylation of MEK and AKT, supporting the rationale for combination strategies (OpenTargets Search: neurofibroma).

---

## 11. Prevention

### Primary Prevention
No primary prevention exists for NF1-associated neurofibromas given the genetic etiology. Genetic counseling is recommended for affected families. MAXO term: MAXO:0000127 (genetic counseling).

### Secondary Prevention
- **Surveillance protocols:** Regular clinical examinations, ophthalmologic assessments, developmental screening, and neuroimaging per age-appropriate guidelines (lalvani2024neurofibromatosistype1 pages 1-2, almuqbil2024epidemiologyandoutcomes pages 2-4)
- **Selumetinib for prevention:** An active Phase 2 trial (NCT06188741) is investigating selumetinib for prevention of plexiform neurofibroma growth in NF1 (OpenTargets Search: neurofibroma)
- **Early detection:** An NF1 Tumor Early Detection Study (NCT06515860) with 1,000 planned participants is currently recruiting (OpenTargets Search: neurofibroma)
- **Liquid biopsy:** ctDNA-based approaches for early detection of malignant transformation are under development (busciglio2025thepathogenesisof pages 1-2)

### Screening
Cascade genetic testing of first-degree relatives is recommended. Standardized genotyping enables early identification of high-risk genotypes (e.g., 17q11.2 microdeletion) for intensified surveillance (kitsera2026moleculargeneticsand pages 2-3, peduto2023neurofibromatosistype1 pages 11-13).

---

## 12. Model Organisms

### Mouse Models
Multiple genetically engineered mouse models recapitulate aspects of human neurofibroma (plante2024revisitingthenpcis pages 8-11, plante2024revisitingthenpcis pages 1-2, plante2024revisitingthenpcis pages 11-12, plante2024revisitingthenpcis pages 2-4, mo2025humanizedneurofibromamodel pages 1-2):
- **Conditional Nf1 knockout models:** Tissue-specific Cre recombinase (Krox20-Cre, P0-Cre, DhhCre, Hoxb7-Cre) combined with Nf1 flox mice generate para-spinal neurofibromas in 6–12 months
- **NPcis model:** The most widely used MPNST model; develops MPNSTs in 3–6 months with 30% penetrance. Intentional sciatic nerve injury converts it into a plexiform neurofibroma model within 1–6 months with 50% penetrance (plante2024revisitingthenpcis pages 8-11, plante2024revisitingthenpcis pages 11-12, plante2024revisitingthenpcis pages 2-4)
- **Sox10-Cre Nf1 knockout:** Inactivation of both Nf1 alleles in Sox10+ cells generates classic nodular cutaneous and plexiform neurofibromas that completely recapitulate human counterparts – described as the first genetically engineered mouse model of nodular cutaneous neurofibroma (mo2025humanizedneurofibromamodel pages 1-2)

### Porcine Models
Genetically engineered NF1-mutant minipigs closely resemble human neurofibromas histologically and contain all known cellular components of their human counterparts, including Schwann cells, fibroblasts, immune cells, and vascular elements. These models are used for single-cell transcriptomic profiling and preclinical drug testing (mclean2023singlecellrnasequencing pages 16-17, mclean2023singlecellrnasequencing pages 1-2).

### iPSC-Derived Models
Patient-specific NF1-mutant human induced pluripotent stem cells (hiPSCs) differentiated into Schwannian lineage cells (SLCs) form bona fide neurofibromas upon mouse sciatic nerve implantation when NF1-null, while wild-type and heterozygous cells do not (mo2025humanizedneurofibromamodel pages 1-2).

### Model Limitations
Current tissue-specific knockout models primarily recapitulate para-spinal neurofibromas (a rare subtype in humans), and de novo rapid MPNST development in mice does not accurately mirror the slow human neurofibroma-to-MPNST progression (plante2024revisitingthenpcis pages 8-11, mclean2023singlecellrnasequencing pages 1-2).

---

## 13. Summary

Neurofibroma represents the defining neoplastic manifestation of NF1, driven by biallelic inactivation of the *NF1* tumor suppressor gene and constitutive RAS/MAPK pathway activation. The disease has undergone a therapeutic revolution with the approval of MEK inhibitors, particularly selumetinib (68–71% partial response rate) and mirdametinib (42–50% partial response rate) for inoperable plexiform neurofibromas (souza2022clinicaltrialstargeting pages 5-6, armstrong2023treatmentdecisionsand pages 2-4). Single-cell transcriptomic studies have revealed the remarkable complexity of the neurofibroma tumor microenvironment, with immune and stromal cells comprising ~90% of tumor cellularity and multiple immunosuppressive mechanisms identified (kershner2022multiplenf1schwann pages 1-2, mclean2023singlecellrnasequencing pages 11-13, mclean2023singlecellrnasequencing pages 14-15). The malignant transformation pathway from neurofibroma to MPNST involves sequential loss of CDKN2A and PRC2 components, representing actionable biomarkers for early detection and therapeutic targeting (busciglio2025thepathogenesisof pages 2-4, busciglio2025thepathogenesisof pages 1-2). Ongoing clinical trials are exploring prevention strategies, topical MEK inhibitors for cutaneous neurofibromas, and gene therapy approaches, representing a rapidly evolving therapeutic landscape for this complex tumor predisposition syndrome.

References

1. (sur2022neurofibromatosisinchildren pages 1-2): Maria Lucia Sur, Ionel Armat, Genel Sur, Diana-Cristina Pop, Gabriel Samasca, Iulia Lupan, Teodora-Larisa Timis, Ioan-Alexandru Florian, and Daniel Sur. Neurofibromatosis in children: actually and perspectives. Children, 9:40, Jan 2022. URL: https://doi.org/10.3390/children9010040, doi:10.3390/children9010040. This article has 19 citations.

2. (mo2022neurofibrominandsuppression pages 1-3): Juan Mo, Stefanie L. Moye, Renee M. McKay, and Lu Q. Le. Neurofibromin and suppression of tumorigenesis: beyond the gap. Oncogene, 41:1235-1251, Jan 2022. URL: https://doi.org/10.1038/s41388-021-02156-y, doi:10.1038/s41388-021-02156-y. This article has 99 citations and is from a domain leading peer-reviewed journal.

3. (kitsera2026moleculargeneticsand pages 2-3): N.I. Kitsera, M.I. Drobchak, M.V. Bondarenko, R.V. Kozovyi, L.Ye. Kovalchuk, O.I. Dorosh, and I.L. Kozova. Molecular genetics and clinical spectrum of neurofibromatosis type 1 in patients: a case-based review. CHILD`S HEALTH, 21:49-59, Mar 2026. URL: https://doi.org/10.22141/2224-0551.21.1.2026.1939, doi:10.22141/2224-0551.21.1.2026.1939. This article has 0 citations.

4. (anastasaki2022rasandbeyond pages 2-3): Corina Anastasaki, Paola Orozco, and David H. Gutmann. Ras and beyond: the many faces of the neurofibromatosis type 1 protein. Disease Models & Mechanisms, Feb 2022. URL: https://doi.org/10.1242/dmm.049362, doi:10.1242/dmm.049362. This article has 108 citations and is from a domain leading peer-reviewed journal.

5. (sur2022neurofibromatosisinchildren pages 2-4): Maria Lucia Sur, Ionel Armat, Genel Sur, Diana-Cristina Pop, Gabriel Samasca, Iulia Lupan, Teodora-Larisa Timis, Ioan-Alexandru Florian, and Daniel Sur. Neurofibromatosis in children: actually and perspectives. Children, 9:40, Jan 2022. URL: https://doi.org/10.3390/children9010040, doi:10.3390/children9010040. This article has 19 citations.

6. (yu2025emergingmechanismand pages 2-4): Xuan Yu, Yi-Hui Gu, Jun Liu, Jing-Xuan Huang, Qingfeng Li, and Zhichao Wang. Emerging mechanism and therapeutic potential of neurofibromatosis type 1-related nerve system tumor: advancing insights into tumor development. Neuro-Oncology Advances, Feb 2025. URL: https://doi.org/10.1093/noajnl/vdaf040, doi:10.1093/noajnl/vdaf040. This article has 2 citations and is from a peer-reviewed journal.

7. (imataka2025neurofibromatosistype1 pages 4-5): George Imataka, Shigeko Kuwashima, Shujiro Hayashi, Kei Ogino, Eisei Hoshiyama, Katsuhiko Naruse, and Hideaki Shiraishi. Neurofibromatosis type 1 and mek inhibition: a comprehensive review with focus on selumetinib therapy. Journal of Clinical Medicine, Jul 2025. URL: https://doi.org/10.3390/jcm14145071, doi:10.3390/jcm14145071. This article has 6 citations.

8. (lee2023incidenceandprevalence pages 1-2): Tin-Suet Joan Lee, Meera Chopra, Raymond H. Kim, Patricia C. Parkin, and Carolina Barnett-Tapia. Incidence and prevalence of neurofibromatosis type 1 and 2: a systematic review and meta-analysis. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02911-2, doi:10.1186/s13023-023-02911-2. This article has 171 citations and is from a peer-reviewed journal.

9. (lee2023incidenceandprevalence pages 2-4): Tin-Suet Joan Lee, Meera Chopra, Raymond H. Kim, Patricia C. Parkin, and Carolina Barnett-Tapia. Incidence and prevalence of neurofibromatosis type 1 and 2: a systematic review and meta-analysis. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02911-2, doi:10.1186/s13023-023-02911-2. This article has 171 citations and is from a peer-reviewed journal.

10. (hussain2024roleoflong pages 3-5): Md Sadique Hussain, Somya Sharma, Alka Kumari, Almaz Kamran, Gurusha Bahl, Ajay Singh Bisht, Ayesha Sultana, Sumel Ashique, Prasanna Srinivasan Ramalingam, and Sivakumar Arumugam. Role of long non-coding rnas in neurofibromatosis and schwannomatosis: pathogenesis and therapeutic potential. Epigenomics, 16:1-12, Nov 2024. URL: https://doi.org/10.1080/17501911.2024.2430170, doi:10.1080/17501911.2024.2430170. This article has 15 citations and is from a peer-reviewed journal.

11. (lu2025neurofibromatosistype1 pages 2-4): Yuqing Lu, Manzhu Xu, Xiaojun Chen, Huazhen Xu, Nihao Sun, Karis E. Weisgerber, and Ren-Yuan Bai. Neurofibromatosis type 1: genetic mechanisms and advances in therapeutic innovation. Cancers, 17:3788, Nov 2025. URL: https://doi.org/10.3390/cancers17233788, doi:10.3390/cancers17233788. This article has 3 citations.

12. (OpenTargets Search: neurofibroma): Open Targets Query (neurofibroma, 42 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

13. (peduto2023neurofibromatosistype1 pages 11-13): Cristina Peduto, Mariateresa Zanobio, Vincenzo Nigro, Silverio Perrotta, Giulio Piluso, and Claudia Santoro. Neurofibromatosis type 1: pediatric aspects and review of genotype–phenotype correlations. Cancers, 15:1217, Feb 2023. URL: https://doi.org/10.3390/cancers15041217, doi:10.3390/cancers15041217. This article has 88 citations.

14. (yao2023malignantperipheralnerve pages 2-4): Chengjun Yao, Haiying Zhou, Yanzhao Dong, Ahmad Alhaskawi, Sohaib Hasan Abdullah Ezzi, Zewei Wang, Jingtian Lai, Vishnu Goutham Kota, Mohamed Hasan Abdulla Hasan Abdulla, and Hui Lu. Malignant peripheral nerve sheath tumors: latest concepts in disease pathogenesis and clinical management. Cancers, 15:1077, Feb 2023. URL: https://doi.org/10.3390/cancers15041077, doi:10.3390/cancers15041077. This article has 129 citations.

15. (plante2024revisitingthenpcis pages 8-11): Camille Plante, Teddy Mohamad, Dhanushka Hewa Bostanthirige, Michel Renaud, Harsimran Sidhu, Michel ElChoueiry, Jean-Paul Sabo Vatasescu, Mikael Poirier, Sameh Geha, and Jean-Philippe Brosseau. Revisiting the npcis mouse model: a new tool to model plexiform neurofibroma. PLOS ONE, 19:e0301040, Jun 2024. URL: https://doi.org/10.1371/journal.pone.0301040, doi:10.1371/journal.pone.0301040. This article has 1 citations and is from a peer-reviewed journal.

16. (plante2024revisitingthenpcis pages 1-2): Camille Plante, Teddy Mohamad, Dhanushka Hewa Bostanthirige, Michel Renaud, Harsimran Sidhu, Michel ElChoueiry, Jean-Paul Sabo Vatasescu, Mikael Poirier, Sameh Geha, and Jean-Philippe Brosseau. Revisiting the npcis mouse model: a new tool to model plexiform neurofibroma. PLOS ONE, 19:e0301040, Jun 2024. URL: https://doi.org/10.1371/journal.pone.0301040, doi:10.1371/journal.pone.0301040. This article has 1 citations and is from a peer-reviewed journal.

17. (lalvani2024neurofibromatosistype1 pages 1-2): Shaan Lalvani and Rebecca Brown. Neurofibromatosis type 1: optimizing management with a multidisciplinary approach. Journal of Multidisciplinary Healthcare, 17:1803-1817, Apr 2024. URL: https://doi.org/10.2147/jmdh.s362791, doi:10.2147/jmdh.s362791. This article has 31 citations and is from a peer-reviewed journal.

18. (imataka2025neurofibromatosistype1 pages 2-4): George Imataka, Shigeko Kuwashima, Shujiro Hayashi, Kei Ogino, Eisei Hoshiyama, Katsuhiko Naruse, and Hideaki Shiraishi. Neurofibromatosis type 1 and mek inhibition: a comprehensive review with focus on selumetinib therapy. Journal of Clinical Medicine, Jul 2025. URL: https://doi.org/10.3390/jcm14145071, doi:10.3390/jcm14145071. This article has 6 citations.

19. (almuqbil2024epidemiologyandoutcomes pages 1-2): Mohammed Almuqbil, Fatimah Alshaikh, Waleed Altwaijri, Duaa Baarmah, Raid Hommady, Maryam Alshaikh, Fares Alammari, Meshal Alhussain, Reem Almotawa, Faris Alqarni, Amna Kashgari, Rayan Alkhodair, Jumanah Alkhater, Lujeen Alkhater, Sawsan Alharthi, Mada Alsadi, and Ahmed AlRumayyan. Epidemiology and outcomes of neurofibromatosis type 1 (nf-1): multicenter tertiary experience. Journal of Multidisciplinary Healthcare, 17:1303-1314, Mar 2024. URL: https://doi.org/10.2147/jmdh.s454921, doi:10.2147/jmdh.s454921. This article has 14 citations and is from a peer-reviewed journal.

20. (almuqbil2024epidemiologyandoutcomes pages 5-7): Mohammed Almuqbil, Fatimah Alshaikh, Waleed Altwaijri, Duaa Baarmah, Raid Hommady, Maryam Alshaikh, Fares Alammari, Meshal Alhussain, Reem Almotawa, Faris Alqarni, Amna Kashgari, Rayan Alkhodair, Jumanah Alkhater, Lujeen Alkhater, Sawsan Alharthi, Mada Alsadi, and Ahmed AlRumayyan. Epidemiology and outcomes of neurofibromatosis type 1 (nf-1): multicenter tertiary experience. Journal of Multidisciplinary Healthcare, 17:1303-1314, Mar 2024. URL: https://doi.org/10.2147/jmdh.s454921, doi:10.2147/jmdh.s454921. This article has 14 citations and is from a peer-reviewed journal.

21. (peduto2023neurofibromatosistype1 pages 2-4): Cristina Peduto, Mariateresa Zanobio, Vincenzo Nigro, Silverio Perrotta, Giulio Piluso, and Claudia Santoro. Neurofibromatosis type 1: pediatric aspects and review of genotype–phenotype correlations. Cancers, 15:1217, Feb 2023. URL: https://doi.org/10.3390/cancers15041217, doi:10.3390/cancers15041217. This article has 88 citations.

22. (busciglio2025thepathogenesisof pages 1-2): Sabrina Busciglio, Ilenia Rita Cannizzaro, Anita Luberto, Antonietta Taiani, Barbara Moschella, Enrico Ambrosini, Sofia Cesarini, Mirko Treccani, Cinzia Azzoni, Lorena Bottarelli, Domenico Corradi, Vera Uliana, Davide Martorana, Valeria Barili, and Antonio Percesepe. The pathogenesis of the neurofibroma-to-sarcoma transition in neurofibromatosis type i: from molecular profiles to diagnostic applications. Cancers, 17:3955, Dec 2025. URL: https://doi.org/10.3390/cancers17243955, doi:10.3390/cancers17243955. This article has 3 citations.

23. (almuqbil2024epidemiologyandoutcomes pages 2-4): Mohammed Almuqbil, Fatimah Alshaikh, Waleed Altwaijri, Duaa Baarmah, Raid Hommady, Maryam Alshaikh, Fares Alammari, Meshal Alhussain, Reem Almotawa, Faris Alqarni, Amna Kashgari, Rayan Alkhodair, Jumanah Alkhater, Lujeen Alkhater, Sawsan Alharthi, Mada Alsadi, and Ahmed AlRumayyan. Epidemiology and outcomes of neurofibromatosis type 1 (nf-1): multicenter tertiary experience. Journal of Multidisciplinary Healthcare, 17:1303-1314, Mar 2024. URL: https://doi.org/10.2147/jmdh.s454921, doi:10.2147/jmdh.s454921. This article has 14 citations and is from a peer-reviewed journal.

24. (liang2024longtermdistressthroughout pages 1-2): Wanxian Liang, Shihuan Cao, Yusi Suo, Lining Zhang, Lujia Yang, Ping Wang, Hanfei Wang, Hanfei Wang, Guannan Bai, Qingnan Li, Jiayin Zheng, and Xuejing Jin. Long-term distress throughout one’s life: health-related quality of life, economic and caregiver burden of patients with neurofibromatosis type 1 in china. Frontiers in Public Health, Aug 2024. URL: https://doi.org/10.3389/fpubh.2024.1398803, doi:10.3389/fpubh.2024.1398803. This article has 4 citations.

25. (liang2024longtermdistressthroughout pages 4-5): Wanxian Liang, Shihuan Cao, Yusi Suo, Lining Zhang, Lujia Yang, Ping Wang, Hanfei Wang, Hanfei Wang, Guannan Bai, Qingnan Li, Jiayin Zheng, and Xuejing Jin. Long-term distress throughout one’s life: health-related quality of life, economic and caregiver burden of patients with neurofibromatosis type 1 in china. Frontiers in Public Health, Aug 2024. URL: https://doi.org/10.3389/fpubh.2024.1398803, doi:10.3389/fpubh.2024.1398803. This article has 4 citations.

26. (mo2022neurofibrominandsuppression pages 19-21): Juan Mo, Stefanie L. Moye, Renee M. McKay, and Lu Q. Le. Neurofibromin and suppression of tumorigenesis: beyond the gap. Oncogene, 41:1235-1251, Jan 2022. URL: https://doi.org/10.1038/s41388-021-02156-y, doi:10.1038/s41388-021-02156-y. This article has 99 citations and is from a domain leading peer-reviewed journal.

27. (busciglio2025thepathogenesisof pages 2-4): Sabrina Busciglio, Ilenia Rita Cannizzaro, Anita Luberto, Antonietta Taiani, Barbara Moschella, Enrico Ambrosini, Sofia Cesarini, Mirko Treccani, Cinzia Azzoni, Lorena Bottarelli, Domenico Corradi, Vera Uliana, Davide Martorana, Valeria Barili, and Antonio Percesepe. The pathogenesis of the neurofibroma-to-sarcoma transition in neurofibromatosis type i: from molecular profiles to diagnostic applications. Cancers, 17:3955, Dec 2025. URL: https://doi.org/10.3390/cancers17243955, doi:10.3390/cancers17243955. This article has 3 citations.

28. (busciglio2025thepathogenesisof pages 4-6): Sabrina Busciglio, Ilenia Rita Cannizzaro, Anita Luberto, Antonietta Taiani, Barbara Moschella, Enrico Ambrosini, Sofia Cesarini, Mirko Treccani, Cinzia Azzoni, Lorena Bottarelli, Domenico Corradi, Vera Uliana, Davide Martorana, Valeria Barili, and Antonio Percesepe. The pathogenesis of the neurofibroma-to-sarcoma transition in neurofibromatosis type i: from molecular profiles to diagnostic applications. Cancers, 17:3955, Dec 2025. URL: https://doi.org/10.3390/cancers17243955, doi:10.3390/cancers17243955. This article has 3 citations.

29. (busciglio2025thepathogenesisof pages 6-7): Sabrina Busciglio, Ilenia Rita Cannizzaro, Anita Luberto, Antonietta Taiani, Barbara Moschella, Enrico Ambrosini, Sofia Cesarini, Mirko Treccani, Cinzia Azzoni, Lorena Bottarelli, Domenico Corradi, Vera Uliana, Davide Martorana, Valeria Barili, and Antonio Percesepe. The pathogenesis of the neurofibroma-to-sarcoma transition in neurofibromatosis type i: from molecular profiles to diagnostic applications. Cancers, 17:3955, Dec 2025. URL: https://doi.org/10.3390/cancers17243955, doi:10.3390/cancers17243955. This article has 3 citations.

30. (busciglio2025thepathogenesisof pages 14-14): Sabrina Busciglio, Ilenia Rita Cannizzaro, Anita Luberto, Antonietta Taiani, Barbara Moschella, Enrico Ambrosini, Sofia Cesarini, Mirko Treccani, Cinzia Azzoni, Lorena Bottarelli, Domenico Corradi, Vera Uliana, Davide Martorana, Valeria Barili, and Antonio Percesepe. The pathogenesis of the neurofibroma-to-sarcoma transition in neurofibromatosis type i: from molecular profiles to diagnostic applications. Cancers, 17:3955, Dec 2025. URL: https://doi.org/10.3390/cancers17243955, doi:10.3390/cancers17243955. This article has 3 citations.

31. (busciglio2025thepathogenesisof pages 10-12): Sabrina Busciglio, Ilenia Rita Cannizzaro, Anita Luberto, Antonietta Taiani, Barbara Moschella, Enrico Ambrosini, Sofia Cesarini, Mirko Treccani, Cinzia Azzoni, Lorena Bottarelli, Domenico Corradi, Vera Uliana, Davide Martorana, Valeria Barili, and Antonio Percesepe. The pathogenesis of the neurofibroma-to-sarcoma transition in neurofibromatosis type i: from molecular profiles to diagnostic applications. Cancers, 17:3955, Dec 2025. URL: https://doi.org/10.3390/cancers17243955, doi:10.3390/cancers17243955. This article has 3 citations.

32. (mo2025humanizedneurofibromamodel pages 1-2): Juan Mo, Corina Anastasaki, Zhiguo Chen, Tracey Shipman, Jason Papke, Kevin Yin, David H. Gutmann, and Lu Q. Le. Humanized neurofibroma model from induced pluripotent stem cells delineates tumor pathogenesis and developmental origins. Journal of Clinical Investigation, Jan 2025. URL: https://doi.org/10.1172/jci139807, doi:10.1172/jci139807. This article has 81 citations and is from a highest quality peer-reviewed journal.

33. (kershner2022multiplenf1schwann pages 1-2): Leah J. Kershner, Kwangmin Choi, Jianqiang Wu, Xiyuan Zhang, Melissa Perrino, Nathan Salomonis, Jack F. Shern, and Nancy Ratner. Multiple nf1 schwann cell populations reprogram the plexiform neurofibroma tumor microenvironment. JCI Insight, Sep 2022. URL: https://doi.org/10.1172/jci.insight.154513, doi:10.1172/jci.insight.154513. This article has 60 citations and is from a domain leading peer-reviewed journal.

34. (mclean2023singlecellrnasequencing pages 5-6): Dalton T. McLean, J. Meudt, Loren D. Lopez Rivera, Dominic T. Schomberg, Derek M Pavelec, Tyler T. Duellman, Darya G. Buehler, Patrick B. Schwartz, Melissa Graham, Laura M. Lee, Keri D. Graff, Jamie L Reichert, Sandra S. Bon-Durant, Charles M. Konsitzke, Sean M. Ronnekleiv-Kelly, D. Shanmuganayagam, C. Rubinstein, Luciane R. Cavalli, Zhirui Zeng, and Paula Dobosz. Single-cell rna sequencing of neurofibromas reveals a tumor microenvironment favorable for neural regeneration and immune suppression in a neurofibromatosis type 1 porcine model. Frontiers in Oncology, Sep 2023. URL: https://doi.org/10.3389/fonc.2023.1253659, doi:10.3389/fonc.2023.1253659. This article has 5 citations.

35. (mclean2023singlecellrnasequencing pages 11-13): Dalton T. McLean, J. Meudt, Loren D. Lopez Rivera, Dominic T. Schomberg, Derek M Pavelec, Tyler T. Duellman, Darya G. Buehler, Patrick B. Schwartz, Melissa Graham, Laura M. Lee, Keri D. Graff, Jamie L Reichert, Sandra S. Bon-Durant, Charles M. Konsitzke, Sean M. Ronnekleiv-Kelly, D. Shanmuganayagam, C. Rubinstein, Luciane R. Cavalli, Zhirui Zeng, and Paula Dobosz. Single-cell rna sequencing of neurofibromas reveals a tumor microenvironment favorable for neural regeneration and immune suppression in a neurofibromatosis type 1 porcine model. Frontiers in Oncology, Sep 2023. URL: https://doi.org/10.3389/fonc.2023.1253659, doi:10.3389/fonc.2023.1253659. This article has 5 citations.

36. (mclean2023singlecellrnasequencing pages 14-15): Dalton T. McLean, J. Meudt, Loren D. Lopez Rivera, Dominic T. Schomberg, Derek M Pavelec, Tyler T. Duellman, Darya G. Buehler, Patrick B. Schwartz, Melissa Graham, Laura M. Lee, Keri D. Graff, Jamie L Reichert, Sandra S. Bon-Durant, Charles M. Konsitzke, Sean M. Ronnekleiv-Kelly, D. Shanmuganayagam, C. Rubinstein, Luciane R. Cavalli, Zhirui Zeng, and Paula Dobosz. Single-cell rna sequencing of neurofibromas reveals a tumor microenvironment favorable for neural regeneration and immune suppression in a neurofibromatosis type 1 porcine model. Frontiers in Oncology, Sep 2023. URL: https://doi.org/10.3389/fonc.2023.1253659, doi:10.3389/fonc.2023.1253659. This article has 5 citations.

37. (swanson2025singlecellanalysisof pages 12-15): Grace M Swanson, Marcia Arenas-Hernandez, and Katherine Gurdziel. Single-cell analysis of <i>nf1</i> -expressing and <i>nf1</i> -deficient schwann and fibroblast cells reveals divergent neurofibroma programs. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.26.677858, doi:10.1101/2025.09.26.677858. This article has 0 citations.

38. (swanson2025singlecellanalysisof pages 25-27): Grace M Swanson, Marcia Arenas-Hernandez, and Katherine Gurdziel. Single-cell analysis of <i>nf1</i> -expressing and <i>nf1</i> -deficient schwann and fibroblast cells reveals divergent neurofibroma programs. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.26.677858, doi:10.1101/2025.09.26.677858. This article has 0 citations.

39. (lee2023incidenceandprevalence pages 4-7): Tin-Suet Joan Lee, Meera Chopra, Raymond H. Kim, Patricia C. Parkin, and Carolina Barnett-Tapia. Incidence and prevalence of neurofibromatosis type 1 and 2: a systematic review and meta-analysis. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02911-2, doi:10.1186/s13023-023-02911-2. This article has 171 citations and is from a peer-reviewed journal.

40. (armstrong2023treatmentdecisionsand pages 2-4): Amy E. Armstrong, Allan J. Belzberg, John R. Crawford, Angela C. Hirbe, and Zhihong J. Wang. Treatment decisions and the use of mek inhibitors for children with neurofibromatosis type 1-related plexiform neurofibromas. BMC Cancer, Jun 2023. URL: https://doi.org/10.1186/s12885-023-10996-y, doi:10.1186/s12885-023-10996-y. This article has 97 citations and is from a peer-reviewed journal.

41. (souza2022clinicaltrialstargeting pages 5-6): Gabriel Roman Souza, Ahmed Abdalla, and Daruka Mahadevan. Clinical trials targeting neurofibromatoses-associated tumors: a systematic review. Neuro-oncology Advances, Jan 2022. URL: https://doi.org/10.1093/noajnl/vdac005, doi:10.1093/noajnl/vdac005. This article has 18 citations and is from a peer-reviewed journal.

42. (souza2022clinicaltrialstargeting pages 9-10): Gabriel Roman Souza, Ahmed Abdalla, and Daruka Mahadevan. Clinical trials targeting neurofibromatoses-associated tumors: a systematic review. Neuro-oncology Advances, Jan 2022. URL: https://doi.org/10.1093/noajnl/vdac005, doi:10.1093/noajnl/vdac005. This article has 18 citations and is from a peer-reviewed journal.

43. (imataka2025neurofibromatosistype1 pages 9-11): George Imataka, Shigeko Kuwashima, Shujiro Hayashi, Kei Ogino, Eisei Hoshiyama, Katsuhiko Naruse, and Hideaki Shiraishi. Neurofibromatosis type 1 and mek inhibition: a comprehensive review with focus on selumetinib therapy. Journal of Clinical Medicine, Jul 2025. URL: https://doi.org/10.3390/jcm14145071, doi:10.3390/jcm14145071. This article has 6 citations.

44. (imataka2025neurofibromatosistype1 pages 12-13): George Imataka, Shigeko Kuwashima, Shujiro Hayashi, Kei Ogino, Eisei Hoshiyama, Katsuhiko Naruse, and Hideaki Shiraishi. Neurofibromatosis type 1 and mek inhibition: a comprehensive review with focus on selumetinib therapy. Journal of Clinical Medicine, Jul 2025. URL: https://doi.org/10.3390/jcm14145071, doi:10.3390/jcm14145071. This article has 6 citations.

45. (armstrong2023treatmentdecisionsand pages 6-7): Amy E. Armstrong, Allan J. Belzberg, John R. Crawford, Angela C. Hirbe, and Zhihong J. Wang. Treatment decisions and the use of mek inhibitors for children with neurofibromatosis type 1-related plexiform neurofibromas. BMC Cancer, Jun 2023. URL: https://doi.org/10.1186/s12885-023-10996-y, doi:10.1186/s12885-023-10996-y. This article has 97 citations and is from a peer-reviewed journal.

46. (souza2022clinicaltrialstargeting pages 6-7): Gabriel Roman Souza, Ahmed Abdalla, and Daruka Mahadevan. Clinical trials targeting neurofibromatoses-associated tumors: a systematic review. Neuro-oncology Advances, Jan 2022. URL: https://doi.org/10.1093/noajnl/vdac005, doi:10.1093/noajnl/vdac005. This article has 18 citations and is from a peer-reviewed journal.

47. (imataka2025neurofibromatosistype1 pages 7-9): George Imataka, Shigeko Kuwashima, Shujiro Hayashi, Kei Ogino, Eisei Hoshiyama, Katsuhiko Naruse, and Hideaki Shiraishi. Neurofibromatosis type 1 and mek inhibition: a comprehensive review with focus on selumetinib therapy. Journal of Clinical Medicine, Jul 2025. URL: https://doi.org/10.3390/jcm14145071, doi:10.3390/jcm14145071. This article has 6 citations.

48. (plante2024revisitingthenpcis pages 11-12): Camille Plante, Teddy Mohamad, Dhanushka Hewa Bostanthirige, Michel Renaud, Harsimran Sidhu, Michel ElChoueiry, Jean-Paul Sabo Vatasescu, Mikael Poirier, Sameh Geha, and Jean-Philippe Brosseau. Revisiting the npcis mouse model: a new tool to model plexiform neurofibroma. PLOS ONE, 19:e0301040, Jun 2024. URL: https://doi.org/10.1371/journal.pone.0301040, doi:10.1371/journal.pone.0301040. This article has 1 citations and is from a peer-reviewed journal.

49. (plante2024revisitingthenpcis pages 2-4): Camille Plante, Teddy Mohamad, Dhanushka Hewa Bostanthirige, Michel Renaud, Harsimran Sidhu, Michel ElChoueiry, Jean-Paul Sabo Vatasescu, Mikael Poirier, Sameh Geha, and Jean-Philippe Brosseau. Revisiting the npcis mouse model: a new tool to model plexiform neurofibroma. PLOS ONE, 19:e0301040, Jun 2024. URL: https://doi.org/10.1371/journal.pone.0301040, doi:10.1371/journal.pone.0301040. This article has 1 citations and is from a peer-reviewed journal.

50. (mclean2023singlecellrnasequencing pages 16-17): Dalton T. McLean, J. Meudt, Loren D. Lopez Rivera, Dominic T. Schomberg, Derek M Pavelec, Tyler T. Duellman, Darya G. Buehler, Patrick B. Schwartz, Melissa Graham, Laura M. Lee, Keri D. Graff, Jamie L Reichert, Sandra S. Bon-Durant, Charles M. Konsitzke, Sean M. Ronnekleiv-Kelly, D. Shanmuganayagam, C. Rubinstein, Luciane R. Cavalli, Zhirui Zeng, and Paula Dobosz. Single-cell rna sequencing of neurofibromas reveals a tumor microenvironment favorable for neural regeneration and immune suppression in a neurofibromatosis type 1 porcine model. Frontiers in Oncology, Sep 2023. URL: https://doi.org/10.3389/fonc.2023.1253659, doi:10.3389/fonc.2023.1253659. This article has 5 citations.

51. (mclean2023singlecellrnasequencing pages 1-2): Dalton T. McLean, J. Meudt, Loren D. Lopez Rivera, Dominic T. Schomberg, Derek M Pavelec, Tyler T. Duellman, Darya G. Buehler, Patrick B. Schwartz, Melissa Graham, Laura M. Lee, Keri D. Graff, Jamie L Reichert, Sandra S. Bon-Durant, Charles M. Konsitzke, Sean M. Ronnekleiv-Kelly, D. Shanmuganayagam, C. Rubinstein, Luciane R. Cavalli, Zhirui Zeng, and Paula Dobosz. Single-cell rna sequencing of neurofibromas reveals a tumor microenvironment favorable for neural regeneration and immune suppression in a neurofibromatosis type 1 porcine model. Frontiers in Oncology, Sep 2023. URL: https://doi.org/10.3389/fonc.2023.1253659, doi:10.3389/fonc.2023.1253659. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](Neurofibroma-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Neurofibroma-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Neurofibroma-deep-research-falcon_artifacts/artifact-02.md)