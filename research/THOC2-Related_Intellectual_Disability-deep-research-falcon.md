---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T23:39:57.128250'
end_time: '2026-07-31T23:48:04.424690'
duration_seconds: 487.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: THOC2-Related Intellectual Disability
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: THOC2-Related_Intellectual_Disability-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** THOC2-Related Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **THOC2-Related Intellectual Disability** covering all of the
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
- **Disease Name:** THOC2-Related Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **THOC2-Related Intellectual Disability** covering all of the
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


# THOC2-Related Intellectual Disability: Disease Characteristics Report

## Executive summary

THOC2-related intellectual disability is an ultra-rare, predominantly X-linked neurodevelopmental disorder caused by pathogenic or likely pathogenic germline variants in **THOC2**, which encodes the largest subunit of the nuclear TREX transcription–mRNA-export complex. Intellectual disability and speech/language impairment are central; hypotonia, gait or cerebellar-type motor abnormalities, seizures, behavioral abnormalities, short stature, microcephaly, low birth weight, and later truncal obesity occur variably. The best-supported mechanism is partial loss of THOC2/TREX function. A major 2024 study refined this to a causal chain of abnormal R-loop homeostasis, DNA damage, cell-cycle disruption and apoptosis during neurodevelopment, followed by neuronal migration, axonal, synaptic and network dysfunction. Evidence remains limited to small cohorts, patient cells and one hypomorphic mouse model; prevalence, longitudinal prognosis, validated biomarkers and disease-modifying treatments are unknown. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 1-3, bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2, bhattacharjee2024compromisedtranscriptionmrnaexport pages 13-14)

The following table summarizes the most actionable evidence and its limitations.

| domain | established finding | quantitative/variant detail | evidence type and year | evidence limitation |
|---|---|---|---|---|
| Disease naming / identifiers | A rare Mendelian neurodevelopmental disorder caused by pathogenic THOC2 variation; retrieved evidence supports names such as **THOC2-related intellectual disability**, **THOC2-associated neurodevelopmental disorder**, and **X-linked intellectual disability due to THOC2**. Do **not** assert MONDO/OMIM IDs here because they were not established in the retrieved evidence. (kumar2018severeneurocognitiveand pages 3-5, kumar2018severeneurocognitiveand pages 1-3) | Core phenotype is intellectual disability with variable syndromic features; THOC2 is on chromosome X and encodes the largest TREX subunit. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2, kumar2018severeneurocognitiveand pages 3-5) | Human clinical cohorts/reports, 2015 and 2018; mechanistic disease framing, 2024. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 1-3, bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2) | Naming is consistent across papers, but registry identifiers were not retrieved directly. |
| Inheritance | Established **X-linked** inheritance with affected hemizygous males in multigenerational families; also **de novo** disease in at least one affected female and additional de novo male cases. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 1-3, kumar2018severeneurocognitiveand pages 6-8) | 2015 cohort: 4 multigenerational families, 20 affected individuals. 2018 expansion: 6 affected individuals from 5 unrelated families plus 1 affected female with de novo p.Tyr517Cys. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 1-3, kumar2018severeneurocognitiveand pages 6-8) | Human pedigree/genomic evidence, 2015 and 2018. | Penetrance is not formally quantified; female manifestations appear uncommon and likely influenced by X-inactivation. |
| Sex effects / X-inactivation | Heterozygous mothers were usually clinically unaffected and showed highly skewed X-chromosome inactivation when tested. (kumar2018severeneurocognitiveand pages 8-10, kumar2018severeneurocognitiveand pages 6-8) | Reported XCI skewing included ~94%, 98:2%, and 99.9:0.1%. (kumar2018severeneurocognitiveand pages 6-8, kumar2018severeneurocognitiveand pages 26-27) | Human clinical/molecular evidence, 2018. | Small number of carrier females studied; cannot define full female penetrance spectrum. |
| Core phenotypes | Intellectual disability is the consistent core phenotype, often with speech/language impairment, hypotonia, gait disturbance, tremor, seizures/epileptic encephalopathy, growth abnormalities, and occasional behavioral/autism features. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 5-6, kumar2018severeneurocognitiveand pages 8-10) | 2015: severity ranged from borderline to severe; speech delay, short stature, elevated BMI/truncal obesity in older males in 2/4 families, seizure disorders, tremors, gait disturbance. (kumar2015thoc2mutationsimplicate pages 1-3) 2018 established series: all 7 had at least moderate ID; 2/7 non-ambulatory, 3/7 non-verbal, 4/7 behavioral problems, 1/7 ASD, 4/7 infantile hypotonia, 2/7 tremor, 1/7 confirmed seizures, 1/7 suspected seizures, 3/7 low birth weight, 2/7 microcephaly, 2/7 short stature. (kumar2018severeneurocognitiveand pages 5-6) | Human clinical cohort data, 2015 and 2018. | Frequencies are from small cohorts and partly enriched for severe referrals; not population estimates. |
| Neuroimaging / neurologic findings | Brain imaging can be normal or show nonspecific structural abnormalities; cerebellar-type signs may occur even without major cerebellar MRI abnormalities. (kumar2018severeneurocognitiveand pages 8-10, kumar2015thoc2mutationsimplicate pages 1-3) | 2018: abnormal MRI in 2/5 tested—cortical gyral changes, corpus callosum hypoplasia, reduced brainstem volume, lateral ventricle dilatation, delayed myelination, periventricular white matter lesions; 3/5 were normal. (kumar2018severeneurocognitiveand pages 5-6) 2015: mild ventriculomegaly, gliosis, inferior cerebellar vermis dysplasia, cervical cord compression reported in a limited subset. (kumar2015thoc2mutationsimplicate pages 1-3) | Human imaging observations, 2015 and 2018. | Imaging numbers are very small; no disease-specific radiologic signature established. |
| Established pathogenic / likely pathogenic variants | Established disease-causing variants include multiple missense and splice-altering THOC2 variants that reduce protein stability or create C-terminal truncation. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 6-8, kumar2018severeneurocognitiveand pages 5-6, kumar2018severeneurocognitiveand pages 8-10) | 2015 established missense variants: c.937C>T (p.Leu313Phe), c.1313T>C (p.Leu438Pro), c.2399T>C (p.Ile800Thr), c.3034T>C (p.Ser1012Pro). (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 3-5) 2018 established variants include p.Tyr517Cys, p.Thr696Ile, p.Gly713Asp, p.His1187Tyr, and splice variants c.4450-2A>G and c.3503+4A>C / p.Gly1168fs7*. (kumar2018severeneurocognitiveand pages 1-3, kumar2018severeneurocognitiveand pages 6-8, kumar2018severeneurocognitiveand pages 5-6) | Human genomic + functional evidence, 2015 and 2018. | Variant list is restricted to retrieved papers; no contemporaneous ClinVar aggregation was retrieved. |
| VUS / candidate variants | Additional rare missense THOC2 variants were reported as **variants of uncertain significance** rather than established causes. (kumar2018severeneurocognitiveand pages 10-11) | Reported VUS: p.Arg77Cys, p.Ser1108Leu, p.Arg1121Gly, p.Asn1261His. They were rare/conserved and in silico-predicted damaging but lacked sufficient functional confirmation. (kumar2018severeneurocognitiveand pages 10-11) | Human genomic interpretation, 2018. | These should not be treated as confirmed causal variants without stronger evidence. |
| Population frequency | Established pathogenic variants were absent from large reference datasets, supporting rarity. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 26-27, kumar2018severeneurocognitiveand pages 10-11) | 2015 variants absent in >60,000 individuals from 1000 Genomes/ExAC; 2018 variants absent in gnomAD/ExAC per report. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 26-27, kumar2018severeneurocognitiveand pages 10-11) | Human variant interpretation, 2015 and 2018. | Database versions were historical; current allele frequencies were not independently re-queried here. |
| Molecular mechanism | THOC2 dysfunction compromises TREX-associated RNA biology and, in the 2024 model, causes **R-loop accumulation → DNA damage → cell-cycle disruption / apoptosis → adverse neurodevelopment**. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2, bhattacharjee2024compromisedtranscriptionmrnaexport pages 13-14) | 2024 mouse/patient study showed RNase H-sensitive R-loop accumulation in Thoc2Δ/Y neural stem cells and patient fibroblasts; RNase H1 overexpression reduced R-loops and DNA damage (****p<0.0001). (bhattacharjee2024compromisedtranscriptionmrnaexport pages 6-9, bhattacharjee2024compromisedtranscriptionmrnaexport pages 14-16) | Mouse + patient-derived cell mechanistic study, 2024. | Mechanism is strongly supported in the hypomorphic mouse model and patient fibroblasts, but not yet proven for every human variant. |
| 2024 model-organism / cell findings | A hypomorphic **Thoc2Δ/Y** mouse recapitulated major syndrome features and linked them to impaired neurodevelopment. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2, bhattacharjee2024compromisedtranscriptionmrnaexport pages 10-11, bhattacharjee2024compromisedtranscriptionmrnaexport pages 4-5) | Smaller size/weight; reduced birth rate by ~33%; deficits in spatial learning, working memory, fine motor/sensorimotor tasks; reduced cortical ventricular zone, cortical plate, and corpus callosum thickness; 32% shorter primary axons; fewer mature dendritic spines; reduced electrophysiologic activity. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 10-11, bhattacharjee2024compromisedtranscriptionmrnaexport pages 11-13, bhattacharjee2024compromisedtranscriptionmrnaexport pages 4-5) | Mouse model + primary neurons/NSCs, 2024. | A hypomorphic exon 37-38 deletion model may not reflect all missense/splice variants or full human natural history. |
| Diagnostics | Diagnosis has been made by family-based sequencing approaches and modern exome/genome sequencing, followed by segregation and functional RNA/protein studies when needed. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 5-6, kumar2018severeneurocognitiveand pages 3-5, kumar2018severeneurocognitiveand pages 27-27) | 2015: X-chromosome exome sequencing plus linkage (combined LOD 8.1) in 4 families. (kumar2015thoc2mutationsimplicate pages 1-3) 2018: WES/WGS/trio exome with Sanger confirmation; cDNA PCR, RT-qPCR, western blotting, immunofluorescence, cycloheximide chase used for splice/protein effect resolution. (kumar2018severeneurocognitiveand pages 6-8, kumar2018severeneurocognitiveand pages 5-6, kumar2018severeneurocognitiveand pages 3-5, kumar2018severeneurocognitiveand pages 27-27) | Human diagnostic genomics, 2015 and 2018. | No disease-specific consensus testing guideline or biomarker was retrieved. |
| Treatment / management | No disease-modifying therapy, targeted therapy, or disease-specific clinical trial was identified in the retrieved evidence; management appears supportive and symptom-based. (kumar2018severeneurocognitiveand pages 5-6, kumar2015thoc2mutationsimplicate pages 1-3) | Isolated report: one male had growth-hormone deficiency treated with replacement therapy. Supportive needs are implied by nonverbal/nonambulatory status, seizures, behavioral issues, and developmental disability. (kumar2015thoc2mutationsimplicate pages 3-4, kumar2018severeneurocognitiveand pages 5-6) Clinical trials search retrieved no relevant THOC2-specific interventional trial. | Human case management observations, 2015/2018; trial search negative. | Supportive care details were not systematically reported; no treatment outcome series or guidelines were retrieved. |
| Epidemiology | THOC2-related intellectual disability is **ultra-rare**; no prevalence or incidence estimate was identified in retrieved sources. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 1-3) | Evidence base consists of small family series and case reports: 20 affected individuals in 2015 families, plus 7 established additional cases in 2018; papers mention broader totals including previously reported individuals, but no population denominator. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 3-5, kumar2018severeneurocognitiveand pages 1-3) | Human rare-disease literature, 2015 and 2018. | No registry-based epidemiology, sex ratio estimate, or geographic prevalence study was retrieved. |


*Table: This table compacts the strongest retrieved evidence on THOC2-related intellectual disability, including inheritance, core phenotypes, variant classes, 2024 mechanism data, diagnostics, and major gaps. It is designed for rapid knowledge-base curation while clearly separating established findings from limited or absent evidence.*

## Evidence base and source provenance

The principal human evidence comprises a 2015 *American Journal of Human Genetics* study of four multigenerational families with 20 affected individuals and a 2018 *Human Mutation* expansion containing additional de novo and inherited cases. The principal recent advance is the February 2024 *Nature Communications* study using a hypomorphic mouse, neural stem cells, primary neurons and fibroblasts from an affected person. Thus, most clinical information is aggregated disease-level information abstracted from research cohorts, pedigrees and case reports—not EHR-derived population data. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 1-3, bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2)

Key publications are:

* Kumar et al., “THOC2 Mutations Implicate mRNA-Export Pathway in X-Linked Intellectual Disability,” published August 2015, DOI: https://doi.org/10.1016/j.ajhg.2015.05.021; PMID: **26166475**. (kumar2015thoc2mutationsimplicate pages 1-3)
* Kumar et al., “Severe neurocognitive and growth disorders due to variation in THOC2, an essential component of nuclear mRNA export machinery,” published June 2018, DOI: https://doi.org/10.1002/humu.23557; PMID should be verified against PubMed before database ingestion. (kumar2018severeneurocognitiveand pages 5-6)
* Bhattacharjee et al., “Compromised transcription-mRNA export factor THOC2 causes R-loop accumulation, DNA damage and adverse neurodevelopment,” published February 2024, DOI: https://doi.org/10.1038/s41467-024-45121-5; PubMed record: https://pubmed.ncbi.nlm.nih.gov/?term=10.1038%2Fs41467-024-45121-5. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2)

Representative exact abstract statements include: **“We implicated the X-chromosome THOC2 gene, which encodes the largest subunit of the highly-conserved TREX (Transcription-Export) complex, in a clinically complex neurodevelopmental disorder with intellectual disability as the core phenotype”** and **“Overall, we suggest that perturbed R-loop homeostasis… and DNA damage-associated functional alterations are at the root of THOC2 syndrome.”** (bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2)

## 1. Disease information

### Definition and nomenclature

The condition is a Mendelian neurodevelopmental syndrome in which damaging THOC2 variants compromise an essential RNA-processing/export factor. Preferred practical label: **THOC2-related neurodevelopmental disorder** or **THOC2-related intellectual disability**. Literature alternatives include **THOC2-associated intellectual disability**, **THOC2 syndrome**, **X-linked intellectual disability due to THOC2**, and historically **X-linked intellectual disability 12/MRX12** for one linked family. Because phenotypes extend beyond cognition, “THOC2-related neurodevelopmental disorder” is the broadest label. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 3-5, bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2)

### Identifiers

* **Gene:** THOC2; the retrieved literature establishes X-chromosomal localization but did not independently validate HGNC/NCBI identifiers.
* **OMIM:** MRX12 is the historical family designation. The exact current OMIM disease and gene numbers should be verified directly in OMIM before knowledge-base release; they were not returned by the available evidence tools.
* **MONDO:** no disease-specific MONDO identifier was recoverable in the searches; Open Targets also returned no matching disease entity. Do not assign an unverified MONDO ID.
* **Orphanet:** no disease-specific ORPHA identifier was established.
* **ICD-10/ICD-11 and MeSH:** there is no retrieved evidence of a THOC2-specific code. Use broader intellectual-developmental-disorder and genetic-syndrome coding as locally appropriate, without implying molecular specificity.

## 2. Etiology, risk, protection and gene–environment interaction

The primary cause is a **germline pathogenic or likely pathogenic THOC2 variant**, usually hemizygous in a male. Both maternally inherited X-linked variants and de novo variants occur; an affected female with a de novo missense variant demonstrates that disease is not male-exclusive. (kumar2018severeneurocognitiveand pages 1-3, kumar2018severeneurocognitiveand pages 6-8)

Established genetic risk factors are damaging missense substitutions and splice-altering variants that destabilize THOC2, reduce protein abundance or produce C-terminal truncation. Skewed X-chromosome inactivation appears to protect many heterozygous females: clinically unaffected mothers had reported skewing of approximately 94%, 98:2% or 99.9:0.1%. This is a plausible protective modifier rather than a quantified guarantee of nonpenetrance. (kumar2018severeneurocognitiveand pages 6-8, kumar2018severeneurocognitiveand pages 26-27, kumar2018severeneurocognitiveand pages 8-10)

No environmental, infectious, dietary, occupational or lifestyle cause has been demonstrated. No protective diet, exposure, medication or genetic modifier other than the observed association with favorable X-inactivation has been validated. There are no established gene–environment interactions. Family history raises prior probability in inherited families but is not required because de novo disease occurs. (kumar2018severeneurocognitiveand pages 1-3, kumar2018severeneurocognitiveand pages 6-8)

## 3. Phenotypes

### Core clinical spectrum

In the 2015 families, all affected males had intellectual disability ranging from borderline to severe. Frequently reported associated findings were speech delay, short stature, elevated BMI or adult-onset truncal obesity, seizures, tremor and gait disturbance. Truncal obesity was especially noted among older males in two of four families, suggesting an age-related feature rather than a universal congenital manifestation. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 3-5)

Among seven established individuals characterized in the 2018 series, all had at least moderate intellectual disability; **3/7 were non-verbal, 2/7 non-ambulatory, 4/7 had infantile hypotonia, 2/7 tremor, 4/7 behavioral problems, 1/7 autism spectrum disorder, 1/7 confirmed seizures and 1/7 suspected seizures**. Low birth weight occurred in 3/7, microcephaly in 2/7 and short stature in 2/7. These are referral-cohort frequencies, not population estimates. (kumar2018severeneurocognitiveand pages 5-6)

Suggested HPO annotations include:

* Intellectual disability—**HP:0001249**; global developmental delay—**HP:0001263**.
* Speech delay—**HP:0000750**; absent speech—**HP:0001344**.
* Infantile hypotonia—**HP:0008947** or generalized hypotonia—**HP:0001290**.
* Abnormal gait—**HP:0001288**; ataxic gait—**HP:0002066**; tremor—**HP:0001337**; nystagmus—**HP:0000639**.
* Seizure—**HP:0001250**; epileptic encephalopathy—**HP:0200134**.
* Autism—**HP:0000717**; behavioral abnormality—**HP:0000708**; hyperactivity—**HP:0000752**.
* Microcephaly—**HP:0000252**; short stature—**HP:0004322**; low birth weight—**HP:0001518**; truncal obesity—**HP:0001956**.
* Non-ambulation may be represented by inability to walk—**HP:0002540**.

### Imaging and other manifestations

In 2018, MRI was normal in 3/5 examined individuals. Abnormal findings in 2/5 included cortical gyral abnormalities, corpus-callosum hypoplasia, reduced brainstem volume, ventricular dilation, delayed myelination and periventricular white-matter lesions. Earlier reports described mild ventriculomegaly, gliosis, inferior cerebellar-vermis dysplasia and cervical-cord compression in selected individuals. There is therefore no established pathognomonic imaging signature. (kumar2018severeneurocognitiveand pages 5-6, kumar2015thoc2mutationsimplicate pages 1-3)

Suggested HPO terms include hypoplasia of the corpus callosum (**HP:0002079**), ventriculomegaly (**HP:0002119**), delayed CNS myelination (**HP:0002188**) and abnormal cerebral white matter morphology (**HP:0002500**). Cerebellar-type signs may occur despite a structurally unremarkable cerebellum. (kumar2018severeneurocognitiveand pages 8-10)

### Onset, course and quality of life

Onset is developmental and generally evident in infancy or childhood through hypotonia, delayed milestones, speech delay or cognitive impairment. Available cohorts do not define formal stages, annual progression or remission. Intellectual and adaptive impairments appear chronic and lifelong; adult truncal obesity may emerge later. Non-verbal and non-ambulatory status in some children indicates substantial effects on communication, mobility, education, caregiving needs and independence. No THOC2-specific EQ-5D, SF-36, PROMIS or caregiver-burden study was found. (kumar2018severeneurocognitiveand pages 5-6, kumar2018severeneurocognitiveand pages 3-5)

## 4. Genetic and molecular information

### Causal gene and variant spectrum

THOC2 is the established causal gene. The 2015 study identified four segregating missense variants: **c.937C>T (p.Leu313Phe), c.1313T>C (p.Leu438Pro), c.2399T>C (p.Ile800Thr), and c.3034T>C (p.Ser1012Pro)**. They affected conserved residues, were absent from more than 60,000 reference individuals in the then-current 1000 Genomes/ExAC datasets and produced a combined pedigree LOD score of 8.1. Two destabilized THOC2 and TREX partners. (kumar2015thoc2mutationsimplicate pages 1-3)

The 2018 expansion added established missense changes including **p.Tyr517Cys, p.Thr696Ile, p.Gly713Asp and p.His1187Tyr**, plus splice variants including **c.4450-2A>G** and **c.3503+4A>C**, which generated abnormal C-terminal products. p.Tyr517Cys shortened measured protein turnover from approximately eight hours for wild type to three hours. These variants were assessed as pathogenic or likely pathogenic using segregation, rarity, ACMG criteria and functional evidence. (kumar2018severeneurocognitiveand pages 6-8, kumar2018severeneurocognitiveand pages 5-6, kumar2018severeneurocognitiveand pages 8-10)

Reported **VUS**, which must not be represented as confirmed causes, include **p.Arg77Cys, p.Ser1108Leu, p.Arg1121Gly and p.Asn1261His**. Their rarity, conservation and computational predictions were insufficient without stronger segregation or functional evidence. (kumar2018severeneurocognitiveand pages 10-11)

All reported disease variants are germline. No somatic THOC2 mechanism is implicated in this syndrome. The dominant molecular theme is partial loss of function or hypomorphism; complete loss is expected to be poorly tolerated because THOC2 is essential. Some truncated products may exert additional dominant-negative effects, but this is variant-specific and not a universal disease mechanism. (kumar2018severeneurocognitiveand pages 10-11, kumar2018severeneurocognitiveand pages 8-10)

No validated modifier gene, disease-specific methylation episignature, repeat expansion, aneuploidy or recurrent large chromosomal rearrangement was found. Historical reference-database absences should be rechecked in current gnomAD before clinical classification.

## 5. Environmental information

No toxin, radiation, pollution, occupation, smoking, alcohol, diet or exercise exposure is known to cause or materially modify THOC2-related intellectual disability. No bacterial, viral, fungal or parasitic trigger is implicated. Ordinary environmental and educational context may affect functional attainment, as in other developmental disabilities, but this is not a demonstrated molecular gene–environment interaction.

## 6. Mechanism and pathophysiology

### Upstream molecular defect

THOC2 is the largest subunit of the conserved nuclear TREX complex, which links transcription, mRNA processing and export while helping preserve genome stability. Earlier cellular studies supported variant-dependent THOC2/TREX destabilization and disturbed RNA export. The 2024 work showed that a hypomorphic exon 37–38 deletion can leave bulk mRNA export relatively intact while profoundly disturbing R-loop and genome homeostasis. (kumar2015thoc2mutationsimplicate pages 1-3, bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2, bhattacharjee2024compromisedtranscriptionmrnaexport pages 14-16)

### Current causal model

The best-supported chain is:

**Pathogenic THOC2 variant → compromised THOC2/TREX function → unresolved RNA:DNA hybrid R-loops → replication/transcription-associated DNA damage → G2/M checkpoint disturbance and neural-stem-cell apoptosis → reduced or premature neural progenitor differentiation and altered cortical development → impaired neuronal migration, axon growth, dendritic-spine/synapse maturation and network activity → intellectual, speech and motor phenotypes.** (bhattacharjee2024compromisedtranscriptionmrnaexport pages 6-9, bhattacharjee2024compromisedtranscriptionmrnaexport pages 10-11, bhattacharjee2024compromisedtranscriptionmrnaexport pages 13-14)

R-loop staining was RNase-H sensitive in mutant neural stem cells and patient fibroblasts. RNase H1 overexpression significantly reduced both R-loop burden and DNA damage (reported p<0.0001), providing experimental evidence that R-loops are upstream contributors rather than merely downstream markers. Mutant cells also showed elevated γ-H2AX, comet-assay damage, G2/M abnormalities and apoptosis. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 14-16, bhattacharjee2024compromisedtranscriptionmrnaexport pages 13-14)

### Cellular, anatomical and multi-omic consequences

The 2024 model showed reduced PAX6-positive cortical ventricular-zone thickness, premature neural-stem-cell differentiation, reduced cortical plate and corpus-callosum thickness, impaired migration, **32% shorter primary axons**, fewer mature dendritic spines, reduced SYN1–PSD95 synaptic puncta and abnormal electrophysiological network activity. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 6-9, bhattacharjee2024compromisedtranscriptionmrnaexport pages 10-11)

Embryonic day 18.5 showed the largest transcriptomic disruption, involving transcription, cell cycle, cell death and cognition-related genes. Dysregulated neurodevelopmental genes included **SYNGAP1, HUWE1, SHANK3, DLG4, KDM5C** and **CTNND1**. Proteomics identified 421 dysregulated proteins enriched for translation, peptide biosynthesis and mRNA-catabolic processes. No validated metabolomic, lipidomic, single-cell or spatial-transcriptomic signature has been reported. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 6-9, bhattacharjee2024compromisedtranscriptionmrnaexport pages 13-14)

Suggested ontology terms:

* GO biological process: mRNA export from nucleus (**GO:0006406**), RNA processing (**GO:0006396**), regulation of transcription by RNA polymerase II, DNA-damage response (**GO:0006974**), cell-cycle checkpoint signaling, apoptotic process (**GO:0006915**), neurogenesis (**GO:0022008**), neuron migration (**GO:0001764**), axon development (**GO:0061564**) and synapse organization (**GO:0050808**).
* GO cellular component: nucleus (**GO:0005634**), nuclear speck, TREX complex, neuronal projection, dendritic spine and synapse.
* Cell Ontology: neural stem cell (**CL:0000047**), radial glial cell (**CL:0000681**), neuron (**CL:0000540**), cortical neuron and hippocampal neuron where a more specific supported term is available.

Immune dysregulation, inflammation, metabolic disease and primary mitochondrial dysfunction are not established components.

## 7. Anatomical structures affected

The central nervous system is primary, particularly the developing cerebral cortex and hippocampal/cortical neuronal systems examined experimentally. The cortical ventricular zone, cortical plate, corpus callosum, axons, dendritic spines and synapses are implicated. Variable human MRI findings also involve cerebral white matter, brainstem, ventricles and occasionally cerebellar vermis. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 6-9, bhattacharjee2024compromisedtranscriptionmrnaexport pages 10-11, kumar2018severeneurocognitiveand pages 5-6)

Suggested UBERON annotations include brain (**UBERON:0000955**), cerebral cortex (**UBERON:0000956**), hippocampus (**UBERON:0002421**), corpus callosum (**UBERON:0002336**), brainstem (**UBERON:0002298**), cerebellum (**UBERON:0002037**) and spinal cord (**UBERON:0002240**) where directly supported. No consistent lateralization has been reported.

At the subcellular level, the nucleus is central because THOC2/TREX controls transcription-coupled RNA processing/export and R-loop homeostasis; downstream effects involve axonal, dendritic and synaptic compartments. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 14-16, bhattacharjee2024compromisedtranscriptionmrnaexport pages 10-11)

## 8. Temporal development

The disorder is congenital in genetic origin and pediatric in clinical recognition. Infantile hypotonia, low birth weight or microcephaly may be early findings; developmental, speech and cognitive abnormalities emerge as milestones are missed. Growth impairment can occur during childhood, while truncal obesity was particularly observed in older males. (kumar2018severeneurocognitiveand pages 5-6, kumar2018severeneurocognitiveand pages 3-5)

The 2024 model indicates a critical prenatal neurodevelopmental period: THOC2 was abundant at E14.5/E18.5, with marked transcriptomic disruption at E18.5, reduced progenitor-zone thickness and subsequent cortical/synaptic deficits. This supports early developmental vulnerability but does not establish a human therapeutic window. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 6-9, bhattacharjee2024compromisedtranscriptionmrnaexport pages 11-13)

No relapsing-remitting pattern, spontaneous remission or defined end stage is known. Longitudinal natural-history cohorts are absent.

## 9. Inheritance and population

Inheritance is X-linked. Hemizygous males are predominantly affected, whereas heterozygous mothers are commonly unaffected, plausibly because of highly skewed X-inactivation. De novo disease can affect either sex, and a severely affected female with de novo p.Tyr517Cys was reported. Expressivity in males ranges from borderline ID to severe non-verbal/non-ambulatory disease. Formal penetrance, germline-mosaicism frequency, anticipation, founder effects, carrier frequency and consanguinity effects are unknown. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 8-10, kumar2018severeneurocognitiveand pages 6-8)

No incidence or prevalence estimate exists. The literature consists of a 2015 cohort of 20 affected people in four families and a small number of additional established cases in 2018. Cases arose from multiple countries, arguing against a known geographically restricted population, but the sample is too small for demographic conclusions. The observed male predominance reflects X-linked biology and ascertainment rather than a measured population sex ratio. (kumar2015thoc2mutationsimplicate pages 1-3, kumar2018severeneurocognitiveand pages 27-27)

## 10. Diagnostics

### Clinical recognition and differential diagnosis

Suspect the disorder in a male with unexplained developmental delay/intellectual disability and speech impairment, especially when accompanied by hypotonia, abnormal gait, tremor/ataxia, seizures, short stature, microcephaly, truncal obesity or an X-linked pedigree. The phenotype is not sufficiently distinctive for clinical diagnosis alone. (kumar2015thoc2mutationsimplicate pages 3-4, kumar2015thoc2mutationsimplicate pages 1-3)

Important differential categories include other X-linked intellectual-developmental disorders; epileptic encephalopathies; cerebral-palsy-like genetic motor disorders; chromosomal copy-number disorders; metabolic causes of developmental delay; and other RNA-processing/TREX disorders, including THOC6-associated Beaulieu–Boycott–Innes syndrome. Distinction requires molecular testing.

### Recommended testing strategy

1. **Trio WES or WGS** is the preferred broad approach for an undiagnosed neurodevelopmental disorder. Both were successful in published THOC2 cases. (kumar2018severeneurocognitiveand pages 5-6)
2. A comprehensive intellectual-disability/epilepsy panel that includes **THOC2** is reasonable when sequencing depth and copy-number calling are adequate.
3. Confirm candidate variants and segregation by Sanger sequencing; establish de novo status with parental testing where possible. (kumar2018severeneurocognitiveand pages 6-8, kumar2018severeneurocognitiveand pages 5-6)
4. For intronic or splice-region variants, perform patient RNA/cDNA analysis, RT-PCR or RNA sequencing. Published studies used cDNA PCR, RT-qPCR, western blotting and protein-stability assays to establish consequences. (kumar2018severeneurocognitiveand pages 6-8, kumar2018severeneurocognitiveand pages 3-5)
5. Interpret missense variants conservatively under ACMG/AMP criteria. Rarity and computational prediction alone do not convert a VUS into a diagnosis. (kumar2018severeneurocognitiveand pages 10-11)
6. CMA remains useful for unexplained developmental disability or suspected CNV, but it will usually miss small THOC2 sequence variants. Karyotype/FISH, mitochondrial testing and repeat-expansion assays are not THOC2-specific first-line tests unless the broader phenotype indicates them.

There is no validated biochemical, circulating, proteomic or imaging biomarker. MRI, EEG, vision assessment and growth/endocrine testing are phenotype-directed rather than diagnostic. No newborn-screening assay or standardized disease-specific clinical criteria exist.

## 11. Outcome and prognosis

Published cases demonstrate survival through childhood and into adulthood, but no five- or ten-year survival estimates, life-expectancy analyses or disease-specific mortality rates are available. Complete THOC2 loss is predicted to be poorly tolerated, whereas observed hypomorphic variants are compatible with survival. (kumar2018severeneurocognitiveand pages 10-11)

Morbidity is principally lifelong neurodevelopmental disability. Prognosis is variable: some individuals have borderline or mild ID, while others are non-verbal, non-ambulatory or have epileptic encephalopathy and cortical visual impairment. Motor dysfunction, seizures, behavioral abnormalities and growth problems increase care burden. No validated molecular prognostic biomarker or genotype-based outcome calculator exists. (kumar2018severeneurocognitiveand pages 5-6, kumar2015thoc2mutationsimplicate pages 1-3)

## 12. Treatment and current applications

There is **no approved THOC2-specific disease-modifying therapy**, gene therapy, RNA therapy, cell therapy or targeted pharmacotherapy, and the clinical-trial search found no relevant disease-specific interventional trial. No response-rate or adverse-event series exists.

Current real-world management is multidisciplinary and phenotype-directed:

* early developmental intervention, special education and neuropsychological assessment;
* speech-language therapy, including augmentative and alternative communication for non-verbal individuals;
* physical and occupational therapy for hypotonia, gait, coordination and adaptive skills;
* standard antiseizure therapy guided by seizure type and EEG;
* behavioral, autism and psychiatric assessment and treatment;
* nutrition, weight and growth surveillance;
* ophthalmology for visual impairment and audiology as clinically indicated;
* brain/spine MRI, neurology or orthopedic evaluation when focal signs, gait deterioration or suspected structural disease are present;
* endocrine evaluation for poor growth. One reported boy with growth-hormone deficiency received replacement, but this is treatment of a documented comorbidity, not THOC2-directed therapy. (kumar2018severeneurocognitiveand pages 5-6, kumar2015thoc2mutationsimplicate pages 3-4)

Potential NCIt intervention concepts include Genetic Counseling, Physical Therapy, Occupational Therapy, Speech Therapy, Special Education, Anticonvulsant Therapy and Growth Hormone Replacement Therapy. Exact NCIt codes should be resolved against the current NCIt release.

Experimentally, RNase H1 rescue of R-loops provides target-validation evidence but is not a human therapy. Translation would require safe, cell- and developmentally appropriate correction of R-loop homeostasis without disrupting essential RNA biology. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 14-16)

## 13. Prevention

There is no lifestyle, vaccine, environmental or drug-based primary prevention. Primary genetic prevention options require identification of a familial pathogenic variant and nondirective counseling. These may include carrier testing, cascade testing, prenatal diagnosis and preimplantation genetic testing for monogenic disease. Because de novo variants occur, a negative family history does not eliminate risk. Residual recurrence risk from parental germline mosaicism should be discussed even when parental blood testing is negative, although its THOC2-specific frequency is unknown. (kumar2018severeneurocognitiveand pages 1-3, kumar2018severeneurocognitiveand pages 6-8)

Secondary prevention consists of prompt genomic diagnosis and early developmental, communication, seizure, vision, mobility and growth interventions. Tertiary prevention includes seizure control, contracture/fall prevention, weight management and support for communication and adaptive functioning. Population newborn or carrier screening is not currently established.

## 14. Other species and natural disease

No naturally occurring veterinary THOC2 syndrome, breed predisposition, zoonotic potential or cross-species transmission is established. The disorder is genetic and non-infectious. THOC2 orthologs are evolutionarily conserved, consistent with the essential role of TREX-mediated RNA biology. Ortholog-specific NCBI Gene and NCBI Taxonomy identifiers should be retrieved directly before database ingestion.

Relevant experimental species include **Mus musculus** (NCBI Taxonomy 10090), **Danio rerio** (7955) and **Drosophila melanogaster** (7227). Zebrafish Thoc2 is essential for embryonic development, and depletion in Drosophila S2 cells impairs mRNA export; these findings support conserved essentiality but do not constitute naturally occurring animal disease. (kumar2015thoc2mutationsimplicate pages 1-3, bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2)

## 15. Model organisms

### Mouse

The strongest model is the hemizygous **Thoc2Δ/Y** hypomorphic mouse carrying an exon 37–38 deletion modeled on a human variant. It recapitulated smaller size/weight and deficits in spatial learning, working memory, fine motor control and sensorimotor function. Birth rate was reduced by approximately 33%. Morris water maze, Barnes maze, Y-maze, beam-walking and pasta-handling tests demonstrated cognitive and motor phenotypes; hyperactivity and reduced anxiety-like behavior were also reported. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 11-13, bhattacharjee2024compromisedtranscriptionmrnaexport pages 4-5)

The model reproduced developmental pathology—R-loop accumulation, DNA damage, neural-stem-cell apoptosis, reduced cortical structures and impaired neuronal maturation—and is suitable for studying R-loop rescue, developmental timing and synaptic consequences. Its chief limitation is that one hypomorphic deletion cannot represent every missense or splice variant, female X-inactivation, or the full human phenotypic range. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 6-9, bhattacharjee2024compromisedtranscriptionmrnaexport pages 10-11, bhattacharjee2024compromisedtranscriptionmrnaexport pages 13-14)

### Cellular models

Patient dermal fibroblasts reproduced R-loop accumulation and comet-assay DNA damage. Mouse neural stem cells, neurospheres and primary cortical/hippocampal neurons modeled progenitor survival, differentiation, migration, axonal development, synapses and electrophysiology. HEK293T and patient-derived cells were used for protein localization, abundance and cycloheximide-chase assays. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 14-16, bhattacharjee2024compromisedtranscriptionmrnaexport pages 10-11, kumar2018severeneurocognitiveand pages 5-6)

### Zebrafish and Drosophila

Zebrafish studies support embryonic essentiality, while Drosophila S2-cell depletion supports conserved THO/TREX-dependent mRNA export. These are useful for rapid functional testing but do not reproduce the complete human syndrome. (kumar2015thoc2mutationsimplicate pages 1-3, bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2)

No disease-specific rat, organoid, human iPSC-neuron, CRISPR-screen, single-cell or spatial-transcriptomic model was identified in the retrieved literature.

## Knowledge gaps and expert assessment

The 2024 work materially changes current understanding: THOC2 disease should not be represented solely as a generic “mRNA-export defect.” At least for the modeled hypomorphic deletion, defective R-loop resolution and genome stability are central and experimentally rescuable upstream events, while overt bulk nuclear mRNA retention was not observed. The authors themselves identify nuclear/cytoplasmic RNA sequencing as a needed next step to determine whether selected transcripts nevertheless have export defects. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 14-16, bhattacharjee2024compromisedtranscriptionmrnaexport pages 4-5)

For knowledge-base curation, clinical frequencies should be labeled **small-cohort observations**, not population frequencies. VUS must remain separate from established variants. Likewise, mouse rescue data should be annotated as preclinical target-validation evidence rather than treatment evidence. Highest-priority research needs are an international natural-history registry, systematic female-carrier phenotyping and X-inactivation studies, current ClinVar/gnomAD aggregation, variant-specific functional assays, patient iPSC-derived neural models, transcript-compartment profiling, and development of safe R-loop/genome-stability biomarkers and interventions.

References

1. (kumar2015thoc2mutationsimplicate pages 1-3): Raman Kumar, Mark A. Corbett, Bregje W.M. van Bon, Joshua A. Woenig, Lloyd Weir, Evelyn Douglas, Kathryn L. Friend, Alison Gardner, Marie Shaw, Lachlan A. Jolly, Chuan Tan, Matthew F. Hunter, Anna Hackett, Michael Field, Elizabeth E. Palmer, Melanie Leffler, Carolyn Rogers, Jackie Boyle, Melanie Bienek, Corinna Jensen, Griet Van Buggenhout, Hilde Van Esch, Katrin Hoffmann, Martine Raynaud, Huiying Zhao, Robin Reed, Hao Hu, Stefan A. Haas, Eric Haan, Vera M. Kalscheuer, and Jozef Gecz. Thoc2 mutations implicate mrna-export pathway in x-linked intellectual disability. American journal of human genetics, 97 2:302-10, Aug 2015. URL: https://doi.org/10.1016/j.ajhg.2015.05.021, doi:10.1016/j.ajhg.2015.05.021. This article has 93 citations and is from a highest quality peer-reviewed journal.

2. (kumar2018severeneurocognitiveand pages 1-3): Raman Kumar, Alison Gardner, Claire C. Homan, Evelyn Douglas, Heather Mefford, Dagmar Wieczorek, Hermann-Josef Lüdecke, Zornitza Stark, Simon Sadedin, Catherine Bearce Nowak, Jessica Douglas, Gretchen Parsons, Paul Mark, Lourdes Loidi, Gail E. Herman, Theresa Mihalic Mosher, Meredith K. Gillespie, Lauren Brady, Mark Tarnopolsky, Irene Madrigal, Jesús Eiris, Laura Domènech Salgado, Raquel Rabionet, Tim M. Strom, Naoko Ishihara, Hidehito Inagaki, Hiroki Kurahashi, Tracy Dudding-Byth, Elizabeth E. Palmer, Michael Field, and Jozef Gecz. Severe neurocognitive and growth disorders due to variation in thoc2, an essential component of nuclear mrna export machinery. Human Mutation, 39:1126-1138, Jun 2018. URL: https://doi.org/10.1002/humu.23557, doi:10.1002/humu.23557. This article has 31 citations and is from a domain leading peer-reviewed journal.

3. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 1-2): Rudrarup Bhattacharjee, Lachlan A. Jolly, Mark A. Corbett, Ing Chee Wee, Sushma R. Rao, Alison E. Gardner, Tarin Ritchie, Eline J. H. van Hugte, Ummi Ciptasari, Sandra Piltz, Jacqueline E. Noll, Nazzmer Nazri, Clare L. van Eyk, Melissa White, Dani Fornarino, Cathryn Poulton, Gareth Baynam, Lyndsey E. Collins-Praino, Marten F. Snel, Nael Nadif Kasri, Kim M. Hemsley, Paul Q. Thomas, Raman Kumar, and Jozef Gecz. Compromised transcription-mrna export factor thoc2 causes r-loop accumulation, dna damage and adverse neurodevelopment. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45121-5, doi:10.1038/s41467-024-45121-5. This article has 16 citations and is from a highest quality peer-reviewed journal.

4. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 13-14): Rudrarup Bhattacharjee, Lachlan A. Jolly, Mark A. Corbett, Ing Chee Wee, Sushma R. Rao, Alison E. Gardner, Tarin Ritchie, Eline J. H. van Hugte, Ummi Ciptasari, Sandra Piltz, Jacqueline E. Noll, Nazzmer Nazri, Clare L. van Eyk, Melissa White, Dani Fornarino, Cathryn Poulton, Gareth Baynam, Lyndsey E. Collins-Praino, Marten F. Snel, Nael Nadif Kasri, Kim M. Hemsley, Paul Q. Thomas, Raman Kumar, and Jozef Gecz. Compromised transcription-mrna export factor thoc2 causes r-loop accumulation, dna damage and adverse neurodevelopment. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45121-5, doi:10.1038/s41467-024-45121-5. This article has 16 citations and is from a highest quality peer-reviewed journal.

5. (kumar2018severeneurocognitiveand pages 3-5): Raman Kumar, Alison Gardner, Claire C. Homan, Evelyn Douglas, Heather Mefford, Dagmar Wieczorek, Hermann-Josef Lüdecke, Zornitza Stark, Simon Sadedin, Catherine Bearce Nowak, Jessica Douglas, Gretchen Parsons, Paul Mark, Lourdes Loidi, Gail E. Herman, Theresa Mihalic Mosher, Meredith K. Gillespie, Lauren Brady, Mark Tarnopolsky, Irene Madrigal, Jesús Eiris, Laura Domènech Salgado, Raquel Rabionet, Tim M. Strom, Naoko Ishihara, Hidehito Inagaki, Hiroki Kurahashi, Tracy Dudding-Byth, Elizabeth E. Palmer, Michael Field, and Jozef Gecz. Severe neurocognitive and growth disorders due to variation in thoc2, an essential component of nuclear mrna export machinery. Human Mutation, 39:1126-1138, Jun 2018. URL: https://doi.org/10.1002/humu.23557, doi:10.1002/humu.23557. This article has 31 citations and is from a domain leading peer-reviewed journal.

6. (kumar2018severeneurocognitiveand pages 6-8): Raman Kumar, Alison Gardner, Claire C. Homan, Evelyn Douglas, Heather Mefford, Dagmar Wieczorek, Hermann-Josef Lüdecke, Zornitza Stark, Simon Sadedin, Catherine Bearce Nowak, Jessica Douglas, Gretchen Parsons, Paul Mark, Lourdes Loidi, Gail E. Herman, Theresa Mihalic Mosher, Meredith K. Gillespie, Lauren Brady, Mark Tarnopolsky, Irene Madrigal, Jesús Eiris, Laura Domènech Salgado, Raquel Rabionet, Tim M. Strom, Naoko Ishihara, Hidehito Inagaki, Hiroki Kurahashi, Tracy Dudding-Byth, Elizabeth E. Palmer, Michael Field, and Jozef Gecz. Severe neurocognitive and growth disorders due to variation in thoc2, an essential component of nuclear mrna export machinery. Human Mutation, 39:1126-1138, Jun 2018. URL: https://doi.org/10.1002/humu.23557, doi:10.1002/humu.23557. This article has 31 citations and is from a domain leading peer-reviewed journal.

7. (kumar2018severeneurocognitiveand pages 8-10): Raman Kumar, Alison Gardner, Claire C. Homan, Evelyn Douglas, Heather Mefford, Dagmar Wieczorek, Hermann-Josef Lüdecke, Zornitza Stark, Simon Sadedin, Catherine Bearce Nowak, Jessica Douglas, Gretchen Parsons, Paul Mark, Lourdes Loidi, Gail E. Herman, Theresa Mihalic Mosher, Meredith K. Gillespie, Lauren Brady, Mark Tarnopolsky, Irene Madrigal, Jesús Eiris, Laura Domènech Salgado, Raquel Rabionet, Tim M. Strom, Naoko Ishihara, Hidehito Inagaki, Hiroki Kurahashi, Tracy Dudding-Byth, Elizabeth E. Palmer, Michael Field, and Jozef Gecz. Severe neurocognitive and growth disorders due to variation in thoc2, an essential component of nuclear mrna export machinery. Human Mutation, 39:1126-1138, Jun 2018. URL: https://doi.org/10.1002/humu.23557, doi:10.1002/humu.23557. This article has 31 citations and is from a domain leading peer-reviewed journal.

8. (kumar2018severeneurocognitiveand pages 26-27): Raman Kumar, Alison Gardner, Claire C. Homan, Evelyn Douglas, Heather Mefford, Dagmar Wieczorek, Hermann-Josef Lüdecke, Zornitza Stark, Simon Sadedin, Catherine Bearce Nowak, Jessica Douglas, Gretchen Parsons, Paul Mark, Lourdes Loidi, Gail E. Herman, Theresa Mihalic Mosher, Meredith K. Gillespie, Lauren Brady, Mark Tarnopolsky, Irene Madrigal, Jesús Eiris, Laura Domènech Salgado, Raquel Rabionet, Tim M. Strom, Naoko Ishihara, Hidehito Inagaki, Hiroki Kurahashi, Tracy Dudding-Byth, Elizabeth E. Palmer, Michael Field, and Jozef Gecz. Severe neurocognitive and growth disorders due to variation in thoc2, an essential component of nuclear mrna export machinery. Human Mutation, 39:1126-1138, Jun 2018. URL: https://doi.org/10.1002/humu.23557, doi:10.1002/humu.23557. This article has 31 citations and is from a domain leading peer-reviewed journal.

9. (kumar2018severeneurocognitiveand pages 5-6): Raman Kumar, Alison Gardner, Claire C. Homan, Evelyn Douglas, Heather Mefford, Dagmar Wieczorek, Hermann-Josef Lüdecke, Zornitza Stark, Simon Sadedin, Catherine Bearce Nowak, Jessica Douglas, Gretchen Parsons, Paul Mark, Lourdes Loidi, Gail E. Herman, Theresa Mihalic Mosher, Meredith K. Gillespie, Lauren Brady, Mark Tarnopolsky, Irene Madrigal, Jesús Eiris, Laura Domènech Salgado, Raquel Rabionet, Tim M. Strom, Naoko Ishihara, Hidehito Inagaki, Hiroki Kurahashi, Tracy Dudding-Byth, Elizabeth E. Palmer, Michael Field, and Jozef Gecz. Severe neurocognitive and growth disorders due to variation in thoc2, an essential component of nuclear mrna export machinery. Human Mutation, 39:1126-1138, Jun 2018. URL: https://doi.org/10.1002/humu.23557, doi:10.1002/humu.23557. This article has 31 citations and is from a domain leading peer-reviewed journal.

10. (kumar2018severeneurocognitiveand pages 10-11): Raman Kumar, Alison Gardner, Claire C. Homan, Evelyn Douglas, Heather Mefford, Dagmar Wieczorek, Hermann-Josef Lüdecke, Zornitza Stark, Simon Sadedin, Catherine Bearce Nowak, Jessica Douglas, Gretchen Parsons, Paul Mark, Lourdes Loidi, Gail E. Herman, Theresa Mihalic Mosher, Meredith K. Gillespie, Lauren Brady, Mark Tarnopolsky, Irene Madrigal, Jesús Eiris, Laura Domènech Salgado, Raquel Rabionet, Tim M. Strom, Naoko Ishihara, Hidehito Inagaki, Hiroki Kurahashi, Tracy Dudding-Byth, Elizabeth E. Palmer, Michael Field, and Jozef Gecz. Severe neurocognitive and growth disorders due to variation in thoc2, an essential component of nuclear mrna export machinery. Human Mutation, 39:1126-1138, Jun 2018. URL: https://doi.org/10.1002/humu.23557, doi:10.1002/humu.23557. This article has 31 citations and is from a domain leading peer-reviewed journal.

11. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 6-9): Rudrarup Bhattacharjee, Lachlan A. Jolly, Mark A. Corbett, Ing Chee Wee, Sushma R. Rao, Alison E. Gardner, Tarin Ritchie, Eline J. H. van Hugte, Ummi Ciptasari, Sandra Piltz, Jacqueline E. Noll, Nazzmer Nazri, Clare L. van Eyk, Melissa White, Dani Fornarino, Cathryn Poulton, Gareth Baynam, Lyndsey E. Collins-Praino, Marten F. Snel, Nael Nadif Kasri, Kim M. Hemsley, Paul Q. Thomas, Raman Kumar, and Jozef Gecz. Compromised transcription-mrna export factor thoc2 causes r-loop accumulation, dna damage and adverse neurodevelopment. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45121-5, doi:10.1038/s41467-024-45121-5. This article has 16 citations and is from a highest quality peer-reviewed journal.

12. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 14-16): Rudrarup Bhattacharjee, Lachlan A. Jolly, Mark A. Corbett, Ing Chee Wee, Sushma R. Rao, Alison E. Gardner, Tarin Ritchie, Eline J. H. van Hugte, Ummi Ciptasari, Sandra Piltz, Jacqueline E. Noll, Nazzmer Nazri, Clare L. van Eyk, Melissa White, Dani Fornarino, Cathryn Poulton, Gareth Baynam, Lyndsey E. Collins-Praino, Marten F. Snel, Nael Nadif Kasri, Kim M. Hemsley, Paul Q. Thomas, Raman Kumar, and Jozef Gecz. Compromised transcription-mrna export factor thoc2 causes r-loop accumulation, dna damage and adverse neurodevelopment. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45121-5, doi:10.1038/s41467-024-45121-5. This article has 16 citations and is from a highest quality peer-reviewed journal.

13. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 10-11): Rudrarup Bhattacharjee, Lachlan A. Jolly, Mark A. Corbett, Ing Chee Wee, Sushma R. Rao, Alison E. Gardner, Tarin Ritchie, Eline J. H. van Hugte, Ummi Ciptasari, Sandra Piltz, Jacqueline E. Noll, Nazzmer Nazri, Clare L. van Eyk, Melissa White, Dani Fornarino, Cathryn Poulton, Gareth Baynam, Lyndsey E. Collins-Praino, Marten F. Snel, Nael Nadif Kasri, Kim M. Hemsley, Paul Q. Thomas, Raman Kumar, and Jozef Gecz. Compromised transcription-mrna export factor thoc2 causes r-loop accumulation, dna damage and adverse neurodevelopment. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45121-5, doi:10.1038/s41467-024-45121-5. This article has 16 citations and is from a highest quality peer-reviewed journal.

14. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 4-5): Rudrarup Bhattacharjee, Lachlan A. Jolly, Mark A. Corbett, Ing Chee Wee, Sushma R. Rao, Alison E. Gardner, Tarin Ritchie, Eline J. H. van Hugte, Ummi Ciptasari, Sandra Piltz, Jacqueline E. Noll, Nazzmer Nazri, Clare L. van Eyk, Melissa White, Dani Fornarino, Cathryn Poulton, Gareth Baynam, Lyndsey E. Collins-Praino, Marten F. Snel, Nael Nadif Kasri, Kim M. Hemsley, Paul Q. Thomas, Raman Kumar, and Jozef Gecz. Compromised transcription-mrna export factor thoc2 causes r-loop accumulation, dna damage and adverse neurodevelopment. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45121-5, doi:10.1038/s41467-024-45121-5. This article has 16 citations and is from a highest quality peer-reviewed journal.

15. (bhattacharjee2024compromisedtranscriptionmrnaexport pages 11-13): Rudrarup Bhattacharjee, Lachlan A. Jolly, Mark A. Corbett, Ing Chee Wee, Sushma R. Rao, Alison E. Gardner, Tarin Ritchie, Eline J. H. van Hugte, Ummi Ciptasari, Sandra Piltz, Jacqueline E. Noll, Nazzmer Nazri, Clare L. van Eyk, Melissa White, Dani Fornarino, Cathryn Poulton, Gareth Baynam, Lyndsey E. Collins-Praino, Marten F. Snel, Nael Nadif Kasri, Kim M. Hemsley, Paul Q. Thomas, Raman Kumar, and Jozef Gecz. Compromised transcription-mrna export factor thoc2 causes r-loop accumulation, dna damage and adverse neurodevelopment. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45121-5, doi:10.1038/s41467-024-45121-5. This article has 16 citations and is from a highest quality peer-reviewed journal.

16. (kumar2018severeneurocognitiveand pages 27-27): Raman Kumar, Alison Gardner, Claire C. Homan, Evelyn Douglas, Heather Mefford, Dagmar Wieczorek, Hermann-Josef Lüdecke, Zornitza Stark, Simon Sadedin, Catherine Bearce Nowak, Jessica Douglas, Gretchen Parsons, Paul Mark, Lourdes Loidi, Gail E. Herman, Theresa Mihalic Mosher, Meredith K. Gillespie, Lauren Brady, Mark Tarnopolsky, Irene Madrigal, Jesús Eiris, Laura Domènech Salgado, Raquel Rabionet, Tim M. Strom, Naoko Ishihara, Hidehito Inagaki, Hiroki Kurahashi, Tracy Dudding-Byth, Elizabeth E. Palmer, Michael Field, and Jozef Gecz. Severe neurocognitive and growth disorders due to variation in thoc2, an essential component of nuclear mrna export machinery. Human Mutation, 39:1126-1138, Jun 2018. URL: https://doi.org/10.1002/humu.23557, doi:10.1002/humu.23557. This article has 31 citations and is from a domain leading peer-reviewed journal.

17. (kumar2015thoc2mutationsimplicate pages 3-4): Raman Kumar, Mark A. Corbett, Bregje W.M. van Bon, Joshua A. Woenig, Lloyd Weir, Evelyn Douglas, Kathryn L. Friend, Alison Gardner, Marie Shaw, Lachlan A. Jolly, Chuan Tan, Matthew F. Hunter, Anna Hackett, Michael Field, Elizabeth E. Palmer, Melanie Leffler, Carolyn Rogers, Jackie Boyle, Melanie Bienek, Corinna Jensen, Griet Van Buggenhout, Hilde Van Esch, Katrin Hoffmann, Martine Raynaud, Huiying Zhao, Robin Reed, Hao Hu, Stefan A. Haas, Eric Haan, Vera M. Kalscheuer, and Jozef Gecz. Thoc2 mutations implicate mrna-export pathway in x-linked intellectual disability. American journal of human genetics, 97 2:302-10, Aug 2015. URL: https://doi.org/10.1016/j.ajhg.2015.05.021, doi:10.1016/j.ajhg.2015.05.021. This article has 93 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](THOC2-Related_Intellectual_Disability-deep-research-falcon_artifacts/artifact-00.md)