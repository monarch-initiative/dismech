---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T13:28:51.734367'
end_time: '2026-05-06T13:49:08.544779'
duration_seconds: 1216.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pulmonary Veno-Occlusive Disease and/or Pulmonary Capillary Haemangiomatosis
  mondo_id: ''
  category: Cardiovascular Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pulmonary Veno-Occlusive Disease and/or Pulmonary Capillary Haemangiomatosis
- **MONDO ID:**  (if available)
- **Category:** Cardiovascular Disorder

## Research Objectives

Please provide a comprehensive research report on **Pulmonary Veno-Occlusive Disease and/or Pulmonary Capillary Haemangiomatosis** covering all of the
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
- **Disease Name:** Pulmonary Veno-Occlusive Disease and/or Pulmonary Capillary Haemangiomatosis
- **MONDO ID:**  (if available)
- **Category:** Cardiovascular Disorder

## Research Objectives

Please provide a comprehensive research report on **Pulmonary Veno-Occlusive Disease and/or Pulmonary Capillary Haemangiomatosis** covering all of the
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


# Comprehensive Disease Characteristics Report: Pulmonary Veno-Occlusive Disease (PVOD) and Pulmonary Capillary Haemangiomatosis (PCH)

**Target disease:** Pulmonary veno-occlusive disease and/or pulmonary capillary haemangiomatosis (PVOD/PCH)
**Category:** Cardiovascular disorder → pulmonary vascular disease (pulmonary hypertension)
**Evidence note:** The retrieved corpus contains strong peer‑reviewed clinical reviews and primary mechanistic/genetic studies, but it did **not** include OMIM/Orphanet/ICD/MeSH/MONDO identifier pages; therefore, identifier fields are flagged as **not available from current retrieved sources**.

| Domain | Key facts (concise) | Quantitative data | Evidence/source (author year + URL) | Citation id(s) |
|---|---|---|---|---|
| Identifiers / classification / synonyms | PVOD and PCH are now generally treated as a spectrum of **PAH with overt venous/capillary involvement**; reviews note they are often clinically indistinguishable and commonly grouped as **PVOD/PCH**. PVOD is a rare cause of precapillary pulmonary hypertension with fibrotic obstruction of small pulmonary veins/venules; PCH reflects prominent capillary congestion/proliferation. | Classified within Group 1 PAH; recent reviews describe subgroup **1.5** / “PAH with features of venous/capillary involvement.” | Lechartier et al. 2024, European Respiratory Review. https://doi.org/10.1183/16000617.0156-2023; Deshwal et al. 2025, Breathe. https://doi.org/10.1183/20734735.0098-2024 | (lechartier2024pulmonaryvenoocclusivedisease pages 1-2, deshwal2025pulmonaryvenoocclusivedisease pages 1-2, deshwal2025pulmonaryvenoocclusivedisease pages 2-3) |
| Epidemiology | PVOD/PCH is ultra-rare and likely under-recognized; cases are often initially labeled as PAH. Affected patients can present from childhood to late adulthood, but heritable cases tend to be younger. | Incidence **0.1–0.5 per million/year**; prevalence **1–2 per million** (or **1–2 per 10 million** in one 2024 case report). Some reviews estimate **5–25%** of patients labeled PAH may have PVOD features. | Lechartier et al. 2024. https://doi.org/10.1183/16000617.0156-2023; Deshwal et al. 2025. https://doi.org/10.1183/20734735.0098-2024; Stener & Tsareva 2024. https://doi.org/10.18093/0869-0189-2024-34-4-595-598 | (lechartier2024pulmonaryvenoocclusivedisease pages 1-2, deshwal2025pulmonaryvenoocclusivedisease pages 1-2) |
| Prognosis | Natural history is poor, with rapid progression to right-heart failure and frequent need for lung transplantation. Outcomes are generally worse than idiopathic PAH. | **1-year mortality ~72%**; mean time from diagnosis to death or transplant **11.8 months**; mean time from first symptoms to death/transplant **24.4 months**; median survival often cited as **2–3 years** after diagnosis. | Lechartier et al. 2024. https://doi.org/10.1183/16000617.0156-2023; Prabhakar et al. 2024. https://doi.org/10.1172/jci.insight.181877 | (lechartier2024pulmonaryvenoocclusivedisease pages 3-5, prabhakar2024mechanismsunderlyingageassociated pages 1-2) |
| Diagnostic clues: CT / physiology / hemodynamics | Noninvasive diagnosis relies on a characteristic **HRCT triad** plus severe gas-exchange impairment and precapillary PH. Typical clues are **centrilobular ground-glass opacities**, **smooth interlobular septal thickening**, and **mediastinal lymphadenopathy**; many patients also have marked hypoxemia and very low DLCO. | Suggested confirmatory pattern in one review: at least **2 HRCT features**, **PaO2 <70 mmHg**, **DLCO <55% predicted**. RHC shows precapillary PH: **mPAP >20 mmHg**, **PAWP/PCWP ≤15 mmHg**, **PVR >2 WU**. Markedly reduced DLCO often **<40%** in some series. | Lechartier et al. 2024. https://doi.org/10.1183/16000617.0156-2023; Deshwal et al. 2025. https://doi.org/10.1183/20734735.0098-2024; Foster et al. 2025. https://doi.org/10.3390/arm93060048 | (lechartier2024pulmonaryvenoocclusivedisease pages 2-3, lechartier2024pulmonaryvenoocclusivedisease pages 3-5, deshwal2025pulmonaryvenoocclusivedisease pages 8-9, deshwal2025pulmonaryvenoocclusivedisease pages 7-8, foster2025pulmonaryvenoocclusivedisease pages 4-6) |
| Diagnostic workflow / procedures to avoid | Lung biopsy is the histologic gold standard but is generally **not recommended** in routine suspected PVOD/PCH because of bleeding/perioperative risk in pulmonary hypertension. Diagnosis is instead based on clinical-radiologic-genetic synthesis. Development of pulmonary edema after vasodilator exposure is a major diagnostic red flag. | 2022 ESC/ERS recommendation table states diagnosis should rely on **clinical + radiological findings** and that **lung biopsy is not recommended**. | Lechartier et al. 2024. https://doi.org/10.1183/16000617.0156-2023 | (lechartier2024pulmonaryvenoocclusivedisease pages 5-6, lechartier2024pulmonaryvenoocclusivedisease media a49a6475) |
| Causal gene / inheritance | **EIF2AK4 (GCN2)** is the established causal gene for heritable PVOD/PCH. Disease is caused by **biallelic** pathogenic variants, typically autosomal recessive / compound heterozygous or homozygous. Detection of biallelic pathogenic EIF2AK4 variants can establish diagnosis without histology. | Biallelic EIF2AK4 variants reported in **all 13 familial** PVOD cases and **5/20 (25%)** sporadic cases in foundational series; another review cites **9% (7/81)** in suspected sporadic cases. EIF2AK4 carriers present younger: median **26 vs 60 years**. | Park et al. 2023. https://doi.org/10.1159/000527524; Emanuelli et al. 2024. https://doi.org/10.17863/cam.108223; Lechartier et al. 2024. https://doi.org/10.1183/16000617.0156-2023 | (park2023differentialdiagnosisof pages 2-3, park2023differentialdiagnosisof pages 1-2, emanuelli2024functionalvalidationof pages 3-5, lechartier2024pulmonaryvenoocclusivedisease pages 2-3, lechartier2024pulmonaryvenoocclusivedisease pages 1-2) |
| Variant examples / molecular data | Reported pathogenic EIF2AK4 examples include truncating, splice, missense, and frameshift alleles. Park 2023 identified two novel compound-heterozygous variants; Emanuelli 2024 functionally classified multiple missense variants and showed not all rare missense alleles are pathogenic. | Park 2023: **NM_001013703.3:c.2137_2138dup (p.Ser714Leufs*78)** and **c.3358-1G>A**, both absent from **gnomAD**. Emanuelli 2024: pathogenic/likely pathogenic examples include **p.R585Q, p.G599R, p.V607G, p.L643R, p.S909R, p.G1109R, p.P1115L, p.H1202L, p.L1295R**; common polymorphisms include **p.I441L, p.E556G, p.G1306C**. | Park et al. 2023. https://doi.org/10.1159/000527524; Emanuelli et al. 2024. https://doi.org/10.17863/cam.108223 | (park2023differentialdiagnosisof pages 2-3, park2023differentialdiagnosisof pages 1-2, emanuelli2024functionalvalidationof pages 1-3, emanuelli2024functionalvalidationof pages 3-5) |
| Environmental / occupational risk factors | Strongest reported non-genetic associations are **organic solvents** (especially **trichloroethylene**) and **chemotherapy**, particularly alkylating agents such as **mitomycin C**, cyclophosphamide, and cisplatin. Tobacco may be additive with solvent exposure. | Organic solvents: adjusted OR **12.8**; trichloroethylene exposure in **42% of PVOD vs 3% of PAH**, adjusted OR **8.2**. Chemotherapy-associated PVOD in anal-cancer cohort estimated at **3.9/1000 patient-years** vs idiopathic PVOD **0.5/million/year**. | Lechartier et al. 2024. https://doi.org/10.1183/16000617.0156-2023; Deshwal et al. 2025. https://doi.org/10.1183/20734735.0098-2024 | (lechartier2024pulmonaryvenoocclusivedisease pages 2-3, deshwal2025pulmonaryvenoocclusivedisease pages 2-3) |
| Mechanistic highlights | Pathobiology centers on venular/capillary remodeling with endothelial injury and stress-response dysfunction. Recent work implicates **EIF2AK4/GCN2**, **PKR**, and the **integrated stress response (ISR)**, with endothelial barrier failure (VE-cadherin/Rad51 disruption), inflammation, and age-related amplification. | Aging increased endothelial ISR markers in rat lungs: p-PKR **2.7-fold**, total PKR **1.6-fold**, p-eIF2α **1.8-fold**, ATF4 **2.3-fold**. In MMC model, RVSP rose from **25.0→34.1 mmHg** (young) and **24.4→34.6 mmHg** (aged); RV/LV+S from **0.21→0.31** and **0.21→0.34**. | Prabhakar et al. 2024. https://doi.org/10.1172/jci.insight.181877; Bignard et al. 2023. https://doi.org/10.1152/ajplung.00460.2021 | (prabhakar2024mechanismsunderlyingageassociated pages 1-2, prabhakar2024mechanismsunderlyingageassociated pages 2-4, bignard2023tcelldysregulationand pages 1-5, bignard2023tcelldysregulationand pages 16-19) |
| Management recommendations | Management emphasizes **early referral to PH/transplant expert centers**, oxygen and diuretics, cautious rehabilitation/immunization, and genetic counseling/testing. **Bilateral lung transplantation** is the only established curative therapy. Routine anticoagulation is generally not recommended unless another indication exists. | Post-transplant survival reported as similar to PAH in review summaries; one study cited higher pre-transplant mortality in PVOD (**22.6% vs 11% at 6 months**). | Lechartier et al. 2024. https://doi.org/10.1183/16000617.0156-2023; Deshwal et al. 2025. https://doi.org/10.1183/20734735.0098-2024; Foster et al. 2025. https://doi.org/10.3390/arm93060048 | (lechartier2024pulmonaryvenoocclusivedisease pages 3-5, deshwal2025pulmonaryvenoocclusivedisease pages 8-9, deshwal2025pulmonaryvenoocclusivedisease pages 9-10, foster2025pulmonaryvenoocclusivedisease pages 10-12, lechartier2024pulmonaryvenoocclusivedisease pages 1-2) |
| PAH-targeted therapy and pulmonary edema risk | PAH drugs may occasionally be used cautiously as a **bridge to transplant**, but evidence is limited and pulmonary edema risk is the central limitation. Reviews emphasize careful monitoring of symptoms and gas exchange if vasodilators are tried. | Large cohort/review estimates: drug-induced pulmonary edema in **>20%** of treated patients; systematic review found edema in about **30/64** patients; older series reported edema in **20–50%** with PAH therapy and about **70%** with CCBs. One epoprostenol bridge series had **1/12** mild edema, with **9/12** transplanted. | Lechartier et al. 2024. https://doi.org/10.1183/16000617.0156-2023; Deshwal et al. 2025. https://doi.org/10.1183/20734735.0098-2024 | (lechartier2024pulmonaryvenoocclusivedisease pages 3-5, deshwal2025pulmonaryvenoocclusivedisease pages 9-10, lechartier2024pulmonaryvenoocclusivedisease pages 5-6) |
| Current real-world studies / implementation | Active real-world efforts include registries and targeted screening of **EIF2AK4 carriers**. These studies operationalize surveillance with CT, DLCO, echo, CPET, and genomics to define penetrance and natural history. | **NCT03902353** screens **20** heterozygous EIF2AK4 carriers; **NCT03169010** is a rare-PH registry with target enrollment **2000** including PVOD/PCH; **NCT01907295** UK cohort enrolls PAH/PVOD/PCH cases and relatives with deep phenotyping and sequencing. | ClinicalTrials.gov: NCT03902353; NCT03169010; NCT01907295 | (NCT03902353 chunk 1, NCT03169010 chunk 1, NCT01907295 chunk 1) |


*Table: This table condenses the highest-yield disease characteristics for PVOD/PCH from the gathered evidence, including classification, epidemiology, diagnostics, genetics, risk factors, mechanisms, and management. It is designed as a database-ready summary with quantitative findings and direct context citations.*

---

## 1. Disease Information

### 1.1 Concise overview
PVOD is an ultra‑rare pulmonary microvascular vasculopathy characterized by fibrotic obstruction/obliteration of small pulmonary veins and venules, producing **pre‑capillary pulmonary hypertension**, severe gas‑exchange impairment, and progressive right‑heart failure. PCH (pulmonary capillary haemangiomatosis) is characterized by prominent pulmonary capillary congestion/proliferation and is widely regarded as part of the same clinicopathologic spectrum as PVOD; the entities often coexist and are frequently grouped as **PVOD/PCH**. (lechartier2024pulmonaryvenoocclusivedisease pages 3-5, deshwal2025pulmonaryvenoocclusivedisease pages 2-3)

A recent authoritative ERS review explicitly frames PVOD as “pulmonary arterial hypertension (PAH) with overt features of venous/capillary involvement” and stresses that distinguishing PVOD from idiopathic PAH is critical because of **poor response and risk of life‑threatening pulmonary edema with PAH vasodilators**. (lechartier2024pulmonaryvenoocclusivedisease pages 1-2, lechartier2024pulmonaryvenoocclusivedisease pages 3-5)

**Direct abstract quotes (for definition/importance):**
- Lechartier et al. (Jan 2024) state PVOD is “a rare cause of PAH characterised by substantial small pulmonary vein and capillary involvement, leading to increased pulmonary vascular resistance and right ventricular failure.” (Published 2024‑01; https://doi.org/10.1183/16000617.0156-2023) (lechartier2024pulmonaryvenoocclusivedisease pages 1-2)
- Deshwal et al. (Jan 2025) describe PVOD as “a progressive and fatal spectrum of pulmonary vascular disorders” and note PVOD and PCH “can be clinically indistinguishable and often coexist… referred to together as PVOD/PCH.” (Published 2025‑01; https://doi.org/10.1183/20734735.0098-2024) (deshwal2025pulmonaryvenoocclusivedisease pages 1-2)

### 1.2 Key identifiers (availability)
Not available in the retrieved full‑text evidence for this run:
- **MONDO ID:** not retrieved
- **OMIM / Orphanet / ICD‑10 / ICD‑11 / MeSH IDs:** not retrieved

### 1.3 Common synonyms / alternative names (from literature)
- “PAH with features of venous/capillary involvement” (classification term used in ESC/ERS context) (lechartier2024pulmonaryvenoocclusivedisease pages 1-2, lechartier2024pulmonaryvenoocclusivedisease pages 5-6)
- “PVOD/PCH” (combined term used in multiple reviews) (deshwal2025pulmonaryvenoocclusivedisease pages 1-2, deshwal2025pulmonaryvenoocclusivedisease pages 2-3)

### 1.4 Evidence source type
- Aggregated disease‑level resources: ERS/European Respiratory Review and Breathe clinical reviews (lechartier2024pulmonaryvenoocclusivedisease pages 1-2, deshwal2025pulmonaryvenoocclusivedisease pages 1-2)
- Individual patient evidence: genetic case report with compound heterozygous EIF2AK4 variants (park2023differentialdiagnosisof pages 2-3)
- Experimental/model organism evidence: rat and mouse mechanistic models (mitomycin C; amino‑acid deprivation) including RNA‑seq/scRNA‑seq (bignard2023tcelldysregulationand pages 1-5, prabhakar2024mechanismsunderlyingageassociated pages 2-4)

---

## 2. Etiology

### 2.1 Disease causal factors
**Genetic (causal): EIF2AK4 (GCN2) biallelic pathogenic variants** cause heritable PVOD/PCH. (lechartier2024pulmonaryvenoocclusivedisease pages 2-3, emanuelli2024functionalvalidationof pages 3-5)

**Direct abstract quote (genetic causality):**
- Emanuelli et al. (Apr 2024) state: “Biallelic mutations of EIF2AK4… are causal in… pulmonary veno-occlusive disease and pulmonary capillary haemangiomatosis.” (Published 2024‑04; https://doi.org/10.17863/cam.108223) (emanuelli2024functionalvalidationof pages 1-3)

**Environmental/iatrogenic:** Epidemiologic associations include occupational exposure to organic solvents (notably trichloroethylene) and chemotherapy (notably **mitomycin C** and other alkylating agents). (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)

### 2.2 Risk factors (with quantitative data)
- **Occupational organic solvents / trichloroethylene:** Lechartier et al. report strong association; trichloroethylene exposure occurred in **42% of PVOD vs 3% of PAH** with adjusted OR **8.2**, and organic solvents overall had adjusted OR **12.8**. (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)
- **Chemotherapy (alkylating agents):** Mitomycin C (MMC), cyclophosphamide, cisplatin are repeatedly associated; MMC has experimental support for endothelial toxicity and PVOD induction in rats. (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)
- **Tobacco:** Tobacco co‑exposure is common and may be additive with solvent exposure, with permeability effects. (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
The 2024 ERS review links solvent exposure (trichloroethylene), tobacco, and chemotherapy to **endothelial permeability/barrier injury**, and separately identifies EIF2AK4 (GCN2) as a stress‑response kinase—supporting a convergent model in which genetically reduced stress‑response capacity and/or environmentally induced endothelial injury contribute to PVOD/PCH pathogenesis. (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with suggested HPO terms)
PVOD/PCH cannot be reliably distinguished from idiopathic PAH on symptoms or routine hemodynamics alone; diagnostic suspicion rests on gas‑exchange impairment and imaging patterns. (deshwal2025pulmonaryvenoocclusivedisease pages 1-2, lechartier2024pulmonaryvenoocclusivedisease pages 3-5)

**Symptoms/signs**
- Progressive exertional dyspnea → **Dyspnea (HP:0002094)** (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)
- Hypoxemia (often disproportionate) → **Hypoxemia (HP:0012418)**; severe resting hypoxemia highlighted as a red flag (foster2025pulmonaryvenoocclusivedisease pages 4-6)
- Right‑heart failure manifestations (peripheral edema, hepatomegaly, ascites) → **Peripheral edema (HP:0000969)**; **Hepatomegaly (HP:0002240)**; **Ascites (HP:0001541)** (foster2025pulmonaryvenoocclusivedisease pages 4-6)

**Pulmonary function / lab abnormalities**
- Markedly reduced diffusion capacity → **Decreased DLCO (HP:0045051)** (threshold examples below) (deshwal2025pulmonaryvenoocclusivedisease pages 8-9)

**Radiology/pathology manifestations**
- HRCT: centrilobular ground‑glass opacities → **Ground-glass opacity on pulmonary imaging (HP:0031969)**
- Smooth interlobular septal thickening → **Interlobular septal thickening (HP:0031944)**
- Mediastinal lymphadenopathy → **Mediastinal lymphadenopathy (HP:0030111)** (lechartier2024pulmonaryvenoocclusivedisease pages 3-5, deshwal2025pulmonaryvenoocclusivedisease pages 8-9)

### 3.2 Phenotype characteristics (age, severity, progression)
- Age of onset: heritable EIF2AK4‑associated cases present younger (median **26** vs **60** years in one series) (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)
- Course: rapid progression with poor prognosis; median survival often cited as **2–3 years after diagnosis** (prabhakar2024mechanismsunderlyingageassociated pages 1-2)

### 3.3 Frequencies / quantitative thresholds reported
- Suggested clinical criteria in one review include **PaO2 <70 mmHg** and **DLCO <55% predicted** along with ≥2 HRCT features. (deshwal2025pulmonaryvenoocclusivedisease pages 8-9)
- Another review notes DLCO often “below **40% predicted**” and mean ≈35% in studies. (foster2025pulmonaryvenoocclusivedisease pages 4-6)

### 3.4 Quality-of-life impact
No disease‑specific QoL instrument results (e.g., SF‑36/EQ‑5D) were identified in the retrieved evidence; functional limitation is implied by severe dyspnea, hypoxemia, and CPET impairment. (deshwal2025pulmonaryvenoocclusivedisease pages 7-8)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **EIF2AK4 (GCN2)**: biallelic pathogenic variants are causal for PVOD/PCH and can establish diagnosis without histology. (emanuelli2024functionalvalidationof pages 3-5, emanuelli2024functionalvalidationof pages 1-3)

### 4.2 Pathogenic variant examples (HGVS where available)
**Case‑level PVOD/PCH genetic diagnosis (whole‑exome sequencing):**
- Park et al. 2023 reported **compound heterozygous** EIF2AK4 variants: **NM_001013703.3:c.2137_2138dup (p.Ser714Leufs*78)** and **c.3358-1G>A**, both described as absent from gnomAD; parental segregation supported biallelic inheritance. (Published 2023‑02; https://doi.org/10.1159/000527524) (park2023differentialdiagnosisof pages 2-3)

**Variant spectrum and functional interpretation (2024):**
Emanuelli et al. 2024 list pathogenic/likely pathogenic EIF2AK4 missense examples (protein notation) including **p.R585Q, p.G599R, p.V607G, p.L643R, p.S909R, p.G1109R, p.P1115L, p.H1202L, p.L1295R** and also note that some alleles represent common polymorphisms (e.g., **I441L, E556G, G1306C**), highlighting the need for functional validation of VUS. (emanuelli2024functionalvalidationof pages 1-3)

**Direct quote (diagnostic impact of biallelic EIF2AK4):**
- Emanuelli et al. 2024: “Detection of biallelic pathogenic EIF2AK4 mutations establishes the diagnosis of PVOD or PCH without the need for histological confirmation.” (emanuelli2024functionalvalidationof pages 3-5)

### 4.3 Inheritance
Autosomal recessive/biallelic inheritance is supported by:
- Parent‑of‑origin segregation consistent with compound heterozygosity (Park 2023) (park2023differentialdiagnosisof pages 2-3)
- Statement that PVOD due to EIF2AK4 is a “recessive form of pulmonary hypertension” (park2023differentialdiagnosisof pages 4-4)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
Not identified in the retrieved evidence.

---

## 5. Environmental Information

### 5.1 Environmental factors
- Organic solvents, especially **trichloroethylene** (occupational exposure) (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)

### 5.2 Lifestyle factors
- Tobacco exposure is commonly reported and may act cumulatively with solvent exposure, potentially via permeability effects. (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)

### 5.3 Infectious agents
No specific infectious etiologies were identified in the retrieved evidence.

---

## 6. Mechanism / Pathophysiology (with causal chains and ontology suggestions)

### 6.1 Pathologic substrate (vascular remodeling)
PVOD is defined pathologically by diffuse fibrous thickening/obliteration of septal veins and pre‑septal venules, with characteristic involvement of small venules (<100 µm). PCH is part of the same spectrum with capillary congestion/proliferation. (lechartier2024pulmonaryvenoocclusivedisease pages 3-5)

**Causal chain (high‑level):**
Trigger(s) (biallelic EIF2AK4 loss and/or endothelial toxic exposures such as MMC/solvents) → endothelial stress response/barrier dysfunction → increased permeability, microvascular remodeling and venular obstruction → increased pulmonary vascular resistance → pre‑capillary PH → RV hypertrophy/failure and hypoxemia due to impaired gas exchange. (prabhakar2024mechanismsunderlyingageassociated pages 2-4, lechartier2024pulmonaryvenoocclusivedisease pages 2-3)

### 6.2 Integrated stress response (ISR) and PKR/PP1 axis (recent 2023–2024 developments)
A key 2024 mechanistic study reports that MMC induces PVOD‑like disease in rats via activation of **PKR** and the **integrated stress response (ISR)**, with sustained **eIF2α phosphorylation** due to reduced **protein phosphatase 1 (PP1)**, leading to endothelial junction disruption and barrier dysfunction. (prabhakar2024mechanismsunderlyingageassociated pages 1-2, prabhakar2024mechanismsunderlyingageassociated pages 2-4)

Quantitative findings in the MMC rat model include increased RV systolic pressure and RV hypertrophy after MMC, with greater severity in aged animals; pharmacologic PKR or ISR blockade mitigated PVOD phenotypes. (prabhakar2024mechanismsunderlyingageassociated pages 2-4)

**Direct abstract quote (2024):**
- Prabhakar et al. 2024: “We previously showed that… mitomycin C (MMC) in rats mediates PVOD through the activation of… protein kinase R (PKR) and the integrated stress response (ISR), resulting in the impairment of vascular endothelial junctional structure and barrier function.” (Published 2024‑09; https://doi.org/10.1172/jci.insight.181877) (prabhakar2024mechanismsunderlyingageassociated pages 1-2)

**GO term suggestions (processes):**
- Integrated stress response → **GO:0140749 (integrated stress response)** (conceptually aligned with eIF2α‑ATF4 pathway described) (prabhakar2024mechanismsunderlyingageassociated pages 1-2)
- Regulation of endothelial barrier / permeability → **GO:0035633 (maintenance of barrier function)** (conceptual) (prabhakar2024mechanismsunderlyingageassociated pages 1-2)
- Vascular remodeling/fibrosis → **GO:0001525 (angiogenesis)**; **GO:0045766 (positive regulation of angiogenesis)** (supported by angiogenesis mentions and remodeling) (bignard2023tcelldysregulationand pages 16-19)

**Cell Ontology (CL) suggestions (cell types implicated):**
- Pulmonary vascular endothelial cells → **Endothelial cell (CL:0000115)**, supported by CD31+ endothelial localization of ISR markers (prabhakar2024mechanismsunderlyingageassociated pages 2-4)
- T cells (LAG3+ and proliferative populations) → **T cell (CL:0000084)**; regulatory/exhausted‑like subsets conceptually consistent with LAG3+ population (bignard2023tcelldysregulationand pages 1-5)
- Neutrophils → **Neutrophil (CL:0000775)** (bignard2023tcelldysregulationand pages 1-5)
- Macrophages/mononuclear phagocytes involved in inflammation signals (supported by infiltration language) → **Macrophage (CL:0000235)** (bignard2023tcelldysregulationand pages 1-5)

### 6.3 Immune dysregulation in EIF2AK4/GCN2 deficiency (2023)
In a 2023 rat model, Gcn2 (Eif2ak4) deficiency did not spontaneously cause PVOD but produced immune dysregulation and inflammatory signatures under metabolic stress (asparaginase‑induced amino‑acid deprivation), including expansion of specific T‑cell populations at baseline and neutrophil infiltration plus innate immune gene upregulation after stress; scRNA‑seq and RNA‑seq were used. (bignard2023tcelldysregulationand pages 1-5)

**Direct abstract quote (2023):**
- Bignard et al. 2023: “Hereditary pulmonary veno-occlusive disease… is… due to biallelic loss-of-function of the EIF2AK4 gene… Lung mRNAS were analyzed by RNASeq and single cell RNASeq (scRNA-seq)… Under basal conditions, scRNA-seq analysis… revealed increases in two T cell populations…” (Published 2023‑05; https://doi.org/10.1152/ajplung.00460.2021) (bignard2023tcelldysregulationand pages 1-5)

### 6.4 Anatomical localization (UBERON suggestions)
- Lung (primary) → **lung (UBERON:0002048)**
- Pulmonary venules/small pulmonary veins (microvasculature) → **pulmonary vein (UBERON:0002017)** (approximate macro term; microvenules not explicitly mapped in retrieved evidence)
- Right ventricle (secondary) → **right ventricle (UBERON:0002080)** (supported by RV hypertrophy/failure) (prabhakar2024mechanismsunderlyingageassociated pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ level
- Primary: lung microvasculature (pulmonary venules/veins and capillary bed) (lechartier2024pulmonaryvenoocclusivedisease pages 3-5)
- Secondary: right ventricle/right heart due to increased pulmonary vascular resistance (prabhakar2024mechanismsunderlyingageassociated pages 1-2)

### 7.2 Tissue/cell level
- Vascular endothelium (CD31+ endothelial cells implicated in ISR signaling) (prabhakar2024mechanismsunderlyingageassociated pages 2-4)
- Perivascular inflammatory infiltrates (T cells and neutrophils highlighted in Gcn2 deficiency models) (bignard2023tcelldysregulationand pages 1-5)

### 7.3 Subcellular level (GO cellular component suggestions)
Not directly specified in retrieved evidence; however, ISR signaling implies involvement of cytosolic translation machinery and stress‑kinase signaling complexes.

---

## 8. Temporal Development

### 8.1 Onset
- Broad: children/young adults to older ages; EIF2AK4 carriers present younger (median 26 vs 60 years in one series). (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)

### 8.2 Progression / stages
PVOD/PCH is described as rapidly progressive with poor prognosis; quantitative endpoints reported include time from diagnosis to death/transplant and 1‑year mortality. (lechartier2024pulmonaryvenoocclusivedisease pages 3-5)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- Incidence ~0.1–0.5 per million/year; prevalence ~1–2 per million (rare). (lechartier2024pulmonaryvenoocclusivedisease pages 1-2)

### 9.2 Inheritance
- EIF2AK4‑associated PVOD/PCH is recessive/biallelic (compound heterozygous or homozygous), supported by segregation in Park 2023 and explicit “recessive form” statement. (park2023differentialdiagnosisof pages 2-3, park2023differentialdiagnosisof pages 4-4)

### 9.3 Demographics
- In one cohort description, EIF2AK4 carriers had a near‑equal sex ratio and younger age. (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)

---

## 10. Diagnostics

### 10.1 Clinical tests and biomarkers
**Hemodynamics (gold standard for PH diagnosis):** pre‑capillary PH with mPAP >20 mmHg, PAWP/PCWP ≤15 mmHg, PVR >2 WU. (lechartier2024pulmonaryvenoocclusivedisease pages 2-3, deshwal2025pulmonaryvenoocclusivedisease pages 8-9)

**Pulmonary function:** reduced DLCO is a key clue (e.g., <55% predicted in one suggested clinical pattern). (deshwal2025pulmonaryvenoocclusivedisease pages 8-9)

### 10.2 Imaging
**HRCT diagnostic triad:** centrilobular ground‑glass opacities + smooth interlobular septal thickening + mediastinal lymphadenopathy; parenchymal changes may precede overt PH. (lechartier2024pulmonaryvenoocclusivedisease pages 3-5)

### 10.3 Genetic testing
Genetic testing for **EIF2AK4** is recommended in suggestive cases; biallelic pathogenic variants can confirm heritable PVOD/PCH without histology. (lechartier2024pulmonaryvenoocclusivedisease pages 5-6, emanuelli2024functionalvalidationof pages 3-5)

### 10.4 Biopsy and procedure risk
ESC/ERS‑referenced guidance emphasizes clinical‑radiologic diagnosis and recommends against lung biopsy for confirmation. (lechartier2024pulmonaryvenoocclusivedisease pages 5-6, lechartier2024pulmonaryvenoocclusivedisease media a49a6475)

### 10.5 Differential diagnosis
Differential diagnoses include idiopathic PAH, ILD‑associated PH, and CTEPH (with V/Q scanning as key screen for CTEPH). (foster2025pulmonaryvenoocclusivedisease pages 10-12, deshwal2025pulmonaryvenoocclusivedisease pages 7-8)

---

## 11. Outcome / Prognosis

PVOD/PCH carries a very poor prognosis:
- 1‑year mortality ~72% and mean time from diagnosis to death/transplant 11.8 months (lechartier2024pulmonaryvenoocclusivedisease pages 3-5)
- Median survival often reported as 2–3 years after diagnosis (prabhakar2024mechanismsunderlyingageassociated pages 1-2)

A major adverse management outcome is **pulmonary edema precipitated by PAH vasodilators**, reported as >20% in a cohort and ~30/64 in a systematic review summarized in a clinical review. (lechartier2024pulmonaryvenoocclusivedisease pages 3-5, deshwal2025pulmonaryvenoocclusivedisease pages 9-10)

---

## 12. Treatment

### 12.1 Supportive care (real‑world standard)
- Supplemental oxygen and diuretics are commonly recommended supportive measures. (lechartier2024pulmonaryvenoocclusivedisease pages 3-5)
- Routine anticoagulation is not recommended unless another indication exists. (lechartier2024pulmonaryvenoocclusivedisease pages 3-5, foster2025pulmonaryvenoocclusivedisease pages 10-12)

**MAXO suggestions:**
- Oxygen therapy → **MAXO:0000861 (oxygen therapy)** (conceptual)
- Diuretic therapy → **MAXO:0000930 (diuretic therapy)** (conceptual)

### 12.2 PAH‑targeted therapies (caution)
PAH‑approved drugs “may be considered with careful monitoring of clinical symptoms and gas exchange” in guideline‑summarized recommendations, reflecting risk–benefit uncertainty; pulmonary edema can occur with any PAH drug class and can be life‑threatening. (lechartier2024pulmonaryvenoocclusivedisease pages 5-6, lechartier2024pulmonaryvenoocclusivedisease pages 3-5)

- Pulmonary edema incidence: >20% in a large cohort summary; systematic review summary indicates ~30/64 with edema; older series suggest 20–50% with PAH therapies and ~70% with calcium channel blockers. (lechartier2024pulmonaryvenoocclusivedisease pages 3-5, deshwal2025pulmonaryvenoocclusivedisease pages 9-10)

**MAXO suggestions:**
- Pulmonary vasodilator therapy → **MAXO:0001298 (vasodilator therapy)** (conceptual)

### 12.3 Definitive therapy
**Bilateral lung transplantation** is consistently described as the definitive/curative option; early referral to a transplant center is emphasized due to rapid progression. (lechartier2024pulmonaryvenoocclusivedisease pages 3-5, lechartier2024pulmonaryvenoocclusivedisease pages 1-2)

**MAXO suggestion:**
- Lung transplantation → **MAXO:0000602 (lung transplantation)** (conceptual)

### 12.4 Emerging/experimental (mechanism‑based)
Recent mechanistic work suggests that pharmacologic blockade of PKR/ISR pathways can mitigate disease phenotypes in MMC models, supporting investigational therapeutic directions; this is preclinical/experimental. (prabhakar2024mechanismsunderlyingageassociated pages 2-4)

---

## 13. Prevention

No established primary prevention strategies were identified in the retrieved evidence. Practical prevention in high‑risk contexts is best framed as:
- Avoidance/mitigation of exposures (occupational solvents; high‑risk chemotherapies when alternatives exist) consistent with risk association evidence. (lechartier2024pulmonaryvenoocclusivedisease pages 2-3)
- Genetic counseling and cascade testing in families with EIF2AK4‑associated disease. (lechartier2024pulmonaryvenoocclusivedisease pages 1-2)

---

## 14. Other Species / Natural Disease

Not identified in the retrieved evidence.

---

## 15. Model Organisms

### 15.1 Genetic models
- **Gcn2 (Eif2ak4)‑deficient rats**: phenotypically normal at baseline but show immune/inflammatory dysregulation under amino‑acid deprivation, analyzed with bulk RNA‑seq and scRNA‑seq. (bignard2023tcelldysregulationand pages 1-5)

### 15.2 Induced models
- **Mitomycin C (MMC) rat model**: induces PVOD‑like remodeling via PKR/ISR activation; aged rats show more severe remodeling and RV hypertrophy. (prabhakar2024mechanismsunderlyingageassociated pages 1-2, prabhakar2024mechanismsunderlyingageassociated pages 2-4)

### 15.3 Model limitations
Gcn2‑deficient rats did not spontaneously develop PVOD, suggesting additional triggers/factors are required to reproduce human disease fully. (bignard2023tcelldysregulationand pages 1-5)

---

## Current applications / real-world implementations (registries and carrier screening)
Clinical implementation is active in longitudinal registries and carrier surveillance:
- **NCT03902353** (2019; ClinicalTrials.gov): screening of **heterozygous EIF2AK4 carriers** using CT, DLCO, echo, CPET, and biomarkers to identify early abnormalities and predictors of PVOD development. (NCT03902353 chunk 1)
- **NCT03169010** (2017; ClinicalTrials.gov): long‑term rare pulmonary hypertension registry explicitly including PVOD and PCH with planned sequencing/biobank and survival/transplant outcomes. (NCT03169010 chunk 1)
- **NCT01907295** (2014; ClinicalTrials.gov): UK national cohort/biorepository including PVOD/PCH, deep phenotyping, and next‑generation sequencing for natural history and predictors. (NCT01907295 chunk 1)

---

## Visual evidence (guideline table)
The ESC/ERS 2022 PVOD/PCH recommendation summary table (diagnosis based on clinical+radiologic findings, lung biopsy not recommended, PAH drugs may be considered with careful monitoring) was retrieved as an image from Lechartier et al. 2024. (lechartier2024pulmonaryvenoocclusivedisease media a49a6475)

---

## Expert synthesis (authoritative interpretation grounded in cited sources)
1) **PVOD/PCH is best approached as a distinct PAH spectrum disorder** with venous/capillary involvement, where accurate early identification matters because common PAH vasodilator strategies can be dangerous (pulmonary edema) and the therapeutic window for transplant referral is short. (lechartier2024pulmonaryvenoocclusivedisease pages 3-5, lechartier2024pulmonaryvenoocclusivedisease pages 1-2)

2) **Genetic confirmation is increasingly central**: biallelic EIF2AK4 pathogenic variants can establish diagnosis without lung biopsy, enabling family testing and earlier care pathway decisions (e.g., transplant evaluation, exposure avoidance). (emanuelli2024functionalvalidationof pages 3-5, park2023differentialdiagnosisof pages 2-3)

3) **2023–2024 mechanistic advances converge on stress-response and barrier biology** (ISR/PKR/PP1 axis; endothelial junction disruption) and suggest tractable therapeutic targets, but these remain preclinical and not yet standard of care. (prabhakar2024mechanismsunderlyingageassociated pages 2-4)

---

## URLs and publication dates (key sources used)
- Lechartier B. et al. **2024‑01**. *European Respiratory Review.* https://doi.org/10.1183/16000617.0156-2023 (lechartier2024pulmonaryvenoocclusivedisease pages 1-2)
- Park J.E. et al. **2023‑02**. *Molecular Syndromology.* https://doi.org/10.1159/000527524 (park2023differentialdiagnosisof pages 2-3)
- Prabhakar A. et al. **2024‑09**. *JCI Insight.* https://doi.org/10.1172/jci.insight.181877 (prabhakar2024mechanismsunderlyingageassociated pages 1-2)
- Bignard J. et al. **2023‑05**. *AJP-Lung.* https://doi.org/10.1152/ajplung.00460.2021 (bignard2023tcelldysregulationand pages 1-5)
- Emanuelli G. et al. **2024‑04**. https://doi.org/10.17863/cam.108223 (emanuelli2024functionalvalidationof pages 1-3)

---

## Limitations of this report (evidence availability)
- Standard identifiers (OMIM/Orphanet/ICD/MeSH/MONDO) and some phenotype frequency statistics were not present in the retrieved corpus for this run; the report therefore focuses on high‑confidence clinical, genetic, imaging, mechanistic, and guideline‑linked evidence available in the provided texts. (lechartier2024pulmonaryvenoocclusivedisease pages 1-2, deshwal2025pulmonaryvenoocclusivedisease pages 1-2)

References

1. (lechartier2024pulmonaryvenoocclusivedisease pages 1-2): Benoit Lechartier, Athénaïs Boucly, Sabina Solinas, Deepa Gopalan, Peter Dorfmüller, Teodora Radonic, Olivier Sitbon, and David Montani. Pulmonary veno-occlusive disease: illustrative cases and literature review. European Respiratory Review, 33:230156, Jan 2024. URL: https://doi.org/10.1183/16000617.0156-2023, doi:10.1183/16000617.0156-2023. This article has 28 citations and is from a peer-reviewed journal.

2. (deshwal2025pulmonaryvenoocclusivedisease pages 1-2): Himanshu Deshwal, Sauradeep Sarkar, Atreyee Basu, and Bilal A. Jalil. Pulmonary veno-occlusive disease: a clinical review. Breathe, 21:240098, Jan 2025. URL: https://doi.org/10.1183/20734735.0098-2024, doi:10.1183/20734735.0098-2024. This article has 4 citations.

3. (deshwal2025pulmonaryvenoocclusivedisease pages 2-3): Himanshu Deshwal, Sauradeep Sarkar, Atreyee Basu, and Bilal A. Jalil. Pulmonary veno-occlusive disease: a clinical review. Breathe, 21:240098, Jan 2025. URL: https://doi.org/10.1183/20734735.0098-2024, doi:10.1183/20734735.0098-2024. This article has 4 citations.

4. (lechartier2024pulmonaryvenoocclusivedisease pages 3-5): Benoit Lechartier, Athénaïs Boucly, Sabina Solinas, Deepa Gopalan, Peter Dorfmüller, Teodora Radonic, Olivier Sitbon, and David Montani. Pulmonary veno-occlusive disease: illustrative cases and literature review. European Respiratory Review, 33:230156, Jan 2024. URL: https://doi.org/10.1183/16000617.0156-2023, doi:10.1183/16000617.0156-2023. This article has 28 citations and is from a peer-reviewed journal.

5. (prabhakar2024mechanismsunderlyingageassociated pages 1-2): Amit Prabhakar, Meetu Wadhwa, Rahul Kumar, Prajakta Ghatpande, Aneta Gandjeva, Rubin M. Tuder, Brian B. Graham, Giorgio Lagna, and Akiko Hata. Mechanisms underlying age-associated exacerbation of pulmonary veno-occlusive disease. JCI Insight, Sep 2024. URL: https://doi.org/10.1172/jci.insight.181877, doi:10.1172/jci.insight.181877. This article has 7 citations and is from a domain leading peer-reviewed journal.

6. (lechartier2024pulmonaryvenoocclusivedisease pages 2-3): Benoit Lechartier, Athénaïs Boucly, Sabina Solinas, Deepa Gopalan, Peter Dorfmüller, Teodora Radonic, Olivier Sitbon, and David Montani. Pulmonary veno-occlusive disease: illustrative cases and literature review. European Respiratory Review, 33:230156, Jan 2024. URL: https://doi.org/10.1183/16000617.0156-2023, doi:10.1183/16000617.0156-2023. This article has 28 citations and is from a peer-reviewed journal.

7. (deshwal2025pulmonaryvenoocclusivedisease pages 8-9): Himanshu Deshwal, Sauradeep Sarkar, Atreyee Basu, and Bilal A. Jalil. Pulmonary veno-occlusive disease: a clinical review. Breathe, 21:240098, Jan 2025. URL: https://doi.org/10.1183/20734735.0098-2024, doi:10.1183/20734735.0098-2024. This article has 4 citations.

8. (deshwal2025pulmonaryvenoocclusivedisease pages 7-8): Himanshu Deshwal, Sauradeep Sarkar, Atreyee Basu, and Bilal A. Jalil. Pulmonary veno-occlusive disease: a clinical review. Breathe, 21:240098, Jan 2025. URL: https://doi.org/10.1183/20734735.0098-2024, doi:10.1183/20734735.0098-2024. This article has 4 citations.

9. (foster2025pulmonaryvenoocclusivedisease pages 4-6): Brian Foster, Sikandar Khan, Ana Suarez Gonzalez, and Samantha Gillenwater. Pulmonary veno-occlusive disease: a comprehensive review of diagnostic challenges, therapeutic limitations, and evolving management. Advances in Respiratory Medicine, 93:48, Oct 2025. URL: https://doi.org/10.3390/arm93060048, doi:10.3390/arm93060048. This article has 2 citations.

10. (lechartier2024pulmonaryvenoocclusivedisease pages 5-6): Benoit Lechartier, Athénaïs Boucly, Sabina Solinas, Deepa Gopalan, Peter Dorfmüller, Teodora Radonic, Olivier Sitbon, and David Montani. Pulmonary veno-occlusive disease: illustrative cases and literature review. European Respiratory Review, 33:230156, Jan 2024. URL: https://doi.org/10.1183/16000617.0156-2023, doi:10.1183/16000617.0156-2023. This article has 28 citations and is from a peer-reviewed journal.

11. (lechartier2024pulmonaryvenoocclusivedisease media a49a6475): Benoit Lechartier, Athénaïs Boucly, Sabina Solinas, Deepa Gopalan, Peter Dorfmüller, Teodora Radonic, Olivier Sitbon, and David Montani. Pulmonary veno-occlusive disease: illustrative cases and literature review. European Respiratory Review, 33:230156, Jan 2024. URL: https://doi.org/10.1183/16000617.0156-2023, doi:10.1183/16000617.0156-2023. This article has 28 citations and is from a peer-reviewed journal.

12. (park2023differentialdiagnosisof pages 2-3): Jong Eun Park, Sung-A Chang, Shin Yi Jang, Kyung Soo Lee, Duk-Kyung Kim, and Chang-Seok Ki. Differential diagnosis of pulmonary veno-occlusive disease and/or pulmonary capillary hemangiomatosis after identification of two novel eif2ak4 variants by whole-exome sequencing. Molecular Syndromology, 14:254-257, Feb 2023. URL: https://doi.org/10.1159/000527524, doi:10.1159/000527524. This article has 6 citations and is from a peer-reviewed journal.

13. (park2023differentialdiagnosisof pages 1-2): Jong Eun Park, Sung-A Chang, Shin Yi Jang, Kyung Soo Lee, Duk-Kyung Kim, and Chang-Seok Ki. Differential diagnosis of pulmonary veno-occlusive disease and/or pulmonary capillary hemangiomatosis after identification of two novel eif2ak4 variants by whole-exome sequencing. Molecular Syndromology, 14:254-257, Feb 2023. URL: https://doi.org/10.1159/000527524, doi:10.1159/000527524. This article has 6 citations and is from a peer-reviewed journal.

14. (emanuelli2024functionalvalidationof pages 3-5): Giulia Emanuelli, JiaYi Zhu, Wei Li, Nicholas W Morrell, and Stefan J Marciniak. Functional validation of eif2ak4 (gcn2) missense variants associated with pulmonary arterial hypertension. JournalArticle, Apr 2024. URL: https://doi.org/10.17863/cam.108223, doi:10.17863/cam.108223. This article has 14 citations.

15. (emanuelli2024functionalvalidationof pages 1-3): Giulia Emanuelli, JiaYi Zhu, Wei Li, Nicholas W Morrell, and Stefan J Marciniak. Functional validation of eif2ak4 (gcn2) missense variants associated with pulmonary arterial hypertension. JournalArticle, Apr 2024. URL: https://doi.org/10.17863/cam.108223, doi:10.17863/cam.108223. This article has 14 citations.

16. (prabhakar2024mechanismsunderlyingageassociated pages 2-4): Amit Prabhakar, Meetu Wadhwa, Rahul Kumar, Prajakta Ghatpande, Aneta Gandjeva, Rubin M. Tuder, Brian B. Graham, Giorgio Lagna, and Akiko Hata. Mechanisms underlying age-associated exacerbation of pulmonary veno-occlusive disease. JCI Insight, Sep 2024. URL: https://doi.org/10.1172/jci.insight.181877, doi:10.1172/jci.insight.181877. This article has 7 citations and is from a domain leading peer-reviewed journal.

17. (bignard2023tcelldysregulationand pages 1-5): Juliette Bignard, Fabrice Atassi, Olivier Claude, Maria-Rosa Ghigna, Nathalie Mougenot, Bahgat Soilih Abdoulkarim, Florence Deknuydt, Aurélie Gestin, Virginie Monceau, David Montani, Sophie Nadaud, Florent Soubrier, and Frédéric Perros. T-cell dysregulation and inflammatory process in <i>gcn2</i> (<i>eif2ak4</i><sup>−/−</sup>)-deficient rats in basal and stress conditions. American Journal of Physiology-Lung Cellular and Molecular Physiology, 324:L609-L624, May 2023. URL: https://doi.org/10.1152/ajplung.00460.2021, doi:10.1152/ajplung.00460.2021. This article has 5 citations.

18. (bignard2023tcelldysregulationand pages 16-19): Juliette Bignard, Fabrice Atassi, Olivier Claude, Maria-Rosa Ghigna, Nathalie Mougenot, Bahgat Soilih Abdoulkarim, Florence Deknuydt, Aurélie Gestin, Virginie Monceau, David Montani, Sophie Nadaud, Florent Soubrier, and Frédéric Perros. T-cell dysregulation and inflammatory process in <i>gcn2</i> (<i>eif2ak4</i><sup>−/−</sup>)-deficient rats in basal and stress conditions. American Journal of Physiology-Lung Cellular and Molecular Physiology, 324:L609-L624, May 2023. URL: https://doi.org/10.1152/ajplung.00460.2021, doi:10.1152/ajplung.00460.2021. This article has 5 citations.

19. (deshwal2025pulmonaryvenoocclusivedisease pages 9-10): Himanshu Deshwal, Sauradeep Sarkar, Atreyee Basu, and Bilal A. Jalil. Pulmonary veno-occlusive disease: a clinical review. Breathe, 21:240098, Jan 2025. URL: https://doi.org/10.1183/20734735.0098-2024, doi:10.1183/20734735.0098-2024. This article has 4 citations.

20. (foster2025pulmonaryvenoocclusivedisease pages 10-12): Brian Foster, Sikandar Khan, Ana Suarez Gonzalez, and Samantha Gillenwater. Pulmonary veno-occlusive disease: a comprehensive review of diagnostic challenges, therapeutic limitations, and evolving management. Advances in Respiratory Medicine, 93:48, Oct 2025. URL: https://doi.org/10.3390/arm93060048, doi:10.3390/arm93060048. This article has 2 citations.

21. (NCT03902353 chunk 1):  Screening of Pulmonary Veino Occlusive Disease in Heterozygous EIF2AK4 Mutation Carriers. Assistance Publique - Hôpitaux de Paris. 2019. ClinicalTrials.gov Identifier: NCT03902353

22. (NCT03169010 chunk 1): Zhi-Cheng JING, MD. Registration Study for Rare Type of Pulmonary Hypertension. China National Center for Cardiovascular Diseases. 2017. ClinicalTrials.gov Identifier: NCT03169010

23. (NCT01907295 chunk 1): Nick Morrell. National Cohort Study of Idiopathic and Heritable Pulmonary Arterial Hypertension. University of Cambridge. 2014. ClinicalTrials.gov Identifier: NCT01907295

24. (park2023differentialdiagnosisof pages 4-4): Jong Eun Park, Sung-A Chang, Shin Yi Jang, Kyung Soo Lee, Duk-Kyung Kim, and Chang-Seok Ki. Differential diagnosis of pulmonary veno-occlusive disease and/or pulmonary capillary hemangiomatosis after identification of two novel eif2ak4 variants by whole-exome sequencing. Molecular Syndromology, 14:254-257, Feb 2023. URL: https://doi.org/10.1159/000527524, doi:10.1159/000527524. This article has 6 citations and is from a peer-reviewed journal.