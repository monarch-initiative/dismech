---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T17:45:37.900403'
end_time: '2026-07-31T17:56:14.025744'
duration_seconds: 636.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Burn-McKeown Syndrome
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
  path: Burn-McKeown_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Burn-McKeown Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Burn-McKeown Syndrome** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
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
- **Disease Name:** Burn-McKeown Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Burn-McKeown Syndrome** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Burn–McKeown Syndrome: Disease-Characteristics Research Report

## Executive summary

Burn–McKeown syndrome (BMKS) is an exceptionally rare, congenital, autosomal-recessive craniofacial spliceosomopathy caused by biallelic variants that reduce **TXNL4A** function. Bilateral choanal atresia or stenosis is the defining manifestation; hearing loss, cleft lip/palate, lower-eyelid coloboma, short palpebral fissures, a prominent high-bridged nose, short philtrum, large ears, and occasional cardiac or other visceral anomalies form the broader phenotype. Fewer than 20 affected families had been reported by 2020, precluding reliable prevalence, survival, penetrance, or quality-of-life estimates. (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 1-2)

The usual molecular architecture is a hypomorphic 34-bp TXNL4A promoter deletion in trans with a rare loss-of-function allele. Reduced TXNL4A disrupts U4/U6.U5 tri-snRNP assembly and selectively changes pre-mRNA splicing. Patient-derived neural-crest models implicate diminished WNT signaling, abnormal **TCF7L2** splicing, delayed epithelial-to-mesenchymal transition (EMT), and reduced proliferation; Xenopus knockdown additionally supports apoptosis-mediated depletion of cranial neural-crest progenitors. (wieczorek2014compoundheterozygosityof pages 7-8, wood2020modellingthedevelopmental pages 37-41, park2022thecoresplicing pages 7-10)

No disease-modifying treatment, validated biomarker, formal clinical guideline, or BMKS-specific interventional trial was identified. Current care is multidisciplinary and directed at airway obstruction, hearing impairment, clefting, cardiac defects, and other individual anomalies.

| domain | established finding | quantitative evidence | suggested ontology terms | evidence type/source |
|---|---|---|---|---|
| Disease identity | Burn-McKeown syndrome is a rare congenital craniofacial spliceosomopathy; OMIM 608572 | Fewer than 20 affected families reported worldwide by 2020 (wood2020modellingthedevelopmental pages 1-5) | OMIM: 608572; congenital disorder; craniofacial developmental disorder | Human disease synthesis and patient-derived model background (wood2020modellingthedevelopmental pages 1-5) |
| Inheritance | Autosomal recessive disease caused by biallelic TXNL4A variants | 9 of 11 families in the discovery study had biallelic TXNL4A mutations (wieczorek2014compoundheterozygosityof pages 1-2, wieczorek2014compoundheterozygosityof pages 7-8) | autosomal recessive inheritance; TXNL4A | Human clinical genetics, AJHG 2014 (wieczorek2014compoundheterozygosityof pages 1-2, wieczorek2014compoundheterozygosityof pages 7-8) |
| Causal gene/mechanism class | TXNL4A encodes a U5 snRNP/spliceosome component; disease reflects reduced TXNL4A dosage rather than simple heterozygous haploinsufficiency | Unaffected heterozygous relatives carried single variants; disease required biallelic hypomorphic/LoF combinations (wieczorek2014compoundheterozygosityof pages 4-6) | TXNL4A; U5 snRNP; pre-mRNA splicing | Human genetics with functional interpretation (wieczorek2014compoundheterozygosityof pages 4-6) |
| Pathogenic variant architecture | Typical genotype is compound heterozygosity for a 34-bp promoter deletion on one allele plus a loss-of-function allele on the other; homozygous promoter deletion also reported | Promoter D1: chr18:g.77,748,581_77,748,614del; promoter D2: chr18:g.77,748,604_77,748,637del; LoF examples: c.349G>T p.(Glu117*), c.37C>T p.(Gln13*), c.131delT p.(Val44Alafs*48); terminal 18q deletions also observed (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 4-6) | TXNL4A; promoter deletion; nonsense variant; frameshift variant; copy-number loss | Human clinical genetics and molecular characterization (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 4-6) |
| Population genetics | The commonest disease-associated promoter allele is low frequency in the general population, consistent with a rare recessive disorder | Type 1 promoter deletion allele frequency 0.76%; predicted homozygous frequency ~1 in 17,300 (wieczorek2014compoundheterozygosityof pages 1-2, wieczorek2014compoundheterozygosityof pages 7-8) | low-frequency regulatory allele | Human case-control/segregation data (wieczorek2014compoundheterozygosityof pages 1-2, wieczorek2014compoundheterozygosityof pages 7-8) |
| Core phenotype | Choanal atresia/stenosis is the defining feature; reported synthesis states it was observed in all patients, with associated craniofacial, hearing, and occasional visceral anomalies | Choanal atresia observed in all patients in the 2020 synthesis; common additional features include hearing loss, cleft lip/palate, short palpebral fissures, lower eyelid coloboma, short philtrum, prominent nose/high bridge, large ears; congenital heart defects can occur (wood2020modellingthedevelopmental pages 1-5) | choanal atresia; cleft palate; hearing impairment; eyelid coloboma; short philtrum; prominent nose; congenital heart defect | Human disease synthesis and original family series (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 1-2) |
| Additional variable features | Reported variable findings extend beyond the canonical craniofacial pattern | Patent foramen ovale, persistent ductus arteriosus, imperforate anus, fifth-finger clinodactyly, hallux valgus, preauricular tags, renal agenesis, inguinal hernia reported across families (wieczorek2014compoundheterozygosityof pages 3-4, wieczorek2014compoundheterozygosityof pages 2-3) | imperforate anus; clinodactyly; renal agenesis; preauricular tag | Human family series (wieczorek2014compoundheterozygosityof pages 3-4, wieczorek2014compoundheterozygosityof pages 2-3) |
| Neurodevelopment | Intellectual development is usually normal, but severe intellectual disability has been reported rarely | One exceptional severe intellectual disability case noted in the literature/model background (wood2020modellingthedevelopmental pages 1-5, wood2020modellingthedevelopmental pages 37-41) | intellectual disability | Human case-based synthesis and iPSC-study background (wood2020modellingthedevelopmental pages 1-5, wood2020modellingthedevelopmental pages 37-41) |
| Molecular pathophysiology upstream | Promoter deletions reduce TXNL4A expression; reduced TXNL4A impairs U4/U6.U5 tri-snRNP assembly | Type 1 and type 2 promoter deletions reduced promoter activity by 59% and 72%, respectively; yeast DIB1 depletion impaired tri-snRNP assembly (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 7-8) | TXNL4A; U4/U6.U5 tri-snRNP assembly; mRNA splicing | Human regulatory assay plus yeast functional model (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 7-8) |
| Molecular pathophysiology downstream | Reduced TXNL4A causes selective mis-splicing and altered gene expression, especially in neural crest-relevant programs | In patient iPSCs: 1,511 alternative splicing events in 1,096 genes and 1,181 DEGs; in iNCCs: 2,991 splicing events in 2,029 genes and 5,746 DEGs, with 88% of differential splicing unique to iNCCs (wood2020modellingthedevelopmental pages 24-27, wood2020modellingthedevelopmental pages 27-31, wood2020modellingthedevelopmental pages 69-74) | alternative splicing; gene expression regulation; neural crest development | Human patient-derived iPSC/iNCC transcriptomics (preprint) (wood2020modellingthedevelopmental pages 24-27, wood2020modellingthedevelopmental pages 27-31, wood2020modellingthedevelopmental pages 69-74) |
| WNT/neural crest mechanism | A leading mechanistic model links TXNL4A deficiency to dampened WNT signaling via TCF7L2 mis-splicing, delaying neural crest epithelial-to-mesenchymal transition | Patient iNCC EMT score -5 vs +5 (mother) and +8 (controls); AXIN2 downregulated (p=0.0004); TCF7L2 exon 4 mis-splicing validated; patient iPSCs proliferated 52%-65% more slowly than controls/mother (wood2020modellingthedevelopmental pages 34-37, wood2020modellingthedevelopmental pages 27-31, wood2020modellingthedevelopmental pages 21-24) | WNT signaling; TCF7L2; epithelial to mesenchymal transition; neural crest cell | Human patient-derived iPSC/iNCC functional model (preprint) (wood2020modellingthedevelopmental pages 34-37, wood2020modellingthedevelopmental pages 27-31, wood2020modellingthedevelopmental pages 21-24) |
| Developmental cell biology | Neural crest depletion/dysfunction is supported across models as a proximate cause of craniofacial malformation | Xenopus Txnl4a knockdown increased apoptosis in dorsal ectoderm at stage 15 (n=41, p<0.0005) and produced craniofacial cartilage defects in 38% of tadpoles; sox10 reduction was partially rescued by morpholino-resistant txnl4a (park2022thecoresplicing pages 7-10, park2022thecoresplicing pages 4-7, park2022thecoresplicing pages 1-2) | neural crest cell; apoptosis; craniofacial cartilage development; sox10 | Xenopus morpholino/rescue model (park2022thecoresplicing pages 7-10, park2022thecoresplicing pages 4-7, park2022thecoresplicing pages 1-2) |
| Onset/course | Disease onset is congenital/developmental and non-remitting; manifestations arise from embryonic craniofacial development defects | Choanal atresia and craniofacial anomalies are present from birth; no evidence for episodic course or spontaneous remission (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 1-2) | congenital onset; craniofacial malformation | Human clinical description/synthesis (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 1-2) |
| Diagnostic strategy | Diagnosis is clinical plus molecular: recognize the choanal-atresia/facial dysostosis pattern, then confirm biallelic TXNL4A variants including regulatory deletion and CNV detection | Discovery study used exome/genome sequencing, microarray, and MLPA; CNVs ranged from 0.484 Mb to 4.7 Mb; promoter deletions would be missed by coding-only analysis if regulatory regions are not interrogated (wieczorek2014compoundheterozygosityof pages 3-4, wieczorek2014compoundheterozygosityof pages 4-6) | facial dysostosis; TXNL4A molecular testing; copy-number analysis; promoter variant analysis | Human genetics workflow evidence (wieczorek2014compoundheterozygosityof pages 3-4, wieczorek2014compoundheterozygosityof pages 4-6) |
| Management | No disease-modifying BMKS therapy is established; care is supportive and anomaly-directed | No BMKS-specific interventional trials identified; reported care needs include airway management for choanal atresia, hearing support including possible cochlear implantation, and management of cleft/cardiac/other anomalies as indicated (wieczorek2014compoundheterozygosityof pages 2-3) | supportive care; surgical repair; hearing rehabilitation | Human case series plus evidence gap on trials (wieczorek2014compoundheterozygosityof pages 2-3) |
| Prognosis/evidence gaps | Prognosis is poorly quantified because of the rarity of the condition; survival, QoL, and natural-history metrics are not well defined in the literature retrieved | No robust prevalence, incidence, survival, or treatment-response statistics identified beyond family counts and phenotype summaries (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 1-2) | rare disease epidemiology | Evidence-gap synthesis from available literature (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 1-2) |
| Model systems | BMKS has mechanistic models in yeast, patient-derived iPSC/iNCC systems, and Xenopus embryos | Yeast DIB1 depletion showed tri-snRNP assembly defects; iPSC/iNCC model demonstrated proliferation, splicing, and EMT/WNT abnormalities; Xenopus knockdown caused neural crest/apoptosis/cartilage phenotypes with partial rescue (wieczorek2014compoundheterozygosityof pages 7-8, wood2020modellingthedevelopmental pages 37-41, park2022thecoresplicing pages 7-10) | Saccharomyces cerevisiae model; induced pluripotent stem cell; induced neural crest cell; Xenopus laevis | Yeast, in vitro human, and amphibian model evidence (wieczorek2014compoundheterozygosityof pages 7-8, wood2020modellingthedevelopmental pages 37-41, park2022thecoresplicing pages 7-10) |


*Table: This table condenses the main disease-level, genetic, mechanistic, diagnostic, and model-system findings for Burn-McKeown syndrome. It highlights established evidence and key quantitative details while preserving citations to the retrieved source contexts.*

## Evidence scope and currency

The principal human genetic evidence remains the 2014 *American Journal of Human Genetics* study of 11 families. The most detailed disease-specific mechanistic investigation is a May 2020 bioRxiv patient-iPSC study and should be treated as **preprint evidence**. The principal organismal BMKS model is a peer-reviewed 2022 Xenopus study. Searches prioritizing 2023–2024 identified no new BMKS-specific clinical cohort, natural-history study, therapeutic trial, or definitive molecular update; recent spliceosomopathy work remains largely contextual rather than BMKS-specific.

---

## 1. Disease information

### Definition and classification

BMKS is a **Mendelian congenital craniofacial developmental disorder**, more specifically a U5-snRNP-related craniofacial spliceosomopathy or mandibulofacial dysostosis spectrum disorder. It was clinically recognized before its genetic cause was established; biallelic TXNL4A variants were demonstrated in 2014. (wieczorek2014compoundheterozygosityof pages 1-2)

### Identifiers and synonyms

- **OMIM:** 608572.
- **MONDO:** A dedicated MONDO identifier was not verified in the retrieved primary literature; it should be resolved directly against the current MONDO release rather than inferred.
- **Orphanet:** Not verified from the retrieved evidence.
- **ICD-10/ICD-11:** No disease-specific code was identified. Coding generally requires congenital-malformation codes for choanal atresia and associated defects.
- **MeSH:** No dedicated BMKS descriptor was verified.
- **Synonyms:** Burn–McKeown syndrome; Burn-McKeown syndrome; BMKS; occasionally discussed in relation to **oculo-oto-facial dysplasia**, which may lie within the same phenotypic spectrum. (wieczorek2014compoundheterozygosityof pages 1-2)

The evidence is predominantly **aggregated disease-level literature assembled from individually phenotyped families**, not population EHR data. The 2014 study evaluated 11 families and found the relevant biallelic TXNL4A genotype in 9. (wieczorek2014compoundheterozygosityof pages 1-2, wieczorek2014compoundheterozygosityof pages 3-4)

**Key abstract statement:** the discovery report described BMKS as a rare autosomal-recessive condition “characterized by bilateral choanal atresia” with characteristic craniofacial anomalies and identified biallelic TXNL4A mutations. (wieczorek2014compoundheterozygosityof pages 1-2)

---

## 2. Etiology

### Causal factor

The cause is genetic: insufficient TXNL4A dosage from **biallelic germline variants**. The common configuration combines a low-frequency promoter deletion with a severe coding or copy-number loss on the other chromosome. Heterozygous relatives can be unaffected, arguing against ordinary monoallelic haploinsufficiency. (wieczorek2014compoundheterozygosityof pages 4-6)

### Genetic risk factors

- TXNL4A 34-bp promoter deletion D1/type 1: **chr18:g.77,748,581_77,748,614del** in the reference used by the 2014 report.
- D2/type 2: **chr18:g.77,748,604_77,748,637del**.
- Reported loss-of-function examples include **c.349G>T, p.(Glu117Ter)**; **c.37C>T, p.(Gln13Ter)**; and **c.131delT, p.(Val44AlafsTer48)**.
- Larger terminal 18q deletions encompassing TXNL4A, ranging from approximately 0.484 to 4.7 Mb in the discovery series, can constitute one allele. (wieczorek2014compoundheterozygosityof pages 3-4, wieczorek2014compoundheterozygosityof pages 4-6)

The type-1 promoter deletion had an estimated allele frequency of **0.76%** in the original study. Its predicted homozygous frequency was approximately 1 in 17,300, but homozygosity for that allele was not established as equivalent to classic BMKS; pathogenicity depends on allelic context and residual expression. (wieczorek2014compoundheterozygosityof pages 1-2, wieczorek2014compoundheterozygosityof pages 7-8)

### Environmental, infectious, and lifestyle risk factors

No toxin, infection, diet, smoking, occupation, parental age, or lifestyle exposure has been demonstrated to cause or modify BMKS. It is not infectious or multifactorial on present evidence.

### Protective factors and gene–environment interaction

No protective allele, environmental protective factor, modifier gene, or reproducible gene–environment interaction has been reported. Avoidance of ordinary environmental exposures cannot prevent the inherited developmental defect.

---

## 3. Phenotypes

All manifestations are congenital or developmentally determined. Exact percentages are unavailable for most findings because published cohorts are extremely small and ascertainment is non-uniform.

| Phenotype | Type, onset, frequency/course | Functional impact | Suggested HPO term |
|---|---|---|---|
| Bilateral choanal atresia/stenosis | Structural sign; neonatal; reported as universal in the 2020 synthesis | Potential neonatal airway emergency; feeding and breathing impairment; surgical burden | Choanal atresia; Bilateral choanal atresia |
| Hearing loss | Sensorineural and/or conductive impairment; congenital/childhood; recurrent but not quantified | Speech-language, educational, and social effects; severe cases may need implantation | Hearing impairment; Sensorineural hearing impairment; Conductive hearing impairment |
| Cleft lip/palate, bifid uvula | Congenital structural signs; variable | Feeding, speech, dental, and middle-ear morbidity | Cleft palate; Cleft lip; Bifid uvula |
| Short palpebral fissures | Congenital dysmorphism; characteristic | Primarily morphological | Short palpebral fissure |
| Lower-eyelid coloboma | Congenital ocular/adnexal sign; variable | Exposure and ocular-surface risk depending on severity | Coloboma of eyelid |
| Prominent nose/high nasal bridge | Congenital facial morphology; characteristic | Primarily morphological | Prominent nose; High nasal bridge |
| Short philtrum, thin lips, small mouth/chin or micrognathia | Congenital; variable | Feeding, dental, airway, and speech consequences can occur | Short philtrum; Thin upper lip vermilion; Microstomia; Micrognathia |
| Large/protruding ears, preauricular tags | Congenital; variable | Cosmetic and audiological relevance | Large ears; Protruding ear; Preauricular skin tag |
| Congenital heart defects | Variable: patent foramen ovale, persistent ductus arteriosus and other defects reported | Depends on anatomy and hemodynamic significance | Congenital heart defect; Patent ductus arteriosus |
| Renal agenesis | Rare reported associated anomaly | Reduced renal reserve when unilateral; severe if bilateral | Renal agenesis |
| Imperforate anus | Rare congenital anomaly | Neonatal obstruction requiring surgery | Anal atresia |
| Clinodactyly/hallux valgus | Variable skeletal signs | Usually mild functional effect | Clinodactyly of the fifth finger; Hallux valgus |
| Short stature | Variable | Growth and psychosocial effects | Short stature |
| Intellectual disability | Usually absent; one severe case highlighted | Potential major lifelong support need in the exceptional case | Intellectual disability |

The clinical series also reported hypertelorism and inguinal hernia. Intellectual development is generally normal, so severe intellectual disability should prompt assessment for a larger deletion, blended diagnosis, complications, or expanded phenotype. (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 3-4, wieczorek2014compoundheterozygosityof pages 2-3)

No BMKS-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or disease-specific quality-of-life data were found. Quality-of-life effects above are clinically plausible consequences of the lesions, not measured BMKS outcomes.

---

## 4. Genetic and molecular information

### Causal gene

**TXNL4A** at 18q23, also called **DIB1**, encodes an essential U5 small nuclear ribonucleoprotein component. A current HGNC identifier and transcript accession should be imported directly from HGNC/NCBI for production annotation because reference-transcript differences affect variant nomenclature.

### Variant classes and interpretation

Established disease alleles include promoter deletions, nonsense and frameshift variants, splice-disrupting variants, intragenic/terminal copy-number deletions, and possibly other severe loss-of-function alleles. They are constitutional **germline** variants, not somatic mutations. The original severe coding variants were absent from 1000 Genomes, dbSNP, and approximately 3,000 control exomes available at the time. (wieczorek2014compoundheterozygosityof pages 4-6)

D1 and D2 reduced promoter activity by **59% and 72%**, respectively. Classic BMKS therefore appears to require residual expression: a hypomorphic regulatory allele paired with a null allele, or an appropriate biallelic hypomorphic configuration. Complete biallelic null loss is considered likely incompatible with life because DIB1 is essential in experimental organisms. (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 7-8)

Variant classifications should nevertheless be checked in current ClinVar and assessed using ACMG/AMP rules, including noncoding-variant guidance. A common promoter allele should not be called pathogenic in isolation; phase, second-allele severity, phenotype, segregation, and functional evidence are essential.

### Modifiers, epigenetics, and chromosomal abnormalities

No validated modifier gene or BMKS-specific DNA-methylation/chromatin signature is known. Large 18q deletions may broaden the phenotype through contiguous-gene effects. No recurrent aneuploidy, balanced translocation, or inversion defines BMKS. (wieczorek2014compoundheterozygosityof pages 3-4, wieczorek2014compoundheterozygosityof pages 4-6)

---

## 5. Environmental information

No environmental toxin, radiation exposure, pollutant, occupational factor, diet, alcohol, smoking behavior, or infectious agent is causally associated with BMKS. Environmental influences may affect general pregnancy or postoperative outcomes but are not established components of disease etiology. CTD-style chemical–disease assertions should therefore not be populated as causal without separate evidence.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic defect:** biallelic TXNL4A alleles lower functional protein dosage.
2. **Spliceosomal defect:** insufficient TXNL4A/DIB1 compromises U5-snRNP and U4/U6.U5 tri-snRNP assembly and control of spliceosome activation.
3. **Selective RNA-processing vulnerability:** transcripts with particular exon/intron architecture and weaker splice sites are disproportionately mis-spliced rather than all transcripts failing uniformly.
4. **Developmental signaling disturbance:** neural-crest-relevant expression programs, cell adhesion, WNT/β-catenin signaling, and EMT become abnormal.
5. **Cellular phenotype:** reduced proliferation, delayed/failed neural-crest differentiation and EMT, and—in Xenopus—excess dorsal-ectoderm/neural-crest apoptosis deplete or impair cranial neural-crest progenitors.
6. **Tissue phenotype:** deficient formation of neural-crest-derived craniofacial cartilage, bone, and nasal/choanal structures produces choanal atresia and facial dysostosis. (wieczorek2014compoundheterozygosityof pages 7-8, wood2020modellingthedevelopmental pages 37-41, park2022thecoresplicing pages 1-2)

### Human iPSC/iNCC evidence

Patient iPSCs proliferated **52% more slowly than maternal cells and 65% more slowly than unrelated controls**, without increased apoptosis. RNA sequencing identified 1,181 differentially expressed genes and **1,511 alternative-splicing events in 1,096 genes**; 1,154 were exon-skipping events. (wood2020modellingthedevelopmental pages 24-27, wood2020modellingthedevelopmental pages 21-24)

After neural-crest differentiation, there were **5,746 differentially expressed genes** and **2,991 differential-splicing events in 2,029 genes**; 88% of affected splicing events were iNCC-specific. Patient cells retained epithelial markers and had reduced mesenchymal/neural-crest markers, with an EMT score of −5 versus +5 in maternal and +8 in unrelated-control cells. Extending differentiation to 168 hours did not rescue the defect. (wood2020modellingthedevelopmental pages 34-37, wood2020modellingthedevelopmental pages 27-31, wood2020modellingthedevelopmental pages 69-74)

AXIN2 was downregulated (p=0.0004), supporting reduced WNT activation. Abnormal inclusion of **TCF7L2 exon 4**, which is associated with a dampened WNT response, was proposed as one mechanistic link. This is a leading model, not yet proof that TCF7L2 alone causes the human phenotype. (wood2020modellingthedevelopmental pages 34-37, wood2020modellingthedevelopmental pages 27-31)

**Exact abstract excerpt from the 2020 preprint:** “Patient iPSCs displayed defective differentiation into iNCCs … in particular a delay in undergoing an epithelial-to-mesenchymal transition (EMT).” The abstract further reports “a dampened response to WNT signalling” and identifies TCF7L2 exon-4 mis-splicing as a potential cause. (wood2020modellingthedevelopmental pages 1-5, wood2020modellingthedevelopmental pages 37-41)

### Model-organism evidence

In Xenopus, 30-ng Txnl4a morpholino knockdown reduced **sox10** in 85.7% and **tfap2e** in 32.4% of embryos; morpholino-resistant txnl4a increased normal sox10 expression from 14% to 62%, supporting specificity. TUNEL-positive apoptosis increased in dorsal ectoderm at stage 15 (n=41, p<0.0005), and 38% of stage-45 morphants showed craniofacial cartilage defects (p<0.0001). (park2022thecoresplicing pages 7-10, park2022thecoresplicing pages 4-7)

### Ontology suggestions

- **GO biological process:** mRNA splicing via spliceosome; spliceosomal complex assembly; neural crest cell development; epithelial-to-mesenchymal transition; canonical WNT signaling; regulation of apoptotic process; craniofacial morphogenesis; cartilage development.
- **GO cellular component:** spliceosomal complex; U5 snRNP; U4/U6.U5 tri-snRNP; nucleus/nucleoplasm.
- **Cell Ontology:** neural crest cell; cranial neural crest cell; craniofacial chondrocyte; osteoblast progenitor; craniofacial mesenchymal cell. Exact CL identifiers should be ontology-validated before ingestion.

No BMKS-specific proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, epigenomic, organoid, or in-vivo CRISPR-screen dataset was identified. The iPSC experiment is bulk transcriptomic evidence from one family, a major limitation. (wood2020modellingthedevelopmental pages 37-41, wood2020modellingthedevelopmental pages 45-49)

---

## 7. Anatomical structures affected

### Primary structures

- Posterior nasal apertures/choanae and nasal airway.
- Craniofacial skeleton and neural-crest-derived cartilage.
- Palate and lip.
- Eyelids and periocular region.
- External/middle/inner auditory system, depending on the basis of hearing loss.

### Secondary or variable structures

Heart and great-vessel derivatives, kidney, anus/rectum, digits, feet, and inguinal region can be involved. (wieczorek2014compoundheterozygosityof pages 3-4, wieczorek2014compoundheterozygosityof pages 2-3)

**Suggested anatomy terms:** choana; nasal cavity; nasopharynx; palate; mandible; eyelid; external ear; middle ear; inner ear; craniofacial skeleton; heart; kidney; anus. Exact UBERON identifiers should be resolved against the active release. Bilateral involvement is characteristic for choanal atresia; other anomalies may be unilateral, bilateral, or asymmetric.

At the subcellular level, the primary compartment is the **nuclear spliceosome**, especially the U5 and U4/U6.U5 snRNP assemblies.

---

## 8. Temporal development

BMKS begins during embryogenesis and is clinically evident at birth. Bilateral choanal atresia can present acutely with neonatal respiratory compromise, whereas hearing, speech, dental, growth, and educational consequences become clearer through childhood.

The underlying malformations are stable congenital lesions rather than relapsing or degenerative disease. Functional morbidity may evolve with growth or after reconstructive procedures. There are no validated disease stages, progression rate, remission pattern, or longitudinal natural-history model. Critical developmental vulnerability probably coincides with cranial neural-crest specification, EMT, migration, and craniofacial morphogenesis; clinically, birth is the critical airway-intervention window. (wood2020modellingthedevelopmental pages 1-5, park2022thecoresplicing pages 7-10)

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive.
- **Recurrence risk:** when both parents carry relevant alleles, each pregnancy conventionally has a 25% probability of an affected child, 50% of a carrier, and 25% of inheriting neither familial allele, subject to confirmation of phase and variant pathogenicity.
- **Penetrance:** apparently high for appropriately damaging biallelic genotypes, but not numerically estimable.
- **Expressivity:** variable for clefting, hearing loss, heart/renal/anal defects, growth, and neurodevelopment.
- **Anticipation:** not expected and not reported.
- **Germline mosaicism:** not established.
- **Consanguinity:** can facilitate homozygosity; one consanguineous family was homozygous for the D2 promoter deletion. (wieczorek2014compoundheterozygosityof pages 1-2)
- **Founder effect:** no confirmed founder population was identified.
- **Carrier frequency:** cannot be equated with the 0.76% D1 allele frequency because multiple alleles and genotype-dependent pathogenicity are involved.

Fewer than 20 families were reported worldwide by 2020. No defensible cases-per-100,000 prevalence, annual incidence, geographic concentration, ethnic enrichment, age distribution, or sex ratio is available. (wood2020modellingthedevelopmental pages 1-5)

---

## 10. Diagnostics

### Clinical recognition and immediate evaluation

Suspect BMKS in a neonate or child with bilateral choanal atresia/stenosis plus the characteristic oculo-oto-facial pattern, clefting, hearing loss, or congenital heart disease. Immediate priorities are airway patency, feeding, and cardiorespiratory stability.

A reasonable phenotype-directed work-up includes nasal endoscopy and thin-section CT for choanal anatomy; formal audiology; ophthalmologic assessment; cleft/craniofacial examination; echocardiography; renal ultrasonography; assessment for anal patency, feeding, growth, development, and speech. These are anomaly-directed clinical practices; no BMKS-specific consensus protocol was found.

### Molecular testing

1. **Preferred:** a craniofacial/choanal-atresia panel or genome analysis that includes TXNL4A coding exons, splice regions, the recurrent promoter interval, and copy-number analysis.
2. **WES:** can identify coding loss-of-function alleles but may miss the 34-bp promoter deletion and some CNVs.
3. **WGS:** potentially best single assay because it can interrogate coding, promoter, and structural alleles, provided the pipeline calls and interprets the repetitive promoter region reliably.
4. **Targeted testing:** PCR/fragment analysis or Sanger sequencing for D1/D2 plus sequencing of coding/splice regions in a strongly suggestive case.
5. **CMA/MLPA:** useful when a deletion encompassing TXNL4A is suspected; the discovery study used microarray and MLPA.
6. Karyotype, FISH, mtDNA, and repeat-expansion testing have no routine disease-specific role unless another diagnosis is suspected. (wieczorek2014compoundheterozygosityof pages 3-4, wieczorek2014compoundheterozygosityof pages 4-6)

Confirm trans configuration through parental testing. RNA analysis or promoter functional studies may help resolve unusual splice/regulatory VUS but are not validated routine biomarkers.

### Differential diagnosis

Important alternatives include CHARGE syndrome/CHD7 disorder; Treacher Collins syndrome (**TCOF1, POLR1D, POLR1C**); mandibulofacial dysostosis with microcephaly (**EFTUD2**); Nager syndrome (**SF3B4**); cerebro-costo-mandibular syndrome (**SNRPB**); Miller syndrome (**DHODH**); craniofacial microsomia; isolated choanal atresia; and 18q deletion syndromes. BMKS is favored by bilateral choanal atresia together with short palpebral fissures, lower-eyelid coloboma, prominent high-bridged nose, short philtrum, large ears, hearing loss, clefting, usually normal intellect, and biallelic TXNL4A variants. Oculo-oto-facial dysplasia may overlap the same spectrum. (wieczorek2014compoundheterozygosityof pages 2-3, wieczorek2014compoundheterozygosityof pages 1-2)

No biochemical, histopathologic, electrophysiologic, circulating, proteomic, metabolomic, or liquid-biopsy marker is established. There are no standardized diagnostic criteria beyond phenotype plus molecular confirmation.

---

## 11. Outcome and prognosis

No 5- or 10-year survival estimate, life expectancy, disease-specific mortality rate, disability score, or validated prognostic biomarker exists. The main immediate risk is neonatal airway obstruction from bilateral choanal atresia. Longer-term morbidity is expected to reflect restenosis or repeated airway procedures, hearing and speech impairment, cleft-related feeding/dental problems, and the severity of cardiac, renal, or anorectal anomalies.

Normal intellectual development is typical, but rare severe disability has been reported. Recovery means correction or adaptation to individual malformations; the constitutional molecular defect is lifelong. Prognosis is therefore anatomy-dependent rather than governed by a validated TXNL4A genotype score. (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 2-3)

---

## 12. Treatment

There is no approved TXNL4A-directed therapy, pharmacotherapy, gene therapy, RNA therapy, cell therapy, or splice-correcting treatment.

### Current clinical management

- **Bilateral choanal atresia:** emergency airway stabilization followed by definitive otolaryngologic repair, generally using an endoscopic transnasal approach according to anatomy and local expertise; monitor for restenosis.
- **Hearing loss:** serial audiology, hearing aids or bone-conduction devices as appropriate, and cochlear-implant assessment for severe sensorineural loss. Cochlear implantation was contemplated in reported BMKS care. (wieczorek2014compoundheterozygosityof pages 2-3)
- **Cleft lip/palate:** multidisciplinary craniofacial repair, feeding support, dental/orthodontic care, and speech-language therapy.
- **Eyelid coloboma:** ocular-surface protection and ophthalmic reconstruction when indicated.
- **Cardiac, renal, anorectal, and hernia anomalies:** standard specialty-specific surveillance and surgery.
- **Development:** early-intervention, educational, occupational, and speech support based on individual assessment.

Suggested NCIT intervention concepts include surgical procedure, reconstructive surgery, airway management, hearing aid, cochlear implantation, speech therapy, genetic counseling, and supportive care; exact NCIT codes should be terminology-validated.

No treatment-response rate, comparative surgical outcome, pharmacogenomic recommendation, or BMKS-specific adverse-event profile was found. The ClinicalTrials.gov search identified **no relevant BMKS interventional study or NCT identifier**.

The WNT/TCF7L2 and apoptosis findings are mechanistic research leads, not justification for prenatal or postnatal WNT- or apoptosis-targeted therapy. (wood2020modellingthedevelopmental pages 34-37, park2022thecoresplicing pages 7-10)

---

## 13. Prevention

Primary lifestyle or vaccine prevention is not applicable. Evidence-based prevention is reproductive and complication-focused:

- Offer genetic counseling and parental testing after molecular confirmation.
- Provide cascade testing to at-risk adult relatives for the known familial alleles.
- For a known familial genotype, discuss prenatal diagnosis by chorionic-villus sampling or amniocentesis and preimplantation genetic testing for monogenic disease.
- Ensure assays test both the promoter deletion and the family’s second allele.
- Targeted fetal imaging may detect clefting or major associated anomalies but cannot exclude BMKS or reliably establish choanal patency.
- Tertiary prevention consists of early airway treatment, newborn/serial hearing assessment, feeding support, cardiac and renal evaluation, and timely craniofacial intervention.

BMKS is not part of standard biochemical newborn screening, and population carrier screening is not established.

---

## 14. Other species and natural disease

No naturally occurring veterinary syndrome definitively homologous to human BMKS was identified, and there is no zoonotic or cross-species transmission. TXNL4A/DIB1 function is evolutionarily conserved. Experimental ortholog evidence exists in:

- *Saccharomyces cerevisiae* DIB1: depletion reduces U4/U6.U5 tri-snRNP assembly.
- *Caenorhabditis elegans*: null ortholog loss is reported as lethal in the disease-model literature.
- *Xenopus laevis*: experimentally reduced txnl4a produces neural-crest and craniofacial defects. (wood2020modellingthedevelopmental pages 1-5, wieczorek2014compoundheterozygosityof pages 7-8, park2022thecoresplicing pages 2-4)

These are induced models, not natural animal disease. Exact NCBI Taxonomy and ortholog Gene IDs should be imported from NCBI/Alliance rather than inferred here.

---

## 15. Model organisms and experimental systems

### Yeast

Conditional DIB1 depletion models the upstream spliceosome defect and demonstrated impaired tri-snRNP assembly. It is powerful for molecular spliceosome biology but cannot model vertebrate neural crest or facial anatomy. (wieczorek2014compoundheterozygosityof pages 7-8)

### Patient-derived iPSCs and induced neural-crest cells

Peripheral blood cells from one affected individual and her unaffected carrier mother were reprogrammed and compared with unrelated controls. This system recapitulated reduced proliferation, extensive mis-splicing, diminished WNT response, and delayed EMT during neural-crest differentiation. Its strengths are human genetic context and disease-relevant cell lineage; limitations include one family, a patient with atypical severe intellectual disability, non-isogenic controls, bulk RNA sequencing, and preprint publication status. (wood2020modellingthedevelopmental pages 37-41, wood2020modellingthedevelopmental pages 1-5, wood2020modellingthedevelopmental pages 45-49)

### Xenopus

Morpholino knockdown at the two-cell stage reduced neural-crest markers, increased apoptosis, and produced craniofacial-cartilage defects; partial rescue with morpholino-resistant txnl4a supports on-target action. Limitations include transient knockdown, incomplete phenotype penetrance, dosage sensitivity, and absence of the precise human promoter/compound-heterozygous architecture. (park2022thecoresplicing pages 7-10, park2022thecoresplicing pages 2-4)

No published BMKS-specific knock-in mouse, zebrafish germline mutant, patient organoid, or isogenic CRISPR-corrected iPSC model was identified in the retrieved literature. The highest-value next steps are isogenic correction/introduction of D1 and D2 alleles, multiple-patient iPSC cohorts, single-cell time courses of cranial neural-crest differentiation, direct spliceosome-complex proteomics, and animal knock-in models reproducing human residual TXNL4A dosage.

---

## Key publications

1. **Wieczorek et al.** “Compound heterozygosity of low-frequency promoter deletions and rare loss-of-function mutations in TXNL4A causes Burn-McKeown syndrome.” *American Journal of Human Genetics* 95:698–707. Published December 2014. DOI/URL: https://doi.org/10.1016/j.ajhg.2014.10.014. This is the landmark human genetic and functional study. (wieczorek2014compoundheterozygosityof pages 1-2, wieczorek2014compoundheterozygosityof pages 4-6)
2. **Wood et al.** “Modelling the developmental spliceosomal craniofacial disorder Burn-McKeown syndrome using induced pluripotent stem cells.” bioRxiv preprint, posted May 14, 2020. DOI/URL: https://doi.org/10.1101/2020.05.13.094029. This is the principal patient-derived transcriptomic/mechanistic study but was retrieved as a preprint. (wood2020modellingthedevelopmental pages 1-5, wood2020modellingthedevelopmental pages 37-41)
3. **Park et al.** “The Core Splicing Factors EFTUD2, SNRPB and TXNL4A Are Essential for Neural Crest and Craniofacial Development.” *Journal of Developmental Biology* 10:29. Published July 2022. DOI/URL: https://doi.org/10.3390/jdb10030029. This provides the principal TXNL4A Xenopus knockdown/rescue evidence. (park2022thecoresplicing pages 7-10, park2022thecoresplicing pages 1-2)

PMIDs were not consistently exposed by the retrieved full-text records and have therefore not been guessed. For database ingestion, they should be resolved through PubMed using the exact titles/DOIs above.

## Overall evidence assessment

The causal association between biallelic TXNL4A insufficiency and BMKS is strong, based on segregation across multiple human families plus promoter assays and conserved functional evidence. The detailed WNT/TCF7L2–EMT mechanism is biologically coherent but rests principally on one-family, preprint iPSC data and should be represented as **supported/provisional**, not definitive. Xenopus data independently support neural-crest progenitor loss and craniofacial consequences. Clinical epidemiology, longitudinal outcome, quality of life, genotype–phenotype prediction, standardized management, and disease-modifying treatment remain major evidence gaps.

References

1. (wood2020modellingthedevelopmental pages 1-5): Katherine A. Wood, Charlie F. Rowlands, Huw B. Thomas, Steven Woods, Julieta O’Flaherty, Sofia Douzgou, Susan J. Kimber, William G. Newman, and Raymond T. O’Keefe. Modelling the developmental spliceosomal craniofacial disorder burn-mckeown syndrome using induced pluripotent stem cells. BioRxiv, May 2020. URL: https://doi.org/10.1101/2020.05.13.094029, doi:10.1101/2020.05.13.094029. This article has 30 citations.

2. (wieczorek2014compoundheterozygosityof pages 1-2): Dagmar Wieczorek, William G. Newman, Thomas Wieland, Tea Berulava, Maria Kaffe, Daniela Falkenstein, Christian Beetz, Elisabeth Graf, Thomas Schwarzmayr, Sofia Douzgou, Jill Clayton-Smith, Sarah B. Daly, Simon G. Williams, Sanjeev S. Bhaskar, Jill E. Urquhart, Beverley Anderson, James O’Sullivan, Odile Boute, Jasmin Gundlach, Johanna Christina Czeschik, Anthonie J. van Essen, Filiz Hazan, Sarah Park, Anne Hing, Alma Kuechler, Dietmar R. Lohmann, Kerstin U. Ludwig, Elisabeth Mangold, Laura Steenpaß, Michael Zeschnigk, Johannes R. Lemke, Charles Marques Lourenco, Ute Hehr, Eva-Christina Prott, Melanie Waldenberger, Anne C. Böhmer, Bernhard Horsthemke, Raymond T. O’Keefe, Thomas Meitinger, John Burn, Hermann-Josef Lüdecke, and Tim M. Strom. Compound heterozygosity of low-frequency promoter deletions and rare loss-of-function mutations in txnl4a causes burn-mckeown syndrome. American journal of human genetics, 95 6:698-707, Dec 2014. URL: https://doi.org/10.1016/j.ajhg.2014.10.014, doi:10.1016/j.ajhg.2014.10.014. This article has 78 citations and is from a highest quality peer-reviewed journal.

3. (wieczorek2014compoundheterozygosityof pages 7-8): Dagmar Wieczorek, William G. Newman, Thomas Wieland, Tea Berulava, Maria Kaffe, Daniela Falkenstein, Christian Beetz, Elisabeth Graf, Thomas Schwarzmayr, Sofia Douzgou, Jill Clayton-Smith, Sarah B. Daly, Simon G. Williams, Sanjeev S. Bhaskar, Jill E. Urquhart, Beverley Anderson, James O’Sullivan, Odile Boute, Jasmin Gundlach, Johanna Christina Czeschik, Anthonie J. van Essen, Filiz Hazan, Sarah Park, Anne Hing, Alma Kuechler, Dietmar R. Lohmann, Kerstin U. Ludwig, Elisabeth Mangold, Laura Steenpaß, Michael Zeschnigk, Johannes R. Lemke, Charles Marques Lourenco, Ute Hehr, Eva-Christina Prott, Melanie Waldenberger, Anne C. Böhmer, Bernhard Horsthemke, Raymond T. O’Keefe, Thomas Meitinger, John Burn, Hermann-Josef Lüdecke, and Tim M. Strom. Compound heterozygosity of low-frequency promoter deletions and rare loss-of-function mutations in txnl4a causes burn-mckeown syndrome. American journal of human genetics, 95 6:698-707, Dec 2014. URL: https://doi.org/10.1016/j.ajhg.2014.10.014, doi:10.1016/j.ajhg.2014.10.014. This article has 78 citations and is from a highest quality peer-reviewed journal.

4. (wood2020modellingthedevelopmental pages 37-41): Katherine A. Wood, Charlie F. Rowlands, Huw B. Thomas, Steven Woods, Julieta O’Flaherty, Sofia Douzgou, Susan J. Kimber, William G. Newman, and Raymond T. O’Keefe. Modelling the developmental spliceosomal craniofacial disorder burn-mckeown syndrome using induced pluripotent stem cells. BioRxiv, May 2020. URL: https://doi.org/10.1101/2020.05.13.094029, doi:10.1101/2020.05.13.094029. This article has 30 citations.

5. (park2022thecoresplicing pages 7-10): Byung-Yong Park, Melanie Tachi-Duprat, Chibuike Ihewulezi, Arun Devotta, and Jean-Pierre Saint-Jeannet. The core splicing factors eftud2, snrpb and txnl4a are essential for neural crest and craniofacial development. Journal of Developmental Biology, 10:29, Jul 2022. URL: https://doi.org/10.3390/jdb10030029, doi:10.3390/jdb10030029. This article has 27 citations.

6. (wieczorek2014compoundheterozygosityof pages 4-6): Dagmar Wieczorek, William G. Newman, Thomas Wieland, Tea Berulava, Maria Kaffe, Daniela Falkenstein, Christian Beetz, Elisabeth Graf, Thomas Schwarzmayr, Sofia Douzgou, Jill Clayton-Smith, Sarah B. Daly, Simon G. Williams, Sanjeev S. Bhaskar, Jill E. Urquhart, Beverley Anderson, James O’Sullivan, Odile Boute, Jasmin Gundlach, Johanna Christina Czeschik, Anthonie J. van Essen, Filiz Hazan, Sarah Park, Anne Hing, Alma Kuechler, Dietmar R. Lohmann, Kerstin U. Ludwig, Elisabeth Mangold, Laura Steenpaß, Michael Zeschnigk, Johannes R. Lemke, Charles Marques Lourenco, Ute Hehr, Eva-Christina Prott, Melanie Waldenberger, Anne C. Böhmer, Bernhard Horsthemke, Raymond T. O’Keefe, Thomas Meitinger, John Burn, Hermann-Josef Lüdecke, and Tim M. Strom. Compound heterozygosity of low-frequency promoter deletions and rare loss-of-function mutations in txnl4a causes burn-mckeown syndrome. American journal of human genetics, 95 6:698-707, Dec 2014. URL: https://doi.org/10.1016/j.ajhg.2014.10.014, doi:10.1016/j.ajhg.2014.10.014. This article has 78 citations and is from a highest quality peer-reviewed journal.

7. (wieczorek2014compoundheterozygosityof pages 3-4): Dagmar Wieczorek, William G. Newman, Thomas Wieland, Tea Berulava, Maria Kaffe, Daniela Falkenstein, Christian Beetz, Elisabeth Graf, Thomas Schwarzmayr, Sofia Douzgou, Jill Clayton-Smith, Sarah B. Daly, Simon G. Williams, Sanjeev S. Bhaskar, Jill E. Urquhart, Beverley Anderson, James O’Sullivan, Odile Boute, Jasmin Gundlach, Johanna Christina Czeschik, Anthonie J. van Essen, Filiz Hazan, Sarah Park, Anne Hing, Alma Kuechler, Dietmar R. Lohmann, Kerstin U. Ludwig, Elisabeth Mangold, Laura Steenpaß, Michael Zeschnigk, Johannes R. Lemke, Charles Marques Lourenco, Ute Hehr, Eva-Christina Prott, Melanie Waldenberger, Anne C. Böhmer, Bernhard Horsthemke, Raymond T. O’Keefe, Thomas Meitinger, John Burn, Hermann-Josef Lüdecke, and Tim M. Strom. Compound heterozygosity of low-frequency promoter deletions and rare loss-of-function mutations in txnl4a causes burn-mckeown syndrome. American journal of human genetics, 95 6:698-707, Dec 2014. URL: https://doi.org/10.1016/j.ajhg.2014.10.014, doi:10.1016/j.ajhg.2014.10.014. This article has 78 citations and is from a highest quality peer-reviewed journal.

8. (wieczorek2014compoundheterozygosityof pages 2-3): Dagmar Wieczorek, William G. Newman, Thomas Wieland, Tea Berulava, Maria Kaffe, Daniela Falkenstein, Christian Beetz, Elisabeth Graf, Thomas Schwarzmayr, Sofia Douzgou, Jill Clayton-Smith, Sarah B. Daly, Simon G. Williams, Sanjeev S. Bhaskar, Jill E. Urquhart, Beverley Anderson, James O’Sullivan, Odile Boute, Jasmin Gundlach, Johanna Christina Czeschik, Anthonie J. van Essen, Filiz Hazan, Sarah Park, Anne Hing, Alma Kuechler, Dietmar R. Lohmann, Kerstin U. Ludwig, Elisabeth Mangold, Laura Steenpaß, Michael Zeschnigk, Johannes R. Lemke, Charles Marques Lourenco, Ute Hehr, Eva-Christina Prott, Melanie Waldenberger, Anne C. Böhmer, Bernhard Horsthemke, Raymond T. O’Keefe, Thomas Meitinger, John Burn, Hermann-Josef Lüdecke, and Tim M. Strom. Compound heterozygosity of low-frequency promoter deletions and rare loss-of-function mutations in txnl4a causes burn-mckeown syndrome. American journal of human genetics, 95 6:698-707, Dec 2014. URL: https://doi.org/10.1016/j.ajhg.2014.10.014, doi:10.1016/j.ajhg.2014.10.014. This article has 78 citations and is from a highest quality peer-reviewed journal.

9. (wood2020modellingthedevelopmental pages 24-27): Katherine A. Wood, Charlie F. Rowlands, Huw B. Thomas, Steven Woods, Julieta O’Flaherty, Sofia Douzgou, Susan J. Kimber, William G. Newman, and Raymond T. O’Keefe. Modelling the developmental spliceosomal craniofacial disorder burn-mckeown syndrome using induced pluripotent stem cells. BioRxiv, May 2020. URL: https://doi.org/10.1101/2020.05.13.094029, doi:10.1101/2020.05.13.094029. This article has 30 citations.

10. (wood2020modellingthedevelopmental pages 27-31): Katherine A. Wood, Charlie F. Rowlands, Huw B. Thomas, Steven Woods, Julieta O’Flaherty, Sofia Douzgou, Susan J. Kimber, William G. Newman, and Raymond T. O’Keefe. Modelling the developmental spliceosomal craniofacial disorder burn-mckeown syndrome using induced pluripotent stem cells. BioRxiv, May 2020. URL: https://doi.org/10.1101/2020.05.13.094029, doi:10.1101/2020.05.13.094029. This article has 30 citations.

11. (wood2020modellingthedevelopmental pages 69-74): Katherine A. Wood, Charlie F. Rowlands, Huw B. Thomas, Steven Woods, Julieta O’Flaherty, Sofia Douzgou, Susan J. Kimber, William G. Newman, and Raymond T. O’Keefe. Modelling the developmental spliceosomal craniofacial disorder burn-mckeown syndrome using induced pluripotent stem cells. BioRxiv, May 2020. URL: https://doi.org/10.1101/2020.05.13.094029, doi:10.1101/2020.05.13.094029. This article has 30 citations.

12. (wood2020modellingthedevelopmental pages 34-37): Katherine A. Wood, Charlie F. Rowlands, Huw B. Thomas, Steven Woods, Julieta O’Flaherty, Sofia Douzgou, Susan J. Kimber, William G. Newman, and Raymond T. O’Keefe. Modelling the developmental spliceosomal craniofacial disorder burn-mckeown syndrome using induced pluripotent stem cells. BioRxiv, May 2020. URL: https://doi.org/10.1101/2020.05.13.094029, doi:10.1101/2020.05.13.094029. This article has 30 citations.

13. (wood2020modellingthedevelopmental pages 21-24): Katherine A. Wood, Charlie F. Rowlands, Huw B. Thomas, Steven Woods, Julieta O’Flaherty, Sofia Douzgou, Susan J. Kimber, William G. Newman, and Raymond T. O’Keefe. Modelling the developmental spliceosomal craniofacial disorder burn-mckeown syndrome using induced pluripotent stem cells. BioRxiv, May 2020. URL: https://doi.org/10.1101/2020.05.13.094029, doi:10.1101/2020.05.13.094029. This article has 30 citations.

14. (park2022thecoresplicing pages 4-7): Byung-Yong Park, Melanie Tachi-Duprat, Chibuike Ihewulezi, Arun Devotta, and Jean-Pierre Saint-Jeannet. The core splicing factors eftud2, snrpb and txnl4a are essential for neural crest and craniofacial development. Journal of Developmental Biology, 10:29, Jul 2022. URL: https://doi.org/10.3390/jdb10030029, doi:10.3390/jdb10030029. This article has 27 citations.

15. (park2022thecoresplicing pages 1-2): Byung-Yong Park, Melanie Tachi-Duprat, Chibuike Ihewulezi, Arun Devotta, and Jean-Pierre Saint-Jeannet. The core splicing factors eftud2, snrpb and txnl4a are essential for neural crest and craniofacial development. Journal of Developmental Biology, 10:29, Jul 2022. URL: https://doi.org/10.3390/jdb10030029, doi:10.3390/jdb10030029. This article has 27 citations.

16. (wood2020modellingthedevelopmental pages 45-49): Katherine A. Wood, Charlie F. Rowlands, Huw B. Thomas, Steven Woods, Julieta O’Flaherty, Sofia Douzgou, Susan J. Kimber, William G. Newman, and Raymond T. O’Keefe. Modelling the developmental spliceosomal craniofacial disorder burn-mckeown syndrome using induced pluripotent stem cells. BioRxiv, May 2020. URL: https://doi.org/10.1101/2020.05.13.094029, doi:10.1101/2020.05.13.094029. This article has 30 citations.

17. (park2022thecoresplicing pages 2-4): Byung-Yong Park, Melanie Tachi-Duprat, Chibuike Ihewulezi, Arun Devotta, and Jean-Pierre Saint-Jeannet. The core splicing factors eftud2, snrpb and txnl4a are essential for neural crest and craniofacial development. Journal of Developmental Biology, 10:29, Jul 2022. URL: https://doi.org/10.3390/jdb10030029, doi:10.3390/jdb10030029. This article has 27 citations.

## Artifacts

- [Edison artifact artifact-00](Burn-McKeown_Syndrome-deep-research-falcon_artifacts/artifact-00.md)