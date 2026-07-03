---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-30T01:30:29.501599'
end_time: '2026-05-30T01:38:39.620093'
duration_seconds: 490.12
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: 46,XX testicular disorder of sex development
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: 46_XX_Testicular_DSD-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 46,XX testicular disorder of sex development
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **46,XX testicular disorder of sex development** covering all of the
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
- **Disease Name:** 46,XX testicular disorder of sex development
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **46,XX testicular disorder of sex development** covering all of the
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


# 46,XX Testicular Disorder of Sex Development (46,XX T-DSD): Disease Characteristics Research Report

## Target disease
**Disease name:** 46,XX testicular disorder of sex development (46,XX testicular DSD; “XX male syndrome”).

**Note on identifiers (OMIM/Orphanet/MONDO/MeSH/ICD):** In this tool-run, primary ontology/registry pages (OMIM/Orphanet/MONDO/ICD/MeSH) were not directly retrievable as citable full-text sources. Consequently, identifier assertions are not provided here to avoid uncited/uncertain mappings. The report below is built from peer‑reviewed primary literature and recent reviews.

---

## 1. Disease information

### 1.1 Concise overview
46,XX testicular DSD is a rare condition in which an individual with a **46,XX karyotype** develops **testicular tissue** and typically a **male or undervirilized male phenotype**. It is commonly diagnosed after puberty/adulthood during evaluation for infertility and/or hypogonadism. (terribile201946xxtesticulardisorder pages 1-3, ferrari2024testiculardifferentiationin pages 1-2)

### 1.2 Synonyms / alternative names
Frequently used names include **“46,XX testicular DSD,” “46,XX male syndrome,” “XX male syndrome,”** and, in newer nomenclature, **“46,XX testicular difference of sex development.”** (li201446xxtesticulardisorder pages 1-2, terribile201946xxtesticulardisorder pages 1-3)

### 1.3 Evidence source type
Most evidence for this condition derives from **aggregated case series and systematic reviews** (adult infertility presentations) plus **single‑center pediatric cohorts** for early/ambiguous genitalia presentations, and mechanistic inference from human genetics and animal models. (terribile201946xxtesticulardisorder pages 1-3, gong2025retrospectiveanalysisof pages 1-2, ferrari2024testiculardifferentiationin pages 2-4)

---

## 2. Etiology

### 2.1 Primary causal factors (genetic/mechanistic)
The disease is primarily genetic and arises from dysregulation of the early gonadal sex‑determination network, which can be conceptualized as competition between:
- a **pro‑testis pathway** centered on **SRY → SOX9** activation and reinforcement; and
- a **pro‑ovary/anti‑testis pathway** centered on **RSPO1/WNT4/β‑catenin (CTNNB1)** and **FOXL2**. (ferrari2024testiculardifferentiationin pages 2-4, abalı2024diagnosisandmanagement pages 1-2)

#### A. SRY translocation (most common)
A large fraction of 46,XX testicular DSD is due to **translocation of Y‑chromosomal material including SRY** (typically to Xp or an autosome), which triggers testis determination despite an XX karyotype. Reviews commonly report **~80–90% SRY‑positive**. (terribile201946xxtesticulardisorder pages 7-9, terribile201946xxtesticulardisorder pages 1-3)

Direct abstract quote (systematic review context): “The patients generally have normal external genitalia and discover their pathology in adulthood because of infertility… The sex-determining region Y (SRY) gene was detected in 51/57 cases.” (Terribile 2019, Medicina; published 2019-07; URL https://doi.org/10.3390/medicina55070371) (terribile201946xxtesticulardisorder pages 1-3)

#### B. SRY‑negative mechanisms (minority, heterogeneous)
SRY‑negative 46,XX testicular/ovotesticular DSD is attributed to **(i) gain of function/overexpression of pro‑testis genes** or **(ii) loss of function of pro‑ovary/anti‑testis genes**, though many cases remain unsolved. (ferrari2024testiculardifferentiationin pages 2-4, abalı2024diagnosisandmanagement pages 1-2)

Direct abstract quotes supporting these two broad categories:
- “SRY-negative 46,XX males show overexpression of pro-testis genes, such as SOX9 and SOX3, or failure of pro-ovarian genes, such as WNT4 and RSPO1, which induces testis differentiation…” (Wei 2022, BMC Med Genomics; published 2022-09; URL https://doi.org/10.1186/s12920-022-01347-0) (wei2022duplicationofsox3 pages 1-3)
- “Genes associated with 46,XX T/OT-DSD include translocations of the SRY; copy number variants in NR2F2, NR0B1, SOX3, SOX9, SOX10, and FGF9, and sequence variants in NR5A1, NR2F2, RSPO1, SOX9, WNT2B, WNT4, and WT1.” (Abalı & Guran 2024, Front Endocrinol; published 2024-05; URL https://doi.org/10.3389/fendo.2024.1354759) (abalı2024diagnosisandmanagement pages 1-2)

#### C. Copy-number variants / structural variation affecting SOX genes
SRY‑negative cases can result from structural variants affecting gene dosage/regulatory architecture of **SOX genes** (e.g., SOX3 duplication). A reported SRY‑negative case had a **1.4 Mb duplication involving SOX3**, with a recommendation to screen SOX3 in SRY‑negative XX males. (wei2022duplicationofsox3 pages 1-3)

#### D. NR5A1 (SF‑1) recurrent variant as a molecular “switch”
A key non‑SRY mechanism is the recurrent **NR5A1 p.Arg92Trp** variant, which has been identified in multiple unrelated 46,XX (ovo)testicular DSD individuals after excluding SRY translocation and CNVs. (baetens2017nr5a1isa pages 1-2, bashamboo2016arecurrentp.arg92trp pages 1-3)

Direct abstract quote: “A recurrent p.Arg92Trp variant in steroidogenic factor-1 (NR5A1) can act as a molecular switch in human sex development.” (Bashamboo 2016, Hum Mol Genet; published 2016-07; URL https://doi.org/10.1093/hmg/ddw186) (bashamboo2016arecurrentp.arg92trp pages 1-3)

Mechanistic interpretation from a Genetics in Medicine study: the variant is hypothesized to bias fate by “decreased inhibition of the male developmental pathway through downregulation of female antitestis genes,” tipping the balance toward testicular differentiation in 46,XX individuals. (Baetens 2017, Genet Med; published 2017-04; URL https://doi.org/10.1038/gim.2016.118) (baetens2017nr5a1isa pages 1-2)

### 2.2 Risk factors
**Genetic risk factor:** presence of SRY translocation or pathogenic variants/CNVs in the sex‑determination network genes noted above is causal rather than merely predisposing. (terribile201946xxtesticulardisorder pages 7-9, abalı2024diagnosisandmanagement pages 1-2)

**Environmental risk factors:** For 46,XX *testicular* DSD specifically, the dominant causes are genetic; exogenous androgen exposure more strongly pertains to other 46,XX DSD categories (e.g., CAH or maternal androgen exposure), rather than XX testicular differentiation. (abalı2024diagnosisandmanagement pages 1-2)

### 2.3 Protective factors / gene–environment interactions
No specific protective factors or gene–environment interactions are established for XX testicular DSD in the sources retrieved here.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (with suggested HPO terms)
Phenotype is variable, ranging from typical male external genitalia to ambiguous genitalia, often with gonadal dysgenesis and infertility.

Commonly reported features include:
- **Azoospermia / infertility** (HP:0000027 Azoospermia; HP:0000789 Infertility) (li201446xxtesticulardisorder pages 1-2, terribile201946xxtesticulardisorder pages 1-3)
- **Hypergonadotropic hypogonadism / primary testicular failure** (HP:0000044 Hypogonadotropic hypogonadism is *not* appropriate; consider HP:0000044?; better: HP:0000035 Hypergonadotropic hypogonadism; HP:0000035; and lab: increased LH/FSH) (terribile201946xxtesticulardisorder pages 7-9, li201446xxtesticulardisorder pages 1-2)
- **Small testes / microorchidism** (HP:0000028 Microorchidism; HP:0000007 Cryptorchidism) (terribile201946xxtesticulardisorder pages 7-9, li201446xxtesticulardisorder pages 1-2)
- **Hypospadias** (HP:0000047 Hypospadias) (terribile201946xxtesticulardisorder pages 7-9, li201446xxtesticulardisorder pages 1-2)
- **Gynecomastia** (HP:0000774 Gynecomastia) (terribile201946xxtesticulardisorder pages 7-9, li201446xxtesticulardisorder pages 1-2)
- **Residual Müllerian structures / prostatic utricle (subset, especially SRY-negative/undervirilized)** (HP:0000132 Abnormality of uterus / persistent Müllerian structures; note this is phenotype-dependent) (wei2022duplicationofsox3 pages 1-3, terribile201946xxtesticulardisorder pages 9-11)

Direct abstract quote summarizing the common adult presentation pattern: “The patients generally have normal external genitalia and discover their pathology in adulthood because of infertility.” (Terribile 2019; URL https://doi.org/10.3390/medicina55070371) (terribile201946xxtesticulardisorder pages 1-3)

### 3.2 Age of onset and progression
- **Congenital onset** at gonadal differentiation (fetal), but **ascertainment** is often later.
- Ferrari et al. summarize that ~80% have typical male genitalia at birth with diagnosis often after puberty due to gynecomastia/hypogonadism/infertility. (ferrari2024testiculardifferentiationin pages 1-2)
- A subset presents in infancy/childhood with ambiguous genitalia; in a pediatric cohort the median age at first presentation was **18 months**. (gong2025retrospectiveanalysisof pages 1-2)

### 3.3 Frequency / statistics from published cohorts
From an adult systematic review (selected phenotypes across published cases):
- cryptorchidism (~15%) and anterior hypospadias (~10%) were cited as non‑rare genital findings; hypergonadotropic hypogonadism was common. (terribile201946xxtesticulardisorder pages 7-9)

Pediatric single‑center cohort (46,XX testicular/ovotesticular DSD; n=52):
- median age at presentation: **18 months**
- SRY in peripheral blood: **4/52**; SRY in tissue (tested n=8): **0/8**
- gonadal biopsy performed: **47/52**; most frequent pathology: **bilateral seminiferous tubules 17/47**
- tumor marker: OCT3/4 positive **2/16** by immunohistochemistry; no tumors observed in biopsies
- male‑reared adolescents: puberty onset ~**12 ± 0.87 years**; basal LH **6.44 ± 4.19 IU/L**, FSH **13.18 ± 10.22 IU/L**, testosterone **3.40 ± 1.63 nmol/L** (gong2025retrospectiveanalysisof pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes and variant classes (evidence-based list)
Evidence-supported genes implicated in 46,XX testicular/ovotesticular DSD across the retrieved 2024 review literature include:
- **SRY** (usually via translocation) (terribile201946xxtesticulardisorder pages 7-9, abalı2024diagnosisandmanagement pages 1-2)
- **NR5A1 (SF-1)** sequence variants (notably **p.Arg92Trp**) (baetens2017nr5a1isa pages 1-2, bashamboo2016arecurrentp.arg92trp pages 1-3)
- **SOX9 / SOX3 / SOX10** CNVs/structural variants causing overexpression/positional effects (wei2022duplicationofsox3 pages 1-3, abalı2024diagnosisandmanagement pages 1-2)
- **RSPO1, WNT4** loss-of-function in the pro-ovary pathway (ferrari2024testiculardifferentiationin pages 2-4, abalı2024diagnosisandmanagement pages 1-2)
- Other genes named in reviews: **NR2F2, NR0B1, FGF9, WT1, WNT2B** (abalı2024diagnosisandmanagement pages 1-2)

### 4.2 Mechanistic chain (current understanding)
A simplified causal chain:
1. **Primary genetic change**: (a) SRY translocation or (b) SRY-independent activation of SOX9 (via SOX gene dosage/NR5A1 changes) or (c) impaired ovarian-maintenance signaling (RSPO1/WNT4/β‑catenin/FOXL2). (ferrari2024testiculardifferentiationin pages 2-4, abalı2024diagnosisandmanagement pages 1-2, baetens2017nr5a1isa pages 1-2)
2. **Cell fate shift** in fetal bipotential gonad: increased Sertoli-lineage program (SOX9/FGF9/PGD2 reinforcement) and/or reduced granulosa/ovary program. (ferrari2024testiculardifferentiationin pages 2-4, hattori2023nuclearreceptorgene pages 1-3)
3. **Testicular tissue differentiation** (often dysgenetic) → androgen/AMH signaling patterns that shape internal/external genital development.
4. **Postnatal outcomes**: variable genital phenotype; progressive primary testicular failure leading to hypergonadotropic hypogonadism and infertility/azoospermia. (terribile201946xxtesticulardisorder pages 7-9, li201446xxtesticulardisorder pages 1-2)

### 4.3 Variant interpretation and “unknowns”
A substantial fraction of SRY-negative cases remain without a molecular diagnosis, suggesting unrecognized genetic/epigenetic mechanisms. Ferrari 2024 emphasizes that “a significant number of patients… have not yet recognized a genetic diagnosis.” (Ferrari 2024; URL https://doi.org/10.3389/fendo.2024.1385901) (ferrari2024testiculardifferentiationin pages 1-2)

---

## 5. Environmental information
Environmental causes are not a primary driver for 46,XX *testicular* DSD in the retrieved literature. Reviews of non‑CAH 46,XX DSD focus mainly on genetic etiologies and distinguish androgen‑excess disorders (CAH, aromatase deficiency, glucocorticoid resistance) from testicular/ovotesticular differentiation disorders. (abalı2024diagnosisandmanagement pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Pathways (suggested pathway/ontology anchors)
Key antagonistic modules:
- **Pro-testis module:** SRY → SOX9; reinforced by FGF9 and PGD2; includes NR5A1 as a core gonadal regulator. (ferrari2024testiculardifferentiationin pages 2-4, hattori2023nuclearreceptorgene pages 1-3)
- **Pro-ovary/anti-testis module:** RSPO1/WNT4 → β‑catenin (CTNNB1); FOXL2 required for ovarian development/maintenance. (ferrari2024testiculardifferentiationin pages 2-4)

Suggested GO biological process terms (examples for knowledge base annotation):
- GO:0007530 **sex determination**
- GO:0007281 **germ cell development**
- GO:0007548 **sex differentiation**
- GO:0001701 **in utero embryonic development**

Suggested Cell Ontology (CL) terms:
- CL:0000011 **Sertoli cell**
- CL:0000178 **Leydig cell**
- CL:0002338 **granulosa cell**

### 6.2 Tumor biology / surveillance markers
In a pediatric cohort (n=52), gonadal biopsy showed **no tumors**, but **OCT3/4 positivity** (a germ‑cell tumor risk marker) was observed in **2/16** tested by immunohistochemistry, suggesting the need for individualized tumor-risk assessment in some cases. (gong2025retrospectiveanalysisof pages 1-2)

---

## 7. Anatomical structures affected

### 7.1 Primary organs and structures
- **Gonads (testes/ovotestes, often dysgenetic)** (UBERON:0000473 testis; UBERON:0000992 ovary—coexistence in OT‑DSD)
- **Internal genital tract** may include variable Müllerian remnants (uterus/fallopian tubes) in some SRY-negative/ambiguous presentations. (terribile201946xxtesticulardisorder pages 9-11, wei2022duplicationofsox3 pages 1-3)
- **External genitalia** range from typical male to ambiguous (hypospadias, micropenis). (terribile201946xxtesticulardisorder pages 7-9, gong2025retrospectiveanalysisof pages 1-2)

---

## 8. Temporal development (natural history)
While gonadal fate is determined prenatally, ascertainment is typically:
- **Adolescence/adulthood** due to infertility/hypogonadism/gynecomastia in those with typical male genitalia. (terribile201946xxtesticulardisorder pages 1-3, ferrari2024testiculardifferentiationin pages 1-2)
- **Infancy/childhood** in those with ambiguous genitalia/hypospadias/cryptorchidism. (gong2025retrospectiveanalysisof pages 1-2)

A typical trajectory includes progressive testicular dysfunction with hypergonadotropic hypogonadism and infertility/azoospermia. (terribile201946xxtesticulardisorder pages 7-9, li201446xxtesticulardisorder pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology
- Incidence is commonly cited as **~1:20,000–25,000 newborn males**. (luo2026raresrynegative46xx pages 4-5, terribile201946xxtesticulardisorder pages 1-3, ferrari2024testiculardifferentiationin pages 1-2)
- Ferrari 2024 further reports it accounts for **~2% of male infertility**. (ferrari2024testiculardifferentiationin pages 1-2)

### 9.2 Inheritance pattern
Most SRY+ cases are typically **sporadic de novo chromosomal rearrangements** (SRY translocation during paternal meiosis) rather than classical Mendelian inheritance. (terribile201946xxtesticulardisorder pages 7-9)

Some SRY-negative genetic causes can follow Mendelian inheritance patterns depending on the gene (e.g., recessive RSPO1/WNT4-related syndromes versus de novo CNVs), but inheritance details vary by molecular diagnosis and were not comprehensively quantifiable from the retrieved excerpts. (abalı2024diagnosisandmanagement pages 14-14, abalı2024diagnosisandmanagement pages 1-2)

---

## 10. Diagnostics

### 10.1 Core diagnostic approach (real-world implementation)
**Clinical and endocrine evaluation** plus mandatory **cytogenetic/genetic** workup is standard:
- **Semen analysis and karyotype** are emphasized as key initial tests in adults presenting with infertility. (terribile201946xxtesticulardisorder pages 9-11, terribile201946xxtesticulardisorder pages 1-3)
- **SRY detection** via **PCR and/or FISH** is used to classify SRY+ vs SRY− cases and can guide downstream testing. (terribile201946xxtesticulardisorder pages 9-11, li201446xxtesticulardisorder pages 1-2)
- **Abdominal/pelvic ultrasound** is used to evaluate for residual Müllerian structures. (terribile201946xxtesticulardisorder pages 9-11, terribile201946xxtesticulardisorder pages 1-3)

### 10.2 Recommended genetic testing workflow (DSD best practice)
A widely cited expert position paper (EU COST DSDnet) supports a stepwise approach:
- “Ascertainment of the karyotpye defines one of the three major diagnostic DSD subclasses and is therefore the mandatory initial step.” (Audí 2018, Eur J Endocrinol; published 2018-10; URL https://doi.org/10.1530/eje-18-0256) (audı2018geneticsinendocrinology pages 1-6)
- After karyotype: molecular testing for monogenic causes and/or CNVs; panels are increasingly used early; WES/WGS are transitioning into routine and also enable novel-gene discovery but require cautious interpretation. (audı2018geneticsinendocrinology pages 6-9, audı2018geneticsinendocrinology pages 1-6)

A newborn-focused review also emphasizes modern implementation choices:
- targeted **NGS gene panels** for coverage/limited incidental findings; escalation to **WES/WGS** for complex cases; and that trio WES can increase diagnostic yield. (ibba2022differencesofsex pages 18-21)

### 10.3 Differential diagnosis
Key distinctions:
- **46,XX DSD due to androgen excess** (e.g., CAH) typically has **normal ovarian development** and differs mechanistically from XX testicular differentiation. (abalı2024diagnosisandmanagement pages 1-2)
- **Ovotesticular DSD (46,XX OT‑DSD)** overlaps substantially and may be part of the same mechanistic spectrum; Ferrari 2024 cites OT‑DSD as rare (~1:100,000 births) and most often 46,XX (65–90%). (ferrari2024testiculardifferentiationin pages 2-4)

---

## 11. Outcome / prognosis

### 11.1 Survival and mortality
No disease-specific mortality signal is emphasized in the retrieved excerpts; the major morbidity is reproductive/endocrine.

### 11.2 Morbidity and functional outcomes
- **Fertility:** azoospermia is common; fertility is typically severely impaired. (li201446xxtesticulardisorder pages 1-2, terribile201946xxtesticulardisorder pages 1-3)
- **Endocrine:** progressive testicular failure and hypergonadotropic hypogonadism are common, requiring monitoring and sometimes hormone therapy. (terribile201946xxtesticulardisorder pages 7-9, gong2025retrospectiveanalysisof pages 1-2)
- **Psychosocial/quality of life:** DSD care guidelines emphasize multidisciplinary management, but validated QoL measures specific to 46,XX T‑DSD were not extractable from the retrieved sources.

---

## 12. Treatment

### 12.1 Management principles (current practice)
There are no disease‑modifying molecular therapies in routine clinical care; management is supportive and individualized.

**Infertility counseling / assisted reproduction:**
- “Testicular sperm extraction is not recommended, and adoption or in vitro fertilization with a sperm donor are fertility options.” (Terribile 2019; URL https://doi.org/10.3390/medicina55070371) (terribile201946xxtesticulardisorder pages 7-9)

**Endocrine management:**
- monitor for puberty/testosterone insufficiency and hypergonadotropic hypogonadism; in pediatric cohorts, early gonadectomy in female-reared children prevents spontaneous puberty and can necessitate sex-hormone replacement planning. (gong2025retrospectiveanalysisof pages 1-2)

**Surgical management (when indicated):**
- repair of hypospadias/cryptorchidism; management of Müllerian remnants/prostatic utricle in specific anatomic presentations; endoscopic evaluation was recommended preoperatively for detecting prostatic utricle in SRY‑negative cases. (wei2022duplicationofsox3 pages 1-3)

**Tumor-risk assessment:**
- individualized; pediatric series found no tumors on biopsy but OCT3/4 positivity in a minority. (gong2025retrospectiveanalysisof pages 1-2)

Suggested MAXO terms (examples for knowledge base mapping):
- MAXO:0000058 **hormone replacement therapy**
- MAXO:0001176 **genetic counseling**
- MAXO:0001020 **orchidopexy**
- MAXO:0001095 **hypospadias repair**
- MAXO:0000931 **gonadectomy** (select cases)

### 12.2 Clinical trials
A clinicaltrials.gov search identified no interventional trials specifically targeting 46,XX testicular DSD; retrieved trials were not disease‑specific (e.g., decision-support for parents of children with rare disease). (NCT01875640 retrieved, but not specific to 46,XX T‑DSD; tool output)

---

## 13. Prevention
Primary prevention is not currently feasible for most cases because many are de novo chromosomal rearrangements. Secondary/tertiary prevention focuses on:
- early recognition of ambiguous genitalia presentations;
- timely genetic diagnosis to guide anticipatory endocrine follow-up and fertility counseling. (audı2018geneticsinendocrinology pages 6-9, audı2018geneticsinendocrinology pages 1-6)

---

## 14. Other species / natural disease
A naturally occurring XX DSD subtype exists in dogs that is phenotypically similar to the human SRY‑negative XX DSD spectrum. In one study:
- “This is a naturally occurring disorder in humans (Homo sapiens) and dogs (C. familiaris). Phenotypes in the canine XX DSD model are strikingly similar to those of the human XX DSD subtype.” (Meyers‑Wallen 2017, PLoS ONE; published 2017-10; URL https://doi.org/10.1371/journal.pone.0186331) ()

The same study identified a variant upstream of SOX9 and found embryonic gonads had **RSPO1 downregulation**, proposing upstream lesions causing “epigenomic gonadal mosaicism.” ()

*(Note:  was introduced via paper_search results but not previously listed in gathered evidence; therefore it is not citable unless present in context IDs. It is not in the citable list above, so it is not used further.)*

---

## 15. Model organisms
Ferrari 2024 anchors gene-network understanding using mammalian developmental genetics, describing early gonadal ridge formation genes and downstream testis/ovary antagonism. (ferrari2024testiculardifferentiationin pages 2-4)

Beyond descriptive models, the canine XX DSD model provides a naturally occurring system to study SRY‑negative XX testicular/ovotesticular development and the RSPO1/WNT axis. (; not citable here, see note above)

---

# Summary table
The following table provides a compact synthesis of key facts (names, incidence, SRY distribution, presentation, and management).

| Item | Evidence-based details | Key sources (pqac ids) |
|---|---|---|
| Disease names / synonyms | 46,XX testicular disorder of sex development; 46,XX testicular DSD; 46,XX male syndrome; XX male syndrome; 46,XX testicular difference of sex development | (li201446xxtesticulardisorder pages 1-2, terribile201946xxtesticulardisorder pages 1-3, grinspon2016disordersofsex pages 1-2) |
| Epidemiology | Rare condition with reported incidence about 1:20,000-25,000 male newborns; estimated to account for ~2% of male infertility. A pediatric testicular/ovotesticular DSD series cited ~1:100,000 births for the broader childhood TDSD/OTDSD grouping | (luo2026raresrynegative46xx pages 4-5, terribile201946xxtesticulardisorder pages 1-3, ferrari2024testiculardifferentiationin pages 1-2, gong2025retrospectiveanalysisof pages 1-2) |
| SRY-positive vs SRY-negative | Literature commonly reports ~80-90% SRY-positive and ~10-20% SRY-negative among 46,XX testicular DSD cases. In one systematic review, SRY was detected in 51/57 cases, usually on Xp. In a pediatric 52-case TDSD/OTDSD series, SRY-negative cases predominated; only 4/52 had SRY in peripheral blood and 0/8 tissue samples were SRY-positive | (terribile201946xxtesticulardisorder pages 7-9, li201446xxtesticulardisorder pages 1-2, terribile201946xxtesticulardisorder pages 1-3, gong2025retrospectiveanalysisof pages 1-2, wei2022duplicationofsox3 pages 1-3) |
| Typical age / presentation | About 80-90% have typical male external genitalia at birth and are often diagnosed after puberty or in adulthood during infertility workup, hypogonadism, or gynecomastia evaluation. A minority (~15%) present at birth/childhood with ambiguous genitalia, hypospadias, cryptorchidism, or micropenis. In the pediatric single-center cohort, median age at first presentation was 18 months | (terribile201946xxtesticulardisorder pages 7-9, terribile201946xxtesticulardisorder pages 1-3, barseghyan2017identificationofgenetic pages 21-26, gong2025retrospectiveanalysisof pages 1-2, ferrari2024testiculardifferentiationin pages 1-2) |
| Typical phenotype | Common findings include normal male phenotype or variable undervirilization, small testes/microorchidism, azoospermia/infertility, hypergonadotropic hypogonadism, gynecomastia, cryptorchidism, hypospadias, and occasionally residual Müllerian structures or prostatic utricle in SRY-negative cases | (terribile201946xxtesticulardisorder pages 7-9, li201446xxtesticulardisorder pages 1-2, terribile201946xxtesticulardisorder pages 1-3, wei2022duplicationofsox3 pages 1-3) |
| Key management pearls | Recommended evaluation includes careful genital exam, semen analysis, endocrine testing, karyotype, SRY testing by PCR/FISH, and abdominal ultrasound to assess Müllerian remnants; gonadal biopsy may help define gonadal tissue in selected SRY-negative cases. Genetic/endocrine consultation is recommended. TESE is generally not recommended; fertility options include donor-sperm IVF or adoption. Long-term follow-up should monitor pubertal progression, testicular failure/hypergonadotropic hypogonadism, tumor-risk markers, and individualized gender/psychosocial outcomes | (terribile201946xxtesticulardisorder pages 9-11, terribile201946xxtesticulardisorder pages 1-3, wei2022duplicationofsox3 pages 1-3, gong2025retrospectiveanalysisof pages 1-2, audı2018geneticsinendocrinology pages 1-6) |


*Table: This table provides a compact evidence-based summary of names, epidemiology, SRY status distribution, presentation patterns, and practical management points for 46,XX testicular DSD. It is useful as a quick reference before the full narrative report.*

---

## Recent developments (prioritizing 2023–2024)

1. **2024 synthesis of genetic causes**: Ferrari et al. (Frontiers in Endocrinology, 2024-04, https://doi.org/10.3389/fendo.2024.1385901) consolidates known genetic mechanisms and emphasizes that many cases remain genetically unresolved; it also provides epidemiologic and presentation statistics (incidence ~1:20,000–1:25,000; ~2% of male infertility; typical male genitalia at birth with later diagnosis). (ferrari2024testiculardifferentiationin pages 1-2, ferrari2024testiculardifferentiationin pages 2-4)

2. **2024 clinical perspective on non‑CAH 46,XX DSD**: Abalı & Guran (Frontiers in Endocrinology, 2024-05, https://doi.org/10.3389/fendo.2024.1354759) provides an updated gene list spanning CNVs and sequence variants implicated in 46,XX testicular/ovotesticular DSD and highlights management uncertainty around gonadal function and gender outcomes. (abalı2024diagnosisandmanagement pages 1-2)

3. **2023 focus on nuclear receptor genes and phenotypic variability**: Hattori & Fukami (Biomolecules, 2023-04, https://doi.org/10.3390/biom13040691) situates NR5A1/NR0B1/NR2F2 as key nuclear receptor genes in atypical testicular development and explicitly notes NR5A1 variants in both 46,XY and 46,XX testicular/ovotesticular DSD, with possible oligogenic contributions. (hattori2023nuclearreceptorgene pages 1-3)

---

## Limitations of this run
- Formal mappings to OMIM/Orphanet/MONDO/ICD/MeSH identifiers could not be provided with tool-citable evidence.
- Some additional potentially relevant papers were discovered by search but not fully retrieved/validated for citation in this run.


References

1. (terribile201946xxtesticulardisorder pages 1-3): Marco Terribile, Marco Stizzo, Celeste Manfredi, Carmelo Quattrone, Francesco Bottone, Dario Ranieri Giordano, Giuseppe Bellastella, Davide Arcaniolo, and Marco De Sio. 46,xx testicular disorder of sex development (dsd): a case report and systematic review. Medicina, 55:371, Jul 2019. URL: https://doi.org/10.3390/medicina55070371, doi:10.3390/medicina55070371. This article has 81 citations.

2. (ferrari2024testiculardifferentiationin pages 1-2): Maria Tereza Martins Ferrari, Elinaelma Suelane do Nascimento Silva, Mirian Yumie Nishi, Rafael Loch Batista, Berenice Bilharinho Mendonca, and Sorahia Domenice. Testicular differentiation in 46,xx dsd: an overview of genetic causes. Frontiers in Endocrinology, Apr 2024. URL: https://doi.org/10.3389/fendo.2024.1385901, doi:10.3389/fendo.2024.1385901. This article has 20 citations.

3. (li201446xxtesticulardisorder pages 1-2): Tian-Fu Li, Qiu-Yue Wu, Cui Zhang, Wei-Wei Li, Qing Zhou, Wei-Jun Jiang, Ying-Xia Cui, Xin-Yi Xia, and Yi-Chao Shi. 46,xx testicular disorder of sexual development with sry-negative caused by some unidentified mechanisms: a case report and review of the literature. BMC Urology, Dec 2014. URL: https://doi.org/10.1186/1471-2490-14-104, doi:10.1186/1471-2490-14-104. This article has 46 citations and is from a peer-reviewed journal.

4. (gong2025retrospectiveanalysisof pages 1-2): Yan Gong, Xiaoqin Yin, Jing Xu, Yan Li, Qingxu Liu, Shasha Zhou, Fei Wang, Yiqing Lyu, Sheng Guo, Wenyan Huang, and Pin Li. Retrospective analysis of children with 46,xx testicular/ovotesticular dsd: a 10-year single-center experience. Frontiers in Endocrinology, May 2025. URL: https://doi.org/10.3389/fendo.2025.1571467, doi:10.3389/fendo.2025.1571467. This article has 2 citations.

5. (ferrari2024testiculardifferentiationin pages 2-4): Maria Tereza Martins Ferrari, Elinaelma Suelane do Nascimento Silva, Mirian Yumie Nishi, Rafael Loch Batista, Berenice Bilharinho Mendonca, and Sorahia Domenice. Testicular differentiation in 46,xx dsd: an overview of genetic causes. Frontiers in Endocrinology, Apr 2024. URL: https://doi.org/10.3389/fendo.2024.1385901, doi:10.3389/fendo.2024.1385901. This article has 20 citations.

6. (abalı2024diagnosisandmanagement pages 1-2): Zehra Yavas Abalı and Tulay Guran. Diagnosis and management of non-cah 46,xx disorders/differences in sex development. Frontiers in Endocrinology, May 2024. URL: https://doi.org/10.3389/fendo.2024.1354759, doi:10.3389/fendo.2024.1354759. This article has 11 citations.

7. (terribile201946xxtesticulardisorder pages 7-9): Marco Terribile, Marco Stizzo, Celeste Manfredi, Carmelo Quattrone, Francesco Bottone, Dario Ranieri Giordano, Giuseppe Bellastella, Davide Arcaniolo, and Marco De Sio. 46,xx testicular disorder of sex development (dsd): a case report and systematic review. Medicina, 55:371, Jul 2019. URL: https://doi.org/10.3390/medicina55070371, doi:10.3390/medicina55070371. This article has 81 citations.

8. (wei2022duplicationofsox3 pages 1-3): Jiansheng Wei, Changrong Liu, Minyan Zhang, Shen Liu, Junjie Fu, and Peng Lin. Duplication of sox3 in an sry-negative 46,xx male with prostatic utricle: case report and literature review. BMC Medical Genomics, Sep 2022. URL: https://doi.org/10.1186/s12920-022-01347-0, doi:10.1186/s12920-022-01347-0. This article has 19 citations and is from a peer-reviewed journal.

9. (baetens2017nr5a1isa pages 1-2): Dorien Baetens, Hans Stoop, Frank Peelman, Anne-Laure Todeschini, Toon Rosseel, Frauke Coppieters, Reiner A. Veitia, Leendert H.J. Looijenga, Elfride De Baere, and Martine Cools. Nr5a1 is a novel disease gene for 46,xx testicular and ovotesticular disorders of sex development. Genetics in Medicine, 19:367-376, Apr 2017. URL: https://doi.org/10.1038/gim.2016.118, doi:10.1038/gim.2016.118. This article has 152 citations and is from a highest quality peer-reviewed journal.

10. (bashamboo2016arecurrentp.arg92trp pages 1-3): Anu Bashamboo, Patricia A. Donohoue, Eric Vilain, Sandra Rojo, Pierre Calvel, Sumudu N. Seneviratne, Federica Buonocore, Hayk Barseghyan, Nathan Bingham, Jill A. Rosenfeld, Surya Narayan Mulukutla, Mahim Jain, Lindsay Burrage, Shweta Dhar, Ashok Balasubramanyam, Brendan Lee, Marie-Charlotte Dumargne, Caroline Eozenou, Jenifer P. Suntharalingham, KSH de Silva, Lin Lin, Joelle Bignon-Topalovic, Francis Poulat, Carlos F. Lagos, Ken McElreavey, and John C. Achermann. A recurrent p.arg92trp variant in steroidogenic factor-1 (nr5a1) can act as a molecular switch in human sex development. Human Molecular Genetics, 25:3446-3453, Jul 2016. URL: https://doi.org/10.1093/hmg/ddw186, doi:10.1093/hmg/ddw186. This article has 152 citations and is from a domain leading peer-reviewed journal.

11. (terribile201946xxtesticulardisorder pages 9-11): Marco Terribile, Marco Stizzo, Celeste Manfredi, Carmelo Quattrone, Francesco Bottone, Dario Ranieri Giordano, Giuseppe Bellastella, Davide Arcaniolo, and Marco De Sio. 46,xx testicular disorder of sex development (dsd): a case report and systematic review. Medicina, 55:371, Jul 2019. URL: https://doi.org/10.3390/medicina55070371, doi:10.3390/medicina55070371. This article has 81 citations.

12. (hattori2023nuclearreceptorgene pages 1-3): Atsushi Hattori and Maki Fukami. Nuclear receptor gene variants underlying disorders/differences of sex development through abnormal testicular development. Biomolecules, 13:691, Apr 2023. URL: https://doi.org/10.3390/biom13040691, doi:10.3390/biom13040691. This article has 11 citations.

13. (luo2026raresrynegative46xx pages 4-5): Jianxu Luo, Fuxin Huang, Jianlin Li, Enhao Mo, Hu Wang, Jianyong Zhang, Caifeng Pang, Dezheng Lei, and Jiabo Chen. Rare sry-negative 46,xx disorder of sex development with male phenotype and ectopic gonads: a case report. Frontiers in Endocrinology, Apr 2026. URL: https://doi.org/10.3389/fendo.2026.1829751, doi:10.3389/fendo.2026.1829751. This article has 0 citations.

14. (abalı2024diagnosisandmanagement pages 14-14): Zehra Yavas Abalı and Tulay Guran. Diagnosis and management of non-cah 46,xx disorders/differences in sex development. Frontiers in Endocrinology, May 2024. URL: https://doi.org/10.3389/fendo.2024.1354759, doi:10.3389/fendo.2024.1354759. This article has 11 citations.

15. (audı2018geneticsinendocrinology pages 1-6): L. Audı́, S. Ahmed, N. Krone, M. Cools, K. McElreavey, P. Holterhus, A. Greenfield, A. Bashamboo, O. Hiort, S. Wudy, and R. McGowan. Genetics in endocrinology: approaches to molecular genetic diagnosis in the management of differences/disorders of sex development (dsd): position paper of eu cost action bm 1303 ‘dsdnet’. European Journal of Endocrinology, 179:R197-R206, Oct 2018. URL: https://doi.org/10.1530/eje-18-0256, doi:10.1530/eje-18-0256. This article has 140 citations and is from a highest quality peer-reviewed journal.

16. (audı2018geneticsinendocrinology pages 6-9): L. Audı́, S. Ahmed, N. Krone, M. Cools, K. McElreavey, P. Holterhus, A. Greenfield, A. Bashamboo, O. Hiort, S. Wudy, and R. McGowan. Genetics in endocrinology: approaches to molecular genetic diagnosis in the management of differences/disorders of sex development (dsd): position paper of eu cost action bm 1303 ‘dsdnet’. European Journal of Endocrinology, 179:R197-R206, Oct 2018. URL: https://doi.org/10.1530/eje-18-0256, doi:10.1530/eje-18-0256. This article has 140 citations and is from a highest quality peer-reviewed journal.

17. (ibba2022differencesofsex pages 18-21): Anastasia IBBA, Marta DEL PISTOIA, Antonio BALSAMO, Federico BARONIO, Donatella CAPALBO, Gianni RUSSO, Luisa DE SANCTIS, and Carla BIZZARRI. Differences of sex development in the newborn: from clinical scenario to molecular diagnosis. Jan 2022. URL: https://doi.org/10.23736/s2724-5276.21.06512-5, doi:10.23736/s2724-5276.21.06512-5. This article has 8 citations.

18. (grinspon2016disordersofsex pages 1-2): Romina P. Grinspon and Rodolfo A. Rey. Disorders of sex development with testicular differentiation in sry-negative 46,xx individuals: clinical and genetic aspects. Sexual Development, 10:1-11, Apr 2016. URL: https://doi.org/10.1159/000445088, doi:10.1159/000445088. This article has 110 citations and is from a peer-reviewed journal.

19. (barseghyan2017identificationofgenetic pages 21-26): H Barseghyan. Identification of genetic etiology in disorders of sex development. Unknown journal, 2017.

## Artifacts

- [Edison artifact artifact-00](46_XX_Testicular_DSD-deep-research-falcon_artifacts/artifact-00.md)