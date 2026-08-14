---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-24T16:41:29.889223'
end_time: '2026-07-24T16:48:58.372401'
duration_seconds: 448.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: apparent mineralocorticoid excess
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
  path: Apparent_Mineralocorticoid_Excess-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** apparent mineralocorticoid excess
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **apparent mineralocorticoid excess** covering all of the
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
- **Disease Name:** apparent mineralocorticoid excess
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **apparent mineralocorticoid excess** covering all of the
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


# Apparent Mineralocorticoid Excess: Disease Characteristics Report

## Executive summary

Apparent mineralocorticoid excess (AME) is a rare, usually autosomal-recessive monogenic hypertension syndrome caused by deficient **11β-hydroxysteroid dehydrogenase type 2 (11β-HSD2)**. The enzyme normally converts cortisol to cortisone in mineralocorticoid-sensitive tissues. Its loss allows abundant cortisol to activate the mineralocorticoid receptor (MR), producing renal sodium retention, potassium and hydrogen loss, volume expansion, suppressed renin and aldosterone, and often severe childhood hypertension. The classic disorder is caused by biallelic germline **HSD11B2** variants; partial genetic, epigenetic, and environmental impairment produces a broader, less firmly delimited “nonclassic AME” phenotype. (carvajal2020classicandnonclassic pages 6-7, lu2022apparentmineralocorticoidexcess pages 1-3)

The following table provides a curated overview.

| Core fact | Summary | Key details / ontology suggestions | Evidence |
|---|---|---|---|
| Identifiers | Apparent mineralocorticoid excess (AME) is a rare monogenic mineralocorticoid-hypertension disorder caused by impaired cortisol inactivation. | MONDO:0009025; OMIM: 218030; MeSH: D043204 (“Mineralocorticoid Excess Syndrome, Apparent”); category: Mendelian / autosomal recessive low-renin hypertension. Synonyms: AME, apparent mineralocorticoid excess syndrome, mineralocorticoid excess syndrome apparent. | (OpenTargets Search: apparent mineralocorticoid excess-HSD11B2, lu2022apparentmineralocorticoidexcess pages 1-3, NCT00474942 chunk 1) |
| Cause / inheritance | Classic AME is caused by biallelic germline pathogenic variants in **HSD11B2**, encoding 11β-HSD2; inheritance is autosomal recessive. | Causal gene: **HSD11B2**; protein: hydroxysteroid 11-beta dehydrogenase 2; mechanism is usually loss of function. Founder effects and consanguinity are recurrent in reported families. Nonclassic AME reflects partial deficiency with genetic/epigenetic contribution. | (carvajal2020classicandnonclassic pages 6-7, lu2022apparentmineralocorticoidexcess pages 1-3, palermo2004apparentmineralocorticoidexcess pages 2-4, carvajal2020classicandnonclassic pages 28-29) |
| Hallmark phenotype | Core phenotype is childhood-onset low-renin, low-aldosterone hypertension with hypokalemic metabolic alkalosis due to cortisol-mediated mineralocorticoid receptor activation. | Suggested HPO: Hypertension, Hypokalemia, Metabolic alkalosis, Low renin hypertension, Failure to thrive, Polyuria, Polydipsia, Nephrocalcinosis, Left ventricular hypertrophy, Low birth weight. Classic AME usually presents from infancy/childhood; nonclassic AME often in adolescents/adults and may be normotensive or mildly hypertensive. | (carvajal2020classicandnonclassic pages 6-7, NCT00474942 chunk 1, lu2022apparentmineralocorticoidexcess pages 16-16, lu2022apparentmineralocorticoidexcess pages 3-4) |
| Diagnostic signature | Biochemical hallmark is impaired cortisol-to-cortisone conversion with suppressed renin and aldosterone plus elevated cortisol/cortisone metabolite ratios; confirmation is by genetic testing. | Typical tests: plasma renin activity or concentration low/suppressed; aldosterone low; urinary steroid profile with elevated (THF + 5αTHF)/THE and/or serum/urine cortisol:cortisone ratio; classic AME often has 11βHSD2 activity ~1–6%, nonclassic ~40–60%. ClinicalTrials.gov eligibility required low renin, low aldosterone, elevated urinary cortisol/cortisone metabolite ratio, and two HSD11B2 mutations. | (carvajal2020classicandnonclassic pages 28-29, lu2022apparentmineralocorticoidexcess pages 1-3, NCT00474942 chunk 1) |
| Mechanism / pathophysiology | Loss of renal 11β-HSD2 prevents conversion of cortisol to cortisone, allowing cortisol to activate mineralocorticoid receptor despite low aldosterone, driving sodium retention and potassium wasting. | Upstream defect: HSD11B2 loss/partial loss. Downstream pathway: MR activation → ENaC and Na+/K+-ATPase upregulation → sodium and water retention, hypokalemia, low renin, hypertension. Primary anatomy: kidney distal nephron/collecting duct; additional expression in placenta, colon, brain. Suggested GO/UBERON/CL concepts: cortisol catabolic process, mineralocorticoid receptor signaling pathway, kidney, placenta, colon, renal tubular epithelial cell. | (lu2022apparentmineralocorticoidexcess pages 1-3, palermo2004apparentmineralocorticoidexcess pages 1-2) |
| Treatment / real-world management | Mainstays are salt restriction, mineralocorticoid receptor blockade, potassium-sparing approaches, potassium replacement, and selected glucocorticoid suppression therapy; renal transplant can cure the endocrine-renal defect in advanced kidney failure. | Reported regimens: spironolactone or eplerenone for classic and nonclassic AME; low-dose nonclassic examples include spironolactone 12.5–25 mg/day or eplerenone 25–50 mg/day; classic AME may need higher weight-based MR antagonist dosing plus potassium; amiloride blocks ENaC mechanistically; glucocorticoids may suppress ACTH-driven cortisol production in selected classic cases; kidney transplantation reported as curative. Suggested MAXO: low sodium diet, mineralocorticoid receptor antagonist therapy, potassium supplementation, renal transplantation. | (carvajal2020classicandnonclassic pages 17-19, lu2022apparentmineralocorticoidexcess pages 3-4, ding2025casereportclinical pages 6-7) |
| Prognosis / statistics | Prognosis depends strongly on early diagnosis and treatment; untreated disease can cause severe target-organ injury. | Long-term data cited in review: cardiovascular mortality 19%, persistent nephrocalcinosis 89%, kidney failure 15% in a 36-patient classic AME series; one long-term family follow-up found worst outcomes in the sibling with longest diagnostic delay. Natural-history study NCT00474942 enrolled 130 participants and notes some patients progress despite spironolactone. | (lu2022apparentmineralocorticoidexcess pages 3-4, NCT00474942 chunk 1) |
| Evidence limitations | Evidence base is dominated by case reports, small family series, reviews, and observational natural-history data; randomized trials and population prevalence estimates for classic AME are lacking. | Classic AME prevalence remains unclear; nonclassic AME estimate of 7.1% comes from one Chilean primary-care cohort and should not be generalized. Recent 2023–2024 literature mainly provides reviews, low-renin hypertension synthesis, epigenetic discussion, and case-series updates rather than interventional trials or gene therapy. | (carvajal2020classicandnonclassic pages 3-3, carvajal2020classicandnonclassic pages 9-9, NCT00474942 chunk 1, lu2022apparentmineralocorticoidexcess pages 1-3) |


*Table: This table summarizes the most important knowledge-base facts for apparent mineralocorticoid excess, including identifiers, etiology, phenotype, diagnosis, mechanism, treatment, prognosis, and major evidence gaps. It is designed as a compact reference for disease curation and clinical interpretation.*

## 1. Disease information

**Definition.** Classic AME is an inborn error of cortisol metabolism and a form of low-renin monogenic hypertension. Its characteristic combination is juvenile resistant hypertension, hypokalemic metabolic alkalosis, low renin, low aldosterone, and an elevated cortisol-to-cortisone metabolite ratio. It is “apparent” mineralocorticoid excess because the phenotype resembles excess aldosterone even though aldosterone is suppressed. (carvajal2020classicandnonclassic pages 6-7, lu2022apparentmineralocorticoidexcess pages 1-3)

**Identifiers and synonyms**

- **MONDO:** MONDO:0009025.
- **OMIM:** 218030.
- **MeSH:** D043204, *Mineralocorticoid Excess Syndrome, Apparent*.
- **Open Targets disease–gene association:** HSD11B2, Ensembl ENSG00000176387; association score 0.835 based on five evidence records. (OpenTargets Search: apparent mineralocorticoid excess-HSD11B2)
- **Common names:** apparent mineralocorticoid excess; apparent mineralocorticoid excess syndrome; AME; syndrome of apparent mineralocorticoid excess; 11β-HSD2 deficiency; inherited cortisol-cortisone shuttle defect. “AME type II” has historically described a milder phenotype, now often termed nonclassic AME.
- **ICD:** No uniquely disease-specific ICD-10 code was established in the retrieved evidence. Cases are commonly represented through hypertension, hypokalemia, endocrine/metabolic, or rare-disease codes. Mapping to a unique ICD code should therefore not be inferred without jurisdiction-specific verification.

The evidence is primarily **aggregated disease-level literature**, family studies, case series, and a prospective natural-history protocol—not routine EHR-derived population evidence. The completed multicenter natural-history study NCT00474942 enrolled 130 affected individuals and family members. (NCT00474942 chunk 1)

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

Classic AME results from **biallelic germline loss-of-function variants in HSD11B2**, inherited in an autosomal-recessive manner. More than 50 deleterious variants had been reported worldwide by 2022. They reduce enzyme function through protein instability, impaired substrate or NAD⁺-cofactor affinity, disrupted folding, altered catalytic activity, or disruption of the dimer interface. (lu2022apparentmineralocorticoidexcess pages 1-3)

### Genetic and demographic risk factors

- Having two pathogenic **HSD11B2** alleles is the principal risk factor.
- Consanguinity, endogamy, and founder effects increase the probability of biallelic disease in particular families and populations. (lu2022apparentmineralocorticoidexcess pages 3-4, palermo2004apparentmineralocorticoidexcess pages 2-4)
- Some heterozygotes have normal findings, whereas others show mild or moderate biochemical or blood-pressure phenotypes. Proposed explanations include haploinsufficiency, dominant-negative effects of particular proteins, and environmental “second hits”; this is not equivalent to established dominant inheritance of classic AME. (lu2022apparentmineralocorticoidexcess pages 3-4)
- No consistent sex predominance has been reported. (lu2022apparentmineralocorticoidexcess pages 3-4)

### Environmental and acquired causes

Licorice or glycyrrhizin/glycyrrhetinic acid, carbenoxolone, certain bioflavonoids, grapefruit-associated compounds, and some azole antifungals can inhibit 11β-HSD2 and produce an acquired AME-like state. Cortisol substrate excess in Cushing syndrome or ectopic ACTH production can overwhelm residual enzyme capacity. High sodium intake magnifies volume expansion and hypertension. (palermo2004apparentmineralocorticoidexcess pages 1-2, carvajal2020classicandnonclassic pages 11-12)

The proposed **two-hit model** for nonclassic AME comprises a first hit—partial genetic or epigenetic impairment of HSD11B2—and a second hit such as high salt intake, age-related change, or an endogenous/exogenous 11β-HSD2 inhibitor. (carvajal2020classicandnonclassic pages 3-3, carvajal2020classicandnonclassic pages 28-29)

### Protective factors

No validated protective allele is established. Avoidance of licorice and other inhibitors, sodium restriction, early diagnosis, adherence to MR/ENaC-directed treatment, and correction of hypokalemia reduce expression or complications but do not prevent inherited genotype formation. (lu2022apparentmineralocorticoidexcess pages 3-4, palermo2004apparentmineralocorticoidexcess pages 1-2)

## 3. Phenotypes

### Core clinical and laboratory phenotype

| Phenotype | Type and usual characteristics | Suggested HPO term |
|---|---|---|
| Hypertension | Clinical sign; often severe, resistant, and beginning in infancy or childhood in classic AME; normal to mildly/severely elevated in nonclassic disease | Hypertension; Early-onset hypertension |
| Suppressed renin and aldosterone | Laboratory abnormality; persistent unless treatment restores volume homeostasis | Low-renin hypertension; Decreased circulating renin; Hypoaldosteronism |
| Hypokalemia | Laboratory abnormality; often marked and chronic; may cause weakness, paralysis, tetany, or arrhythmia | Hypokalemia |
| Metabolic alkalosis | Laboratory abnormality secondary to renal hydrogen and potassium loss | Metabolic alkalosis |
| Low birth weight/IUGR | Prenatal manifestation related partly to loss of placental glucocorticoid protection | Low birth weight; Intrauterine growth retardation |
| Failure to thrive/growth retardation | Pediatric physical manifestation; variable and often improved with disease control | Failure to thrive; Short stature/Growth delay |
| Polyuria and polydipsia | Symptoms, partly related to chronic hypokalemia and renal concentrating impairment | Polyuria; Polydipsia |
| Muscle weakness or hypokalemic paralysis | Symptom; episodic or persistent according to potassium level | Muscle weakness; Hypokalemic paralysis |
| Nephrocalcinosis, hypercalciuria, renal calculi/cysts | Renal manifestations; nephrocalcinosis may persist despite treatment | Nephrocalcinosis; Hypercalciuria; Nephrolithiasis; Renal cyst |
| LV hypertrophy/cardiac dysfunction | Target-organ manifestations of severe hypertension | Left ventricular hypertrophy; Cardiomyopathy |
| Hypertensive retinopathy/stroke | Advanced vascular complications, especially after delayed control | Hypertensive retinopathy; Stroke |
| Delayed puberty | Reported in severe pediatric disease | Delayed puberty |

Classic AME generally starts in infancy or childhood with low birth weight, growth delay, severe hypertension, polyuria/polydipsia, hypokalemia, alkalosis, and failure to thrive. Nephrocalcinosis and renal cysts are repeatedly reported. Nonclassic AME usually presents in adolescence or adulthood with subtler steroid abnormalities and normal or moderately increased blood pressure. (NCT00474942 chunk 1, lu2022apparentmineralocorticoidexcess pages 3-4)

Phenotype frequencies are poorly quantified because most evidence consists of small families and case series. In a 36-patient long-term classic AME series summarized in the 2022 review, persistent nephrocalcinosis occurred in **89%**, kidney failure in **15%**, and cardiovascular mortality in **19%**. These estimates should not be treated as population-wide rates. (lu2022apparentmineralocorticoidexcess pages 3-4)

No disease-specific EQ-5D, SF-36, or PROMIS dataset was identified. Expected quality-of-life burdens include medication and dietary demands, weakness or arrhythmia from hypokalemia, polyuria, growth and pubertal effects, and disability from renal, cardiac, retinal, or cerebrovascular injury.

## 4. Genetic and molecular information

### Causal gene

- **Gene:** HSD11B2, hydroxysteroid 11-beta dehydrogenase 2.
- **Location:** chromosome 16q22; the historically described gene spans approximately 6.2 kb and contains five exons. (palermo2004apparentmineralocorticoidexcess pages 2-4)
- **Origin:** constitutional/germline, not somatic.
- **Mechanism:** loss or marked reduction of 11β-HSD2 enzymatic activity.

### Variant spectrum and examples

Reported classes include missense, nonsense, frameshift, and splice-disrupting variants. One review catalogued more than 260 HSD11B2 SNPs, including 66 coding variants, 35 missense changes, 10 frameshifts, and two variants causing severe splicing impairment; these totals mix disease-causing mutations and polymorphisms and therefore must not be interpreted as counts of pathogenic variants. (carvajal2020classicandnonclassic pages 12-13)

Examples include:

- **p.Arg213Cys (R213C):** pathogenic in recessive AME; disrupts hydrogen bonding in the central β-sheet, protein folding, stability, and catalytic activity. It has also been reported in subjects with nonclassic phenotypes. (carvajal2020classicandnonclassic pages 13-14)
- **c.650T>C, p.Val217Ala:** reported as an ACMG VUS in a homozygous child, with multiple computational predictions suggesting damage; computational evidence alone does not establish pathogenicity.
- **c.763dup, p.Val255GlyfsTer102; c.204_226del, p.Leu69AlafsTer15; c.1017C>A, p.Tyr339Ter:** truncating variants reported in compound-heterozygous pediatric cases.
- **c.662C>T, p.Ala221Val:** missense variant reported with p.Tyr339Ter. (ding2025casereportclinical pages 4-5)
- **rs5479, c.468C>A, p.Thr156=**, and **rs45483293, c.534G>A, p.Glu178=** are synonymous variants associated in some cohorts with hypertension-related phenotypes, but they are not equivalent to highly penetrant classic-AME alleles. (carvajal2020classicandnonclassic pages 13-14, carvajal2020classicandnonclassic pages 12-13)

Variant-specific gnomAD/TOPMed frequencies were not supplied in the retrieved literature and should be obtained directly from the current database release and transcript before curation. Most classic-AME pathogenic alleles are expected to be individually very rare. Copy-number changes or large chromosomal abnormalities are not established as a common mechanism; CMA, karyotyping, and FISH are therefore not first-line tests.

### Modifiers and epigenetics

Glucocorticoid receptor signaling, RAC1-GTPase, SUMOylation at 11β-HSD2 residue K266, and Hedgehog signaling can alter HSD11B2 expression or function. Promoter/first-exon CpG methylation, histone regulation, and microRNAs have been implicated in tissue-specific expression and nonclassic or salt-sensitive phenotypes, but none is a validated routine diagnostic biomarker. (carvajal2020classicandnonclassic pages 13-14, carvajal2020classicandnonclassic pages 11-12)

## 5. Environmental information

The environmental component is principally chemical and dietary rather than infectious:

- **Licorice/glycyrrhizin and related herbal medicines:** direct 11β-HSD2 inhibition.
- **Carbenoxolone, selected azoles, grapefruit/bioflavonoid compounds:** reported or proposed enzyme inhibition.
- **High sodium intake:** amplifies sodium retention and salt-sensitive blood pressure.
- **Cushing syndrome/ectopic ACTH:** endogenous cortisol overload can saturate the enzyme.
- **Infectious agents, smoking, radiation, pollution, and occupational exposures:** no established causal role in inherited AME.

A detailed medication, supplement, confectionery, herbal-product, and dietary history is essential before diagnosing genetic AME. (lu2022apparentmineralocorticoidexcess pages 3-4, palermo2004apparentmineralocorticoidexcess pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream trigger:** biallelic HSD11B2 loss, partial genetic/epigenetic suppression, or pharmacological enzyme inhibition.
2. **Biochemical defect:** reduced NAD⁺-dependent conversion of active cortisol to inactive cortisone.
3. **Receptor-level effect:** cortisol reaches and activates MR in epithelial target cells. MR binds cortisol and aldosterone with similar affinity in vitro, while circulating cortisol is vastly more abundant.
4. **Renal effector response:** MR-dependent transcription increases epithelial sodium channel (**ENaC**) and Na⁺/K⁺-ATPase activity in the distal nephron.
5. **Physiological effects:** sodium/water retention, potassium and hydrogen loss, extracellular-volume expansion, hypokalemic alkalosis, and suppression of renin and aldosterone.
6. **Downstream injury:** sustained hypertension and MR signaling promote endothelial oxidative stress, inflammation, vascular remodeling, cardiac hypertrophy, retinopathy, stroke, nephrocalcinosis, albuminuria, and progressive kidney damage. (carvajal2020classicandnonclassic pages 6-7, lu2022apparentmineralocorticoidexcess pages 1-3, palermo2004apparentmineralocorticoidexcess pages 1-2)

Urinary tetrahydrocortisol and allo-tetrahydrocortisol increase relative to tetrahydrocortisone, creating the elevated **(THF + 5αTHF)/THE** ratio. Serum cortisol can remain normal because intact hypothalamic-pituitary-adrenal feedback reduces secretion while cortisol clearance is prolonged; historical measurements found a cortisol half-life of 120–190 minutes versus 70–90 minutes in controls. (lu2022apparentmineralocorticoidexcess pages 1-3, palermo2004apparentmineralocorticoidexcess pages 2-4)

Suggested ontology annotations include **cortisol catabolic process**, **steroid metabolic process**, **mineralocorticoid receptor signaling**, **renal sodium-ion transport**, **potassium-ion homeostasis**, and **regulation of blood pressure**. Relevant cell types are renal tubular epithelial cells, particularly distal-nephron/collecting-duct principal cells; placental trophoblasts; colonic epithelial cells; and selected neurons. No AME-specific single-cell, spatial-transcriptomic, proteomic, lipidomic, or validated multi-omic clinical classifier was identified.

## 7. Anatomical structures affected

- **Primary organ:** kidney, especially distal tubule and collecting duct epithelium where 11β-HSD2 and MR are coexpressed.
- **Developmental organ:** placenta, where 11β-HSD2 forms a glucocorticoid barrier protecting the fetus.
- **Other expressing tissues:** distal colon, salivary gland, and restricted brain regions.
- **Secondary target organs:** heart and vasculature, retina, brain, and kidneys themselves through hypertensive injury. (lu2022apparentmineralocorticoidexcess pages 1-3, palermo2004apparentmineralocorticoidexcess pages 1-2)

Suggested UBERON concepts are kidney, renal collecting duct, distal convoluted tubule, placenta, colon, heart, blood vessel, retina, and brain. Suggested Cell Ontology concepts are kidney collecting-duct principal cell, distal-tubule epithelial cell, trophoblast, colonic epithelial cell, vascular endothelial cell, vascular smooth-muscle cell, and cardiomyocyte. At the subcellular level, 11β-HSD2 is associated mainly with the endoplasmic-reticulum membrane, while MR acts through cytoplasmic/nuclear receptor trafficking and nuclear transcription. Disease is systemic and has no meaningful lateralization.

## 8. Temporal development and natural history

Classic AME commonly begins prenatally with growth restriction or low birth weight and becomes clinically evident during infancy or childhood. Onset is chronic rather than acute, although hypokalemic paralysis, arrhythmia, stroke, or hypertensive crisis can be episodic acute presentations. Nonclassic disease generally appears in adolescence or adulthood and may remain subtle. (NCT00474942 chunk 1, lu2022apparentmineralocorticoidexcess pages 3-4)

The untreated course is chronic and potentially progressive: persistent hypertension and electrolyte disturbance lead to cardiac, vascular, retinal, and renal injury. Early biochemical and genetic diagnosis is the principal window for preventing irreversible damage. Treatment can normalize blood pressure and potassium, but nephrocalcinosis or established organ injury may persist. The natural-history protocol explicitly notes that some individuals progress or die within years despite spironolactone, although it does not provide a controlled treatment comparison. (NCT00474942 chunk 1)

## 9. Inheritance and population characteristics

Classic AME is **autosomal recessive**. Penetrance for severe biallelic loss-of-function genotypes appears high, but expressivity varies with residual activity, genotype, salt exposure, treatment, and diagnostic delay. Anticipation is not expected. Germline mosaicism has not emerged as an important recurrent mechanism. Each sibling of an affected individual born to two confirmed carriers has the standard recessive risks: 25% affected, 50% carrier, and 25% inheriting neither familial allele.

True prevalence and incidence of classic AME remain unknown. Fewer than 100 cases were noted in a recent pediatric case-series discussion, but case counts are subject to publication and ascertainment bias. Cases occur worldwide, with clustering in consanguineous, endogamous, or founder populations; no reliable global sex, incidence, or carrier-frequency estimate was established in the evidence reviewed. (lu2022apparentmineralocorticoidexcess pages 3-4, ding2025casereportclinical pages 4-5)

A Chilean primary-care study found biochemical evidence interpreted as partial 11β-HSD2 deficiency in **7.1%** of its cohort. This is a proposed nonclassic phenotype estimate, not the prevalence of biallelic classic AME and not necessarily generalizable to other populations. (carvajal2020classicandnonclassic pages 3-3, lu2022apparentmineralocorticoidexcess pages 3-4)

## 10. Diagnostics

### When to suspect AME

Suspect AME in a child, adolescent, or young adult with severe or resistant hypertension plus hypokalemia, metabolic alkalosis, suppressed renin, and unexpectedly low aldosterone—especially with low birth weight, growth failure, polyuria/polydipsia, nephrocalcinosis, consanguinity, or similarly affected siblings. (carvajal2020classicandnonclassic pages 6-7, NCT00474942 chunk 1)

### Recommended sequence

1. Confirm blood pressure using age-appropriate repeated or ambulatory measurements.
2. Measure serum electrolytes, bicarbonate, creatinine/eGFR, magnesium, calcium, and urine potassium/calcium; obtain ECG when hypokalemia is substantial.
3. Measure plasma renin activity or direct renin and plasma/serum aldosterone under interpretable medication, posture, sodium, and potassium conditions.
4. Obtain serum or urine cortisol/cortisone and preferably urinary steroid profiling. The characteristic ratio is elevated **(THF + 5αTHF)/THE**.
5. Exclude licorice, herbal products, carbenoxolone, azoles, Cushing syndrome, and exogenous glucocorticoids.
6. Confirm with sequence and deletion/duplication analysis of **HSD11B2**; parental testing establishes phase. A multigene monogenic-hypertension panel or WES/WGS is appropriate when the phenotype overlaps other disorders or single-gene testing is negative. (NCT00474942 chunk 1, lu2022apparentmineralocorticoidexcess pages 1-3)

Classic AME was summarized as having 11β-HSD2 activity of roughly **1–6%**, versus an inferred **40–60%** in nonclassic AME. Proposed biochemical definitions use cortisol/cortisone ratios above the 97.5th percentile for classic and above the 75th percentile for nonclassic disease, but these percentile criteria are research-oriented and assay/population dependent. (carvajal2020classicandnonclassic pages 28-29)

CMA, karyotyping, FISH, mitochondrial testing, repeat-expansion testing, biopsy, and liquid biopsy are not routinely indicated. Renal ultrasound evaluates nephrocalcinosis; echocardiography, retinal examination, urine albumin, and renal-function assessment identify target-organ damage.

### Differential diagnosis

- **Primary aldosteronism:** low renin but aldosterone elevated/inappropriately normal, unlike AME.
- **Liddle syndrome:** low renin/aldosterone and ENaC activation, but normal cortisol–cortisone metabolism; caused by SCNN1B/SCNN1G gain-of-function.
- **11β-hydroxylase or 17α-hydroxylase deficiency:** excess deoxycorticosterone with characteristic adrenal/sex-steroid abnormalities.
- **Glucocorticoid-remediable aldosteronism:** aldosterone-mediated and genetically distinct.
- **Gordon syndrome:** usually hyperkalemia and metabolic acidosis rather than hypokalemic alkalosis.
- **Cushing syndrome/ectopic ACTH**, licorice-induced pseudoaldosteronism, renal artery disease, and other causes of secondary hypertension.

The completed natural-history study required low renin and aldosterone, an elevated urinary metabolite ratio, and two HSD11B2 mutations for affected-participant enrollment. (NCT00474942 chunk 1)

## 11. Outcome and prognosis

Early diagnosis and sustained control of blood pressure and potassium can produce substantial clinical improvement and prevent target-organ injury. Delayed diagnosis predicts worse renal and cardiac outcomes: in one 20-year family follow-up, the sibling with the longest diagnostic delay developed left-ventricular dysfunction and renal failure requiring transplantation, whereas the two earlier-managed siblings avoided comparable end-organ damage. (lu2022apparentmineralocorticoidexcess pages 3-4)

The best available long-term statistics are small-series estimates rather than survival curves: cardiovascular mortality 19%, persistent nephrocalcinosis 89%, and kidney failure 15% among 36 classic-AME patients summarized in the 2022 review. No reliable five- or ten-year survival rate, population mortality rate, or validated prognostic calculator exists. (lu2022apparentmineralocorticoidexcess pages 3-4)

Adverse prognostic features include very low residual enzyme activity, very early/severe hypertension, profound chronic hypokalemia, delayed diagnosis, poor medication adherence, high sodium intake, albuminuria/nephrocalcinosis, left-ventricular hypertrophy, and declining eGFR.

## 12. Treatment

### Core management

- **Dietary sodium restriction:** reduces the salt-sensitive component; suggested MAXO concept: therapeutic low-sodium diet.
- **MR antagonists:** spironolactone or eplerenone directly oppose inappropriate cortisol-driven MR activation. Reviews cite classic-AME spironolactone-equivalent dosing in the approximate range of **2–10 mg/kg/day**, individualized carefully, and lower nonclassic doses such as spironolactone **12.5–25 mg/day** or eplerenone **25–50 mg/day**. Suggested MAXO: mineralocorticoid-receptor antagonist therapy. (lu2022apparentmineralocorticoidexcess pages 3-4, carvajal2020classicandnonclassic pages 17-19)
- **ENaC blockade:** amiloride targets the downstream epithelial sodium channel and can be used alone or with MR blockade; suggested MAXO: potassium-sparing diuretic therapy.
- **Potassium replacement:** oral potassium chloride for active depletion; suggested MAXO: potassium supplementation.
- **Glucocorticoid suppression:** dexamethasone or related therapy has sometimes been used to suppress ACTH-driven endogenous cortisol production, but long-term glucocorticoid toxicity and incomplete response limit routine use.
- **Additional antihypertensives:** used when MR/ENaC blockade and sodium restriction do not adequately control pressure.
- **Kidney transplantation:** reported to resolve the renal enzymatic defect in patients with end-stage kidney disease, permitting discontinuation of spironolactone in reported cases; suggested MAXO: renal transplantation. (lu2022apparentmineralocorticoidexcess pages 3-4, ding2025casereportclinical pages 6-7)

Monitoring should include blood pressure, renin as a marker of adequate reversal of volume suppression, potassium, bicarbonate, creatinine/eGFR, urine albumin and calcium, growth/puberty, ECG where indicated, renal imaging, and cardiac assessment. Spironolactone can cause gynecomastia and sex-steroid adverse effects; eplerenone is more selective but often more costly and may require divided dosing. MR antagonists, amiloride, and potassium all create hyperkalemia risk as renal function changes.

No approved gene therapy, cell therapy, RNA therapy, immunotherapy, or AME-specific pharmacogenomic dosing guideline was identified. NCT00474942 was observational, not a therapeutic trial. (NCT00474942 chunk 1)

## 13. Prevention

**Primary prevention of inherited disease** requires reproductive rather than lifestyle intervention: genetic counseling, carrier testing for adult relatives, partner testing when relevant, and discussion of prenatal or preimplantation genetic testing once familial variants are known. Population-wide newborn screening is not established.

**Secondary prevention** consists of cascade testing, blood-pressure and electrolyte assessment of siblings, and early steroid profiling/genetic testing in high-risk relatives. Family members carrying one variant may merit blood-pressure review, especially under high-salt or 11β-HSD2-inhibiting exposures. (NCT00474942 chunk 1)

**Tertiary prevention** includes lifelong sodium restriction, avoidance of licorice and interacting products, treatment adherence, correction of potassium, and surveillance for renal, retinal, cardiac, and cerebrovascular injury. There is no vaccine or infectious prophylaxis relevant to AME.

## 14. Other species and natural disease

11β-HSD2 is evolutionarily conserved across mammals, and orthologous **Hsd11b2** genes regulate glucocorticoid access to MR. No well-established, naturally occurring veterinary counterpart with a defined breed association was identified in the retrieved evidence. AME is noninfectious and has no zoonotic or cross-species transmission potential.

Suggested comparative taxa are *Mus musculus* (NCBI Taxon 10090) and *Rattus norvegicus* (Taxon 10116). Veterinary breed-ontology mapping is not applicable without a documented natural breed disorder.

## 15. Model organisms and experimental systems

Genetic **Hsd11b2-null and haploinsufficient mouse/rat models** are the principal mammalian systems. They reproduce key mechanistic features—salt-sensitive hypertension, suppressed renin, altered electrolyte handling, renal/cardiac injury, and dependence on dietary sodium—and are used to dissect kidney-specific versus extra-renal 11β-HSD2 functions and test MR/ENaC-directed treatment. Their limitations include species differences in the predominant glucocorticoid (corticosterone rather than cortisol), developmental severity, diet dependence, and incomplete replication of human allelic heterogeneity.

Cell-based expression systems are used to measure cortisol-to-cortisone conversion, protein abundance/stability, cofactor or substrate affinity, and effects of individual variants. Placental and renal epithelial models are biologically relevant. No validated patient-derived organoid, iPSC, CRISPR-screen, or advanced spatial/single-cell AME platform was identified as a clinical implementation in the retrieved evidence.

## Recent developments and expert assessment

Recent work has shifted emphasis from AME as a binary ultra-rare syndrome toward a **continuum of cortisol-mediated MR activation**, including nonclassic, epigenetically modified, and environmentally unmasked phenotypes. However, classic AME remains a genetically defined recessive disease, whereas nonclassic AME criteria and prevalence require external validation. The 7.1% Chilean estimate should therefore be regarded as hypothesis-generating rather than a global disease-frequency estimate. (carvajal2020classicandnonclassic pages 3-3, carvajal2020classicandnonclassic pages 9-9)

The strongest contemporary expert message is that molecular testing should occur early in young patients with low-renin/low-aldosterone hypertension because “**a precise diagnosis depends on genetic testing, which allows for early and specific management to avoid the morbidity and mortality from target organ damage**.” This is a direct quotation from the November 2022 open-access molecular-genetics review (DOI: https://doi.org/10.1186/s12967-022-03698-9). (lu2022apparentmineralocorticoidexcess pages 1-3)

The available 2023–2024 literature is dominated by expert reviews of low-renin hypertension, HSD11B2 epigenetic regulation, and case-based diagnosis rather than randomized AME trials. A recent Chinese pediatric series, published online under DOI https://doi.org/10.3389/fendo.2024.1491825, expanded the allelic spectrum and reported normalization of blood pressure and potassium with spironolactone plus potassium in three children, but its size and case-report design preclude response-rate estimation. (ding2025casereportclinical pages 4-5, ding2025casereportclinical pages 6-7)

## Evidence-quality statement

Mechanistic certainty is high for biallelic HSD11B2 deficiency, impaired cortisol inactivation, and cortisol-driven MR activation. Clinical-management evidence is much weaker: it is derived mostly from biochemical physiology, family studies, case reports, small series, and one 130-participant observational natural-history protocol. No randomized AME-specific drug trial, validated population screening program, robust quality-of-life dataset, or approved molecular therapy was identified. Exact phenotype frequencies, variant penetrance, carrier frequency, and long-term survival therefore remain incompletely defined. (NCT00474942 chunk 1, lu2022apparentmineralocorticoidexcess pages 3-4, lu2022apparentmineralocorticoidexcess pages 1-3)

### Key source links and dates

- Lu et al., *Journal of Translational Medicine*, **November 2022**, “Apparent mineralocorticoid excess: comprehensive overview of molecular genetics,” DOI: https://doi.org/10.1186/s12967-022-03698-9. (lu2022apparentmineralocorticoidexcess pages 1-3)
- Carvajal et al., *Journal of Clinical Endocrinology & Metabolism*, **2020**, “Classic and Nonclassic Apparent Mineralocorticoid Excess Syndrome,” DOI: https://doi.org/10.1210/clinem/dgz315. (carvajal2020classicandnonclassic pages 6-7)
- Palermo et al., *Arquivos Brasileiros de Endocrinologia & Metabologia*, **October 2004**, PMID **15761540**, DOI: https://doi.org/10.1590/S0004-27302004000500015. (NCT00474942 chunk 1, palermo2004apparentmineralocorticoidexcess pages 1-2)
- Natural History of Apparent Mineralocorticoid Excess Syndrome, **NCT00474942**, posted May 17, 2007; completed November 2013: https://clinicaltrials.gov/study/NCT00474942. (NCT00474942 chunk 1)
- Ding et al., *Frontiers in Endocrinology*, article DOI year **2024**, published January 2025, DOI: https://doi.org/10.3389/fendo.2024.1491825. (ding2025casereportclinical pages 4-5)

References

1. (carvajal2020classicandnonclassic pages 6-7): Cristian A Carvajal, Alejandra Tapia-Castillo, Andrea Vecchiola, Rene Baudrand, and Carlos E Fardella. Classic and nonclassic apparent mineralocorticoid excess syndrome. The Journal of clinical endocrinology and metabolism, 105:e924-e936, Dec 2020. URL: https://doi.org/10.1210/clinem/dgz315, doi:10.1210/clinem/dgz315. This article has 55 citations.

2. (lu2022apparentmineralocorticoidexcess pages 1-3): Yi-ting Lu, Di Zhang, Qiong-yu Zhang, Ze-ming Zhou, Kun-qi Yang, Xian-liang Zhou, and Fan Peng. Apparent mineralocorticoid excess: comprehensive overview of molecular genetics. Journal of Translational Medicine, Nov 2022. URL: https://doi.org/10.1186/s12967-022-03698-9, doi:10.1186/s12967-022-03698-9. This article has 44 citations and is from a peer-reviewed journal.

3. (OpenTargets Search: apparent mineralocorticoid excess-HSD11B2): Open Targets Query (apparent mineralocorticoid excess-HSD11B2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (NCT00474942 chunk 1):  Natural History of Apparent Mineralocorticoid Excess Syndrome. Icahn School of Medicine at Mount Sinai. 2007. ClinicalTrials.gov Identifier: NCT00474942

5. (palermo2004apparentmineralocorticoidexcess pages 2-4): Mario Palermo, Marcus Quinkler, and Paul M. Stewart. Apparent mineralocorticoid excess syndrome: an overview. Arquivos brasileiros de endocrinologia e metabologia, 48 5:687-96, Oct 2004. URL: https://doi.org/10.1590/s0004-27302004000500015, doi:10.1590/s0004-27302004000500015. This article has 128 citations and is from a peer-reviewed journal.

6. (carvajal2020classicandnonclassic pages 28-29): Cristian A Carvajal, Alejandra Tapia-Castillo, Andrea Vecchiola, Rene Baudrand, and Carlos E Fardella. Classic and nonclassic apparent mineralocorticoid excess syndrome. The Journal of clinical endocrinology and metabolism, 105:e924-e936, Dec 2020. URL: https://doi.org/10.1210/clinem/dgz315, doi:10.1210/clinem/dgz315. This article has 55 citations.

7. (lu2022apparentmineralocorticoidexcess pages 16-16): Yi-ting Lu, Di Zhang, Qiong-yu Zhang, Ze-ming Zhou, Kun-qi Yang, Xian-liang Zhou, and Fan Peng. Apparent mineralocorticoid excess: comprehensive overview of molecular genetics. Journal of Translational Medicine, Nov 2022. URL: https://doi.org/10.1186/s12967-022-03698-9, doi:10.1186/s12967-022-03698-9. This article has 44 citations and is from a peer-reviewed journal.

8. (lu2022apparentmineralocorticoidexcess pages 3-4): Yi-ting Lu, Di Zhang, Qiong-yu Zhang, Ze-ming Zhou, Kun-qi Yang, Xian-liang Zhou, and Fan Peng. Apparent mineralocorticoid excess: comprehensive overview of molecular genetics. Journal of Translational Medicine, Nov 2022. URL: https://doi.org/10.1186/s12967-022-03698-9, doi:10.1186/s12967-022-03698-9. This article has 44 citations and is from a peer-reviewed journal.

9. (palermo2004apparentmineralocorticoidexcess pages 1-2): Mario Palermo, Marcus Quinkler, and Paul M. Stewart. Apparent mineralocorticoid excess syndrome: an overview. Arquivos brasileiros de endocrinologia e metabologia, 48 5:687-96, Oct 2004. URL: https://doi.org/10.1590/s0004-27302004000500015, doi:10.1590/s0004-27302004000500015. This article has 128 citations and is from a peer-reviewed journal.

10. (carvajal2020classicandnonclassic pages 17-19): Cristian A Carvajal, Alejandra Tapia-Castillo, Andrea Vecchiola, Rene Baudrand, and Carlos E Fardella. Classic and nonclassic apparent mineralocorticoid excess syndrome. The Journal of clinical endocrinology and metabolism, 105:e924-e936, Dec 2020. URL: https://doi.org/10.1210/clinem/dgz315, doi:10.1210/clinem/dgz315. This article has 55 citations.

11. (ding2025casereportclinical pages 6-7): Yuan Ding, Ming Cheng, Bingyan Cao, Min Liu, Xuyun Hu, and Di Wu. Case report: clinical characteristics and genetical analysis of hsd11b2 in three chinese children with apparent mineralocorticoid excess: a case series. Frontiers in Endocrinology, Jan 2025. URL: https://doi.org/10.3389/fendo.2024.1491825, doi:10.3389/fendo.2024.1491825. This article has 3 citations.

12. (carvajal2020classicandnonclassic pages 3-3): Cristian A Carvajal, Alejandra Tapia-Castillo, Andrea Vecchiola, Rene Baudrand, and Carlos E Fardella. Classic and nonclassic apparent mineralocorticoid excess syndrome. The Journal of clinical endocrinology and metabolism, 105:e924-e936, Dec 2020. URL: https://doi.org/10.1210/clinem/dgz315, doi:10.1210/clinem/dgz315. This article has 55 citations.

13. (carvajal2020classicandnonclassic pages 9-9): Cristian A Carvajal, Alejandra Tapia-Castillo, Andrea Vecchiola, Rene Baudrand, and Carlos E Fardella. Classic and nonclassic apparent mineralocorticoid excess syndrome. The Journal of clinical endocrinology and metabolism, 105:e924-e936, Dec 2020. URL: https://doi.org/10.1210/clinem/dgz315, doi:10.1210/clinem/dgz315. This article has 55 citations.

14. (carvajal2020classicandnonclassic pages 11-12): Cristian A Carvajal, Alejandra Tapia-Castillo, Andrea Vecchiola, Rene Baudrand, and Carlos E Fardella. Classic and nonclassic apparent mineralocorticoid excess syndrome. The Journal of clinical endocrinology and metabolism, 105:e924-e936, Dec 2020. URL: https://doi.org/10.1210/clinem/dgz315, doi:10.1210/clinem/dgz315. This article has 55 citations.

15. (carvajal2020classicandnonclassic pages 12-13): Cristian A Carvajal, Alejandra Tapia-Castillo, Andrea Vecchiola, Rene Baudrand, and Carlos E Fardella. Classic and nonclassic apparent mineralocorticoid excess syndrome. The Journal of clinical endocrinology and metabolism, 105:e924-e936, Dec 2020. URL: https://doi.org/10.1210/clinem/dgz315, doi:10.1210/clinem/dgz315. This article has 55 citations.

16. (carvajal2020classicandnonclassic pages 13-14): Cristian A Carvajal, Alejandra Tapia-Castillo, Andrea Vecchiola, Rene Baudrand, and Carlos E Fardella. Classic and nonclassic apparent mineralocorticoid excess syndrome. The Journal of clinical endocrinology and metabolism, 105:e924-e936, Dec 2020. URL: https://doi.org/10.1210/clinem/dgz315, doi:10.1210/clinem/dgz315. This article has 55 citations.

17. (ding2025casereportclinical pages 4-5): Yuan Ding, Ming Cheng, Bingyan Cao, Min Liu, Xuyun Hu, and Di Wu. Case report: clinical characteristics and genetical analysis of hsd11b2 in three chinese children with apparent mineralocorticoid excess: a case series. Frontiers in Endocrinology, Jan 2025. URL: https://doi.org/10.3389/fendo.2024.1491825, doi:10.3389/fendo.2024.1491825. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](Apparent_Mineralocorticoid_Excess-deep-research-falcon_artifacts/artifact-00.md)