---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-04T15:23:57.020981'
end_time: '2026-06-04T15:35:16.231668'
duration_seconds: 679.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Weaver Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Weaver_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Weaver Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Weaver Syndrome** covering all of the
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
- **Disease Name:** Weaver Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Weaver Syndrome** covering all of the
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


# Weaver Syndrome (MIM 277590) — Comprehensive Disease Characteristics Report

## Target Disease
- **Disease name:** Weaver syndrome (WS) (gibson2012mutationsinezh2 pages 1-3, tatton‐brown2013weaversyndromeand pages 1-2)
- **Category:** Mendelian (autosomal dominant overgrowth/intellectual disability syndrome) (kendirdemirkol2024expandingthephenotypic pages 1-2, gibson2012mutationsinezh2 pages 1-3)
- **MONDO ID:** Not identified in the retrieved primary texts used for this report (limitation of current tool-retrieved corpus).

## Summary (current understanding)
Weaver syndrome is a rare congenital anomaly/overgrowth syndrome characterized by pre- and/or postnatal generalized overgrowth, markedly advanced bone age (accelerated osseous maturation), characteristic craniofacial gestalt (e.g., hypertelorism, broad forehead, retrognathia with “stuck-on” chin crease), and variable developmental delay/intellectual disability (gibson2012mutationsinezh2 pages 1-3, tatton‐brown2013weaversyndromeand pages 3-4). Since 2011–2012, heterozygous germline pathogenic variants in **EZH2** (encoding the catalytic subunit of Polycomb Repressive Complex 2, PRC2) have been established as the primary cause (tattonbrown2011germlinemutationsin pages 1-2, gibson2012mutationsinezh2 pages 1-3). 

Recent mechanistic work (2024–2025) supports that many WS-associated EZH2 missense alleles can act through **dominant-negative interference** with PRC2, producing global reductions in H3K27me2/3, increases in H3K27ac, and chromatin decompaction (deevy2024dominantnegativeeffects pages 1-2, deevy2025dominantnegativeeffectsof pages 1-2). A 2024 knock-in mouse model (Ezh2 p.R684C) recapitulates skeletal overgrowth/excess osteogenesis and demonstrates pharmacologic reversibility of osteogenic phenotypes by inhibiting the opposing H3K27 demethylases KDM6A/KDM6B (gao2024amousemodel pages 1-2).

---

## 1. Disease Information

### 1.1 Concise overview
Weaver syndrome (MIM 277590) was originally described in 1974 and is now recognized as an **EZH2-related** overgrowth syndrome with characteristic craniofacial features and variable intellectual disability (tatton‐brown2013weaversyndromeand pages 1-2, gibson2012mutationsinezh2 pages 1-3). 

**Primary literature abstract quote (2011 discovery):**
- “**Weaver syndrome is a human overgrowth condition characterised by tall stature, dysmorphic facial features, learning disability and variable additional features**.” (Tatton-Brown et al., 2011; published 2011-12-21; URL: https://doi.org/10.18632/oncotarget.385) (tattonbrown2011germlinemutationsin pages 1-2)

### 1.2 Key identifiers (from retrieved sources)
- **OMIM/MIM disease:** Weaver syndrome **MIM 277590** (Gibson et al., *AJHG*, 2012-01-13; DOI: 10.1016/j.ajhg.2011.11.018; URL: https://doi.org/10.1016/j.ajhg.2011.11.018) (gibson2012mutationsinezh2 pages 1-3)
- **Causal gene:** **EZH2** (Enhancer of Zeste Homolog 2) (gibson2012mutationsinezh2 pages 1-3)
- **EZH2 gene identifier:** **MIM #601573** (Cohen et al., *Human Mutation*, published online 2015-12-23; DOI: 10.1002/humu.22946; URL: https://doi.org/10.1002/humu.22946) (cohen2016weaversyndrome‐associatedezh2 pages 1-2)

**Not found in retrieved texts:** ICD-10/ICD-11 codes, MeSH terms, MONDO ID.

### 1.3 Synonyms / alternative names
- “EZH2-related overgrowth syndrome” (descriptor used in contemporary literature) (kendirdemirkol2024expandingthephenotypic pages 1-2)

### 1.4 Evidence provenance (individual vs aggregated)
- Aggregated cohort-level phenotyping is available from the large **EZH2-mutation positive series (n=48)** (Tatton-Brown et al., 2013) (tatton‐brown2013weaversyndromeand pages 1-2), and from mechanistic/biomarker studies that aggregate multiple WS cases (Choufani et al., 2020) (choufani2020dnamethylationsignature pages 1-2).
- Many additional details come from individual case reports/series and experimental models (e.g., Gao et al., 2024 mouse model) (gao2024amousemodel pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause (genetic):** heterozygous germline pathogenic variants in **EZH2** (gibson2012mutationsinezh2 pages 1-3, tattonbrown2011germlinemutationsin pages 1-2).
- Gibson et al. used trio-based whole-exome sequencing and identified **de novo EZH2 mutations**, concluding “mutations in EZH2 cause Weaver syndrome” (AJHG, 2012-01-13; URL: https://doi.org/10.1016/j.ajhg.2011.11.018) (gibson2012mutationsinezh2 pages 1-3).

### 2.2 Risk factors
- For this Mendelian disorder, the dominant “risk factor” is carrying a pathogenic EZH2 variant; most cases are sporadic/de novo, with rare familial autosomal dominant transmission (tattonbrown2011germlinemutationsin pages 1-2, gibson2012mutationsinezh2 pages 1-3).

### 2.3 Protective factors / gene–environment interactions
- No protective genetic variants or gene–environment interactions were identified in the retrieved primary literature for Weaver syndrome specifically.

---

## 3. Phenotypes (with suggested HPO terms)

### 3.1 Core phenotype spectrum and frequencies
The best quantitative frequencies in the retrieved corpus come from Tatton-Brown et al. (2013), an EZH2-positive cohort (tatton‐brown2013weaversyndromeand pages 3-4). Key findings:
- **Tall stature (postnatal height ≥ +2 SD):** 41/45 (91%) (tatton‐brown2013weaversyndromeand pages 3-4)
- **Intellectual disability/developmental delay:** 37/45 (82%); often mild (21/37 mild) (tatton‐brown2013weaversyndromeand pages 3-4)
- **Camptodactyly/contractures:** 45% (tatton‐brown2013weaversyndromeand pages 3-4)
- **Soft/doughy skin:** 49% (tatton‐brown2013weaversyndromeand pages 3-4)
- **Umbilical hernia:** 43% (tatton‐brown2013weaversyndromeand pages 3-4)
- **Hoarse, low-pitched cry:** 37% (tatton‐brown2013weaversyndromeand pages 3-4)
- **Poor coordination/clumsiness:** 28/35 (80%) (tatton‐brown2013weaversyndromeand pages 3-4)
- **Hypotonia:** 44%; **hypertonia:** 28% (tatton‐brown2013weaversyndromeand pages 3-4)

Birth metrics in the same cohort:
- **Birth length > +2 SD:** 12/18
- **Birth weight > +2 SD:** 15/39 (38%) (tatton‐brown2013weaversyndromeand pages 3-4)

Craniofacial gestalt is described as sometimes subtle and age-dependent but classically includes hypertelorism, broad forehead, almond-shaped palpebral fissures, large fleshy ears in early childhood, retrognathia, and a pointed “stuck-on” chin with a horizontal crease (tatton‐brown2013weaversyndromeand pages 3-4).

### 3.2 Suggested HPO terms (examples; not exhaustive)
Below are phenotype-to-HPO suggestions aligned to the retrieved descriptions:
- Overgrowth / tall stature: **Tall stature (HP:0000098)** (tatton‐brown2013weaversyndromeand pages 3-4)
- Prenatal overgrowth/macrosomia: **Large for gestational age (HP:0001520)** (supported by prenatal/postnatal overgrowth descriptions) (gibson2012mutationsinezh2 pages 1-3)
- Macrocephaly: **Macrocephaly (HP:0000256)** (gibson2012mutationsinezh2 pages 1-3, tatton‐brown2013weaversyndromeand pages 3-4)
- Advanced bone age: **Advanced bone age (HP:0005616)** (gibson2012mutationsinezh2 pages 1-3)
- Intellectual disability: **Intellectual disability (HP:0001249)** (tatton‐brown2013weaversyndromeand pages 3-4)
- Hypotonia: **Hypotonia (HP:0001252)**; Hypertonia: **Hypertonia (HP:0001276)** (tatton‐brown2013weaversyndromeand pages 3-4)
- Hypertelorism: **Hypertelorism (HP:0000316)** (gibson2012mutationsinezh2 pages 1-3)
- Retrognathia/micrognathia: **Retrognathia (HP:0000278)** (gibson2012mutationsinezh2 pages 1-3)
- Camptodactyly: **Camptodactyly (HP:0012385)** (tatton‐brown2013weaversyndromeand pages 3-4)
- Umbilical hernia: **Umbilical hernia (HP:0001537)** (tatton‐brown2013weaversyndromeand pages 3-4)
- Hoarse cry: **Hoarse cry (HP:0001609)** (tatton‐brown2013weaversyndromeand pages 3-4)
- Clumsiness/coordination: **Motor delay / impaired coordination (e.g., HP:0002311 for abnormal coordination)** (tatton‐brown2013weaversyndromeand pages 3-4)

### 3.3 Quality of life impact
Formal QoL instruments were not reported in the retrieved sources; however, developmental delay/intellectual disability (82%), hypotonia/hypertonia, and contractures/camptodactyly plausibly affect function and require early intervention/therapy (tatton‐brown2013weaversyndromeand pages 3-4).

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene(s)
- **EZH2** is the primary causal gene for classic Weaver syndrome (gibson2012mutationsinezh2 pages 1-3, tattonbrown2011germlinemutationsin pages 1-2).
- PRC2-related overlapping overgrowth syndromes exist for **EED** and **SUZ12**; these are clinically overlapping OGID syndromes and share a peripheral blood DNAm signature with WS (gao2024amousemodel pages 1-2, choufani2020dnamethylationsignature pages 1-2).

### 4.2 Pathogenic variants (types and examples)
- Variant spectrum is predominantly **missense** and many cases are **de novo** (tattonbrown2011germlinemutationsin pages 1-2, tatton‐brown2013weaversyndromeand pages 1-2).
- Truncating variants are uncommon and in the Tatton-Brown 2013 cohort were only identified in the final exon after the SET domain (tatton‐brown2013weaversyndromeand pages 1-2).
- A recurrent hotspot variant **p.Arg684Cys (R684C)** is described in early discovery cohorts and used for model organism work (tattonbrown2011germlinemutationsin pages 1-2, gao2024amousemodel pages 1-2).

### 4.3 Functional consequences (LoF vs dominant-negative)
**Canonical EZH2/PRC2 function:** EZH2 is the catalytic subunit of PRC2 and mediates methylation of histone H3 lysine 27 (H3K27), which is linked to chromatin compaction and repression (cohen2016weaversyndrome‐associatedezh2 pages 1-2, choufani2020dnamethylationsignature pages 1-2).

**In vitro LoF evidence:** Cohen et al. report WS-associated EZH2 amino-acid changes reduce EZH2 histone methyltransferase function in an in vitro PRC2 assay (DOI: 10.1002/humu.22946; published online 2015-12-23) (cohen2016weaversyndrome‐associatedezh2 pages 1-2).

**Recent (2024–2025) dominant-negative model:** Deevy et al. modeled 10 WS-associated EZH2 variants in isogenic ESCs and found global reductions in H3K27me2/3, increased H3K27ac, and chromatin decompaction consistent with dominant-negative interference with PRC2 activity (preprint posted 2023-06-01, cited here in 2024 posting; URL: https://doi.org/10.1101/2023.06.01.543208) (deevy2024dominantnegativeeffects pages 1-2). The peer-reviewed extension similarly concludes “dominant-negative interference” and reports derepression of weak Polycomb-bound growth control genes (Genes & Development, 2025-08; URL: https://doi.org/10.1101/gad.351884.124) (deevy2025dominantnegativeeffectsof pages 1-2).

### 4.4 Epigenetic information / DNA methylation episignatures
Choufani et al. reported a **highly specific and sensitive peripheral-blood DNA methylation (DNAm) signature** for EZH2/WS and showed it can distinguish LoF vs GoF missense variants and detect mosaicism (AJHG, 2020-05-07; DOI: 10.1016/j.ajhg.2020.03.008; URL: https://doi.org/10.1016/j.ajhg.2020.03.008) (choufani2020dnamethylationsignature pages 1-2). 

**Abstract quote (2020):**
- “Using genome-wide DNA methylation (DNAm) data… **pathogenic variants in EZH2 generate a highly specific and sensitive DNAm signature** … [that] **can be used to distinguish loss-of-function from gain-of-function missense variants and to detect somatic mosaicism**.” (choufani2020dnamethylationsignature pages 1-2)

A 2024 perspective emphasizes clinical use of DNAm signatures for VUS classification and warns that classifier scores should be complemented with additional analyses (Human Genetics; published online 2023-04-06; DOI: 10.1007/s00439-023-02544-2; URL: https://doi.org/10.1007/s00439-023-02544-2) (awamleh2024dnamethylationsignatures pages 1-2).

---

## 5. Environmental Information
No specific environmental contributors, lifestyle factors, or infectious triggers for Weaver syndrome were identified in the retrieved primary literature; the disorder is primarily monogenic (EZH2) (gibson2012mutationsinezh2 pages 1-3).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (genotype → epigenome → transcription → phenotype)
1. **Trigger:** Heterozygous pathogenic EZH2 missense variants (often de novo) (tattonbrown2011germlinemutationsin pages 1-2, gibson2012mutationsinezh2 pages 1-3).
2. **Primary molecular lesion:** Reduced and/or dominantly perturbed PRC2 catalytic activity altering H3K27 methylation balance (H3K27me2/3 depleted; H3K27ac increased), with chromatin decompaction and derepression of Polycomb-regulated gene sets (deevy2024dominantnegativeeffects pages 1-2, deevy2025dominantnegativeeffectsof pages 1-2).
3. **Downstream tissue programs:** In bone, dysregulated osteoblast differentiation and BMP pathway programs contribute to advanced bone age/skeletal overgrowth (gao2024amousemodel pages 1-2).
4. **Clinical manifestations:** Overgrowth/tall stature, advanced bone age, craniofacial phenotype, neurodevelopmental impairment (tatton‐brown2013weaversyndromeand pages 3-4, gibson2012mutationsinezh2 pages 1-3).

### 6.2 Pathways/processes implicated
- **Polycomb repression / chromatin organization:** PRC2-mediated H3K27 methylation and downstream PRC1 recruitment (chromatin compaction) (deevy2024dominantnegativeeffects pages 1-2).
- **Bone morphogenetic protein (BMP) pathway and osteoblast differentiation:** dysregulated in Ezh2R684C/+ osteoblasts by RNA-seq (gao2024amousemodel pages 1-2).

### 6.3 Suggested GO biological process terms (examples)
- **Histone H3-K27 methylation** (GO:0051568)
- **Chromatin organization** (GO:0006325)
- **Transcriptional regulation by Polycomb group proteins** (broadly captured under chromatin silencing terms)
- **Osteoblast differentiation** (GO:0001649)
- **BMP signaling pathway** (GO:0030509)

### 6.4 Suggested cell types (CL terms; examples)
- **Osteoblast (CL:0000062)** and **mesenchymal stem/stromal cell (MSC)**-like populations (bone marrow MSCs) are mechanistically implicated in the mouse model (gao2024amousemodel pages 1-2).

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level (with suggested UBERON terms)
- **Skeletal system / bone** (advanced bone age; skeletal overgrowth) (UBERON:0001434 “skeleton”) (gibson2012mutationsinezh2 pages 1-3, gao2024amousemodel pages 1-2)
- **Brain / nervous system** (developmental delay, variable intellectual disability) (UBERON:0000955 “brain”) (tatton‐brown2013weaversyndromeand pages 3-4)
- **Craniofacial structures** (distinct facial gestalt, retrognathia/chin crease) (UBERON craniofacial terms as appropriate) (tatton‐brown2013weaversyndromeand pages 3-4)

### 7.2 Tissue/cell level
- Bone-forming lineages: osteoblasts and bone marrow MSC-derived osteoblast differentiation programs (gao2024amousemodel pages 1-2).

### 7.3 Subcellular level
- **Nucleus / chromatin** (PRC2 is a chromatin-modifying complex; H3K27 modifications regulate compaction) (deevy2024dominantnegativeeffects pages 1-2, choufani2020dnamethylationsignature pages 1-2).

---

## 8. Temporal Development
- **Onset:** commonly prenatal and/or early postnatal overgrowth (gibson2012mutationsinezh2 pages 1-3, tatton‐brown2013weaversyndromeand pages 3-4).
- **Course:** overgrowth is often present from birth/early childhood; facial features may become more subtle with age, complicating adult recognition (tatton‐brown2013weaversyndromeand pages 1-2, tatton‐brown2013weaversyndromeand pages 3-4).

---

## 9. Inheritance and Population

### 9.1 Inheritance
- Primarily **de novo**, but **autosomal dominant** inheritance is supported by rare parent-to-child transmission (gibson2012mutationsinezh2 pages 1-3, tattonbrown2011germlinemutationsin pages 1-2).

### 9.2 Epidemiology
Robust prevalence/incidence estimates were not found in the retrieved primary texts used here. Available quantitative statements are limited to reported-case counts in specific publications (e.g., “Approximately 40 cases are known from the literature” in 2012; and “48 individuals with EZH2 mutations” in a 2013 cohort) (gibson2012mutationsinezh2 pages 1-3, tatton‐brown2013weaversyndromeand pages 1-2).

---

## 10. Diagnostics

### 10.1 Clinical recognition and differential diagnosis
Clinical overlap with Sotos syndrome is emphasized; distinguishing features for Weaver syndrome include retrognathia with prominent chin crease (“stuck-on” chin), increased prenatal growth, and a carpal bone age disproportionately advanced relative to metacarpal/phalangeal bone age (gibson2012mutationsinezh2 pages 1-3). 

### 10.2 Genetic testing approaches (current practice reflected in literature)
- **Trio-based WES** and confirmatory **Sanger sequencing** were used in the discovery paper to identify de novo EZH2 variants (gibson2012mutationsinezh2 pages 1-3).
- **Chromosomal microarray (CMA)** was used to exclude submicroscopic CNVs in discovery cases, and **NSD1 sequencing** was performed to exclude Sotos-like etiologies (gibson2012mutationsinezh2 pages 1-3).

### 10.3 Omics-based diagnostics: DNA methylation episignatures (real-world implementation)
- **Clinical implementation concept:** DNAm episignatures are used as syndrome-specific biomarkers and are “well established… especially for the classification of variants of uncertain significance (VUS)” (Awamleh et al., Human Genetics; published online 2023-04-06) (awamleh2024dnamethylationsignatures pages 1-2).
- **Weaver/PRC2-specific evidence:** an EZH2 DNAm signature for WS supports functional classification of EZH2 variants and can also classify variants in EED and SUZ12 (Choufani et al., AJHG 2020-05-07) (choufani2020dnamethylationsignature pages 1-2).

---

## 11. Outcome / Prognosis
Quantitative long-term outcomes (life expectancy, validated QoL, survival curves) were not present in the retrieved primary literature. Available evidence supports:
- Intellectual disability is common but “highly variable and frequently mild” in the large 2013 series (tatton‐brown2013weaversyndromeand pages 1-2).
- Clinical management is typically supportive and multidisciplinary (no disease-modifying therapy established in humans in the retrieved literature) (gao2024amousemodel pages 1-2).

---

## 12. Treatment

### 12.1 Current applications / real-world implementations (supportive care)
Disease management in the retrieved sources is largely symptomatic and supportive; MDEMs in general “still only consist of symptomatic management and preventative screening for known complications” (Gao et al., JCI Insight, 2024-01-09) (gao2024amousemodel pages 1-2).

**Suggested MAXO terms (examples):**
- **Genetic testing** (MAXO term for genetic diagnostic procedure; mapping depends on MAXO version)
- **Physical therapy** / **occupational therapy** / **speech therapy** (supportive developmental therapies)
- **Orthopedic management** (for contractures/camptodactyly)

### 12.2 Experimental / emerging therapeutics (preclinical)
A key 2024 advance is a genetically faithful mouse model for the common EZH2 p.R684C variant, which shows excess osteogenesis reversible by inhibiting KDM6A/KDM6B (gao2024amousemodel pages 1-2).

**Abstract quote (2024 JCI Insight):**
- “**Inhibition of the opposing H3K27 demethylases KDM6A and KDM6B substantially reversed the excessive osteogenesis…**” (Gao et al., 2024-01-09; DOI: 10.1172/jci.insight.173392; URL: https://doi.org/10.1172/jci.insight.173392) (gao2024amousemodel pages 1-2)

This provides a mechanistic rationale for considering **epigenetic modulating agents** in PRC2-related overgrowth disorders, though there is no clinical trial evidence for such agents in Weaver syndrome in the retrieved clinicaltrials.gov search results.

---

## 13. Prevention
Primary prevention is not applicable for a monogenic, typically de novo disorder. Practical prevention focuses on:
- **Genetic counseling** for recurrence risk and reproductive planning (autosomal dominant; most de novo) (tattonbrown2011germlinemutationsin pages 1-2, gibson2012mutationsinezh2 pages 1-3).
- **Secondary/tertiary prevention** via anticipatory guidance and monitoring for complications (developmental supports; orthopedic issues; malignancy vigilance) (tatton‐brown2013weaversyndromeand pages 3-4).

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary Weaver-syndrome analogs were identified in the retrieved texts.

---

## 15. Model Organisms
A 2024 **knock-in mouse model** of the common EZH2 p.R684C variant demonstrates:
- molecular phenotype (global H3K27me3 depletion in homozygous MEFs),
- organismal phenotype (skeletal overgrowth in heterozygotes),
- cellular phenotype (increased osteogenic activity),
- pathway dysregulation (BMP pathway and osteoblast differentiation transcriptome changes),
- and pharmacologic reversibility (KDM6A/6B inhibition) (gao2024amousemodel pages 1-2).

---

## Cancer risk and surveillance (expert opinion and recent consensus)
A 2024 AACR Childhood Cancer Predisposition Workshop update notes Weaver syndrome is associated with germline EZH2 variants and reports multiple cancers including **neuroblastoma**, germ cell tumors, leukemias, and lymphomas; neuroblastoma is described as the most common reported tumor type among Weaver cases (Clinical Cancer Research, 2024-06; DOI: 10.1158/1078-0432.CCR-24-0237; URL: https://doi.org/10.1158/1078-0432.ccr-24-0237) (kamihara2024neuroblastomapredispositionand pages 1-2). The same source describes a threshold framework for recommending neuroblastoma surveillance (≥1% neuroblastoma prevalence among carriers or segregation in multiple pedigrees) but the provided excerpt does not state a finalized surveillance recommendation for Weaver syndrome (kamihara2024neuroblastomapredispositionand pages 1-2).

---

## Structured disease tables (identifiers and phenotypic frequencies)
| Category | Field | Value | Source year | Journal | DOI / URL | PMID | Citation |
|---|---|---|---|---|---|---|---|
| Identifier | Disease name | Weaver syndrome | 2012 | The American Journal of Human Genetics | https://doi.org/10.1016/j.ajhg.2011.11.018 |  | (gibson2012mutationsinezh2 pages 1-3) |
| Identifier | MIM / OMIM | MIM 277590 | 2012 | The American Journal of Human Genetics | https://doi.org/10.1016/j.ajhg.2011.11.018 |  | (gibson2012mutationsinezh2 pages 1-3) |
| Identifier | Abbreviation | WS | 2024 | Molecular Syndromology | https://doi.org/10.1159/000533733 |  | (kendirdemirkol2024expandingthephenotypic pages 1-2) |
| Nomenclature | Synonyms / descriptors | Rare congenital overgrowth disorder; autosomal dominant overgrowth disorder; EZH2-related overgrowth syndrome | 2024 | Molecular Syndromology | https://doi.org/10.1159/000533733 |  | (kendirdemirkol2024expandingthephenotypic pages 1-2) |
| Genetics | Primary causal gene | EZH2 (enhancer of zeste homolog 2) | 2011 | Oncotarget | https://doi.org/10.18632/oncotarget.385 |  | (tattonbrown2011germlinemutationsin pages 1-2) |
| Genetics | EZH2 MIM / OMIM | MIM #601573 | 2016 | Human Mutation | https://doi.org/10.1002/humu.22946 |  | (cohen2016weaversyndrome‐associatedezh2 pages 1-2) |
| Genetics | Molecular class | Germline heterozygous pathogenic / likely pathogenic EZH2 variants, usually missense; many de novo | 2011 | Oncotarget | https://doi.org/10.18632/oncotarget.385 |  | (tattonbrown2011germlinemutationsin pages 1-2, tattonbrown2011germlinemutationsin pages 2-4) |
| Inheritance | Inheritance pattern | Autosomal dominant | 2024 | Molecular Syndromology | https://doi.org/10.1159/000533733 |  | (kendirdemirkol2024expandingthephenotypic pages 1-2) |
| Diagnostic descriptor | Typical diagnostic basis | Characteristic overgrowth/facial phenotype plus heterozygous pathogenic EZH2 variant on genetic testing | 2024 | Molecular Syndromology | https://doi.org/10.1159/000533733 |  | (kendirdemirkol2024expandingthephenotypic pages 1-2, tatton‐brown2013weaversyndromeand pages 1-2) |

| Clinical feature | Frequency / quantitative detail | Cohort / source detail | Source year | Journal | DOI / URL | PMID | Citation |
|---|---|---|---|---|---|---|---|
| Tall stature / height ≥ +2 SD | 41/45 (91%) | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Very tall stature / height ≥ +4 SD | 16 individuals | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Tall stature | ~90% | Review summary in case report | 2024 | Molecular Syndromology | https://doi.org/10.1159/000533733 |  | (kendirdemirkol2024expandingthephenotypic pages 1-2) |
| Intellectual disability / developmental delay | 37/45 (82%), usually mild (21/37 mild) | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Intellectual disability / developmental delay | ~80% | Review summary in case report | 2024 | Molecular Syndromology | https://doi.org/10.1159/000533733 |  | (kendirdemirkol2024expandingthephenotypic pages 1-2) |
| Camptodactyly / contractures | 45% | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Umbilical hernia | 43% | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Soft / doughy skin | 49% | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Hoarse, low-pitched cry | 37% | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Poor coordination / clumsiness | 28/35 (80%) | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Hypotonia | 44% | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Hypertonia | 28% | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Birth length > +2 SD | 12/18 | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Birth weight > +2 SD | 15/39 (38%) | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Macrocephaly / enlarged head circumference | Median +1.8 SD; range up to +5.5 SD | Tatton-Brown et al. EZH2-positive cohort | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Broad forehead, hypertelorism, almond-shaped palpebral fissures, retrognathia, pointed “stuck-on” chin, large fleshy ears | Qualitative recurrent craniofacial gestalt | Summarized clinical phenotype | 2013 | American Journal of Medical Genetics Part A | https://doi.org/10.1002/ajmg.a.36229 |  | (tatton‐brown2013weaversyndromeand pages 3-4) |
| Broad thumbs, large hands, prominent digit pads, deep palmar creases, overriding toes | Qualitative recurrent skeletal/digital findings | Review summary in case report | 2024 | Molecular Syndromology | https://doi.org/10.1159/000533733 |  | (kendirdemirkol2024expandingthephenotypic pages 1-2) |


*Table: These tables summarize key disease identifiers and nomenclature for Weaver syndrome and compile core clinical features with reported frequencies, prioritizing Tatton-Brown 2013 and Kendir-Demirkol 2024. They are useful for rapid knowledge-base extraction of ontology-ready identifiers, inheritance, and phenotype prevalence.*

---

## Key limitations of this report (based on tool-accessible full text)
- **MONDO/ICD/MeSH identifiers** were not present in the retrieved texts used here.
- **Prevalence/incidence** estimates were not found; available data are mainly reported-case counts and cohort sizes.
- **PMIDs** were not retrievable from the tool outputs for several papers; DOIs/URLs and publication dates are provided where available in-text.


References

1. (gibson2012mutationsinezh2 pages 1-3): William T. Gibson, Rebecca L. Hood, Shing Hei Zhan, Dennis E. Bulman, Anthony P. Fejes, Richard Moore, Andrew J. Mungall, Patrice Eydoux, Riyana Babul-Hirji, Jianghong An, Marco A. Marra, David Chitayat, Kym M. Boycott, David D. Weaver, and Steven J.M. Jones. Mutations in ezh2 cause weaver syndrome. The American Journal of Human Genetics, 90:110-118, Jan 2012. URL: https://doi.org/10.1016/j.ajhg.2011.11.018, doi:10.1016/j.ajhg.2011.11.018. This article has 346 citations.

2. (tatton‐brown2013weaversyndromeand pages 1-2): Katrina Tatton‐Brown, Anne Murray, Sandra Hanks, Jenny Douglas, Ruth Armstrong, Siddharth Banka, Lynne M. Bird, Carol L. Clericuzio, Valerie Cormier‐Daire, Tom Cushing, Frances Flinter, Marie‐Line Jacquemont, Shelagh Joss, Esther Kinning, Sally Ann Lynch, Alex Magee, Vivienne McConnell, Ana Medeira, Keiichi Ozono, Michael Patton, Julia Rankin, Debbie Shears, Marleen Simon, Miranda Splitt, Volker Strenger, Kyra Stuurman, Clare Taylor, Hannah Titheradge, Lionel Van Maldergem, I. Karen Temple, Trevor Cole, Sheila Seal, and Nazneen Rahman. Weaver syndrome and ezh2 mutations: clarifying the clinical phenotype. American Journal of Medical Genetics Part A, 161:2972-2980, Dec 2013. URL: https://doi.org/10.1002/ajmg.a.36229, doi:10.1002/ajmg.a.36229. This article has 181 citations.

3. (kendirdemirkol2024expandingthephenotypic pages 1-2): Yasemin Kendir-Demirkol, Burcu Yeter, and Laura A. Jenny. Expanding the phenotypic and genotypic spectrum of weaver syndrome: a missense variant of the ezh2 gene. Molecular Syndromology, 15:161-166, Sep 2024. URL: https://doi.org/10.1159/000533733, doi:10.1159/000533733. This article has 5 citations and is from a peer-reviewed journal.

4. (tatton‐brown2013weaversyndromeand pages 3-4): Katrina Tatton‐Brown, Anne Murray, Sandra Hanks, Jenny Douglas, Ruth Armstrong, Siddharth Banka, Lynne M. Bird, Carol L. Clericuzio, Valerie Cormier‐Daire, Tom Cushing, Frances Flinter, Marie‐Line Jacquemont, Shelagh Joss, Esther Kinning, Sally Ann Lynch, Alex Magee, Vivienne McConnell, Ana Medeira, Keiichi Ozono, Michael Patton, Julia Rankin, Debbie Shears, Marleen Simon, Miranda Splitt, Volker Strenger, Kyra Stuurman, Clare Taylor, Hannah Titheradge, Lionel Van Maldergem, I. Karen Temple, Trevor Cole, Sheila Seal, and Nazneen Rahman. Weaver syndrome and ezh2 mutations: clarifying the clinical phenotype. American Journal of Medical Genetics Part A, 161:2972-2980, Dec 2013. URL: https://doi.org/10.1002/ajmg.a.36229, doi:10.1002/ajmg.a.36229. This article has 181 citations.

5. (tattonbrown2011germlinemutationsin pages 1-2): Katrina Tatton-Brown, Sandra Hanks, Elise Ruark, Anna Zachariou, Silvana Del Vecchio Duarte, Emma Ramsay, Katie Snape, Anne Murray, Elizabeth R Perdeaux, Sheila Seal, Chey Loveday, Siddharth Banka, Carol Clericuzio, Frances Flinter, Alex Magee, Vivienne McConnell, Michael Patton, Wolfgang Raith, Julia Rankin, Miranda Splitt, Volker Strenger, Clare Taylor, Patricia Wheeler, I Karen Temple, Trevor Cole, Jenny Douglas, and Nazneen Rahman. Germline mutations in the oncogene ezh2 cause weaver syndrome and increased human height. Oncotarget, 2:1127-1133, Dec 2011. URL: https://doi.org/10.18632/oncotarget.385, doi:10.18632/oncotarget.385. This article has 195 citations.

6. (deevy2024dominantnegativeeffects pages 1-2): Orla Deevy, Craig Monger, Francesca Matrà, Ellen Tuck, Eric Conway, Mihaly Badonyi, Darragh Nimmo, Simona Rodighiero, Qi Zhang, Chen Davidovich, Joseph A. Marsh, Diego Pasini, and Adrian P. Bracken. Dominant negative effects on h3k27 methylation by weaver syndrome-associated ezh2 variants. bioRxiv, May 2024. URL: https://doi.org/10.1101/2023.06.01.543208, doi:10.1101/2023.06.01.543208. This article has 5 citations.

7. (deevy2025dominantnegativeeffectsof pages 1-2): Orla Deevy, Jingjing Li, Craig Monger, Francesca Matrà, Ellen Tuck, Molly Davies, Mihaly Badonyi, Maeve Boyce, Emma J. Doyle, Karsten Hokamp, Darragh Nimmo, Simona Rodighiero, Qi Zhang, Chen Davidovich, Joseph A. Marsh, Diego Pasini, Eric Conway, and Adrian P. Bracken. Dominant-negative effects of weaver syndrome-associated ezh2 variants. Genes &amp; Development, 39:1355-1376, Aug 2025. URL: https://doi.org/10.1101/gad.351884.124, doi:10.1101/gad.351884.124. This article has 7 citations and is from a highest quality peer-reviewed journal.

8. (gao2024amousemodel pages 1-2): Christine W. Gao, WanYing Lin, Ryan C. Riddle, Priyanka Kushwaha, Leandros Boukas, Hans T. Björnsson, Kasper D. Hansen, and Jill A. Fahrner. A mouse model of weaver syndrome displays overgrowth and excess osteogenesis reversible with kdm6a/6b inhibition. JCI Insight, Jan 2024. URL: https://doi.org/10.1172/jci.insight.173392, doi:10.1172/jci.insight.173392. This article has 14 citations and is from a domain leading peer-reviewed journal.

9. (cohen2016weaversyndrome‐associatedezh2 pages 1-2): Ana S.A. Cohen, Damian B. Yap, M.E. Suzanne Lewis, Chieko Chijiwa, Maria A. Ramos‐Arroyo, Natália Tkachenko, Valentina Milano, Mélanie Fradin, Margaret L. McKinnon, Katelin N. Townsend, Jieqing Xu, M.I. Allen, Colin J.D. Ross, William B. Dobyns, David D. Weaver, and William T. Gibson. Weaver syndrome‐associated ezh2 protein variants show impaired histone methyltransferase function in vitro. Human Mutation, 37:301-307, Jan 2016. URL: https://doi.org/10.1002/humu.22946, doi:10.1002/humu.22946. This article has 102 citations and is from a domain leading peer-reviewed journal.

10. (choufani2020dnamethylationsignature pages 1-2): Sanaa Choufani, William T. Gibson, Andrei L. Turinsky, Brian H.Y. Chung, Tianren Wang, Kopal Garg, Alessandro Vitriolo, Ana S.A. Cohen, Sharri Cyrus, Sarah Goodman, Eric Chater-Diehl, Jack Brzezinski, Michael Brudno, Luk Ho Ming, Susan M. White, Sally Ann Lynch, Carol Clericuzio, I. Karen Temple, Frances Flinter, Vivienne McConnell, Tom Cushing, Lynne M. Bird, Miranda Splitt, Bronwyn Kerr, Stephen W. Scherer, Jerry Machado, Eri Imagawa, Nobuhiko Okamoto, Naomichi Matsumoto, Guiseppe Testa, Maria Iascone, Romano Tenconi, Oana Caluseriu, Roberto Mendoza-Londono, David Chitayat, Cheryl Cytrynbaum, Katrina Tatton-Brown, and Rosanna Weksberg. Dna methylation signature for ezh2 functionally classifies sequence variants in three prc2 complex genes. The American Journal of Human Genetics, 106:596-610, May 2020. URL: https://doi.org/10.1016/j.ajhg.2020.03.008, doi:10.1016/j.ajhg.2020.03.008. This article has 98 citations.

11. (awamleh2024dnamethylationsignatures pages 1-2): Zain Awamleh, Sarah Goodman, Sanaa Choufani, and Rosanna Weksberg. Dna methylation signatures for chromatinopathies: current challenges and future applications. Human Genetics, 143:551-557, Apr 2024. URL: https://doi.org/10.1007/s00439-023-02544-2, doi:10.1007/s00439-023-02544-2. This article has 23 citations and is from a peer-reviewed journal.

12. (kamihara2024neuroblastomapredispositionand pages 1-2): Junne Kamihara, Lisa R. Diller, William D. Foulkes, Orli Michaeli, Yoshiko Nakano, Kristian W. Pajtler, Melissa Perrino, Sarah R. Scollon, Douglas R. Stewart, Stephan Voss, Rosanna Weksberg, Jordan R. Hansford, and Garrett M. Brodeur. Neuroblastoma predisposition and surveillance-an update from the 2023 aacr childhood cancer predisposition workshop. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:OF1-OF7, Jun 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-0237, doi:10.1158/1078-0432.ccr-24-0237. This article has 29 citations.

13. (tattonbrown2011germlinemutationsin pages 2-4): Katrina Tatton-Brown, Sandra Hanks, Elise Ruark, Anna Zachariou, Silvana Del Vecchio Duarte, Emma Ramsay, Katie Snape, Anne Murray, Elizabeth R Perdeaux, Sheila Seal, Chey Loveday, Siddharth Banka, Carol Clericuzio, Frances Flinter, Alex Magee, Vivienne McConnell, Michael Patton, Wolfgang Raith, Julia Rankin, Miranda Splitt, Volker Strenger, Clare Taylor, Patricia Wheeler, I Karen Temple, Trevor Cole, Jenny Douglas, and Nazneen Rahman. Germline mutations in the oncogene ezh2 cause weaver syndrome and increased human height. Oncotarget, 2:1127-1133, Dec 2011. URL: https://doi.org/10.18632/oncotarget.385, doi:10.18632/oncotarget.385. This article has 195 citations.

## Artifacts

- [Edison artifact artifact-00](Weaver_Syndrome-deep-research-falcon_artifacts/artifact-00.md)