---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-30T19:39:05.050094'
end_time: '2026-07-30T19:48:41.686471'
duration_seconds: 576.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Angioedema
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hereditary_Angioedema-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Angioedema
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Angioedema** covering all of the
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
- **Disease Name:** Hereditary Angioedema
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Angioedema** covering all of the
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


# Hereditary Angioedema: Disease-Characteristics Research Report

## Executive summary

Hereditary angioedema (HAE) is a rare, usually autosomal-dominant disorder causing recurrent, self-limited, nonpruritic swelling of subcutaneous and submucosal tissues without urticaria. Most disease is caused by heterozygous **SERPING1** variants producing quantitative C1-inhibitor deficiency (HAE type I) or dysfunctional C1 inhibitor (type II). Less common HAE with normal C1 inhibitor (HAE-nC1INH) is genetically heterogeneous. Excess bradykinin and loss of endothelial-barrier integrity are the final common mechanisms; consequently, antihistamines, glucocorticoids, and epinephrine generally do not control established HAE swelling. Laryngeal attacks are medical emergencies.

The principal recent developments are broader genomic testing, recognition of endothelial-barrier mechanisms, oral and long-acting kallikrein/bradykinin-pathway therapies, RNA silencing, and in-vivo CRISPR editing of **KLKB1**. Nevertheless, evidence for many HAE-nC1INH genotypes remains based on small families or expert consensus rather than randomized trials.

## 1. Disease information

### Definition and classification

HAE comprises intermittent, localized, self-limited episodes of increased vascular permeability and tissue edema. Attacks affect skin, gastrointestinal mucosa, upper airway, oral cavity, face, genital/urogenital tissues, or combinations thereof. The clinically useful classification is:

1. **HAE-C1INH type I:** low C1-INH antigen and function, usually from a loss-of-function **SERPING1** allele.
2. **HAE-C1INH type II:** normal/high C1-INH antigen but low function, usually from a dysfunctional **SERPING1** allele.
3. **HAE-nC1INH:** normal C1-INH quantity and activity, with genetically defined or unknown subtypes. “Type III” is now discouraged because it obscures molecular heterogeneity. HAE-nC1INH was first described in 2000. (zuraw2025hereditaryangioedemawith pages 1-2, tutunaru2024unveilingthecomplexities pages 1-2)

A 2024 review summarized HAE as approximately 2% of clinical angioedema and estimated type I at 80–85%, type II at 15–20%, with HAE-nC1INH substantially rarer; percentages vary because ascertainment and subtype definitions differ. (tutunaru2024unveilingthecomplexities pages 2-4, tutunaru2024unveilingthecomplexities pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0019623, hereditary angioedema. More specific entries include MONDO:0033946, HAE with C1-INH deficiency; MONDO:0015053, type I; MONDO:0015054, type II; and MONDO:0012526, historically “type III.” (OpenTargets Search: hereditary angioedema)
- **OMIM:** commonly mapped disease entries include HAE type I/II (#106100) and factor-XII-associated HAE with normal C1-INH (#610618). Database versioning should be checked before ingestion.
- **Orphanet:** ORPHA:91378 is widely used for hereditary angioedema; molecular subtypes have child terms.
- **ICD-10-CM:** D84.1, defects in the complement system, includes C1 esterase inhibitor deficiency/HAE but is not molecularly specific.
- **ICD-11:** HAE is represented under complement-system defects; implementation-specific coding should be verified against the current ICD-11 release.
- **MeSH:** “Hereditary Angioedema Types I and II” and related angioedema/C1-inhibitor headings.
- **Synonyms:** hereditary angioneurotic edema/oedema, hereditary angio-oedema, HAE, C1-INH-HAE, C1 esterase inhibitor deficiency, HAE-1, HAE-2, HAE-nC1INH.

This report synthesizes **aggregated disease-level resources, reviews, guidelines, trials, and cohorts**, not identifiable EHR records. Individual case/family studies are explicitly identified below.

The subtype-oriented summary is:

| Subtype/entity | Principal gene/protein | C4 / C1-INH antigen / function pattern | Core mechanism | Typical clinical clue | Targeted treatment classes |
|---|---|---|---|---|---|
| HAE type I (HAE-C1INH-1) | **SERPING1** / C1 inhibitor | **Low C4; low C1-INH antigen; low C1-INH function** (classic pattern) (caballero2022medicalalgorithmmanagement pages 2-2, tutunaru2024unveilingthecomplexities pages 1-2) | C1-INH deficiency permits excess contact-system activation, kallikrein activity, and **bradykinin** generation → endothelial leak (tutunaru2024unveilingthecomplexities pages 1-2, recke2025statusquoand pages 1-2) | Childhood/adolescent onset, recurrent nonurticarial skin swelling, abdominal attacks, possible laryngeal edema; attacks often last 2-5 days untreated (tutunaru2024unveilingthecomplexities pages 2-4, recke2025statusquoand pages 1-2) | On-demand **pdC1-INH/rhC1-INH**, **icatibant**, **ecallantide**; long-term prophylaxis **SC/IV C1-INH**, **lanadelumab**, **berotralstat** (johnson2025unravelingangioedemadiagnostic pages 9-10, caballero2022medicalalgorithmmanagement pages 2-2) |
| HAE type II (HAE-C1INH-2) | **SERPING1** / dysfunctional C1 inhibitor | **Low C4; normal or elevated C1-INH antigen; low C1-INH function** (caballero2022medicalalgorithmmanagement pages 2-2) | Dysfunctional C1-INH fails to restrain kallikrein-kinin and related protease cascades → **bradykinin-mediated** angioedema (caballero2022medicalalgorithmmanagement pages 2-2, tutunaru2024unveilingthecomplexities pages 1-2) | Similar phenotype to type I; family history may be present; recurrent angioedema without wheals and poor response to antihistamines/steroids (tutunaru2024unveilingthecomplexities pages 1-2, caballero2022medicalalgorithmmanagement pages 2-2) | Same targeted classes as HAE type I: C1-INH replacement, B2 receptor antagonism, kallikrein inhibition; prophylaxis with C1-INH, lanadelumab, berotralstat (johnson2025unravelingangioedemadiagnostic pages 9-10, caballero2022medicalalgorithmmanagement pages 2-2) |
| HAE-nC1INH, **F12**-associated | **F12** / factor XII | Usually **normal C4, normal C1-INH antigen, normal C1-INH function** (zuraw2025hereditaryangioedemawith pages 1-2, caballero2022medicalalgorithmmanagement pages 2-2) | Increased factor XII-driven contact activation with downstream **bradykinin** excess (zuraw2025hereditaryangioedemawith pages 1-2, santacroce2021thegeneticsof pages 8-9) | Often estrogen-sensitive; attacks can be triggered/worsened by estrogens; normal complement studies despite convincing hereditary angioedema phenotype (tutunaru2024unveilingthecomplexities pages 2-4, zuraw2025hereditaryangioedemawith pages 1-2) | Evidence-based use in practice/expert consensus: **icatibant**, **C1-INH**, kallikrein-pathway prophylaxis in selected patients; evidence base weaker than for HAE-C1INH (zuraw2025hereditaryangioedemawith pages 1-2) |
| HAE-nC1INH, **PLG**-associated | **PLG** / plasminogen | Usually **normal C4, normal C1-INH antigen, normal C1-INH function** (zuraw2025hereditaryangioedemawith pages 1-2, rozevska2024hereditaryoracquired? pages 2-3) | Likely plasminogen/plasmin-linked promotion of **bradykinin** formation; mechanistic evidence supports bradykinin-mediated disease (zuraw2025hereditaryangioedemawith pages 1-2, santacroce2021thegeneticsof pages 8-9) | Recurrent hereditary angioedema phenotype with normal C1-INH studies; diagnosis generally requires genetics when suspected clinically (zuraw2025hereditaryangioedemawith pages 1-2, rozevska2024hereditaryoracquired? pages 2-3) | Often treated with bradykinin-pathway agents used for HAE-C1INH; response reported but evidence remains limited/consensus-based (zuraw2025hereditaryangioedemawith pages 1-2) |
| HAE-nC1INH, **ANGPT1**-associated | **ANGPT1** / angiopoietin-1 | Usually **normal C4, normal C1-INH antigen, normal C1-INH function** (zuraw2025hereditaryangioedemawith pages 1-2, santacroce2021thegeneticsof pages 8-9) | **Endothelial barrier dysfunction**/vascular permeability mechanism rather than pure upstream C1-INH deficiency; may intersect with bradykinin pathways (gao2025expandingthegenetic pages 1-2, zuraw2025hereditaryangioedemawith pages 1-2) | Familial nonurticarial angioedema with normal complement/C1-INH studies; clinical heterogeneity (zuraw2025hereditaryangioedemawith pages 1-2, gao2025expandingthegenetic pages 1-2) | No subtype-specific approved therapy; HAE-directed acute/prophylactic agents are used empirically, with expert-opinion support and variable response (zuraw2025hereditaryangioedemawith pages 1-2, gao2025expandingthegenetic pages 1-2) |
| HAE-nC1INH, **KNG1**-associated | **KNG1** / high-molecular-weight kininogen precursor | Usually **normal C4, normal C1-INH antigen, normal C1-INH function** (zuraw2025hereditaryangioedemawith pages 1-2, santacroce2021thegeneticsof pages 8-9) | Altered kininogen biology with downstream **bradykinin** dysregulation (santacroce2021thegeneticsof pages 8-9, zuraw2025hereditaryangioedemawith pages 1-2) | Hereditary angioedema phenotype despite normal standard complement workup; often requires sequencing for confirmation (rozevska2024hereditaryoracquired? pages 2-3, santacroce2021thegeneticsof pages 8-9) | Managed with standard HAE targeted classes in practice; subtype-specific efficacy evidence remains sparse (zuraw2025hereditaryangioedemawith pages 1-2) |
| HAE-nC1INH, **MYOF**-associated | **MYOF** / myoferlin | Usually **normal C4, normal C1-INH antigen, normal C1-INH function** (gao2025expandingthegenetic pages 1-2) | Proposed endothelial/vesicular membrane regulation abnormality; not as securely established as classic bradykinin-only forms (gao2025expandingthegenetic pages 1-2, santacroce2021thegeneticsof pages 8-9) | In one cohort, recurrent edema with **prolonged duration**; treatment response to lanadelumab variable (gao2025expandingthegenetic pages 1-2) | HAE-directed acute/prophylactic therapies used off-label/empirically; **variable** response reported (gao2025expandingthegenetic pages 1-2) |
| HAE-nC1INH, **HS3ST6**-associated | **HS3ST6** / heparan sulfate 3-O-sulfotransferase 6 | Usually **normal C4, normal C1-INH antigen, normal C1-INH function** (gao2025expandingthegenetic pages 1-2, santacroce2021thegeneticsof pages 8-9) | Proposed endothelial/glycocalyx or permeability regulation defect; causal confidence lower than **F12/PLG** (gao2025expandingthegenetic pages 1-2, santacroce2021thegeneticsof pages 8-9) | Reported association with **refractory angioedema** and persistent lower-extremity involvement in a small cohort (gao2025expandingthegenetic pages 1-2) | Empiric use of HAE-directed agents; personalized management needed; evidence limited (gao2025expandingthegenetic pages 1-2) |
| HAE-nC1INH, rarer/newer candidate genes with weaker evidence | Reported/candidate: **CPN1, DAB2IP**; some literature also discusses other rare candidates with uncertain validation | Usually **normal standard complement/C1-INH studies** (gao2025expandingthegenetic pages 1-2, recke2025statusquoand pages 1-2) | Mixed hypotheses: bradykinin dysregulation and/or **VEGF/endothelial permeability** pathways; evidence weaker and not yet equivalent to established genes (gao2025expandingthegenetic pages 1-2, recke2025statusquoand pages 1-2) | Consider when phenotype is convincing but common genes are negative; diagnosis remains expert-dependent and may change after re-evaluation (rozevska2024hereditaryoracquired? pages 2-3, gao2025expandingthegenetic pages 1-2) | No gene-specific approved treatment; use individualized HAE-directed acute/prophylactic therapy with cautious interpretation of response (rozevska2024hereditaryoracquired? pages 2-3, gao2025expandingthegenetic pages 1-2) |
| **Acquired C1-INH deficiency** (important differential) | Acquired loss/consumption of **C1-INH** rather than inherited pathogenic variant | **Low C4; low C1-INH function; often low C1-INH antigen; C1q often low** (helps distinguish from hereditary C1-INH deficiency) (caballero2022medicalalgorithmmanagement pages 2-2, tutunaru2024unveilingthecomplexities pages 1-2) | Acquired C1-INH depletion/consumption with bradykinin-mediated angioedema (caballero2022medicalalgorithmmanagement pages 2-2, tutunaru2024unveilingthecomplexities pages 1-2) | Usually later onset, absent family history, evaluation for acquired causes warranted; C1q more informative here than in routine pediatric hereditary testing (tutunaru2024unveilingthecomplexities pages 1-2, caballero2022medicalalgorithmmanagement pages 2-2) | Acute therapy may overlap with HAE agents (C1-INH, icatibant, kallikrein-pathway agents), but management also requires treating the underlying acquired disorder (tutunaru2024unveilingthecomplexities pages 1-2, caballero2022medicalalgorithmmanagement pages 2-2) |


*Table: This table summarizes the main hereditary angioedema entities and the key differential of acquired C1-INH deficiency, highlighting diagnostic laboratory patterns, mechanisms, clinical clues, and targeted treatment classes. It is designed as a compact reference for subtype-oriented interpretation of HAE workup and management.*

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factors

HAE is principally genetic. In HAE-C1INH, reduced effective C1-INH removes inhibition of factor XIIa and plasma kallikrein, allowing cleavage of high-molecular-weight kininogen and excessive bradykinin formation. Bradykinin activates endothelial B2 receptors and increases paracellular fluid movement. HAE is therefore not primarily an IgE-mediated allergy. (OpenTargets Search: hereditary angioedema, tutunaru2024unveilingthecomplexities pages 1-2, caballero2022medicalalgorithmmanagement pages 2-2)

### Genetic risk

The strongest association is **SERPING1**. OpenTargets also supports disease associations involving **F12, PLG, KNG1, ANGPT1, MYOF**, and **HS3ST6**, while **KLKB1** and **BDKRB2** are strongly supported therapeutic-mechanism targets rather than usual germline causes. (OpenTargets Search: hereditary angioedema)

Approximately one quarter of HAE-C1INH cases are reported without an affected parent and may reflect de-novo **SERPING1** variation; absence of family history therefore does not exclude HAE. Each child of a heterozygous affected person has a 50% transmission probability. (tutunaru2024unveilingthecomplexities pages 2-4)

### Attack-promoting environmental and physiological factors

Mechanical trauma, dental work, surgery, intubation, infection, psychological stress, fatigue, and hormonal changes can precipitate attacks, but many attacks have no identifiable trigger. Estrogen-containing contraception, estrogen replacement, pregnancy in some patients, and puberty can increase attacks—especially in HAE-FXII and some HAE-nC1INH phenotypes. ACE inhibitors reduce bradykinin degradation and should generally be avoided. These exposures modify attack expression rather than cause the inherited disease.

### Protective factors

No validated germline “protective allele” prevents HAE. Reduced estrogen exposure or withdrawal of exogenous estrogen may lower attack activity in estrogen-sensitive disease. Avoiding ACE inhibitors and known individual mechanical triggers is prudent. Effective on-demand treatment and prophylaxis reduce manifestations but do not eliminate the inherited genotype. Evidence for special diets, smoking cessation, alcohol restriction, or exercise as HAE-specific protection is insufficient.

Proposed modifiers include **F12** regulatory polymorphisms and, more recently, candidate modifier loci, but findings are not sufficiently replicated for routine prognostication. (santacroce2021thegeneticsof pages 8-9)

## 3. Phenotypes

### Core phenotype and suggested HPO mappings

- **Recurrent subcutaneous edema**, usually nonpitting, nonpruritic and asymmetric: HP:0100665, Angioedema; HP:0010741, Edema of the limbs; HP:0001999, Facial edema.
- **Abdominal attacks:** cramping pain, nausea, vomiting, diarrhea, bowel-wall edema and ascites: HP:0002027, Abdominal pain; HP:0002013, Vomiting; HP:0002014, Diarrhea; HP:0003270, Abdominal distention; HP:0001541, Ascites.
- **Upper-airway/laryngeal edema:** voice change, dysphagia, stridor, dyspnea and asphyxiation risk: HP:0100659, Laryngeal edema; HP:0002094, Dyspnea; HP:0001650, Dysphonia; HP:0002015, Dysphagia.
- **Oropharyngeal, tongue, lip, genital, facial, hand or foot swelling:** use site-specific edema terms where available.
- **Prodrome:** erythema marginatum, fatigue, paresthesias, mood change or localized discomfort may precede swelling. Erythema marginatum is not urticaria.
- **Laboratory phenotype:** low C4 and low functional C1-INH in HAE-C1INH; low antigenic C1-INH in type I but normal/high antigen in type II.

A 2024 review reported cutaneous swelling in about 75%, recurrent abdominal pain in 52%, and facial/airway edema in 36%; estimates vary by cohort and phenotype definitions. About 25% were described as having severe abdominal attacks. (tutunaru2024unveilingthecomplexities pages 2-4)

### Onset, severity, course, and frequency

Symptoms often begin in childhood and intensify around puberty. One review estimated onset before age five in 40% of type I/II patients and symptoms by age 15 in 75%; approximately 5% of adult variant carriers remained asymptomatic. HAE-nC1INH often becomes evident later, particularly after estrogen exposure. (tutunaru2024unveilingthecomplexities pages 2-4)

Attacks generally evolve over hours and resolve in approximately 2–5 days without treatment, although a broader 1–7-day range is reported. Disease activity is episodic and highly variable both within and between families; genotype does not reliably predict attack site or frequency. (tutunaru2024unveilingthecomplexities pages 2-4, recke2025statusquoand pages 1-2)

### Quality of life

The unpredictable possibility of pain, visible swelling, emergency airway compromise, missed school/work, travel restrictions, and treatment burden causes substantial anticipatory anxiety. In a multinational survey of 242 adults, mean age at first symptoms was 11.5 years and diagnosis at 20.8 years; participants reported a mean 12.5 attacks over six months. Moderate-to-severe anxiety affected 38.0%, depression 17.4%, 6.6% of most recent attacks involved the larynx, and 21.9% lasted at least three days. This was patient-reported cross-sectional evidence and may overrepresent symptomatic patients.

A 2024 systematic review of 65 studies and 10,310 patients found marked impairment across AE-QoL, anxiety, depression, stress, productivity, and direct medical utilization. (recke2025statusquoand pages 1-2)

## 4. Genetic and molecular information

### Causal genes and strength of evidence

- **SERPING1**, chromosome 11q12–q13.1, encodes C1 inhibitor: definitive cause of HAE types I and II.
- **F12:** established cause of a subset of HAE-nC1INH; several gain-of-function or activation-enhancing variants affect factor XII.
- **PLG:** established familial HAE-nC1INH, classically associated with a recurrent plasminogen variant.
- **ANGPT1, KNG1, MYOF, HS3ST6:** reported segregating causes in rare families, but aggregate evidence and replication are less extensive than for SERPING1, F12, and PLG.
- **CPN1 and DAB2IP:** newer reported associations requiring continuing validation and careful ClinGen-style evidence appraisal. (recke2025statusquoand pages 1-2, gao2025expandingthegenetic pages 1-2, santacroce2021thegeneticsof pages 8-9)

### Variant classes and origin

**SERPING1** disease variants include missense, nonsense, frameshift, canonical and noncanonical splice variants, small insertions/deletions, exon-level deletions/duplications, and whole-gene deletions. They are constitutional/germline, usually heterozygous; somatic HAE is not a recognized common category. A cohort of 106 patients from 46 families found 41 causal variants: 45.65% missense, 19.57% frameshift, 17.36% nonsense, 8.7% splice defects, 6.52% large deletions and 2.17% nonstop variants. Protein-truncating/large-deletion variants were associated with severe or very severe disease in 55.39% versus 29.18% for missense variants, but individual prediction remains unreliable. (kariko2026abstractsofthe pages 31-32)

A 2024 primary study showed the utility of genome plus RNA sequencing: it detected a **SERPING1** exon-4 deletion, chr11(GRCh38):g.57600729_57603011del, and demonstrated intron retention from NM_000062.2:c.1249+4A>G. Among 21 suspected HAE-nC1INH cases, only one received a molecular diagnosis, emphasizing the low yield and risk of misclassification in this group. (rozevska2024hereditaryoracquired? pages 2-3)

### Functional consequences

Most type-I alleles cause haploinsufficiency through absent synthesis, defective secretion, degradation, or unstable protein. Some missense alleles cause intracellular polymerization/retention and dominant-negative effects. A 2024 family study identified **SERPING1 c.708T>G** and linked C1-INH retention in the endoplasmic reticulum to GRP75 upregulation, calcium overload, mitochondrial injury, and apoptosis in cellular experiments. Intracellular calcium was proposed—not validated—as an attack biomarker. (jiang2024uncoveringanovel pages 1-2)

A Colombian cluster study identified heterozygous c.1420C>T (p.Gln474*) and novel c.1238T>G (p.Met413Arg). Structural modeling suggested reactive-center-loop insertion, latent C1-INH conformation, impaired secretion, clearance, or aggregation. This is computational/mechanistic support, not proof of clinical severity. (ariasflorez2024phenotypicandmolecular pages 13-14)

### Population frequency and classification

Pathogenic HAE alleles are individually rare and generally absent or extremely rare from population databases such as gnomAD. Classification should use ACMG/AMP criteria, segregation, phenotype/biochemistry, RNA evidence for splice variants, and copy-number analysis. A VUS should not independently establish HAE-nC1INH. Variant interpretation must use current ClinVar/ClinGen records because classifications change.

### Epigenetics and chromosomal abnormalities

No reproducible disease-defining DNA-methylation or histone signature is established. Large intragenic or whole-gene **SERPING1** deletions occur, but HAE is not usually a cytogenetic syndrome. Conventional karyotyping and FISH have negligible routine yield; chromosomal microarray is reserved for broader syndromic presentations or suspected large rearrangements.

## 5. Environmental, lifestyle, and infectious information

HAE is not caused by toxins, radiation, pollution, occupation, diet, smoking, alcohol, or a pathogen. Infections can trigger individual attacks through inflammation/contact-system activation. Trauma and procedures are the most actionable external precipitants. Estrogens and ACE inhibitors are clinically important pharmacological exposures. There is no evidence that vaccination causes HAE, although any inflammatory or mechanical stress could coincidentally precede an attack.

Lifestyle management should focus on individualized trigger recognition without excessive restriction. Patients should not be advised to avoid ordinary activity when effective treatment and an emergency plan are available.

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream:** pathogenic **SERPING1** allele → insufficient functional C1-INH.  
**Intermediate:** inadequately restrained factor XIIa/plasma kallikrein activity → high-molecular-weight kininogen cleavage → excess local bradykinin.  
**Downstream:** bradykinin binds BDKRB2 on vascular endothelial cells → cytoskeletal and junctional changes, vasodilation and increased permeability → plasma extravasation into subcutaneous/submucosal tissue → edema, bowel-wall pain/ascites, or airway obstruction. (OpenTargets Search: hereditary angioedema, tutunaru2024unveilingthecomplexities pages 1-2, caballero2022medicalalgorithmmanagement pages 2-2)

C1-INH also regulates complement and fibrinolytic proteases, explaining low C4 and biochemical cross-talk, but complement-derived anaphylatoxins are not considered the principal mediator of HAE swelling.

In HAE-FXII, PLG and KNG1, altered contact/fibrinolytic processing converges on kinin production. ANGPT1, MYOF, HS3ST6 and DAB2IP observations support a complementary “endothelial-barrier disorder” model involving angiopoietin/Tie2, glycocalyx or VEGF-related permeability. The proximate mechanism across angioedema is endothelial leak, but not every nC1INH subtype has been definitively shown to be exclusively bradykinin mediated. (zuraw2025hereditaryangioedemawith pages 1-2, gao2025expandingthegenetic pages 1-2)

### Cells, tissues, GO and CL suggestions

- **Endothelial cell — CL:0000115:** principal effector cell.
- **Hepatocyte — CL:0000182:** major source of circulating C1-INH and contact-system proteins.
- Possible modulatory cells include **mast cells — CL:0000097**, but HAE is not primarily mast-cell-mediated.
- Suggested GO biological processes: regulation of vascular permeability (GO:0043114), kallikrein–kinin system, complement activation (GO:0006956), proteolysis (GO:0006508), blood coagulation (GO:0007596), inflammatory response (GO:0006954), regulation of endothelial barrier.
- Suggested GO molecular functions/components: serine-type endopeptidase inhibitor activity (GO:0004867), extracellular region (GO:0005576), blood microparticle (GO:0072562), endoplasmic-reticulum lumen (GO:0005788) for retained variants.

### Molecular profiling and advanced technology

Potential biomarkers include cleaved high-molecular-weight kininogen, activated plasma kallikrein, enzyme–inhibitor complexes, D-dimer, endothelial activation markers, and attack-related transcript/protein signatures. Direct bradykinin measurement is technically difficult because it is generated locally and rapidly degraded. No transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial signature is sufficiently validated for routine diagnosis. Genome plus RNA sequencing can resolve cryptic splice/CNV cases, whereas broad sequencing of clinically uncertain nC1INH cases has low yield. (rozevska2024hereditaryoracquired? pages 2-3)

## 7. Anatomical structures affected

- **Skin/subcutis:** face, lips, hands, feet, limbs, trunk and genitalia; UBERON:0002097 skin of body and UBERON:0002190 subcutaneous adipose tissue.
- **Gastrointestinal tract:** stomach and small/large intestine, mesentery and peritoneal cavity; bowel-wall edema may produce ascites and mimic an acute surgical abdomen.
- **Upper respiratory tract:** tongue, soft palate, pharynx, epiglottis and larynx; laryngeal edema is the critical lethal lesion.
- **Urogenital tissues:** genital edema and less commonly urinary-tract symptoms.

The lesion is extracellular/interstitial fluid accumulation caused by postcapillary endothelial leak rather than primary epithelial destruction. Swelling is often asymmetric; lateralization has no diagnostic significance. There is no characteristic chronic fibrosis or necrosis after ordinary attacks.

## 8. Temporal development

HAE is congenital at the genetic level but usually not symptomatic neonatally. Childhood onset is common, activity often increases at puberty, and HAE-nC1INH may emerge after hormonal exposure. Attacks are acute/subacute, increase over hours and remit spontaneously over days. The lifelong course is episodic rather than continuously progressive; there are no accepted early/intermediate/end-stage categories. (tutunaru2024unveilingthecomplexities pages 2-4, recke2025statusquoand pages 1-2)

Periods without attacks are not molecular remission. Pregnancy may improve, worsen, or not change disease. Critical windows include airway symptoms, the hours after dental/airway procedures, and early attack onset, when self-administered therapy generally works best.

## 9. Inheritance and population

### Epidemiology

A 2024 systematic review found reported prevalence from **0.13 to 1.6 per 100,000**, with major geographic ascertainment differences and probable underdiagnosis. Another contemporary synthesis uses approximately 1:50,000 to 1:150,000. Among 10,310 collated patients, 5,861 were female; among cases with subtype data, 81% were type I, 9% type II, and 8% HAE-nC1INH. Diagnostic delay ranged from 3.9 to 26 years. (tutunaru2024unveilingthecomplexities pages 2-4, tutunaru2024unveilingthecomplexities pages 1-2)

HAE occurs worldwide across ancestries and both sexes. HAE-C1INH has no strong biological sex bias, although women may have greater hormonal modulation and are overrepresented in clinical cohorts. Incidence is difficult to estimate because HAE is inherited and often diagnosed years after birth.

### Mendelian properties

Inheritance is predominantly autosomal dominant, with incomplete/age-dependent penetrance and markedly variable expressivity. About 5% of adult carriers may remain asymptomatic in some series. There is no established anticipation. Germline mosaicism is possible but appears uncommon. Consanguinity is not a usual risk factor for dominant HAE, although rare biallelic **SERPING1** cases exist. Founder clusters occur; a 2024 study described four Colombian families with 79 suspected affected members and distinct **SERPING1** variants. (tutunaru2024unveilingthecomplexities pages 2-4, ariasflorez2024phenotypicandmolecular pages 13-14)

## 10. Diagnostics

### Clinical suspicion

Suspect HAE with recurrent angioedema without wheals, recurrent severe unexplained abdominal attacks, laryngeal edema, childhood/adolescent onset, family history, prodromes, and failure of adequate antihistamine/glucocorticoid therapy. Family history is absent in de-novo disease.

### Laboratory algorithm

1. Measure **C4, antigenic C1-INH and functional C1-INH** together.
2. Repeat abnormal or discordant results in a properly handled fresh sample, preferably when the patient is well and before labeling the condition lifelong.
3. Type I: low C4, low C1-INH antigen and function.
4. Type II: low C4, normal/high antigen, low function.
5. Measure **C1q** when acquired C1-INH deficiency is plausible—especially adult onset with no family history. C1q is often low in acquired disease and usually normal in hereditary C1-INH deficiency.
6. Normal C4 does not absolutely exclude HAE, especially outside attacks, and all complement tests are normal in HAE-nC1INH. (tutunaru2024unveilingthecomplexities pages 1-2, caballero2022medicalalgorithmmanagement pages 2-2)

Antigenic C1-INH can be measured by nephelometry/turbidimetry; function by chromogenic assay or ELISA. Preanalytics are important because delayed processing or improper storage can artifactually reduce function.

### Genetics

For biochemically confirmed HAE-C1INH, sequence **SERPING1** with deletion/duplication analysis such as MLPA. If negative despite convincing biochemistry, consider genome sequencing and RNA studies. For nC1INH, use a carefully curated panel including **F12, PLG, ANGPT1, KNG1, MYOF, HS3ST6**, with cautious inclusion of newer genes. WES/WGS may discover structural or intronic variants but also generate VUS. In a 2024 cohort, conventional testing diagnosed 10/32 patients, while broad investigation produced a molecular answer in only 1/21 suspected nC1INH cases. (rozevska2024hereditaryoracquired? pages 2-3)

CMA, karyotyping, FISH, mitochondrial analysis and repeat-expansion testing are not routine HAE tests. Cascade biochemical/genetic testing is recommended for first-degree relatives. Complement results in infants can be difficult to interpret; repeat age-appropriate testing is needed.

### Imaging and pathology

Imaging is supportive only. During abdominal attacks, ultrasound or CT can show transient bowel-wall thickening, mesenteric edema and ascites. Airway evaluation must not delay treatment and should be undertaken where airway intervention is available. Biopsy, histopathology, electrophysiology and liquid biopsy have no routine role.

### Differential diagnosis

Key alternatives are mast-cell-mediated angioedema/anaphylaxis, chronic spontaneous urticaria, ACE-inhibitor angioedema, acquired C1-INH deficiency, idiopathic non-mast-cell angioedema, contact dermatitis, cellulitis, superior vena-cava syndrome, nephrotic/cardiac/hepatic edema, and gastrointestinal surgical/inflammatory disease. Wheals, pruritus, rapid response to antihistamine/epinephrine and an allergic exposure favor mast-cell disease; low C1q and late onset favor acquired C1-INH deficiency.

## 11. Outcome and prognosis

HAE does not ordinarily cause progressive organ failure or shorten life when recognized and adequately treated. The dominant mortality mechanism is acute upper-airway obstruction. A 2024 systematic review estimated asphyxiation death risk at **8.6%** in historical/heterogeneous data, while older untreated laryngeal-attack series report much higher case fatality; these estimates should not be applied to patients with modern therapy and emergency plans. (zhao2026advancesinhereditary pages 1-2, recke2025statusquoand pages 1-2)

Delayed diagnosis remains a major adverse prognostic factor. Other burden predictors include high attack frequency, prior laryngeal attacks, poor access to on-demand treatment, uncontrolled disease, estrogen/ACE-inhibitor exposure, and anxiety. A Chinese scoping review reported 129 deaths in literature through 2021 versus five during 2021–September 2024, consistent with—but not proving—benefit from awareness and modern treatment. (zhao2026advancesinhereditary pages 1-2)

Recovery from each treated or untreated nonfatal attack is usually complete. Morbidity includes pain, dehydration, unnecessary abdominal surgery, emergency visits, work/school loss, anxiety, depression and treatment burden. Recommended patient-reported outcomes include AE-QoL, AECT, HAE Activity Score and treatment-satisfaction instruments.

## 12. Treatment

### Treatment goals and strategy

Management has three layers: **on-demand treatment of every attack**, **short-term prophylaxis** before high-risk procedures, and individualized **long-term prophylaxis (LTP)**. Every patient should have rapid access to enough on-demand medicine for at least two attacks and a written emergency/airway plan. Treat early; any tongue, pharyngeal or laryngeal involvement requires immediate therapy and emergency airway assessment.

Suggested MAXO mappings include pharmacotherapy (MAXO:0000058), intravenous medication administration, subcutaneous medication administration, prophylactic treatment, genetic counseling, molecular genetic testing and emergency airway management; exact identifiers should be validated against the deployed MAXO release.

### On-demand therapy

- **Plasma-derived or recombinant C1-INH:** replaces deficient inhibition and suppresses upstream contact-system activation. Intravenous administration is effective across attack sites.
- **Icatibant:** subcutaneous bradykinin-B2 receptor antagonist; may require repeat dosing.
- **Ecallantide:** subcutaneous plasma-kallikrein inhibitor, US-specific availability; must be administered by a healthcare professional because of anaphylaxis risk.
- Where specific agents are unavailable, solvent/detergent-treated plasma or fresh frozen plasma may be considered, but are not preferred.

Antihistamines and glucocorticoids do not treat the bradykinin mechanism; epinephrine remains appropriate if anaphylaxis cannot initially be excluded.

### Short-term prophylaxis

Intravenous plasma-derived C1-INH shortly before dental work, upper-airway instrumentation or surgery is preferred when procedure-related trauma could provoke edema. Even with prophylaxis, rescue treatment and airway capability must be available. Attenuated androgens may be used where modern options are unavailable but have slower onset and toxicity.

### Long-term prophylaxis

Established options include:

- **Lanadelumab:** subcutaneous monoclonal antibody against active plasma kallikrein.
- **Berotralstat:** once-daily oral plasma-kallikrein inhibitor; 150 mg daily is a common adult regimen where approved.
- **Subcutaneous or intravenous plasma-derived C1-INH.**
- **Attenuated androgens** such as danazol and **antifibrinolytics** such as tranexamic acid are generally later-line because efficacy/tolerability are inferior. Androgens can cause virilization, menstrual disturbance, dyslipidemia, hypertension, hepatic toxicity and mood effects.

Choice should incorporate attack burden, prior airway events, age, pregnancy, comorbidities, route, access, preference and QoL—not an arbitrary attack-count threshold. Breakthrough attacks still require on-demand therapy. OpenTargets evidence independently supports approved intervention at **KLKB1** and bradykinin/contact-system targets. (OpenTargets Search: hereditary angioedema, johnson2025unravelingangioedemadiagnostic pages 9-10)

### Emerging and recent therapy research

- **Garadacimab:** long-acting monoclonal antibody inhibiting activated factor XII for LTP.
- **Donidalorsen:** antisense oligonucleotide reducing prekallikrein RNA; a phase III study reported approximately **81% attack-rate reduction** with 80 mg every four weeks. NCT05139810 is the pivotal OASIS-HAE study; NCT05392114 is a long-term study. (johnson2025unravelingangioedemadiagnostic pages 9-10, recke2025statusquoand pages 13-14)
- **Sebetralstat and deucrictibant:** oral B2-receptor antagonists intended to reduce injection burden. Phase-II deucrictibant data reported median symptom-resolution times around 25–26 minutes; phase III on-demand study NCT06343779 enrolled 134 participants. (johnson2025unravelingangioedemadiagnostic pages 9-10)
- **Navenibart/STAR-0215:** long-acting kallikrein antibody designed for infrequent administration; phase-II reports showed approximately 90–95% mean monthly attack-rate reductions. NCT06007677 is a long-term study. (johnson2025unravelingangioedemadiagnostic pages 9-10)
- **ADX-324:** RNA-targeting prophylaxis under phase I–III evaluation, including NCT05691361 and NCT06960213.
- **BMN 331:** AAV-mediated **SERPING1** gene transfer, NCT05121376.
- **NTLA-2002:** systemic in-vivo CRISPR/Cas9 editing of hepatic **KLKB1**, designed as one-time therapy. Early-phase reports described 97–99% attack reductions over about 20 months, but long-term off-target, hepatic, reproductive and irreversible-editing risks remain incompletely characterized. NCT05120830 is phase I/II; NCT06634420 is the HAELO phase III study. (johnson2025unravelingangioedemadiagnostic pages 9-10, recke2025statusquoand pages 13-14)

These investigational results are not interchangeable with regulatory approval, and cross-trial efficacy comparisons are unreliable.

### Special populations

Plasma-derived C1-INH has the broadest experience in pregnancy and lactation. Pediatric approvals differ by product and jurisdiction. Androgens are contraindicated in pregnancy and generally avoided in children. HAE-nC1INH treatment evidence is much weaker and often consists of case series/expert opinion; response should support management but not be used as a stand-alone diagnostic test. (zuraw2025hereditaryangioedemawith pages 1-2)

No validated HAE pharmacogenomic dosing guideline comparable to CPIC recommendations currently exists.

## 13. Prevention

Primary prevention of the inherited genotype is not possible after conception. Reproductive options include genetic counseling, natural conception with prenatal testing where desired, and preimplantation genetic testing for a known familial pathogenic variant. Counseling must address variable expressivity and the availability of effective therapy.

Secondary prevention consists of early biochemical diagnosis, cascade screening of relatives, confirmatory genetics where useful, and education before symptoms occur. Population or newborn screening is not standard. Dried-blood-spot C1-INH approaches remain investigational.

Tertiary prevention includes avoiding ACE inhibitors and estrogen where appropriate, procedure-specific prophylaxis, ready access to on-demand medication, self-administration training, medical identification, emergency plans, regular disease-control/QoL assessment, and LTP when burden remains unacceptable. Vaccination should follow routine recommendations; there is no HAE vaccine.

## 14. Other species and natural disease

The relevant genes and contact-system biology are evolutionarily conserved across vertebrates, including mouse **Serping1**, **F12**, **Klkb1**, **Kng1**, and bradykinin receptors. However, the searched evidence did not identify a well-established, naturally occurring veterinary counterpart that is routinely classified as hereditary angioedema in a specific dog, cat, horse, livestock or wildlife population. Reports of animal angioedema more commonly describe allergic reactions rather than a genetically proven C1-INH-deficient syndrome.

Accordingly, no validated VBO breed term, animal carrier frequency, zoonotic transmission or cross-species transmission applies. HAE is noninfectious and nonzoonotic.

## 15. Model organisms

### Mouse models

**Serping1-deficient mice** show increased vascular permeability measurable by Evans-blue extravasation, supporting the causal link between C1-INH loss and endothelial leak. Pharmacological C1-INH replacement and blockade of downstream bradykinin signaling can reverse permeability, providing target validation for human treatment. (OpenTargets Search: hereditary angioedema)

Other useful models include contact-system or bradykinin-receptor knockout combinations, acute permeability models, and mice exposed to agents that activate kallikrein–kinin pathways. These systems are used to study endothelial permeability, factor-XII/kallikrein activation and preclinical drug activity.

### Cellular and in-vitro systems

Hepatocyte-like expression systems assess secretion, polymerization and intracellular retention of C1-INH variants. Endothelial monolayers quantify barrier resistance and permeability after bradykinin or patient-plasma exposure. The 2024 c.708T>G study used cellular experiments to connect ER retention, GRP75, calcium overload, mitochondrial injury and apoptosis. (jiang2024uncoveringanovel pages 1-2)

### Limitations

Mice do not spontaneously reproduce the full stochastic human pattern of abdominal, cutaneous and laryngeal attacks, hormonal modulation, or psychosocial burden. Homozygous knockout is also not equivalent to the usual human heterozygous state. Cell models isolate particular pathways and cannot reproduce systemic contact-system, hepatic and endothelial interactions. No widely accepted HAE organoid, zebrafish, Drosophila or naturally affected companion-animal model currently supersedes mouse and endothelial-cell platforms.

## Evidence-quality and knowledge-gap assessment

The highest-confidence evidence concerns **SERPING1**, C1-INH biochemistry, bradykinin/contact-system pathophysiology, complement testing, and approved therapies for HAE-C1INH. HAE-nC1INH is less secure: the 2025 international consensus explicitly states that recommendations are largely expert opinion because high-level evidence is sparse. (zuraw2025hereditaryangioedemawith pages 1-2)

Recent primary studies strengthen genomic diagnosis but also caution against overdiagnosis. In the 2024 32-patient investigation, extensive sequencing found a recognized HAE-nC1INH pathogenic variant in only one of 21 suspected cases, and clinical re-evaluation changed several diagnoses. (rozevska2024hereditaryoracquired? pages 2-3)

Important unresolved questions are reliable attack-prediction biomarkers, penetrance modifiers, standardized HAE-nC1INH criteria, comparative effectiveness among modern prophylactics, pregnancy data for newer drugs, equitable global access, and the lifetime safety of RNA/gene-editing interventions.

## Selected recent sources and exact abstract language

- **Rozevska et al., March 2024**, *Allergy, Asthma & Clinical Immunology*, DOI: https://doi.org/10.1186/s13223-024-00889-5. Primary genomic cohort. Abstract: “**the diagnostic yield for nC1-INH HAE remains low in our study**.” (rozevska2024hereditaryoracquired? pages 2-3)
- **Jiang et al., September 2024**, *Orphanet Journal of Rare Diseases*, DOI: https://doi.org/10.1186/s13023-024-03306-7. Primary family/cellular study. Abstract: “**this variant leads to an increase in the accumulation of C1-INH within the endoplasmic reticulum**.” (jiang2024uncoveringanovel pages 1-2)
- **Arias-Flórez et al., December 2024**, *PLOS ONE* 19:e0311316, DOI: https://doi.org/10.1371/journal.pone.0311316. Primary founder-cluster study. Abstract describes “**sudden local, often asymmetric, and episodic subcutaneous and submucosal swelling**.” (ariasflorez2024phenotypicandmolecular pages 13-14)
- **Tutunaru et al., October 2024**, *Biomolecules* 14:1298, DOI: https://doi.org/10.3390/biom14101298. Review. Abstract: HAE causes “**recurrent episodes of non-pruritic angioedema, which occurs in the absence of urticaria**.” (tutunaru2024unveilingthecomplexities pages 1-2)
- **Zuraw et al., March 2025**, *Clinical Reviews in Allergy & Immunology*, DOI: https://doi.org/10.1007/s12016-025-09027-4. International expert consensus derived from a September 2023 symposium. It emphasizes that HAE-nC1INH recommendations are expert opinion because of limited high-level evidence. (zuraw2025hereditaryangioedemawith pages 1-2)

PMIDs explicitly available in the retrieved disease-target evidence include **26452350, 29316335, 22994404, 28795768, 29548426, 29952006, 31087670, 31860755, 33508266, 33799813**, among others linking SERPING1, PLG, KNG1, ANGPT1 and HS3ST6 to HAE. These should be reconciled with current PubMed/ClinVar records during database curation. (OpenTargets Search: hereditary angioedema)

References

1. (zuraw2025hereditaryangioedemawith pages 1-2): Bruce L. Zuraw, Konrad Bork, Laurence Bouillet, Sandra C. Christiansen, Henriette Farkas, Anastasios E. Germenis, Anete S. Grumach, Allen Kaplan, Alberto López-Lera, Markus Magerl, Marc A. Riedl, Adil Adatia, Aleena Banerji, Stephen Betschel, Isabelle Boccon-Gibod, Maria Bova, Henrik Balle Boysen, Teresa Caballero, Mauro Cancian, Anthony J. Castaldo, Danny M. Cohn, Deborah Corcoran, Christian Drouet, Atsushi Fukunaga, Michihiro Hide, Constance H. Katelaris, Philip H. Li, Hilary Longhurst, Jonny Peter, Fotis Psarros, Avner Reshef, Bruce Ritchie, Christine N. Selva, Andrea Zanichelli, and Marcus Maurer. Hereditary angioedema with normal c1 inhibitor: an updated international consensus paper on diagnosis, pathophysiology, and treatment. Clinical Reviews in Allergy & Immunology, Mar 2025. URL: https://doi.org/10.1007/s12016-025-09027-4, doi:10.1007/s12016-025-09027-4. This article has 59 citations and is from a peer-reviewed journal.

2. (tutunaru2024unveilingthecomplexities pages 1-2): Cristina Violeta Tutunaru, Oana Maria Ică, George G. Mitroi, Carmen Daniela Neagoe, George F. Mitroi, Olguța Anca Orzan, Beatrice Bălăceanu-Gurău, and Simona Laura Ianoși. Unveiling the complexities of hereditary angioedema. Biomolecules, 14:1298, Oct 2024. URL: https://doi.org/10.3390/biom14101298, doi:10.3390/biom14101298. This article has 22 citations.

3. (tutunaru2024unveilingthecomplexities pages 2-4): Cristina Violeta Tutunaru, Oana Maria Ică, George G. Mitroi, Carmen Daniela Neagoe, George F. Mitroi, Olguța Anca Orzan, Beatrice Bălăceanu-Gurău, and Simona Laura Ianoși. Unveiling the complexities of hereditary angioedema. Biomolecules, 14:1298, Oct 2024. URL: https://doi.org/10.3390/biom14101298, doi:10.3390/biom14101298. This article has 22 citations.

4. (OpenTargets Search: hereditary angioedema): Open Targets Query (hereditary angioedema, 16 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (caballero2022medicalalgorithmmanagement pages 2-2): Teresa Caballero, Rosario Cabañas, and María Pedrosa. Medical algorithm: management of c1 inhibitor hereditary angioedema. Allergy, 77:1060-1063, Oct 2022. URL: https://doi.org/10.1111/all.15115, doi:10.1111/all.15115. This article has 4 citations and is from a highest quality peer-reviewed journal.

6. (recke2025statusquoand pages 1-2): Andreas Recke. Status quo and future developments in the diagnosis and treatment of hereditary angioedema. JDDG: Journal der Deutschen Dermatologischen Gesellschaft, 23:1512-1525, Sep 2025. URL: https://doi.org/10.1111/ddg.15889, doi:10.1111/ddg.15889. This article has 0 citations.

7. (johnson2025unravelingangioedemadiagnostic pages 9-10): Felix Johnson and Benedikt Hofauer. Unraveling angioedema: diagnostic challenges and emerging therapies. Frontiers in Immunology, Oct 2025. URL: https://doi.org/10.3389/fimmu.2025.1681763, doi:10.3389/fimmu.2025.1681763. This article has 3 citations and is from a peer-reviewed journal.

8. (santacroce2021thegeneticsof pages 8-9): Rosa Santacroce, Giovanna D'Andrea, Angela Bruna Maffione, Maurizio Margaglione, and Maria d'Apolito. The genetics of hereditary angioedema: a review. Journal of Clinical Medicine, 10:2023, May 2021. URL: https://doi.org/10.3390/jcm10092023, doi:10.3390/jcm10092023. This article has 178 citations.

9. (rozevska2024hereditaryoracquired? pages 2-3): Marija Rozevska, Adine Kanepa, Signe Purina, Linda Gailite, Inga Nartisa, Henriette Farkas, Dmitrijs Rots, and Natalja Kurjane. Hereditary or acquired? comprehensive genetic testing assists in stratifying angioedema patients. Allergy, Asthma, and Clinical Immunology : Official Journal of the Canadian Society of Allergy and Clinical Immunology, Mar 2024. URL: https://doi.org/10.1186/s13223-024-00889-5, doi:10.1186/s13223-024-00889-5. This article has 7 citations.

10. (gao2025expandingthegenetic pages 1-2): Haiqing Gao, Ying Zhao, Shengan Chen, Zhen Zhang, Fanping Yang, Zihua Chen, Lanting Wang, Jin Yang, Shan He, Chang Tang, Shenyuan Zheng, Chenggong Guan, Yu Xu, Lin Tang, Aiyuan Zhang, Marcus Maurer, Dylan Lee, Li Ma, and Xiaoqun Luo. Expanding the genetic and clinical spectrum of hereditary angioedema with normal c1 inhibitor: novel variants and treatment insights. Journal of Clinical Immunology, Aug 2025. URL: https://doi.org/10.1007/s10875-025-01912-z, doi:10.1007/s10875-025-01912-z. This article has 4 citations and is from a domain leading peer-reviewed journal.

11. (kariko2026abstractsofthe pages 31-32): PhD Katalin Karikó, S. Thiel, A. Germenis, László Cervenak, F. Marceau, Ahmed Sahli, R. C.-Gaudreault, E. Pardali, H. Horváth, Oliver Domenig, D. V. Oyen, D. Sexton, G. Zahn, A. Lesage, H. Farkas, D. Parolin, S. Berra, Sonia Caccia, J. Gil-Serrano, M. Labrador-Horrillo, P. Galvan-Blasco, A. Sala-Cunill, J. Pereira-González, M. Planas-Vinos, Victoria Cardona, Yingyang Xu, Xiangyi Cui, Zejian Zhang, Yuxiang Zhi, A. S. Pinheiro, Douglas E. Teixiera, R. Silva-Aguiar, A. Merkulova, Y. Skomorovska-Prokvolit, Y. J. Shim, Keith R. McCrae, D. Midem, S. Ogolla, Celso Caruso Neves, A. S. Pinheiro, J. Kazura, A. H. Schmaier, M. Guilarte, A. López-Lera, Ethel Ibáñez-Echevarría, K. Baynova, C. Marcos-Bravo, Eugenia Sanchis-Merino, Gabriela Leon-Zambrana, Patricia Bigas Peñuela, Leah Landaveri-Sánchez, S. Cimbollek, Marta Goyanes-Malumbres, Isora Vidal-Sernandez, Roger Colobran, T. Caballero, M. Barešić, Boris Karanović, D. Vergles, B. Anić, A. Bocquet, David Launay, I. Boccon-Gibod, A. Du-Thanh, D. Gobert, S. Sanges, L. Bouillet, Emel Aygören-Pursun, N. Bara, T. Buttgereit, D. Cohn, S. Kiani-Alikhan, M. Magerl, Johanna M. Mandelin, Marc Riedl, Sinisa Savic, M. Sobotková, M. Stobiecki, A. Zanichelli, D. Gobert, Mélanie Javaud, E. Cohen, O. Fain, Boris Bienvenu, E. Aygören‐Pürsün, Mona Al-Ahmad, A. Recke, K. Hartmann, Maureen Watt, Daniel Nova Estepan, Irmgard Andresen, Natalie Khutoryansky, Aharon Kessel, M. Cancian, H. Longhurst, Paul K Keith, Harsha Shetty, M. Pollen, H. Feuersenger, J. Bernstein, A. Banerji, J. Jacobs, Allen P. Kaplan, James S. Butler, David Maag, Catherine Miller, Jonathan Phillips, I. Guryanova, A. V. Liubushkin, E. Polyakova, A. Salivonchik, V. Vertelko, M. Belevtsev, A. Solntsava, A. Valerieva, Alex Fam, Ferhat Maksudov, E. Petkova, Teresa De Aramburu, J. Lucena, M. Staevska, W. Lumry, John Anderson, Henry Li, James Hao, Michael Smith8, P. Bajcic, P. Audhya, Teresa De, Aramburu Mera, J. Raúl, G. Lozano, J. Manuel, L. Soto, F. Perego, A. C. Marcelli, R. Senter, Federica Ruin, L. Zingale, A. Gidaro, V. P. Janu, F. Arcoleo, P. Accardo, Mariangela Lo Pizzo, Giada De Angeli, F. Giardino, E. Cataudella, A. Vultaggio, A. Matucci, A. Petraroli, Roberta Gatti, Giuseppe Spadaro, Luisa Brussino, Stefania Nicola, Luca Lo Sardo, M. Guarino, Helena Jakopič, M. Košnik, M. Zidarn, J. Šelb, Peter Korošec, and M. Rijavec. Abstracts of the 14th c1-inhibitor deficiency and angioedema workshop. Allergy, Asthma &amp; Clinical Immunology, Jan 2026. URL: https://doi.org/10.1186/s13223-025-00992-1, doi:10.1186/s13223-025-00992-1. This article has 1 citations.

12. (jiang2024uncoveringanovel pages 1-2): Lingxi Jiang, Chao Dai, Suyang Duan, Tingting Wang, Chunbao Xie, Luhan Zhang, Zimeng Ye, Xiumei Ma, and Yi Shi. Uncovering a novel serping1 pathogenic variant: insights into the aggregation of c1-inh in hereditary angioedema. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03306-7, doi:10.1186/s13023-024-03306-7. This article has 5 citations and is from a peer-reviewed journal.

13. (ariasflorez2024phenotypicandmolecular pages 13-14): Juan Sebastian Arias-Flórez, Sandra Ximena Ramirez, Bibiana Bayona-Gomez, Lina Castro-Castillo, Valeria Correa-Martinez, Yasmín Sanchez-Gomez, William Usaquén-Martínez, Lilian Andrea Casas-Vargas, Carlos Eduardo Olmos Olmos, Nora Contreras Bravo, Camilo Andres Velandia-Piedrahita, Adrien Morel, Rodrigo Cabrera-Perez, Natalia Santiago-Tovar, Cristian Camilo Gaviria-Sabogal, Ingrid Tatyana Bernal, Dora Janeth Fonseca-Mendoza, and Carlos M. Restrepo. Phenotypic and molecular characterization of the largest worldwide cluster of hereditary angioedema type 1. PLOS ONE, 19:e0311316, Dec 2024. URL: https://doi.org/10.1371/journal.pone.0311316, doi:10.1371/journal.pone.0311316. This article has 1 citations and is from a peer-reviewed journal.

14. (zhao2026advancesinhereditary pages 1-2): Ye Zhao and Duowu Zou. Advances in hereditary angioedema in the modern treatment era in china: a focus on diagnosis, treatment, and prognosis. Orphanet Journal of Rare Diseases, Mar 2026. URL: https://doi.org/10.1186/s13023-026-04314-5, doi:10.1186/s13023-026-04314-5. This article has 0 citations and is from a peer-reviewed journal.

15. (recke2025statusquoand pages 13-14): Andreas Recke. Status quo and future developments in the diagnosis and treatment of hereditary angioedema. JDDG: Journal der Deutschen Dermatologischen Gesellschaft, 23:1512-1525, Sep 2025. URL: https://doi.org/10.1111/ddg.15889, doi:10.1111/ddg.15889. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Hereditary_Angioedema-deep-research-falcon_artifacts/artifact-00.md)