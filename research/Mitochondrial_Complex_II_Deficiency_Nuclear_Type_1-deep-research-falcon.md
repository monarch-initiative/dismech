---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-24T16:53:29.168034'
end_time: '2026-07-24T17:04:30.686945'
duration_seconds: 661.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mitochondrial Complex II Deficiency, Nuclear Type 1
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
  path: Mitochondrial_Complex_II_Deficiency_Nuclear_Type_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex II Deficiency, Nuclear Type 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex II Deficiency, Nuclear Type 1** covering all of the
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
- **Disease Name:** Mitochondrial Complex II Deficiency, Nuclear Type 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex II Deficiency, Nuclear Type 1** covering all of the
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


# Mitochondrial Complex II Deficiency, Nuclear Type 1: Disease-Characteristics Report

## Executive summary

Mitochondrial complex II deficiency, nuclear type 1 is an ultra-rare, usually autosomal-recessive primary mitochondrial disorder caused by biallelic pathogenic variants in **SDHA**, which encodes the flavoprotein catalytic subunit of succinate dehydrogenase/respiratory-chain complex II. The best-established presentation is an infantile or childhood-onset Leigh/Leigh-like encephalopathy, although leukodystrophy, optic atrophy–ataxia–myopathy, cardiomyopathy, and other multisystem presentations broaden the spectrum. Published evidence consists predominantly of individual patients and small case series; as of a major 2015 study, only 25 patients with 11 recessive SDHA variants had been reported. Therefore, disease-specific frequencies, survival estimates, penetrance, and treatment-response rates remain unavailable. (renkema2015sdhamutationscausing pages 1-2, jackson2014mutationsinsdhd pages 1-2)

The key biochemical defect is impaired FAD-dependent oxidation of succinate to fumarate and electron transfer through SDHB to ubiquinone. Patient fibroblasts may retain only 8–26% of normal complex II activity, with reduced succinate oxidation and substrate-specific impairment of ATP/phosphocreatine production. There is currently no proven SDHA-specific disease-modifying therapy; care is supportive, multidisciplinary, and phenotype-directed. (renkema2015sdhamutationscausing pages 4-5, renkema2015sdhamutationscausing pages 5-6, vranken2014sdhaf4promotesmitochondrial pages 1-2)

The following table provides a concise knowledge-base summary before the detailed report.

| Domain | Summary | Evidence type | Ontology / terms | Key citations |
|---|---|---|---|---|
| Identifiers | **Mitochondrial Complex II Deficiency, Nuclear Type 1** is a rare primary mitochondrial disease caused by **SDHA** dysfunction; disease-target mapping supports **MONDO:0100294**. The condition corresponds to **OMIM 252011** in recent diagnostic literature. It is a disease-level entity derived from curated literature/databases rather than EHR-only evidence. | Curated disease resource + human literature | MONDO:0100294 | (OpenTargets Search: mitochondrial complex II deficiency-SDHA, renkema2015sdhamutationscausing pages 1-2) |
| Gene / inheritance | **SDHA** is the established causal gene for nuclear type 1 disease. In the mitochondrial disease context, inheritance is **autosomal recessive** with **biallelic** pathogenic variants. This is distinct from **heterozygous SDHA** tumor-predisposition states (paraganglioma/pheochromocytoma/GIST risk), which are a separate clinical context. | Human clinical/genetic; expert curation | SDHA; AR inheritance | (renkema2015sdhamutationscausing pages 1-2, renkema2015sdhamutationscausing pages 2-3, jackson2014mutationsinsdhd pages 1-2, mccormick2023expertpanelcuration pages 15-20) |
| Molecular defect | SDHA encodes the **flavoprotein subunit of succinate dehydrogenase / respiratory chain complex II**, containing covalently bound **FAD** and participating in succinate oxidation with electron transfer through SDHB to ubiquinone. Disease variants reduce SDHA protein, impair holocomplex II assembly/function, and can arise from nonsense, missense, or splice-disrupting alleles. Reported pathogenic alleles in the gathered evidence include **c.356G>A (p.Trp119\*)**, **c.248C>T** (novel splice site), **c.91C>T (p.Arg31\*)**, **c.565T>G (p.Cys189Gly)**, **c.1065-3C>A**, and **c.64-2A>G**. | Human clinical/genetic + biochemical + model-organism mechanistic | GO suggestions: succinate dehydrogenase activity; mitochondrial respiratory chain complex II; tricarboxylic acid cycle | (renkema2015sdhamutationscausing pages 3-4, renkema2015sdhamutationscausing pages 4-5, renkema2015sdhamutationscausing pages 5-6, vranken2014sdhaf4promotesmitochondrial pages 1-2, ackrell2002cytopathiesinvolvingmitochondrial pages 1-3) |
| Phenotype spectrum | Reported SDHA-specific manifestations span **Leigh syndrome / Leigh-like disease**, **leukodystrophy**, and broader multisystem mitochondrial disease. Features reported in the gathered evidence include **developmental regression**, **ataxia**, **dystonia**, **myopathy**, **optic atrophy**, **hepatomegaly**, **seizures/epilepsy**, **lactic acidemia**, and elevated urinary TCA-cycle intermediates. Suggested HPO terms: Leigh syndrome phenotype, developmental regression, ataxia, dystonia, myopathy, optic atrophy, seizures, hepatomegaly, lactic acidosis. | Human clinical | HPO suggestions listed in Summary | (renkema2015sdhamutationscausing pages 1-2) |
| Onset / course | In reported SDHA-specific cases, symptoms often begin **in the first year of life** with regression and progressive neurologic disease; however, literature cited in the gathered evidence also notes **late-onset neurodegenerative presentations** with optic atrophy, ataxia, and myopathy for SDHA-related complex II disease more broadly. Disease course is therefore **progressive and variable**, but often severe in infantile Leigh-spectrum presentations. | Human clinical | HPO suggestions: infantile onset; progressive neurologic deterioration | (jackson2014mutationsinsdhd pages 1-2, renkema2015sdhamutationscausing pages 1-2) |
| Biochemical signature | Hallmarks are **isolated complex II deficiency** with markedly reduced complex II enzymatic activity in **fibroblasts and/or muscle**, reduced **succinate oxidation**, impaired **ATP + phosphocreatine production** with **succinate + acetylcarnitine** substrate, and relative preservation of **pyruvate + malate** oxidation. Residual complex II activity reported in patient fibroblasts was about **8–26%** of normal in one study. General SDH biology predicts **succinate accumulation** and depletion of downstream TCA intermediates. | Human biochemical + mechanistic model evidence | CHEBI suggestions: succinate, fumarate, FAD | (renkema2015sdhamutationscausing pages 4-5, renkema2015sdhamutationscausing pages 5-6, vranken2014sdhaf4promotesmitochondrial pages 7-8, vranken2014sdhaf4promotesmitochondrial pages 1-2) |
| Diagnosis | **SDHA-specific evidence:** diagnosis has used enzyme studies in **fibroblasts/muscle**, ATP production assays, Western blot/blue native analysis for reduced SDHA/complex II, and molecular testing confirming biallelic SDHA variants. **General PMD guidance:** current best practice has shifted from **“biopsy first”** to **genomics first**, with **simultaneous mtDNA + nuclear DNA testing** recommended where possible; trio **WES/WGS** is appropriate especially for urgent pediatric cases, and muscle biopsy remains useful when blood/urine testing is unrevealing or for some mtDNA-specific questions. Differential diagnosis includes other mitochondrial and non-mitochondrial metabolic/neurogenetic disorders. | SDHA-specific human studies + general PMD consensus/guideline | General PMD guidance clearly labeled | (renkema2015sdhamutationscausing pages 2-3, renkema2015sdhamutationscausing pages 4-5, mavraki2023genetictestingfor pages 2-3, mavraki2023genetictestingfor pages 1-2, mavraki2023genetictestingfor pages 3-4) |
| Treatment / management | **No SDHA-specific disease-modifying therapy was identified in the gathered evidence.** Management is supportive and phenotype-directed. **General PMD guidance:** seizure care should generally follow **NICE** pathways, with the important exception that **valproic acid is contraindicated in POLG disease**; many ASMs are considered not generally contraindicated in PMD with monitoring, and **ketogenic diet** is considered not contraindicated in PMD overall though this is not SDHA-specific evidence. Vitamins/cofactors are widely used in PMD practice, but strong efficacy data are lacking in general PMD surveys/reviews. | General PMD expert consensus; limited direct SDHA evidence | MAXO suggestions: seizure management; ketogenic diet; genetic counseling; supportive care | (mancuso2024managementofseizures pages 4-5, mancuso2024managementofseizures pages 1-2) |
| Prognosis | Direct SDHA nuclear type 1 prognosis data are sparse in the gathered evidence. Available case-based evidence supports a **severe, progressive neurologic disorder** in many infantile Leigh-spectrum cases. Outcome heterogeneity exists, with some broader SDHA disease presentations occurring later in life. No disease-specific survival percentages were identified. | Human case literature | HPO suggestions: neurodegeneration; failure to thrive / severe disability where present | (jackson2014mutationsinsdhd pages 1-2, renkema2015sdhamutationscausing pages 1-2) |
| Epidemiology | Ultra-rare disorder. One cited SDHA study noted that, at the time of publication, **11 different autosomal-recessive SDHA mutations** had been described in **25 patients** with isolated complex II deficiency. General PMD prevalence figures from guidelines are **~12.5/100,000 adults** and **~4.7/100,000 children**, but these are **not specific** to SDHA nuclear type 1. | Human literature + general PMD guideline | Rare disease | (renkema2015sdhamutationscausing pages 1-2, mavraki2023genetictestingfor pages 1-2) |
| Key evidence gaps | Major gaps include: absence of large natural-history cohorts; no disease-specific prevalence/incidence estimates; no robust penetrance estimates for recessive SDHA mitochondrial disease; limited quantitative genotype-phenotype correlation; little direct quality-of-life data; no established SDHA-specific treatment trials found; and limited omics/single-cell/spatial data specific to this disease. | Evidence synthesis | Not applicable | (renkema2015sdhamutationscausing pages 1-2, mccormick2023expertpanelcuration pages 15-20, mavraki2023genetictestingfor pages 2-3, mancuso2024managementofseizures pages 1-2) |


*Table: This table provides a compact knowledge-base summary of Mitochondrial Complex II Deficiency, Nuclear Type 1, separating SDHA-specific evidence from broader primary mitochondrial disease guidance. It is useful for rapid curation of identifiers, genetics, pathophysiology, diagnosis, and current evidence gaps.*

## 1. Disease information

### Definition and scope

This disease is an inherited oxidative-phosphorylation disorder in which deficient succinate dehydrogenase causes an isolated respiratory-chain complex II defect. “Nuclear type 1” refers specifically to **SDHA-related disease**. It should not be conflated with complex II deficiencies caused by **SDHB, SDHC, SDHD, SDHAF1**, or other assembly genes, nor with monoallelic SDHA-associated tumor predisposition. Open Targets maps the entity to SDHA and, less specifically, also reports SDHAF1 association evidence; for strict knowledge-base curation, however, nuclear type 1 should be modeled as the SDHA disease entity. (OpenTargets Search: mitochondrial complex II deficiency-SDHA, renkema2015sdhamutationscausing pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0100294.
- **OMIM:** 252011.
- **Common names:** mitochondrial complex II deficiency, nuclear type 1; SDHA-related mitochondrial complex II deficiency; SDHA deficiency; succinate dehydrogenase flavoprotein-subunit deficiency; isolated complex II deficiency due to SDHA; SDHA-related Leigh syndrome/Leigh-like syndrome.
- **Broader phenotype labels:** Leigh syndrome spectrum, mitochondrial encephalomyopathy, leukodystrophy, and optic atrophy–ataxia–myopathy phenotype.
- **Orphanet/MeSH:** a specific validated identifier was not recovered from the accessed evidence. Broad MeSH indexing would generally fall under mitochondrial diseases, electron-transport-chain complex diseases, Leigh disease, or succinate dehydrogenase deficiency.
- **ICD-10/ICD-11:** no unique disease-specific code was identified. Coding generally uses broader mitochondrial-metabolism/respiratory-chain or Leigh-syndrome categories.

The evidence is principally **aggregated disease-level curation plus published individual-patient observations**, not EHR-derived population evidence. The 2015 primary study analyzed four patients and summarized the prior literature. (renkema2015sdhamutationscausing pages 1-2)

## 2. Etiology

### Causal factor

The primary cause is a germline, usually biallelic pathogenic or likely pathogenic variant in **SDHA**. SDHA forms the FAD-containing catalytic subunit of complex II. Recessive alleles reduce protein abundance, destabilize complex II, disrupt flavoprotein function, or impair catalysis. Parents are generally heterozygous carriers. (renkema2015sdhamutationscausing pages 3-4, renkema2015sdhamutationscausing pages 4-5)

### Genetic risk factors

The major risk factor is having two disease-causing SDHA alleles inherited in trans or, in consanguineous families, a homozygous pathogenic allele. Reported molecular classes include nonsense, missense, canonical or near-splice-site, and cryptic splice-creating variants. No validated common susceptibility loci, polygenic risk scores, protective alleles, or disease-specific modifier genes have been established. (renkema2015sdhamutationscausing pages 3-4, renkema2015sdhamutationscausing pages 4-5)

A clinically important distinction is that **biallelic SDHA variants cause systemic mitochondrial disease**, whereas some **heterozygous SDHA loss-of-function variants predispose to paraganglioma, pheochromocytoma, or gastrointestinal stromal tumor**, usually after somatic loss of the remaining allele. The same allele, such as c.91C>T, p.Arg31*, can occur in these different genetic contexts. (renkema2015sdhamutationscausing pages 1-2, renkema2015sdhamutationscausing pages 3-4, renkema2015sdhamutationscausing pages 2-3)

### Environmental, infectious, and lifestyle risk factors

No environmental exposure, lifestyle behavior, toxin, or pathogen is known to cause this Mendelian disease. Fever, fasting, infection, anesthesia, or other catabolic stress may plausibly precipitate metabolic decompensation in mitochondrial disorders, but disease-specific SDHA interaction data were not identified. Smoking, diet, alcohol, occupation, sex, and radiation are not established causal risks.

### Protective factors and gene–environment interaction

No validated human protective factor is known. In a **conditional Sdhc-loss mouse model**, chronic 10% oxygen substantially prolonged survival despite profound oxidative-metabolism impairment. This is a preclinical complex II observation, not evidence supporting therapeutic hypoxia in people with SDHA deficiency. (khazal2019aconditionalmouse pages 1-2)

## 3. Phenotypes

Because published cohorts are tiny, frequencies below should be treated as qualitative rather than population estimates.

| Phenotype | Type and usual characteristics | Suggested HPO term |
|---|---|---|
| Developmental delay/regression | Symptom/sign; commonly begins during infancy, may be progressive and severe | Global developmental delay; Developmental regression |
| Leigh/Leigh-like encephalopathy | Clinical/imaging syndrome; bilateral deep-gray or brainstem lesions with neurologic deterioration | Leigh syndrome; Abnormality of the basal ganglia |
| Ataxia | Neurologic sign; childhood or later onset; progressive or episodically worsened | Ataxia |
| Dystonia | Movement-disorder sign, often associated with basal-ganglia injury | Dystonia |
| Seizures/epilepsy | Neurologic symptom; may be early and difficult to control | Seizure; Epileptic encephalopathy |
| Hypotonia or myopathy | Neuromuscular sign; variable proximal weakness/exercise intolerance | Muscular hypotonia; Myopathy; Muscle weakness |
| Optic atrophy | Ophthalmic sign; can dominate later-onset disease and impair vision severely | Optic atrophy |
| Leukodystrophy | MRI/neuropathologic phenotype; reported in SDHA patients | Leukodystrophy; Abnormal cerebral white matter morphology |
| Lactic acidemia | Laboratory abnormality; may fluctuate with illness and tissue energy demand | Lactic acidosis; Increased serum lactate |
| Abnormal urinary TCA intermediates | Laboratory abnormality; nonspecific but mechanistically consistent | Abnormal urine metabolite level |
| Hepatomegaly | Physical sign in some multisystem cases | Hepatomegaly |
| Cardiomyopathy | Reported within the broader complex II/SDHA spectrum; severity variable | Dilated or hypertrophic cardiomyopathy, as observed |

The primary SDHA series describes regression beginning in the first year, ataxia, dystonia, myopathy, optic atrophy, hepatomegaly, seizures, lactic acidemia, and elevated urinary citric-acid-cycle intermediates. MRI may show focal bilateral lesions in the basal ganglia, thalamus, cerebellum, or spinal cord; leukodystrophy was also observed. (renkema2015sdhamutationscausing pages 1-2, renkema2015sdhamutationscausing pages 2-3)

Direct EQ-5D, SF-36, PROMIS, caregiver-burden, or disease-specific quality-of-life studies were not identified. Nevertheless, regression, motor disability, epilepsy, visual loss, feeding/respiratory complications, and multisystem surveillance are expected to substantially restrict mobility, communication, education, independence, and family well-being.

## 4. Genetic and molecular information

### Gene annotation

- **Gene:** SDHA — succinate dehydrogenase complex flavoprotein subunit A.
- **Ensembl target in Open Targets:** ENSG00000073578.
- **Inheritance:** predominantly autosomal recessive for mitochondrial complex II deficiency.
- **Origin:** germline. Somatic second hits pertain to tumorigenesis, not the inherited metabolic phenotype itself. (OpenTargets Search: mitochondrial complex II deficiency-SDHA, renkema2015sdhamutationscausing pages 2-3)

### Selected reported variants

| Variant | Class/consequence | Evidence summarized in the primary study |
|---|---|---|
| c.356G>A, p.Trp119* | Nonsense | Premature termination and nonsense-mediated decay |
| c.248C>T | Cryptic splice-creating | Abnormal splicing and reduced expression |
| c.91C>T, p.Arg31* | Nonsense | Mitochondrial disease allele also reported in tumor-predisposition contexts |
| c.565T>G, p.Cys189Gly | Missense in/near FAD-binding region | Severe activity defect; partial function; wild-type complementation restored activity |
| c.1065-3C>A | Near-splice-site | Exon 9 skipping, frameshift/NMD, with some residual normal splicing |
| c.64-2A>G | Canonical splice acceptor | Alternative transcripts, including an 18-amino-acid insertion; reduced SDHA |

All four patients in the 2015 series had clearly reduced SDHA protein; blue-native analysis demonstrated reduced complex II holocomplex. (renkema2015sdhamutationscausing pages 3-4, renkema2015sdhamutationscausing pages 4-5, renkema2015sdhamutationscausing pages 5-6)

### Variant classification and allele frequency

The cited functional and segregation evidence supports pathogenicity for the reported biallelic alleles. However, current ClinVar classifications and exact gnomAD/TOPMed frequencies were not available in the retrieved record and should be added by a live variant-level database query before production use. Variant interpretation should incorporate segregation, rarity, RNA studies for splice variants, complex II enzymology, SDHA protein/assembly studies, and functional complementation. A single heterozygous variant is generally insufficient to diagnose recessive mitochondrial complex II deficiency.

### Modifiers, epigenetics, and structural variants

No confirmed modifier gene, disease-specific methylation signature, histone mark, recurrent CNV, aneuploidy, inversion, or translocation has been established. Succinate can inhibit α-ketoglutarate-dependent dioxygenases and alter DNA/histone demethylation in SDH-null tumor models, but that mechanism should not be automatically assigned to residual-activity SDHA mitochondrial disease without direct evidence. (takacsvellai2021modelsystemsin pages 11-12)

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupation, lifestyle factor, or infectious agent is established as a primary contributor. Avoidance of prolonged fasting, dehydration, overheating, and severe catabolic stress is often advised in mitochondrial medicine, but this is general practice rather than trial-proven SDHA-specific prevention. There is no zoonotic or transmissible component.

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. **Biallelic SDHA variant** causes absent, reduced, unstable, or catalytically impaired SDHA.
2. **FAD-dependent succinate oxidation falls.** SDHA normally contains covalently attached FAD and oxidizes succinate to fumarate.
3. **Electron transfer is impaired.** Electrons normally pass through SDHB iron–sulfur centers to ubiquinone in the inner mitochondrial membrane.
4. **Complex II assembly/activity declines**, producing an isolated respiratory-chain defect and blocking a TCA-cycle step.
5. **Downstream metabolic effects** include impaired succinate-supported respiration, reduced ATP/phosphocreatine production, succinate accumulation, and depletion of fumarate/malate.
6. **Secondary injury** may include redox imbalance and ROS, failure of neuronal/muscular bioenergetic adaptation, cellular dysfunction, and neurodegeneration.
7. **Clinical manifestations** emerge preferentially in high-energy tissues—brain, skeletal muscle, retina/optic nerve, and sometimes heart. (renkema2015sdhamutationscausing pages 5-6, vranken2014sdhaf4promotesmitochondrial pages 7-8, vranken2014sdhaf4promotesmitochondrial pages 1-2, ackrell2002cytopathiesinvolvingmitochondrial pages 1-3)

Complex II does not itself pump protons, but it feeds electrons into the ubiquinone pool and supports proton pumping by downstream complexes III and IV. Thus, its loss reduces respiratory flux and ATP generation. Patient cells showed impaired ATP plus phosphocreatine production with succinate/acetylcarnitine while pyruvate/malate-supported oxidation was preserved, providing a substrate-specific functional signature. (renkema2015sdhamutationscausing pages 5-6)

### Biochemical and profiling findings

In the four-patient study, fibroblast complex II activity was approximately **8–26% of control**, accompanied by reduced succinate oxidation, SDHA protein, and holocomplex assembly. Wild-type SDHA lentiviral complementation partially and significantly restored activity, supporting causality. (renkema2015sdhamutationscausing pages 4-5, renkema2015sdhamutationscausing pages 5-6)

Model systems show increased succinate and reduced fumarate/malate after SDH disruption. Excess ROS may arise from incompletely assembled flavinated SDHA or disturbed electron flow. These findings are mechanistically persuasive but not a validated human plasma metabolomic signature. (vranken2014sdhaf4promotesmitochondrial pages 7-8, vranken2014sdhaf4promotesmitochondrial pages 1-2, vranken2014sdhaf4promotesmitochondrial pages 6-7)

No disease-specific bulk transcriptomic, proteomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omic dataset was identified. Contemporary Leigh organoid/single-cell work largely concerns other genes and cannot yet be transferred directly to SDHA.

### Suggested ontology annotations

- **GO biological process:** tricarboxylic acid cycle; aerobic respiration; mitochondrial electron transport, succinate to ubiquinone; ATP metabolic process; response to oxidative stress; nervous-system development.
- **GO molecular function:** succinate dehydrogenase (ubiquinone) activity; FAD binding; oxidoreductase activity.
- **GO cellular component:** mitochondrial inner membrane; respiratory-chain complex II; mitochondrial matrix-facing catalytic domain.
- **CL suggestions:** neuron, neural progenitor cell, astrocyte, skeletal-muscle fiber, cardiomyocyte, retinal ganglion cell, oligodendrocyte.
- **CHEBI suggestions:** succinate, fumarate, flavin adenine dinucleotide, ubiquinone, ATP, lactate, reactive oxygen species.

## 7. Anatomical structures affected

The **central nervous system** is the principal organ system in classic disease. Lesions can involve basal ganglia, thalamus, brainstem, cerebellum, spinal cord, and cerebral white matter. Skeletal muscle, optic nerve/retinal ganglion-cell axons, liver, and myocardium may also be involved. Laterality is usually bilateral/symmetric for Leigh-pattern MRI lesions rather than unilateral. (renkema2015sdhamutationscausing pages 1-2)

Suggested anatomical terms include brain, basal ganglion, thalamus, brainstem, cerebellum, spinal cord, cerebral white matter, skeletal muscle tissue, optic nerve, retina, liver, and heart. Subcellular annotation should use **mitochondrion**, **mitochondrial inner membrane**, and **respiratory-chain complex II**.

## 8. Temporal development

Typical severe disease begins congenitally, in infancy, or early childhood. Regression in the first year is well documented, often followed by progressive movement disorder, epilepsy, weakness, optic dysfunction, and multisystem complications. Later-onset optic atrophy, ataxia, and myopathy demonstrate broader expressivity. (jackson2014mutationsinsdhd pages 1-2, renkema2015sdhamutationscausing pages 1-2)

There is no validated staging system. A practical clinical framework is:

- **Early:** developmental delay/regression, hypotonia, feeding difficulty, episodic decompensation, or initial MRI abnormalities.
- **Intermediate:** progressive ataxia/dystonia, epilepsy, weakness, visual impairment, and expanding MRI lesions.
- **Advanced:** severe motor/cognitive disability, refractory epilepsy, bulbar or respiratory dysfunction, and possible cardiac or other organ failure.

The course is chronic and lifelong, commonly progressive and potentially punctuated by illness-associated deterioration. Spontaneous remission is not established. Early genetic diagnosis, nutritional support, seizure control, surveillance, and avoidance of metabolic stress are the main actionable windows.

## 9. Inheritance and population

### Epidemiology

No disease-specific prevalence or incidence estimate exists. By 2015, the literature contained **25 patients and 11 different recessive SDHA variants**, demonstrating extreme rarity and substantial ascertainment bias. Complex II deficiency has been estimated to account for roughly **2–4% of oxidative-phosphorylation defects**, but that includes genes other than SDHA. (jackson2014mutationsinsdhd pages 1-2, renkema2015sdhamutationscausing pages 1-2)

For context only, primary mitochondrial diseases collectively occur in approximately 1 in 4,300 people; UK guidance cites about 12.5 per 100,000 adults and 4.7 per 100,000 children. These figures must not be entered as SDHA-disease prevalence. (mavraki2023genetictestingfor pages 1-2, mancuso2024managementofseizures pages 1-2)

### Recurrence and population genetics

- **Recurrence risk:** for two carrier parents, 25% affected, 50% carrier, and 25% unaffected/non-carrier per pregnancy.
- **Penetrance:** likely high for clearly damaging biallelic combinations, but not quantified; hypomorphic alleles produce variable expressivity.
- **Anticipation:** not expected.
- **Germline mosaicism:** theoretically possible but not a reported defining feature.
- **Consanguinity:** increases homozygous recessive risk but is not necessary.
- **Founder effects/carrier frequency:** no reliable SDHA nuclear type 1 estimates were identified.
- **Sex ratio:** no demonstrated sex bias.
- **Ethnic/geographic distribution:** reported across multiple populations; no validated high-prevalence population.

## 10. Diagnostics

### Recommended diagnostic approach

Current mitochondrial guidelines support a **genomics-first** strategy rather than routine “biopsy first.” For complex or urgent pediatric presentations, simultaneous nuclear and mitochondrial testing is preferred when available, with trio WES or WGS particularly useful. WGS can assess nuclear genes, mtDNA, CNVs, and difficult intronic regions more comprehensively than conventional panels; WES may need separate high-depth mtDNA sequencing. (mavraki2023genetictestingfor pages 2-3, mavraki2023genetictestingfor pages 1-2, mavraki2023genetictestingfor pages 3-4)

For suspected SDHA disease:

1. Perform a comprehensive mitochondrial/Leigh/leukodystrophy panel or trio WES/WGS that includes **SDHA, SDHB, SDHC, SDHD, SDHAF1, SDHAF2**, other respiratory-chain genes, and relevant phenocopies.
2. Analyze mtDNA concurrently where feasible.
3. Confirm candidate SDHA variants by an orthogonal method and establish phase/parental segregation.
4. For splice variants, perform RNA/cDNA analysis when possible.
5. If genetics is negative or uncertain but biochemical suspicion remains high, assay respiratory-chain complexes in fibroblasts or muscle, including complex II normalized to citrate synthase and other complexes.
6. Assess SDHA protein and complex II assembly by immunoblot/blue-native PAGE where available.
7. Consider functional complementation or validated activity assays for unresolved VUS.

Single-gene SDHA sequencing is reasonable when isolated complex II deficiency is already demonstrated, but broad sequencing is usually more efficient because Leigh syndrome is genetically heterogeneous. CMA, karyotyping, and FISH are not first-line tests unless a syndromic CNV is suspected. Repeat-expansion testing is not relevant. mtDNA testing is necessary for the broader differential but does not directly detect this nuclear disease. (renkema2015sdhamutationscausing pages 2-3, renkema2015sdhamutationscausing pages 4-5, mavraki2023genetictestingfor pages 2-3)

### Clinical tests and biomarkers

- Plasma/serum lactate, pyruvate, lactate:pyruvate ratio, glucose, electrolytes, bicarbonate, liver enzymes, CK, amino acids, and acylcarnitines.
- Urine organic acids, including TCA-cycle intermediates.
- Brain MRI with diffusion and spectroscopy where indicated; typical abnormalities are bilateral deep-gray, brainstem/cerebellar, spinal, or white-matter lesions.
- EEG for seizures; ECG, echocardiography, and rhythm monitoring for cardiac involvement.
- Ophthalmologic assessment including optic nerve and retinal evaluation.
- Swallow, respiratory, hearing, endocrine, renal, and nutritional assessments according to phenotype.
- Muscle biopsy may show isolated complex II deficiency; histology can be nondiagnostic, making enzymology and genetics essential.

Lactate can be normal between crises, and no single circulating biomarker confirms SDHA deficiency.

### Differential diagnosis

Important alternatives include other Leigh-spectrum disorders; other complex II deficiencies; complex I, III, IV, or V deficiencies; pyruvate dehydrogenase deficiency; mitochondrial aminoacyl-tRNA-synthetase disorders; POLG disease; biotin-thiamine-responsive basal-ganglia disease; organic acidemias; leukodystrophies; hereditary optic neuropathies; and primary cardiomyopathy or epilepsy genes. Trio gene-agnostic WES/WGS is valuable where mitochondrial disease is one of several possible diagnoses. (mavraki2023genetictestingfor pages 2-3, mavraki2023genetictestingfor pages 3-4)

### Screening

There is no population or newborn screening program. Once familial variants are known, cascade carrier testing, prenatal diagnosis, and preimplantation genetic testing for monogenic disease are technically feasible. Biochemical screening of asymptomatic relatives is less reliable than targeted molecular testing.

## 11. Outcome and prognosis

Disease-specific 5-year survival, median life expectancy, mortality rate, and validated prognostic models are unavailable. Infantile Leigh-spectrum disease is frequently severe and progressive; later-onset SDHA phenotypes can be milder but still disabling. Major morbidity includes developmental and cognitive impairment, movement disorder, epilepsy, weakness, optic atrophy, feeding/bulbar dysfunction, and possible respiratory or cardiac failure. (jackson2014mutationsinsdhd pages 1-2, renkema2015sdhamutationscausing pages 1-2)

Likely adverse prognostic features include very early onset, near-null biallelic variants, extremely low residual complex II activity, rapid regression, extensive brainstem disease, refractory epilepsy, respiratory failure, and cardiomyopathy. These are clinically plausible but have not been validated in a sufficiently large SDHA cohort. There is no established molecular prognostic biomarker.

## 12. Treatment

### Current standard

No FDA/EMA-approved or trial-proven SDHA-specific therapy exists. Treatment is supportive and should involve mitochondrial medicine/metabolic genetics, neurology, rehabilitation, nutrition, cardiology, ophthalmology, respiratory medicine, and palliative care as required.

- Treat seizures according to standard epilepsy guidelines, individualized to seizure type and organ function.
- Provide physical, occupational, speech, feeding, and visual rehabilitation.
- Use gastrostomy or respiratory support when clinically necessary.
- Treat dystonia, spasticity, pain, cardiomyopathy, arrhythmia, reflux, constipation, and endocrine abnormalities conventionally while considering mitochondrial safety.
- Develop an emergency plan to minimize fasting, dehydration, hypoglycemia, acidosis, fever, and prolonged catabolism.

### Seizure-specific expert guidance

A 2024 InterERN Delphi statement involved 24 experts from seven countries and two patient representatives. It endorsed standard NICE seizure/status pathways for primary mitochondrial disease, with genotype-specific exceptions. Levetiracetam, benzodiazepines, lamotrigine, lacosamide, carbamazepine, several other antiseizure medicines, vagus-nerve stimulation, and ketogenic diet were considered not generally contraindicated. Topiramate requires caution where renal tubular acidosis is a concern. Valproate is absolutely contraindicated in **POLG** disease and should be approached cautiously in mitochondrial liver disease; this is not an SDHA-specific absolute prohibition. New treatments should be monitored for adverse effects and blood lactate changes. (mancuso2024managementofseizures pages 2-4, mancuso2024managementofseizures pages 5-10, mancuso2024managementofseizures pages 4-5, mancuso2024managementofseizures pages 1-2)

### Vitamins, cofactors, and diets

Coenzyme Q10, riboflavin, thiamine, antioxidants, carnitine, and multicomponent “mitochondrial cocktails” are sometimes used empirically. No controlled SDHA-specific response rate is available. The ketogenic diet is not generally contraindicated in mitochondrial epilepsy, but efficacy in SDHA deficiency has not been established. Pharmacogenomic rules specific to SDHA are unavailable.

### Advanced and experimental therapies

No SDHA-targeted gene replacement, RNA therapy, gene editing, cell therapy, or approved small-molecule program was identified in clinical trials. Because SDHA is nuclear encoded, AAV or mRNA replacement is conceptually more tractable than mtDNA editing, but delivery to widespread brain, muscle, retina, and heart remains a major barrier. Chronic hypoxia is protective in an Sdhc conditional mouse but is investigational and potentially hazardous, not a clinical recommendation. (khazal2019aconditionalmouse pages 1-2)

Suggested MAXO terms include genetic counseling, molecular genetic testing, mitochondrial respiratory-chain enzyme assay, brain MRI, EEG, cardiac surveillance, ophthalmologic examination, physical therapy, occupational therapy, speech therapy, nutritional support, gastrostomy, noninvasive ventilation, antiseizure therapy, and palliative care.

## 13. Prevention

Primary prevention through lifestyle or vaccination is not possible because the disease is genetic. Effective reproductive prevention options include carrier testing for relatives, genetic counseling, prenatal diagnosis, and PGT-M once both familial variants are known. Each pregnancy of two carriers has a 25% recurrence risk.

Secondary prevention consists of early recognition in siblings or relatives, prompt genetic confirmation, baseline cardiac/ophthalmic/neurologic evaluation, and anticipatory management. Tertiary prevention focuses on avoiding prolonged fasting and catabolism, rapidly treating infection and seizures, optimizing nutrition, monitoring swallowing/respiration/cardiac function, and maintaining rehabilitation. Routine immunization is appropriate because infection can impose major metabolic stress; there is no disease-specific vaccine.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart specifically caused by biallelic **SDHA** variants was identified. Consequently, no breed-specific VBO term, veterinary incidence, or natural cross-species transmission applies. The mechanism is evolutionarily conserved across eukaryotes, but most comparative evidence comes from engineered models rather than natural disease. There is no zoonotic potential.

Relevant taxa for experimental comparison include *Saccharomyces cerevisiae* (NCBI Taxonomy 4932), *Drosophila melanogaster* (7227), *Caenorhabditis elegans* (6239), *Danio rerio* (7955), *Mus musculus* (10090), and *Homo sapiens* (9606).

## 15. Model organisms

### Cellular and biochemical models

Patient fibroblasts are the most directly relevant model. They reproduce reduced SDHA protein, complex II assembly/activity, succinate oxidation, and succinate-supported energy production. Lentiviral wild-type SDHA complementation partially restored activity, providing strong functional evidence. Limitations include glycolytic adaptation and failure to represent neurons, optic nerve, muscle, or brain architecture. (renkema2015sdhamutationscausing pages 4-5, renkema2015sdhamutationscausing pages 5-6)

Yeast models are useful for flavinylation, assembly, respiratory growth, ROS, metabolomics, and rapid VUS testing. Loss of the SDHAF4 ortholog reduced SDH activity by about 60%, increased succinate, depleted fumarate/malate, and elevated oxidative stress. Yeast lacks the human nervous system and therefore cannot model Leigh neuroanatomy. (vranken2014sdhaf4promotesmitochondrial pages 7-8, vranken2014sdhaf4promotesmitochondrial pages 1-2, takacsvellai2021modelsystemsin pages 11-12)

### Drosophila

Drosophila complex II assembly mutants develop paralysis, early-adult lethality, photoreceptor degeneration, and oxygen hypersensitivity. Under hyperoxia, one dSdhaf4 mutant survived approximately one day compared with nine days for controls. These models demonstrate conserved neuronal and muscular vulnerability, but they are not exact knock-ins of most human SDHA alleles. (vranken2014sdhaf4promotesmitochondrial pages 7-8, vranken2014sdhaf4promotesmitochondrial pages 6-7)

### Mouse

Inducible systemic **Sdhc** loss produces lactic acidosis and a lethal Leigh-like syndrome within four weeks. Chronic 10% oxygen substantially prolongs survival. This is a powerful whole-organism model of complex II failure and metabolic-environment interaction, but it disrupts SDHC rather than SDHA and uses abrupt systemic knockout rather than human hypomorphic biallelic alleles. (khazal2019aconditionalmouse pages 1-2)

### Other prospective models

Zebrafish, C. elegans, patient-derived iPSC neurons, cardiomyocytes, retinal cells, and brain organoids are suitable future platforms. In particular, isogenic CRISPR-corrected SDHA iPSC neurons/organoids could resolve cell-type-specific energy failure, developmental effects, and therapeutic response. No mature SDHA-specific single-cell or organoid dataset was identified.

## Recent developments and expert interpretation, 2023–2024

1. **Gene validity:** a 2023 international expert panel curated 113 Leigh-spectrum genes and included autosomal-recessive **SDHA**, supporting its clinical validity in the Leigh spectrum. The panel emphasized that accurate gene–disease definition enables medication decisions, multisystem surveillance, recurrence counseling, and trial eligibility. (mccormick2023expertpanelcuration pages 15-20)
2. **Diagnostics:** 2023 UK best-practice guidance formalized the transition from “biopsy first” to genome-wide testing and recommended simultaneous nuclear/mtDNA analysis where feasible. Its abstract states: **“Technological advances, particularly next-generation sequencing, have driven a shift in diagnostic practice from ‘biopsy first’ to genome-wide analyses of blood and/or urine DNA.”** Publication: European Journal of Human Genetics 31:148–163; online 13 December 2022, issue year 2023; DOI: https://doi.org/10.1038/s41431-022-01249-w. (mavraki2023genetictestingfor pages 2-3, mavraki2023genetictestingfor pages 1-2)
3. **Seizure management:** the 2024 InterERN consensus explicitly acknowledged that PMDs encompass more than 400 ultra-rare disorders and that controlled treatment trials are generally absent. It concluded that standard antiseizure therapies should not be unnecessarily withheld, while preserving POLG/valproate and other genotype-specific cautions. Publication accepted 28 February 2024; DOI: https://doi.org/10.1111/ene.16275. (mancuso2024managementofseizures pages 2-4, mancuso2024managementofseizures pages 4-5, mancuso2024managementofseizures pages 1-2)
4. **Disease-model trend:** a 2024 review highlights movement from yeast and invertebrates toward patient-derived iPSCs and organoids for Leigh syndrome. This is an enabling development, but an SDHA-specific human organoid program was not identified in the retrieved literature.
5. **Persistent gap:** no 2023–2024 natural-history cohort, randomized trial, validated biomarker study, or SDHA-specific therapeutic implementation was found. Recent advances are therefore predominantly in classification, genomic diagnosis, consensus management, and model methodology rather than disease-modifying treatment.

## Exact supporting quotations

- Renkema et al. describe the disease scope as **“SDHA mutations causing a multisystem mitochondrial disease”** and experimentally documented isolated complex II deficiency with genetic overlap with hereditary tumors. Publication: April 2015; DOI: https://doi.org/10.1038/ejhg.2014.80. (renkema2015sdhamutationscausing pages 1-2, renkema2015sdhamutationscausing pages 2-3)
- The 2023 diagnostic guideline states that primary mitochondrial disease is **“a diverse group of neuro-metabolic disorders characterised by impaired oxidative phosphorylation”** and reports that more than 350 nuclear and mitochondrial genes were then known. (mavraki2023genetictestingfor pages 1-2)
- The 2024 seizure consensus states: **“Epilepsy may be the presenting feature of PMD, can be difficult to treat and often represents a poor prognostic feature.”** (mancuso2024managementofseizures pages 1-2)
- The conditional mouse study reports a complex II-deficient condition **“reminiscent of Leigh-like syndrome that is lethal to mice within 4 wk”** and that chronic hypoxia provided substantial protection. Publication: August 2019; DOI: https://doi.org/10.1096/fj.201802655rr. (khazal2019aconditionalmouse pages 1-2)

## Evidence limitations

The evidence base is dominated by case reports, one small four-patient functional series, and mechanistic models. Variant lists are incomplete and historical; frequencies and classifications require current ClinVar/gnomAD verification. Most management recommendations are extrapolated from primary mitochondrial disease or Leigh syndrome rather than tested specifically in SDHA deficiency. Assertions about ROS, epigenetic remodeling, hypoxia, and succinate signaling are strongest in model systems or tumors and should be labeled accordingly. Disease-specific epidemiology, standardized phenotype frequencies, quality-of-life measures, survival, penetrance, genotype–phenotype models, omics, and treatment outcomes remain major unmet needs.

References

1. (renkema2015sdhamutationscausing pages 1-2): G Herma Renkema, Saskia B Wortmann, Roel J Smeets, Hanka Venselaar, Marion Antoine, Gepke Visser, Tawfeg Ben-Omran, Lambert P van den Heuvel, Henri J L M Timmers, Jan A Smeitink, and Richard J T Rodenburg. Sdha mutations causing a multisystem mitochondrial disease: novel mutations and genetic overlap with hereditary tumors. European Journal of Human Genetics, 23:202-209, Apr 2015. URL: https://doi.org/10.1038/ejhg.2014.80, doi:10.1038/ejhg.2014.80. This article has 119 citations and is from a domain leading peer-reviewed journal.

2. (jackson2014mutationsinsdhd pages 1-2): Christopher Jackson, Jean-Marc Nuoffer, Dagmar Karen Hahn, Holger Prokisch, Birgit Haberberger, Matthias Gautschi, Annemarie Haeberli, Sabina Gallati, and André Schaller. Mutations in sdhd lead to autosomal recessive encephalomyopathy and isolated mitochondrial complex ii deficiency. Journal of Medical Genetics, 51:170-175, Dec 2014. URL: https://doi.org/10.1136/jmedgenet-2013-101932, doi:10.1136/jmedgenet-2013-101932. This article has 117 citations and is from a domain leading peer-reviewed journal.

3. (renkema2015sdhamutationscausing pages 4-5): G Herma Renkema, Saskia B Wortmann, Roel J Smeets, Hanka Venselaar, Marion Antoine, Gepke Visser, Tawfeg Ben-Omran, Lambert P van den Heuvel, Henri J L M Timmers, Jan A Smeitink, and Richard J T Rodenburg. Sdha mutations causing a multisystem mitochondrial disease: novel mutations and genetic overlap with hereditary tumors. European Journal of Human Genetics, 23:202-209, Apr 2015. URL: https://doi.org/10.1038/ejhg.2014.80, doi:10.1038/ejhg.2014.80. This article has 119 citations and is from a domain leading peer-reviewed journal.

4. (renkema2015sdhamutationscausing pages 5-6): G Herma Renkema, Saskia B Wortmann, Roel J Smeets, Hanka Venselaar, Marion Antoine, Gepke Visser, Tawfeg Ben-Omran, Lambert P van den Heuvel, Henri J L M Timmers, Jan A Smeitink, and Richard J T Rodenburg. Sdha mutations causing a multisystem mitochondrial disease: novel mutations and genetic overlap with hereditary tumors. European Journal of Human Genetics, 23:202-209, Apr 2015. URL: https://doi.org/10.1038/ejhg.2014.80, doi:10.1038/ejhg.2014.80. This article has 119 citations and is from a domain leading peer-reviewed journal.

5. (vranken2014sdhaf4promotesmitochondrial pages 1-2): Jonathan G. Van Vranken, Daniel K. Bricker, Noah Dephoure, Steven P. Gygi, James E. Cox, Carl S. Thummel, and Jared Rutter. Sdhaf4 promotes mitochondrial succinate dehydrogenase activity and prevents neurodegeneration. Cell metabolism, 20 2:241-52, Aug 2014. URL: https://doi.org/10.1016/j.cmet.2014.05.012, doi:10.1016/j.cmet.2014.05.012. This article has 145 citations and is from a highest quality peer-reviewed journal.

6. (OpenTargets Search: mitochondrial complex II deficiency-SDHA): Open Targets Query (mitochondrial complex II deficiency-SDHA, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (renkema2015sdhamutationscausing pages 2-3): G Herma Renkema, Saskia B Wortmann, Roel J Smeets, Hanka Venselaar, Marion Antoine, Gepke Visser, Tawfeg Ben-Omran, Lambert P van den Heuvel, Henri J L M Timmers, Jan A Smeitink, and Richard J T Rodenburg. Sdha mutations causing a multisystem mitochondrial disease: novel mutations and genetic overlap with hereditary tumors. European Journal of Human Genetics, 23:202-209, Apr 2015. URL: https://doi.org/10.1038/ejhg.2014.80, doi:10.1038/ejhg.2014.80. This article has 119 citations and is from a domain leading peer-reviewed journal.

8. (mccormick2023expertpanelcuration pages 15-20): E. McCormick, Kierstin N. Keller, Julie Taylor, A. Coffey, Lishuang Shen, D. Krotoski, B. Harding, C. Alves, A. Ardissone, Renkui Bai, I.P. de Barcelos, E. Bertini, Krista K. Bluske, J. Christodoulou, Amanda R. Clause, W. Copeland, G. Diaz, D. Diodato, M. Dulik, G. Enns, A. Feigenbaum, C. Fratter, D. Ghezzi, A. Goldstein, A. Gropman, R. Haas, A. Karaa, M. Koenig, B. Monteleone, S. Parikh, B. P. Dueñas, Revathi Rajkumar, Ann Saada, R. Saneto, K. Sergeant, J. Shoffner, Conrad Smith, C. Stanley, Isabelle Thiffault, D. Thorburn, M. Walker, D. Wallace, L. Wong, Xiaowu Gai, Marni J. Falk, Z. Zolkipli-Cunningham, and S. Rahman. Expert panel curation of 113 primary mitochondrial disease genes for the leigh syndrome spectrum. Annals of Neurology, 94:696-712, Aug 2023. URL: https://doi.org/10.1002/ana.26716, doi:10.1002/ana.26716. This article has 68 citations and is from a highest quality peer-reviewed journal.

9. (renkema2015sdhamutationscausing pages 3-4): G Herma Renkema, Saskia B Wortmann, Roel J Smeets, Hanka Venselaar, Marion Antoine, Gepke Visser, Tawfeg Ben-Omran, Lambert P van den Heuvel, Henri J L M Timmers, Jan A Smeitink, and Richard J T Rodenburg. Sdha mutations causing a multisystem mitochondrial disease: novel mutations and genetic overlap with hereditary tumors. European Journal of Human Genetics, 23:202-209, Apr 2015. URL: https://doi.org/10.1038/ejhg.2014.80, doi:10.1038/ejhg.2014.80. This article has 119 citations and is from a domain leading peer-reviewed journal.

10. (ackrell2002cytopathiesinvolvingmitochondrial pages 1-3): Brian A.C Ackrell. Cytopathies involving mitochondrial complex ii. Molecular aspects of medicine, 23 5:369-84, Oct 2002. URL: https://doi.org/10.1016/s0098-2997(02)00012-2, doi:10.1016/s0098-2997(02)00012-2. This article has 122 citations and is from a highest quality peer-reviewed journal.

11. (vranken2014sdhaf4promotesmitochondrial pages 7-8): Jonathan G. Van Vranken, Daniel K. Bricker, Noah Dephoure, Steven P. Gygi, James E. Cox, Carl S. Thummel, and Jared Rutter. Sdhaf4 promotes mitochondrial succinate dehydrogenase activity and prevents neurodegeneration. Cell metabolism, 20 2:241-52, Aug 2014. URL: https://doi.org/10.1016/j.cmet.2014.05.012, doi:10.1016/j.cmet.2014.05.012. This article has 145 citations and is from a highest quality peer-reviewed journal.

12. (mavraki2023genetictestingfor pages 2-3): Eleni Mavraki, Robyn Labrum, Kate Sergeant, Charlotte L. Alston, Cathy Woodward, Conrad Smith, Charlotte V. Y. Knowles, Yogen Patel, Philip Hodsdon, Jack P. Baines, Emma L. Blakely, James Polke, Robert W. Taylor, and Carl Fratter. Genetic testing for mitochondrial disease: the united kingdom best practice guidelines. European Journal of Human Genetics, 31:148-163, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01249-w, doi:10.1038/s41431-022-01249-w. This article has 88 citations and is from a domain leading peer-reviewed journal.

13. (mavraki2023genetictestingfor pages 1-2): Eleni Mavraki, Robyn Labrum, Kate Sergeant, Charlotte L. Alston, Cathy Woodward, Conrad Smith, Charlotte V. Y. Knowles, Yogen Patel, Philip Hodsdon, Jack P. Baines, Emma L. Blakely, James Polke, Robert W. Taylor, and Carl Fratter. Genetic testing for mitochondrial disease: the united kingdom best practice guidelines. European Journal of Human Genetics, 31:148-163, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01249-w, doi:10.1038/s41431-022-01249-w. This article has 88 citations and is from a domain leading peer-reviewed journal.

14. (mavraki2023genetictestingfor pages 3-4): Eleni Mavraki, Robyn Labrum, Kate Sergeant, Charlotte L. Alston, Cathy Woodward, Conrad Smith, Charlotte V. Y. Knowles, Yogen Patel, Philip Hodsdon, Jack P. Baines, Emma L. Blakely, James Polke, Robert W. Taylor, and Carl Fratter. Genetic testing for mitochondrial disease: the united kingdom best practice guidelines. European Journal of Human Genetics, 31:148-163, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01249-w, doi:10.1038/s41431-022-01249-w. This article has 88 citations and is from a domain leading peer-reviewed journal.

15. (mancuso2024managementofseizures pages 4-5): Michelangelo Mancuso, Maria T. Papadopoulou, Yi Shiau Ng, Anna Ardissone, Marcello Bellusci, Enrico Bertini, Lidia Di Vito, Teresinha Evangelista, Carmen Fons, Omar Hikmat, Rita Horvath, Thomas Klopstock, Cornelia Kornblum, Costanza Lamperti, Laura Licchetta, Maria Judit Molnar, Kristin N. Varhaug, Mar O'Callaghan, Ronit M. Pressler, Manuel Schiff, Serenella Servidei, Nora Szabo, Gráinne S. Gorman, J Helen Cross, and Shamima Rahman. Management of seizures in patients with primary mitochondrial diseases: consensus statement from the intererns mitochondrial working group. European Journal of Neurology, Apr 2024. URL: https://doi.org/10.1111/ene.16275, doi:10.1111/ene.16275. This article has 18 citations and is from a domain leading peer-reviewed journal.

16. (mancuso2024managementofseizures pages 1-2): Michelangelo Mancuso, Maria T. Papadopoulou, Yi Shiau Ng, Anna Ardissone, Marcello Bellusci, Enrico Bertini, Lidia Di Vito, Teresinha Evangelista, Carmen Fons, Omar Hikmat, Rita Horvath, Thomas Klopstock, Cornelia Kornblum, Costanza Lamperti, Laura Licchetta, Maria Judit Molnar, Kristin N. Varhaug, Mar O'Callaghan, Ronit M. Pressler, Manuel Schiff, Serenella Servidei, Nora Szabo, Gráinne S. Gorman, J Helen Cross, and Shamima Rahman. Management of seizures in patients with primary mitochondrial diseases: consensus statement from the intererns mitochondrial working group. European Journal of Neurology, Apr 2024. URL: https://doi.org/10.1111/ene.16275, doi:10.1111/ene.16275. This article has 18 citations and is from a domain leading peer-reviewed journal.

17. (khazal2019aconditionalmouse pages 1-2): Fatimah Al Khazal, Molly Nelson Holte, Brad Bolon, Thomas A. White, Nathan LeBrasseur, and L. James Maher III. A conditional mouse model of complex ii deficiency manifesting as leigh‐like syndrome. The FASEB Journal, 33(12):13189-13201, Aug 2019. URL: https://doi.org/10.1096/fj.201802655rr, doi:10.1096/fj.201802655rr. This article has 30 citations.

18. (takacsvellai2021modelsystemsin pages 11-12): Krisztina Takács-Vellai, Zsolt Farkas, Fanni Ősz, and Gordon W. Stewart. Model systems in sdhx-related pheochromocytoma/paraganglioma. Cancer Metastasis Reviews, 40:1177-1201, Dec 2021. URL: https://doi.org/10.1007/s10555-021-10009-z, doi:10.1007/s10555-021-10009-z. This article has 14 citations.

19. (vranken2014sdhaf4promotesmitochondrial pages 6-7): Jonathan G. Van Vranken, Daniel K. Bricker, Noah Dephoure, Steven P. Gygi, James E. Cox, Carl S. Thummel, and Jared Rutter. Sdhaf4 promotes mitochondrial succinate dehydrogenase activity and prevents neurodegeneration. Cell metabolism, 20 2:241-52, Aug 2014. URL: https://doi.org/10.1016/j.cmet.2014.05.012, doi:10.1016/j.cmet.2014.05.012. This article has 145 citations and is from a highest quality peer-reviewed journal.

20. (mancuso2024managementofseizures pages 2-4): Michelangelo Mancuso, Maria T. Papadopoulou, Yi Shiau Ng, Anna Ardissone, Marcello Bellusci, Enrico Bertini, Lidia Di Vito, Teresinha Evangelista, Carmen Fons, Omar Hikmat, Rita Horvath, Thomas Klopstock, Cornelia Kornblum, Costanza Lamperti, Laura Licchetta, Maria Judit Molnar, Kristin N. Varhaug, Mar O'Callaghan, Ronit M. Pressler, Manuel Schiff, Serenella Servidei, Nora Szabo, Gráinne S. Gorman, J Helen Cross, and Shamima Rahman. Management of seizures in patients with primary mitochondrial diseases: consensus statement from the intererns mitochondrial working group. European Journal of Neurology, Apr 2024. URL: https://doi.org/10.1111/ene.16275, doi:10.1111/ene.16275. This article has 18 citations and is from a domain leading peer-reviewed journal.

21. (mancuso2024managementofseizures pages 5-10): Michelangelo Mancuso, Maria T. Papadopoulou, Yi Shiau Ng, Anna Ardissone, Marcello Bellusci, Enrico Bertini, Lidia Di Vito, Teresinha Evangelista, Carmen Fons, Omar Hikmat, Rita Horvath, Thomas Klopstock, Cornelia Kornblum, Costanza Lamperti, Laura Licchetta, Maria Judit Molnar, Kristin N. Varhaug, Mar O'Callaghan, Ronit M. Pressler, Manuel Schiff, Serenella Servidei, Nora Szabo, Gráinne S. Gorman, J Helen Cross, and Shamima Rahman. Management of seizures in patients with primary mitochondrial diseases: consensus statement from the intererns mitochondrial working group. European Journal of Neurology, Apr 2024. URL: https://doi.org/10.1111/ene.16275, doi:10.1111/ene.16275. This article has 18 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_II_Deficiency_Nuclear_Type_1-deep-research-falcon_artifacts/artifact-00.md)