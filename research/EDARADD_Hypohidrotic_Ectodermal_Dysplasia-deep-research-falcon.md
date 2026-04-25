---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T18:17:33.386841'
end_time: '2026-04-24T18:24:52.031483'
duration_seconds: 438.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: EDARADD-Related Hypohidrotic Ectodermal Dysplasia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** EDARADD-Related Hypohidrotic Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **EDARADD-Related Hypohidrotic Ectodermal Dysplasia** covering all of the
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
- **Disease Name:** EDARADD-Related Hypohidrotic Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **EDARADD-Related Hypohidrotic Ectodermal Dysplasia** covering all of the
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


# EDARADD‑Related Hypohidrotic Ectodermal Dysplasia (HED): Comprehensive Disease Characteristics Report (2026-04-25)

## Executive summary
EDARADD‑related hypohidrotic ectodermal dysplasia is a rare, primarily autosomal form of HED caused by pathogenic variants in **EDARADD**, an intracellular adaptor in the **EDA‑A1 → EDAR → EDARADD → TRAF6 → NF‑κB** signaling axis required for ectodermal appendage development. Clinically it overlaps strongly with other HED genetic etiologies and is defined by the classic triad of **hypohidrosis/anhidrosis**, **hypodontia/anodontia**, and **hypotrichosis**, with additional skin, craniofacial, ocular, and respiratory sequelae reported across HED. Mechanistically, recent functional work demonstrates that specific EDARADD missense variants can act via **dominant‑negative disruption of EDAR–EDARADD complex formation and TRAF6 binding**, decreasing NF‑κB activation. (asano2021characterizationofedaradd pages 1-3, asano2021characterizationofedaradd pages 5-7)

## 1. Disease information
### 1.1 Concise overview (current understanding)
Hypohidrotic ectodermal dysplasia (HED) is an inherited developmental disorder affecting ectoderm‑derived structures, classically involving the triad of impaired sweating, abnormal/missing teeth, and sparse hair. (asano2021characterizationofedaradd pages 1-3, callea2022extendedoverviewof pages 2-4)

**EDARADD‑related HED** refers to autosomal forms attributable to pathogenic variants in **EDARADD (EDAR‑associated death domain)**. In contemporary clinical genetics, EDARADD‑related HED is usually considered within the broader HED spectrum because phenotypes due to EDA, EDAR, and EDARADD defects are often clinically similar due to shared pathway disruption. (kablan2024novelhomozygousframeshift pages 1-2)

### 1.2 Key identifiers (from accessible primary/review literature)
A compact identifier table is provided below.

| Item | Value | Source / date / URL | Evidence citation IDs |
|---|---|---|---|
| Disease name | EDARADD-related hypohidrotic ectodermal dysplasia | Kablan & Tasdelen, *Italian Journal of Pediatrics*, 2024-06, https://doi.org/10.1186/s13052-024-01681-2 | (kablan2024novelhomozygousframeshift pages 1-2) |
| Preferred broader disease term | Hypohidrotic ectodermal dysplasia (HED); most common ED subtype | Martínez-Romero et al., *Orphanet Journal of Rare Diseases*, 2019-12, https://doi.org/10.1186/s13023-019-1251-x | (martinezromero2019edaedaredaradd pages 1-2) |
| Key synonyms / nomenclature | Autosomal recessive HED; autosomal dominant HED; anhidrotic/hypohidrotic ectodermal dysplasia; hypohidrotic/hair/tooth type; hypohidrotic/hair/nail type | Callea et al., *Children*, 2022-09, https://doi.org/10.3390/children9091357; Higashino et al., *Expert Opinion on Orphan Drugs*, 2017-11, http://dx.doi.org/10.1080/21678707.2017.1405806 | (callea2022extendedoverviewof pages 2-4, higashino2017advancesinthe pages 1-7, higashino2017advancesinthe pages 12-16) |
| OMIM disease IDs mentioned in sources | HED/EDA1 MIM#305100 (XLHED); AD HED MIM#129490; AR HED MIM#224900; EDARADD-related AR HED MIM#614940 | Callea et al., *Children*, 2022-09, https://doi.org/10.3390/children9091357; Higashino et al., *Expert Opinion on Orphan Drugs*, 2017-11, http://dx.doi.org/10.1080/21678707.2017.1405806 | (callea2022extendedoverviewof pages 2-4, higashino2017advancesinthe pages 1-7) |
| Gene | **EDARADD** (EDAR-associated death domain) | Martínez-Romero et al., *Orphanet Journal of Rare Diseases*, 2019-12, https://doi.org/10.1186/s13023-019-1251-x | (martinezromero2019edaedaredaradd pages 1-2) |
| Gene OMIM ID | EDARADD MIM*606603 | Callea et al., *Children*, 2022-09, https://doi.org/10.3390/children9091357; Martínez-Romero et al., *Orphanet Journal of Rare Diseases*, 2019-12, https://doi.org/10.1186/s13023-019-1251-x | (callea2022extendedoverviewof pages 2-4, martinezromero2019edaedaredaradd pages 1-2) |
| Chromosomal location | 1q42-q43 / 1q42.3 | Callea et al., *Children*, 2022-09, https://doi.org/10.3390/children9091357; Martínez-Romero et al., *Orphanet Journal of Rare Diseases*, 2019-12, https://doi.org/10.1186/s13023-019-1251-x | (callea2022extendedoverviewof pages 2-4, martinezromero2019edaedaredaradd pages 1-2) |
| Core clinical triad used in nomenclature | Hypodontia/anodontia, hypotrichosis, hypohidrosis (reduced or absent sweating) | Asano et al., *Journal of Dermatology*, 2021, https://doi.org/10.1111/1346-8138.16044; Callea et al., *Children*, 2022-09, https://doi.org/10.3390/children9091357 | (asano2021characterizationofedaradd pages 1-3, callea2022extendedoverviewof pages 2-4) |
| Epidemiology estimate (overall HED) | At least 1 in 17,000 people worldwide | Callea et al., *Children*, 2022-09, https://doi.org/10.3390/children9091357 | (callea2022extendedoverviewof pages 2-4) |
| Epidemiology estimate (XLHED) | 1/50,000–100,000 males | Martínez-Romero et al., *Orphanet Journal of Rare Diseases*, 2019-12, https://doi.org/10.1186/s13023-019-1251-x | (martinezromero2019edaedaredaradd pages 1-2) |
| Additional prevalence estimate reported in review literature | ~7 per 10,000 live births (reported in one review; likely refers broadly to HED/ED literature and should be interpreted cautiously against rarer estimates above) | Higashino et al., *Expert Opinion on Orphan Drugs*, 2017-11, http://dx.doi.org/10.1080/21678707.2017.1405806 | (higashino2017advancesinthe pages 1-7) |


*Table: This table summarizes the core identifiers, synonyms, OMIM entries, gene details, chromosomal locus, and commonly cited epidemiology figures relevant to EDARADD-related hypohidrotic ectodermal dysplasia. It is useful as a compact nomenclature and disease-mapping reference for downstream knowledge-base curation.*

**Notes on identifiers not retrieved with tools in this run:** MONDO and MeSH identifiers were not directly retrievable using the available tool set (no direct OMIM/Orphanet/MeSH ingestion tools were available in this session). Therefore, this report cites OMIM/MIM numbers as stated in the peer‑reviewed sources above. (callea2022extendedoverviewof pages 2-4, higashino2017advancesinthe pages 1-7)

### 1.3 Common synonyms / alternative names
* Hypohidrotic ectodermal dysplasia (HED); anhidrotic ectodermal dysplasia (AED) (frequently used as overlapping terminology) (kablan2024novelhomozygousframeshift pages 1-2)
* Autosomal recessive HED; autosomal dominant HED (depending on variant mechanism) (asano2021characterizationofedaradd pages 1-3)
* “Hypohidrotic/hair/tooth type” (terminology used in some OMIM‑linked descriptions cited in reviews) (callea2022extendedoverviewof pages 2-4)

### 1.4 Evidence source type
The disease characterization in this report is derived from:
* **Aggregated disease-level resources** embedded in peer‑reviewed reviews (e.g., epidemiology and phenotype summaries) (callea2022extendedoverviewof pages 2-4, higashino2017advancesinthe pages 1-7)
* **Human clinical case reports/series** with genotype–phenotype data (kablan2024novelhomozygousframeshift pages 1-2)
* **Human cohort molecular studies** (diagnostic yield statistics and genetic profiling) (martinezromero2019edaedaredaradd pages 1-2, kim2024geneticprofilingand pages 1-2)
* **In vitro functional studies** of EDARADD variants (asano2021characterizationofedaradd pages 1-3, asano2021characterizationofedaradd pages 5-7)

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** Germline pathogenic variants in **EDARADD** disrupting ectodysplasin pathway signaling required for ectodermal appendage development. EDARADD is described as an **adaptor protein of EDAR**; after **EDA‑A1 binds EDAR**, EDAR and EDARADD interact via death domains, and EDARADD binds TRAF6 leading to **downstream activation of NF‑κB**. (asano2021characterizationofedaradd pages 1-3)

Verbatim abstract support for triad and autosomal genetic causes:
* Asano et al. 2021: “Hypohidrotic ectodermal dysplasia (HED) is a genetic disorder characterized by hypohidrosis, hypodontia, and hypotrichosis. Autosomal forms of the disease are caused by mutations in either EDAR or EDARADD.” (asano2021characterizationofedaradd pages 1-3)

### 2.2 Risk factors
**Genetic risk factors:**
* Having a pathogenic EDARADD variant consistent with autosomal inheritance (recessive or dominant depending on variant). Dominantly inherited EDARADD variants have been functionally demonstrated to reduce NF‑κB signaling in a dominant‑negative manner. (asano2021characterizationofedaradd pages 1-3, asano2021characterizationofedaradd pages 5-7)
* Consanguinity can increase risk for autosomal recessive EDARADD‑related HED; a 2024 report describes two affected brothers born to consanguineous parents with a homozygous frameshift EDARADD variant. (kablan2024novelhomozygousframeshift pages 1-2)

**Environmental risk factors:** Not established as causal; disease is genetic/developmental. However, clinical complications (e.g., hyperthermia) are sensitive to ambient temperature and infection‑related fever episodes. (kablan2024novelhomozygousframeshift pages 1-2, callea2022extendedoverviewof pages 2-4)

### 2.3 Protective factors
No validated genetic “protective variants” or environmental protective factors specific to EDARADD‑related HED were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No direct gene–environment interaction studies specific to EDARADD‑related HED were identified in the retrieved evidence. Downstream, inability to sweat (genetic) interacts with heat exposure (environment) to increase risk for hyperthermia. (callea2022extendedoverviewof pages 2-4)

## 3. Phenotypes
### 3.1 Core phenotypes (symptoms/signs) with suggested HPO terms
The classic HED triad is consistently emphasized:
* **Hypohidrosis/anhidrosis** (reduced/absent sweating) (asano2021characterizationofedaradd pages 1-3, callea2022extendedoverviewof pages 2-4)
  * Suggested HPO: **HP:0000972** (Anhidrosis) / **HP:0000966** (Hypohidrosis)
* **Hypodontia/anodontia** (missing teeth) and/or abnormal tooth shape (kablan2024novelhomozygousframeshift pages 1-2, callea2022extendedoverviewof pages 2-4)
  * Suggested HPO: **HP:0000668** (Hypodontia), **HP:0000674** (Anodontia), **HP:0000692** (Abnormality of tooth shape), **HP:0000689** (Dental crowding) where present
* **Hypotrichosis / sparse hair** (kablan2024novelhomozygousframeshift pages 1-2, callea2022extendedoverviewof pages 2-4)
  * Suggested HPO: **HP:0001006** (Hypotrichosis), **HP:0002209** (Sparse scalp hair)

Additional manifestations described in an EDARADD case report include dry skin and craniofacial features:
* **Dry skin** (kablan2024novelhomozygousframeshift pages 1-2)
  * Suggested HPO: **HP:0000958** (Dry skin)
* **Facial dysmorphism** (mildly prominent forehead; periorbital wrinkles; sparse eyebrows/eyelashes) (kablan2024novelhomozygousframeshift pages 1-2)
  * Suggested HPO: **HP:0000337** (Broad forehead) / **HP:0011220** (Prominent forehead), **HP:0000534** (Sparse eyelashes), **HP:0002223** (Sparse eyebrow)

### 3.2 Phenotype characteristics
* **Age of onset:** Congenital/early childhood presentation is typical; in the EDARADD case report, features were present in early childhood (ages 2 and 5). (kablan2024novelhomozygousframeshift pages 1-2)
* **Severity/variability:** Variable expressivity is implied; in siblings with the same homozygous EDARADD frameshift, the younger sibling had “less severe” features. (kablan2024novelhomozygousframeshift pages 1-2)

### 3.3 Quality of life impact
HED is associated with clinically significant morbidity from thermoregulation issues and downstream complications. A review notes that affected individuals are “at risk for life-threatening hyperthermia” and may experience “chronic developmental, respiratory, cutaneous, ocular, and psychosocial disorders.” (callea2022extendedoverviewof pages 2-4)

## 4. Genetic / molecular information
### 4.1 Causal gene
* **EDARADD** (EDAR‑associated death domain), OMIM/MIM*606603, chromosomal locus **1q42‑q43 / 1q42.3** as reported in review and cohort literature. (callea2022extendedoverviewof pages 2-4, martinezromero2019edaedaredaradd pages 1-2)

### 4.2 Pathogenic variants and functional consequences
#### 4.2.1 Dominant‑negative EDARADD missense variants (functional study)
Asano et al. (2021; *J Dermatol*; DOI 10.1111/1346-8138.16044) performed in vitro characterization of three dominantly inherited and one recessively inherited EDARADD missense variants:

Verbatim abstract quotes:
* “we performed detailed in vitro analyses in order to characterize three dominantly inherited missense mutations, **p.D120Y, p.L122R, and p.D123N**, and one recessively inherited missense mutation, **p.E152K**, in the EDARADD gene.” (asano2021characterizationofedaradd pages 1-3)
* “Nuclear factor (NF)-κB reporter assays demonstrated that all the mutant EDARADD showed reduction in activation of NF-κB.” (asano2021characterizationofedaradd pages 1-3)
* “Importantly, p.D120Y-, p.L122R-, and p.D123N-mutant EDARADD slightly reduced the NF-κB activity induced by wild-type EDARADD in a **dominant negative manner**.” (asano2021characterizationofedaradd pages 1-3)
* “Finally, we found that p.D120Y-, p.L122R-, and p.D123N-mutant EDARADD completely lost the ability to bind with **TRAF6**, while p.E152K-mutant EDARADD showed a mild reduction in the affinity.” (asano2021characterizationofedaradd pages 1-3)

Mechanistic details from results/discussion text:
* Dominant mutants reduced EDAR–WT‑EDARADD interaction: the amount of EDAR intracellular domain co‑immunoprecipitated with WT EDARADD was “markedly reduced” when **p.D120Y/p.L122R/p.D123N** were overexpressed, supporting interference with EDAR–EDARADD complex formation. (asano2021characterizationofedaradd pages 5-7)
* TRAF6 binding: **p.D120Y/p.L122R/p.D123N** “completely failed to bind with TRAF6,” while **p.E152K** retained binding with only a “slight” reduction (~20% as reported in text). (asano2021characterizationofedaradd pages 5-7)

**Interpretation (current expert consensus based on evidence above):**
* p.D120Y, p.L122R, p.D123N behave as dominant‑negative variants that disrupt the EDAR signalosome and abolish TRAF6 recruitment, resulting in strongly decreased NF‑κB signaling. (asano2021characterizationofedaradd pages 1-3, asano2021characterizationofedaradd pages 5-7)
* p.E152K appears hypomorphic/partial loss‑of‑function in the same assays. (asano2021characterizationofedaradd pages 1-3, asano2021characterizationofedaradd pages 5-7)

#### 4.2.2 Recessive truncating variant (human case report)
Kablan & Tasdelen (2024; *Italian Journal of Pediatrics*; DOI 10.1186/s13052-024-01681-2) reported a novel homozygous frameshift:
* **EDARADD c.322_323insCGGGC, p.(Arg108ProfsTer7)** identified in two affected brothers. (kablan2024novelhomozygousframeshift pages 1-2)

Verbatim abstract quote:
* “targeted next-generation sequencing analysis yielded the novel homozygous insertion variant **c.322_323insCGGGC p.(Arg108ProfsTer7)** in EDARADD.” (kablan2024novelhomozygousframeshift pages 1-2)

The authors explicitly link the pathway to NF‑κB:
* “Proper function of these three genes and their products is crucial for downstream activation of the nuclear factor (NF‑κB) … involved in ectodermal development.” (kablan2024novelhomozygousframeshift pages 1-2)

### 4.3 Modifier genes
No EDARADD‑specific modifier gene evidence was identified in the retrieved texts. Broader ED genetics includes other genes that can produce ED/HED‑like phenotypes (e.g., TRAF6, NF‑κB pathway genes), but modifier roles for EDARADD phenotypic severity were not established in the available evidence. (kim2024geneticprofilingand pages 2-4)

### 4.4 Epigenetics
No EDARADD‑specific epigenetic mechanisms were identified in the retrieved evidence.

### 4.5 Chromosomal abnormalities
No EDARADD‑related structural chromosomal abnormalities were identified in the retrieved evidence.

## 5. Environmental information
No specific environmental toxins/lifestyle/infectious triggers as causal factors were identified; HED is primarily genetic. Clinically, fever/infections and heat exposure are important exacerbating contexts for hyperthermia risk due to hypohidrosis. (kablan2024novelhomozygousframeshift pages 1-2, callea2022extendedoverviewof pages 2-4)

## 6. Mechanism / pathophysiology
### 6.1 Molecular pathway (EDA‑EDAR‑EDARADD‑TRAF6‑NF‑κB)
As described in Asano et al. 2021:
* “EDARADD is an adaptor protein of EDAR… EDARADD also binds to key proteins for the signal transduction, such as… **TRAF6**, which finally leads to the downstream activation of… **NF‑κB**.” (asano2021characterizationofedaradd pages 1-3)

**Causal chain to phenotype (integrated):**
1. **Upstream trigger:** Germline EDARADD pathogenic variant (loss‑of‑function or dominant negative). (kablan2024novelhomozygousframeshift pages 1-2, asano2021characterizationofedaradd pages 1-3)
2. **Signalosome defect:** Impaired EDAR–EDARADD interactions and/or impaired EDARADD–TRAF6 binding. (asano2021characterizationofedaradd pages 5-7)
3. **Pathway output:** Reduced downstream **NF‑κB activation** (reporter assay reductions; abolished TRAF6 binding for dominant variants). (asano2021characterizationofedaradd pages 1-3, asano2021characterizationofedaradd pages 5-7)
4. **Developmental consequence:** NF‑κB‑dependent transcriptional programs for ectodermal appendage development are disrupted, resulting in hypoplasia/absence of sweat glands, abnormal dentition, and hypotrichosis. (asano2021characterizationofedaradd pages 1-3, callea2022extendedoverviewof pages 2-4)

### 6.2 Suggested ontology terms
**GO Biological Process (suggestions):**
* NF‑κB signaling (e.g., “I‑kappaB kinase/NF‑kappaB signaling”)
* Ectodermal appendage development (hair follicle development; tooth development; sweat gland development)

**Cell types (CL suggestions):**
* Epidermal keratinocyte
* Epithelial cell of eccrine sweat gland
* Odontogenic epithelial cell / dental epithelium

Because ontology identifiers were not retrieved by tools in this session, the above are suggestions for curation rather than evidence‑linked claims.

## 7. Anatomical structures affected
HED affects ectoderm‑derived structures. In EDARADD‑related disease, the most prominently affected include:
* **Hair follicles / scalp hair** (hypotrichosis) (kablan2024novelhomozygousframeshift pages 1-2, callea2022extendedoverviewof pages 2-4)
* **Teeth / dentition** (hypodontia; conical teeth; spacing) (kablan2024novelhomozygousframeshift pages 1-2, callea2022extendedoverviewof pages 2-4)
* **Eccrine sweat glands** (hypohidrosis/anhidrosis) (callea2022extendedoverviewof pages 2-4)

Suggested UBERON terms (for curation):
* Eccrine sweat gland; hair follicle; tooth; epidermis.

## 8. Temporal development
* **Onset:** Congenital/developmental; recognized in infancy/childhood due to tooth eruption abnormalities, sparse hair, and heat intolerance/anhidrosis. (kablan2024novelhomozygousframeshift pages 1-2, callea2022extendedoverviewof pages 2-4)
* **Course:** Lifelong developmental disorder; complications (hyperthermia risk; ocular/respiratory/skin issues) persist and require ongoing management. (callea2022extendedoverviewof pages 2-4)

## 9. Inheritance and population
### 9.1 Inheritance
* EDARADD‑related HED can be **autosomal recessive** (e.g., homozygous frameshift c.322_323insCGGGC) (kablan2024novelhomozygousframeshift pages 1-2)
* Specific EDARADD missense variants can be **autosomal dominant** via dominant‑negative mechanisms (p.D120Y/p.L122R/p.D123N). (asano2021characterizationofedaradd pages 1-3)

### 9.2 Epidemiology (recent/authoritative statistics)
Reported estimates vary by source and by whether the estimate refers to all HED, XLHED specifically, or broader ED.

* HED affects “at least **1 in 17,000** people worldwide” (review). (callea2022extendedoverviewof pages 2-4)
* XLHED incidence: “**1/50,000–100,000 males**” (Spanish cohort background statement). (martinezromero2019edaedaredaradd pages 1-2)
* One review reports HED “occurs in **~7 per 10,000 live births**” (interpretation caution: this may reflect broader ED ascertainment or mixed definitions across sources). (higashino2017advancesinthe pages 1-7)

**Population-level ED diagnostic yield (implementation statistic):**
In a 2024 Korean ED cohort (n=27), **74.1% (20/27)** were mutation-positive; among positives, EDA/EDAR comprised **80% (16/20)**. The authors also report WES virtual panel yield 56.5% (13/23), and expanded OMIM analysis adding 4 more diagnoses (~17% increase). (kim2024geneticprofilingand pages 1-2)

## 10. Diagnostics
### 10.1 Clinical diagnosis
Clinical suspicion is typically triggered by the triad of hair/sweating/dental anomalies. (callea2022extendedoverviewof pages 2-4)

### 10.2 Genetic testing (real-world implementation)
**Testing approaches supported by 2024 evidence:**
* For “classical symptoms,” targeted sequencing of core genes (e.g., EDA/EDAR; in broader practice this often includes EDARADD and WNT10A panels) can be prioritized; when classic features are absent or phenotype is atypical, WES can improve yield. (kim2024geneticprofilingand pages 1-2, kim2024geneticprofilingand pages 2-4)

Verbatim abstract quote (Kim et al. 2024):
* “When conducting molecular diagnostics for ED, opting for targeted sequencing of EDA/EDAR mutations is advisable for cases with classical symptoms, while WES is deemed an effective strategy for cases in which these symptoms are absent.” (kim2024geneticprofilingand pages 1-2)

### 10.3 Prenatal diagnosis (expert discussion)
A review describes ultrasound assessment of tooth germs/maxilla/mandible in at‑risk fetuses as a prenatal diagnostic tool in families with ED history. (callea2022extendedoverviewof pages 2-4)

### 10.4 Differential diagnosis
Other ED/HED‑like disorders arise from mutations in EDA, EDAR, WNT10A and additional ED genes (including NF‑κB pathway–related genes), which can overlap clinically. (higashino2017advancesinthe pages 1-7, kim2024geneticprofilingand pages 2-4)

## 11. Outcome / prognosis
HED can involve substantial morbidity. A review notes risk for “life‑threatening hyperthermia” and chronic multi‑system burdens (respiratory, cutaneous, ocular, psychosocial). (callea2022extendedoverviewof pages 2-4)

Specific survival/life‑expectancy statistics for EDARADD‑related HED were not identified in the retrieved evidence.

## 12. Treatment
### 12.1 Standard of care (current applications)
For HED generally, management is largely supportive and preventive, focusing on avoiding/mitigating hyperthermia and addressing dental/dermatologic/ocular complications. (higashino2017advancesinthe pages 1-7)

Suggested MAXO terms (for curation):
* Cooling therapy / thermoregulation support
* Dental prosthodontic rehabilitation
* Artificial tears / ocular surface lubrication

### 12.2 Targeted/experimental therapies (latest research and real-world implementations)
Although EDARADD‑related disease itself does not yet have an EDARADD‑specific molecular therapy, targeted replacement therapy has advanced for **XLHED (EDA mutations)** and is mechanistically relevant as pathway restoration.

#### 12.2.1 Postnatal EDA‑A1 replacement protein (EDI200) — clinical trial
ClinicalTrials.gov NCT01775462 (Edimer Pharmaceuticals), Phase 2, male neonates with genetically confirmed XLHED:
* Dosing initiated “between day‑of‑life 2 and 14,” 2 doses/week for 5 total doses; cohorts at **3 mg/kg/dose** and **10 mg/kg/dose**. (NCT01775462 chunk 1)

#### 12.2.2 Prenatal intra‑amniotic EDA replacement — clinical trial and prior compassionate-use evidence
A 2022 review summarizes intra‑amniotic recombinant EDA (Fc‑EDA) administration in three pregnancies (26 weeks; and for twins, 26 and 31 weeks), reporting normal sweating and absence of XLHED symptoms at 14 and 22 months follow‑up. (callea2022extendedoverviewof pages 2-4)

ClinicalTrials.gov NCT04980638 (EDELIFE) — prenatal ER004:
* Phase 2, open‑label, multicenter trial of **intra‑amniotic ER004**, described as “a first‑in‑class signaling protein replacement molecule designed for specific, high affinity binding to the endogenous EDA1 receptor (EDAR).” (NCT04980638 chunk 1)
* Dosing: “Intra‑amniotic route **100 mg/kg of estimated fetal weight per injection. 3 injections, approximately 3 weeks apart starting from gestational week 26**.” (NCT04980638 chunk 1)
* Primary endpoint includes pilocarpine‑induced sweat volume at 6 months. (NCT04980638 chunk 1)

**Relevance to EDARADD:** EDARADD lies downstream of EDAR; thus, EDARADD loss‑of‑function would not be expected to be corrected by EDA ligand replacement, whereas EDARADD dominant‑negative or partial function could hypothetically influence pathway responsiveness. No EDARADD‑targeted clinical trials were identified in the retrieved ClinicalTrials.gov evidence.

## 13. Prevention
Primary prevention is not currently feasible for a Mendelian developmental disorder; however, **genetic counseling**, carrier testing, and prenatal/preimplantation genetic diagnosis are key preventive strategies for at‑risk families. Reviews highlight that identification of causative genes enables “DNA‑based prenatal diagnosis.” (higashino2017advancesinthe pages 1-7)

Secondary/tertiary prevention includes anticipatory guidance to prevent hyperthermia and prompt management of complications. (higashino2017advancesinthe pages 1-7, callea2022extendedoverviewof pages 2-4)

## 14. Other species / natural disease
No EDARADD‑specific natural disease in non‑human species was retrieved in the evidence available for citation in this run.

## 15. Model organisms
No EDARADD‑specific model organism papers were available for citation within the collected evidence set in this run (despite known existence in the broader literature). As such, this section cannot be completed with citable primary sources here.

---

## Key references (with publication dates and URLs)
* Kablan A, Tasdelen E. **2024-06**. *Italian Journal of Pediatrics*. “Novel homozygous frameshift insertion variant… EDARADD…” https://doi.org/10.1186/s13052-024-01681-2 (kablan2024novelhomozygousframeshift pages 1-2)
* Asano N, et al. **2021** (accepted 2021-06-08). *The Journal of Dermatology*. “Characterization of EDARADD gene mutations…” https://doi.org/10.1111/1346-8138.16044 (asano2021characterizationofedaradd pages 1-3, asano2021characterizationofedaradd pages 5-7)
* Kim MJ, et al. **2024-09**. *Orphanet Journal of Rare Diseases*. “Genetic profiling and diagnostic strategies…” https://doi.org/10.1186/s13023-024-03331-6 (kim2024geneticprofilingand pages 1-2)
* Martínez‑Romero MC, et al. **2019-12**. *Orphanet Journal of Rare Diseases*. “EDA, EDAR, EDARADD and WNT10A…” https://doi.org/10.1186/s13023-019-1251-x (martinezromero2019edaedaredaradd pages 1-2)
* Callea M, et al. **2022-09**. *Children*. “Extended overview of ocular phenotype…” https://doi.org/10.3390/children9091357 (callea2022extendedoverviewof pages 2-4)
* ClinicalTrials.gov. NCT01775462 (posted 2013-01-25; last update posted 2016-01-20). EDI200 neonate Phase 2. (NCT01775462 chunk 1)
* ClinicalTrials.gov. NCT04980638 (first posted 2021-07-28; last update posted 2025-04-30). EDELIFE ER004 prenatal Phase 2. (NCT04980638 chunk 1)


References

1. (asano2021characterizationofedaradd pages 1-3): Nobuyuki Asano, Shuichiro Yasuno, Ryota Hayashi, and Yutaka Shimomura. Characterization of edaradd gene mutations responsible for hypohidrotic ectodermal dysplasia. The Journal of Dermatology, 48:1533-1541, Jul 2021. URL: https://doi.org/10.1111/1346-8138.16044, doi:10.1111/1346-8138.16044. This article has 23 citations.

2. (asano2021characterizationofedaradd pages 5-7): Nobuyuki Asano, Shuichiro Yasuno, Ryota Hayashi, and Yutaka Shimomura. Characterization of edaradd gene mutations responsible for hypohidrotic ectodermal dysplasia. The Journal of Dermatology, 48:1533-1541, Jul 2021. URL: https://doi.org/10.1111/1346-8138.16044, doi:10.1111/1346-8138.16044. This article has 23 citations.

3. (callea2022extendedoverviewof pages 2-4): Michele Callea, Stefano Bignotti, Francesco Semeraro, Francisco Cammarata-Scalisi, Jinia El-Feghaly, Antonino Morabito, Vito Romano, and Colin E. Willoughby. Extended overview of ocular phenotype with recent advances in hypohidrotic ectodermal dysplasia. Children, 9:1357, Sep 2022. URL: https://doi.org/10.3390/children9091357, doi:10.3390/children9091357. This article has 9 citations.

4. (kablan2024novelhomozygousframeshift pages 1-2): Ahmet Kablan and Elifcan Tasdelen. Novel homozygous frameshift insertion variant in the last exon of the edaradd causing hypohidrotic ectodermal dysplasia in two siblings: case report and review of the literature. Italian Journal of Pediatrics, Jun 2024. URL: https://doi.org/10.1186/s13052-024-01681-2, doi:10.1186/s13052-024-01681-2. This article has 2 citations and is from a peer-reviewed journal.

5. (martinezromero2019edaedaredaradd pages 1-2): M. C. Martínez-Romero, M. Ballesta-Martínez, V. López‐González, M. J. Sánchez-Soler, A. T. Serrano-Antón, M. Barreda-Sánchez, L. Rodríguez-Peña, M. T. Martínez-Menchon, J. Frías-Iniesta, P. Sánchez‐Pedreño, Pablo Carbonell-Meseguer, G. Glover-López, E. Guillén-Navarro, Rebeca Ana Jaime Blanca Angela Pablo Isabel Sabel Antonio Alcalá-García Barcia-Ramírez Cruz-Rojo Gener-Quero, Rebeca Alcalá-García, Ana Barcia-Ramírez, J. Cruz-Rojo, Blanca Gener-Querol, Á. Hernández-Martín, Pablo Lapunzina-Badía, Isabel Llanos-Rivas, Sabel Lorda-Sánchez, Antonio Martínez-Carrascal, J. Mascaró-Galy, L. Noguera‐Morel, M. A. Rodríguez-González, J. S. del Pozo, Verónica Seidel, A. Torrelo, and M. Trujillo-Tiebas. Eda, edar, edaradd and wnt10a allelic variants in patients with ectodermal derivative impairment in the spanish population. Orphanet Journal of Rare Diseases, Dec 2019. URL: https://doi.org/10.1186/s13023-019-1251-x, doi:10.1186/s13023-019-1251-x. This article has 53 citations and is from a peer-reviewed journal.

6. (higashino2017advancesinthe pages 1-7): Toshihide Higashino, John Y. W. Lee, and John A. McGrath. Advances in the genetic understanding of hypohidrotic ectodermal dysplasia. Expert Opinion on Orphan Drugs, 5:967-975, Nov 2017. URL: https://doi.org/10.1080/21678707.2017.1405806, doi:10.1080/21678707.2017.1405806. This article has 2 citations.

7. (higashino2017advancesinthe pages 12-16): Toshihide Higashino, John Y. W. Lee, and John A. McGrath. Advances in the genetic understanding of hypohidrotic ectodermal dysplasia. Expert Opinion on Orphan Drugs, 5:967-975, Nov 2017. URL: https://doi.org/10.1080/21678707.2017.1405806, doi:10.1080/21678707.2017.1405806. This article has 2 citations.

8. (kim2024geneticprofilingand pages 1-2): Man Jin Kim, Jee-Soo Lee, Seung Won Chae, Sung Im Cho, Jangsup Moon, Jung Min Ko, Jong-Hee Chae, and Moon-Woo Seong. Genetic profiling and diagnostic strategies for patients with ectodermal dysplasias in korea. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03331-6, doi:10.1186/s13023-024-03331-6. This article has 1 citations and is from a peer-reviewed journal.

9. (kim2024geneticprofilingand pages 2-4): Man Jin Kim, Jee-Soo Lee, Seung Won Chae, Sung Im Cho, Jangsup Moon, Jung Min Ko, Jong-Hee Chae, and Moon-Woo Seong. Genetic profiling and diagnostic strategies for patients with ectodermal dysplasias in korea. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03331-6, doi:10.1186/s13023-024-03331-6. This article has 1 citations and is from a peer-reviewed journal.

10. (NCT01775462 chunk 1):  Phase 2 Study to Evaluate Safety, Pharmacokinetics, Immunogenicity and Pharmacodynamics/Efficacy of EDI200 in Male Infants With X-Linked Hypohidrotic Ectodermal Dysplasia (XLHED). Edimer Pharmaceuticals. 2013. ClinicalTrials.gov Identifier: NCT01775462

11. (NCT04980638 chunk 1):  Intraamniotic Administrations of ER004 to Male Subjects With X-linked Hypohidrotic Ectodermal Dysplasia. EspeRare Foundation. 2022. ClinicalTrials.gov Identifier: NCT04980638