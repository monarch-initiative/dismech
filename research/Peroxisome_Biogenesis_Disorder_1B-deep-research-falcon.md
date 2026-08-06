---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T01:14:34.995200'
end_time: '2026-07-31T01:24:28.251318'
duration_seconds: 593.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peroxisome Biogenesis Disorder 1B
  mondo_id: MONDO:0011101,PEX1-related,OMIM:601539,non-classic-Zellweger-spectrum/NALD/IRD
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Peroxisome_Biogenesis_Disorder_1B-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome Biogenesis Disorder 1B
- **MONDO ID:** MONDO:0011101,PEX1-related,OMIM:601539,non-classic-Zellweger-spectrum/NALD/IRD (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 1B** covering all of the
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
- **Disease Name:** Peroxisome Biogenesis Disorder 1B
- **MONDO ID:** MONDO:0011101,PEX1-related,OMIM:601539,non-classic-Zellweger-spectrum/NALD/IRD (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 1B** covering all of the
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


# Peroxisome Biogenesis Disorder 1B (PEX1-related non-classic Zellweger spectrum disorder)

## Scope and evidence note

**Peroxisome biogenesis disorder 1B (PBD1B)** is best treated as the **non-classic/residual-function end of PEX1-related Zellweger spectrum disorder (ZSD)** rather than as a sharply separated disease. Historical labels—**neonatal adrenoleukodystrophy (NALD)** and **infantile Refsum disease (IRD)**—describe severity bands within a continuous phenotype. Consequently, much clinical guidance is ZSD-level evidence, whereas the strongest PBD1B-specific evidence concerns individuals carrying the residual-function **PEX1 c.2528G>A (p.Gly843Asp; G843D)** allele.

The evidence base is limited by rarity, small cohorts, genotype heterogeneity, and replacement of historical NALD/IRD labels by ZSD. Findings below are identified as human clinical, patient-cell/in-vitro, or model-organism evidence. Exact PMID values were not present in most retrieved full texts; DOI links are therefore supplied rather than inventing identifiers.

## 1. Disease information

PBD1B is an **autosomal-recessive Mendelian disorder caused by biallelic pathogenic PEX1 variants**, producing incomplete peroxisome assembly and impaired import of matrix enzymes. It generally presents less severely than classic neonatal Zellweger syndrome but remains a chronic multisystem disease involving hearing, retina, nervous system, liver, skeleton, adrenal function, and growth. ZSD encompasses classic Zellweger syndrome, NALD, and IRD; historical survival descriptions place NALD into adolescence and IRD into adulthood, although residual-function PEX1 patients may survive considerably longer. PEX1 is the most frequently implicated ZSD gene—reported as 58.9% in one summarized cohort—followed by PEX6 (15.9%) and PEX12 (7.1%). (chang2022geneticsbehindcerebral pages 26-27)

**Identifiers and mappings**

- **MONDO:** MONDO:0011101, as supplied for PBD1B; contemporary broader mappings include **MONDO:0100259**, “peroxisome biogenesis disorder due to PEX1 defect,” and **MONDO:0019609**, “Zellweger spectrum disorder.” Open Targets independently links PEX1/ENSG00000127980 to all three disease concepts. (OpenTargets Search: Zellweger spectrum disorder-PEX1)
- **OMIM phenotype:** **601539**, per the query, historically PBD1B/NALD-IRD. The severe PEX1-related allelic phenotype is conventionally PBD1A.
- **Orphanet:** the broader entity is **ORPHA:79189**, peroxisome biogenesis disorder–Zellweger syndrome spectrum. (OpenTargets Search: Zellweger spectrum disorder-PEX1)
- **MeSH:** use *Zellweger Syndrome* and *Peroxisomal Disorders*; MeSH does not reliably preserve the PBD1B severity subdivision.
- **ICD:** no robust PEX1/PBD1B-specific ICD-10 code was established in the retrieved evidence. Use the jurisdiction-specific code for disorders of peroxisomal function/congenital metabolic disease, with genetic specificity stored separately. ICD-11 likewise should be verified against the current national release before production use.
- **Synonyms:** PBD1B; PEX1-related non-classic ZSD; PEX1 deficiency; peroxisome biogenesis disorder due to PEX1 defect; neonatal adrenoleukodystrophy; infantile Refsum disease; mild/intermediate Zellweger spectrum disorder.

This report synthesizes **aggregated disease-level resources and published cohorts**, not individual EHR records. The 2024 ophthalmic study is patient-level research aggregated across ten participants.

## 2. Etiology, risk, and protective factors

### Causal factor

The necessary cause is **biallelic germline PEX1 dysfunction**. PEX1 encodes peroxisomal biogenesis factor 1, an AAA-family ATPase that complexes with PEX6. The complex supplies ATP-dependent mechanical activity needed to recycle the PEX5 matrix-protein receptor. Dysfunction compromises import of numerous enzymes rather than one metabolic reaction, explaining the broad biochemical and organ phenotype. PEX1–ZSD association is supported by curated human genetic evidence. (OpenTargets Search: Zellweger spectrum disorder-PEX1, chang2022geneticsbehindcerebral pages 26-27)

### Genetic risk and modifiers

- **p.Gly843Asp:** the principal residual-function allele associated with non-classic disease. Nine of ten patients in the 2024 mild-PBD cohort were homozygous; one carried p.Gly843Asp in trans with **c.2097_2098insT (p.Ile700TyrfsTer42)**. (karuntu2024systematicstudyof pages 5-6)
- A residual-function missense allele on both chromosomes generally predicts milder disease than two null alleles; a null allele in trans may worsen visual or systemic severity. This is probabilistic, not deterministic.
- Marked inter- and intrafamilial variability despite identical p.Gly843Asp genotypes supports additional genetic, epigenetic, metabolic, or environmental modifiers, but no validated clinical modifier gene or protective allele was identified. (karuntu2024systematicstudyof pages 12-13)
- Variants are **germline**, not somatic. Pathogenic classes include missense, nonsense, frameshift, splice, and deletion/duplication alleles. Variant-level ACMG classification and gnomAD frequency must be checked in the current ClinVar/gnomAD record; no defensible universal frequency was available from the retrieved literature.

### Environmental, lifestyle, infectious, and protective factors

No toxin, infection, smoking behavior, diet, occupation, sex, or lifestyle exposure is known to cause PBD1B. Dietary phytanic acid can increase biochemical substrate burden after disease is established, but is not a primary cause. Avoidance of prolonged fasting, adequate nutrition, and avoidance of hepatotoxic exposures are complication-reduction measures rather than proven protection against disease onset. No established gene–environment interaction, protective variant, vaccine strategy, or environmental primary prevention exists.

## 3. Phenotypes

Clinical expression ranges from neonatal hypotonia/feeding problems to childhood hearing and visual impairment or an insidious adolescent/adult neurologic-hepatic presentation. Frequencies outside the recent ophthalmic cohort should be encoded as qualitative because well-powered PEX1-PBD1B frequency studies are lacking.

| Domain and suggested HPO terms | Typical onset/course | Clinical and functional effect |
|---|---|---|
| **Sensorineural hearing impairment**—HP:0000407 | Often infancy/childhood; generally persistent or progressive. Hearing loss was the presenting manifestation in 7/10 patients in the 2024 mild cohort. | Language acquisition, communication, education, and social participation; may mimic Usher syndrome when combined with retinal dystrophy. (karuntu2024systematicstudyof pages 12-13) |
| **Retinal dystrophy/retinitis-pigmentosa-like retinopathy**—HP:0000556; **nyctalopia** HP:0000662; **reduced visual acuity** HP:0007663; **nystagmus** HP:0000639; **hypermetropia** HP:0000540 | Often within the first two years, variably progressive. In 10 patients, initial ocular findings included nyctalopia 6/10, nystagmus 4/10, and reduced acuity 3/10. | Moderate–severe visual disability, impaired mobility/night navigation and reading. Median BCVA was 0.8 logMAR and remained stable over 10.8 years in this selected mild cohort. (karuntu2024systematicstudyof pages 5-6, karuntu2024systematicstudyof pages 12-13) |
| **Retinal structural abnormalities**—consider HP:0000610/retinal degeneration plus local OCT annotations | All nine assessed patients had SD-OCT abnormalities; central cystoid cavities occurred in 16 eyes, external-limiting-membrane/ellipsoid-zone loss in 15 eyes, and outer-nuclear-layer fluid in 14 eyes. | Can further reduce central vision; the cavities resemble retinoschisis/cystoid change. (karuntu2024systematicstudyof pages 5-6) |
| **Hypotonia**—HP:0001252; **developmental delay** HP:0001263; **intellectual disability** HP:0001249 | Congenital/infantile in intermediate disease; milder patients may have near-normal cognition. Variable and sometimes progressive through secondary leukodystrophy/neuropathy. | Feeding, mobility, schooling, independence. ZSD-level evidence includes seizures and developmental delay. (chang2022geneticsbehindcerebral pages 26-27) |
| **Seizures**—HP:0001250; **leukodystrophy** HP:0002415; **peripheral neuropathy** HP:0009830; **ataxia** HP:0001251 | Childhood to adulthood; may be absent initially and emerge later. | Falls, loss of ambulation, self-care dependency. |
| **Hepatomegaly**—HP:0002240; **elevated transaminases** HP:0002910; **cholestasis** HP:0001396; **hepatic fibrosis/cirrhosis** HP:0001395/HP:0002613 | Liver abnormalities may begin in infancy and remain mild or progress over decades. | Medication risk, bleeding/coagulopathy, portal disease, and possible malignancy risk. Chronic liver disease is a major determinant of survival and quality of life in ZSD models and cohorts. (chang2022geneticsbehindcerebral pages 26-27, klouwer2018thecholicacid pages 1-2) |
| **Failure to thrive/short stature**—HP:0001508/HP:0004322; **feeding difficulty** HP:0011968 | Usually early and chronic. | Nutritional support and caregiver burden. |
| **Adrenal insufficiency**—HP:0000824 | Variable, sometimes clinically silent; can emerge during follow-up. | Risk of adrenal crisis during illness; requires biochemical surveillance and stress-dose planning if confirmed. |
| **Skeletal abnormalities**—osteopenia HP:0000938; fractures HP:0002757; calcific stippling HP:0000929 | Congenital stippling is more typical of severe disease; osteopenia/fractures may appear later. | Pain and reduced mobility. |
| **Renal involvement**—renal cysts HP:0000107/hyperoxaluria HP:0003153 | Variable; severe congenital cysts are less typical of non-classic disease, whereas nephrolithiasis/oxalate problems can occur later. | Renal surveillance and hydration burden. |

**Quality of life:** no validated PBD1B-specific EQ-5D, SF-36, or PROMIS effect sizes were found. A completed proxy-reported ZSD symptom/QoL study, **NCT03440905**, enrolled 92, but no retrieved result text permitted quantitative claims. Hearing/visual loss, mobility limitation, chronic surveillance, nutritional problems, and caregiver demands are the major plausible drivers.

## 4. Genetic and molecular information

- **Gene:** PEX1; approved name *peroxisomal biogenesis factor 1*; Ensembl **ENSG00000127980**. The HGNC identifier should be imported directly from current HGNC rather than inferred. (OpenTargets Search: Zellweger spectrum disorder-PEX1)
- **Protein:** a cytosolic/peroxisome-associated AAA ATPase that forms a PEX1–PEX6 complex at the peroxisomal membrane.
- **Disease mechanism:** predominantly recessive **loss or reduction of function**. p.Gly843Asp is a hypomorphic missense allele with temperature-sensitive/misfolding and assembly defects reported in cell systems; truncating alleles generally provide little or no residual activity.
- **Representative variants:** **NM_000466.3:c.2528G>A, p.(Gly843Asp)**, residual-function missense; **c.2097_2098insT, p.(Ile700TyrfsTer42)**, frameshift/null. Exact transcript versions and ClinVar assertions must be normalized during ingestion. The 2024 cohort provides direct human genotype evidence. (karuntu2024systematicstudyof pages 5-6)
- **Penetrance:** expected to be high for pathogenic biallelic genotypes, but organ-specific expressivity is highly variable. No evidence supports anticipation. Gonadal mosaicism is theoretically possible but not established as a recurrent feature.
- **Chromosomal abnormalities:** focal PEX1 deletions/duplications can be causal, but PBD1B is not characteristically an aneuploidy or translocation syndrome. CMA/karyotype/FISH are not first-line unless another genomic disorder is suspected.
- **Epigenetics:** no validated PBD1B-specific DNA-methylation signature or clinically actionable chromatin alteration was found.

## 5. Environmental information

Environmental toxins, radiation, pollution, pathogens, alcohol, or smoking have no established etiologic role. Management commonly minimizes fasting and hepatotoxic exposure and uses balanced nutrition. Dietary restriction of phytanic-acid-rich foods is sometimes considered where phytanic acid is elevated, but aggressive restriction in a growing child may worsen nutrition and lacks strong outcome evidence. PBD1B is neither infectious nor zoonotic.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic PEX1 loss/hypomorphism.
2. **Protein-complex defect:** reduced PEX1–PEX6 AAA-ATPase activity compromises extraction/recycling of ubiquitinated PEX5 from the peroxisomal membrane.
3. **Organelle defect:** failed PEX5 recycling impairs PTS1/PTS2 matrix-protein import; enzymes remain cytosolic, residual peroxisomes are enlarged/abnormal, and pexophagy may increase.
4. **Primary metabolic consequences:** reduced peroxisomal β-oxidation of very-long-chain and branched-chain fatty acids; reduced α-oxidation; impaired C27-to-C24 bile-acid maturation; reduced ether-lipid/plasmalogen synthesis; disturbed DHA and redox homeostasis.
5. **Downstream injury:** accumulation of C26:0, phytanic/pristanic acids and DHCA/THCA, combined with plasmalogen/DHA deficiency, disrupts membranes, myelin, photoreceptors, hepatocytes, adrenal cortex, and peripheral nerves. Mitochondrial dysfunction, oxidative stress, altered lipid signaling, inflammation, fibrosis, and cell death amplify disease.

PEX1 and PEX6 are cytosolic AAA ATPases forming an ATP-dependent heteromer required for substrate translocation/unfolding. (chang2022geneticsbehindcerebral pages 26-27) In PEX1-G843D cell models, autophagy/pexophagy is not simply corrective: a 2024 mechanistic study found that upregulated pexophagy can consume ULK1 and impair mitophagy and aggrephagy, suggesting cross-organelle proteostasis stress. This remains cell-model evidence, not a validated clinical biomarker.

### Biochemistry and omics

Expected human diagnostic signatures are elevated C26:0 and C26:0-lysophosphatidylcholine, elevated phytanic/pristanic acids and C27 bile-acid intermediates, and decreased erythrocyte plasmalogens; mild patients may have borderline conventional VLCFA results. A 2023 human LC-MS/MS study of 598 samples, including 19 PEX1/PEX6-PBD patients, identified elevated C8-DC–C22-DC dicarboxylic acylcarnitines; C20-DC was elevated in 100% and C22-DC in 68% of PBD cases. These are promising second-tier markers, not definitive tests. (wangler2023dicarboxylicacylcarnitinebiomarkers pages 1-2, wangler2023dicarboxylicacylcarnitinebiomarkers pages 8-9)

In the Pex1-G844D mouse, C26:0 and C24:0 were 2.5- and 2.2-fold elevated; pristanic and phytanic acids were 58- and 51-fold elevated; DHCA and THCA reached 282- and 550-fold elevations; mature cholic acid fell to 9–41% of control; and C26:0-lysoPC rose 7.52-fold. Secondary hepatocyte mitochondrial respiration/ATP production fell by approximately 50–70%. These quantitative values are **model-organism**, not human reference ranges. (chen2025longitudinalstudyof pages 19-21)

Mouse lipidomics showed hepatic triglyceride/cholesterol accumulation with deficient ether phosphatidylcholines and sphingomyelins, while circulating triglycerides and membrane lipids decreased. Transcript/protein data supported PPARα activation, increased hepatic lipid uptake, reduced de-novo lipogenesis, altered glucose/glycogen metabolism, and hypoinsulinemia. (chen2025longitudinalstudyof pages 38-43, chen2025longitudinalstudyof pages 6-10)

**Suggested ontology annotations:**

- GO biological process: peroxisome organization; protein import into peroxisome matrix; peroxisomal transport; very-long-chain-fatty-acid β-oxidation; phytanic-acid α-oxidation; ether-lipid biosynthesis; bile-acid biosynthesis; selective autophagy/pexophagy; cellular lipid homeostasis; response to oxidative stress.
- GO cellular component: peroxisome; peroxisomal membrane; peroxisomal matrix; PEX1–PEX6 ATPase complex; cytosol; mitochondrion as a secondary site.
- Cell Ontology suggestions: hepatocyte; retinal photoreceptor cell/rod photoreceptor; retinal pigment epithelial cell; oligodendrocyte; Schwann cell; neuron; adrenal cortical cell; renal proximal-tubule epithelial cell.
- CHEBI concepts: hexacosanoic acid/C26:0; phytanic acid; pristanic acid; DHCA; THCA; cholic acid; plasmalogens; docosahexaenoic acid.

No disease-specific single-cell atlas, spatial transcriptomic map, or validated human multi-omic classifier was identified.

## 7. Anatomical structures affected

**Primary organs/systems:** brain and white matter, peripheral nerves, cochlea, retina/retinal pigment epithelium, liver and biliary system, adrenal cortex, skeleton, kidney, and gastrointestinal/nutritional system. Severe disease also affects craniofacial development and lung.

**Suggested UBERON mappings:** liver; hepatic lobule; retina; retinal photoreceptor layer; retinal pigment epithelium; cochlea/organ of Corti; cerebral white matter; peripheral nerve; adrenal gland/adrenal cortex; kidney/proximal tubule; bone.

At subcellular level the primary compartment is the **peroxisome**, especially membrane-associated import/receptor-recycling machinery and matrix-protein import. Mitochondria, ER/lipid droplets, and autophagosomes are downstream interacting compartments. Mouse ultrastructure showed cytosolic catalase mislocalization, scarce/enlarged peroxisomes, and enlarged mitochondria with abnormal cristae. (chen2025longitudinalstudyof pages 31-38)

Disease is typically bilateral/systemic, not lateralized; retinal and hearing manifestations are generally bilateral but can be asymmetric in severity.

## 8. Temporal development

PBD1B is genetically present from conception, but recognition ranges from infancy to adulthood. Early clues include hypotonia, feeding difficulty, hearing loss, nystagmus, nyctalopia, or hepatomegaly. In the 2024 p.Gly843Asp-dominant cohort, median symptom onset was six months and median symptom duration at assessment was 22.1 years. (karuntu2024systematicstudyof pages 5-6)

The course is **chronic lifelong and variably progressive**, not relapsing-remitting. A useful clinical staging framework is:

1. **Early:** hearing/visual symptoms, growth/feeding difficulty, biochemical abnormalities, mild liver disease.
2. **Intermediate:** established retinal dystrophy, neuropathy/ataxia, osteopenia, adrenal or renal complications, chronic hepatopathy.
3. **Advanced:** severe sensory disability, loss of mobility, leukodystrophy, cirrhosis/portal complications, and potentially hepatic malignancy.

No spontaneous molecular remission is expected. Apparent stability of one domain does not imply global stability: visual acuity was stable over 10.8 years in the selected mild cohort despite structural retinal disease. (karuntu2024systematicstudyof pages 5-6)

Critical windows include early hearing/language intervention, visual habilitation, nutrition and liver surveillance, and adrenal stress planning. Prenatal and early-life disease modification remains investigational.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two confirmed heterozygous parents, each pregnancy has a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability. Males and females should be affected equally; the 2024 cohort’s 6/10 male composition is too small to indicate sex bias. (karuntu2024systematicstudyof pages 5-6)

ZSD overall is rare; a reliable PBD1B-specific incidence/prevalence was not established by the retrieved evidence. Published ZSD birth-incidence estimates vary geographically and by ascertainment, and milder adult disease is likely underdiagnosed. PEX1 accounts for the largest molecular subgroup. (chang2022geneticsbehindcerebral pages 26-27)

- **Penetrance:** likely high for biallelic pathogenic variants, with variable age-dependent manifestations.
- **Expressivity:** markedly variable, including within families. (karuntu2024systematicstudyof pages 12-13)
- **Anticipation:** not expected.
- **Consanguinity:** increases the probability of homozygous rare alleles but is not required.
- **Founder effects:** possible for particular alleles/populations; no single PBD1B founder population was established here.
- **Carrier frequency/geographic variant frequency:** should be calculated from ancestry-stratified gnomAD rather than inferred from case cohorts.

## 10. Diagnostics

### Recommended workflow

1. **Clinical suspicion:** bilateral sensorineural hearing loss plus retinal dystrophy, unexplained liver disease, developmental/neurologic findings, adrenal dysfunction, or a phenotype mistaken for Usher syndrome. Two patients in the 2024 cohort were initially diagnosed with Usher syndrome. (karuntu2024systematicstudyof pages 5-6, karuntu2024systematicstudyof pages 12-13)
2. **Biochemical screen:** plasma VLCFA ratios/concentrations including C26:0; C26:0-lysoPC; phytanic and pristanic acids; plasma/urine DHCA and THCA; erythrocyte plasmalogens. Add liver enzymes, bilirubin, INR/coagulation factors, glucose, fat-soluble vitamins, ACTH/cortisol, renal/urine oxalate assessment as clinically indicated.
3. **Molecular confirmation:** a peroxisomal-disorder or leukodystrophy/hearing-retinal panel including **PEX1** is efficient. If phenotype strongly indicates PEX1, sequence plus deletion/duplication analysis is reasonable. WES/WGS is useful for atypical or biochemically equivocal cases and can identify noncoding/structural alleles; RNA studies may resolve splice VUS.
4. **Functional confirmation when needed:** cultured fibroblast catalase/PTS1 immunofluorescence, matrix-protein import, VLCFA β-oxidation, plasmalogen synthesis, and complementation studies.

Mild disease can have near-normal plasma VLCFAs; normal screening therefore does not exclude PBD1B. The 2023 dicarboxylic-acylcarnitine study suggests C20-DC/C22-DC as accessible orthogonal markers after an elevated newborn-screen C26:0-lysoPC result, but confirmatory molecular/biochemical testing remains mandatory. (wangler2023dicarboxylicacylcarnitinebiomarkers pages 1-2, wangler2023dicarboxylicacylcarnitinebiomarkers pages 8-9)

**Imaging/functional tests:** brain MRI for leukodystrophy/migration abnormalities; liver ultrasound and elastography; ophthalmic examination, OCT, fundus autofluorescence, visual fields and electroretinography; audiometry/ABR; nerve-conduction studies when neuropathy is suspected; DXA for bone health. The 2024 study shows multimodal retinal imaging can reveal disease even when acuity changes slowly. (karuntu2024systematicstudyof pages 5-6)

**Differential diagnosis:** Usher syndrome; Heimler syndrome/PEX6-related disease; other PEX-gene ZSD; D-bifunctional protein deficiency; acyl-CoA oxidase deficiency; X-linked adrenoleukodystrophy; adult Refsum disease; mitochondrial/hepatocerebral disease; congenital infection; other leukodystrophies, retinal dystrophies, and hereditary deafness.

CMA, karyotype, FISH, mitochondrial-DNA testing, and repeat-expansion testing are not routine PBD1B tests unless the phenotype suggests an alternative diagnosis.

### Screening

C26:0-lysoPC is detectable in dried blood spots and is already used in newborn screening for X-linked adrenoleukodystrophy; it can incidentally identify ZSD. Population-wide PBD1B screening is not universally established. Cascade testing of relatives and reproductive carrier testing are appropriate after familial variants are known.

## 11. Outcome and prognosis

Non-classic PEX1-ZSD is compatible with survival into adolescence and adulthood; exact five- and ten-year survival rates for PBD1B are unavailable. Major morbidity includes hearing and visual disability, neuropathy/ataxia, developmental limitation, chronic liver disease, adrenal insufficiency, osteopenia/fractures, renal complications, and nutritional/growth impairment. Historical spectrum descriptions contrast death before one year in classic Zellweger syndrome with survival into adolescence for NALD and adulthood for IRD. (chang2022geneticsbehindcerebral pages 26-27)

Prognosis is generally better with residual-function missense alleles such as p.Gly843Asp than with two null alleles. Adverse factors include early severe neurologic disease, progressive leukodystrophy, advanced fibrosis/cirrhosis, coagulopathy, adrenal crisis, and compound heterozygosity with a null allele. The 2024 cohort also demonstrates that identical genotypes do not guarantee identical visual outcomes. (karuntu2024systematicstudyof pages 12-13)

The Pex1-G844D mouse progressed from hepatomegaly to cell death, steatosis, inflammation, fibrosis, and tumors/HCC-like disease over 1–18 months, supporting long-term liver and malignancy vigilance; direct human cancer-risk quantification remains unavailable. (chen2025longitudinalstudyof pages 31-38, chen2025longitudinalstudyof pages 6-10)

## 12. Treatment and applications

There is **no established curative or approved genotype-correcting treatment**. Current implementation is multidisciplinary surveillance and symptom-directed care.

- **Nutrition/feeding:** dietitian-guided caloric support, feeding therapy, and enteral feeding when needed; avoid prolonged fasting. MAXO suggestions: nutritional assessment, dietary therapy, gastrostomy.
- **Hearing:** hearing aids, FM systems, speech/language therapy, and cochlear-implant assessment. MAXO: audiologic assessment, hearing-aid fitting, cochlear implantation.
- **Vision:** refraction, low-vision aids, orientation/mobility training, management of retinal cavities where clinically appropriate. In the 2024 cohort two patients received acetazolamide, but efficacy was not established. (karuntu2024systematicstudyof pages 5-6)
- **Neurology/rehabilitation:** standard antiseizure medication, physical/occupational/speech therapy, orthoses, mobility aids, and neuropathic-pain management.
- **Liver/coagulation:** serial enzymes, bilirubin, INR, ultrasound/elastography; vitamin K and fat-soluble vitamin replacement when deficient; avoid hepatotoxic drugs. Liver transplantation is individualized and does not correct extrahepatic disease.
- **Adrenal:** periodic ACTH/cortisol evaluation; physiologic hydrocortisone and stress dosing when insufficiency is confirmed.
- **Bone/renal:** calcium/vitamin-D optimization, DXA and fracture care; monitor renal function, stones, and oxalate.

### Cholic acid

In a 21-month extension, cholic acid suppressed bile-acid synthesis and reduced plasma/urine DHCA and THCA but produced **no clinically relevant improvement** in liver tests, elastography, coagulation, fat-soluble vitamins, or weight. Four patients with baseline cirrhosis developed concerning transaminase/bilirubin increases requiring reduction or withdrawal. Across 22 analyzed patients, including six with advanced liver disease, the authors considered evidence inadequate for routine use and advised strongly against treatment in advanced liver disease. (klouwer2018thecholicacid pages 1-2, klouwer2018thecholicacid pages 8-9)

### Pexophagy/autophagy approaches

Hydroxychloroquine, chloroquine, and 3-methyladenine failed to restore function in four PEX1-G843D cell types, including primary patient cells, and worsened import/metabolic measures; ATG5/NBR1 knockdown gave only minimal benefit. The authors concluded that autophagy inhibitors should not be used for this purpose, whereas L-arginine remained preclinically promising. This is primarily **in-vitro evidence**, not proof of L-arginine clinical efficacy. (klouwer2021autophagyinhibitorsdo pages 1-2)

### Trials and research implementation

- **NCT01668186:** recruiting longitudinal natural-history study; planned enrollment 244.
- **NCT06190626:** recruiting prospective retinopathy natural-history study; planned enrollment 30.
- **NCT03440905:** completed proxy-reported symptoms/QoL survey; enrollment 92.
- **NCT01838941:** completed phase 3 betaine study; enrollment 12; retrieved evidence did not establish clinical efficacy.
- **NCT03856866:** completed phase 2 hydroxychloroquine/pexophagy study; enrollment 3; tiny enrollment plus adverse in-vitro evidence precludes routine use.

Recent experimental directions include pharmacologic rescue of residual PEX1 folding/function, pexophagy modulation, and gene correction. A 2025 mouse preprint refined liver mechanisms, while a post-2024 base-editing report described correction of PEX1-G843D in mouse liver and patient fibroblasts; neither constitutes available clinical therapy.

| domain | key finding/statistic | evidence type | source/year |
|---|---|---|---|
| Ophthalmology / natural history | Mild PEX1-mediated ZSD cohort: n=10 from 6 families; 9/10 homozygous PEX1 c.2528G>A (p.Gly843Asp); median age 22.6 y; symptom onset median 6 months; RP-like phenotype with stable BCVA over 10.8 y; SD-OCT abnormalities in all evaluated patients (karuntu2024systematicstudyof pages 5-6, karuntu2024systematicstudyof pages 12-13) | Human clinical, cross-sectional with longitudinal visual follow-up | Karuntu et al., 2024 |
| Biomarkers / screening | LC-MS/MS study of n=598 samples including 19 PBD patients with PEX1/PEX6 deficiency found elevated dicarboxylic acylcarnitines; C20-DC elevated in 100% and C22-DC in 68% of PBD patients; proposed as orthogonal follow-up to elevated C26:0-lysoPC, not standalone diagnostic markers (wangler2023dicarboxylicacylcarnitinebiomarkers pages 1-2, wangler2023dicarboxylicacylcarnitinebiomarkers pages 8-9) | Human biochemical diagnostics | Wangler et al., 2023 |
| Therapy / bile acids | Cholic acid extension: 17 patients continued in extension; 22 total analyzed. CA suppressed toxic C27 bile acid intermediates (DHCA/THCA), but no clinically relevant improvement in liver tests, elastography, coagulation, fat-soluble vitamins, or weight after 21 months; advanced liver disease subgroup had worsening bilirubin/transaminases and CA could be harmful (klouwer2018thecholicacid pages 1-2, klouwer2018thecholicacid pages 8-9) | Human interventional extension study | Klouwer et al., 2018 |
| Therapy / pexophagy modulation | In four PEX1-G843D cell types including primary patient fibroblasts, chloroquine, hydroxychloroquine, and 3-methyladenine did not restore peroxisomal function and instead worsened matrix-protein import/metabolic readouts; ATG5/NBR1 knockdown gave only minimal improvement; L-arginine remained more promising (klouwer2021autophagyinhibitorsdo pages 1-2) | In vitro patient-cell mechanistic/therapeutic study | Klouwer et al., 2021 |
| Mechanism / liver disease model | Pex1-G844D mouse model of mild ZSD shows progressive hepatopathy from hepatomegaly to inflammation, fibrosis, tumors/HCC-like changes; severe import defect with catalase mislocalization; secondary mitochondrial dysfunction; elevated VLCFA, pristanic/phytanic acids, C27 bile acid intermediates, C26:0-lysoPC; decreased plasmalogens and dysregulated hepatic lipid homeostasis (chen2025longitudinalstudyof pages 31-38, chen2025longitudinalstudyof pages 19-21, chen2025longitudinalstudyof pages 24-27, chen2025longitudinalstudyof pages 6-10) | Model organism, longitudinal mechanistic study | Chen et al., 2025 preprint |


*Table: This compact table summarizes key clinical, biomarker, treatment, and mechanistic evidence for PEX1-related non-classic Zellweger spectrum disorder. It highlights the most decision-relevant findings from recent human cohorts, therapeutic studies, and the Pex1-G844D mouse model.*

## 13. Prevention

**Primary prevention of manifestations is not currently possible after conception.** Primary genetic prevention options for at-risk families include carrier testing, genetic counseling, preimplantation genetic testing, chorionic-villus sampling, or amniocentesis after familial variants are known.

**Secondary prevention:** cascade testing; incidental newborn detection using C26:0-lysoPC; early molecular confirmation; early hearing/vision, liver, adrenal, nutrition, and developmental assessment. Early recognition prevents diagnostic delay and inappropriate classification as Usher syndrome. (karuntu2024systematicstudyof pages 5-6, karuntu2024systematicstudyof pages 12-13)

**Tertiary prevention:** vaccination according to routine schedules, prompt infection care, adrenal stress dosing where indicated, avoidance of fasting and hepatotoxic agents, fall/fracture prevention, visual and hearing habilitation, nutrition support, and surveillance for liver, renal, neurologic, and bone complications. Vaccination prevents intercurrent infection complications but does not prevent PBD1B itself.

## 14. Other species and natural disease

- **Human:** *Homo sapiens*, NCBI Taxon **9606**; PEX1 is the causal ortholog.
- **Mouse:** *Mus musculus*, Taxon **10090**; ortholog **Pex1**. Engineered p.Gly844Asp models reproduce the human p.Gly843Asp residue shift.
- **Zebrafish:** *Danio rerio*, Taxon **7955**; pex-gene models are used for developmental biology and drug screening.
- **Drosophila/yeast:** conserved peroxin machinery is useful for mechanistic genetics, although organ systems and lipid metabolism differ from humans.

No well-established, naturally occurring companion-animal PEX1-PBD1B syndrome or breed association was identified in the retrieved evidence. There is no transmission or zoonotic potential.

## 15. Model organisms and experimental systems

### Pex1-G844D mouse

This knock-in is the principal mammalian model of residual-function PEX1-ZSD. It reproduces abnormal peroxisomal import, elevated VLCFA/branched-chain fatty acids/C27 bile-acid intermediates, low plasmalogens, growth restriction, retinal disease, and chronic hepatopathy. Recent longitudinal work found hepatomegaly at one month, cell injury by approximately four to six months, inflammation around eight months, and fibrosis/tumors at 12–18 months. It also demonstrated cytosolic catalase, scarce/enlarged peroxisomes, secondary mitochondrial dysfunction, hypoglycemia/hypoinsulinemia, and hepatic/systemic lipid dyshomeostasis. (chen2025longitudinalstudyof pages 31-38, chen2025longitudinalstudyof pages 38-43, chen2025longitudinalstudyof pages 19-21, chen2025longitudinalstudyof pages 6-10)

**Applications:** natural history, retinal and hepatic pathogenesis, lipidomics/transcriptomics, biomarker validation, cholic-acid studies, and gene/pharmacologic rescue. **Limitations:** murine lifespan and liver tumor susceptibility, species-specific bile-acid/lipid metabolism, and inability to capture human cognition, communication, or QoL.

### Patient-derived cells

Primary fibroblasts carrying p.Gly843Asp permit catalase/PTS1-import imaging, peroxisomal β-oxidation, plasmalogen synthesis, pexophagy, folding rescue, and variant-functional assays. Four-cell-type testing showed that autophagy inhibitors worsened rather than rescued peroxisomal function. (klouwer2021autophagyinhibitorsdo pages 1-2)

### Other models

Zebrafish provide vertebrate developmental imaging and scalable drug screening; Drosophila permits tissue-specific peroxisomal-import and inter-organ signaling studies; yeast provides high-resolution analysis of conserved PEX1–PEX6 ATPase/import machinery. None individually reproduces the complete human sensory-neurologic-hepatic course.

## Key recent developments and authoritative interpretation

1. **2024 human phenotyping:** systematic multimodal imaging established a distinctive RP-like retinopathy with retinal cavities and hyperautofluorescent abnormalities in mild p.Gly843Asp-associated disease. The authors’ abstract conclusion was: **“This study highlights the ophthalmological phenotype resembling RP with moderate to severe visual impairment in patients with mild ZSD.”** (Published April 2024; DOI: https://doi.org/10.1080/13816810.2024.2330389.) (karuntu2024systematicstudyof pages 5-6, karuntu2024systematicstudyof pages 12-13)
2. **2023 biomarkers:** C20-DC and C22-DC dicarboxylic acylcarnitines emerged as practical second-tier candidates, with 100% and 68% detection among 19 PBD patients, respectively, but require confirmation. (Published November 2023; DOI: https://doi.org/10.1016/j.ymgme.2023.107680.) (wangler2023dicarboxylicacylcarnitinebiomarkers pages 1-2, wangler2023dicarboxylicacylcarnitinebiomarkers pages 8-9)
3. **2024 cell biology:** elevated pexophagy can competitively limit other selective-autophagy pathways through ULK1 consumption, broadening pathophysiology beyond passive loss of peroxisomal metabolism. Clinical actionability remains unproven.
4. **Therapeutic caution:** cholic acid improves toxic bile-acid biomarkers without demonstrated clinical benefit and can harm patients with advanced liver disease; hydroxychloroquine/autophagy inhibition is unsupported and may worsen peroxisomal function. (klouwer2021autophagyinhibitorsdo pages 1-2, klouwer2018thecholicacid pages 1-2, klouwer2018thecholicacid pages 8-9)

## Knowledge-base conclusions

PBD1B should be represented as an autosomal-recessive, residual-function **PEX1-related ZSD** with continuous and highly variable expression. The central causal chain is **PEX1–PEX6 ATPase dysfunction → defective PEX5 recycling and matrix import → global peroxisomal lipid/bile-acid/redox failure → sensory, neurologic, hepatic, adrenal, skeletal, and renal injury**. The highest-value current applications are biochemical-plus-genetic diagnosis, early sensory habilitation, multidisciplinary complication surveillance, and enrollment in natural-history studies. No curative treatment, validated protective factor, PBD1B-specific population incidence, disease-specific survival curve, established modifier gene, epigenetic signature, or clinically validated single-cell/spatial profile is presently available.

References

1. (chang2022geneticsbehindcerebral pages 26-27): Kao-Jung Chang, Hsin-Yu Wu, Aliaksandr Yarmishyn, Cheng-Yi Li, Yu-Jer Hsiao, Yi-Chun Chi, Tzu-Chen Lo, He-Jhen Dai, Yi-Chiang Yang, Ding-Hao Liu, De-Kuang Hwang, Shih-Jen Chen, Chih-Chien Hsu, and Chung-Lan Kao. Genetics behind cerebral disease with ocular comorbidity: finding parallels between the brain and eye molecular pathology. International Journal of Molecular Sciences, 23:9707, Aug 2022. URL: https://doi.org/10.3390/ijms23179707, doi:10.3390/ijms23179707. This article has 11 citations.

2. (OpenTargets Search: Zellweger spectrum disorder-PEX1): Open Targets Query (Zellweger spectrum disorder-PEX1, 47 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (karuntu2024systematicstudyof pages 5-6): Jessica S. Karuntu, Femke C. C. Klouwer, Marc Engelen, and Camiel J. F. Boon. Systematic study of ophthalmological findings in 10 patients with pex1-mediated zellweger spectrum disorder. Ophthalmic Genetics, 45:351-362, Apr 2024. URL: https://doi.org/10.1080/13816810.2024.2330389, doi:10.1080/13816810.2024.2330389. This article has 7 citations and is from a peer-reviewed journal.

4. (karuntu2024systematicstudyof pages 12-13): Jessica S. Karuntu, Femke C. C. Klouwer, Marc Engelen, and Camiel J. F. Boon. Systematic study of ophthalmological findings in 10 patients with pex1-mediated zellweger spectrum disorder. Ophthalmic Genetics, 45:351-362, Apr 2024. URL: https://doi.org/10.1080/13816810.2024.2330389, doi:10.1080/13816810.2024.2330389. This article has 7 citations and is from a peer-reviewed journal.

5. (klouwer2018thecholicacid pages 1-2): Femke C. C. Klouwer, Bart G. P. Koot, Kevin Berendse, Elles M. Kemper, Sacha Ferdinandusse, Kiran V. K. Koelfat, Martin Lenicek, Frédéric M. Vaz, Marc Engelen, Peter L. M. Jansen, Ronald J. A. Wanders, Hans R. Waterham, Frank G. Schaap, and Bwee Tien Poll-The. The cholic acid extension study in zellweger spectrum disorders: results and implications for therapy. Journal of Inherited Metabolic Disease, pages 1-10, May 2018. URL: https://doi.org/10.1007/s10545-018-0194-z, doi:10.1007/s10545-018-0194-z. This article has 36 citations and is from a peer-reviewed journal.

6. (wangler2023dicarboxylicacylcarnitinebiomarkers pages 1-2): Michael F. Wangler, Barbara Lesko, Rejwi Dahal, Sharayu Jangam, Pradnya Bhadane, Theodore E. Wilson, Molly McPheron, and Marcus J. Miller. Dicarboxylic acylcarnitine biomarkers in peroxisome biogenesis disorders. Molecular Genetics and Metabolism, 140:107680, Nov 2023. URL: https://doi.org/10.1016/j.ymgme.2023.107680, doi:10.1016/j.ymgme.2023.107680. This article has 8 citations and is from a peer-reviewed journal.

7. (wangler2023dicarboxylicacylcarnitinebiomarkers pages 8-9): Michael F. Wangler, Barbara Lesko, Rejwi Dahal, Sharayu Jangam, Pradnya Bhadane, Theodore E. Wilson, Molly McPheron, and Marcus J. Miller. Dicarboxylic acylcarnitine biomarkers in peroxisome biogenesis disorders. Molecular Genetics and Metabolism, 140:107680, Nov 2023. URL: https://doi.org/10.1016/j.ymgme.2023.107680, doi:10.1016/j.ymgme.2023.107680. This article has 8 citations and is from a peer-reviewed journal.

8. (chen2025longitudinalstudyof pages 19-21): Lingxiao Chen, Hong Choi, Catherine Argyriou, Monica Hsieh, Erminia Di Pietro, Wei Cui, Esther Nuebel, Caroline Daneaul, Matthieu Ruiz, Daniel Carpentier, Joseph G Hacia, Van-Hung Nguyen, Zu-Hua Gao, and Nancy Braverman. Longitudinal study of liver disease progression in the pex1-gly844asp mouse model of mild zellweger spectrum disorder. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.08.652960, doi:10.1101/2025.05.08.652960. This article has 0 citations.

9. (chen2025longitudinalstudyof pages 38-43): Lingxiao Chen, Hong Choi, Catherine Argyriou, Monica Hsieh, Erminia Di Pietro, Wei Cui, Esther Nuebel, Caroline Daneaul, Matthieu Ruiz, Daniel Carpentier, Joseph G Hacia, Van-Hung Nguyen, Zu-Hua Gao, and Nancy Braverman. Longitudinal study of liver disease progression in the pex1-gly844asp mouse model of mild zellweger spectrum disorder. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.08.652960, doi:10.1101/2025.05.08.652960. This article has 0 citations.

10. (chen2025longitudinalstudyof pages 6-10): Lingxiao Chen, Hong Choi, Catherine Argyriou, Monica Hsieh, Erminia Di Pietro, Wei Cui, Esther Nuebel, Caroline Daneaul, Matthieu Ruiz, Daniel Carpentier, Joseph G Hacia, Van-Hung Nguyen, Zu-Hua Gao, and Nancy Braverman. Longitudinal study of liver disease progression in the pex1-gly844asp mouse model of mild zellweger spectrum disorder. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.08.652960, doi:10.1101/2025.05.08.652960. This article has 0 citations.

11. (chen2025longitudinalstudyof pages 31-38): Lingxiao Chen, Hong Choi, Catherine Argyriou, Monica Hsieh, Erminia Di Pietro, Wei Cui, Esther Nuebel, Caroline Daneaul, Matthieu Ruiz, Daniel Carpentier, Joseph G Hacia, Van-Hung Nguyen, Zu-Hua Gao, and Nancy Braverman. Longitudinal study of liver disease progression in the pex1-gly844asp mouse model of mild zellweger spectrum disorder. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.08.652960, doi:10.1101/2025.05.08.652960. This article has 0 citations.

12. (klouwer2018thecholicacid pages 8-9): Femke C. C. Klouwer, Bart G. P. Koot, Kevin Berendse, Elles M. Kemper, Sacha Ferdinandusse, Kiran V. K. Koelfat, Martin Lenicek, Frédéric M. Vaz, Marc Engelen, Peter L. M. Jansen, Ronald J. A. Wanders, Hans R. Waterham, Frank G. Schaap, and Bwee Tien Poll-The. The cholic acid extension study in zellweger spectrum disorders: results and implications for therapy. Journal of Inherited Metabolic Disease, pages 1-10, May 2018. URL: https://doi.org/10.1007/s10545-018-0194-z, doi:10.1007/s10545-018-0194-z. This article has 36 citations and is from a peer-reviewed journal.

13. (klouwer2021autophagyinhibitorsdo pages 1-2): Femke C. C. Klouwer, Kim D. Falkenberg, Rob Ofman, Janet Koster, Démi van Gent, Sacha Ferdinandusse, Ronald J. A. Wanders, and Hans R. Waterham. Autophagy inhibitors do not restore peroxisomal functions in cells with the most common peroxisome biogenesis defect. Frontiers in Cell and Developmental Biology, Apr 2021. URL: https://doi.org/10.3389/fcell.2021.661298, doi:10.3389/fcell.2021.661298. This article has 23 citations.

14. (chen2025longitudinalstudyof pages 24-27): Lingxiao Chen, Hong Choi, Catherine Argyriou, Monica Hsieh, Erminia Di Pietro, Wei Cui, Esther Nuebel, Caroline Daneaul, Matthieu Ruiz, Daniel Carpentier, Joseph G Hacia, Van-Hung Nguyen, Zu-Hua Gao, and Nancy Braverman. Longitudinal study of liver disease progression in the pex1-gly844asp mouse model of mild zellweger spectrum disorder. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.08.652960, doi:10.1101/2025.05.08.652960. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Peroxisome_Biogenesis_Disorder_1B-deep-research-falcon_artifacts/artifact-00.md)