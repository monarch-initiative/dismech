---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T17:44:52.892051'
end_time: '2026-04-25T18:11:57.792110'
duration_seconds: 1624.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Central Core Myopathy
  mondo_id: MONDO:0007294
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 68
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Central Core Myopathy
- **MONDO ID:** MONDO:0007294 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Central Core Myopathy** covering all of the
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
- **Disease Name:** Central Core Myopathy
- **MONDO ID:** MONDO:0007294 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Central Core Myopathy** covering all of the
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


## Central Core Myopathy (Central Core Disease): Comprehensive Disease Characteristics Report

### Executive summary
Central core myopathy (also called central core disease, CCD) is a Mendelian congenital myopathy primarily caused by pathogenic variants in **RYR1**, encoding the skeletal-muscle ryanodine receptor (RyR1) Ca2+ release channel required for excitation–contraction coupling (ECC). It is characterized histopathologically by **central “cores”**—longitudinal regions of reduced oxidative enzyme activity and mitochondrial depletion within muscle fibers—and clinically by early-onset hypotonia and predominantly proximal weakness with variable orthopedic complications. A key real-world implication is increased risk of **malignant hyperthermia susceptibility (MHS)**, requiring trigger-free anesthesia and preparedness (dantrolene availability). Recent work (2023–2024) emphasizes trial readiness, patient-reported burden (fatigue, pain, functional limitations), and translational approaches including RyR1 channel stabilizers (Rycals/ARM210) and genome editing proof-of-concept (prime editing). (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease pages 4-6, campuzanodonoso2026molecularbasesof pages 7-9, o’connor2023ryr1relateddiseasesinternational pages 3-4)

---

## 1. Disease Information

### 1.1 Overview (what is the disease?)
CCD is an inherited muscle disorder (congenital myopathy) defined by the presence of **central cores** in muscle biopsy, typically in type I fibers, and associated congenital-myopathy clinical features (hypotonia, delayed motor milestones, proximal weakness). (baba2024anestheticmanagementof pages 1-2)

### 1.2 Key identifiers and ontology mappings
Authoritative identifiers available from retrieved sources:
- **MONDO:** MONDO:0007294 (user-specified target) (artifact-00)
- **OMIM disease:** **117000** (Central core disease) (lillis2012clinicalutilitygene pages 1-2)
- **OMIM gene:** **RYR1 *180901** (lillis2012clinicalutilitygene pages 1-2)
- **MeSH:** **D020512** (“Myopathy, Central Core”) (NCT06157268 chunk 3)

*Not found in retrieved evidence:* explicit Orphanet (ORPHA) numeric identifier and ICD-10/ICD-11 codes.

### 1.3 Synonyms / alternative names
- Central core disease (CCD) (lillis2012clinicalutilitygene pages 1-2)
- Central core myopathy (baba2024anestheticmanagementof pages 1-2)
- Central core myopathy (CCM) (crisafulli2024casereporta pages 1-2)

### 1.4 Evidence provenance
Evidence in this report is derived from aggregated disease resources (e.g., gene cards and reviews), cohort studies, clinical trials registries, and case reports; not from EHR-only sources. (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease pages 4-6, NCT02362425 chunk 1)

| Item category | Data point | Source (authors/year/journal) | Publication date | URL | Evidence notes |
|---|---|---|---|---|---|
| Disease identifier | MONDO:0007294 | User-provided target disease metadata | not stated | not available | Included from the task specification; not independently confirmed in retrieved literature. |
| Disease identifier | OMIM disease: **#117000** (Central core disease) | Lillis et al., 2012, *European Journal of Human Genetics* | 2012-10 | https://doi.org/10.1038/ejhg.2011.179 | Explicit OMIM disease identifier reported in gene card (lillis2012clinicalutilitygene pages 1-2). |
| Gene identifier | OMIM gene: **RYR1 *180901** | Lillis et al., 2012, *European Journal of Human Genetics* | 2012-10 | https://doi.org/10.1038/ejhg.2011.179 | Explicit OMIM gene identifier for the main causal gene (lillis2012clinicalutilitygene pages 1-2). |
| Disease identifier | MeSH: **D020512** (“Myopathy, Central Core”) | ClinicalTrials.gov record NCT06157268 | 2024 | https://clinicaltrials.gov/study/NCT06157268 | Explicit MeSH term/ID listed in trial metadata (NCT06157268 chunk 3). |
| Synonym / naming | **Central core disease (CCD)** | Lillis et al., 2012, *European Journal of Human Genetics* | 2012-10 | https://doi.org/10.1038/ejhg.2011.179 | Gene card uses “Central core disease (CCD) and related phenotypes” (lillis2012clinicalutilitygene pages 1-2). |
| Synonym / naming | **Central core myopathy / CCM** | Crisafulli et al., 2024, *Frontiers in Physiology* | 2024-07 | https://doi.org/10.3389/fphys.2024.1404657 | Case report explicitly uses “Central core myopathy (CCM)” (crisafulli2024casereporta pages 1-2). |
| Epidemiology | Frequency estimate: **1 in 250,000** | Lillis et al., 2012, *European Journal of Human Genetics* | 2012-10 | https://doi.org/10.1038/ejhg.2011.179 | Regional study in north of England cited as CCD frequency estimate (lillis2012clinicalutilitygene pages 1-2, lillis2012clinicalutilitygene pages 2-3). |
| Epidemiology | Prevalence estimate: **1–9 per 1,000,000** | Crisafulli et al., 2024, *Frontiers in Physiology* | 2024-07 | https://doi.org/10.3389/fphys.2024.1404657 | Recent case report cites rare-disease prevalence estimate and attributes it to Orphanet (crisafulli2024casereporta pages 1-2). |
| Epidemiology / ascertainment | CCD represented **53% (92/173)** of diagnoses in a 2024 RYR1-RD survey | van de Camp et al., 2024, *Journal of Neuromuscular Diseases* | 2024-08 | https://doi.org/10.3233/jnd-240029 | Reflects distribution within a surveyed RYR1-related disease cohort, not population prevalence (camp2024individualsandfamilies pages 4-5). |
| Inheritance | **Predominantly autosomal dominant**, with less frequent recessive forms | Lillis et al., 2012, *European Journal of Human Genetics* | 2012-10 | https://doi.org/10.1038/ejhg.2011.179 | Gene card states RYR1-associated CCD is mostly dominant but recessive inheritance also occurs (lillis2012clinicalutilitygene pages 1-2). |
| Inheritance | AD in 4 families; AR in 2 families; sporadic cases common | Cotta et al., 2022, *Genes* | 2022-04 | https://doi.org/10.3390/genes13050760 | In 27 Brazilian CCD patients: 11 AD, 3 AR, 13 sporadic; biallelic RYR1 variants in 43% of molecularly analyzed families (cotta2022centralcoredisease pages 2-4, cotta2022centralcoredisease pages 9-10). |
| Inheritance | Autosomal dominant entry in treatment phenotype table; onset neonatal or later infancy | Raga et al., 2024, treatment protocol | 2024 | not available | Protocol table lists central core disease as AD with early-life onset; useful as current summary but protocol/non-final source (raga2024treatmentsforryr1relateddisorders pages 12-13). |
| Hallmark finding | Muscle biopsy hallmark: **well-defined central/eccentric cores** running along longitudinal fiber axis | Lillis et al., 2012, *European Journal of Human Genetics* | 2012-10 | https://doi.org/10.1038/ejhg.2011.179 | Classic histopathologic criterion for CCD diagnosis (lillis2012clinicalutilitygene pages 1-2). |
| Hallmark finding | Cores are **areas devoid of oxidative reaction** with **myofibrillar disorganization and scarce mitochondria** | Cotta et al., 2022, *Genes* | 2022-04 | https://doi.org/10.3390/genes13050760 | Histology in cohort supports mitochondrial depletion/oxidative stain loss as core feature (cotta2022centralcoredisease pages 4-6). |
| Hallmark finding | Clinical pattern: **hypotonia** and **predominantly proximal weakness** | Cotta et al., 2022, *Genes* | 2022-04 | https://doi.org/10.3390/genes13050760 | In cohort, hypotonia common and weakness proximal in 96%; childhood onset in nearly all patients (cotta2022centralcoredisease pages 4-6). |
| Hallmark finding | Orthopedic features: **hip dislocation, scoliosis/kyphoscoliosis, club feet, joint contractures** | Cotta et al., 2022, *Genes*; Raga et al., 2024, protocol | 2022-04; 2024 | https://doi.org/10.3390/genes13050760 | Recurrent musculoskeletal complications across cohort/protocol summaries (cotta2022centralcoredisease pages 4-6, raga2024treatmentsforryr1relateddisorders pages 12-13). |
| Hallmark finding | EMG often myopathic; CK usually normal or near-normal | Cotta et al., 2022, *Genes* | 2022-04 | https://doi.org/10.3390/genes13050760 | EMG myopathic in 88%; CK normal/near-normal in 84% of cohort (cotta2022centralcoredisease pages 4-6). |
| Hallmark finding / imaging | Selective muscle imaging pattern can support RYR1 involvement; e.g., rectus femoris relative sparing vs vasti | Lillis et al., 2012, *European Journal of Human Genetics*; Cotta et al., 2022, *Genes* | 2012-10; 2022-04 | https://doi.org/10.1038/ejhg.2011.179 | MRI pattern described in gene card; cohort figure showed severe vastus lateralis fat replacement with relative rectus femoris preservation (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease media ead0977b). |
| Hallmark association | Increased risk of **malignant hyperthermia susceptibility (MHS)** with RYR1-related CCD | Lillis et al., 2012, *European Journal of Human Genetics*; Baba et al., 2024, *Cureus* | 2012-10; 2024-01 | https://doi.org/10.1038/ejhg.2011.179 | Important disease-defining association for peri-anesthetic management; trigger-free anesthesia recommended (lillis2012clinicalutilitygene pages 4-5, baba2024anestheticmanagementof pages 1-2). |


*Table: This table compiles core disease-level facts for Central Core Myopathy/Disease, including identifiers, naming, epidemiology, inheritance, and hallmark clinical-pathologic findings. It is designed as a compact evidence-backed reference for knowledge-base population.*

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** Germline pathogenic variants in **RYR1** are the major cause of CCD/central core myopathy. (leao2020dominantorrecessive pages 2-3, cotta2022centralcoredisease pages 7-9)

**Rare alternative/phenocopy cause:** Recessive CCD due to **NEB** variants has been reported (gene-card evidence; details not captured in retrieved pages). (lillis2012clinicalutilitygene pages 5-5)

### 2.2 Risk factors
#### Genetic risk factors
- **RYR1 pathogenic variants** (dominant or recessive) are causal. Many CCD alleles are missense variants, with clustering in the C-terminal hotspot region, but pathogenic variants also occur outside hotspots—supporting whole-gene sequencing strategies. (leao2020dominantorrecessive pages 1-2, cotta2022centralcoredisease pages 7-9)
- MH risk is an important associated risk: RYR1 variants may confer susceptibility to malignant hyperthermia, sometimes independently of overt myopathy severity. (lillis2012clinicalutilitygene pages 4-5, rosenberg2015malignanthyperthermiaa pages 4-5)

#### Environmental/iatrogenic risk factors
- **Exposure to malignant hyperthermia triggers** (volatile anesthetics and succinylcholine) is a major avoidable risk for life-threatening MH episodes in susceptible individuals. (baba2024anestheticmanagementof pages 1-2, rosenberg2015malignanthyperthermiaa pages 4-5)
- **Exertion/heat** can precipitate episodic symptoms (myalgia, rhabdomyolysis) across the RYR1 spectrum. (crisafulli2024casereporta pages 1-2, o’connor2023ryr1relateddiseasesinternational pages 3-4)

### 2.3 Protective factors
No specific genetic protective alleles or proven environmental protective factors were identified in the retrieved CCD-focused evidence. Tailored exercise programs may reduce deconditioning and improve fitness while minimizing rhabdomyolysis risk, but are not “protective” in a causal sense. (crisafulli2024casereporta pages 1-2)

### 2.4 Gene–environment interactions
Best-supported interaction is **RYR1 genotype × anesthetic trigger exposure**, which can precipitate MH through abnormal RyR1-mediated Ca2+ release and hypermetabolism. (rosenberg2015malignanthyperthermiaa pages 4-5)

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum
Across cohorts and surveys, CCD/RYR1-related disease most commonly features:
- Early hypotonia and delayed motor milestones (cotta2022centralcoredisease pages 4-6)
- Predominantly **proximal weakness** (96% in a CCD cohort) with variable distal/axial involvement (cotta2022centralcoredisease pages 4-6)
- Orthopedic complications including congenital hip dislocation, clubfeet, scoliosis/kyphoscoliosis, contractures (cotta2022centralcoredisease pages 4-6, raga2024treatmentsforryr1relateddisorders pages 12-13)
- Myalgia/cramps, fatigue, heat intolerance, exercise limitations—prominent in patient-reported studies across the RYR1 spectrum (o’connor2023ryr1relateddiseasesinternational pages 3-4, camp2024individualsandfamilies pages 13-15)

### 3.2 Frequencies, onset, severity, progression
Quantitative cohort data (example single-center CCD cohort, Brazil, n=27):
- Childhood onset in almost all patients (cotta2022centralcoredisease pages 4-6)
- Hypotonia: 14/23; developmental delay: 15/23 (cotta2022centralcoredisease pages 4-6)
- Proximal weakness: 96%; distal weakness 26%; axial weakness 32% (cotta2022centralcoredisease pages 4-6)
- Deep tendon reflexes absent 45%, decreased 29% (cotta2022centralcoredisease pages 4-6)
- CK normal/near normal in 84% (cotta2022centralcoredisease pages 4-6)
- Facial weakness 8/27 overall, but much higher in biallelic vs monoallelic cases (71% vs 6.7%), suggesting facial weakness as a marker of recessive/biallelic disease in that cohort. (cotta2022centralcoredisease pages 7-9)

Patient-reported disease burden (international RYR1-RD survey summarized at 2022 workshop; n=226):
- Most common self-reported diagnosis: **CCD 53.2%** (o’connor2023ryr1relateddiseasesinternational pages 3-4)
- Ambulation: 64.2% walk unassisted; 11.9% require assistance; 5.8% require wheelchair assistance (o’connor2023ryr1relateddiseasesinternational pages 3-4)
- Disease course perception: 47.1% progressive, 33.9% non-progressive (o’connor2023ryr1relateddiseasesinternational pages 3-4)
- Challenges: 88.9% physical, 63.7% emotional, 58% social (o’connor2023ryr1relateddiseasesinternational pages 3-4)

Patient/caregiver perspective study (2024; n=227) similarly found that only 8% reported no impact on well-being and emphasized fatigue/weakness and higher burden in congenital myopathies compared with MHS. (camp2024individualsandfamilies pages 13-15)

### 3.3 Quality of life impact
Patient-reported evidence shows substantial impact on overall well-being, functional limitations, fatigue and pain, with congenital myopathy phenotypes (including CCD) more affected than MHS-only phenotypes. (camp2024individualsandfamilies pages 13-15)

### 3.4 Suggested HPO terms
| Phenotype (plain language) | Suggested HPO term (name and HP ID if known) | Typical onset/course | Frequency/notes | Key supporting sources (author/year) with URL |
|---|---|---|---|---|
| Congenital/early hypotonia | Hypotonia (HP:0001252) | Usually neonatal or childhood onset; often non-progressive or slowly progressive, though ~47% of surveyed RYR1-RD patients perceived progression | In a CCD cohort, hypotonia in 14/23 (60.9%); central core myopathy typically presents postnatally with hypotonia (cotta2022centralcoredisease pages 4-6, crisafulli2024casereporta pages 1-2, camp2024individualsandfamilies pages 5-7) | Cotta 2022 — https://doi.org/10.3390/genes13050760; Crisafulli 2024 — https://doi.org/10.3389/fphys.2024.1404657; van de Camp 2024 — https://doi.org/10.3233/jnd-240029 |
| Delayed motor milestones / developmental motor delay | Delayed gross motor development (HP:0002194) | Infancy/early childhood onset; may improve in milder cases but can persist | Developmental delay in 15/23 (65.2%) in CCD cohort; many patient testimonials describe early developmental delay (cotta2022centralcoredisease pages 4-6, camp2024individualsandfamilies pages 5-7) | Cotta 2022 — https://doi.org/10.3390/genes13050760; van de Camp 2024 — https://doi.org/10.3233/jnd-240029 |
| Proximal muscle weakness (hip-girdle predominant) | Proximal muscle weakness (HP:0003701) | Usually childhood onset; often mild/non-progressive in dominant CCD, but variable | Proximal weakness in 96% of CCD cohort; classic CCM description emphasizes pelvic-girdle/axial weakness (cotta2022centralcoredisease pages 4-6, crisafulli2024casereporta pages 1-2) | Cotta 2022 — https://doi.org/10.3390/genes13050760; Crisafulli 2024 — https://doi.org/10.3389/fphys.2024.1404657 |
| Axial muscle weakness | Axial muscle weakness (HP:0003323, HPO ID to verify) | Early onset; variable severity | Axial weakness in 32% of CCD cohort; often accompanies proximal pattern (cotta2022centralcoredisease pages 4-6) | Cotta 2022 — https://doi.org/10.3390/genes13050760 |
| Distal muscle weakness | Distal muscle weakness (HP:0002460) | Less common; childhood onset when present | Distal weakness in 26% of CCD cohort (cotta2022centralcoredisease pages 4-6) | Cotta 2022 — https://doi.org/10.3390/genes13050760 |
| Facial weakness | Facial weakness (HP:0000297) | Childhood onset; may help identify biallelic disease | Facial weakness in 8/27 (29.6%) overall; markedly higher in biallelic vs monoallelic CCD, 71.0% vs 6.7% (cotta2022centralcoredisease pages 7-9, cotta2022centralcoredisease pages 9-10) | Cotta 2022 — https://doi.org/10.3390/genes13050760 |
| Ptosis | Ptosis (HP:0000508) | Uncommon; variable onset | Rare in CCD cohort: 2/28 (7.1%); no ophthalmoplegia reported in that cohort (cotta2022centralcoredisease pages 4-6) | Cotta 2022 — https://doi.org/10.3390/genes13050760 |
| Reduced/absent reflexes | Areflexia (HP:0001284) / Hyporeflexia (HP:0001265) | Chronic; accompanies weakness | Deep tendon reflexes absent in 45% and decreased in 29% of CCD cohort (cotta2022centralcoredisease pages 4-6) | Cotta 2022 — https://doi.org/10.3390/genes13050760 |
| Myalgia / muscle pain | Myalgia (HP:0003326) | Can occur from childhood through adulthood; may worsen with exertion | Common in broader RYR1-RD survey; CCM case literature notes exertional myalgia; O’Connor workshop lists myalgia among prominent symptoms (crisafulli2024casereporta pages 1-2, camp2024individualsandfamilies pages 13-15, o’connor2023ryr1relateddiseasesinternational pages 3-4) | Crisafulli 2024 — https://doi.org/10.3389/fphys.2024.1404657; van de Camp 2024 — https://doi.org/10.3233/jnd-240029; O’Connor 2023 — https://doi.org/10.3233/jnd-221609 |
| Fatigue / easy fatigability | Fatigability (HP:0012378, HPO ID to verify) | Chronic across lifespan; major contributor to quality-of-life burden | Fatigue is a key symptom in RYR1-RD surveys; only 8% reported no impact on well-being; fatigue/pain more pronounced in congenital myopathies including CCD (camp2024individualsandfamilies pages 13-15, camp2024individualsandfamilies pages 1-3) | van de Camp 2024 — https://doi.org/10.3233/jnd-240029 |
| Exercise intolerance | Exercise intolerance (HP:0003546) | Often lifelong; may trigger myalgia/rhabdomyolysis | Survey respondents reported difficulty walking/running and benefit from carefully selected activity; exercise-induced symptoms recognized in CCM (o’connor2023ryr1relateddiseasesinternational pages 3-4, crisafulli2024casereporta pages 1-2) | O’Connor 2023 — https://doi.org/10.3233/jnd-221609; Crisafulli 2024 — https://doi.org/10.3389/fphys.2024.1404657 |
| Rhabdomyolysis risk with exertion | Rhabdomyolysis (HP:0003201) | Episodic; may be triggered by exercise/heat | Recognized complication/risk in CCM; case report highlights concern for exercise-induced rhabdomyolysis and myalgia (crisafulli2024casereporta pages 1-2) | Crisafulli 2024 — https://doi.org/10.3389/fphys.2024.1404657 |
| HyperCKemia / elevated creatine kinase | Elevated circulating creatine kinase concentration (HP:0003236) | Intermittent or mild; not universal | CK is usually normal or near-normal in classic CCD (84% in Cotta cohort), but hyperCKemia is reported in some CCM patients (cotta2022centralcoredisease pages 4-6, crisafulli2024casereporta pages 1-2) | Cotta 2022 — https://doi.org/10.3390/genes13050760; Crisafulli 2024 — https://doi.org/10.3389/fphys.2024.1404657 |
| Scoliosis / kyphoscoliosis | Scoliosis (HP:0002650) / Kyphoscoliosis (HP:0002751) | May emerge in childhood/adolescence; chronic orthopedic complication | Frequently reported across CCD/RYR1-RD summaries and surveys; included among orthopedic complications in workshop and protocol summaries (o’connor2023ryr1relateddiseasesinternational pages 3-4, raga2024treatmentsforryr1relateddisorders pages 12-13) | O’Connor 2023 — https://doi.org/10.3233/jnd-221609; Raga 2024 — not provided in evidence text |
| Congenital hip dislocation | Congenital hip dislocation (HP:0001385, HPO ID to verify) | Congenital | In CCD cohort, hip dislocation in 5/25 (20%); workshop survey also notes hip dislocation among frequent problems (cotta2022centralcoredisease pages 4-6, o’connor2023ryr1relateddiseasesinternational pages 3-4) | Cotta 2022 — https://doi.org/10.3390/genes13050760; O’Connor 2023 — https://doi.org/10.3233/jnd-221609 |
| Club feet / foot deformity | Talipes equinovarus (HP:0001762) / Foot deformity (HP:0001760) | Congenital or early childhood | Club feet in 4/26 (15.4%) in CCD cohort; foot deformities also listed in phenotype summaries (cotta2022centralcoredisease pages 4-6, raga2024treatmentsforryr1relateddisorders pages 12-13) | Cotta 2022 — https://doi.org/10.3390/genes13050760; Raga 2024 — not provided in evidence text |
| Joint contractures / stiff joints | Joint contracture (HP:0001371) | Congenital or progressive over time | Stiff joints were frequent in workshop survey; contractures appear in RYR1-RD phenotype tables (o’connor2023ryr1relateddiseasesinternational pages 3-4, raga2024treatmentsforryr1relateddisorders pages 12-13) | O’Connor 2023 — https://doi.org/10.3233/jnd-221609; Raga 2024 — not provided in evidence text |
| Respiratory involvement / breathing difficulty | Respiratory insufficiency due to muscle weakness (HP:0002747, HPO ID to verify) | Usually neonatal in severe cases or later with more severe disability | Severe neonatal respiratory involvement in 2/17 (11.8%) in CCD cohort; breathing difficulties more frequent in full-time wheelchair users in survey data (cotta2022centralcoredisease pages 4-6, camp2024individualsandfamilies pages 5-7) | Cotta 2022 — https://doi.org/10.3390/genes13050760; van de Camp 2024 — https://doi.org/10.3233/jnd-240029 |
| Bulbar/feeding problems | Dysphagia (HP:0002015) / Feeding difficulties (HP:0011968, HPO ID to verify) | Early onset in more severe cases | Bulbar symptoms in 3/15 (20%) in CCD cohort; feeding difficulties noted in RYR1 phenotype summaries (cotta2022centralcoredisease pages 4-6, raga2024treatmentsforryr1relateddisorders pages 13-15) | Cotta 2022 — https://doi.org/10.3390/genes13050760; Raga 2024 — not provided in evidence text |
| Heat intolerance / muscle tightness-cramping | Heat intolerance (HP:0002046, HPO ID to verify) / Muscle cramp (HP:0003394) | Episodic; often exertion/heat related | Workshop survey highlighted heat intolerance, muscle tightness/cramping among frequent symptoms (o’connor2023ryr1relateddiseasesinternational pages 3-4) | O’Connor 2023 — https://doi.org/10.3233/jnd-221609 |
| Ambulation impairment / wheelchair dependence | Abnormality of gait (HP:0001288) / Wheelchair dependence (HP:0002495, HPO ID to verify) | Variable progression; severity tracks inheritance and symptom burden | In 2024 survey: 65% walked unassisted, 12% with assistance, 6% required wheelchair assistance, 17% full-time wheelchair; AR/de novo cases had higher full-time wheelchair use (30.5% and 38% vs 5%) (camp2024individualsandfamilies pages 4-5, camp2024individualsandfamilies pages 5-7) | van de Camp 2024 — https://doi.org/10.3233/jnd-240029 |
| Perceived disease progression | Progressive muscle weakness (HP:0003325, HPO ID to verify) | Variable; some stable, some progressive | 47% of RYR1-RD respondents considered symptoms progressive and 34% stable; classic dominant CCD often described as mild/non-progressive, so progression is heterogeneous (camp2024individualsandfamilies pages 5-7, o’connor2023ryr1relateddiseasesinternational pages 3-4, cotta2022centralcoredisease pages 9-10) | van de Camp 2024 — https://doi.org/10.3233/jnd-240029; O’Connor 2023 — https://doi.org/10.3233/jnd-221609; Cotta 2022 — https://doi.org/10.3390/genes13050760 |


*Table: This table maps major clinical features reported for central core disease/myopathy to suggested HPO terms, with onset/course and frequency notes drawn from cohort and survey evidence. It is useful for structured phenotype annotation and knowledge-base population.*

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **RYR1** is the principal causal gene for CCD/central core myopathy. (leao2020dominantorrecessive pages 2-3, cotta2022centralcoredisease pages 7-9)
- **NEB**: rare recessive CCD reported (limited details in retrieved evidence). (lillis2012clinicalutilitygene pages 5-5)

### 4.2 Pathogenic variant classes, hotspots, and example alleles
In RYR1-related CCD cohorts, the variant spectrum is predominantly missense, with additional truncating/intronic variants:
- In one Brazilian cohort, 22/23 variants were missense and 1 was frameshift (leao2020dominantorrecessive pages 2-3)
- In another CCD cohort, 16/18 variants were missense, 1 nonsense, 1 intronic (cotta2022centralcoredisease pages 7-9)

Hotspots/domain trends:
- CCD alleles often cluster in a C-terminal “D3” hotspot region, while MH alleles are commonly in N-terminal/central hotspots, although overlap occurs and variants outside hotspots exist. (leao2020dominantorrecessive pages 1-2, cotta2022centralcoredisease pages 9-10)

Monoallelic vs biallelic inheritance:
- Biallelic (recessive/compound heterozygous) disease can represent a substantial fraction of cases in some series (e.g., 6/14 families biallelic in one cohort). (cotta2022centralcoredisease pages 7-9)

### 4.3 Functional consequences (mechanistic genotype → phenotype)
- MH is frequently described as **gain-of-function** (hypersensitive RyR1 with excessive SR Ca2+ release). (schartner2019abnormalexcitationcontractioncoupling pages 4-6)
- CCD is often described as **loss-of-function / ECC uncoupling** with reduced depolarization-induced Ca2+ release, though some variants may also produce Ca2+ leak phenotypes. (parker2017functionalcharacterizationof pages 1-3)

### 4.4 Modifier genes / epigenetics
No specific validated modifier genes for CCD were identified in retrieved evidence beyond broader discussions of Ca2+ handling and oxidative stress pathways; the 2023 workshop report emphasizes discovery of modifiers and high-throughput screens for RyR1 and SERCA1 modulators. (o’connor2023ryr1relateddiseasesinternational pages 14-16)

| Gene | Role | Inheritance patterns | Variant classes reported (missense/nonsense/frameshift/intronic) | Example variants (protein change) | Hotspot/domain notes | Evidence notes (e.g., % missense; biallelic rates) | Key sources with publication date and URL |
|---|---|---|---|---|---|---|---|
| **RYR1** | Encodes the skeletal-muscle ryanodine receptor 1, the principal sarcoplasmic reticulum Ca²⁺ release channel required for excitation-contraction coupling and the major causal gene for central core disease/myopathy | Predominantly **autosomal dominant**; also **autosomal recessive**/biallelic; sporadic and de novo cases reported; some alleles linked to malignant hyperthermia susceptibility | Predominantly **missense**; also **nonsense**, **frameshift**, and **intronic** variants reported | p.Arg4861His, p.Arg4861Cys, p.Arg4914Met, p.Arg4914Thr, p.Ala4846Val, p.Gly4897Asp, p.Gln1613Ter, p.Y4864H | Classic hotspot regions D1 (N-terminal), D2 (central), D3/C-terminal; CCD-associated variants predominate in the **C-terminal/transmembrane D3 region**, but pathogenic alleles also occur outside hotspots; some pore/selectivity-filter enrichment described in recessive disease | In Brazilian CCD cohort, **22/23 (95.7%)** detected variants were missense and **1** was frameshift; **7/20 families** had biallelic mutations, corresponding to about **30%** possible AR inheritance (Leão 2020). In another CCD cohort, **16/18 (~89%)** variants were missense, **1** nonsense, **1** intronic; **6/14 families (43%)** had biallelic variants and **8/14 (57%)** monoallelic variants (Cotta 2022). Recessive RYR1 series showed hypomorphic/null alleles enriched in more severe and often non-core phenotypes, while missense variants were enriched in MH/CCD hotspots and pore/selectivity filter regions (Amburgey 2013). Functional studies support both **gain-of-function/MH-type** and **loss-of-function/EC-uncoupling CCD-type** mechanisms depending on variant (Parker 2017) (leao2020dominantorrecessive pages 2-3, leao2020dominantorrecessive pages 1-2, cotta2022centralcoredisease pages 9-10, cotta2022centralcoredisease pages 7-9, amburgey2013genotypephenotypecorrelationsin pages 1-2, amburgey2013genotypephenotypecorrelationsin pages 10-11, parker2017functionalcharacterizationof pages 1-3) | Leão et al. **2020-12**, *Acta Myologica*, https://doi.org/10.36185/2532-1900-030; Cotta et al. **2022-04**, *Genes*, https://doi.org/10.3390/genes13050760; Lillis et al. **2012-10**, *Eur J Hum Genet*, https://doi.org/10.1038/ejhg.2011.179; Amburgey et al. **2013-08**, *Orphanet J Rare Dis*, https://doi.org/10.1186/1750-1172-8-117; Parker et al. **2017-05**, *J Neuromuscul Dis*, https://doi.org/10.3233/jnd-170210; Cacheux et al. **2015-11**, *J Neuromuscul Dis*, https://doi.org/10.3233/jnd-150073 |
| **NEB** | Encodes nebulin, a giant sarcomeric thin-filament protein; rarely implicated in recessive core myopathy/central core-like disease rather than classic RYR1-related CCD | **Autosomal recessive** reported | Not specified in retrieved evidence for CCD-specific cases | Not specified in retrieved evidence | Not specified in retrieved evidence | Mentioned in the CCD gene card as at least one report of **recessive central core disease due to nebulin variants**; however, variant-level details, frequencies, and domain mapping were not available in the retrieved evidence. This supports NEB as a rare alternative/phenocopy gene rather than the main CCD gene (lillis2012clinicalutilitygene pages 5-5) | Lillis et al. **2012-10**, *Eur J Hum Genet*, https://doi.org/10.1038/ejhg.2011.179 |


*Table: This table summarizes the main genetic and molecular evidence for central core disease/myopathy, emphasizing RYR1 as the principal causal gene, the distribution of inheritance patterns, reported variant classes, representative alleles, and hotspot/domain information. It is useful for quickly mapping genotype architecture and evidence strength across key foundational studies.*

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle contributors
CCD is primarily genetic; major clinically actionable environmental exposures relate to **anesthetic triggers** of MH and to exertional/heat stress that may precipitate myalgia or rhabdomyolysis in some RYR1 phenotypes. (rosenberg2015malignanthyperthermiaa pages 4-5, crisafulli2024casereporta pages 1-2)

### 5.2 Infectious agents
Not applicable as a primary etiology based on retrieved evidence.

---

## 6. Mechanism / Pathophysiology

### 6.1 Core mechanistic concept: ECC and Ca2+ dysregulation
RyR1 mediates SR Ca2+ release during skeletal muscle ECC. RYR1 variants can cause:
- **Excess Ca2+ release/leak (MH-type gain-of-function):** hypersensitivity to triggers → uncontrolled Ca2+ release → increased contractile activity and hypermetabolism; SERCA is unable to resequester Ca2+ adequately, increasing ATP consumption and heat. (rosenberg2015malignanthyperthermiaa pages 4-5)
- **Reduced Ca2+ release / ECC uncoupling (CCD-type loss-of-function):** reduced depolarization-induced Ca2+ release and impaired contraction. (parker2017functionalcharacterizationof pages 1-3)

### 6.2 SOICR (store overload-induced Ca2+ release)
A mechanistic study showed that multiple RyR1 mutations associated with MH and CCD reduce the threshold for **SOICR**, promoting spontaneous SR Ca2+ release and contracture; dantrolene suppresses SOICR in this model system. (chen2017reducedthresholdfor pages 1-3)

### 6.3 SOCE and Ca2+ entry pathways
Reviews describe involvement of store-operated Ca2+ entry (STIM1–ORAI1) and other Ca2+ entry pathways in MH-susceptible muscle, linking RyR1 dysfunction to sustained Ca2+ dysregulation. (rosenberg2015malignanthyperthermiaa pages 4-5, schartner2019abnormalexcitationcontractioncoupling pages 1-2)

### 6.4 Mitochondrial depletion and core pathology
Core lesions show reduced oxidative activity and scarce mitochondria in biopsies, consistent with downstream mitochondrial damage/dysfunction. Mechanistic reviews outline feed-forward loops where Ca2+ leak and oxidative stress (including RyR1 post-translational modifications and FKBP12/calstabin dissociation) promote cytosolic Ca2+ overload, proteolysis, mitochondrial dysfunction and cell death. (cotta2022centralcoredisease pages 4-6, campuzanodonoso2026molecularbasesof pages 7-9)

### 6.5 Suggested ontology terms
- **GO Biological Process (examples to annotate; IDs to verify):** excitation–contraction coupling; sarcoplasmic reticulum calcium ion release; regulation of cytosolic calcium ion concentration; response to oxidative stress; mitochondrial organization.
- **GO Cellular Component (examples; IDs to verify):** sarcoplasmic reticulum membrane; triad; ryanodine receptor complex; mitochondrion.
- **CL Cell types (examples; IDs to verify):** skeletal muscle fiber (type I), skeletal muscle cell/myofiber.

---

## 7. Anatomical Structures Affected

### 7.1 Primary organs/systems
- **Skeletal muscle system** (primary), especially muscles with selective involvement patterns on imaging (e.g., thigh/lower limb muscles) (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease media ead0977b)

### 7.2 Tissue/cell level
- Skeletal muscle fibers, particularly type I fibers with core lesions. (baba2024anestheticmanagementof pages 1-2)

### 7.3 Subcellular level
- **Triad/ECC machinery** (T-tubule/SR junction including DHPR–RyR1 coupling) and **mitochondria** (core-associated depletion/dysfunction). (schartner2019abnormalexcitationcontractioncoupling pages 1-2, cotta2022centralcoredisease pages 4-6)

### 7.4 Localization (imaging-guided)
Selective muscle involvement patterns (e.g., relative rectus femoris sparing compared with vasti) can guide biopsy and support RYR1 involvement. (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease media ead0977b)

---

## 8. Temporal Development

### 8.1 Onset
Typically **congenital/neonatal or childhood onset**; adult recognition can occur, especially with mild cases and delayed diagnosis. (cotta2022centralcoredisease pages 4-6, o’connor2023ryr1relateddiseasesinternational pages 3-4)

### 8.2 Progression
Often described as non-progressive or slowly progressive in classic dominant CCD, but patient-reported data show heterogeneity, with ~47% perceiving progression. (o’connor2023ryr1relateddiseasesinternational pages 3-4, camp2024individualsandfamilies pages 5-7)

### 8.3 Critical periods
Peri-anesthesia exposure to MH-triggering agents represents a critical risk period. (rosenberg2015malignanthyperthermiaa pages 4-5)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
Frequency estimates reported:
- Regional CCD frequency estimate: **1 in 250,000** (north of England study cited in gene card). (lillis2012clinicalutilitygene pages 1-2)
- Central core myopathy prevalence estimate cited in 2024 case report: **1–9 per 1,000,000**. (crisafulli2024casereporta pages 1-2)

Related RYR1/MH population genetics context in gene card:
- Carrier frequency for heterozygous RYR1 mutations in Japan estimated as high as **1 in 2,000** (lillis2012clinicalutilitygene pages 2-3)
- Allelic MHS trait estimated 1 in 3,000–10,000; clinical MH reaction prevalence 1 in 60,000–100,000 (gene card summary). (lillis2012clinicalutilitygene pages 2-3)

### 9.2 Inheritance patterns
- Predominantly autosomal dominant, with recessive/biallelic cases increasingly recognized. (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease pages 7-9)

Survey-reported inheritance across RYR1-RD (not population-based): autosomal dominant 27.0%, autosomal recessive 26.1%, de novo 9.3%, unknown 32.7%. (o’connor2023ryr1relateddiseasesinternational pages 3-4)

### 9.3 Demographics
In a 2024 survey cohort, ages ranged 0–85 years, mean 37±21, with 143 females and 84 males. (camp2024individualsandfamilies pages 4-5)

---

## 10. Diagnostics

### 10.1 Clinical tests
- CK: usually normal/near-normal in classic CCD cohorts (84%), though may be elevated in broader RYR1 phenotypes. (cotta2022centralcoredisease pages 4-6)
- EMG: myopathic pattern common (88% in one cohort). (cotta2022centralcoredisease pages 4-6)

### 10.2 Imaging
Characteristic MRI pattern can be highly suggestive of RYR1 involvement and can be used to guide biopsy. (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease media ead0977b)

### 10.3 Biopsy
Core lesions with oxidative enzyme depletion are hallmark findings; biopsy processing includes oxidative stains (SDH/COX/NADH) and routine histology. (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease pages 2-4)

### 10.4 Genetic testing
Gene card recommends sequencing the entire RYR1 gene; modern real-world practice often uses neuromuscular NGS panels and broad exome panels with ACMG classification and segregation confirmation. (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease pages 2-4)

### 10.5 Malignant hyperthermia testing
IVCT/CHCT remains a diagnostic standard but is invasive and limited to specialized centers; DNA testing is increasingly used but challenged by variant interpretation and coverage gaps. (rosenberg2015malignanthyperthermiaa pages 6-8)

| Modality/test | What it shows in CCD | Implementation details (e.g., biopsy stains, MRI pattern, EMG yield) | Distinguishing value/differential notes | Supporting sources with URL and publication date |
|---|---|---|---|---|
| Muscle biopsy (light microscopy) | Hallmark **central cores**: well-defined single or multiple central/eccentric core lesions extending longitudinally in muscle fibers; areas correspond to myofibrillar disorganization | Recommended after specialist clinical assessment; biopsy can be targeted using imaging. In the Brazilian CCD cohort, biopsies were processed from frozen muscle with H&E, modified Gomori trichrome, PAS ± diastase, Oil-red-O, myosin ATPase, acid phosphatase, nonspecific esterase, and oxidative stains. All examined patients showed core lesions/areas devoid of oxidative reaction (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease pages 2-4, cotta2022centralcoredisease pages 4-6) | Helps distinguish CCD from other congenital myopathies, but cores/minicores are **not fully specific** and can also occur in MYH7, ACTA1, DNM2, and NEB-related disease; therefore pathology must be integrated with genotype and imaging (lillis2012clinicalutilitygene pages 3-4) | Lillis et al. *Eur J Hum Genet* (2012-10), https://doi.org/10.1038/ejhg.2011.179; Cotta et al. *Genes* (2022-04), https://doi.org/10.3390/genes13050760 (lillis2012clinicalutilitygene pages 1-2, lillis2012clinicalutilitygene pages 3-4, cotta2022centralcoredisease pages 2-4, cotta2022centralcoredisease pages 4-6) |
| Oxidative/mitochondrial histochemistry | Core regions are **devoid of oxidative enzyme activity** with **scarce mitochondria/mitochondrial depletion** | Stains used in real-world workflows include SDH, COX, and NADH; Cotta et al. reported that biopsy areas lacked oxidative reaction and corresponded to myofibrillar disorganization with scarce mitochondria; figure evidence showed round core structures and EM myofibrillar disorganization (cotta2022centralcoredisease pages 2-4, cotta2022centralcoredisease media ead0977b) | Useful for distinguishing CCD from nonspecific myopathy and for confirming that the lesion reflects oxidative/mitochondrial depletion rather than inflammatory necrosis; however, similar oxidative abnormalities may be seen in related core myopathies, so correlation with genetics is required | Cotta et al. *Genes* (2022-04), https://doi.org/10.3390/genes13050760; figure summary from same source (cotta2022centralcoredisease pages 2-4, cotta2022centralcoredisease media ead0977b) |
| Electron microscopy (when performed) | Ultrastructural confirmation of cores and myofibrillar disorganization | Used as adjunct pathology; Cotta figure summary reported biopsy plus electron microscopy demonstrating characteristic round core structures and myofibrillar disorganization (cotta2022centralcoredisease media ead0977b) | Adds specificity when light microscopy is equivocal; helps separate structured cores from multiminicores/other ultrastructural congenital myopathies | Cotta et al. *Genes* (2022-04), https://doi.org/10.3390/genes13050760 (cotta2022centralcoredisease media ead0977b) |
| Muscle MRI / CT pattern | Selective pattern of fatty replacement supporting **RYR1 involvement**; classic relative sparing of **rectus femoris** compared with vasti | Lillis gene card describes a characteristic MRI pattern: sparing of rectus femoris vs vasti, adductor longus vs adductor magnus, gracilis vs sartorius; in lower leg, greater peroneal involvement than tibialis anterior and soleus more than gastrocnemii. Cotta cohort used T1 axial MRI or CT to guide biopsy; when vastus lateralis showed fatty replacement, rectus femoris was chosen for biopsy. Figure summary showed severe vastus lateralis fat replacement with relative rectus femoris preservation (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease pages 2-4, cotta2022centralcoredisease media ead0977b) | Particularly valuable when biopsy is nonspecific; may be **more indicative of RYR1 involvement than biopsy** in some cases and helps differentiate RYR1-related core myopathy from other congenital myopathies with different selective involvement patterns (lillis2012clinicalutilitygene pages 1-2) | Lillis et al. *Eur J Hum Genet* (2012-10), https://doi.org/10.1038/ejhg.2011.179; Cotta et al. *Genes* (2022-04), https://doi.org/10.3390/genes13050760 (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease pages 2-4, cotta2022centralcoredisease media ead0977b) |
| Electromyography (EMG) | Usually a **myopathic pattern** supportive of congenital myopathy | In the Cotta cohort, EMG showed a myopathic pattern or myopathic motor unit potentials in **88%** of patients (21/24) (cotta2022centralcoredisease pages 4-6) | Supports myopathy over neuropathy/SMA, but is not disease-specific; useful in differential diagnosis when combined with biopsy and genetics | Cotta et al. *Genes* (2022-04), https://doi.org/10.3390/genes13050760 (cotta2022centralcoredisease pages 4-6) |
| Serum creatine kinase (CK) | Often **normal or near-normal** in CCD; occasionally elevated | In Cotta et al., CK was normal or near-normal in **84%** (22/26), with one marked elevation; ancillary labs in clinical workflows also included aldolase (cotta2022centralcoredisease pages 4-6, cotta2022centralcoredisease pages 2-4) | Near-normal CK helps distinguish CCD from many muscular dystrophies with consistently higher CK; however, episodic hyperCKemia/rhabdomyolysis can occur in the broader RYR1 spectrum | Cotta et al. *Genes* (2022-04), https://doi.org/10.3390/genes13050760 (cotta2022centralcoredisease pages 4-6, cotta2022centralcoredisease pages 2-4) |
| Genetic testing: single-gene/full-gene RYR1 sequencing | Identifies causal **RYR1** variants; can confirm dominant monoallelic or recessive biallelic disease | Lillis recommends sequencing the **entire RYR1 gene** to resolve diagnosis because hotspot-only approaches can miss variants; definitive diagnosis requires one dominant pathogenic variant or two recessive variants in trans. Sanger sequencing was the standard in 2012, with confirmation of variants on repeat analysis and use of cDNA when needed (lillis2012clinicalutilitygene pages 4-5, lillis2012clinicalutilitygene pages 1-2) | Crucial because pathology can be atypical or overlap with other congenital myopathies; enables family testing, inheritance clarification, MH counseling, and predictive/prenatal testing | Lillis et al. *Eur J Hum Genet* (2012-10), https://doi.org/10.1038/ejhg.2011.179 (lillis2012clinicalutilitygene pages 4-5, lillis2012clinicalutilitygene pages 1-2) |
| Genetic testing: NGS neuromuscular panel | Broad detection of RYR1 and differential congenital myopathy genes | In Cotta et al., first-line testing used a customized **95-gene neuromuscular NGS panel** including RYR1, followed by broader exome capture when needed; variant filtering used gnomAD/ExAC/1000 Genomes/ClinVar/HGMD/LOVD and ACMG criteria, with Sanger confirmation and segregation (cotta2022centralcoredisease pages 2-4) | Improves yield because CCD can mimic other congenital myopathies and because pathogenic RYR1 variants can lie outside classic hotspots; also helps rule in/out other genetic differentials | Cotta et al. *Genes* (2022-04), https://doi.org/10.3390/genes13050760 (cotta2022centralcoredisease pages 2-4) |
| Genetic testing: exome / broad exome panel | Captures atypical or non-hotspot RYR1 variants and alternative diagnoses | Cotta et al. used **TruSight One Expanded** (>6700 genes) after panel testing; Lillis anticipated increasing roles for NGS, array CGH, and MLPA for larger deletions/duplications/rearrangements (cotta2022centralcoredisease pages 2-4, lillis2012clinicalutilitygene pages 1-2) | Especially useful when biopsy is nonspecific, phenotype is broad, or panel testing is negative; helps distinguish CCD from other congenital myopathies with overlapping core pathology | Cotta et al. *Genes* (2022-04), https://doi.org/10.3390/genes13050760; Lillis et al. *Eur J Hum Genet* (2012-10), https://doi.org/10.1038/ejhg.2011.179 (cotta2022centralcoredisease pages 2-4, lillis2012clinicalutilitygene pages 1-2) |
| cDNA analysis / copy-number confirmation | Can reveal variants missed on genomic sequencing and confirm structural calls | Lillis notes some causative variants, often recessive, may not be detectable on genomic sequencing and require **cDNA analysis**; gross deletions/duplications found by NGS should be confirmed with a second technique such as MLPA/array methods (lillis2012clinicalutilitygene pages 1-2) | Important in unresolved suspected CCD with strong clinicopathologic evidence but negative genomic testing | Lillis et al. *Eur J Hum Genet* (2012-10), https://doi.org/10.1038/ejhg.2011.179 (lillis2012clinicalutilitygene pages 1-2) |
| Malignant hyperthermia susceptibility testing (IVCT/CHCT) | Assesses functional susceptibility to MH in CCD/RYR1-variant carriers | Lillis recommends **IVCT** in patients or asymptomatic carriers >16 years when MH risk of the variant is undocumented. Rosenberg review notes IVCT is a diagnostic standard under EMHG/NAMHG protocols but requires surgical biopsy and specialized centers, and can yield false positives/negatives (lillis2012clinicalutilitygene pages 4-5, rosenberg2015malignanthyperthermiaa pages 6-8) | Key differential/risk linkage: separates structural congenital myopathy diagnosis from peri-anesthetic pharmacogenetic susceptibility assessment; important because not all RYR1 variants have established MH risk | Lillis et al. *Eur J Hum Genet* (2012-10), https://doi.org/10.1038/ejhg.2011.179; Rosenberg et al. *Orphanet J Rare Dis* (2015-08), https://doi.org/10.1186/s13023-015-0310-1 (lillis2012clinicalutilitygene pages 4-5, rosenberg2015malignanthyperthermiaa pages 6-8) |
| Perioperative risk-management linkage | Genetic/pathologic diagnosis of CCD triggers **MH precautions** during anesthesia | Baba et al. describe real-world trigger-free anesthesia in CCD: removal of vaporizers, replacement of circuit and soda lime, prolonged machine flush, total intravenous anesthesia, core temperature monitoring, and immediate availability of unopened **dantrolene** vials; masseter neuromuscular monitoring was used because recovery lagged behind adductor pollicis (baba2024anestheticmanagementof pages 1-2, baba2024anestheticmanagementof pages 4-5) | Distinguishes CCD from other congenital myopathies by the need for MH-focused perioperative planning; diagnosis has direct management implications even outside neuromuscular clinics | Baba et al. *Cureus* (2024-01), https://doi.org/10.7759/cureus.52456 (baba2024anestheticmanagementof pages 1-2, baba2024anestheticmanagementof pages 4-5) |
| Differential diagnosis integration (clinicopathologic + imaging + genetics) | Final diagnosis relies on multimodal correlation rather than one test alone | Lillis recommends testing only after specialist clinical, biopsy, and MRI assessment; Cotta integrates EMG, CK, imaging-guided biopsy, and tiered NGS/exome; workshop report highlights broad availability of NGS and expert pathogenicity panels for trial-readiness and care harmonization (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease pages 2-4, o’connor2023ryr1relateddiseasesinternational pages 1-3) | Helps distinguish CCD from multiminicore disease, centronuclear myopathy, congenital fiber-type disproportion, nemaline myopathy, and even neurogenic disorders such as SMA when individual tests are equivocal | Lillis et al. *Eur J Hum Genet* (2012-10), https://doi.org/10.1038/ejhg.2011.179; Cotta et al. *Genes* (2022-04), https://doi.org/10.3390/genes13050760; O’Connor et al. *J Neuromuscul Dis* (2023-01), https://doi.org/10.3233/jnd-221609 (lillis2012clinicalutilitygene pages 1-2, cotta2022centralcoredisease pages 2-4, o’connor2023ryr1relateddiseasesinternational pages 1-3) |


*Table: This table summarizes the main diagnostic modalities used for central core disease/myopathy, what each contributes, and how they help distinguish CCD from overlapping congenital myopathies and malignant hyperthermia susceptibility.*

---

## 11. Outcome / Prognosis

CCD prognosis is variable and dependent on genotype (monoallelic vs biallelic), severity of weakness, respiratory involvement, and orthopedic complications. Survey data show that most individuals remain ambulant, but a meaningful subset requires wheelchair assistance and many perceive progression. (camp2024individualsandfamilies pages 4-5, o’connor2023ryr1relateddiseasesinternational pages 3-4)

Quantitative survival and life expectancy statistics specific to CCD were not found in retrieved evidence.

---

## 12. Treatment

### 12.1 Standard of care and supportive management
- Supportive care including physiotherapy/rehabilitation and orthopedic management is standard; no cure is established. (crisafulli2024casereporta pages 1-2, ziemian2025integrativeapproachesto pages 36-37)

### 12.2 Perioperative management (real-world implementation)
Trigger-free anesthesia and careful neuromuscular monitoring are recommended for CCD patients given MH risk; a 2024 case report provides detailed workstation preparation and monitoring steps and emphasizes immediate dantrolene availability. (baba2024anestheticmanagementof pages 1-2)

### 12.3 Pharmacologic/interventional evidence and trials
- **NAC (antioxidant):** NIH phase II RCT summarized in workshop report; 33 randomized; NAC 30 mg/kg/day for 6 months; did not improve urine 15-F2t isoprostane or 6MWT. ClinicalTrials.gov record NCT02362425 provides trial metadata (completed; results posted 2019-12-24). (o’connor2023ryr1relateddiseasesinternational pages 13-14, NCT02362425 chunk 1)
- **Salbutamol/albuterol:** small pilot and case evidence suggest improved myometry/MRC/FVC in CCD/MmD cohorts and in individual case(s). (raga2024treatmentsforryr1relateddisorders pages 13-15)
- **Rycal S48168 (ARM210):** phase I trial (NCT04141670) summarized by workshop report: 7 participants, 1 month dosing; well tolerated; fatigue scores decreased and shoulder strength trended higher in high-dose group. (o’connor2023ryr1relateddiseasesinternational pages 13-14, NCT04141670 chunk 2)

### 12.4 MAXO suggestions
See treatment artifact below for suggested MAXO/CHEBI mappings.

| Intervention (drug/therapy) | Mechanism/rationale | Evidence type (trial/case report/preclinical) | Key data (dose, duration, sample size, outcomes) | Safety notes | Related ontology term suggestions (MAXO, CHEBI if relevant) | Key sources with publication date, URL, and identifiers (NCT when available) |
|---|---|---|---|---|---|---|
| Trigger-free anesthesia with immediate dantrolene availability | Prevent malignant hyperthermia (MH) in RYR1-related CCD by avoiding volatile anesthetics/succinylcholine and preparing for acute RyR1-mediated hypermetabolic crisis | Real-world case report; guideline-linked perioperative management | 2024 CCD thoracoscopic lung resection case used total intravenous anesthesia; workstation prepared by removing vaporizers, replacing circuit and soda lime, flushing with 10 L/min air for 12 h; unopened dantrolene kept immediately available; uneventful course; masseter neuromuscular monitoring suggested as adjunct because recovery there was slower than adductor pollicis (baba2024anestheticmanagementof pages 1-2, baba2024anestheticmanagementof pages 4-5) | Core safety principle is strict trigger avoidance; prolonged effects of non-depolarizing relaxants may occur; dantrolene should be readily available (baba2024anestheticmanagementof pages 1-2) | MAXO: trigger avoidance during anesthesia; perioperative monitoring; emergency dantrolene administration. CHEBI: dantrolene (CHEBI ID to verify), succinylcholine (CHEBI ID to verify), volatile anesthetic agent (CHEBI ID to verify) | Baba et al., 2024-01, https://doi.org/10.7759/cureus.52456; cites EMHG/OrphanAnesthesia guidance (baba2024anestheticmanagementof pages 1-2, baba2024anestheticmanagementof pages 4-5, baba2024anestheticmanagementof pages 5-5) |
| N-acetylcysteine (NAC) | Antioxidant therapy to reduce oxidative stress/redox imbalance reported in RYR1-related myopathies | Randomized, double-/triple-masked placebo-controlled clinical trial; translational/preclinical rationale | NCT02362425; completed phase 1/2 trial. Enrollment 63 total in registry; workshop summary states 150 screened, 53 entered natural history, 33 randomized 1:1 to NAC vs placebo. Dose: 30 mg/kg/day orally (max 2700 mg/day) for 6 months. Primary endpoints: urine 15-F2t isoprostane and 6MWT. Result: baseline oxidative stress elevated, but NAC did not correct urine 15-F2t isoprostane and did not significantly improve 6MWT; trial did not meet primary efficacy endpoints (o’connor2023ryr1relateddiseasesinternational pages 13-14, NCT02362425 chunk 1) | Reported as well tolerated in workshop summary; lack of efficacy may reflect insufficient muscle target engagement/metabolic degradation rather than clear toxicity (o’connor2023ryr1relateddiseasesinternational pages 13-14, o’connor2023ryr1relateddiseasesinternational pages 11-13) | MAXO: antioxidant therapy; oral administration. CHEBI: N-acetyl-L-cysteine (CHEBI ID to verify) | ClinicalTrials.gov NCT02362425, first results posted 2019-12-24, https://clinicaltrials.gov/study/NCT02362425; workshop synthesis O'Connor et al., 2023-01, https://doi.org/10.3233/jnd-221609 (NCT02362425 chunk 1, o’connor2023ryr1relateddiseasesinternational pages 11-13, o’connor2023ryr1relateddiseasesinternational pages 13-14) |
| Salbutamol | Beta-agonist used to improve muscle strength and pulmonary function in congenital/core myopathies | Small pilot clinical study; protocol/review summary | In children with CCD/MmD (total n=13; 8 CCD, 5 MmD), oral salbutamol 2 mg four times daily, assessed at 3 and 6 months; reported significant increases in myometry, MRC scores, and FVC between baseline and 6 months; some measures improved by 3 months (raga2024treatmentsforryr1relateddisorders pages 13-15) | Described as well tolerated in pilot summary (raga2024treatmentsforryr1relateddisorders pages 4-5) | MAXO: beta-adrenergic agonist therapy; pulmonary function support. CHEBI: salbutamol/albuterol (CHEBI ID to verify) | Raga et al. protocol summary, 2024, URL not available in retrieved record; workshop notes on COMPIS/salbutamol development in O'Connor et al., 2023-01, https://doi.org/10.3233/jnd-221609 (raga2024treatmentsforryr1relateddisorders pages 13-15, raga2024treatmentsforryr1relateddisorders pages 4-5) |
| Albuterol plus aerobic exercise | Beta-agonist plus conditioning/rehab to improve strength, respiratory function, and daily function | Case report; supportive clinical evidence | Case report in CCD used albuterol 2 mg daily for 1 year plus aerobic exercise 20 min three times/week; reported “striking increase in strength” at 6 months with further gains at 1 year, including fine motor development, activity, and speech (raga2024treatmentsforryr1relateddisorders pages 13-15) | No major adverse effects reported in summarized case; one older report noted mild contracture progression in a complex case (not central to 2023-2024 focus) (raga2024treatmentsforryr1relateddisorders pages 13-15) | MAXO: beta-agonist therapy; aerobic exercise therapy; physical therapy. CHEBI: albuterol/salbutamol (CHEBI ID to verify) | Raga et al. protocol summary, 2024, URL not available in retrieved record; supportive recent exercise-tailoring case in Front Physiol 2024 below (raga2024treatmentsforryr1relateddisorders pages 13-15) |
| Tailored mixed aerobic/resistance training with CK/Borg monitoring | Personalized rehabilitation to improve fitness while reducing risk of exertional rhabdomyolysis/myalgia in central core myopathy | 2024 case report | 17-year-old CCM patient underwent preliminary tolerance testing with three 25-min sessions (aerobic, resistance, mixed) at Borg CR-10 intensity level 6; CK checked 36 h later. Training phase: 3 months, 3 sessions/week, mixed aerobic/resistance plus nutrition plan. Outcomes: anaerobic threshold +6.9%, normalized VO2max +15%, muscle mass +1.1 kg, fat mass −1.1 kg; no pain, rhabdomyolysis, or CK increase versus baseline (crisafulli2024casereporta pages 1-2) | Explicitly designed to mitigate exercise-induced rhabdomyolysis risk; authors propose CK/Borg-based dosing as safety tool (crisafulli2024casereporta pages 1-2) | MAXO: physical therapy; resistance exercise; aerobic exercise; nutritional management; laboratory monitoring. CHEBI: creatine kinase as biomarker (CHEBI/LOINC ID to verify) | Crisafulli et al., 2024-07, https://doi.org/10.3389/fphys.2024.1404657 (crisafulli2024casereporta pages 1-2) |
| Rycal S48168 / ARM210 | RyR1 channel stabilizer; binds/stabilizes closed state to reduce pathological SR Ca2+ leak | Phase I open-label dose-escalation trial; ex vivo and structure-guided translational development | NCT04141670; one-month dosing. Workshop summary: 7 participants received 120 mg/day (n=3) or 200 mg/day (n=4). Primary endpoint safety/tolerability. Results: well tolerated; 3 grade ≥2 adverse events deemed unrelated; no serious AEs; dose-dependent PK; fatigue scores decreased and shoulder abduction strength trended higher in high-dose group, though efficacy signals were mixed (o’connor2023ryr1relateddiseasesinternational pages 13-14). Structural work identified ARM210/S48168 binding in Repeat12 domain and cooperative binding with ATP to stabilize closed RyR1 (o’connor2023ryr1relateddiseasesinternational pages 8-10) | Favorable short-term safety/tolerability profile in phase I; efficacy preliminary only (o’connor2023ryr1relateddiseasesinternational pages 14-16, o’connor2023ryr1relateddiseasesinternational pages 13-14) | MAXO: RyR1 stabilizer therapy; clinical trial participation. CHEBI: S48168/ARM210 (CHEBI ID to verify) | ClinicalTrials.gov NCT04141670, https://clinicaltrials.gov/study/NCT04141670; O'Connor et al., 2023-01, https://doi.org/10.3233/jnd-221609; cited EClinicalMedicine 2024 publication in record (NCT04141670 chunk 2, o’connor2023ryr1relateddiseasesinternational pages 14-16, o’connor2023ryr1relateddiseasesinternational pages 13-14) |
| Future gene editing: prime editing of RYR1 | Correct pathogenic RYR1 variants at nucleotide level; precision therapy concept for mutation-defined disease | In vitro human myoblast proof-of-concept; workshop translational update | Godbout et al. reported 59% correction of recessive T4709M RYR1 mutation in human myoblasts via RNA delivery of prime editing components (godbout2023successfulcorrectionby pages 1-3). Workshop report notes prime editing strategy for recurrent T4706M/T4709M with planned/considered delivery approaches including dual AAV, extracellular vesicles, and lipid nanoparticles, and suggests platform utility beyond one variant (o’connor2023ryr1relateddiseasesinternational pages 11-13, o’connor2023ryr1relateddiseasesinternational pages 10-11) | Major current limitation is delivery; mouse primary cells showed lower transfection/editing efficiency than HEK293T systems (o’connor2023ryr1relateddiseasesinternational pages 10-11) | MAXO: genome editing therapy; gene correction therapy. CHEBI: none established/NA | Godbout et al., 2023-12, https://doi.org/10.3390/cells13010031; O'Connor et al., 2023-01, https://doi.org/10.3233/jnd-221609 (o’connor2023ryr1relateddiseasesinternational pages 11-13, o’connor2023ryr1relateddiseasesinternational pages 10-11, godbout2023successfulcorrectionby pages 1-3) |
| Preclinical/experimental modifiers: Rycals broadly, AICAR, pyridostigmine, NAC in models | Aim to reduce Ca2+ leak, improve endurance/fatigue, or reduce oxidative stress | Preclinical studies and protocol summaries | Rycals: stabilize RyR channels and reduce Ca2+ leak (raga2024treatmentsforryr1relateddisorders pages 4-5). AICAR: AMPK activation may improve endurance without exercise (raga2024treatmentsforryr1relateddisorders pages 4-5). Pyridostigmine in mouse models showed modest improvement in grip fatigue and treadmill endurance (raga2024treatmentsforryr1relateddisorders pages 13-15). NAC in zebrafish, mice, and human myotubes reduced oxidative stress and improved survival/muscle function preclinically despite negative human trial (raga2024treatmentsforryr1relateddisorders pages 4-5) | Mostly preclinical or early-stage; not established standard of care for CCD (raga2024treatmentsforryr1relateddisorders pages 4-5, raga2024treatmentsforryr1relateddisorders pages 13-15) | MAXO: experimental small-molecule therapy; AMPK activator therapy; cholinesterase inhibitor therapy. CHEBI: AICAR (CHEBI ID to verify), pyridostigmine (CHEBI ID to verify), N-acetylcysteine (CHEBI ID to verify) | Raga et al. protocol summary, 2024, URL not available in retrieved record; O'Connor et al., 2023-01, https://doi.org/10.3233/jnd-221609 (raga2024treatmentsforryr1relateddisorders pages 4-5, raga2024treatmentsforryr1relateddisorders pages 13-15) |
| Clinical care guidelines and trial-readiness infrastructure | Standardized supportive management and harmonized outcomes/testing to enable safer care and future trials | Workshop/research-network implementation update | Workshop report highlighted comprehensive Clinical Care Guidelines translated into eight languages (www.ryr1.org/ccg), expansion of natural history studies, standardized outcome measures, and patient registries/databases to improve trial readiness and real-world care delivery (o’connor2023ryr1relateddiseasesinternational pages 1-3, o’connor2023ryr1relateddiseasesinternational pages 14-16) | Not a therapy itself, but important systems-level intervention for quality/safety in rare disease care | MAXO: clinical guideline-based care; multidisciplinary care; natural history study participation | O'Connor et al., 2023-01, https://doi.org/10.3233/jnd-221609 (o’connor2023ryr1relateddiseasesinternational pages 14-16, o’connor2023ryr1relateddiseasesinternational pages 1-3) |


*Table: This table summarizes current and emerging treatments, supportive management, and trial activity relevant to central core disease/myopathy, emphasizing 2023-2024 developments and real-world implementation details. It is useful for linking interventions to mechanism, evidence strength, safety, and ontology annotations.*

---

## 13. Prevention

The most evidence-supported preventive strategy is **primary prevention of MH crises** by avoiding triggering anesthetics in individuals with CCD/RYR1 variants and ensuring availability of dantrolene and appropriate perioperative protocols. (baba2024anestheticmanagementof pages 1-2, rosenberg2015malignanthyperthermiaa pages 4-5)

Genetic counseling and cascade testing in families can prevent unrecognized MH risk during anesthesia. (lillis2012clinicalutilitygene pages 4-5)

---

## 14. Other Species / Natural Disease

Direct naturally occurring CCD analogs in companion animals were not retrieved for CCD specifically; however, malignant hyperthermia occurs in multiple species (including pigs), and porcine RyR1 mutation R615C is referenced mechanistically for SOICR enhancement. (chen2017reducedthresholdfor pages 1-3)

---

## 15. Model Organisms

Model systems used for RYR1/CCD mechanism and therapy development include:
- **Mouse models:** RYR1 knock-in MH models (e.g., R2509C) used for therapy testing; inducible muscle-specific RYR1 knockout mice; models for severe recessive RYR1 myopathy. (o’connor2023ryr1relateddiseasesinternational pages 8-10, o’connor2023ryr1relateddiseasesinternational pages 10-11)
- **Zebrafish and C. elegans:** used for large-scale drug screens and modifier discovery. (o’connor2023ryr1relateddiseasesinternational pages 10-11)
- **Cellular/in vitro systems:** HEK293-based RyR1 assays and reconstituted ECC platform; primary human myoblasts/myotubes derived from patient biopsies used for Ca2+ release assays and screening. (o’connor2023ryr1relateddiseasesinternational pages 8-10, cacheux2015functionalcharacterizationof pages 1-3)
- **Human myoblast gene editing:** prime editing correction of RYR1 T4709M in human myoblasts (59% correction). (godbout2023successfulcorrectionby pages 1-3)

---

## Figure evidence (imaging + biopsy)
A cohort figure demonstrates a typical selective muscle imaging pattern and biopsy core findings (fat replacement in vastus lateralis with relative rectus femoris preservation; biopsy/EM images of cores). (cotta2022centralcoredisease media ead0977b)

---

## Recent developments and expert analysis (2023–2024 emphasis)

1) **Patient-centered disease burden and trial readiness:** 2023 workshop and 2024 patient/caregiver studies emphasize fatigue, psychosocial impact, and willingness to participate in trials, supporting patient-driven registry infrastructure and outcome-measure development. (o’connor2023ryr1relateddiseasesinternational pages 3-4, camp2024individualsandfamilies pages 13-15, o’connor2023ryr1relateddiseasesinternational pages 14-16)

2) **Therapeutic pipeline maturation:** completion of early-phase trials (NAC; ARM210/S48168) and design of ongoing trials (e.g., COMPIS salbutamol trial) reflect increasing interventional maturity, with emphasis on standardized functional endpoints (MFM-32, 6MWT, FVC). (o’connor2023ryr1relateddiseasesinternational pages 13-14, o’connor2023ryr1relateddiseasesinternational pages 11-13)

3) **Mechanism-driven therapies:** mechanistic work on Ca2+ leak/SOICR and channel-stabilizing compounds underpins Rycal development and supports exploration of additional RyR1 modulators; dantrolene remains a mechanistically grounded acute therapy for MH and suppresses SOICR in cellular models. (chen2017reducedthresholdfor pages 1-3, o’connor2023ryr1relateddiseasesinternational pages 13-14)

4) **Gene correction proof-of-concept:** prime editing correction in human myoblasts (2023) demonstrates feasibility of precise correction for RYR1 point mutations, with delivery as a major remaining barrier. (godbout2023successfulcorrectionby pages 1-3, o’connor2023ryr1relateddiseasesinternational pages 10-11)

---

## Limitations of retrieved evidence
- Explicit Orphanet (ORPHA) and ICD-10/ICD-11 codes were not identified in retrieved texts.
- CCD-specific mortality/life expectancy data and robust population incidence were not retrieved.
- Some ontology IDs (HPO/GO/CL/CHEBI/MAXO) are suggested where standard, but several require verification against the current ontology releases.



References

1. (lillis2012clinicalutilitygene pages 1-2): Suzanne Lillis, Stephen Abbs, Clemens R Mueller, Francesco Muntoni, and Heinz Jungbluth. Clinical utility gene card for: central core disease. European Journal of Human Genetics, 20:-, Oct 2012. URL: https://doi.org/10.1038/ejhg.2011.179, doi:10.1038/ejhg.2011.179. This article has 10 citations and is from a domain leading peer-reviewed journal.

2. (cotta2022centralcoredisease pages 4-6): Ana Cotta, Lucas Santos Souza, Elmano Carvalho, Leticia Nogueira Feitosa, Antonio Cunha, Monica Machado Navarro, Jaquelin Valicek, Miriam Melo Menezes, Simone Vilela Nunes Neves, Rafael Xavier-Neto, Antonio Pedro Vargas, Reinaldo Issao Takata, Julia Filardi Paim, and Mariz Vainzof. Central core disease: facial weakness differentiating biallelic from monoallelic forms. Genes, 13:760, Apr 2022. URL: https://doi.org/10.3390/genes13050760, doi:10.3390/genes13050760. This article has 6 citations.

3. (campuzanodonoso2026molecularbasesof pages 7-9): Martín Campuzano-Donoso, Claudia Reytor-González, Melannie Toral-Noristz, Yamilia González, and Daniel Simancas-Racines. Molecular bases of myopathies and their impact on clinical practice: advances and future perspectives. International Journal of Molecular Sciences, 27:1392, Jan 2026. URL: https://doi.org/10.3390/ijms27031392, doi:10.3390/ijms27031392. This article has 1 citations.

4. (o’connor2023ryr1relateddiseasesinternational pages 3-4): Thomas N. O’Connor, L. R. van den Bersselaar, Y. Chen, Stefan Nicolau, Brentney Simon, Andrew Huseth, Joshua J. Todd, Filip Van Petegem, Anna Sarkozy, Michael F. Goldberg, N. Voermans, Robert T. Dirksen, Leslie Johann Carsten Oliver Razvan Robert James Michael Biesecker Böhm Bönnemann Clarke Cornea Dirksen Dow, Leslie Biesecker, Johann Böhm, Carsten G Bönnemann, Oliver Clarke, Razvan Cornea, Robert T. Dirksen, James Dowling, Michael F. Goldberg, Susan Hamilton, Drew Huseth, H. Jungbluth, Tokunbor A. Lawal, A. Marks, Isabelle Marty, L. Medne, Eva Michael, P. Mohassel, Takashi Murayama, S. Riazi, Anna Sarkozy, Brentney Simon, Joshua J. Todd, Jacques Tremblay, S. Treves, L. R. van den Bersselaar, Filip Van Petegem, N. Voermans, and N. Witting. Ryr-1-related diseases international research workshop: from mechanisms to treatments pittsburgh, pa, u.s.a., 21-22 july 2022. Journal of Neuromuscular Diseases, 10:135-154, Jan 2023. URL: https://doi.org/10.3233/jnd-221609, doi:10.3233/jnd-221609. This article has 10 citations and is from a peer-reviewed journal.

5. (baba2024anestheticmanagementof pages 1-2): Hiroko Baba, Ryo Wakabayashi, Hiroki Ichiyanagi, Aki Suzuki, and Nobukazu Sato. Anesthetic management of a patient with central core disease undergoing thoracoscopic lung resection: the importance of neuromuscular monitoring at the masseter muscle. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.52456, doi:10.7759/cureus.52456. This article has 1 citations.

6. (NCT06157268 chunk 3):  The Natural History and Muscle Fatigability of Patients With Congenital Myopathies.. Radboud University Medical Center. 2024. ClinicalTrials.gov Identifier: NCT06157268

7. (crisafulli2024casereporta pages 1-2): Oscar Crisafulli, Jessica Lacetera, Giorgio Bottoni, Angela Berardinelli, Luca Grattarola, Martina Veltroni, Stefano Acquadro, Massimo Negro, Emanuela Lavaselli, and Giuseppe D’Antona. Case report: a creatine kinase-borg scale values-based approach to tailor physical training in a central core myopathy patient. Frontiers in Physiology, Jul 2024. URL: https://doi.org/10.3389/fphys.2024.1404657, doi:10.3389/fphys.2024.1404657. This article has 7 citations.

8. (NCT02362425 chunk 1):  Antioxidant Therapy in RYR1-Related Congenital Myopathy. National Institute of Nursing Research (NINR). 2015. ClinicalTrials.gov Identifier: NCT02362425

9. (lillis2012clinicalutilitygene pages 2-3): Suzanne Lillis, Stephen Abbs, Clemens R Mueller, Francesco Muntoni, and Heinz Jungbluth. Clinical utility gene card for: central core disease. European Journal of Human Genetics, 20:-, Oct 2012. URL: https://doi.org/10.1038/ejhg.2011.179, doi:10.1038/ejhg.2011.179. This article has 10 citations and is from a domain leading peer-reviewed journal.

10. (camp2024individualsandfamilies pages 4-5): Sanne A.J.H. van de Camp, Lizan Stinissen, Andrew Huseth, Brentney Simon, Jennifer Ryan, Anna Sarkozy, Filip Van Petegem, Michael F. Goldberg, Heinz Jungbluth, Johann Böhm, Wija Oortwijn, Robert T. Dirksen, and Nicol C. Voermans. Individuals and families affected by ryr1-related diseases: the patient/caregiver perspective. Journal of Neuromuscular Diseases, 11:1067-1083, Aug 2024. URL: https://doi.org/10.3233/jnd-240029, doi:10.3233/jnd-240029. This article has 2 citations and is from a peer-reviewed journal.

11. (cotta2022centralcoredisease pages 2-4): Ana Cotta, Lucas Santos Souza, Elmano Carvalho, Leticia Nogueira Feitosa, Antonio Cunha, Monica Machado Navarro, Jaquelin Valicek, Miriam Melo Menezes, Simone Vilela Nunes Neves, Rafael Xavier-Neto, Antonio Pedro Vargas, Reinaldo Issao Takata, Julia Filardi Paim, and Mariz Vainzof. Central core disease: facial weakness differentiating biallelic from monoallelic forms. Genes, 13:760, Apr 2022. URL: https://doi.org/10.3390/genes13050760, doi:10.3390/genes13050760. This article has 6 citations.

12. (cotta2022centralcoredisease pages 9-10): Ana Cotta, Lucas Santos Souza, Elmano Carvalho, Leticia Nogueira Feitosa, Antonio Cunha, Monica Machado Navarro, Jaquelin Valicek, Miriam Melo Menezes, Simone Vilela Nunes Neves, Rafael Xavier-Neto, Antonio Pedro Vargas, Reinaldo Issao Takata, Julia Filardi Paim, and Mariz Vainzof. Central core disease: facial weakness differentiating biallelic from monoallelic forms. Genes, 13:760, Apr 2022. URL: https://doi.org/10.3390/genes13050760, doi:10.3390/genes13050760. This article has 6 citations.

13. (raga2024treatmentsforryr1relateddisorders pages 12-13): S Raga, N Voermans, I Perez-Neri, and J Dowling. Treatmentsfor ryr1-related disorders (protocol). Unknown journal, 2024.

14. (cotta2022centralcoredisease media ead0977b): Ana Cotta, Lucas Santos Souza, Elmano Carvalho, Leticia Nogueira Feitosa, Antonio Cunha, Monica Machado Navarro, Jaquelin Valicek, Miriam Melo Menezes, Simone Vilela Nunes Neves, Rafael Xavier-Neto, Antonio Pedro Vargas, Reinaldo Issao Takata, Julia Filardi Paim, and Mariz Vainzof. Central core disease: facial weakness differentiating biallelic from monoallelic forms. Genes, 13:760, Apr 2022. URL: https://doi.org/10.3390/genes13050760, doi:10.3390/genes13050760. This article has 6 citations.

15. (lillis2012clinicalutilitygene pages 4-5): Suzanne Lillis, Stephen Abbs, Clemens R Mueller, Francesco Muntoni, and Heinz Jungbluth. Clinical utility gene card for: central core disease. European Journal of Human Genetics, 20:-, Oct 2012. URL: https://doi.org/10.1038/ejhg.2011.179, doi:10.1038/ejhg.2011.179. This article has 10 citations and is from a domain leading peer-reviewed journal.

16. (leao2020dominantorrecessive pages 2-3): Leonardo Galleni Leão, Lucas Santos Souza, L. Nogueira, R. Pavanello, J. Gurgel-Giannetti, U. Reed, A. Oliveira, T. Cuperman, A. Cotta, Julia FPaim, M. Zatz, and M. Vainzof. Dominant or recessive mutations in the ryr1 gene causing central core myopathy in brazilian patients. Acta Myologica, 39:274-282, Dec 2020. URL: https://doi.org/10.36185/2532-1900-030, doi:10.36185/2532-1900-030. This article has 5 citations and is from a peer-reviewed journal.

17. (cotta2022centralcoredisease pages 7-9): Ana Cotta, Lucas Santos Souza, Elmano Carvalho, Leticia Nogueira Feitosa, Antonio Cunha, Monica Machado Navarro, Jaquelin Valicek, Miriam Melo Menezes, Simone Vilela Nunes Neves, Rafael Xavier-Neto, Antonio Pedro Vargas, Reinaldo Issao Takata, Julia Filardi Paim, and Mariz Vainzof. Central core disease: facial weakness differentiating biallelic from monoallelic forms. Genes, 13:760, Apr 2022. URL: https://doi.org/10.3390/genes13050760, doi:10.3390/genes13050760. This article has 6 citations.

18. (lillis2012clinicalutilitygene pages 5-5): Suzanne Lillis, Stephen Abbs, Clemens R Mueller, Francesco Muntoni, and Heinz Jungbluth. Clinical utility gene card for: central core disease. European Journal of Human Genetics, 20:-, Oct 2012. URL: https://doi.org/10.1038/ejhg.2011.179, doi:10.1038/ejhg.2011.179. This article has 10 citations and is from a domain leading peer-reviewed journal.

19. (leao2020dominantorrecessive pages 1-2): Leonardo Galleni Leão, Lucas Santos Souza, L. Nogueira, R. Pavanello, J. Gurgel-Giannetti, U. Reed, A. Oliveira, T. Cuperman, A. Cotta, Julia FPaim, M. Zatz, and M. Vainzof. Dominant or recessive mutations in the ryr1 gene causing central core myopathy in brazilian patients. Acta Myologica, 39:274-282, Dec 2020. URL: https://doi.org/10.36185/2532-1900-030, doi:10.36185/2532-1900-030. This article has 5 citations and is from a peer-reviewed journal.

20. (rosenberg2015malignanthyperthermiaa pages 4-5): Henry Rosenberg, Neil Pollock, Anja Schiemann, Terasa Bulger, and Kathryn Stowell. Malignant hyperthermia: a review. Orphanet Journal of Rare Diseases, Aug 2015. URL: https://doi.org/10.1186/s13023-015-0310-1, doi:10.1186/s13023-015-0310-1. This article has 788 citations and is from a peer-reviewed journal.

21. (camp2024individualsandfamilies pages 13-15): Sanne A.J.H. van de Camp, Lizan Stinissen, Andrew Huseth, Brentney Simon, Jennifer Ryan, Anna Sarkozy, Filip Van Petegem, Michael F. Goldberg, Heinz Jungbluth, Johann Böhm, Wija Oortwijn, Robert T. Dirksen, and Nicol C. Voermans. Individuals and families affected by ryr1-related diseases: the patient/caregiver perspective. Journal of Neuromuscular Diseases, 11:1067-1083, Aug 2024. URL: https://doi.org/10.3233/jnd-240029, doi:10.3233/jnd-240029. This article has 2 citations and is from a peer-reviewed journal.

22. (camp2024individualsandfamilies pages 5-7): Sanne A.J.H. van de Camp, Lizan Stinissen, Andrew Huseth, Brentney Simon, Jennifer Ryan, Anna Sarkozy, Filip Van Petegem, Michael F. Goldberg, Heinz Jungbluth, Johann Böhm, Wija Oortwijn, Robert T. Dirksen, and Nicol C. Voermans. Individuals and families affected by ryr1-related diseases: the patient/caregiver perspective. Journal of Neuromuscular Diseases, 11:1067-1083, Aug 2024. URL: https://doi.org/10.3233/jnd-240029, doi:10.3233/jnd-240029. This article has 2 citations and is from a peer-reviewed journal.

23. (camp2024individualsandfamilies pages 1-3): Sanne A.J.H. van de Camp, Lizan Stinissen, Andrew Huseth, Brentney Simon, Jennifer Ryan, Anna Sarkozy, Filip Van Petegem, Michael F. Goldberg, Heinz Jungbluth, Johann Böhm, Wija Oortwijn, Robert T. Dirksen, and Nicol C. Voermans. Individuals and families affected by ryr1-related diseases: the patient/caregiver perspective. Journal of Neuromuscular Diseases, 11:1067-1083, Aug 2024. URL: https://doi.org/10.3233/jnd-240029, doi:10.3233/jnd-240029. This article has 2 citations and is from a peer-reviewed journal.

24. (raga2024treatmentsforryr1relateddisorders pages 13-15): S Raga, N Voermans, I Perez-Neri, and J Dowling. Treatmentsfor ryr1-related disorders (protocol). Unknown journal, 2024.

25. (schartner2019abnormalexcitationcontractioncoupling pages 4-6): Vanessa Schartner, Jocelyn Laporte, and Johann Böhm. Abnormal excitation-contraction coupling and calcium homeostasis in myopathies and cardiomyopathies. Journal of Neuromuscular Diseases, 6:289-305, Sep 2019. URL: https://doi.org/10.3233/jnd-180314, doi:10.3233/jnd-180314. This article has 24 citations and is from a peer-reviewed journal.

26. (parker2017functionalcharacterizationof pages 1-3): Remai Parker, Anja H. Schiemann, Elaine Langton, Terasa Bulger, Neil Pollock, Andrew Bjorksten, Robyn Gillies, David Hutchinson, Richard Roxburgh, and Kathryn M. Stowell. Functional characterization of c-terminal ryanodine receptor 1 variants associated with central core disease or malignant hyperthermia. Journal of Neuromuscular Diseases, 4:147-158, May 2017. URL: https://doi.org/10.3233/jnd-170210, doi:10.3233/jnd-170210. This article has 11 citations and is from a peer-reviewed journal.

27. (o’connor2023ryr1relateddiseasesinternational pages 14-16): Thomas N. O’Connor, L. R. van den Bersselaar, Y. Chen, Stefan Nicolau, Brentney Simon, Andrew Huseth, Joshua J. Todd, Filip Van Petegem, Anna Sarkozy, Michael F. Goldberg, N. Voermans, Robert T. Dirksen, Leslie Johann Carsten Oliver Razvan Robert James Michael Biesecker Böhm Bönnemann Clarke Cornea Dirksen Dow, Leslie Biesecker, Johann Böhm, Carsten G Bönnemann, Oliver Clarke, Razvan Cornea, Robert T. Dirksen, James Dowling, Michael F. Goldberg, Susan Hamilton, Drew Huseth, H. Jungbluth, Tokunbor A. Lawal, A. Marks, Isabelle Marty, L. Medne, Eva Michael, P. Mohassel, Takashi Murayama, S. Riazi, Anna Sarkozy, Brentney Simon, Joshua J. Todd, Jacques Tremblay, S. Treves, L. R. van den Bersselaar, Filip Van Petegem, N. Voermans, and N. Witting. Ryr-1-related diseases international research workshop: from mechanisms to treatments pittsburgh, pa, u.s.a., 21-22 july 2022. Journal of Neuromuscular Diseases, 10:135-154, Jan 2023. URL: https://doi.org/10.3233/jnd-221609, doi:10.3233/jnd-221609. This article has 10 citations and is from a peer-reviewed journal.

28. (amburgey2013genotypephenotypecorrelationsin pages 1-2): Kimberly Amburgey, Angela Bailey, Jean H Hwang, Mark A Tarnopolsky, Carsten G Bonnemann, Livija Medne, Katherine D Mathews, James Collins, Jasper R Daube, Gregory P Wellman, Brian Callaghan, Nigel F Clarke, and James J Dowling. Genotype-phenotype correlations in recessive ryr1-related myopathies. Orphanet Journal of Rare Diseases, 8:117-117, Aug 2013. URL: https://doi.org/10.1186/1750-1172-8-117, doi:10.1186/1750-1172-8-117. This article has 137 citations and is from a peer-reviewed journal.

29. (amburgey2013genotypephenotypecorrelationsin pages 10-11): Kimberly Amburgey, Angela Bailey, Jean H Hwang, Mark A Tarnopolsky, Carsten G Bonnemann, Livija Medne, Katherine D Mathews, James Collins, Jasper R Daube, Gregory P Wellman, Brian Callaghan, Nigel F Clarke, and James J Dowling. Genotype-phenotype correlations in recessive ryr1-related myopathies. Orphanet Journal of Rare Diseases, 8:117-117, Aug 2013. URL: https://doi.org/10.1186/1750-1172-8-117, doi:10.1186/1750-1172-8-117. This article has 137 citations and is from a peer-reviewed journal.

30. (chen2017reducedthresholdfor pages 1-3): Wenqian Chen, Andrea Koop, Yingjie Liu, Wenting Guo, Jinhong Wei, Ruiwu Wang, David H. MacLennan, Robert T. Dirksen, and Sui Rong Wayne Chen. Reduced threshold for store overload-induced ca2+ release is a common defect of ryr1 mutations associated with malignant hyperthermia and central core disease. The Biochemical journal, 474 16:2749-2761, Aug 2017. URL: https://doi.org/10.1042/bcj20170282, doi:10.1042/bcj20170282. This article has 36 citations.

31. (schartner2019abnormalexcitationcontractioncoupling pages 1-2): Vanessa Schartner, Jocelyn Laporte, and Johann Böhm. Abnormal excitation-contraction coupling and calcium homeostasis in myopathies and cardiomyopathies. Journal of Neuromuscular Diseases, 6:289-305, Sep 2019. URL: https://doi.org/10.3233/jnd-180314, doi:10.3233/jnd-180314. This article has 24 citations and is from a peer-reviewed journal.

32. (rosenberg2015malignanthyperthermiaa pages 6-8): Henry Rosenberg, Neil Pollock, Anja Schiemann, Terasa Bulger, and Kathryn Stowell. Malignant hyperthermia: a review. Orphanet Journal of Rare Diseases, Aug 2015. URL: https://doi.org/10.1186/s13023-015-0310-1, doi:10.1186/s13023-015-0310-1. This article has 788 citations and is from a peer-reviewed journal.

33. (lillis2012clinicalutilitygene pages 3-4): Suzanne Lillis, Stephen Abbs, Clemens R Mueller, Francesco Muntoni, and Heinz Jungbluth. Clinical utility gene card for: central core disease. European Journal of Human Genetics, 20:-, Oct 2012. URL: https://doi.org/10.1038/ejhg.2011.179, doi:10.1038/ejhg.2011.179. This article has 10 citations and is from a domain leading peer-reviewed journal.

34. (baba2024anestheticmanagementof pages 4-5): Hiroko Baba, Ryo Wakabayashi, Hiroki Ichiyanagi, Aki Suzuki, and Nobukazu Sato. Anesthetic management of a patient with central core disease undergoing thoracoscopic lung resection: the importance of neuromuscular monitoring at the masseter muscle. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.52456, doi:10.7759/cureus.52456. This article has 1 citations.

35. (o’connor2023ryr1relateddiseasesinternational pages 1-3): Thomas N. O’Connor, L. R. van den Bersselaar, Y. Chen, Stefan Nicolau, Brentney Simon, Andrew Huseth, Joshua J. Todd, Filip Van Petegem, Anna Sarkozy, Michael F. Goldberg, N. Voermans, Robert T. Dirksen, Leslie Johann Carsten Oliver Razvan Robert James Michael Biesecker Böhm Bönnemann Clarke Cornea Dirksen Dow, Leslie Biesecker, Johann Böhm, Carsten G Bönnemann, Oliver Clarke, Razvan Cornea, Robert T. Dirksen, James Dowling, Michael F. Goldberg, Susan Hamilton, Drew Huseth, H. Jungbluth, Tokunbor A. Lawal, A. Marks, Isabelle Marty, L. Medne, Eva Michael, P. Mohassel, Takashi Murayama, S. Riazi, Anna Sarkozy, Brentney Simon, Joshua J. Todd, Jacques Tremblay, S. Treves, L. R. van den Bersselaar, Filip Van Petegem, N. Voermans, and N. Witting. Ryr-1-related diseases international research workshop: from mechanisms to treatments pittsburgh, pa, u.s.a., 21-22 july 2022. Journal of Neuromuscular Diseases, 10:135-154, Jan 2023. URL: https://doi.org/10.3233/jnd-221609, doi:10.3233/jnd-221609. This article has 10 citations and is from a peer-reviewed journal.

36. (ziemian2025integrativeapproachesto pages 36-37): Maja Ziemian, Joanna Szmydtka, Wojciech Snoch, Sandra Milner, Szymon Wojciechowski, Aleksandra Dłuszczakowska, Jakub W. Chojnowski, Zofia Pallach, Katarzyna Żamojda, Grzegorz Węgrzyn, and Estera Rintz. Integrative approaches to myopathies and muscular dystrophies: molecular mechanisms, diagnostics, and future therapies. International Journal of Molecular Sciences, 26:7972, Aug 2025. URL: https://doi.org/10.3390/ijms26167972, doi:10.3390/ijms26167972. This article has 3 citations.

37. (o’connor2023ryr1relateddiseasesinternational pages 13-14): Thomas N. O’Connor, L. R. van den Bersselaar, Y. Chen, Stefan Nicolau, Brentney Simon, Andrew Huseth, Joshua J. Todd, Filip Van Petegem, Anna Sarkozy, Michael F. Goldberg, N. Voermans, Robert T. Dirksen, Leslie Johann Carsten Oliver Razvan Robert James Michael Biesecker Böhm Bönnemann Clarke Cornea Dirksen Dow, Leslie Biesecker, Johann Böhm, Carsten G Bönnemann, Oliver Clarke, Razvan Cornea, Robert T. Dirksen, James Dowling, Michael F. Goldberg, Susan Hamilton, Drew Huseth, H. Jungbluth, Tokunbor A. Lawal, A. Marks, Isabelle Marty, L. Medne, Eva Michael, P. Mohassel, Takashi Murayama, S. Riazi, Anna Sarkozy, Brentney Simon, Joshua J. Todd, Jacques Tremblay, S. Treves, L. R. van den Bersselaar, Filip Van Petegem, N. Voermans, and N. Witting. Ryr-1-related diseases international research workshop: from mechanisms to treatments pittsburgh, pa, u.s.a., 21-22 july 2022. Journal of Neuromuscular Diseases, 10:135-154, Jan 2023. URL: https://doi.org/10.3233/jnd-221609, doi:10.3233/jnd-221609. This article has 10 citations and is from a peer-reviewed journal.

38. (NCT04141670 chunk 2):  S 48168 (ARM 210) for the Treatment of RYR1-related Myopathies (RYR1-RM). RyCarma Therapeutics, Inc.. 2020. ClinicalTrials.gov Identifier: NCT04141670

39. (baba2024anestheticmanagementof pages 5-5): Hiroko Baba, Ryo Wakabayashi, Hiroki Ichiyanagi, Aki Suzuki, and Nobukazu Sato. Anesthetic management of a patient with central core disease undergoing thoracoscopic lung resection: the importance of neuromuscular monitoring at the masseter muscle. Cureus, Jan 2024. URL: https://doi.org/10.7759/cureus.52456, doi:10.7759/cureus.52456. This article has 1 citations.

40. (o’connor2023ryr1relateddiseasesinternational pages 11-13): Thomas N. O’Connor, L. R. van den Bersselaar, Y. Chen, Stefan Nicolau, Brentney Simon, Andrew Huseth, Joshua J. Todd, Filip Van Petegem, Anna Sarkozy, Michael F. Goldberg, N. Voermans, Robert T. Dirksen, Leslie Johann Carsten Oliver Razvan Robert James Michael Biesecker Böhm Bönnemann Clarke Cornea Dirksen Dow, Leslie Biesecker, Johann Böhm, Carsten G Bönnemann, Oliver Clarke, Razvan Cornea, Robert T. Dirksen, James Dowling, Michael F. Goldberg, Susan Hamilton, Drew Huseth, H. Jungbluth, Tokunbor A. Lawal, A. Marks, Isabelle Marty, L. Medne, Eva Michael, P. Mohassel, Takashi Murayama, S. Riazi, Anna Sarkozy, Brentney Simon, Joshua J. Todd, Jacques Tremblay, S. Treves, L. R. van den Bersselaar, Filip Van Petegem, N. Voermans, and N. Witting. Ryr-1-related diseases international research workshop: from mechanisms to treatments pittsburgh, pa, u.s.a., 21-22 july 2022. Journal of Neuromuscular Diseases, 10:135-154, Jan 2023. URL: https://doi.org/10.3233/jnd-221609, doi:10.3233/jnd-221609. This article has 10 citations and is from a peer-reviewed journal.

41. (raga2024treatmentsforryr1relateddisorders pages 4-5): S Raga, N Voermans, I Perez-Neri, and J Dowling. Treatmentsfor ryr1-related disorders (protocol). Unknown journal, 2024.

42. (o’connor2023ryr1relateddiseasesinternational pages 8-10): Thomas N. O’Connor, L. R. van den Bersselaar, Y. Chen, Stefan Nicolau, Brentney Simon, Andrew Huseth, Joshua J. Todd, Filip Van Petegem, Anna Sarkozy, Michael F. Goldberg, N. Voermans, Robert T. Dirksen, Leslie Johann Carsten Oliver Razvan Robert James Michael Biesecker Böhm Bönnemann Clarke Cornea Dirksen Dow, Leslie Biesecker, Johann Böhm, Carsten G Bönnemann, Oliver Clarke, Razvan Cornea, Robert T. Dirksen, James Dowling, Michael F. Goldberg, Susan Hamilton, Drew Huseth, H. Jungbluth, Tokunbor A. Lawal, A. Marks, Isabelle Marty, L. Medne, Eva Michael, P. Mohassel, Takashi Murayama, S. Riazi, Anna Sarkozy, Brentney Simon, Joshua J. Todd, Jacques Tremblay, S. Treves, L. R. van den Bersselaar, Filip Van Petegem, N. Voermans, and N. Witting. Ryr-1-related diseases international research workshop: from mechanisms to treatments pittsburgh, pa, u.s.a., 21-22 july 2022. Journal of Neuromuscular Diseases, 10:135-154, Jan 2023. URL: https://doi.org/10.3233/jnd-221609, doi:10.3233/jnd-221609. This article has 10 citations and is from a peer-reviewed journal.

43. (godbout2023successfulcorrectionby pages 1-3): Kelly Godbout, Joël Rousseau, and Jacques P. Tremblay. Successful correction by prime editing of a mutation in the ryr1 gene responsible for a myopathy. Cells, 13:31, Dec 2023. URL: https://doi.org/10.3390/cells13010031, doi:10.3390/cells13010031. This article has 20 citations.

44. (o’connor2023ryr1relateddiseasesinternational pages 10-11): Thomas N. O’Connor, L. R. van den Bersselaar, Y. Chen, Stefan Nicolau, Brentney Simon, Andrew Huseth, Joshua J. Todd, Filip Van Petegem, Anna Sarkozy, Michael F. Goldberg, N. Voermans, Robert T. Dirksen, Leslie Johann Carsten Oliver Razvan Robert James Michael Biesecker Böhm Bönnemann Clarke Cornea Dirksen Dow, Leslie Biesecker, Johann Böhm, Carsten G Bönnemann, Oliver Clarke, Razvan Cornea, Robert T. Dirksen, James Dowling, Michael F. Goldberg, Susan Hamilton, Drew Huseth, H. Jungbluth, Tokunbor A. Lawal, A. Marks, Isabelle Marty, L. Medne, Eva Michael, P. Mohassel, Takashi Murayama, S. Riazi, Anna Sarkozy, Brentney Simon, Joshua J. Todd, Jacques Tremblay, S. Treves, L. R. van den Bersselaar, Filip Van Petegem, N. Voermans, and N. Witting. Ryr-1-related diseases international research workshop: from mechanisms to treatments pittsburgh, pa, u.s.a., 21-22 july 2022. Journal of Neuromuscular Diseases, 10:135-154, Jan 2023. URL: https://doi.org/10.3233/jnd-221609, doi:10.3233/jnd-221609. This article has 10 citations and is from a peer-reviewed journal.

45. (cacheux2015functionalcharacterizationof pages 1-3): Marine Cacheux, Ariane Blum, Muriel Sébastien, Anne Sophie Wozny, Julie Brocard, Kamel Mamchaoui, Vincent Mouly, Nathalie Roux-Buisson, John Rendu, Nicole Monnier, Renée Krivosic, Paul Allen, Arnaud Lacour, Joël Lunardi, Julien Fauré, and Isabelle Marty. Functional characterization of a central core disease ryr1 mutation (p.y4864h) associated with quantitative defect in ryr1 protein. Journal of Neuromuscular Diseases, 2:421-432, Nov 2015. URL: https://doi.org/10.3233/jnd-150073, doi:10.3233/jnd-150073. This article has 25 citations and is from a peer-reviewed journal.