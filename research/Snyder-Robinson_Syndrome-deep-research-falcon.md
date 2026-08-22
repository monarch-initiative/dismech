---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T01:23:59.787438'
end_time: '2026-07-31T01:34:46.299211'
duration_seconds: 646.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Snyder-Robinson Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Snyder-Robinson_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Snyder-Robinson Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Snyder-Robinson Syndrome** covering all of the
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
- **Disease Name:** Snyder-Robinson Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Snyder-Robinson Syndrome** covering all of the
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


# Snyder–Robinson Syndrome: Disease Characteristics Research Report

## Executive summary and evidence scope

Snyder–Robinson syndrome (SRS) is an ultra-rare, X-linked recessive, multisystem neurodevelopmental and skeletal disorder caused by loss-of-function variants in **SMS**, which encodes spermine synthase. The defining biochemical lesion is reduced conversion of spermidine to spermine, producing low spermine, excess spermidine, and an elevated spermidine:spermine ratio. The strongest human evidence concerns developmental disability, hypotonia, seizures, thin habitus, osteoporosis, fractures, and kyphoscoliosis. Mechanistic evidence additionally implicates excessive spermidine catabolism, reactive oxygen species and aldehydes, lysosomal/autophagic failure, mitochondrial dysfunction, and defective bone mineralization. Most evidence comes from fewer than 30 historically reported individuals, patient-derived cells, and Drosophila or mouse models; therefore frequencies, natural history, prognosis, and treatment effects remain imprecise. No disease-modifying therapy has established human efficacy (dontaine2021digestiveinvolvementin pages 1-7, albert2015impairedosteoblastand pages 1-2, li2017sperminesynthasedeficiency pages 1-2, akinyele2024impairedpolyaminemetabolism pages 1-3).

The following compact curation table summarizes the principal evidence and proposed ontology mappings. Ontology terms labeled “suggested” should be checked against the current ontology release before database ingestion.

| Domain | Key evidence | Suggested ontology terms/IDs | Evidence type / maturity |
|---|---|---|---|
| Disease identifiers | Snyder-Robinson syndrome is an ultra-rare X-linked syndromic intellectual disability caused by SMS deficiency; disease mappings in retrieved sources include MONDO:0010664, OMIM:309583, Orphanet:3063. Open Targets links MONDO_0010664 / Orphanet_3063 to SMS (dontaine2021digestiveinvolvementin pages 1-7, mouskou2021novelhemizygousmissense pages 1-2, OpenTargets Search: Snyder-Robinson syndrome-SMS) | **Exact IDs:** MONDO:0010664; OMIM:309583; Orphanet:3063. **Term suggestion requiring validation:** “Syndromic X-linked intellectual disability, Snyder type” | Aggregated disease resource + human clinical reports; high confidence for identifiers |
| Causal gene / inheritance | Causal gene is **SMS** (spermine synthase), X-linked recessive; reported disease-causing variants include missense and nonsense changes, with inherited, de novo, and reported maternal mosaic transmission in the broader literature; examples in retrieved evidence include p.Gln148Arg, p.Gly203Asp, p.Pro112Ala, p.Ser302Leu (dontaine2021digestiveinvolvementin pages 11-16, albert2015impairedosteoblastand pages 1-2, mouskou2021novelhemizygousmissense pages 1-2, qazi2020wholeexomesequencingidentifies pages 1-3, li2017sperminesynthasedeficiency pages 1-2) | **Exact gene symbol:** SMS. **Term suggestions requiring validation:** HP:0001417 X-linked inheritance; SO terms such as missense_variant, nonsense_variant, splice_region_variant | Human genetic evidence; high confidence for SMS causality, moderate for complete variant spectrum |
| Core biochemical mechanism | SMS catalyzes spermidine → spermine; loss of function lowers spermine and raises spermidine, producing an increased spermidine/spermine ratio, the core biochemical hallmark of SRS (dontaine2021digestiveinvolvementin pages 1-7, qazi2020wholeexomesequencingidentifies pages 1-3, li2017sperminesynthasedeficiency pages 1-2, akinyele2024impairedpolyaminemetabolism pages 1-3) | **Exact/near-exact suggestions:** GO:0006598 polyamine biosynthetic process; CHEBI:15746 spermidine; CHEBI:15729 spermine. **Term suggestion requiring validation:** “increased spermidine to spermine ratio” | Human cells + animal models; high confidence |
| Downstream pathophysiology | Evidence supports a causal chain from polyamine imbalance to excessive spermidine catabolism, toxic aldehydes/ROS, lysosomal dysfunction, impaired autophagy-lysosome flux, mitochondrial dysfunction, acetyl-CoA depletion, altered protein acetylation, and tissue injury affecting brain and bone (li2017sperminesynthasedeficiency pages 1-2, tao2022phenylbutyratemodulatespolyamine pages 1-2, tao2022phenylbutyratemodulatespolyamine pages 2-4) | **Exact/near-exact GO suggestions:** GO:0006979 response to oxidative stress; GO:0000422 autophagy of mitochondrion/mitophagy (validate fit); GO:0005773 vacuole/lysosomal compartment term suggestion; GO:0005739 mitochondrion; GO:0007015 actin filament organization term suggestion if needed. **All mechanistic ontology mappings should be validated** | Primary mechanistic evidence from Drosophila, patient fibroblasts, and supportive review; moderate-high confidence |
| Neurologic phenotype | Common neurologic features include developmental delay/intellectual disability, hypotonia, seizures/epilepsy, speech impairment, gait abnormalities, learning impairment, anxiety-like behavior and reduced brain volumes in mouse models (dontaine2021digestiveinvolvementin pages 1-7, mouskou2021novelhemizygousmissense pages 1-2, qazi2020wholeexomesequencingidentifies pages 1-3, akinyele2024impairedpolyaminemetabolism pages 1-3) | **Exact HPO suggestions:** HP:0001249 Intellectual disability; HP:0001252 Hypotonia; HP:0001250 Seizure; HP:0001263 Global developmental delay; HP:0000750 Delayed speech and language development; HP:0001288 Gait disturbance. **Model-only anatomy suggestions requiring validation:** reduced total brain volume | Human clinical + mouse model; high confidence for core human neurologic features |
| Skeletal phenotype | Characteristic skeletal disease includes low bone density/osteoporosis, atraumatic or low-energy fractures, kyphosis/kyphoscoliosis, thin cortex, low bone volume, absent trabecular meshwork, severe mineralization defect, and reduced osteoblast/osteoclast function (mouskou2021novelhemizygousmissense pages 4-5, albert2015impairedosteoblastand pages 1-2) | **Exact/near-exact HPO suggestions:** HP:0000939 Osteoporosis; HP:0002757 Pathological fracture; HP:0002650 Scoliosis; HP:0002808 Kyphosis. **Process/cell suggestions requiring validation:** osteoblast differentiation defect, osteoclast defect | Human clinical + bone histopathology; high confidence |
| Additional/expanded phenotype | Reported additional manifestations include asthenic/thin habitus, facial dysmorphism, long fingers/toes, genital/renal anomalies, respiratory infections, retinal changes, and possible digestive involvement such as jejunal stenosis, feeding intolerance, cholestasis, pancreatic exocrine insufficiency, and failure to thrive in severe cases (dontaine2021digestiveinvolvementin pages 1-7, dontaine2021digestiveinvolvementin pages 11-16, albert2015impairedosteoblastand pages 1-2, mouskou2021novelhemizygousmissense pages 1-2, dontaine2021digestiveinvolvementin pages 16-21) | **Exact/near-exact HPO suggestions:** HP:0001508 Failure to thrive; HP:0001511 Intrauterine growth restriction/poor growth term suggestions; HP:0001166 Arachnodactyly term suggestion; HP:0002242 Feeding difficulties; HP:0001394 Cholestasis. **All require phenotype-level validation** | Human case reports/series; moderate confidence for expanded GI phenotype |
| Diagnostic biomarkers / tests | Diagnosis can be made by identifying a pathogenic SMS variant and/or showing decreased or absent spermine synthase activity with elevated spermidine/spermine ratio. One severe report provided markedly abnormal erythrocyte polyamines: spermidine >50 nmoles/8×10^9 erythrocytes (norm 5–11) and spermine 2.58 (norm 3.5–8.5). WES/Sanger are established; DXA/radiography are used for bone disease (dontaine2021digestiveinvolvementin pages 1-7, dontaine2021digestiveinvolvementin pages 11-16, mouskou2021novelhemizygousmissense pages 4-5, mouskou2021novelhemizygousmissense pages 1-2, qazi2020wholeexomesequencingidentifies pages 1-3) | **Exact/near-exact suggestions:** biomarker = elevated spermidine:spermine ratio; assay = SMS enzymatic activity test; genetic test = WES / Sanger confirmation. **LOINC/MAXO/other codes require validation** | Human diagnostic evidence; high confidence |
| Supportive care | Current management is mainly supportive: antiepileptic drugs for seizures, calcium/vitamin D with caution because of ectopic calcification concerns, orthopedic surveillance, nutritional/feeding support, and multidisciplinary genetic care. No disease-modifying standard therapy is established (mouskou2021novelhemizygousmissense pages 4-5, dontaine2021digestiveinvolvementin pages 16-21, tao2022phenylbutyratemodulatespolyamine pages 1-2) | **MAXO term suggestions requiring validation:** antiseizure medication therapy; calcium supplementation; vitamin D supplementation; orthopedic monitoring; enteral feeding support; genetic counseling | Human clinical practice from case literature; moderate confidence |
| Experimental therapy: phenylbutyrate (PBA) | PBA improved SRS-related phenotypes in Drosophila and patient fibroblasts by downregulating SAT1, reducing toxic catabolites, restoring acetyl-CoA/protein acetylation, improving mitochondrial and autolysosomal function, and extending fly lifespan. In flies, 2 mM showed benefit, whereas 10 mM was toxic; glycerol-PBA also showed benefit at 0.6 mM (tao2022phenylbutyratemodulatespolyamine pages 1-2, tao2022phenylbutyratemodulatespolyamine pages 2-4) | **CHEBI / drug suggestion requiring validation:** phenylbutyrate. **MAXO suggestions requiring validation:** experimental small-molecule therapy; metabolite-modulating therapy | Preclinical only (patient cells + fly); moderate confidence, not yet human efficacy |
| Experimental therapy: DFMO | A 2023 EMBO Molecular Medicine study is cited in later reviews as showing DFMO can rebalance aberrant polyamine ratios in SRS, but primary quantitative details were not retrievable in the current tool outputs; therefore translational promise is noted without overclaiming clinical efficacy (wu2024structuralinsightsinto pages 11-12) | **Drug suggestion requiring validation:** difluoromethylornithine / eflornithine. **MAXO suggestion requiring validation:** polyamine-pathway inhibition therapy | Secondary/review-level evidence in current retrieval; low-moderate confidence until primary paper details are confirmed |
| Other experimental approaches | Additional exploratory strategies cited in reviews include direct spermine supplementation, polyamine analogs such as (R,R)-1,12-dimethylspermine, antioxidants/ROS scavengers, and redox-sensitive spermine prodrugs; benefits are partial or preclinical only (tao2022phenylbutyratemodulatespolyamine pages 1-2, wu2024structuralinsightsinto pages 11-12, akinyele2024impairedpolyaminemetabolism pages 21-24) | **CHEBI/MAXO suggestions requiring validation:** spermine supplementation; antioxidant therapy; polyamine analog therapy; prodrug therapy | Preclinical / review-supported; low-moderate confidence |
| Model organisms | **Drosophila dSms loss** recapitulates polyamine imbalance, shortened lifespan, locomotor defects, retinal/synaptic degeneration, oxidative stress, lysosomal and mitochondrial dysfunction. **G56S mouse** shows failure to thrive, short stature, reduced bone density, impaired learning, anxiety-like behavior, reduced mobility, heightened fear responses, reduced brain volumes, and impaired mitochondrial oxidative phosphorylation (li2017sperminesynthasedeficiency pages 1-2, akinyele2024impairedpolyaminemetabolism pages 1-3) | **Exact/near-exact suggestions:** Drosophila melanogaster model; Mus musculus G56S Sms model. **Ontology suggestions requiring validation:** model recapitulates HP:0001249, HP:0001252, HP:0000939; CL terms for neurons, osteoblasts, osteoclasts, fibroblasts | Strong preclinical evidence; high value for mechanism and therapeutic testing |
| Evidence gaps / curation notes | Prevalence, penetrance, founder effects, standardized diagnostic criteria, and long-term prognosis remain poorly quantified because very few families have been reported. Several ontology mappings above are term suggestions and should be validated against HPO/GO/CL/MAXO/LOINC before database ingestion (dontaine2021digestiveinvolvementin pages 1-7, qazi2020wholeexomesequencingidentifies pages 1-3, wu2024structuralinsightsinto pages 11-12) | **Curation note:** retain exact IDs only for MONDO:0010664, OMIM:309583, Orphanet:3063, SMS, and high-confidence HPO terms; validate all others | Evidence-synthesis note; high confidence for gap statement |


*Table: This table summarizes high-yield evidence and ontology mappings for Snyder-Robinson syndrome across identifiers, mechanism, phenotype, diagnostics, treatment, and models. It is designed as a compact curation aid and flags which ontology terms are exact versus suggestions needing validation.*

## 1. Disease information

### Definition and classification

SRS is a Mendelian polyaminopathy and syndromic X-linked intellectual-developmental disorder. It is sometimes described as the first recognized inherited disorder of the polyamine pathway or “spermine synthase deficiency syndrome.” Its phenotype combines neurodevelopmental impairment with skeletal fragility, hypotonia, asthenic habitus, dysmorphism, speech and gait abnormalities, and variably epilepsy and visceral involvement (mouskou2021novelhemizygousmissense pages 1-2, dontaine2021digestiveinvolvementin pages 16-21, li2017sperminesynthasedeficiency pages 1-2).

### Identifiers and synonyms

- **MONDO:** MONDO:0010664, *syndromic X-linked intellectual disability, Snyder type*.
- **OMIM phenotype:** **309583**, generally indexed as Snyder–Robinson syndrome/X-linked syndromic intellectual disability, Snyder type.
- **Orphanet:** **ORPHA:3063**, X-linked intellectual disability, Snyder type.
- **Causal gene:** **SMS**, Ensembl ENSG00000102172; the retrieved literature gives SMS gene records as MIM *300105 in one source and *300015 in another, so the current OMIM gene record should be checked directly before ingestion.
- **Synonyms:** Snyder–Robinson syndrome; SRS; spermine synthase deficiency syndrome; X-linked intellectual disability, Snyder type; syndromic X-linked intellectual disability, Snyder type; MRXSSR (dontaine2021digestiveinvolvementin pages 1-7, mouskou2021novelhemizygousmissense pages 1-2, qazi2020wholeexomesequencingidentifies pages 1-3, OpenTargets Search: Snyder-Robinson syndrome-SMS).

No dedicated ICD-10-CM code, ICD-11 entity, or MeSH descriptor was established in the retrieved evidence. Operational coding will generally require a broader intellectual-disability, congenital-malformation, epilepsy, or osteoporosis code, supplemented by the molecular diagnosis.

### Evidence provenance

The knowledge summarized here is primarily **aggregated disease-level evidence** derived from published pedigrees, individual case reports, small case series, cell studies, and model organisms—not population-scale EHR data. Examples include three affected members of one Pakistani family, two severely affected maternal half-brothers, two brothers studied through detailed bone histology, and isolated de novo cases (dontaine2021digestiveinvolvementin pages 11-16, albert2015impairedosteoblastand pages 1-2, qazi2020wholeexomesequencingidentifies pages 1-3).

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The necessary initiating lesion is a **germline hemizygous pathogenic variant in SMS** in an affected male. SMS catalyzes the terminal polyamine-biosynthetic reaction, spermidine to spermine. Reduced or absent activity produces a high spermidine:spermine ratio and initiates downstream cellular toxicity (li2017sperminesynthasedeficiency pages 1-2, akinyele2024impairedpolyaminemetabolism pages 1-3).

### Genetic risk factors

Documented variant classes include missense, nonsense, splice-altering, and other loss-of-function alleles. Retrieved examples are **c.334C>G (p.Pro112Ala)**, de novo; **c.443A>G (p.Gln148Arg)**, affecting the 5′-methylthioadenosine-binding region; **c.608G>A (p.Gly203Asp)**; and **c.905C>T (p.Ser302Leu)** in three related Pakistani males (dontaine2021digestiveinvolvementin pages 11-16, mouskou2021novelhemizygousmissense pages 1-2, qazi2020wholeexomesequencingidentifies pages 1-3, li2017sperminesynthasedeficiency pages 1-2).

Female heterozygosity confers reproductive risk; expression in females may depend on X-inactivation, but penetrance and frequency of symptomatic carriers are insufficiently defined. Most familial cases involve carrier mothers, while de novo cases occur—two of 20 published cases in one 2021 review. Maternal mosaic transmission has also been reported in the literature, making parental testing and consideration of mosaicism important even when a variant appears de novo (mouskou2021novelhemizygousmissense pages 4-5).

No validated modifier gene, susceptibility locus, founder allele, protective allele, or robust genotype–phenotype relationship has been established. Marked intrafamilial variability argues that residual enzyme activity, X-inactivation in females, background genetic variation, and non-genetic factors may modify expression, but these remain hypotheses (dontaine2021digestiveinvolvementin pages 11-16).

### Environmental and protective factors

No toxin, infection, diet, occupation, smoking, alcohol, or lifestyle exposure is known to cause SRS. Likewise, no environmental factor has been shown to prevent occurrence in a genetically affected male. Avoidance of falls and bone trauma, adequate—but carefully monitored—calcium/vitamin D, good nutrition, and infection prevention may reduce complications rather than disease penetrance (mouskou2021novelhemizygousmissense pages 4-5).

A formal gene–environment interaction has not been demonstrated. Oxidative load, nutritional status, immobility, antiseizure medications, and mechanical loading could plausibly alter skeletal or neurologic severity, but this has not been quantified in SRS cohorts.

## 3. Phenotypes

### Core neurologic and developmental phenotype

- **Global developmental delay/intellectual disability**—usually evident in infancy or childhood; moderate-to-severe impairment is typical, with major effects on communication, education, independence, and activities of daily living. Suggested HPO: **HP:0001263**, **HP:0001249**.
- **Hypotonia/low muscle mass**—early and common, contributing to delayed motor milestones, poor mobility, falls, and asthenic habitus. HPO: **HP:0001252**, with muscular hypoplasia as an additional term.
- **Speech impairment**—dysarthric, markedly delayed, or absent speech. Suggested HPO: **HP:0000750** and dysarthria.
- **Gait disturbance/motor impairment**—unsteady gait and difficulty ambulating may evolve through childhood. HPO: **HP:0001288**.
- **Epilepsy/seizures**—often begins in early childhood; one synthesis reported seizures in up to **67%** of cases, with variable type, frequency, and severity. HPO: **HP:0001250**. Epileptic encephalopathy has occurred in severe cases (dontaine2021digestiveinvolvementin pages 11-16, mouskou2021novelhemizygousmissense pages 4-5, mouskou2021novelhemizygousmissense pages 1-2).

### Skeletal, growth, and connective-tissue manifestations

- **Low bone density/osteoporosis** commonly develops during the first decade and particularly affects long bones. HPO: **HP:0000939**.
- **Pathologic or low-energy fractures** substantially impair mobility and quality of life. Suggested HPO: **HP:0002757**.
- **Kyphosis, scoliosis, or kyphoscoliosis**, joint contractures, long fingers/toes, and thin habitus are characteristic. Suggested HPO: **HP:0002808**, **HP:0002650**, arachnodactyly.
- Histomorphometry in two brothers showed profound osteoblast and osteoclast depletion, absent trabecular meshwork, thin cortex, and low bone volume; patient-derived marrow stromal cells had severely deficient calcium-phosphate mineralization (albert2015impairedosteoblastand pages 1-2).

A 2021 review suggested osteoporosis and fracture burden may remain approximately stable after reaching diagnostic severity rather than invariably worsening, but this conclusion rests on very small numbers and should not be encoded as a universal course (mouskou2021novelhemizygousmissense pages 4-5).

### Dysmorphic and multisystem findings

Reported craniofacial features include a long, thin, sometimes asymmetric face, prominent lower lip, high or abnormal palate, and other nonspecific dysmorphism. Additional variably reported findings include cryptorchidism or other genital anomalies, renal cysts/nephrocalcinosis, recurrent respiratory infections, tracheomalacia, hearing loss, retinal pigmentary changes, corpus-callosum abnormalities, cerebral atrophy, and fluctuating hyper-/hypoglycemia (dontaine2021digestiveinvolvementin pages 11-16, albert2015impairedosteoblastand pages 1-2, mouskou2021novelhemizygousmissense pages 1-2).

Severe gastrointestinal/hepatopancreatic disease—jejunal or jejunoduodenal stenosis, feeding intolerance, failure to thrive, cholestasis, hepatic fibrosis, and exocrine pancreatic insufficiency—was reported in two maternal half-brothers. These should presently be curated as **possible expanded/rare phenotypes**, not obligatory features. Suggested HPO includes feeding difficulty, **HP:0001508** failure to thrive, cholestasis, intestinal stenosis, and exocrine pancreatic insufficiency (dontaine2021digestiveinvolvementin pages 1-7, dontaine2021digestiveinvolvementin pages 11-16, dontaine2021digestiveinvolvementin pages 16-21).

### Frequency and quality-of-life evidence

Reliable percentages are unavailable for most features because the literature historically comprised approximately 20 individuals in about 10 families and fewer than 30 total reported patients by 2021. No SRS-specific EQ-5D, SF-36, PROMIS, or validated caregiver-burden dataset was retrieved. Nevertheless, recurrent fractures, severe developmental disability, epilepsy, feeding dependence, and impaired ambulation clearly impose substantial functional and caregiver burden (dontaine2021digestiveinvolvementin pages 1-7, albert2015impairedosteoblastand pages 1-2, qazi2020wholeexomesequencingidentifies pages 1-3).

## 4. Genetic and molecular information

**SMS** is located at **Xp22.11** and encodes spermine synthase. Pathogenic disease alleles are germline; SRS is not a somatic neoplasm. Functional consequence is loss or marked reduction of enzyme activity rather than gain of function or dominant negativity (mouskou2021novelhemizygousmissense pages 1-2, li2017sperminesynthasedeficiency pages 1-2).

Variant interpretation should follow ACMG/AMP criteria using segregation, de novo status, population frequency, computational/structural evidence, enzyme activity, and the polyamine ratio. The p.Pro112Ala and p.Ser302Leu reports illustrate WES discovery followed by Sanger confirmation and in-silico structural analysis. Current ClinVar classifications and gnomAD allele counts must be queried variant-by-variant; exact population frequencies were not available in the retrieved full texts and should not be inferred as zero (mouskou2021novelhemizygousmissense pages 1-2, qazi2020wholeexomesequencingidentifies pages 1-3).

No recurrent chromosomal rearrangement, aneuploidy, repeat expansion, mitochondrial-DNA lesion, validated epigenetic episignature, or established modifier gene is known. Copy-number variants disrupting SMS are biologically plausible and should be detectable by genome sequencing or copy-number analysis, but they were not a major documented class in the retrieved cohort.

## 5. Environmental information

SRS is not caused by pollution, radiation, occupational exposure, lifestyle behavior, or an infectious agent. There is no zoonotic or transmissible component. Environmental management is relevant only to complications: fall prevention, weight-bearing activity within orthopedic safety limits, adequate nutrition, aspiration/infection precautions, and avoidance of excessive supplementation or medications that worsen bone health.

## 6. Mechanism and pathophysiology

### Upstream biochemical defect

The causal chain begins with **SMS loss of function → reduced spermine synthesis → spermine deficiency plus spermidine accumulation → elevated spermidine:spermine ratio**. In patient lymphoblasts, secondary changes include reduced ornithine decarboxylase activity and putrescine, showing that the lesion perturbs broader polyamine homeostasis rather than a single metabolite (li2017sperminesynthasedeficiency pages 1-2).

A representative diagnostic measurement in severe disease found erythrocyte spermidine **>50 nmol/8×10⁹ erythrocytes** (reference 5–11) and spermine **2.58** (reference 3.5–8.5), demonstrating the magnitude of imbalance in at least one individual (dontaine2021digestiveinvolvementin pages 11-16).

### Downstream organelle and metabolic injury

Human cells and Drosophila support the following sequence:

1. Excess spermidine enters catabolism.
2. Catabolism generates reactive oxygen species and toxic aldehyde metabolites.
3. Oxidative injury disrupts lysosomes and autophagy–lysosome flux.
4. Mitochondrial function and oxidative phosphorylation decline.
5. Cellular survival, synaptic maintenance, and tissue homeostasis fail (li2017sperminesynthasedeficiency pages 1-2).

The 2022 phenylbutyrate study added **SAT1 activation, acetyl-CoA depletion, and altered global protein acetylation** to this model. Phenylbutyrate or its phenylacetyl-CoA metabolite downregulated SAT1 and restored aspects of acetyl-CoA/protein acetylation, linking polyamine catabolism to central carbon metabolism (tao2022phenylbutyratemodulatespolyamine pages 1-2, tao2022phenylbutyratemodulatespolyamine pages 2-4).

Suggested GO annotations include polyamine biosynthetic process; spermidine metabolic process; spermine biosynthetic process; response to oxidative stress (**GO:0006979**); autophagy; lysosomal organization/function; mitochondrial respiratory chain/oxidative phosphorylation; and bone mineralization. Suggested cellular components are cytosol, lysosome, autolysosome, mitochondrion (**GO:0005739**), and synapse. Suggested cell types include neuron, retinal neuron/photoreceptor, osteoblast, osteoclast, bone-marrow stromal cell, fibroblast, and lymphoblast; exact CL identifiers should be validated.

### Neural and skeletal tissue specificity

Drosophila loss of dSms causes synaptic and retinal degeneration, locomotor deficits, and reduced survival. The 2024 G56S mouse exhibits reduced whole and regional brain volumes, impaired learning, anxiety-like behavior, reduced mobility, heightened fear responses, and defective cortical mitochondrial oxidative phosphorylation. These model findings plausibly connect cellular bioenergetic injury to human intellectual disability and movement impairment, but mouse behavioral phenotypes are not direct human symptoms (li2017sperminesynthasedeficiency pages 1-2, akinyele2024impairedpolyaminemetabolism pages 1-3).

Bone appears unusually sensitive to polyamine imbalance. Patient osteoblast-lineage cells showed much larger spermine/spermidine disturbances than fibroblasts, deficient mineral deposition, and reduced osteoblast and osteoclast populations. This supports cell-type-specific metabolic vulnerability rather than a collagen-structural defect (albert2015impairedosteoblastand pages 1-2).

### Molecular profiling and advanced technologies

Established profiling includes targeted polyamine metabolomics in erythrocytes and cultured cells, metabolic phenotyping, mitochondrial assays, protein-acetylation analysis, and anatomical MRI/volumetry in mice. **N8-acetylspermidine** has been proposed as a plasma biomarker, but clinical sensitivity and specificity are unvalidated (dontaine2021digestiveinvolvementin pages 16-21).

No replicated SRS-specific single-cell atlas, spatial transcriptomic dataset, human tissue-wide transcriptome/proteome, lipidomic signature, CRISPR therapeutic screen, or integrated multi-omics classifier was identified. These are evidence gaps, not negative biological findings.

## 7. Anatomical structures affected

Primary systems are:

- **Central nervous system:** cerebral cortex, hippocampal systems, synapses, and possibly cerebellum, corpus callosum, and retina. Suggested UBERON terms: brain, cerebral cortex, hippocampus, cerebellum, corpus callosum, retina.
- **Skeleton:** long bones, vertebral column, cortical and trabecular bone; osteoblast and osteoclast compartments.
- **Skeletal muscle/connective tissue:** generalized low muscle mass and hypotonia.
- **Secondary/variable:** kidney, genital tract, respiratory tract, intestine, liver, and pancreas (dontaine2021digestiveinvolvementin pages 11-16, albert2015impairedosteoblastand pages 1-2, li2017sperminesynthasedeficiency pages 1-2, akinyele2024impairedpolyaminemetabolism pages 1-3).

At the subcellular level, lysosomes/autolysosomes and mitochondria are the best-supported affected compartments. No consistent lateralization is established; disease is systemic and generally bilateral.

## 8. Temporal development

Onset is congenital or early pediatric and usually insidious rather than acute. Hypotonia and developmental delay appear first; epilepsy may emerge in early childhood, while osteoporosis, fractures, spinal curvature, facial gestalt, and thin habitus become more conspicuous with age. The phenotype therefore **evolves from childhood into adulthood** (mouskou2021novelhemizygousmissense pages 4-5, qazi2020wholeexomesequencingidentifies pages 1-3).

The disorder is chronic and lifelong. There is no accepted staging system or spontaneous remission pattern. Neurologic and skeletal progression is variable; severe visceral disease can produce early mortality, whereas other affected individuals survive into adulthood. Developmental periods of synaptogenesis and bone accrual are plausible therapeutic windows, but no clinical study has defined an optimal intervention age (dontaine2021digestiveinvolvementin pages 11-16, dontaine2021digestiveinvolvementin pages 16-21).

## 9. Inheritance and population

Inheritance is **X-linked recessive**: hemizygous males are predominantly affected, carrier females transmit the allele to 50% of sons and 50% of daughters at each pregnancy, subject to standard Mendelian probability. De novo variants and maternal mosaicism mean apparently negative family history does not eliminate recurrence risk (mouskou2021novelhemizygousmissense pages 4-5, mouskou2021novelhemizygousmissense pages 1-2).

Penetrance in hemizygous males appears high, but exact penetrance and age dependence are not quantified. Expressivity is variable, including within families; anticipation is not expected because the disease is not a repeat-expansion disorder. Consanguinity is not mechanistically required for an X-linked condition. No validated founder effect, population enrichment, carrier frequency, or ethnic predisposition is known.

Prevalence and incidence per 100,000 cannot be reliably estimated. Approximately 10 families/20 affected individuals and 11 mutations had been described by 2020, and fewer than 30 cases were cited in 2021. These are literature counts, not epidemiologic prevalence estimates. The observed male predominance follows X-linked inheritance rather than demonstrated sex-specific environmental risk (dontaine2021digestiveinvolvementin pages 1-7, qazi2020wholeexomesequencingidentifies pages 1-3).

## 10. Diagnostics

### Recommended approach

1. **Clinical suspicion:** male with developmental delay/intellectual disability, hypotonia, thin habitus, speech/gait impairment, osteoporosis or low-energy fractures, kyphoscoliosis, and possibly epilepsy.
2. **Molecular confirmation:** sequence **SMS** through a neurodevelopmental/epilepsy/bone-fragility panel, WES, WGS, or single-gene testing; confirm candidate variants and segregation by Sanger sequencing.
3. **Functional/biochemical confirmation:** measure spermine synthase activity where available and quantify spermine, spermidine, and their ratio in erythrocytes or validated cells.
4. **Phenotypic assessment:** DXA, skeletal radiographs, fracture history, spine/orthopedic examination, developmental testing, neurologic examination, EEG when seizures are suspected, nutritional assessment, and organ-directed evaluation (dontaine2021digestiveinvolvementin pages 1-7, mouskou2021novelhemizygousmissense pages 4-5, mouskou2021novelhemizygousmissense pages 1-2, qazi2020wholeexomesequencingidentifies pages 1-3).

WGS is useful when coding sequencing is negative because it can detect noncoding, structural, and copy-number lesions. WES has repeatedly diagnosed SRS but may miss deep intronic and some structural variants. CMA can identify larger Xp22.11 deletions but is not sufficient for most single-nucleotide variants. Karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine unless another differential diagnosis is suspected.

RNA sequencing may clarify suspected splice variants. Targeted metabolomics provides functional support. No clinically validated SRS epigenomic, proteomic, liquid-biopsy, or newborn-screening test exists.

### Differential diagnosis

Important alternatives include osteogenesis imperfecta and other monogenic bone-fragility disorders; other X-linked intellectual-developmental syndromes; creatine deficiency syndromes; Menkes disease; congenital muscular disorders; mitochondrial disease; and other polyaminopathies. SRS is distinguished by the combination of SMS variation and the characteristic high spermidine:spermine ratio. A collagen defect is not the primary skeletal mechanism (albert2015impairedosteoblastand pages 1-2, li2017sperminesynthasedeficiency pages 1-2).

No formal consensus clinical criteria were identified; molecular confirmation is therefore central. Cascade testing should be offered to at-risk maternal relatives.

## 11. Outcome and prognosis

No 5-year or 10-year survival rate, median life expectancy, mortality rate, or validated prognostic model exists. Premature death has occurred in severe cases, including the two brothers with major digestive, respiratory, and hepatopancreatic involvement, but this cannot be generalized to all SRS (dontaine2021digestiveinvolvementin pages 11-16, dontaine2021digestiveinvolvementin pages 16-21).

Major long-term morbidity includes intellectual disability, limited communication, impaired mobility, epilepsy, fractures, spinal deformity, feeding difficulty, and dependence in daily living. Recovery of the underlying disorder is not expected with current supportive management. Potential prognostic factors—residual SMS activity, magnitude of the polyamine ratio, seizure burden, nutritional status, bone density, and visceral involvement—are biologically plausible but not prospectively validated.

## 12. Treatment and current applications

### Current clinical management

There is no approved SRS-specific disease-modifying therapy. Care is individualized and multidisciplinary:

- Antiseizure medication; reported agents include carbamazepine, phenobarbital, clobazam, levetiracetam, and valproate.
- Calcium and vitamin D when indicated, monitored carefully because ectopic calcification/nephrocalcinosis has been reported.
- DXA and orthopedic surveillance; fracture prevention and management; scoliosis monitoring.
- Physical, occupational, and speech therapy; mobility aids and fall prevention.
- Nutrition, swallow/feeding support, and enteral feeding where required.
- Monitoring guided by symptoms for renal, respiratory, ophthalmologic, hearing, gastrointestinal, hepatic, and pancreatic complications.
- Clinical genetics and reproductive counseling (mouskou2021novelhemizygousmissense pages 4-5, dontaine2021digestiveinvolvementin pages 16-21, tao2022phenylbutyratemodulatespolyamine pages 1-2).

Suggested MAXO annotations include genetic counseling, molecular genetic testing, biochemical assay, EEG, DXA, orthopedic surveillance, antiseizure pharmacotherapy, calcium/vitamin-D supplementation, physical therapy, occupational therapy, speech therapy, enteral feeding, and fracture management; exact MAXO identifiers require validation.

### Experimental disease-directed strategies

**Phenylbutyrate (PBA):** In patient fibroblasts and Drosophila—not patients—PBA reduced SAT1, toxic polyamine catabolism, and acetyl-CoA depletion; improved mitochondrial/autolysosomal function; and prolonged fly lifespan. In flies, **2 mM** was beneficial, lower concentrations had milder effects, and **10 mM was toxic**; glycerol-PBA prolonged lifespan at **0.6 mM**. These concentrations cannot be directly translated into a human dose (tao2022phenylbutyratemodulatespolyamine pages 1-2, tao2022phenylbutyratemodulatespolyamine pages 2-4).

A useful abstract-level quotation is: **“PBA treatment significantly restored the function of mitochondria and autolysosomes and extended life span in vivo in the Drosophila SRS model.”** The same abstract reports that treatment of patient fibroblasts ameliorated autolysosomal dysfunction. Publication: July 2022; DOI URL: https://doi.org/10.1172/jci.insight.158457 (tao2022phenylbutyratemodulatespolyamine pages 1-2).

**Difluoromethylornithine/eflornithine (DFMO):** A 2023 EMBO Molecular Medicine study reported rebalancing of abnormal polyamine ratios by inhibiting upstream ornithine decarboxylase. The retrieved current review confirms the study and DOI **10.15252/emmm.202317833**, but primary quantitative details were not available in the tool evidence. DFMO should therefore be classified as preclinical/experimental for SRS, not as demonstrated human therapy (wu2024structuralinsightsinto pages 11-12).

**Other approaches:** Antioxidants partially rescued mitochondrial but not lysosomal defects; direct spermine supplementation was ineffective in the cited cell work; polyamine analogues such as (R,R)-1,12-dimethylspermine and redox-sensitive spermine prodrugs have preclinical rationale. These approaches lack established human efficacy (tao2022phenylbutyratemodulatespolyamine pages 1-2, wu2024structuralinsightsinto pages 11-12, akinyele2024impairedpolyaminemetabolism pages 21-24).

The ClinicalTrials.gov search retrieved no relevant SRS-specific interventional study. Trials of PBA or DFMO in cancer and other diseases do not constitute evidence of efficacy in SRS.

### Expert interpretation

The most credible therapeutic principle is **pathway rebalancing**, not simply replacing spermine. Upstream substrate reduction with DFMO, limiting SAT1-mediated toxic catabolism with PBA, reducing oxidative injury, or restoring organelle function may need to be combined. However, CNS exposure, developmental timing, long-term effects on an essential polyamine pathway, skeletal endpoints, and pediatric safety require dedicated preclinical and clinical evaluation (li2017sperminesynthasedeficiency pages 1-2, tao2022phenylbutyratemodulatespolyamine pages 1-2, wu2024structuralinsightsinto pages 11-12).

## 13. Prevention

Primary prevention by lifestyle or vaccination is not applicable. Reproductive prevention options include carrier testing, cascade testing, genetic counseling, preimplantation genetic testing, chorionic-villus or amniotic-fluid prenatal diagnosis when the familial variant is known, and discussion of residual recurrence risk from parental mosaicism (mouskou2021novelhemizygousmissense pages 4-5, mouskou2021novelhemizygousmissense pages 1-2).

There is no population newborn screen. Secondary prevention consists of early molecular diagnosis and surveillance for seizures, low bone density, scoliosis, feeding difficulty, and organ complications. Tertiary prevention includes fracture/fall prevention, nutrition and rehabilitation, seizure control, orthopedic care, aspiration precautions, and prompt treatment of respiratory infections. No vaccine or chemoprophylaxis specifically prevents SRS.

## 14. Other species and natural disease

SMS and polyamine metabolism are deeply conserved across eukaryotes. Orthologues include **Sms** in *Mus musculus* (NCBI Taxonomy **10090**) and **dSms** in *Drosophila melanogaster* (Taxonomy **7227**). No well-established naturally occurring companion-animal, livestock, or wildlife disease equivalent was identified, and no breed association or VBO term is currently justified.

SRS is noninfectious and has no zoonotic potential or cross-species transmission. Comparative relevance lies in conserved biochemical susceptibility rather than transmissibility.

## 15. Model organisms

### Drosophila

Loss of **dSms** recreates the high spermidine/low spermine imbalance and causes reduced viability/lifespan, locomotor impairment, synaptic and retinal degeneration, oxidative stress, lysosomal/autophagic dysfunction, and mitochondrial defects. Genetic or pharmacologic antioxidant enhancement suppresses oxidative stress, and PBA prolongs lifespan, making this a rapid in-vivo platform for mechanism and drug screening (li2017sperminesynthasedeficiency pages 1-2, tao2022phenylbutyratemodulatespolyamine pages 1-2, tao2022phenylbutyratemodulatespolyamine pages 2-4).

**Limitations:** fly neuroanatomy, bone biology, pharmacokinetics, and dosing differ substantially from humans; rescue of lifespan or climbing is not equivalent to clinical benefit.

### Mouse

The **G56S Sms mouse** carries a missense allele and lacks detectable SMS protein. It shows elevated spermidine:spermine ratio, failure to thrive, short stature, reduced bone density, learning impairment, anxiety-like behavior, reduced mobility, heightened fear responses, reduced total/regional brain volumes, and impaired mitochondrial oxidative phosphorylation in cortex, fibroblasts, and Sms-null hippocampal cells (akinyele2024impairedpolyaminemetabolism pages 1-3).

A useful exact abstract quotation is: **“Collectively, our study establishes the suitability of the G56S mice as a preclinical model for SRS and provides a set of molecular and functional outcome measures that can be used to evaluate therapeutic interventions for SRS.”** Publication: May 2024; DOI URL: https://doi.org/10.1242/dmm.050639 (akinyele2024impairedpolyaminemetabolism pages 1-3).

**Applications:** pharmacokinetics, chronic safety, behavioral endpoints, MRI brain volume, bone density, polyamine ratios, and mitochondrial respiration. **Limitations:** one allele cannot represent the full human variant spectrum; anxiety/fear assays are indirect; lifespan and severe visceral phenotypes require further characterization.

### Human cellular models

Patient lymphoblasts, fibroblasts, osteoblast-lineage marrow stromal cells, and engineered hippocampal cells are useful for enzyme activity, polyamine metabolomics, mineralization, lysosomal/autophagic flux, oxidative stress, acetyl-CoA/protein acetylation, and drug-response assays. Their main limitation is the inability to reproduce whole-organism development, blood–brain-barrier pharmacology, biomechanics, and systemic toxicity (albert2015impairedosteoblastand pages 1-2, li2017sperminesynthasedeficiency pages 1-2, tao2022phenylbutyratemodulatespolyamine pages 1-2).

## Key evidence gaps and curation cautions

1. Incidence, prevalence, penetrance, life expectancy, and feature frequencies remain unknown.
2. The apparent lack of a clear genotype–phenotype relationship is based on very small cohorts.
3. Gastrointestinal and hepatopancreatic manifestations remain candidate phenotype expansions.
4. N8-acetylspermidine and the spermidine:spermine ratio require assay standardization and prospective diagnostic validation.
5. PBA, DFMO, antioxidants, analogues, and prodrugs remain experimental; no human SRS response rate or adverse-event profile exists.
6. No established SRS single-cell, spatial, epigenomic, or comprehensive multi-omic reference dataset was identified.
7. Exact PMIDs were not present in the retrieved source metadata; DOI URLs and publication dates are therefore supplied rather than inventing PMID assignments.

Overall, the 2023–2024 literature materially advances SRS from a descriptive syndrome toward a testable metabolic-organelle disease model. The 2024 G56S mouse supplies translational outcome measures, while pathway-rebalancing studies identify SAT1, ornithine decarboxylase, acetyl-CoA homeostasis, oxidative stress, lysosomes, and mitochondrial respiration as candidate intervention points. The central translational challenge is to normalize polyamine flux without disrupting the essential developmental functions of spermine and spermidine.

References

1. (dontaine2021digestiveinvolvementin pages 1-7): Pauline Dontaine, Elisa Kottos, Martine Dassonville, Ovidiu Balasel, Véronique Catros, Julie Soblet, Pascale Perlot, and Catheline Vilain. Digestive involvement in a severe form of snyder-robinson syndrome: possible expansion of the phenotype. Jan 2021. URL: https://doi.org/10.1016/j.ejmg.2020.104097, doi:10.1016/j.ejmg.2020.104097. This article has 10 citations and is from a peer-reviewed journal.

2. (albert2015impairedosteoblastand pages 1-2): Jessica S Albert, Nisan Bhattacharyya, Lynne A Wolfe, William P Bone, Valerie Maduro, John Accardi, David R Adams, Charles E Schwartz, Joy Norris, Tim Wood, Rachel I Gafni, Michael T Collins, Laura L Tosi, Thomas C Markello, William A Gahl, and Cornelius F Boerkoel. Impaired osteoblast and osteoclast function characterize the osteoporosis of snyder - robinson syndrome. Orphanet Journal of Rare Diseases, Mar 2015. URL: https://doi.org/10.1186/s13023-015-0235-8, doi:10.1186/s13023-015-0235-8. This article has 64 citations and is from a peer-reviewed journal.

3. (li2017sperminesynthasedeficiency pages 1-2): Chong Li, Jennifer M. Brazill, Sha Liu, Christofer Bello, Yi Zhu, Marie Morimoto, Lauren Cascio, Rini Pauly, Zoraida Diaz-Perez, May Christine V. Malicdan, Hongbo Wang, Luigi Boccuto, Charles E. Schwartz, William A. Gahl, Cornelius F. Boerkoel, and R. Grace Zhai. Spermine synthase deficiency causes lysosomal dysfunction and oxidative stress in models of snyder-robinson syndrome. Nature Communications, Nov 2017. URL: https://doi.org/10.1038/s41467-017-01289-7, doi:10.1038/s41467-017-01289-7. This article has 107 citations and is from a highest quality peer-reviewed journal.

4. (akinyele2024impairedpolyaminemetabolism pages 1-3): Oluwaseun Akinyele, Anushe Munir, Marie A. Johnson, Megan S. Perez, Yuan Gao, Jackson R. Foley, Ashley Nwafor, Yijen Wu, Tracy Murray-Stewart, Robert A. Casero, Hülya Bayir, and Dwi U. Kemaladewi. Impaired polyamine metabolism causes behavioral and neuroanatomical defects in a mouse model of snyder–robinson syndrome. Disease Models &amp; Mechanisms, May 2024. URL: https://doi.org/10.1242/dmm.050639, doi:10.1242/dmm.050639. This article has 19 citations and is from a domain leading peer-reviewed journal.

5. (mouskou2021novelhemizygousmissense pages 1-2): Stella Mouskou, Adamantios Katerelos, Artemis Doulgeraki, Sofia Leka-Emiri, Emmanouil Manolakos, Ioannis Papoulidis, Athina Ververi, Georgios Vartzelis, Anastasia Korona, Sotiria Mastroyanni, and Konstantinos Voudris. Novel hemizygous missense variant of spermine synthase (sms) gene causes snyder-robinson syndrome in a four-year-old boy. Molecular Syndromology, 12:194-200, Apr 2021. URL: https://doi.org/10.1159/000514122, doi:10.1159/000514122. This article has 9 citations and is from a peer-reviewed journal.

6. (OpenTargets Search: Snyder-Robinson syndrome-SMS): Open Targets Query (Snyder-Robinson syndrome-SMS, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (dontaine2021digestiveinvolvementin pages 11-16): Pauline Dontaine, Elisa Kottos, Martine Dassonville, Ovidiu Balasel, Véronique Catros, Julie Soblet, Pascale Perlot, and Catheline Vilain. Digestive involvement in a severe form of snyder-robinson syndrome: possible expansion of the phenotype. Jan 2021. URL: https://doi.org/10.1016/j.ejmg.2020.104097, doi:10.1016/j.ejmg.2020.104097. This article has 10 citations and is from a peer-reviewed journal.

8. (qazi2020wholeexomesequencingidentifies pages 1-3): Talal J. Qazi, Qiao Wu, Ailikemu Aierken, Daru Lu, Ihtisham Bukhari, Hafiz M. J. Hussain, Jingmin Yang, Asif Mir, and Hong Qing. Whole-exome sequencing identifies a novel mutation in spermine synthase gene (sms) associated with snyder-robinson syndrome. BMC Medical Genetics, Aug 2020. URL: https://doi.org/10.1186/s12881-020-01095-x, doi:10.1186/s12881-020-01095-x. This article has 13 citations and is from a peer-reviewed journal.

9. (tao2022phenylbutyratemodulatespolyamine pages 1-2): Xianzun Tao, Yi Zhu, Zoraida Diaz-Perez, Seok-Ho Yu, Jackson R. Foley, Tracy Murray Stewart, Robert A. Casero, Richard Steet, and R. Grace Zhai. Phenylbutyrate modulates polyamine acetylase and ameliorates snyder-robinson syndrome in a drosophila model and patient cells. JCI Insight, Jul 2022. URL: https://doi.org/10.1172/jci.insight.158457, doi:10.1172/jci.insight.158457. This article has 21 citations and is from a domain leading peer-reviewed journal.

10. (tao2022phenylbutyratemodulatespolyamine pages 2-4): Xianzun Tao, Yi Zhu, Zoraida Diaz-Perez, Seok-Ho Yu, Jackson R. Foley, Tracy Murray Stewart, Robert A. Casero, Richard Steet, and R. Grace Zhai. Phenylbutyrate modulates polyamine acetylase and ameliorates snyder-robinson syndrome in a drosophila model and patient cells. JCI Insight, Jul 2022. URL: https://doi.org/10.1172/jci.insight.158457, doi:10.1172/jci.insight.158457. This article has 21 citations and is from a domain leading peer-reviewed journal.

11. (mouskou2021novelhemizygousmissense pages 4-5): Stella Mouskou, Adamantios Katerelos, Artemis Doulgeraki, Sofia Leka-Emiri, Emmanouil Manolakos, Ioannis Papoulidis, Athina Ververi, Georgios Vartzelis, Anastasia Korona, Sotiria Mastroyanni, and Konstantinos Voudris. Novel hemizygous missense variant of spermine synthase (sms) gene causes snyder-robinson syndrome in a four-year-old boy. Molecular Syndromology, 12:194-200, Apr 2021. URL: https://doi.org/10.1159/000514122, doi:10.1159/000514122. This article has 9 citations and is from a peer-reviewed journal.

12. (dontaine2021digestiveinvolvementin pages 16-21): Pauline Dontaine, Elisa Kottos, Martine Dassonville, Ovidiu Balasel, Véronique Catros, Julie Soblet, Pascale Perlot, and Catheline Vilain. Digestive involvement in a severe form of snyder-robinson syndrome: possible expansion of the phenotype. Jan 2021. URL: https://doi.org/10.1016/j.ejmg.2020.104097, doi:10.1016/j.ejmg.2020.104097. This article has 10 citations and is from a peer-reviewed journal.

13. (wu2024structuralinsightsinto pages 11-12): Bing Wu and Sen Liu. Structural insights into the mechanisms underlying polyaminopathies. International Journal of Molecular Sciences, 25:6340, Jun 2024. URL: https://doi.org/10.3390/ijms25126340, doi:10.3390/ijms25126340. This article has 8 citations.

14. (akinyele2024impairedpolyaminemetabolism pages 21-24): Oluwaseun Akinyele, Anushe Munir, Marie A. Johnson, Megan S. Perez, Yuan Gao, Jackson R. Foley, Ashley Nwafor, Yijen Wu, Tracy Murray-Stewart, Robert A. Casero, Hülya Bayir, and Dwi U. Kemaladewi. Impaired polyamine metabolism causes behavioral and neuroanatomical defects in a mouse model of snyder–robinson syndrome. Disease Models &amp; Mechanisms, May 2024. URL: https://doi.org/10.1242/dmm.050639, doi:10.1242/dmm.050639. This article has 19 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Snyder-Robinson_Syndrome-deep-research-falcon_artifacts/artifact-00.md)