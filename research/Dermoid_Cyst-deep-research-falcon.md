---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T10:29:54.820161'
end_time: '2026-06-30T10:45:22.175502'
duration_seconds: 927.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dermoid Cyst
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Dermoid_Cyst-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Dermoid_Cyst-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dermoid Cyst
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Dermoid Cyst** covering all of the
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
- **Disease Name:** Dermoid Cyst
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Dermoid Cyst** covering all of the
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


# Comprehensive Research Report: Dermoid Cyst

## 1. Disease Information

### 1.1 Overview

Dermoid cysts are benign developmental lesions that originate from ectodermal cells trapped during embryogenesis. They are composed of mature ectodermal derivatives and are histologically lined by keratinizing squamous epithelium containing adnexal structures such as sebaceous glands, hair follicles, and sweat glands (quan2026pediatricnasaldermoid pages 2-3, wiener2021histologicfeaturesof pages 14-16). Dermoid cysts differ from epidermoid cysts, which lack dermal appendages, and from teratomas, which arise from pluripotent germ cells and may contain elements of all three embryonic germ layers (soto2025presentationofa pages 1-3). The term "dermoid cyst" encompasses a heterogeneous group of lesions occurring at various anatomical sites, including the ovary (where mature cystic teratoma is the most common usage), the craniofacial region (nasal, orbital/periorbital), the central nervous system (intracranial, spinal), the skin/subcutaneous tissue, and the ocular surface (limbal/epibulbar).

### 1.2 Key Identifiers

- **ICD-10**: L72.0 (Epidermal cyst, which includes dermoid cysts of skin); D27 (Benign neoplasm of ovary, for ovarian dermoid/mature teratoma); Q84.4 (Congenital dermoid cyst); D33.9 (Benign neoplasm of brain, for intracranial dermoid)
- **ICD-11**: EK90.0 (Follicular cyst of skin and subcutaneous tissue); 2F32 (Benign neoplasms of ovary, for mature teratoma)
- **MeSH**: D003884 (Dermoid Cyst)
- **MONDO**: MONDO:0006233 (dermoid cyst)
- **Orphanet**: Not assigned a specific Orphanet number for dermoid cyst as a standalone entity; ORPHA:141112 (Ovarian germ cell tumor, which includes mature teratoma)
- **OMIM**: Not assigned a specific OMIM entry for sporadic dermoid cyst; 612555 (BMP15-related ovarian dysgenesis, relevant to hereditary forms)

### 1.3 Common Synonyms and Alternative Names

- Mature cystic teratoma (for ovarian dermoid cysts)
- Benign cystic teratoma
- Dermoid
- Dermoid tumor
- Nasal dermoid sinus cyst (NDSC, for midline nasal lesions)
- Epibulbar dermoid (for limbal/conjunctival lesions)
- Orbital dermoid (for periorbital lesions)
- Congenital dermoid cyst
- Choristoma (when referring to ocular dermoids)

### 1.4 Data Source

Information is derived from aggregated disease-level resources, including published peer-reviewed literature, clinical trial registries, and veterinary pathology databases.

The following table provides a comparative overview of dermoid cysts by anatomical location:

| Anatomical Site | Frequency/Prevalence | Typical Age of Onset | Key Clinical Features | Primary Diagnostic Modality | Primary Treatment |
|---|---|---|---|---|---|
| Ovarian (mature cystic teratoma / dermoid cyst) | Ovarian germ cell tumors represent ~2–5% of ovarian cancers; mature teratoma is the benign teratoma subtype and one of the common ovarian germ-cell lesions in children, adolescents, and young adults (saani2023clinicalchallengesin pages 9-10, pinto2023molecularbiologyof pages 1-3) | Usually reproductive age; often children, adolescents, and young adults for ovarian germ-cell tumors (pinto2023molecularbiologyof pages 1-3) | Often asymptomatic until large; may present with adnexal mass, pelvic pain, torsion, rupture, or rarely malignant transformation; histologically a mature teratoma is a dermoid cyst (moraru2023immatureteratomadiagnosis pages 2-4, saani2023clinicalchallengesin pages 9-10) | Pelvic ultrasound first-line; CT/MRI used for characterization of fat/calcification and complications; definitive diagnosis by histopathology after excision (moraru2023immatureteratomadiagnosis pages 2-4) | Surgical excision, usually fertility-sparing cystectomy/oophorectomy; laparoscopy commonly used when feasible (NCT06816316 chunk 2) |
| Intracranial | Rare benign tumor comprising ~0.04–0.6% of brain tumors (soto2025presentationofa pages 1-3) | Congenital in origin but often diagnosed in young adults, especially ages 20–30 for suprasellar supratentorial lesions; can occur from childhood to adulthood (soto2025presentationofa pages 1-3, soto2025presentationofa pages 6-8) | Headache, seizures, dizziness/vertigo, visual symptoms; rupture may cause chemical aseptic meningitis and acute symptomatic seizures (soto2025presentationofa pages 1-3, soto2025presentationofa pages 6-8) | MRI is primary and essential for diagnosis and surgical planning; CT may assist in lesion characterization (soto2025presentationofa pages 6-8, soto2025presentationofa pages 8-10) | Neurosurgical excision aiming for gross total resection when safely possible; subtotal resection may be necessary near critical neurovascular structures (soto2025presentationofa pages 8-10, soto2025presentationofa pages 1-3) |
| Nasal / craniofacial | Nasal dermoids account for at least 60% of congenital developmental midline nasal masses; intracranial involvement occurs in ~20% overall, with wide reported range (4–57%) (kotowski2023thedifferentialdiagnosis pages 2-5) | Congenital; usually recognized in infancy or childhood (quan2026pediatricnasaldermoid pages 2-3, kotowski2023thedifferentialdiagnosis pages 2-5) | Painless noncompressible midline nasal mass; sinus opening with visible hair may be present; recurrent local infection possible, with substantial childhood infection risk when a sinus ostium is present (quan2026pediatricnasaldermoid pages 2-3, kotowski2023thedifferentialdiagnosis pages 2-5) | MRI preferred for defining soft-tissue tract and intracranial extension; CT complements osseous assessment; biopsy is contraindicated (deftereou2025congenitalanomaliesof pages 6-6, quan2026pediatricnasaldermoid pages 4-5) | Complete surgical excision of cyst and tract; external rhinoplasty, endoscopic, or combined craniofacial approaches depending on extension (quan2026pediatricnasaldermoid pages 8-9, quan2026pediatricnasaldermoid pages 10-11) |
| Orbital / periorbital | Common congenital craniofacial dermoid location; literature in this evidence set is mainly case-series/review based rather than population-based, so precise prevalence not established here (soto2025presentationofa pages 6-8, quan2026pediatricnasaldermoid pages 8-9) | Usually congenital and detected in infancy or childhood (quan2026pediatricnasaldermoid pages 8-9) | Superolateral brow/orbital mass, usually painless and slowly enlarging; cosmetic deformity, local pressure effects, and occasional rupture/inflammation may occur (quan2026pediatricnasaldermoid pages 8-9, NCT06816316 chunk 2) | Clinical examination with imaging when deep lesion suspected; MRI/CT used to define orbital extension and surgical anatomy (NCT06816316 chunk 2) | Complete surgical excision; careful removal needed to avoid rupture and recurrence (NCT06816316 chunk 2) |
| Cutaneous / subcutaneous | Developmental anomaly rather than true neoplasm; human population prevalence not well defined in this evidence set (wiener2021histologicfeaturesof pages 14-16, wiener2021histologicfeaturesof pages 16-18) | Congenital, though superficial lesions may be recognized later depending on size/location (wiener2021histologicfeaturesof pages 14-16) | Small dermal/subcutaneous cyst containing keratin, hair, and sebaceous material; often solitary, slow-growing, and sometimes with a surface pore or protruding hair (wiener2021histologicfeaturesof pages 14-16, wiener2021histologicfeaturesof pages 16-18) | Clinical examination with confirmation by histopathology after excision; imaging only if deep extension suspected (wiener2021histologicfeaturesof pages 14-16, wiener2021histologicfeaturesof pages 16-18) | Complete surgical excision (wiener2021histologicfeaturesof pages 16-18) |
| Limbal / epibulbar | Rare ocular surface choristoma/dermoid subtype; no robust prevalence estimate in this evidence set (NCT06816316 chunk 2) | Congenital, typically identified in childhood (NCT06816316 chunk 2) | Visible limbal or epibulbar mass; may induce astigmatism, visual disturbance, irritation, or cosmetic concern (NCT06816316 chunk 2) | Ophthalmologic slit-lamp examination; imaging used selectively for extent/depth; diagnosis confirmed clinically and histopathologically when excised (NCT06816316 chunk 2) | Observation for small asymptomatic lesions or surgical excision/lamellar keratoplasty/corneal autograft in visually significant cases (NCT06816316 chunk 2) |


*Table: This table summarizes how dermoid cysts differ by anatomical site, including frequency, age at presentation, clinical features, diagnostic approach, and treatment. It is useful for comparing the major clinically relevant dermoid cyst subtypes in one place.*

---

## 2. Etiology

### 2.1 Disease Causal Factors

The primary etiology of dermoid cysts is developmental: they arise from ectodermal tissue entrapped during embryogenesis. For craniofacial dermoid cysts, two principal pathogenetic theories exist: (1) the **ectodermal inclusion theory**, in which surface ectoderm becomes entrapped during fusion of facial prominences, and (2) the **embryonic closure-defect theory**, involving extensive midline seam closure failure (quan2026pediatricnasaldermoid pages 2-3). For cutaneous dermoid cysts, incomplete separation of cutaneous ectoderm and neuroectoderm during embryogenesis results in focal skin reduplications that include epidermis, dermis, and adnexal structures (wiener2021histologicfeaturesof pages 14-16).

For **ovarian dermoid cysts (mature cystic teratomas)**, the origin is parthenogenetic: tumors arise from a single ovarian germ cell/oocyte, typically after completed meiosis I with failed meiosis II, producing homozygous chromosomes and containing only maternal genomes (moraru2023immatureteratomadiagnosis pages 2-4, pinto2023molecularbiologyof pages 7-9).

### 2.2 Genetic Risk Factors

A landmark study published in PNAS in 2024 identified a rare germline **BMP15 missense mutation (C262T)** as a causative variant for hereditary ovarian immature teratoma (OIT). This mutation substitutes arginine with cysteine at position 88, reducing BMP15 secretion by 84.7%, and displays **X-linked dominant inheritance** affecting heterozygous female carriers (liu2024araregermline pages 3-4, liu2024araregermline pages 2-3). The mutation significantly increases spontaneous parthenogenetic activation rates of oocytes (8.4% for CC, 32.5% for CT, 51.3% for TT genotypes) (liu2024araregermline pages 2-3).

Gonadal dysgenesis is a recognized risk factor for malignant ovarian germ cell tumors (though not specifically for benign dermoid cysts), particularly in 46,XY individuals with Y chromosomal material, conferring a 30–40% risk of developing gonadoblastomas (pinto2023molecularbiologyof pages 3-4).

### 2.3 Environmental and Lifestyle Risk Factors

No specific environmental or lifestyle risk factors have been established for dermoid cyst formation, consistent with their congenital/developmental nature. Age and sex are the principal demographic risk factors: ovarian dermoid cysts predominantly affect reproductive-age women; nasal and orbital dermoid cysts are congenital and present in pediatric populations; and intracranial dermoid cysts show increased incidence in young adults aged 20–30 years (soto2025presentationofa pages 1-3, kotowski2023thedifferentialdiagnosis pages 2-5).

### 2.4 Protective Factors

No specific genetic or environmental protective factors have been identified for dermoid cysts in the current literature.

### 2.5 Gene–Environment Interactions

No significant gene–environment interactions have been described for dermoid cyst formation. The condition is primarily of developmental/genetic origin.

---

## 3. Phenotypes

### 3.1 Clinical Phenotypes by Site

**Intracranial dermoid cysts** present with headaches (67% of cases) and seizures (44%), including acute symptomatic seizures following cyst rupture and chronic epileptic seizures with impaired awareness. Dizziness, vertigo, and visual symptoms are also common. Cyst rupture may cause chemical aseptic meningitis due to release of lipid contents into cerebrospinal fluid (soto2025presentationofa pages 1-3, soto2025presentationofa pages 6-8, soto2025presentationofa pages 8-10).
- Suggested HPO terms: HP:0002315 (Headache), HP:0001250 (Seizure), HP:0002383 (Encephalitis, for chemical meningitis), HP:0000238 (Hydrocephalus)

**Nasal dermoid sinus cysts** present as painless, non-compressible, non-pulsatile midline nasal masses that do not transilluminate. A sinus opening with visible hair may be present. Crucially, the presence of a sinus opening significantly increases infection risk, estimated at 7% per year during childhood, with 50% of children experiencing at least one infection by age 4 and over 90% by age 9 (kotowski2023thedifferentialdiagnosis pages 2-5). Intracranial involvement occurs in approximately 20% of cases (range 4–57%). Complications include local abscesses, periorbital cellulitis, osteomyelitis, meningitis, and cerebral abscesses (kotowski2023thedifferentialdiagnosis pages 2-5).
- Suggested HPO terms: HP:0000431 (Wide nasal bridge, if applicable), HP:0010781 (Skin dimple), HP:0002090 (Pneumonia, for intracranial complications), HP:0040187 (Abnormality of the nose)

**Ovarian dermoid cysts** are often asymptomatic until they become large. They may present with pelvic pain, adnexal mass, or complications such as ovarian torsion, rupture, or (rarely, ~1–2%) malignant transformation (moraru2023immatureteratomadiagnosis pages 2-4).
- Suggested HPO terms: HP:0000137 (Abnormality of the ovary), HP:0100607 (Dysmenorrhea), HP:0008675 (Enlarged ovaries)

**Cutaneous dermoid cysts** are typically solitary lesions less than 2 cm in diameter with a small pore that may contain protruding hair, located commonly on the dorsal midline (wiener2021histologicfeaturesof pages 14-16).
- Suggested HPO terms: HP:0200040 (Skin cyst), HP:0001053 (Hypopigmented skin patches)

### 3.2 Quality of Life Impact

Intracranial dermoid cysts can significantly impair quality of life through chronic headaches, seizures, and neurological deficits. Nasal dermoid cysts in children carry a high risk of recurrent infection and cosmetic deformity, impacting psychosocial development. Ovarian dermoid cysts may affect fertility and cause anxiety regarding malignant potential. Specific QoL instrument data (EQ-5D, SF-36) specifically for dermoid cysts are limited in the current literature.

---

## 4. Genetic/Molecular Information

The following table summarizes the key molecular and genetic features of dermoid cysts/teratomas:

| Molecular Feature | Details/Findings | Relevant Gene/Pathway | Significance | Key Reference |
|---|---|---|---|---|
| Germline BMP15 missense mutation in hereditary ovarian teratoma | A rare BMP15 C262T missense variant was identified in two pedigrees with hereditary ovarian immature teratoma; the mutation reduces mature BMP15 secretion by ~84.7% and supports an X-linked dominant hereditary form affecting heterozygous females. | **BMP15**; oocyte growth factor signaling | Strongest recent human genetic evidence for a causal predisposition gene in hereditary ovarian teratoma; supports molecular diagnosis and genetic counseling in high-risk families. | PNAS 2024 BMP15 study (liu2024araregermline pages 3-4, liu2024araregermline pages 2-3, liu2024araregermline pages 1-2) |
| Parthenogenetic origin of ovarian teratomas | Mature ovarian teratomas are described as parthenogenetic tumors containing only maternal genomes; they are thought to arise from a single ovarian germ cell/oocyte after meiotic errors or spontaneous activation without fertilization. | Oocyte meiosis / parthenogenesis | Explains why many ovarian teratomas show near-diploid genomes with limited somatic mutation burden and distinctive imprinting features. | Diagnostics 2023; Cancers 2023; PNAS 2024 (moraru2023immatureteratomadiagnosis pages 2-4, pinto2023molecularbiologyof pages 7-9, liu2024araregermline pages 1-2) |
| H-Ras/MAPK pathway activation | In BMP15-mutant oocytes, spontaneous parthenogenetic activation increased markedly, accompanied by elevated **H-Ras** and **MEK1** expression and MAPK pathway activation. | **H-Ras**, **MEK1**, **MAPK signaling** | Provides a mechanistic link between the BMP15 variant and abnormal oocyte activation leading to teratoma formation. | PNAS 2024 BMP15 study (liu2024araregermline pages 6-7, liu2024araregermline pages 4-6, liu2024araregermline pages 2-3) |
| GDF9/BMP15 signaling imbalance | The BMP15 variant may alter the balance between BMP15 homodimers/heterodimers and **GDF9**-related signaling, shifting downstream signaling outputs and enhancing pathways that favor parthenogenesis. | **BMP15**, **GDF9**, **BMPR2**, SMAD/MAPK-related signaling | Suggests that altered oocyte–granulosa cell signaling balance is an upstream event in hereditary teratoma pathogenesis. | PNAS 2024 BMP15 study (liu2024araregermline pages 6-7, liu2024araregermline pages 4-6, liu2024araregermline pages 7-8) |
| DNA methylation subtype differences | Ovarian germ cell tumors show subtype-specific methylation states: undifferentiated germinomas are relatively hypomethylated, whereas differentiated tumors including mature teratomas are more hypermethylated. | DNA methylation / epigenetic regulation | Supports the idea that differentiation state and cell of origin are reflected in methylation profiles; potentially useful for tumor classification and pathogenesis studies. | Cancers 2023 review (pinto2023molecularbiologyof pages 11-12, pinto2023molecularbiologyof pages 1-3, pinto2023molecularbiologyof pages 3-4) |
| Epigenetic imprinting abnormalities | Ovarian teratomas show abnormal imprinting patterns, including reduced methylation at paternally methylated loci and increased methylation at maternally methylated loci; IGF2/H19 imprinting abnormalities have also been reported in ovarian GCTs. | Genomic imprinting; **IGF2/H19** control region | Reinforces the maternal-genome/parthenogenetic model and indicates that imprint erasure/re-establishment defects are central to teratoma biology. | Cancers 2023 review (pinto2023molecularbiologyof pages 11-12, pinto2023molecularbiologyof pages 3-4, moraru2023immatureteratomadiagnosis pages 13-15) |
| Chromosomal abnormality: isochromosome 12p / 12p gain | Gain of chromosome 12p, including **isochromosome 12p**, is frequent in malignant germ cell tumors, especially dysgerminomas and yolk-sac tumors, but is less characteristic of immature teratomas and generally absent from mature teratomas with normal karyotype. | **12p gain / i(12p)** | Helps distinguish malignant ovarian GCT molecular pathways from the more parthenogenetic, usually cytogenetically bland pathway of mature teratoma/dermoid cyst. | Cancers 2023 review; IJERPH 2023 review (saani2023clinicalchallengesin pages 9-10, pinto2023molecularbiologyof pages 7-9) |
| Near-diploid genomes with limited somatic mutations | Immature teratomas may show near-diploid genomes, extensive allelic imbalance, and relative paucity of somatic mutations; mature teratomas often have normal karyotypes and arise after meiosis. | Meiotic nondisjunction; allelic imbalance | Indicates that abnormal germ-cell developmental/meiotic processes, rather than classic oncogenic mutation accumulation, drive teratoma formation. | Diagnostics 2023; Cancers 2023 (moraru2023immatureteratomadiagnosis pages 2-4, pinto2023molecularbiologyof pages 7-9, moraru2023immatureteratomadiagnosis pages 13-15) |
| Distinct pathogenetic pathway of immature teratoma | Immature teratomas appear to follow a pathogenetic route distinct from dysgerminoma/yolk-sac tumor and from some mature teratomas, with less emphasis on 12p gain and more on meiotic errors and epigenetic dysregulation. | Developmental germ-cell pathways | Important for biological classification, prognosis, and future risk stratification/targeted research. | Diagnostics 2023; IJERPH 2023; Cancers 2023 (moraru2023immatureteratomadiagnosis pages 2-4, saani2023clinicalchallengesin pages 9-10, pinto2023molecularbiologyof pages 7-9) |


*Table: This table summarizes the main molecular and genetic findings relevant to ovarian dermoid cysts/teratomas, emphasizing recent evidence on BMP15-associated hereditary teratoma and broader germ-cell tumor epigenetics and cytogenetics. It is useful for distinguishing developmental/parthenogenetic mechanisms from malignant germ-cell tumor pathways.*

### 4.1 Causal Genes

**BMP15** (Xp11.22; OMIM: 300247; HGNC:1068): A rare germline missense mutation BMP15 C262T (p.Arg88Cys) has been identified as the causative variant for hereditary ovarian immature teratoma with X-linked dominant inheritance. The mutation reduces mature BMP15 protein secretion by 84.7% and activates the H-Ras/MAPK signaling pathway, promoting parthenogenetic activation of oocytes (liu2024araregermline pages 3-4, liu2024araregermline pages 2-3, liu2024araregermline pages 1-2). This represents the first identified causal gene for hereditary ovarian teratoma in humans.

### 4.2 Pathogenic Variants

- **BMP15 C262T (p.Arg88Cys)**: Classified as pathogenic in the context of hereditary ovarian immature teratoma. The variant creates a new cysteine residue affecting BMP15 processing and dimerization. It is a rare germline variant with X-linked dominant inheritance, exclusively affecting heterozygous females. Somatic origin is not applicable; this is a germline variant (liu2024araregermline pages 3-4, liu2024araregermline pages 2-3).

### 4.3 Chromosomal Abnormalities

Mature ovarian teratomas typically have a **normal karyotype** (pinto2023molecularbiologyof pages 7-9). Gains on chromosome 12p, including **isochromosome 12p (i(12p))**, are characteristic of malignant germ cell tumors (82% of dysgerminomas, ~44% of all malignant GCTs) but are generally absent from mature teratomas and uncommon in pure immature teratomas (saani2023clinicalchallengesin pages 9-10, pinto2023molecularbiologyof pages 7-9). DNA ploidy analysis shows aneuploidy in 59% and diploidy in 41% of malignant GCT cases (saani2023clinicalchallengesin pages 9-10).

### 4.4 Epigenetic Information

Distinct DNA methylation patterns characterize different germ cell tumor subtypes: undifferentiated GCTs (germinomas) are hypomethylated, while differentiated tumors including mature teratomas are hypermethylated (pinto2023molecularbiologyof pages 11-12). Ovarian teratomas show abnormal genomic imprinting with reduced methylation at paternally methylated loci and increased methylation at maternally methylated loci, consistent with their parthenogenetic origin. Abnormalities in the **IGF2/H19** imprinting control region have been documented in ovarian GCTs (pinto2023molecularbiologyof pages 11-12, pinto2023molecularbiologyof pages 3-4).

---

## 5. Environmental Information

No specific environmental toxins, radiation exposures, or occupational factors have been linked to dermoid cyst formation. These are congenital developmental lesions. No infectious agents are implicated in the formation of dermoid cysts, though secondary infection of nasal and craniofacial dermoid sinuses is a common complication (kotowski2023thedifferentialdiagnosis pages 2-5).

---

## 6. Mechanism / Pathophysiology

### 6.1 Molecular Pathways

For ovarian dermoid cysts, the **H-Ras/MAPK signaling pathway** is a central mechanism in hereditary forms. The BMP15 C262T mutation leads to elevated H-Ras expression (3.2–8.3 fold) and MEK1 expression (3.9–5.8 fold) in mutant oocytes, promoting spontaneous parthenogenetic activation (liu2024araregermline pages 2-3). The mutation disrupts the balance between BMP15 and GDF9 signaling, altering SMAD2/3-MAPK pathway activation and shifting the ratio of heterodimeric signaling complexes (liu2024araregermline pages 6-7, liu2024araregermline pages 7-8).
- GO terms: GO:0000187 (activation of MAPK activity), GO:0007049 (cell cycle), GO:0044703 (multi-organism reproductive process)

For craniofacial and cutaneous dermoid cysts, the mechanism involves **aberrant midline fusion** during embryogenesis with entrapment of ectodermal tissue. This results in formation of epithelial-lined cavities containing keratinaceous material (quan2026pediatricnasaldermoid pages 2-3, wiener2021histologicfeaturesof pages 14-16).

### 6.2 Cellular Processes

The key cellular process in ovarian dermoid cysts is **parthenogenesis**: spontaneous activation of oocytes without fertilization, leading to development of a tumor containing elements of all three germ layers. Mature teratomas develop from oocytes after completed meiosis I with failed meiosis II, producing near-diploid genomes with limited somatic mutations and extensive allelic imbalances (moraru2023immatureteratomadiagnosis pages 2-4, pinto2023molecularbiologyof pages 7-9).
- GO terms: GO:0009566 (fertilization), GO:0007276 (gamete generation), GO:0051301 (cell division)
- CL terms: CL:0000023 (oocyte), CL:0000501 (granulosa cell)

### 6.3 Tissue Damage Mechanisms

Intracranial dermoid cyst rupture releases lipid-rich contents into the subarachnoid space, causing **chemical aseptic meningitis** through inflammatory reactions affecting cortical regions and adjacent brain structures (soto2025presentationofa pages 8-10, soto2025presentationofa pages 1-3).

---

## 7. Anatomical Structures Affected

### 7.1 Organ Level

**Primary organs:**
- Ovary (UBERON:0000992) — most common site for mature teratoma
- Brain (UBERON:0000955) — intracranial dermoid cysts, representing 0.04–0.6% of brain tumors (soto2025presentationofa pages 1-3)
- Nose (UBERON:0000004) — nasal dermoid sinus cysts, most common congenital midline nasal mass (kotowski2023thedifferentialdiagnosis pages 2-5)
- Eye/Orbit (UBERON:0004088) — orbital/periorbital and limbal dermoids
- Skin (UBERON:0002097) — cutaneous dermoid cysts

**Secondary involvement:**
- Meninges (chemical meningitis from intracranial rupture)
- Anterior cranial fossa (intracranial extension of nasal dermoids, ~20% of cases) (kotowski2023thedifferentialdiagnosis pages 2-5)
- Spinal cord (spinal dermoid cysts; cutaneous dermoid sinuses may extend to spinal canal) (wiener2021histologicfeaturesof pages 14-16)

### 7.2 Tissue and Cell Level

Dermoid cysts contain mature ectodermal derivatives:
- Keratinizing squamous epithelium (CL:0000237, squamous epithelial cell)
- Sebaceous glands (CL:0000317, sebum secreting cell)
- Hair follicles
- Apocrine glands
- Dense collagen stroma arranged concentrically around the cyst wall (wiener2021histologicfeaturesof pages 14-16, wiener2021histologicfeaturesof pages 16-18)

### 7.3 Localization

Intracranial dermoid cysts are classified by location as: (1) invasive to adjacent structures, (2) intradural, and (3) intracavernous, with suprasellar supratentorial lesions being most common in young adults (soto2025presentationofa pages 1-3). Nasal dermoid cysts are classified as: (1) superficial (Type 1), (2) sinus-tract type, and (3) intracranially extending type (quan2026pediatricnasaldermoid pages 2-3, quan2026pediatricnasaldermoid pages 4-5). Dermoid cysts are typically midline lesions and can be unilateral or bilateral in paired structures (e.g., ovaries).

---

## 8. Temporal Development

### 8.1 Onset

Dermoid cysts are **congenital** in origin, developing during embryogenesis (quan2026pediatricnasaldermoid pages 2-3, wiener2021histologicfeaturesof pages 14-16). However, clinical presentation varies by site:
- Nasal/orbital dermoids: typically present in infancy/childhood
- Intracranial dermoids: often diagnosed in young adults (20–30 years) (soto2025presentationofa pages 1-3)
- Ovarian dermoid cysts: typically diagnosed in reproductive-age women
- Cutaneous dermoids: variable age of recognition

### 8.2 Progression

Dermoid cysts are generally **slow-growing, chronic lesions** with a benign course. They do not spontaneously resolve and gradually enlarge over time. Critical complications include:
- **Ovarian torsion** and rupture for ovarian dermoid cysts
- **Chemical meningitis** from rupture of intracranial dermoid cysts (soto2025presentationofa pages 8-10)
- **Recurrent infections** for nasal dermoid sinuses (7% annual infection risk) (kotowski2023thedifferentialdiagnosis pages 2-5)
- **Malignant transformation** of ovarian mature teratomas occurs in approximately 1–2% of cases, typically squamous cell carcinoma

### 8.3 Recurrence Patterns

Recurrence after surgical excision depends on completeness of resection. For intracranial giant dermoid cysts, subtotal resection can lead to recurrence, as demonstrated by a case requiring two additional surgeries over 10 years, while gross total resection achieved no recurrence after 10 years of follow-up (soto2025presentationofa pages 1-3). For nasal dermoid cysts, recurrence is most commonly due to incomplete excision or involvement of fistulous tracts and cranial base (quan2026pediatricnasaldermoid pages 10-11).

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Intracranial dermoid cysts**: 0.04–0.6% of all brain tumors (soto2025presentationofa pages 1-3)
- **Ovarian germ cell tumors (including mature teratoma)**: 2–5% of ovarian cancers, with a yearly incidence of ~4 per 100,000; OGCTs account for approximately 11% of cancer diagnoses in children, adolescents, and young adults (saani2023clinicalchallengesin pages 9-10, pinto2023molecularbiologyof pages 1-3)
- **Nasal dermoid sinus cysts**: account for at least 60% of congenital developmental midline nasal masses (kotowski2023thedifferentialdiagnosis pages 2-5)
- **Orbital dermoid cysts**: common congenital periorbital lesions in pediatric populations

### 9.2 Inheritance Pattern

Most dermoid cysts are **sporadic** and non-hereditary. However, hereditary ovarian immature teratoma has been identified with **X-linked dominant inheritance** associated with BMP15 C262T mutation, exclusively affecting heterozygous female carriers (liu2024araregermline pages 3-4, liu2024araregermline pages 2-3). The disease may be classified into hereditary and sporadic types (liu2024araregermline pages 8-9).

### 9.3 Population Demographics

- **Sex ratio**: Ovarian dermoid cysts exclusively affect females. Intracranial dermoid cysts show no strong gender preference (soto2025presentationofa pages 6-8). Cutaneous dermoid sinuses affect both sexes.
- **Age distribution**: Ovarian — reproductive age; intracranial — young adults (20–30); nasal/orbital — infancy and childhood (soto2025presentationofa pages 1-3, quan2026pediatricnasaldermoid pages 2-3)
- **Geographic/racial distribution**: No strong racial predilection for intracranial dermoid cysts. Ovarian GCT histological subtype prevalence varies by race, with higher type 1 ovarian cancer prevalence in Asian populations compared to European/American populations.

---

## 10. Diagnostics

### 10.1 Imaging Studies

- **MRI**: Gold standard for intracranial and nasal dermoid cysts. Intracranial dermoid cysts appear hyperintense on T1-weighted images and hypointense on T2-weighted images due to lipid content (soto2025presentationofa pages 6-8). MRI is essential for evaluating nasal dermoid extension into intracranial structures (deftereou2025congenitalanomaliesof pages 6-6, quan2026pediatricnasaldermoid pages 4-5).
- **CT**: Complementary for osseous assessment in craniofacial dermoids and characterization of calcification/fat in ovarian dermoids (quan2026pediatricnasaldermoid pages 4-5).
- **Ultrasound**: First-line for ovarian dermoid cysts; bedside adjunct for nasal dermoids (quan2026pediatricnasaldermoid pages 4-5).
- RadLex terms: RID39428 (dermoid cyst)

### 10.2 Histopathology

Dermoid cysts are lined by squamous epithelium with prominent keratohyalin granules, containing lamellar keratin, hair fragments, and sebaceous secretions, surrounded by dense collagen with parallel arrangement. Multiple well-differentiated hair follicles, sebaceous glands, and occasional apocrine glands radiate from the cyst wall (wiener2021histologicfeaturesof pages 16-18). Key differentiating features from infundibular cysts include more abundant adnexal structures and concentric collagen arrangement (wiener2021histologicfeaturesof pages 16-18).
- SNOMED CT: 128978008 (Dermoid cyst)

### 10.3 Clinical Criteria

Nasal dermoid cysts are characterized as non-expansile, non-pulsatile, non-compressible masses that do not transilluminate and produce a **negative Furstenberg's sign** (no enlargement with jugular vein compression or Valsalva maneuver) (kotowski2023thedifferentialdiagnosis pages 2-5). Biopsy is contraindicated for nasal dermoids (deftereou2025congenitalanomaliesof pages 6-6).

### 10.4 Differential Diagnosis

- Intracranial: Epidermoid cyst, arachnoid cyst, lipoma, craniopharyngioma
- Nasal: Encephalocele, nasal glioma (glial heterotopia) (kotowski2023thedifferentialdiagnosis pages 2-5)
- Ovarian: Endometrioma, mucinous cystadenoma, other ovarian cysts
- Cutaneous: Trichofolliculoma, infundibular (epidermoid) cyst (wiener2021histologicfeaturesof pages 16-18)

### 10.5 Genetic Testing

Genetic testing is not routinely indicated for sporadic dermoid cysts. For suspected hereditary ovarian teratoma, BMP15 mutation analysis may be considered as a potential biomarker for molecular diagnosis and genetic screening in high-risk families (liu2024araregermline pages 8-9, liu2024araregermline pages 7-8).

---

## 11. Outcome/Prognosis

### 11.1 Survival and Mortality

Dermoid cysts are benign lesions with excellent survival rates. Mature ovarian teratomas have an excellent overall survival rate following surgical excision, with fertility preservation possible through conservative surgery (moraru2023immatureteratomadiagnosis pages 2-4). Intracranial dermoid cysts carry minimal mortality risk when completely resected, but subtotal resection risks recurrence (soto2025presentationofa pages 1-3). Immature teratomas also have good prognoses, with excellent overall survival (moraru2023immatureteratomadiagnosis pages 2-4).

### 11.2 Complications

- **Ovarian**: Torsion, rupture (with chemical peritonitis), malignant transformation (~1–2%)
- **Intracranial**: Chemical aseptic meningitis from rupture; recurrence after incomplete resection (soto2025presentationofa pages 8-10)
- **Nasal**: Recurrent infection (50% by age 4, >90% by age 9 when sinus opening present); potential intracranial complications including meningitis, cerebral abscess (kotowski2023thedifferentialdiagnosis pages 2-5)

### 11.3 Prognostic Factors

Completeness of surgical excision is the primary prognostic determinant. Gross total resection of intracranial dermoid cysts prevents recurrence (soto2025presentationofa pages 1-3). For nasal dermoid cysts, preoperative imaging to identify intracranial extension and meticulous complete excision reduce recurrence risk (quan2026pediatricnasaldermoid pages 8-9, quan2026pediatricnasaldermoid pages 10-11).

---

## 12. Treatment

### 12.1 Surgical Interventions (MAXO:0000004 — surgical procedure)

Surgery is the definitive treatment for all dermoid cyst subtypes:

**Ovarian dermoid cysts:**
- Fertility-sparing cystectomy or oophorectomy, typically via laparoscopy (MAXO:0001185 — laparoscopic surgery)
- Clinical trial NCT02009228 evaluated single-port laparoscopic cystectomy as potentially preferable for managing ovarian dermoid cysts (NCT06816316 chunk 2)
- NCT05054946 evaluated the effect of laparoscopic surgery on ovarian reserve according to cyst type

**Intracranial dermoid cysts:**
- Craniotomy (frontal, temporal, frontotemporal, or transcranial approaches) with goal of gross total resection (soto2025presentationofa pages 6-8, soto2025presentationofa pages 8-10)
- Microsurgical techniques and advanced visualization (exoscope) are essential for safe resection near neurovascular structures (soto2025presentationofa pages 8-10)
- The Reyes-Velez classification system has been proposed to guide surgical planning and predict complications (soto2025presentationofa pages 1-3)

**Nasal dermoid sinus cysts:**
- External rhinoplasty approach for adequate exposure and en bloc removal (quan2026pediatricnasaldermoid pages 8-9)
- Endoscopic endonasal techniques for selected cases
- Combined intracranial–extracranial approaches for cases with intracranial extension (quan2026pediatricnasaldermoid pages 10-11)
- Multidisciplinary team management (otolaryngology, neurosurgery, plastic surgery) is recommended (quan2026pediatricnasaldermoid pages 8-9, quan2026pediatricnasaldermoid pages 10-11)

**Orbital dermoid cysts:**
- Complete excision avoiding rupture
- Clinical trial NCT06816316 evaluated the role of 70% ethyl alcohol versus saline for intraoperative cleaning of accidentally opened angular dermoid cysts to prevent recurrence (NCT06816316 chunk 2)

**Limbal dermoid cysts:**
- Observation for small asymptomatic lesions; corneal autograft or lamellar keratoplasty for visually significant lesions
- Clinical trial NCT03217461 evaluated corneal autograft for limbal dermoid

### 12.2 Supportive Care

Long-term follow-up of 1–3 years with imaging surveillance is recommended after nasal dermoid cyst excision (quan2026pediatricnasaldermoid pages 10-11). Perioperative infection control is critical for nasal dermoid sinuses (quan2026pediatricnasaldermoid pages 8-9).

---

## 13. Prevention

### 13.1 Primary Prevention

No primary prevention strategies exist for dermoid cysts, as they are congenital developmental lesions.

### 13.2 Secondary Prevention (Early Detection)

For nasal dermoid sinus cysts, early surgical excision is recommended to prevent the cumulative infection risk (7% per year) and potential intracranial complications (kotowski2023thedifferentialdiagnosis pages 2-5). Prenatal imaging may detect some ovarian cysts, but prenatal detection of dermoid cysts specifically is uncommon.

### 13.3 Genetic Counseling

For families with hereditary ovarian teratoma, BMP15 mutation analysis may facilitate identification of at-risk heterozygous female carriers and enable genetic counseling and surveillance (liu2024araregermline pages 8-9, liu2024araregermline pages 7-8).

### 13.4 Tertiary Prevention

Complete surgical excision is the key strategy for preventing complications and recurrence. Standardized follow-up protocols with imaging reduce the risk of missed recurrence (quan2026pediatricnasaldermoid pages 10-11).

---

## 14. Other Species / Natural Disease

### 14.1 Canine Dermoid Cysts

Dermoid cysts occur naturally in dogs and are more common than in cats. They represent focal reduplications of skin resulting from developmental anomalies and primarily affect young animals under 2 years of age (wiener2021histologicfeaturesof pages 14-16). **Breed predisposition** exists, particularly in:
- **Rhodesian Ridgeback** — often multiple dorsal midline cysts (dermoid sinuses)
- **Boxer**
- **Kerry Blue Terrier**
- **English Bulldog**
- **Shih Tzu**
- **Saint Bernard** — documented with multiple dermoid sinuses on the head (wiener2021histologicfeaturesof pages 19-19)

Lesions are most commonly located on the dorsal midline but can extend to the spinal canal and dura mater (wiener2021histologicfeaturesof pages 14-16). The VBO identifier for Rhodesian Ridgeback is VBO:0200817.

### 14.2 Feline Dermoid Cysts

Dermoid cysts in cats are less common than in dogs and are particularly found on the lateral neck or shoulder (wiener2021histologicfeaturesof pages 16-18). Histologically, they are identical to canine dermoid cysts.

### 14.3 Non-Human Primates

Ovarian teratomas occur naturally in nonhuman primates, with most ovarian tumors reported in baboons (Papio spp.) (wiener2021histologicfeaturesof pages 14-16).

### 14.4 Mouse Models

A CRISPR/Cas9-engineered **Bmp15 R86C knock-in mouse model** (C57BL/6 background) has been developed to study hereditary ovarian teratoma. Mice carrying the mutation (equivalent to human BMP15 R88C) show significantly increased spontaneous parthenogenetic activation of oocytes, with one transgenic mouse developing an OIT phenotype by 6 months. The mutation causes ovarian overgrowth (>2-fold larger than wild-type) (liu2024araregermline pages 4-6, liu2024araregermline pages 8-8). This model recapitulates key aspects of the human disease.

---

## 15. Model Organisms

### 15.1 Genetic Models

- **Bmp15 C262T knock-in mouse (C57BL/6)**: Generated by CRISPR/Cas9 genome editing; demonstrates increased parthenogenetic activation rates and teratoma development. Phenotype recapitulation includes ovarian teratoma formation and ovarian enlargement (liu2024araregermline pages 4-6, liu2024araregermline pages 8-8).
- Model limitations: Low penetrance of OIT phenotype in mice (only one mouse developed teratoma), species-specific differences in BMP15 signaling, and difficulty obtaining primary oocytes for mechanistic studies (liu2024araregermline pages 7-8).

### 15.2 Applications

The Bmp15 mutant mouse model enables investigation of:
- Parthenogenetic mechanisms of teratoma formation
- BMP15/GDF9 signaling balance in oocyte development
- Preclinical testing of potential preventive interventions
- Validation of genetic biomarkers for screening (liu2024araregermline pages 8-9)

### 15.3 Canine Natural Models

Rhodesian Ridgeback dermoid sinuses serve as natural models for studying congenital dermoid cyst pathogenesis, with well-documented breed predisposition and dorsal midline localization paralleling human nasal/spinal dermoid sinuses (wiener2021histologicfeaturesof pages 14-16).

---

## Summary

Dermoid cysts are a heterogeneous group of benign developmental lesions arising from ectodermal tissue entrapment during embryogenesis. They occur at diverse anatomical sites including the ovary (as mature cystic teratomas), cranium, nasal midline, orbit, skin, and ocular surface. The molecular understanding of ovarian dermoid cysts has been significantly advanced by the 2024 identification of a causal BMP15 germline mutation causing hereditary ovarian teratoma through enhanced oocyte parthenogenetic activation via H-Ras/MAPK pathway dysregulation (liu2024araregermline pages 3-4, liu2024araregermline pages 2-3). Epigenetic studies reveal distinct DNA methylation patterns in germ cell tumor subtypes, with mature teratomas showing characteristic imprinting abnormalities consistent with their parthenogenetic origin (pinto2023molecularbiologyof pages 11-12). Surgical excision remains the definitive treatment across all anatomical subtypes, with completeness of resection being the primary determinant of recurrence and long-term outcome (soto2025presentationofa pages 1-3, quan2026pediatricnasaldermoid pages 10-11). Nasal dermoid sinuses carry significant childhood infection risk (50% by age 4) warranting early intervention (kotowski2023thedifferentialdiagnosis pages 2-5). Intracranial dermoid cysts, though rare (0.04–0.6% of brain tumors), require careful neurosurgical planning due to potential for chemical meningitis upon rupture (soto2025presentationofa pages 1-3, soto2025presentationofa pages 8-10). Natural models in dogs (particularly Rhodesian Ridgebacks) and the CRISPR-engineered Bmp15 mutant mouse provide valuable platforms for studying dermoid cyst pathogenesis across species (wiener2021histologicfeaturesof pages 14-16, liu2024araregermline pages 8-8).

References

1. (quan2026pediatricnasaldermoid pages 2-3): Shan Quan, Li He, Jiangqiao Geng, and Juan Wang. Pediatric nasal dermoid sinus cysts: advances in pathogenesis, management strategies, and translational research—a multidisciplinary management perspective. Frontiers in Pediatrics, Jan 2026. URL: https://doi.org/10.3389/fped.2025.1708853, doi:10.3389/fped.2025.1708853. This article has 3 citations.

2. (wiener2021histologicfeaturesof pages 14-16): Dominique J. Wiener. Histologic features of hair follicle neoplasms and cysts in dogs and cats: a diagnostic guide. Journal of Veterinary Diagnostic Investigation, 33:479-497, Mar 2021. URL: https://doi.org/10.1177/1040638721993565, doi:10.1177/1040638721993565. This article has 44 citations and is from a peer-reviewed journal.

3. (soto2025presentationofa pages 1-3): Gervith Reyes Soto, Daniel Alejandro Vega Moreno, Carlos Castillo Rangel, Vladmir Nikolenko, Mario Alejandro Fulcar, Neysa Sabrina Vasquez Segura, Tshiunza Mpoyi Chérubin, Mario Antonio Furcal Aybar, Andreina Rosario Rosario, and Manuel De Jesus Encarnacion Ramirez. Presentation of a new imaging classification for giant dermoid cyst. case report and literature review. Unknown journal, Jan 2025. URL: https://doi.org/10.21203/rs.3.rs-5685800/v1, doi:10.21203/rs.3.rs-5685800/v1.

4. (saani2023clinicalchallengesin pages 9-10): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 86 citations.

5. (pinto2023molecularbiologyof pages 1-3): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 22 citations.

6. (moraru2023immatureteratomadiagnosis pages 2-4): Liviu Moraru, Melinda-Ildiko Mitranovici, Diana Maria Chiorean, Marius Coroș, Raluca Moraru, Ioan Emilian Oală, and Sabin Gligore Turdean. Immature teratoma: diagnosis and management—a review of the literature. Diagnostics, 13:1516, Apr 2023. URL: https://doi.org/10.3390/diagnostics13091516, doi:10.3390/diagnostics13091516. This article has 68 citations.

7. (NCT06816316 chunk 2): Mohamed Yasser Sayed Saif. Role of Alcohol in Prevention of Recurrence of the Accidentally Opened Angular Dermoid Cyst. Beni-Suef University. 2019. ClinicalTrials.gov Identifier: NCT06816316

8. (soto2025presentationofa pages 6-8): Gervith Reyes Soto, Daniel Alejandro Vega Moreno, Carlos Castillo Rangel, Vladmir Nikolenko, Mario Alejandro Fulcar, Neysa Sabrina Vasquez Segura, Tshiunza Mpoyi Chérubin, Mario Antonio Furcal Aybar, Andreina Rosario Rosario, and Manuel De Jesus Encarnacion Ramirez. Presentation of a new imaging classification for giant dermoid cyst. case report and literature review. Unknown journal, Jan 2025. URL: https://doi.org/10.21203/rs.3.rs-5685800/v1, doi:10.21203/rs.3.rs-5685800/v1.

9. (soto2025presentationofa pages 8-10): Gervith Reyes Soto, Daniel Alejandro Vega Moreno, Carlos Castillo Rangel, Vladmir Nikolenko, Mario Alejandro Fulcar, Neysa Sabrina Vasquez Segura, Tshiunza Mpoyi Chérubin, Mario Antonio Furcal Aybar, Andreina Rosario Rosario, and Manuel De Jesus Encarnacion Ramirez. Presentation of a new imaging classification for giant dermoid cyst. case report and literature review. Unknown journal, Jan 2025. URL: https://doi.org/10.21203/rs.3.rs-5685800/v1, doi:10.21203/rs.3.rs-5685800/v1.

10. (kotowski2023thedifferentialdiagnosis pages 2-5): Michael R. Kotowski. The differential diagnosis of congenital developmental midline nasal masses: histopathological, clinical, and radiological aspects. Diagnostics, 13:2796, Aug 2023. URL: https://doi.org/10.3390/diagnostics13172796, doi:10.3390/diagnostics13172796. This article has 9 citations.

11. (deftereou2025congenitalanomaliesof pages 6-6): T. Deftereou, V. Karapepera, Stergios Lialiaris, George Fotiadis, Konstantinos Chaidas, and Michail Katotomichelakis. Congenital anomalies of the nose: from embryologic to surgical treatment. Cureus, Aug 2025. URL: https://doi.org/10.7759/cureus.89397, doi:10.7759/cureus.89397. This article has 1 citations.

12. (quan2026pediatricnasaldermoid pages 4-5): Shan Quan, Li He, Jiangqiao Geng, and Juan Wang. Pediatric nasal dermoid sinus cysts: advances in pathogenesis, management strategies, and translational research—a multidisciplinary management perspective. Frontiers in Pediatrics, Jan 2026. URL: https://doi.org/10.3389/fped.2025.1708853, doi:10.3389/fped.2025.1708853. This article has 3 citations.

13. (quan2026pediatricnasaldermoid pages 8-9): Shan Quan, Li He, Jiangqiao Geng, and Juan Wang. Pediatric nasal dermoid sinus cysts: advances in pathogenesis, management strategies, and translational research—a multidisciplinary management perspective. Frontiers in Pediatrics, Jan 2026. URL: https://doi.org/10.3389/fped.2025.1708853, doi:10.3389/fped.2025.1708853. This article has 3 citations.

14. (quan2026pediatricnasaldermoid pages 10-11): Shan Quan, Li He, Jiangqiao Geng, and Juan Wang. Pediatric nasal dermoid sinus cysts: advances in pathogenesis, management strategies, and translational research—a multidisciplinary management perspective. Frontiers in Pediatrics, Jan 2026. URL: https://doi.org/10.3389/fped.2025.1708853, doi:10.3389/fped.2025.1708853. This article has 3 citations.

15. (wiener2021histologicfeaturesof pages 16-18): Dominique J. Wiener. Histologic features of hair follicle neoplasms and cysts in dogs and cats: a diagnostic guide. Journal of Veterinary Diagnostic Investigation, 33:479-497, Mar 2021. URL: https://doi.org/10.1177/1040638721993565, doi:10.1177/1040638721993565. This article has 44 citations and is from a peer-reviewed journal.

16. (pinto2023molecularbiologyof pages 7-9): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 22 citations.

17. (liu2024araregermline pages 3-4): Yakun Liu, Hong-wei Fan, Xi Kang, Yuntao Hao, Na Wang, Hui Zheng, Yan Li, and Shan Kang. A rare germline bmp15 missense mutation causes hereditary ovarian immature teratoma in human. Proceedings of the National Academy of Sciences of the United States of America, Mar 2024. URL: https://doi.org/10.1073/pnas.2310409121, doi:10.1073/pnas.2310409121. This article has 4 citations and is from a highest quality peer-reviewed journal.

18. (liu2024araregermline pages 2-3): Yakun Liu, Hong-wei Fan, Xi Kang, Yuntao Hao, Na Wang, Hui Zheng, Yan Li, and Shan Kang. A rare germline bmp15 missense mutation causes hereditary ovarian immature teratoma in human. Proceedings of the National Academy of Sciences of the United States of America, Mar 2024. URL: https://doi.org/10.1073/pnas.2310409121, doi:10.1073/pnas.2310409121. This article has 4 citations and is from a highest quality peer-reviewed journal.

19. (pinto2023molecularbiologyof pages 3-4): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 22 citations.

20. (liu2024araregermline pages 1-2): Yakun Liu, Hong-wei Fan, Xi Kang, Yuntao Hao, Na Wang, Hui Zheng, Yan Li, and Shan Kang. A rare germline bmp15 missense mutation causes hereditary ovarian immature teratoma in human. Proceedings of the National Academy of Sciences of the United States of America, Mar 2024. URL: https://doi.org/10.1073/pnas.2310409121, doi:10.1073/pnas.2310409121. This article has 4 citations and is from a highest quality peer-reviewed journal.

21. (liu2024araregermline pages 6-7): Yakun Liu, Hong-wei Fan, Xi Kang, Yuntao Hao, Na Wang, Hui Zheng, Yan Li, and Shan Kang. A rare germline bmp15 missense mutation causes hereditary ovarian immature teratoma in human. Proceedings of the National Academy of Sciences of the United States of America, Mar 2024. URL: https://doi.org/10.1073/pnas.2310409121, doi:10.1073/pnas.2310409121. This article has 4 citations and is from a highest quality peer-reviewed journal.

22. (liu2024araregermline pages 4-6): Yakun Liu, Hong-wei Fan, Xi Kang, Yuntao Hao, Na Wang, Hui Zheng, Yan Li, and Shan Kang. A rare germline bmp15 missense mutation causes hereditary ovarian immature teratoma in human. Proceedings of the National Academy of Sciences of the United States of America, Mar 2024. URL: https://doi.org/10.1073/pnas.2310409121, doi:10.1073/pnas.2310409121. This article has 4 citations and is from a highest quality peer-reviewed journal.

23. (liu2024araregermline pages 7-8): Yakun Liu, Hong-wei Fan, Xi Kang, Yuntao Hao, Na Wang, Hui Zheng, Yan Li, and Shan Kang. A rare germline bmp15 missense mutation causes hereditary ovarian immature teratoma in human. Proceedings of the National Academy of Sciences of the United States of America, Mar 2024. URL: https://doi.org/10.1073/pnas.2310409121, doi:10.1073/pnas.2310409121. This article has 4 citations and is from a highest quality peer-reviewed journal.

24. (pinto2023molecularbiologyof pages 11-12): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 22 citations.

25. (moraru2023immatureteratomadiagnosis pages 13-15): Liviu Moraru, Melinda-Ildiko Mitranovici, Diana Maria Chiorean, Marius Coroș, Raluca Moraru, Ioan Emilian Oală, and Sabin Gligore Turdean. Immature teratoma: diagnosis and management—a review of the literature. Diagnostics, 13:1516, Apr 2023. URL: https://doi.org/10.3390/diagnostics13091516, doi:10.3390/diagnostics13091516. This article has 68 citations.

26. (liu2024araregermline pages 8-9): Yakun Liu, Hong-wei Fan, Xi Kang, Yuntao Hao, Na Wang, Hui Zheng, Yan Li, and Shan Kang. A rare germline bmp15 missense mutation causes hereditary ovarian immature teratoma in human. Proceedings of the National Academy of Sciences of the United States of America, Mar 2024. URL: https://doi.org/10.1073/pnas.2310409121, doi:10.1073/pnas.2310409121. This article has 4 citations and is from a highest quality peer-reviewed journal.

27. (wiener2021histologicfeaturesof pages 19-19): Dominique J. Wiener. Histologic features of hair follicle neoplasms and cysts in dogs and cats: a diagnostic guide. Journal of Veterinary Diagnostic Investigation, 33:479-497, Mar 2021. URL: https://doi.org/10.1177/1040638721993565, doi:10.1177/1040638721993565. This article has 44 citations and is from a peer-reviewed journal.

28. (liu2024araregermline pages 8-8): Yakun Liu, Hong-wei Fan, Xi Kang, Yuntao Hao, Na Wang, Hui Zheng, Yan Li, and Shan Kang. A rare germline bmp15 missense mutation causes hereditary ovarian immature teratoma in human. Proceedings of the National Academy of Sciences of the United States of America, Mar 2024. URL: https://doi.org/10.1073/pnas.2310409121, doi:10.1073/pnas.2310409121. This article has 4 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Dermoid_Cyst-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Dermoid_Cyst-deep-research-falcon_artifacts/artifact-01.md)