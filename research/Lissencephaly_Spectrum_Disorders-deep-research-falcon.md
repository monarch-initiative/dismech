---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-03T21:46:02.153961'
end_time: '2026-06-03T21:55:26.873496'
duration_seconds: 564.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lissencephaly Spectrum Disorders
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
  path: Lissencephaly_Spectrum_Disorders-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lissencephaly Spectrum Disorders
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lissencephaly Spectrum Disorders** covering all of the
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
- **Disease Name:** Lissencephaly Spectrum Disorders
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lissencephaly Spectrum Disorders** covering all of the
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


## Comprehensive Research Report: Lissencephaly Spectrum Disorders (Mendelian)

### Target disease
**Disease name:** Lissencephaly spectrum disorders

**MONDO ID:** **MONDO:0018838** (“lissencephaly spectrum disorders”). This MONDO term is also explicitly returned as a disease entity in Open Targets disease–target associations. (OpenTargets Search: lissencephaly)

---

## 1. Disease Information

### 1.1 Concise overview
Lissencephaly spectrum disorders are malformations of cortical development (MCDs) characterized by abnormal cortical folding (reduced gyrification) due primarily to impaired neuronal migration and cortical lamination during embryonic development. (uctepe2024biallelictruncatingvariants pages 1-2, alsafh2024multiplexconsanguineousfamily pages 1-2)

A concise definition from a 2024 European Journal of Human Genetics report states: “**Lissencephaly (LIS) is a malformation of cortical development due to deficient neuronal migration and abnormal formation of cerebral convolutions or gyri**.” (uctepe2024biallelictruncatingvariants pages 1-2)

### 1.2 Spectrum terminology (key concepts/definitions)
A core concept is that “lissencephaly” is not a single pattern but a spectrum that includes:
- **Agyria** (near absence of gyri)
- **Pachygyria** (broad, reduced number of gyri)
- **Subcortical band heterotopia (SBH)** (a.k.a. **double cortex**) (uctepe2024biallelictruncatingvariants pages 1-2, tsai2024novellissencephalyassociatedndel1 pages 1-2)

A 2024 paper explicitly defines this: “**LIS spectrum disorder includes agyria, pachygyria and subcortical band heterotopia**.” (uctepe2024biallelictruncatingvariants pages 1-2)

### 1.3 Key identifiers and coding systems
From the tools used here, the disease has:
- **MONDO:** MONDO:0018838 (OpenTargets Search: lissencephaly)

Other identifiers (OMIM disease numbers, Orphanet IDs, ICD-10/ICD-11, MeSH IDs) were not directly retrieved in the available evidence in this run and therefore are not reported here.

### 1.4 Synonyms and alternative names
- **Subcortical band heterotopia (SBH)** is also referred to as **“double cortex”**. (tsai2024novellissencephalyassociatedndel1 pages 1-2)

### 1.5 Evidence source type
The evidence in this report comes from:
- Aggregated disease-level resources/knowledge graphs (Open Targets). (OpenTargets Search: lissencephaly)
- Human clinical genomics cohort studies and gene discovery/expansion papers (exome sequencing, GeneMatcher collaborations). (kooshavar2024diagnosticutilityof pages 1-3, uctepe2024biallelictruncatingvariants pages 1-2)
- Mechanistic human genetics with model-based functional validation (mouse in utero electroporation; scRNA-seq; spatial transcriptomics). (tsai2024novellissencephalyassociatedndel1 pages 1-2)

---

## 2. Etiology

### 2.1 Primary causal factors
Lissencephaly spectrum disorders are genetically heterogeneous, involving multiple pathways critical to neuronal migration, microtubule dynamics, dynein regulation, and cortical organization. Multiple papers emphasize microtubule/dynein/migration biology as central etiologic themes. (alsafh2024multiplexconsanguineousfamily pages 1-2, tsai2024novellissencephalyassociatedndel1 pages 1-2, pavone2023casereportstructural pages 1-2)

A 2024 NDEL1 paper highlights core upstream processes: “**cell proliferation and migration, which rely on the motor protein dynein and its regulators NDE1 and NDEL1**.” (tsai2024novellissencephalyassociatedndel1 pages 1-2)

### 2.2 Genetic risk factors (causal genes and variant classes)
Open Targets provides disease–target associations for lissencephaly and for MONDO:0018838 lissencephaly spectrum disorders, including (not exhaustive): **DCX, PAFAH1B1 (LIS1), TUBA1A, ARX, RELN, CEP85L, LAMB1, MACF1, KATNB1, TMTC3, DYNC1H1, NDE1**. (OpenTargets Search: lissencephaly)

Recent (2023–2024) primary literature expands the gene spectrum and clarifies inheritance modes:

**Autosomal recessive (AR) examples / emerging genes**
- **CASP2**: 2024 GeneMatcher-based series of **7 patients from 5 families** with **biallelic truncating/compound heterozygous variants**, described as “**compatible with an autosomal recessive pattern**.” (uctepe2024biallelictruncatingvariants pages 1-2)
- **CLASP1**: 2024 report of three affected siblings with a **homozygous** CLASP1 variant from a consanguineous family; the paper notes that segregation suggests “**a possible autosomal recessive inheritance**.” (alsafh2024multiplexconsanguineousfamily pages 1-2)

**Autosomal dominant (AD), often de novo examples (notably tubulinopathies)**
- **TUBA1A**: a 2024 case report/literature review states that for TUBA1A “**most cases show de novo autosomal dominant inheritance**,” consistent with broader tubulinopathy patterns. (ren2024lissencephalycausedby pages 1-2)

**Somatic mosaicism**
- **NDEL1 p.Arg105Pro**: 2024 Acta Neuropathologica paper identified “**the same de novo somatic mosaic NDEL1 variant**” in two unrelated patients with pachygyria ± SBH. (tsai2024novellissencephalyassociatedndel1 pages 1-2)

**X-linked**
- **DCX** is a major X-linked lissencephaly-spectrum gene in Open Targets. (OpenTargets Search: lissencephaly)

### 2.3 Environmental risk factors / protective factors / gene–environment interactions
While environmental insults can contribute to cortical malformations, quantitative environmental risk/protective factor evidence specific to “lissencephaly spectrum disorders” was not retrieved in the evidence set used here. The available evidence emphasizes genetic causation in most described cases and cohorts. (kooshavar2024diagnosticutilityof pages 1-3, uctepe2024biallelictruncatingvariants pages 1-2)

---

## 3. Phenotypes (clinical features)

### 3.1 Core phenotype set
Commonly reported features include:
- Global developmental delay / intellectual disability (ID) (uctepe2024biallelictruncatingvariants pages 1-2)
- Hypotonia (uctepe2024biallelictruncatingvariants pages 1-2)
- Seizures / epilepsy, often early-onset and refractory (alsafh2024multiplexconsanguineousfamily pages 1-2, uctepe2024biallelictruncatingvariants pages 1-2)
- Neurobehavioral phenotypes in subsets (ADHD, autistic traits, poor social skills) in CASP2-related cases (uctepe2024biallelictruncatingvariants pages 1-2)

**Abstract quote (CASP2 series):** “**Other findings included developmental delay, attention deficit hyperactivity disorder, hypotonia, seizure, poor social skills, and autistic traits.**” (uctepe2024biallelictruncatingvariants pages 1-2)

### 3.2 Age of onset and progression
Lissencephaly-spectrum disorders typically present congenitally (structural brain malformation present at birth), with clinical manifestations in infancy (developmental delay and seizures often beginning early). In a long-term lissencephaly cohort, the median age at suspected diagnosis was reported as 5 months for LIS1/PAFAH1B1 and 9 months for DCX. (proepper2026genespecificlongtermcourse pages 6-11)

### 3.3 Phenotype frequencies and quantitative data (recent cohort statistics)
A long-term cohort study (published 2026) provides quantitative complication frequencies and supportive-care utilization; although slightly outside the requested 2023–2024 priority, these data are currently among the most detailed quantitative real-world outcomes located in the retrieved evidence:
- Recurrent respiratory infections: **14/38 (37%)** in LIS1/PAFAH1B1; **1/4 (25%)** in DCX (proepper2026genespecificlongtermcourse pages 6-11)
- Dysphagia/vomiting: **23/37 (62%)** in LIS1/PAFAH1B1; **2/4 (50%)** in DCX (proepper2026genespecificlongtermcourse pages 6-11)
- Tube feeding required: **15/38 (40%)** in LIS1/PAFAH1B1; **1/5 (20%)** in DCX (proepper2026genespecificlongtermcourse pages 6-11)
- Supportive therapies: median **8** therapies per patient (range 1–17) (proepper2026genespecificlongtermcourse pages 6-11)

### 3.4 HPO term suggestions (non-exhaustive)
Based on the phenotypes explicitly present in the evidence:
- Lissencephaly (HP:0001339 appears as a disease entity in the Open Targets output) (OpenTargets Search: lissencephaly)
- Microcephaly (mentioned as common and as a prenatal abnormality in cohorts) (hu2026prenataldiagnosisof pages 1-2, proepper2026genespecificlongtermcourse pages 6-11)
- Seizures / epilepsy (alsafh2024multiplexconsanguineousfamily pages 1-2, uctepe2024biallelictruncatingvariants pages 1-2)
- Hypotonia (uctepe2024biallelictruncatingvariants pages 1-2)
- Developmental delay / intellectual disability (uctepe2024biallelictruncatingvariants pages 1-2)
- Subcortical band heterotopia / double cortex (tsai2024novellissencephalyassociatedndel1 pages 1-2, uctepe2024biallelictruncatingvariants pages 1-2)

Frequency-by-HPO mapping beyond these qualitative statements was not available in the retrieved sources.

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes (representative list)
**High-confidence, widely established genes:** PAFAH1B1 (LIS1), DCX, ARX, RELN, TUBA1A, DYNC1H1, NDE1. (OpenTargets Search: lissencephaly, tsai2024novellissencephalyassociatedndel1 pages 1-2)

**Recently expanded/implicated genes (2023–2024 evidence):**
- **NDEL1** (somatic mosaic) (tsai2024novellissencephalyassociatedndel1 pages 1-2)
- **CASP2** (biallelic truncating variants; PIDDosome component) (uctepe2024biallelictruncatingvariants pages 1-2)
- **CLASP1** (candidate AR lissencephaly) (alsafh2024multiplexconsanguineousfamily pages 1-2)

### 4.2 Variant classes and functional consequences
Examples from recent evidence:
- **Truncating / splice-disrupting loss-of-function (AR):** CASP2 truncating and splice-site variants, including frameshift and nonsense; RNA studies showed cryptic splicing generating premature stop codons. (uctepe2024biallelictruncatingvariants pages 1-2)
- **Missense variants with dominant effects (often de novo):** NDEL1 p.Arg105Pro (somatic mosaic missense) (tsai2024novellissencephalyassociatedndel1 pages 1-2); TUBA1A p.Arg402Cys in a de novo case report (ren2024lissencephalycausedby pages 1-2)

### 4.3 Modifier genes / epigenetic information
Specific validated modifier genes or disease-specific epigenetic mechanisms were not retrieved in the evidence set.

### 4.4 Chromosomal abnormalities
General MCD resources emphasize chromosomal abnormalities as part of the etiologic spectrum, and Kooshavar et al. required prior chromosomal microarray (CMA) with exclusion of pathogenic CNVs. However, lissencephaly-specific CNV frequencies were not provided in the extracted evidence snippets. (kooshavar2024diagnosticutilityof pages 1-3)

---

## 5. Environmental Information
No disease-specific environmental or lifestyle contributors were identified in the retrieved evidence set; the evidence emphasizes genetic causation and genomics-guided diagnosis. (kooshavar2024diagnosticutilityof pages 1-3, uctepe2024biallelictruncatingvariants pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Core causal chain (current understanding)
A broadly supported mechanism is:
1) Pathogenic variants disrupt proteins governing neuronal migration/cytoskeletal dynamics (microtubules, dynein regulators, microtubule-associated proteins). (alsafh2024multiplexconsanguineousfamily pages 1-2, pavone2023casereportstructural pages 1-2)
2) This impairs nucleokinesis and/or radial migration and cortical layer formation. (tsai2024novellissencephalyassociatedndel1 pages 1-2)
3) The resulting cortical malformation manifests as agyria/pachygyria/SBH and commonly leads to epilepsy and neurodevelopmental disability. (uctepe2024biallelictruncatingvariants pages 1-2)

### 6.2 Dynein–LIS1–NDE1/NDEL1 and nucleokinesis (major 2024 advance)
The 2024 Acta Neuropathologica study provides unusually direct mechanistic linkage from variant → molecular interaction → cellular process → phenotype:
- “**p.R105P expression alone strongly disrupted neuronal migration … and impaired nucleus–centrosome coupling, suggesting a failure in nucleokinesis**.” (tsai2024novellissencephalyassociatedndel1 pages 1-2)
- “**Mechanistically, p.R105P disrupted NDEL1 binding to the dynein regulator LIS1**.” (tsai2024novellissencephalyassociatedndel1 pages 1-2)

This paper also incorporates modern profiling approaches: “**single-cell RNA sequencing and spatial transcriptomic analysis**,” which showed complementary expression patterns (NDE1 in neural progenitors; NDEL1 in post-mitotic neurons). (tsai2024novellissencephalyassociatedndel1 pages 1-2)

### 6.3 PIDDosome/caspase-2 pathway (CASP2, CRADD, PIDD1)
The 2024 CASP2 study ties an apoptosis/inflammasome-like signaling complex to cortical development: “**Recently, biallelic pathogenic variants in CRADD and PIDD1 have associated with LIS impacting the previously established role of the PIDDosome in activating caspase-2. In this report, we describe biallelic truncating variants in CASP2**.” (uctepe2024biallelictruncatingvariants pages 1-2)

### 6.4 Microtubule biology and tubulinopathies
A 2023 review of TUBA1A tubulinopathies describes tubulinopathies as a heterogeneous group of tubulin-gene disorders with severe cortical and subcortical malformations, emphasizing microtubules as fundamental to neuronal migration, axonal transport, and connectivity. (pavone2023casereportstructural pages 1-2)

### 6.5 Ontology suggestions
**GO biological process (examples):** neuronal migration; nucleokinesis; microtubule-based process; cortical layer formation (supported conceptually by dynein/migration mechanism and explicitly by the NDEL1 paper’s focus on neuronal migration and nucleokinesis). (tsai2024novellissencephalyassociatedndel1 pages 1-2)

**Cell Ontology (CL) suggestions (examples):**
- Radial glial cells / neural progenitors (the NDEL1 paper explicitly discusses neural progenitors and radial glial cells in the ventricular zone) (tsai2024novellissencephalyassociatedndel1 pages 1-2)
- Post-mitotic neurons (explicitly referenced in expression analysis) (tsai2024novellissencephalyassociatedndel1 pages 1-2)

**UBERON suggestions:** cerebral cortex; ventricular zone; subventricular zone; cortical plate (explicitly referenced anatomical compartments in the NDEL1 study). (tsai2024novellissencephalyassociatedndel1 pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary system: **central nervous system**, particularly the **cerebral cortex** (six-layered neocortex) and its gyral/sulcal architecture. (tsai2024novellissencephalyassociatedndel1 pages 1-2, uctepe2024biallelictruncatingvariants pages 1-2)

### 7.2 Tissue/cell level
Key developmental compartments and cell types include ventricular zone progenitors (radial glial cells) and migrating post-mitotic neurons. (tsai2024novellissencephalyassociatedndel1 pages 1-2)

---

## 8. Temporal Development

### 8.1 Onset
Structural malformation is congenital; clinical recognition often occurs in infancy. In one cohort, median suspected diagnosis age was 5–9 months depending on gene subgroup (LIS1 vs DCX). (proepper2026genespecificlongtermcourse pages 6-11)

### 8.2 Course
Neurodevelopmental impairment and epilepsy frequently persist long-term; supportive therapies are heavily used by families. (proepper2026genespecificlongtermcourse pages 6-11)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (statistics)
A recent cohort study reports incidence estimates for classic lissencephaly of **11.7–40 per million births** and cites substantial mortality burden (approximately 50% mortality by age 10 years). (proepper2026genespecificlongtermcourse pages 6-11)

### 9.2 Inheritance patterns (summary)
- **Autosomal dominant, often de novo:** common for tubulinopathies (e.g., TUBA1A) (ren2024lissencephalycausedby pages 1-2)
- **Autosomal recessive:** CASP2; CLASP1; and other emerging genes (uctepe2024biallelictruncatingvariants pages 1-2, alsafh2024multiplexconsanguineousfamily pages 1-2)
- **X-linked:** DCX and ARX are prominent X-linked lissencephaly spectrum genes in Open Targets (OpenTargets Search: lissencephaly)
- **Somatic mosaicism:** NDEL1 p.Arg105Pro (tsai2024novellissencephalyassociatedndel1 pages 1-2)

### 9.3 Consanguinity
The CLASP1 report explicitly involves a “**multiplex consanguineous**” family and demonstrates a recessive segregation pattern, supporting consanguinity as a practical risk factor for AR forms. (alsafh2024multiplexconsanguineousfamily pages 1-2)

---

## 10. Diagnostics

### 10.1 Imaging
**MRI** is foundational for diagnosis and for defining the malformation subtype. Kooshavar et al. recruited only children with MRI-defined malformations. (kooshavar2024diagnosticutilityof pages 1-3)

### 10.2 Genetic testing strategy and real-world yields (key 2024 dataset)
Kooshavar et al. (Brain Communications; accepted Feb 2024; advance access publication Feb 28, 2024) provides “real-world” yield data for exome sequencing in pediatric brain malformations, including lissencephaly and tubulinopathies:

**Direct abstract quotes:**
- “**The overall diagnostic yield for the clinical singleton exome sequencing was 36%, which increased to 43% after research follow-up.**” (kooshavar2024diagnosticutilityof pages 1-3)
- “**The main source of increased diagnostic yield was the reanalysis of the singleton exome data to include newly discovered gene–disease associations. One additional diagnosis was made by trio exome sequencing.**” (kooshavar2024diagnosticutilityof pages 1-3)

This cohort also provides subtype frequencies in their 102-patient series: polymicrogyria 36%, tubulinopathy 10%, lissencephaly 10%, among others. (kooshavar2024diagnosticutilityof pages 1-3)

The study required CMA first and excluded cases with pathogenic CNVs, highlighting the common diagnostic workflow: CMA → exome → research reanalysis/trio when indicated. (kooshavar2024diagnosticutilityof pages 1-3)

### 10.3 Prenatal diagnostics
A 2026 prenatal MCD review quantifies the high de novo burden and limitations of routine prenatal screening:
- “**De novo mutations account for the majority of pathogenic genetic alterations identified in MCD (50.6%); up to 75.1% of pathogenic mutations cannot be detected by routine prenatal screening.**” (hu2026prenataldiagnosisof pages 1-2)

Although not lissencephaly-specific, this is directly relevant to prenatal detection of lissencephaly-spectrum malformations because gyral/sulcal abnormalities are linked to microtubule/migration genes in that review. (hu2026prenataldiagnosisof pages 1-2)

---

## 11. Outcome/Prognosis

Quantitative real-world morbidity and family impact includes high complication burdens (feeding difficulties, respiratory infections) and substantial caregiver HRQL impact. In one cohort, parental HRQL mean was **61.23 (SD 16.79)** by PedsQL Family Impact Module. (proepper2026genespecificlongtermcourse pages 6-11)

---

## 12. Treatment

### 12.1 Current applications and real-world management
There are no established disease-modifying therapies in the retrieved evidence set; care is multidisciplinary and supportive:
- Antiseizure medications (illustrated by a TUBA1A case with infantile spasms treated with valproate and vigabatrin) (ren2024lissencephalycausedby pages 1-2)
- Feeding and dysphagia management including tube feeding/PEG when needed (quantified in a cohort) (proepper2026genespecificlongtermcourse pages 6-11)
- Respiratory therapy and infection management (proepper2026genespecificlongtermcourse pages 6-11)
- Physiotherapy and other developmental therapies (proepper2026genespecificlongtermcourse pages 6-11)

In a lissencephaly cohort, “**physiotherapy and respiratory therapy [were] considered the most effective**,” and families used a median of eight supportive therapies per patient. (proepper2026genespecificlongtermcourse pages 6-11)

### 12.2 MAXO suggestions (examples)
Based on management described:
- Antiepileptic drug therapy (seizure management) (ren2024lissencephalycausedby pages 1-2)
- Enteral feeding / tube feeding (proepper2026genespecificlongtermcourse pages 6-11)
- Physiotherapy (proepper2026genespecificlongtermcourse pages 6-11)
- Respiratory therapy (proepper2026genespecificlongtermcourse pages 6-11)

---

## 13. Prevention
Primary prevention is generally not feasible for monogenic lissencephaly-spectrum disorders, but **genetic counseling** and **reproductive options** (prenatal diagnosis, preimplantation genetic testing) are practical prevention strategies once a familial pathogenic variant is known. This is supported indirectly by the emphasis on the importance of a precise genetic diagnosis for counseling and reproductive planning in genomic-diagnostic cohort work. (kooshavar2024diagnosticutilityof pages 1-3)

---

## 14. Other Species / Natural Disease
Evidence for naturally occurring non-human disease was not retrieved in this run.

---

## 15. Model Organisms and Experimental Systems
Mechanistic validation in modern lissencephaly genetics increasingly uses functional neurodevelopmental assays and advanced transcriptomics:
- The 2024 NDEL1 study used “**single-cell RNA sequencing and spatial transcriptomic analysis**” and in utero electroporation knockdown to test neuronal migration phenotypes. (tsai2024novellissencephalyassociatedndel1 pages 1-2)

This supports the use of mouse neurodevelopmental systems and multi-omic profiling as key current research implementations for lissencephaly-spectrum gene discovery and mechanism elucidation. (tsai2024novellissencephalyassociatedndel1 pages 1-2)

---

## Clinical trials (real-world implementation of research)
ClinicalTrials.gov includes an interventional study explicitly focused on genetic/transcriptomic diagnosis of lissencephalies:
- **NCT05185414** “Combining Exome and Transcriptome Data to Unravel the Genetic Basis of the Lissencephalies” (Universitair Ziekenhuis Brussel; enrollment 50; status unknown). (OpenTargets Search: lissencephaly)

---

## Summary artifact (high-yield structured facts)
| Item | Key details | Evidence/PMID/DOI/URL | Publication date | Context citation id(s) |
|---|---|---|---|---|
| Disease spectrum / definition | Lissencephaly spectrum disorders are malformations of cortical development caused chiefly by defective neuronal migration; the spectrum includes agyria, pachygyria, and subcortical band heterotopia (SBH, “double cortex”). Clinical comorbidity commonly includes developmental delay/intellectual disability, hypotonia progressing to spasticity, and seizures. | Uctepe et al., *Eur J Hum Genet* 2024, DOI: 10.1038/s41431-023-01461-2, https://doi.org/10.1038/s41431-023-01461-2 | 2024-10 | (uctepe2024biallelictruncatingvariants pages 1-2) |
| Spectrum subtypes / pathology | Classic lissencephaly is linked to cortical dyslamination genes such as **PAFAH1B1, DCX, ARX**; cobblestone lissencephaly shows distinct neuropathology associated with glycosylation pathway genes such as **POMGNT1, POMT1, POMT2**. | Brock et al., systematic review; summarized neuropathology of genetically defined MCDs | n/a | (brockUnknownyearneuropathologyofgenetically pages 13-13) |
| Standardized disease concept | MONDO includes **lissencephaly spectrum disorders = MONDO:0018838**; Open Targets links high-confidence associated targets including **DCX, PAFAH1B1, TUBA1A, ARX, RELN, CEP85L, LAMB1, MACF1**. | Open Targets disease-target association, https://platform.opentargets.org | current platform query | (OpenTargets Search: lissencephaly) |
| Key genes / common established causes | The most common established genes across classic lissencephaly are **PAFAH1B1 (LIS1)** and **DCX**; major additional genes include **TUBA1A, DYNC1H1, TUBG1, ARX, RELN, CEP85L, LAMB1, MACF1, KATNB1**. | Open Targets; Proepper et al., *Orphanet J Rare Dis* 2026, DOI: 10.1186/s13023-026-04398-z, https://doi.org/10.1186/s13023-026-04398-z | 2026-05; platform current | (OpenTargets Search: lissencephaly, proepper2026genespecificlongtermcourse pages 6-11) |
| Inheritance pattern: AD / de novo | Many lissencephaly-spectrum disorders are **autosomal dominant, often de novo**, especially tubulinopathies. **TUBA1A** is reported as the most commonly mutated tubulin gene; “most cases” show **de novo autosomal dominant inheritance**. | Ren et al., *Front Pediatr* 2024, DOI: 10.3389/fped.2024.1367305, https://doi.org/10.3389/fped.2024.1367305 | 2024-05 | (ren2024lissencephalycausedby pages 1-2) |
| Inheritance pattern: X-linked | **DCX** is an X-linked cause: males often show classic lissencephaly, while females may show SBH/double cortex; mosaic/non-coding variation can yield milder phenotypes. | Gao et al., *Heliyon* 2023, DOI: 10.1016/j.heliyon.2023.e22323, https://doi.org/10.1016/j.heliyon.2023.e22323; Open Targets | 2023-11 | (OpenTargets Search: lissencephaly) |
| Inheritance pattern: AR | Recessive forms are increasingly recognized, including **CASP2**, **CLASP1**, **TUBGCP2**, and earlier **CRADD/PIDD1**-related anterior-predominant LIS. | Uctepe et al. 2024; Alsafh et al. 2024; Yu et al. 2025 | 2024-10; 2024-08; 2025-02 | (uctepe2024biallelictruncatingvariants pages 1-2, alsafh2024multiplexconsanguineousfamily pages 1-2, yu2025tubgcp2variantscause pages 1-2) |
| Inheritance pattern: somatic mosaic | **NDEL1 p.Arg105Pro** was identified as a **de novo somatic mosaic** cause of pachygyria with or without SBH, establishing mosaic dynein-pathway disease within the lissencephaly spectrum. | Tsai et al., *Acta Neuropathol* 2024, DOI: 10.1007/s00401-023-02665-y, https://doi.org/10.1007/s00401-023-02665-y | 2024-01 | (tsai2024novellissencephalyassociatedndel1 pages 1-2) |
| Quantitative stat: exome diagnostic yield | In 102 children with brain malformations, singleton clinical exome had **36%** diagnostic yield, increasing to **43%** after research follow-up/reanalysis; **one** additional diagnosis came from trio exome. Lissencephaly represented **10%** of the cohort, and the **highest phenotype-based yields** were for cobblestone malformation, tubulinopathy, and lissencephaly. | Kooshavar et al., *Brain Communications* 2024, DOI: 10.1093/braincomms/fcae056, https://doi.org/10.1093/braincomms/fcae056 | 2024-02-28 | (kooshavar2024diagnosticutilityof pages 1-3) |
| Quantitative stat: malformation subtype mix | Among the Kooshavar cohort, commonest subtypes were **polymicrogyria 36%**, **pontocerebellar hypoplasia 14%**, **periventricular nodular heterotopia 11%**, **tubulinopathy 10%**, **lissencephaly 10%**, **cortical dysplasia 9%**. | Kooshavar et al., *Brain Communications* 2024, DOI: 10.1093/braincomms/fcae056, https://doi.org/10.1093/braincomms/fcae056 | 2024-02-28 | (kooshavar2024diagnosticutilityof pages 1-3, kooshavar2024diagnosticutilityof pages 3-4) |
| Quantitative stat: recurrent gene in diagnostics | In the Kooshavar series, the **most frequent genetic diagnosis was TUBA1A**. | Kooshavar et al., *Brain Communications* 2024, DOI: 10.1093/braincomms/fcae056, https://doi.org/10.1093/braincomms/fcae056 | 2024-02-28 | (kooshavar2024diagnosticutilityof pages 1-3) |
| Quantitative stat: prenatal genetics | In prenatal MCD literature synthesized by Hu et al., **de novo mutations accounted for 50.6%** of pathogenic alterations, and **up to 75.1%** of pathogenic mutations were not detectable by routine prenatal screening; proliferation-phase abnormalities were **62.9%** of prenatal MCD phenotypes. | Hu et al., *Biomedicines* 2026, DOI: 10.3390/biomedicines14010107, https://doi.org/10.3390/biomedicines14010107 | 2026-01 | (hu2026prenataldiagnosisof pages 1-2) |
| Quantitative stat: incidence / mortality | A recent long-term cohort summary cites classic lissencephaly incidence of **11.7–40 per million births**, infantile epileptic spasms syndrome in **57%**, and approximately **50% mortality by age 10 years**. | Proepper et al., *Orphanet J Rare Dis* 2026, DOI: 10.1186/s13023-026-04398-z, https://doi.org/10.1186/s13023-026-04398-z | 2026-05 | (proepper2026genespecificlongtermcourse pages 6-11) |
| Quantitative stat: prenatal abnormalities and age at recognition | In the Proepper cohort, prenatal abnormalities were seen in **14/37 (38%)** of **PAFAH1B1/LIS1** and **2/5 (40%)** of **DCX** cases; median age at suspected diagnosis was **5 months** for LIS1-related and **9 months** for DCX-related disease. | Proepper et al., *Orphanet J Rare Dis* 2026, DOI: 10.1186/s13023-026-04398-z, https://doi.org/10.1186/s13023-026-04398-z | 2026-05 | (proepper2026genespecificlongtermcourse pages 6-11, proepper2026genespecificlongtermcourse pages 11-16) |
| Quantitative stat: complications / feeding / respiratory | In the Proepper cohort, frequent complications included recurrent respiratory infections **14/38 (37%)** in LIS1 and **1/4 (25%)** in DCX; dysphagia/vomiting **23/37 (62%)** in LIS1 and **2/4 (50%)** in DCX; tube feeding required in **15/38 (40%)** in LIS1 and **1/5 (20%)** in DCX. | Proepper et al., *Orphanet J Rare Dis* 2026, DOI: 10.1186/s13023-026-04398-z, https://doi.org/10.1186/s13023-026-04398-z | 2026-05 | (proepper2026genespecificlongtermcourse pages 6-11) |
| Quantitative stat: supportive care burden / QoL | Families reported a median of **8 supportive therapies** per patient (range **1–17**); physiotherapy and respiratory therapy were rated most effective. Parental HRQL mean was **61.23 (SD 16.79)**, indicating substantial caregiver burden. | Proepper et al., *Orphanet J Rare Dis* 2026, DOI: 10.1186/s13023-026-04398-z, https://doi.org/10.1186/s13023-026-04398-z | 2026-05 | (proepper2026genespecificlongtermcourse pages 6-11) |
| Recent expansion: NDEL1 | First lissencephaly-associated **NDEL1** variant: two unrelated patients with pachygyria ± SBH carried the same **de novo somatic mosaic p.Arg105Pro**; mechanism implicated failure of nucleokinesis via disrupted **NDEL1–LIS1** interaction. | Tsai et al., *Acta Neuropathol* 2024, DOI: 10.1007/s00401-023-02665-y, https://doi.org/10.1007/s00401-023-02665-y | 2024-01 | (tsai2024novellissencephalyassociatedndel1 pages 1-2) |
| Recent expansion: CASP2 | **CASP2** added to the PIDDosome-related lissencephaly genes: **7 patients from 5 families** with biallelic truncating/splice variants had anterior/frontotemporal LIS and pachygyria resembling **CRADD/PIDD1** disease. | Uctepe et al., *Eur J Hum Genet* 2024, DOI: 10.1038/s41431-023-01461-2, https://doi.org/10.1038/s41431-023-01461-2 | 2024-10 | (uctepe2024biallelictruncatingvariants pages 1-2) |
| Recent expansion: CLASP1 | **CLASP1** emerged as a candidate recessive lissencephaly gene in a multiplex consanguineous family; **3 siblings** had homozygous **c.4442G>A p.Arg1481His** with classic lissencephaly, microcephaly, severe developmental delay, and early refractory epilepsy. | Alsafh et al., *Neurology Genetics* 2024, DOI: 10.1212/NXG.0000000000200172, https://doi.org/10.1212/NXG.0000000000200172 | 2024-08 | (alsafh2024multiplexconsanguineousfamily pages 1-2) |
| Diagnostic approach: imaging | Brain **MRI** remains the core diagnostic modality for defining the malformation pattern and guiding gene prioritization. Recognizable signatures include anterior/frontotemporal LIS in **CASP2/CRADD/PIDD1**, posterior>anterior classic LIS plus thin splenium/pontine hypoplasia in **CLASP1**, and pachygyria ± SBH in mosaic **NDEL1**. | Uctepe et al. 2024; Alsafh et al. 2024; Tsai et al. 2024 | 2024 | (uctepe2024biallelictruncatingvariants pages 1-2, alsafh2024multiplexconsanguineousfamily pages 1-2, tsai2024novellissencephalyassociatedndel1 pages 1-2) |
| Diagnostic approach: genetics | Recommended workflow supported by recent evidence: **CMA first** to detect CNVs; then **exome sequencing**; then **periodic reanalysis** because reanalysis contributed more to added diagnoses than trio expansion in a real-world MCD cohort. | Kooshavar et al., *Brain Communications* 2024, DOI: 10.1093/braincomms/fcae056, https://doi.org/10.1093/braincomms/fcae056 | 2024-02-28 | (kooshavar2024diagnosticutilityof pages 1-3, kooshavar2024diagnosticutilityof pages 3-4) |
| Diagnostic approach: prenatal | For suspected fetal cortical malformations, **fetal neurosonography + fetal MRI + NGS/WES** are increasingly emphasized; routine prenatal screens miss many pathogenic variants. | Hu et al., *Biomedicines* 2026, DOI: 10.3390/biomedicines14010107, https://doi.org/10.3390/biomedicines14010107 | 2026-01 | (hu2026prenataldiagnosisof pages 1-2) |
| Management / supportive therapies | No disease-modifying therapy is established; current care is multidisciplinary and supportive: **antiepileptic therapy**, feeding support including tube feeding/PEG when needed, **physiotherapy**, **respiratory therapy**, developmental therapies, and caregiver support. Physiotherapy and respiratory therapy were reported as most effective in family surveys. | Proepper et al., *Orphanet J Rare Dis* 2026, DOI: 10.1186/s13023-026-04398-z, https://doi.org/10.1186/s13023-026-04398-z; Ren et al. 2024 | 2026-05; 2024-05 | (proepper2026genespecificlongtermcourse pages 6-11, ren2024lissencephalycausedby pages 1-2) |


*Table: This table condenses high-yield definitions, genetics, quantitative clinical statistics, recent gene discoveries, and current diagnostic/management points for lissencephaly spectrum disorders. It is useful as a structured reference for building a disease knowledge-base entry with linked evidence.*

---

## Key recent developments (2023–2024 emphasis)
1) **Diagnostic genomics evidence in real-world cohorts (2024):** singleton exome yield 36% rising to 43% with reanalysis; reanalysis is a major contributor to additional diagnoses, and TUBA1A is a frequent diagnosis. (kooshavar2024diagnosticutilityof pages 1-3)
2) **New mechanistic gene association with modern multi-omics (2024):** somatic mosaic **NDEL1** p.Arg105Pro linked to nucleokinesis failure via disrupted LIS1 binding, with scRNA-seq/spatial transcriptomics and functional migration assays. (tsai2024novellissencephalyassociatedndel1 pages 1-2)
3) **Expansion of AR lissencephaly genes (2024):** **CASP2** biallelic truncating variants implicate the PIDDosome/caspase-2 axis in cortical development; **CLASP1** is a candidate AR lissencephaly gene in a consanguineous family, supporting microtubule minus-end stabilization biology in disease. (uctepe2024biallelictruncatingvariants pages 1-2, alsafh2024multiplexconsanguineousfamily pages 1-2)

---

## URLs and publication dates (selected high-authority recent sources)
- Kooshavar et al. *Brain Communications* (Advance access publication **2024-02-28**): https://doi.org/10.1093/braincomms/fcae056 (kooshavar2024diagnosticutilityof pages 1-3)
- Tsai et al. *Acta Neuropathologica* (**2024**, accepted 2023-11-24; published 2024): https://doi.org/10.1007/s00401-023-02665-y (tsai2024novellissencephalyassociatedndel1 pages 1-2)
- Uctepe et al. *European Journal of Human Genetics* (Published online **2023-10-26**, journal year **2024**): https://doi.org/10.1038/s41431-023-01461-2 (uctepe2024biallelictruncatingvariants pages 1-2)
- Alsafh et al. *Neurology Genetics* (**2024**): https://doi.org/10.1212/NXG.0000000000200172 (alsafh2024multiplexconsanguineousfamily pages 1-2)
- Pavone et al. *Frontiers in Pediatrics* (**2023-09**): https://doi.org/10.3389/fped.2023.1210272 (pavone2023casereportstructural pages 1-2)
- Ren et al. *Frontiers in Pediatrics* (**2024-05**): https://doi.org/10.3389/fped.2024.1367305 (ren2024lissencephalycausedby pages 1-2)



References

1. (OpenTargets Search: lissencephaly): Open Targets Query (lissencephaly, 25 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (uctepe2024biallelictruncatingvariants pages 1-2): Eyyup Uctepe, Barbara Vona, Fatma Nisa Esen, F. Mujgan Sonmez, Thomas Smol, Sait Tümer, Hanifenur Mancılar, Dilan Ece Geylan Durgun, Odile Boute, Meysam Moghbeli, Ehsan Ghayoor Karimiani, Narges Hashemi, Behnoosh Bakhshoodeh, Hyung Goo Kim, Reza Maroofian, and Ahmet Yesilyurt. Bi-allelic truncating variants in casp2 underlie a neurodevelopmental disorder with lissencephaly. European Journal of Human Genetics, 32:52-60, Oct 2024. URL: https://doi.org/10.1038/s41431-023-01461-2, doi:10.1038/s41431-023-01461-2. This article has 13 citations and is from a domain leading peer-reviewed journal.

3. (alsafh2024multiplexconsanguineousfamily pages 1-2): Rawan Alsafh, Amal Alhashem, Aly Elsyed, Zafer Yüksel, Kalthoum Graiess-Tlili, Khalid Hundallah, Farah Thabet, and Brahim Tabarki. Multiplex consanguineous family highlights <i>clasp1</i> as a candidate gene for lissencephaly. Aug 2024. URL: https://doi.org/10.1212/nxg.0000000000200172, doi:10.1212/nxg.0000000000200172. This article has 6 citations.

4. (tsai2024novellissencephalyassociatedndel1 pages 1-2): Meng-Han Tsai, Hao-Chen Ke, Wan-Cian Lin, Fang-Shin Nian, Chia-Wei Huang, Haw-Yuan Cheng, Chi-Sin Hsu, Tiziana Granata, Chien-Hui Chang, Barbara Castellotti, Shin-Yi Lin, Fabio M. Doniselli, Cheng-Ju Lu, Silvana Franceschetti, Francesca Ragona, Pei-Shan Hou, Laura Canafoglia, Chien-Yi Tung, Mei-Hsuan Lee, Won-Jing Wang, and Jin-Wu Tsai. Novel lissencephaly-associated ndel1 variant reveals distinct roles of nde1 and ndel1 in nucleokinesis and human cortical malformations. Acta Neuropathologica, Jan 2024. URL: https://doi.org/10.1007/s00401-023-02665-y, doi:10.1007/s00401-023-02665-y. This article has 11 citations and is from a highest quality peer-reviewed journal.

5. (kooshavar2024diagnosticutilityof pages 1-3): Daniz Kooshavar, David J Amor, Kirsten Boggs, Naomi Baker, Christopher Barnett, Michelle G de Silva, Samantha Edwards, Michael C Fahey, Justine E Marum, Penny Snell, Kiymet Bozaoglu, Kate Pope, Shekeeb S Mohammad, Kate Riney, Rani Sachdev, Ingrid E Scheffer, Sarah Schenscher, John Silberstein, Nicholas Smith, Melanie Tom, Tyson L Ware, Paul J Lockhart, and Richard J Leventer. Diagnostic utility of exome sequencing followed by research reanalysis in human brain malformations. Brain Communications, Feb 2024. URL: https://doi.org/10.1093/braincomms/fcae056, doi:10.1093/braincomms/fcae056. This article has 6 citations and is from a peer-reviewed journal.

6. (pavone2023casereportstructural pages 1-2): Piero Pavone, Pasquale Striano, Giovanni Cacciaguerra, Simona Domenica Marino, Enrico Parano, Xena Giada Pappalardo, Raffaele Falsaperla, and Martino Ruggieri. Case report: structural brain abnormalities in tuba1a-tubulinopathies: a narrative review. Frontiers in Pediatrics, Sep 2023. URL: https://doi.org/10.3389/fped.2023.1210272, doi:10.3389/fped.2023.1210272. This article has 7 citations.

7. (ren2024lissencephalycausedby pages 1-2): Sijing Ren, Yu Kong, Ruihan Liu, Qiu-bo Li, Xuehua Shen, and Qing-xia Kong. Lissencephaly caused by a de novo mutation in tubulin tuba1a: a case report and literature review. Frontiers in Pediatrics, May 2024. URL: https://doi.org/10.3389/fped.2024.1367305, doi:10.3389/fped.2024.1367305. This article has 5 citations.

8. (proepper2026genespecificlongtermcourse pages 6-11): Christiane R. Proepper, Lisa-Maria Schwarz, Sofia M. Schuetz, Katja von Au, Thomas Bast, Nathalie Beaud, Ingo Borggraefe, Friedrich Bosch, Melanie Busse, Jena Chung, Otfried Debus, Katharina Diepold, Thomas Fries, Gero von Gersdorff, Martin Haeussler, Andreas Hahn, Till Hartlieb, Ralf Heiming, Peter Herkenrath, Gerhard Kluger, Jonas H. Kreth, Gerhard Kurlemann, Peter Moeller, Deborah J. Morris-Rosendahl, Axel Panzer, Heike Philippi, Sophia Ruegner, Carolina Toepfer, Silvia Vieker, Adelheid Wiemer-Kruel, Anika Winter, Gerhard Schuierer, Ute Hehr, and Tobias Geis. Gene-specific long-term course, neurodevelopmental outcome and quality of life in patients with lis1/pafah1b1-, dcx-, dync1h1-, tuba1a- and tubg1-related lissencephaly. Orphanet Journal of Rare Diseases, May 2026. URL: https://doi.org/10.1186/s13023-026-04398-z, doi:10.1186/s13023-026-04398-z. This article has 0 citations and is from a peer-reviewed journal.

9. (hu2026prenataldiagnosisof pages 1-2): Jinhua Hu, Xiaogang Xu, Ping Jiang, Ruibin Huang, Jiani Yuan, Long Lu, and Jin Han. Prenatal diagnosis of malformations of cortical development: a review of genetic and imaging advances. Biomedicines, 14:107, Jan 2026. URL: https://doi.org/10.3390/biomedicines14010107, doi:10.3390/biomedicines14010107. This article has 1 citations.

10. (brockUnknownyearneuropathologyofgenetically pages 13-13): S Brock, F Cools, and AC Jansen. Neuropathology of genetically defined malformations of cortical development-a systematic. Unknown journal, Unknown year.

11. (yu2025tubgcp2variantscause pages 1-2): Tao Yu, Miao Yu, Xueyan Liu, and Hua Wang. Tubgcp2 variants cause lissencephaly spectrum disorders: a case report and literature review. Frontiers in Pediatrics, Feb 2025. URL: https://doi.org/10.3389/fped.2025.1476390, doi:10.3389/fped.2025.1476390. This article has 1 citations.

12. (kooshavar2024diagnosticutilityof pages 3-4): Daniz Kooshavar, David J Amor, Kirsten Boggs, Naomi Baker, Christopher Barnett, Michelle G de Silva, Samantha Edwards, Michael C Fahey, Justine E Marum, Penny Snell, Kiymet Bozaoglu, Kate Pope, Shekeeb S Mohammad, Kate Riney, Rani Sachdev, Ingrid E Scheffer, Sarah Schenscher, John Silberstein, Nicholas Smith, Melanie Tom, Tyson L Ware, Paul J Lockhart, and Richard J Leventer. Diagnostic utility of exome sequencing followed by research reanalysis in human brain malformations. Brain Communications, Feb 2024. URL: https://doi.org/10.1093/braincomms/fcae056, doi:10.1093/braincomms/fcae056. This article has 6 citations and is from a peer-reviewed journal.

13. (proepper2026genespecificlongtermcourse pages 11-16): Christiane R. Proepper, Lisa-Maria Schwarz, Sofia M. Schuetz, Katja von Au, Thomas Bast, Nathalie Beaud, Ingo Borggraefe, Friedrich Bosch, Melanie Busse, Jena Chung, Otfried Debus, Katharina Diepold, Thomas Fries, Gero von Gersdorff, Martin Haeussler, Andreas Hahn, Till Hartlieb, Ralf Heiming, Peter Herkenrath, Gerhard Kluger, Jonas H. Kreth, Gerhard Kurlemann, Peter Moeller, Deborah J. Morris-Rosendahl, Axel Panzer, Heike Philippi, Sophia Ruegner, Carolina Toepfer, Silvia Vieker, Adelheid Wiemer-Kruel, Anika Winter, Gerhard Schuierer, Ute Hehr, and Tobias Geis. Gene-specific long-term course, neurodevelopmental outcome and quality of life in patients with lis1/pafah1b1-, dcx-, dync1h1-, tuba1a- and tubg1-related lissencephaly. Orphanet Journal of Rare Diseases, May 2026. URL: https://doi.org/10.1186/s13023-026-04398-z, doi:10.1186/s13023-026-04398-z. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Lissencephaly_Spectrum_Disorders-deep-research-falcon_artifacts/artifact-00.md)