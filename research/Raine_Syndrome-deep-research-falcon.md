---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:42:38.831171'
end_time: '2026-07-31T00:49:53.288411'
duration_seconds: 434.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Raine Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Raine_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Raine Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Raine Syndrome** covering all of the
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
- **Disease Name:** Raine Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Raine Syndrome** covering all of the
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


# Raine Syndrome: Disease Characteristics Research Report

## Executive summary

Raine syndrome (RNS) is an ultra-rare, autosomal-recessive skeletal dysplasia caused by biallelic loss-of-function variants in **FAM20C**, which encodes a Golgi-associated kinase responsible for phosphorylating many secreted proteins. Its spectrum extends from a severe congenital form—characterized by generalized osteosclerosis, distinctive craniofacial abnormalities, intracranial calcification, pulmonary hypoplasia, and death in early infancy—to nonlethal disease with hypophosphatemic rickets/osteomalacia, neurological disability, hearing or visual impairment, and major dental/gingival disease. A 2021 literature synthesis counted 70 reported patients: 41 lethal and 29 nonlethal; prevalence remains estimated at less than 1 per million. These figures reflect published cases rather than population-based surveillance and are therefore vulnerable to ascertainment bias. (costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 1-2)

Recent work has expanded the disease beyond a simple osteosclerotic dysplasia. A 2023 computational study proposed brain-relevant FAM20C substrates involving cholesterol/lipoprotein biology and axodendritic transport; a 2023 mouse study reproduced intracranial calcification; and a 2024 human gingival proteomics study identified a **TGFβ–SMAD–YAP/TAZ profibrotic loop** in affected gingiva. (palmalara2023potentialroleof pages 1-2, costa2024gingivalproteomicsreveals pages 2-3, costa2024gingivalproteomicsreveals pages 1-2)

| domain | key evidence/finding | suggested ontology identifiers |
|---|---|---|
| Disease identifiers | Raine syndrome is an ultra-rare osteosclerotic skeletal dysplasia caused by biallelic **FAM20C** loss-of-function; legacy disease identifiers include **OMIM 259775** and the historical descriptor “congenital sclerosing osteomalacia with cerebral calcification” (**OMIM 259660**). Open Targets links **FAM20C** to **MONDO_0009821 lethal osteosclerotic bone dysplasia**; mapping between MONDO labels and Raine syndrome nomenclature should be curated carefully. Prevalence reported as **<1/1,000,000**. (OpenTargets Search: Raine syndrome-FAM20C, costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 1-2) | MONDO_0009821; OMIM:259775; OMIM:259660; MeSH/Orphanet/ICD term-only suggestions |
| Gene / molecular basis | Causal gene: **FAM20C** (Golgi-associated secretory pathway kinase). Human disease mechanism is predominantly **germline autosomal recessive loss of function**. Reported pathogenic classes include whole-gene deletions, microdeletions, missense, nonsense, splice-site, and frameshift/truncating variants; 2024 review context summarized **42 variants** total (**22 lethal, 20 nonlethal**). Residual kinase activity is thought to correlate with nonlethal survival, but genotype-phenotype prediction remains imperfect. (costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 16-17, costa2024gingivalproteomicsreveals pages 2-3) | HGNC:FAM20C term-only suggestion; SO:missense_variant / nonsense_variant / splice_donor_variant / frameshift_variant / deletion term-only suggestions |
| Inheritance / population | Inheritance is **autosomal recessive**. Published review-level aggregation identified **70 total cases** through 2021 (**41 lethal, 29 nonlethal**), indicating extreme rarity and likely ascertainment bias. No robust carrier-frequency or incidence estimate was identified in the retrieved evidence. (costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 1-2) | HP:Autosomal recessive inheritance (term-only suggestion); epidemiology ontology term-only suggestions |
| Core phenotype (skeletal / craniofacial) | Core recurrent manifestations include **generalized osteosclerosis**, periosteal bone formation, flat facial profile, **hypoplastic nose**, **midface hypoplasia**, **prominent eyes/exophthalmos**, choanal atresia/stenosis, and severe respiratory compromise in lethal neonatal disease. Nonlethal cases may evolve from osteosclerosis toward osteomalacia/rickets-like features with variable craniofacial persistence. (palmalara2023potentialroleof pages 1-2, costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 1-2) | HPO term-only suggestions: osteosclerosis; periosteal bone thickening; flat facies; hypoplastic nose; midface retrusion; exophthalmos; choanal atresia/choanal stenosis; respiratory insufficiency |
| Core phenotype (neurologic / imaging) | **Intracranial/intracerebral calcifications** are a hallmark; neurological features can include **developmental delay, intellectual disability, seizures, structural brain defects**, and in prenatal imaging an echogenic brain or enlarged choroid plexus. 2023 mouse work further supports intracranial calcification as a disease-relevant feature. (palmalara2023potentialroleof pages 1-2, palmalara2021fam20coverviewclassic pages 1-2) | HPO term-only suggestions: intracranial calcification; cerebral calcification; developmental delay; intellectual disability; seizures; abnormality of the choroid plexus |
| Core phenotype (oral / dental / gingival) | Nonlethal disease frequently includes **hypoplastic amelogenesis imperfecta**, dentin defects, gingival hyperplasia/overgrowth, fibrosis, and ectopic gingival calcifications. The 2024 proteomics study documented fibrosis and pathological gingival calcifications in two unrelated patients with distinct nonlethal variants. (costa2024gingivalproteomicsreveals pages 1-2, costa2024gingivalproteomicsreveals pages 2-3) | HPO term-only suggestions: amelogenesis imperfecta; abnormal dentin morphology; gingival overgrowth; gingival fibrosis; ectopic calcification |
| Laboratory abnormalities | Nonlethal Raine syndrome is repeatedly associated with **hypophosphatemia** and disturbed phosphatemia regulation; mechanistic literature links FAM20C deficiency to abnormal **FGF23** handling and phosphate wasting. Exact laboratory ranges were not available in retrieved context. (palmalara2023potentialroleof pages 1-2, costa2024gingivalproteomicsreveals pages 21-22, zhang2020highphosphatedietimproved pages 11-12, costa2024gingivalproteomicsreveals pages 1-2) | HPO term-only suggestions: hypophosphatemia; increased circulating FGF23; renal phosphate wasting |
| Mechanism / pathophysiology | FAM20C is a **Golgi kinase** that phosphorylates secreted phosphoproteins, especially proteins involved in biomineralization. Disease mechanism: FAM20C loss impairs phosphorylation/localization/activity of secreted substrates, disrupting **SIBLING proteins**, **FGF23** regulation, extracellular matrix organization, and mineralization in bone/teeth; 2024 work additionally implicates **TGFβ/SMAD** and **YAP/TAZ** signaling in gingival fibrosis. (palmalara2023potentialroleof pages 1-2, costa2024gingivalproteomicsreveals pages 1-2, costa2024gingivalproteomicsreveals pages 2-3) | GO term-only suggestions: protein phosphorylation; biomineral tissue development; extracellular matrix organization; regulation of phosphate ion homeostasis; TGF-beta receptor signaling pathway; SMAD protein signal transduction; Hippo signaling/YAP-TAZ-related transcription |
| Anatomy affected | Primary structures: **craniofacial skeleton**, long bones, teeth, gingiva, and brain/intracranial tissues; secondary involvement includes airways/choanae and lungs via respiratory compromise/pulmonary hypoplasia in lethal neonatal disease. (palmalara2023potentialroleof pages 1-2, costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 1-2) | UBERON term-only suggestions: craniofacial skeleton; long bone; tooth; gingiva; brain; choroid plexus; choana; lung |
| Cell / tissue types | Disease-relevant cell populations inferred from human and model evidence include **osteoblast-lineage cells**, **odontoblasts**, **ameloblasts**, **gingival fibroblasts**, and likely brain-resident cells affected by abnormal phosphoproteome/mineralization. The 2024 human study specifically analyzed **primary gingival fibroblasts**. (costa2024gingivalproteomicsreveals pages 2-3, costa2024gingivalproteomicsreveals pages 1-2, palmalara2023potentialroleof pages 1-2) | CL term-only suggestions: osteoblast; odontoblast; ameloblast; fibroblast; gingival fibroblast; neuron term-only suggestion |
| Subcellular localization | Normal FAM20C is **Golgi-localized** within the secretory pathway; disease-associated dysfunction includes altered localization and loss of effective Golgi association. In gingival fibroblasts from affected individuals, 2024 data showed increased **ER colocalization** and reduced cis-Golgi association. (costa2024gingivalproteomicsreveals pages 2-3, palmalara2023potentialroleof pages 1-2) | GO Cellular Component term-only suggestions: Golgi apparatus; Golgi lumen; endoplasmic reticulum; extracellular region |
| Diagnostics | Diagnosis is based on clinical-radiologic suspicion plus **molecular confirmation of biallelic FAM20C variants**. Useful findings include prenatal ultrasound recognition of characteristic facies and intracranial calcification, postnatal skeletal imaging showing osteosclerosis, brain imaging for calcifications, and biochemical assessment of phosphate/FGF23 axis where survival permits. No standardized disease-specific diagnostic criteria were identified in the retrieved evidence. (palmalara2021fam20coverviewclassic pages 1-2) | MAXO term-only suggestions: molecular genetic testing; exome sequencing; genome sequencing; targeted gene panel; prenatal ultrasound; skeletal radiography; cranial CT/MRI; serum phosphate measurement |
| Treatment / supportive care | No approved disease-modifying therapy specific to Raine syndrome was identified. Management is **supportive and multidisciplinary**: neonatal airway/respiratory support in lethal presentations; management of hypophosphatemia/rickets-like disease in survivors; dental and periodontal care for amelogenesis imperfecta/gingival disease. Experimental mouse data suggest **high-phosphate diet** can improve skeletal development, but this is preclinical and not an established human therapy. (zhang2020highphosphatedietimproved pages 11-12, costa2024gingivalproteomicsreveals pages 1-2) | MAXO term-only suggestions: respiratory support; phosphate supplementation; active vitamin D analogue therapy term-only suggestion; dental surveillance; periodontal management; nutritional management; multidisciplinary care |
| Prognosis / course | Prognosis is bimodal: classic lethal disease often causes death in the **first weeks of life**, largely due to **pulmonary hypoplasia/respiratory failure**; nonlethal disease shows **variable expressivity** with childhood-to-adult survival and chronic skeletal, neurologic, hearing/vision, and dental morbidity. Long-term survival statistics were not available. (costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 1-2, costa2024gingivalproteomicsreveals pages 2-3) | HPO term-only suggestions: pulmonary hypoplasia; respiratory failure; variable expressivity |
| Model organisms / experimental systems | Mouse **Fam20c-deficient** models recapitulate key features including abnormal mineralization, hypophosphatemic rickets/osteomalacia-like changes, dental defects, and **intracranial calcification** (2023). Human mechanistic evidence also includes 2024 **gingival proteomics**, primary fibroblast studies, siRNA knockdown, and prior in vitro kinase assays. (palmalara2023potentialroleof pages 1-2, zhang2020highphosphatedietimproved pages 11-12, costa2024gingivalproteomicsreveals pages 2-3, costa2024gingivalproteomicsreveals pages 1-2) | NCBITaxon term-only suggestion: Mus musculus; GO/CL term-only suggestions as above |
| Evidence limitations | Much evidence comes from **case reports, small families, reviews, mouse studies, and one 2024 two-patient omics study**. Many exact ontology IDs, laboratory ranges, penetrance estimates, founder effects, and standardized treatment outcomes were not available in retrieved context; phenotype frequencies are incompletely quantified and likely affected by publication bias. (costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 1-2, costa2024gingivalproteomicsreveals pages 2-3) | Evidence Ontology term-only suggestions: case report; review; animal model; in vitro experiment; proteomics study |


*Table: This compact table summarizes the main knowledge-base elements for Raine syndrome, including identifiers, core phenotypes, mechanisms, anatomy, diagnostics, management, and evidence gaps. It is useful as a structured seed for ontology mapping and curation.*

## 1. Disease information

### Definition and classification

Raine syndrome is a Mendelian, autosomal-recessive disorder of secretory-pathway protein phosphorylation, biomineralization, and phosphate homeostasis. It is conventionally classified among osteosclerotic bone dysplasias, although surviving patients can develop hypophosphatemic rickets or osteomalacia alongside radiographic sclerosis. (palmalara2023potentialroleof pages 1-2, costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 1-2)

**Principal identifiers and names**

- **MONDO:** **MONDO:0009821**, labeled “lethal osteosclerotic bone dysplasia” in the retrieved Open Targets mapping.
- **OMIM:** **259775**, Raine syndrome; **259660** is the historical entry “congenital sclerosing osteomalacia with cerebral calcification.”
- **Gene-associated name:** *FAM20C*-related osteosclerotic dysplasia.
- **Synonyms:** Raine syndrome; lethal osteosclerotic bone dysplasia; osteosclerotic bone dysplasia, Raine type; congenital sclerosing osteomalacia with cerebral calcification; lethal and nonlethal Raine syndrome.
- A dedicated, disease-specific ICD-10 or ICD-11 code was not established in the retrieved material; clinically, broader congenital osteochondrodysplasia codes may be used. MeSH and SNOMED CT mappings should be verified directly before production use. (OpenTargets Search: Raine syndrome-FAM20C, palmalara2023potentialroleof pages 26-27, palmalara2021fam20coverviewclassic pages 1-2)

The evidence base is predominantly **aggregated disease-level literature assembled from individual case reports and small families**, not EHR-derived population data. The 2024 mechanistic study used tissue and primary fibroblasts from only two affected individuals. (costa2024gingivalproteomicsreveals pages 2-3, palmalara2021fam20coverviewclassic pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is **germline biallelic loss of FAM20C function**. FAM20C is a serine/threonine kinase located mainly in the Golgi/secretory pathway and recognizes secreted-protein motifs including S-X-E/pS. Loss of kinase activity, defective intracellular localization, altered secretion, or protein truncation impairs extracellular phosphoprotein regulation. (palmalara2023potentialroleof pages 1-2, costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 16-17)

Reported variant classes include whole-gene and multiexon deletions, frameshift, nonsense, splice-site, and missense variants. A 2024 summary listed **42 disease-associated variants—22 associated with lethal and 20 with nonlethal disease**. Variants abolishing protein or kinase activity tend to produce lethal disease, whereas residual activity is more often compatible with survival; this is a trend rather than a deterministic clinical rule. (costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 16-17)

### Risk factors

- **Genetic:** two pathogenic/likely pathogenic alleles in trans; parental consanguinity raises the probability of homozygosity. Each pregnancy of two confirmed carriers has the standard autosomal-recessive risks: 25% affected, 50% carrier, and 25% unaffected/noncarrier.
- **Family history:** an affected sibling or known parental carrier status materially increases prior probability.
- **Sex, age, and ancestry:** no demonstrated sex-specific biological risk or reliable ethnicity-specific prevalence was found.
- **Environment, lifestyle, toxins, occupation, or infection:** no evidence that any of these causes Raine syndrome.

No validated protective FAM20C allele, modifier gene, lifestyle factor, or gene–environment interaction has been established. Dietary phosphate modified skeletal severity in a mouse model, but that is modification of downstream physiology—not prevention of the genetic disorder. (zhang2020highphosphatedietimproved pages 11-12)

## 3. Phenotypes

Because published series are small and enriched for severe cases, robust percentages are unavailable for most manifestations. “Common” below means recurrent in reports/reviews, not a population-derived frequency.

### Congenital skeletal and craniofacial phenotype

- **Generalized osteosclerosis**—congenital, often severe in lethal disease; suggested HPO: *Osteosclerosis*.
- **Periosteal bone formation/thickening**; HPO term suggestion: *Abnormal periosteum morphology*.
- **Flat facial profile, midface hypoplasia, hypoplastic/depressed nasal bridge, prominent eyes or exophthalmos, low-set ears, microcephaly, and cleft palate**; congenital and variably persistent.
- **Choanal stenosis/atresia**, which can compound neonatal respiratory compromise.
- **Craniosynostosis/multisuture synostosis** has been documented prenatally in recent severe presentations.
- **Long-bone and growth-plate abnormalities** can evolve into rickets/osteomalacia in survivors. (palmalara2023potentialroleof pages 1-2, costa2024gingivalproteomicsreveals pages 21-22, palmalara2021fam20coverviewclassic pages 1-2)

Suggested HPO terms include *Midface retrusion*, *Hypoplastic nose*, *Depressed nasal bridge*, *Exophthalmos*, *Low-set ears*, *Microcephaly*, *Cleft palate*, *Choanal atresia*, *Craniosynostosis*, *Rickets*, and *Osteomalacia*.

### Neurological and neuroimaging phenotype

Intracranial or intracerebral calcification is a hallmark and may be visible prenatally. Other reported findings include enlarged choroid plexuses, echogenic fetal brain, ventricular abnormalities, structural brain malformations, developmental delay, intellectual disability, and seizures. Severity ranges from imaging abnormalities without fully defined functional effect to substantial lifelong neurodevelopmental disability. (palmalara2023potentialroleof pages 1-2, palmalara2021fam20coverviewclassic pages 1-2)

Suggested HPO terms: *Intracranial calcification*, *Cerebral calcification*, *Structural brain anomaly*, *Global developmental delay*, *Intellectual disability*, *Seizure*, and *Abnormality of the choroid plexus*.

### Respiratory phenotype

Pulmonary hypoplasia and respiratory insufficiency are major determinants of neonatal lethality; craniofacial airway obstruction can contribute. Most classic lethal cases die during the first weeks of life. Suggested HPO: *Pulmonary hypoplasia*, *Respiratory insufficiency*, *Neonatal respiratory distress*. (palmalara2021fam20coverviewclassic pages 1-2)

### Dental and gingival phenotype

Survivors commonly have hypoplastic amelogenesis imperfecta, abnormal dentin, delayed or abnormal tooth development, gingival overgrowth/fibrosis, and gingival or other ectopic calcifications. These impair mastication, oral hygiene, appearance, speech, and periodontal health and can require repeated dental care. In two 2024 cases, one patient also had visual impairment and the other hearing impairment. (costa2024gingivalproteomicsreveals pages 2-3, costa2024gingivalproteomicsreveals pages 1-2)

Suggested HPO: *Amelogenesis imperfecta*, *Abnormal dentin morphology*, *Gingival overgrowth*, *Gingival fibrosis*, *Ectopic calcification*, *Visual impairment*, and *Hearing impairment*.

### Laboratory abnormalities

Nonlethal disease is associated with hypophosphatemia, FGF23 dysregulation, renal phosphate wasting, and rickets/osteomalacia physiology. Appropriate measurements include fasting serum phosphate interpreted against age-specific ranges, calcium, alkaline phosphatase, PTH, creatinine, 25-hydroxyvitamin D, 1,25-dihydroxyvitamin D, intact and/or C-terminal FGF23, urine phosphate, tubular maximum phosphate reabsorption/GFR, and renal ultrasound for nephrocalcinosis. Exact disease-specific reference ranges or sensitivities have not been established. (palmalara2023potentialroleof pages 1-2, costa2024gingivalproteomicsreveals pages 21-22, zhang2020highphosphatedietimproved pages 11-12)

No validated Raine-specific quality-of-life instrument or EQ-5D/SF-36 dataset was found.

## 4. Genetic and molecular information

**Causal gene:** **FAM20C**, encoding FAM20C Golgi-associated secretory-pathway kinase; Ensembl target **ENSG00000177706**. The variants are constitutional/germline, not somatic drivers. (OpenTargets Search: Raine syndrome-FAM20C)

The pathogenic mechanism is predominantly loss of function through absent protein, truncation/nonsense-mediated decay, catalytic impairment, mislocalization, or defective secretion. Among 22 exclusively lethal variants summarized in a 2021 review, absent/nonsense/truncated forms were the largest category, including homozygous whole-gene deletions and a reported approximately 487-kb 7p22 deletion. (palmalara2021fam20coverviewclassic pages 16-17)

The 2024 gingival study examined two nonlethal genotypes: **p.Pro496Leu**, predicted to disrupt the activation loop, and a splice-associated **p.Trp202Cysfs*** product yielding a 239-amino-acid truncated protein. Variant interpretation should nevertheless use current ACMG/AMP criteria, segregation, population frequency, phenotype match, and functional evidence rather than the publication’s phenotype alone. (costa2024gingivalproteomicsreveals pages 2-3)

Pathogenic alleles are expected to be individually rare or absent from large population databases, but no comprehensive gnomAD allele-frequency table was retrieved. No validated modifier genes, protective alleles, disease-specific methylation signature, repeat expansion, recurrent aneuploidy, or somatic mosaic mechanism is established. Large deletions encompassing FAM20C can cause disease, so copy-number analysis is necessary when sequencing detects only one allele. (palmalara2021fam20coverviewclassic pages 16-17)

## 5. Environmental information

Raine syndrome is not known to be caused or triggered by toxins, radiation, pollution, smoking, alcohol, diet, exercise, occupational exposure, bacteria, viruses, fungi, or parasites. Environment can influence complications—for example, phosphate intake, dental hygiene, respiratory infection burden, and access to specialist care—but evidence for disease-specific gene–environment interaction is absent. There is no zoonotic or transmissible component.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic defect:** biallelic FAM20C loss-of-function.
2. **Subcellular defect:** reduced Golgi/secretory-pathway kinase activity, with some variants causing ER retention or altered localization.
3. **Substrate defect:** hypophosphorylation of secreted phosphoproteins, including SIBLING-family biomineralization proteins and proteins involved in FGF23 processing.
4. **Systemic consequences:** disordered extracellular-matrix mineralization and abnormal FGF23/phosphate homeostasis.
5. **Tissue outcomes:** osteosclerosis and periosteal abnormalities prenatally, followed in survivors by renal-phosphate-wasting hypophosphatemia, rickets/osteomalacia, dental mineralization defects, ectopic calcification, and neurological abnormalities.
6. **Clinical outcomes:** craniofacial dysplasia, respiratory failure in severe neonatal disease, chronic skeletal/dental disability, and variable neurodevelopmental impairment. (palmalara2023potentialroleof pages 1-2, costa2024gingivalproteomicsreveals pages 1-2, zhang2020highphosphatedietimproved pages 11-12)

FAM20C phosphorylates more than 90–100 secreted or body-fluid proteins, supporting a multisystem phosphoproteinopathy rather than a bone-exclusive disorder. Suggested GO annotations include *protein phosphorylation*, *extracellular matrix organization*, *biomineral tissue development*, *regulation of phosphate ion homeostasis*, *skeletal system development*, and *tooth mineralization*. Relevant compartments are *Golgi apparatus*, *Golgi lumen*, *endoplasmic reticulum*, *secretory vesicle*, and *extracellular region*. (palmalara2023potentialroleof pages 1-2, palmalara2021fam20coverviewclassic pages 1-2)

### 2024 human proteomics development

Costa et al. used gingival tissue, primary gingival fibroblasts, label-free LC-MS/MS proteomics, immunomorphology, biochemistry, and siRNA in two unrelated patients. They found excessive/disorganized ECM, fibrosis, pathological calcification, and increased POSTN, SPARC, and VIM. TGFβ/SMAD signaling and YAP/TAZ cofactors were activated; FAM20C knockdown supported a self-reinforcing profibrotic loop. Mutant fibroblasts showed enhanced ER colocalization and loss of normal cis-Golgi association. This is direct human tissue and cell evidence, but sample size was two. (costa2024gingivalproteomicsreveals pages 2-3, costa2024gingivalproteomicsreveals pages 1-2)

The authors’ abstract states: **“They furthermore uncover the contribution of increased TGFβ–YAP/TAZ signaling in the pathogenesis of the gingival fibrosis.”** [Scientific Reports, 12 April 2024; DOI: https://doi.org/10.1038/s41598-024-59713-0]. (costa2024gingivalproteomicsreveals pages 1-2)

### Brain mechanisms

The 2023 computational analysis linked highly expressed brain targets/interactors to cholesterol and lipoprotein processes, axodendritic transport, and neuronal compartments. These are hypothesis-generating associations, not proof that any individual substrate causes seizures or intellectual disability. Suggested GO terms include *axon transport*, *dendrite development*, and *cholesterol metabolic process*; suggested CL terms include *neuron*, *astrocyte*, and *choroid plexus epithelial cell*, although direct cell-specific causality remains unproven. [Published 17 May 2023; DOI: https://doi.org/10.3390/ijms24108904]. (palmalara2023potentialroleof pages 1-2)

No disease-specific single-cell, spatial transcriptomic, lipidomic, metabolomic, CRISPR-screen, or integrated multi-omic human study was identified.

## 7. Anatomical structures affected

Primary sites are the craniofacial skeleton, skull sutures, long bones and growth plates, teeth, dentin, enamel, gingiva/periodontium, and brain/intracranial tissues. The choanae, upper airway, lungs, eyes, ears, and kidneys may be involved directly or through complications. Disease is usually systemic and bilateral rather than consistently lateralized. (palmalara2023potentialroleof pages 1-2, costa2024gingivalproteomicsreveals pages 2-3, palmalara2021fam20coverviewclassic pages 1-2)

Suggested UBERON terms: *craniofacial skeleton*, *calvaria*, *cranial suture*, *long bone*, *growth plate cartilage*, *tooth*, *enamel*, *dentin*, *gingiva*, *periodontal ligament*, *brain*, *choroid plexus*, *choana*, *lung*, and *kidney*. Suggested CL terms: *osteoblast*, *osteocyte*, *chondrocyte*, *odontoblast*, *ameloblast*, *gingival fibroblast*, and *neuron*. The best directly demonstrated human cell type in recent work is the gingival fibroblast. (costa2024gingivalproteomicsreveals pages 2-3, costa2024gingivalproteomicsreveals pages 1-2)

## 8. Temporal development

The severe phenotype begins prenatally. Ultrasound may reveal a flat profile, hypoplastic nose, prominent eyes, echogenic brain, enlarged choroid plexus, ventricular changes, intracranial calcification, and craniosynostosis. Neonatal disease can progress rapidly to respiratory death. (palmalara2021fam20coverviewclassic pages 1-2)

Nonlethal disease is congenital but chronic and variably progressive. Skeletal findings can shift from early osteosclerosis to hypophosphatemic rickets/osteomalacia; dental and gingival abnormalities emerge with tooth development, while developmental disability or seizures may become apparent in childhood. Adult survival—including middle-aged and elderly patients—has been reported, but no formal stages, remission pattern, median survival, or validated longitudinal progression rate exists. (costa2024gingivalproteomicsreveals pages 1-2, costa2024gingivalproteomicsreveals pages 21-22)

Critical clinical windows are prenatal recognition, immediate neonatal airway assessment, childhood growth and phosphate monitoring, tooth eruption, and ongoing neurological surveillance. There is no evidence of spontaneous molecular remission.

## 9. Inheritance and population

Inheritance is autosomal recessive. Penetrance for individuals with two severe pathogenic alleles appears high, but allele-specific penetrance has not been quantified. Expressivity is markedly variable. Anticipation is not expected; no repeat-expansion mechanism exists. Germline mosaicism is theoretically possible but not established as a recurrent feature. (costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 1-2)

The estimated prevalence is **<1 per 1,000,000**. A 2021 review found 70 published patients—41 lethal and 29 nonlethal—while a 2024 paper summarized 42 variants. Neither statistic represents incidence or a complete global registry. Consanguinity is recurrent in autosomal-recessive case literature, but no population-specific founder allele, carrier frequency, geographic hotspot, sex ratio, or robust incidence estimate was identified. (costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 1-2)

## 10. Diagnostics

### Recommended approach

1. **Clinical recognition:** congenital craniofacial phenotype, osteosclerosis, intracranial calcification, choanal obstruction, neonatal respiratory compromise, or—later—hypophosphatemia with osteosclerosis plus enamel/dentin and gingival abnormalities.
2. **Imaging:** prenatal ultrasound; fetal MRI where available; postnatal skeletal survey/radiographs; low-dose cranial CT when calcification detection is essential; brain MRI for anatomy; renal ultrasound for nephrocalcinosis.
3. **Biochemistry:** phosphate/FGF23 and mineral metabolism panel as described above.
4. **Molecular confirmation:** sequencing and deletion/duplication analysis of FAM20C. A skeletal-dysplasia, craniosynostosis, hypophosphatemia, or amelogenesis-imperfecta panel is reasonable. WES/WGS is appropriate when the phenotype is atypical or panel testing is negative.
5. **Family studies:** parental segregation, carrier testing, and testing of at-risk siblings. (palmalara2023potentialroleof pages 26-27, palmalara2021fam20coverviewclassic pages 1-2, costa2024gingivalproteomicsreveals pages 2-3)

Sanger single-gene testing is useful for a known familial variant. CMA can detect larger 7p22 deletions but may miss sequence variants; karyotyping and FISH are not first-line unless a structural rearrangement is suspected. Mitochondrial, repeat-expansion, liquid-biopsy, proteomic, and methylation testing are not established diagnostic methods. No validated clinical scoring criteria or biochemical biomarker with known sensitivity/specificity exists.

### Differential diagnosis

Important alternatives include other osteosclerosing dysplasias and craniotubular disorders, osteopetrosis, pyknodysostosis, dysosteosclerosis, infantile hypophosphatasia, congenital infections and interferonopathies causing intracranial calcification, primary familial brain calcification, hypophosphatemic rickets syndromes, and enamel-renal syndrome due to FAM20A. The combination of biallelic FAM20C variants with osteosclerosis, cerebral calcification, craniofacial dysplasia, and dental/phosphate abnormalities is distinguishing.

Suggested MAXO actions: *molecular genetic testing*, *exome sequencing*, *genome sequencing*, *deletion/duplication analysis*, *prenatal ultrasound*, *fetal MRI*, *skeletal radiography*, *cranial CT*, *brain MRI*, and *serum phosphate measurement*.

## 11. Outcome and prognosis

The classic form often causes death within the first weeks from pulmonary hypoplasia and respiratory failure. No reliable 5- or 10-year survival estimate exists. Survivors may live into adulthood but can experience chronic rickets/osteomalacia, impaired growth or mobility, bone pain, neurodevelopmental disability, seizures, sensory impairment, and extensive dental/periodontal morbidity. (palmalara2021fam20coverviewclassic pages 1-2, costa2024gingivalproteomicsreveals pages 2-3)

Likely adverse prognostic indicators are severe prenatal osteosclerosis, pulmonary hypoplasia, major airway obstruction, multisuture craniosynostosis, extensive brain abnormalities, and variants leaving little or no kinase activity. Residual function is generally associated with nonlethal disease, but individual prognosis should not be inferred from variant class alone. No validated prognostic biomarker or disease-specific patient-reported outcome measure exists. (costa2024gingivalproteomicsreveals pages 1-2, palmalara2021fam20coverviewclassic pages 16-17)

## 12. Treatment and current applications

There is no approved curative or FAM20C-directed therapy, published treatment algorithm, or disease-specific pharmacogenomic guideline.

- **Neonatal care:** airway stabilization, respiratory support, management of choanal obstruction, feeding support, and palliative-care involvement when disease is lethal.
- **Metabolic bone care:** individualized phosphate and active-vitamin-D management may be considered for FGF23-mediated hypophosphatemia, with close monitoring of calcium, PTH, urine calcium, renal function, and nephrocalcinosis. Human response rates specific to Raine syndrome are unavailable.
- **Dental/periodontal care:** preventive dentistry, restoration/prosthodontics as appropriate, treatment of gingival overgrowth and periodontitis, and multidisciplinary management of amelogenesis imperfecta.
- **Developmental care:** physical, occupational, speech/feeding, hearing, vision, and neurological services.
- **Surgery:** individualized correction of choanal atresia, craniosynostosis, cleft palate, or severe orthopedic deformity; disease-specific outcome series are absent.

Suggested MAXO terms include *respiratory support*, *assisted ventilation*, *phosphate supplementation*, *active vitamin D therapy*, *dental surveillance*, *periodontal treatment*, *physical therapy*, *occupational therapy*, *speech therapy*, *hearing assessment*, *vision assessment*, and *genetic counseling*.

In Fam20c-deficient mice, a high-phosphate diet improved long-bone shape and mineral density and nearly normalized growth-plate widening. The abstract concludes: **“These results suggested that the hPi diet significantly improved the skeletal development of the Fam20c-deficient mice, implying that hypophosphatemia partially contributed to the skeletal defects.”** This is preclinical evidence and does not establish safety or efficacy in humans. [Published February 2020; DOI: https://doi.org/10.1159/000506005]. (zhang2020highphosphatedietimproved pages 11-12)

A ClinicalTrials.gov search found no trial whose condition was genuinely Raine syndrome; records using “RNS” for neuromodulation were acronym collisions. Gene replacement, CRISPR editing, RNA therapies, cell therapies, immunotherapy, and anti-FGF23 therapy remain unvalidated for this disease.

## 13. Prevention

The genotype cannot be prevented by lifestyle or vaccination. Evidence-based prevention is reproductive and complication-directed:

- carrier and cascade testing after a molecular diagnosis;
- genetic counseling with 25% recurrence-risk discussion for carrier couples;
- targeted prenatal diagnosis by chorionic-villus sampling or amniocentesis;
- preimplantation genetic testing for a known familial variant;
- detailed prenatal imaging in at-risk pregnancies;
- early respiratory, phosphate, renal, dental, hearing, vision, and developmental surveillance;
- tertiary prevention of rickets, nephrocalcinosis, dental infection, periodontal disease, contractures, and developmental complications.

Population newborn biochemical screening is not available. Expanded genomic screening could detect FAM20C variants, but interpretation, prevalence, and clinical utility have not been established.

## 14. Other species and natural disease

No well-established naturally occurring veterinary analogue or zoonotic form was identified. FAM20C orthologues are evolutionarily conserved across vertebrates, and related secretory-pathway kinase activity also exists in Drosophila. Comparative data support conservation of extracellular phosphoprotein and biomineralization biology, but experimental models should not be described as naturally transmitted disease. Suggested taxonomy terms include *Homo sapiens* and *Mus musculus*; the exact NCBI Gene identifiers should be verified in NCBI Gene before database ingestion.

## 15. Model organisms and experimental systems

**Mouse:** global or conditional Fam20c deficiency reproduces hypophosphatemia, elevated FGF23, rickets/osteomalacia-like skeletal defects, abnormal dentin/enamel, and intracranial calcification. The 2023 study specifically showed that intracranial calcification in Fam20c-deficient mice recapitulates a defining human feature. [Neuroscience Letters, April 2023; DOI: https://doi.org/10.1016/j.neulet.2023.137176]. These models are useful for phosphate physiology, mineralized tissues, brain calcification, and preclinical dietary interventions, but they do not capture the full human lethal craniofacial/respiratory spectrum. (palmalara2023potentialroleof pages 1-2, zhang2020highphosphatedietimproved pages 11-12)

**Human cell systems:** primary gingival fibroblasts and siRNA-mediated FAM20C knockdown model ECM disorganization and the TGFβ–YAP/TAZ fibrotic loop. Their strength is direct patient relevance; limitations include only two genotypes and one tissue lineage. (costa2024gingivalproteomicsreveals pages 2-3, costa2024gingivalproteomicsreveals pages 1-2)

**In-vitro kinase systems:** recombinant FAM20C experiments establish phosphorylation of secreted biomineralization proteins and show that disease-associated substitutions impair localization or kinase activity. This supplies biochemical causality but cannot alone predict organismal severity. The foundational abstract states: **“Our results identify FAM20C as a kinase for secreted phosphoproteins and establish a biochemical basis for Raine syndrome.”** [Published 13 August 2012; DOI: https://doi.org/10.1371/journal.pone.0042988]. (palmalara2023potentialroleof pages 1-2)

## Evidence appraisal and knowledge gaps

The strongest conclusions are the biallelic FAM20C etiology, autosomal-recessive inheritance, core skeletal/craniofacial/calcification phenotype, and secretory-pathway kinase mechanism. Major limitations are extreme rarity, case-report ascertainment, inconsistent laboratory reporting, incomplete functional characterization of variants, and the absence of registries, controlled treatment trials, standardized diagnostic criteria, longitudinal quality-of-life data, or validated prognostic models. The 2023–2024 studies materially advance mechanism but do not yet change standard clinical care. (costa2024gingivalproteomicsreveals pages 1-2, costa2024gingivalproteomicsreveals pages 2-3, palmalara2023potentialroleof pages 1-2)

### Key recent and foundational sources

- Costa et al. **Gingival proteomics reveals the role of TGF beta and YAP/TAZ signaling in Raine syndrome fibrosis.** *Scientific Reports*. Published April 2024. https://doi.org/10.1038/s41598-024-59713-0. (costa2024gingivalproteomicsreveals pages 2-3, costa2024gingivalproteomicsreveals pages 1-2)
- Zhang et al. **Intracranial calcification in Fam20c-deficient mice recapitulates human Raine syndrome.** *Neuroscience Letters*. Published April 2023. https://doi.org/10.1016/j.neulet.2023.137176. (palmalara2023potentialroleof pages 1-2)
- Palma-Lara et al. **Potential Role of Protein Kinase FAM20C on the Brain in Raine Syndrome, an In Silico Analysis.** *International Journal of Molecular Sciences*. Published 17 May 2023. https://doi.org/10.3390/ijms24108904. (palmalara2023potentialroleof pages 1-2)
- Palma-Lara et al. **FAM20C Overview: Classic and Novel Targets, Pathogenic Variants and Raine Syndrome Phenotypes.** *International Journal of Molecular Sciences*. Published July 2021. https://doi.org/10.3390/ijms22158039. (palmalara2021fam20coverviewclassic pages 16-17, palmalara2021fam20coverviewclassic pages 1-2)
- Ishikawa et al. **The Raine Syndrome Protein FAM20C Is a Golgi Kinase That Phosphorylates Bio-Mineralization Proteins.** *PLOS ONE*. Published 13 August 2012. https://doi.org/10.1371/journal.pone.0042988. (palmalara2023potentialroleof pages 1-2)

PMIDs were not exposed in the retrieved records for these papers; DOIs and publication dates are therefore supplied rather than risking incorrect PMID assignment.

References

1. (costa2024gingivalproteomicsreveals pages 1-2): Cláudio Rodrigues Rezende Costa, Rym Chalgoumi, Amina Baker, Clément Guillou, Paulo Marcio Yamaguti, Victor Simancas Escorcia, Lilia Abbad, Bruna Rabelo Amorin, Caroline Lourenço de Lima, Vidjea Cannaya, Mourad Benassarou, Ariane Berdal, Christos Chatziantoniou, Olivier Cases, Pascal Cosette, Renata Kozyraki, and Ana Carolina Acevedo. Gingival proteomics reveals the role of tgf beta and yap/taz signaling in raine syndrome fibrosis. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-59713-0, doi:10.1038/s41598-024-59713-0. This article has 5 citations and is from a peer-reviewed journal.

2. (palmalara2021fam20coverviewclassic pages 1-2): Icela Palma-Lara, Monserrat Pérez-Ramírez, Patricia García Alonso-Themann, Ana María Espinosa-García, Ricardo Godinez-Aguilar, José Bonilla-Delgado, Adolfo López-Ornelas, Georgina Victoria-Acosta, María Guadalupe Olguín-García, José Moreno, and Carmen Palacios-Reyes. Fam20c overview: classic and novel targets, pathogenic variants and raine syndrome phenotypes. International Journal of Molecular Sciences, 22:8039, Jul 2021. URL: https://doi.org/10.3390/ijms22158039, doi:10.3390/ijms22158039. This article has 35 citations.

3. (palmalara2023potentialroleof pages 1-2): Icela Palma-Lara, Patricia García Alonso-Themann, Javier Pérez-Durán, Ricardo Godínez-Aguilar, José Bonilla-Delgado, Damián Gómez-Archila, Ana María Espinosa-García, Manuel Nolasco-Quiroga, Georgina Victoria-Acosta, Adolfo López-Ornelas, Juan Carlos Serrano-Bello, María Guadalupe Olguín-García, and Carmen Palacios-Reyes. Potential role of protein kinase fam20c on the brain in raine syndrome, an in silico analysis. International Journal of Molecular Sciences, 24:8904, May 2023. URL: https://doi.org/10.3390/ijms24108904, doi:10.3390/ijms24108904. This article has 3 citations.

4. (costa2024gingivalproteomicsreveals pages 2-3): Cláudio Rodrigues Rezende Costa, Rym Chalgoumi, Amina Baker, Clément Guillou, Paulo Marcio Yamaguti, Victor Simancas Escorcia, Lilia Abbad, Bruna Rabelo Amorin, Caroline Lourenço de Lima, Vidjea Cannaya, Mourad Benassarou, Ariane Berdal, Christos Chatziantoniou, Olivier Cases, Pascal Cosette, Renata Kozyraki, and Ana Carolina Acevedo. Gingival proteomics reveals the role of tgf beta and yap/taz signaling in raine syndrome fibrosis. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-59713-0, doi:10.1038/s41598-024-59713-0. This article has 5 citations and is from a peer-reviewed journal.

5. (OpenTargets Search: Raine syndrome-FAM20C): Open Targets Query (Raine syndrome-FAM20C, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (palmalara2021fam20coverviewclassic pages 16-17): Icela Palma-Lara, Monserrat Pérez-Ramírez, Patricia García Alonso-Themann, Ana María Espinosa-García, Ricardo Godinez-Aguilar, José Bonilla-Delgado, Adolfo López-Ornelas, Georgina Victoria-Acosta, María Guadalupe Olguín-García, José Moreno, and Carmen Palacios-Reyes. Fam20c overview: classic and novel targets, pathogenic variants and raine syndrome phenotypes. International Journal of Molecular Sciences, 22:8039, Jul 2021. URL: https://doi.org/10.3390/ijms22158039, doi:10.3390/ijms22158039. This article has 35 citations.

7. (costa2024gingivalproteomicsreveals pages 21-22): Cláudio Rodrigues Rezende Costa, Rym Chalgoumi, Amina Baker, Clément Guillou, Paulo Marcio Yamaguti, Victor Simancas Escorcia, Lilia Abbad, Bruna Rabelo Amorin, Caroline Lourenço de Lima, Vidjea Cannaya, Mourad Benassarou, Ariane Berdal, Christos Chatziantoniou, Olivier Cases, Pascal Cosette, Renata Kozyraki, and Ana Carolina Acevedo. Gingival proteomics reveals the role of tgf beta and yap/taz signaling in raine syndrome fibrosis. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-59713-0, doi:10.1038/s41598-024-59713-0. This article has 5 citations and is from a peer-reviewed journal.

8. (zhang2020highphosphatedietimproved pages 11-12): Hua Zhang, Lili Li, Matthew J. Kesterke, Yongbo Lu, and Chunlin Qin. High-phosphate diet improved the skeletal development of fam20c-deficient mice. Cells Tissues Organs, 208:25-36, Feb 2020. URL: https://doi.org/10.1159/000506005, doi:10.1159/000506005. This article has 8 citations and is from a peer-reviewed journal.

9. (palmalara2023potentialroleof pages 26-27): Icela Palma-Lara, Patricia García Alonso-Themann, Javier Pérez-Durán, Ricardo Godínez-Aguilar, José Bonilla-Delgado, Damián Gómez-Archila, Ana María Espinosa-García, Manuel Nolasco-Quiroga, Georgina Victoria-Acosta, Adolfo López-Ornelas, Juan Carlos Serrano-Bello, María Guadalupe Olguín-García, and Carmen Palacios-Reyes. Potential role of protein kinase fam20c on the brain in raine syndrome, an in silico analysis. International Journal of Molecular Sciences, 24:8904, May 2023. URL: https://doi.org/10.3390/ijms24108904, doi:10.3390/ijms24108904. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](Raine_Syndrome-deep-research-falcon_artifacts/artifact-00.md)