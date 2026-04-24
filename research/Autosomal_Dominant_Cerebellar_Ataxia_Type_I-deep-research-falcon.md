---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T14:41:07.486023'
end_time: '2026-04-24T15:13:34.390955'
duration_seconds: 1946.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal dominant cerebellar ataxia type I
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal dominant cerebellar ataxia type I
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal dominant cerebellar ataxia type I** covering all of the
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
- **Disease Name:** Autosomal dominant cerebellar ataxia type I
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal dominant cerebellar ataxia type I** covering all of the
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


# Disease Characteristics Research Report: Autosomal dominant cerebellar ataxia type I (ADCA type I)

## Executive summary
Autosomal dominant cerebellar ataxia type I (ADCA I) is a **legacy clinical classification** (Harding) for dominantly inherited cerebellar ataxias characterized by **progressive cerebellar ataxia plus extracerebellar neurologic signs**. In contemporary practice, most patients are reclassified into **molecularly defined spinocerebellar ataxia (SCA) subtypes** (e.g., SCA1/ATXN1, SCA2/ATXN2, SCA3/ATXN3) and related disorders. ADCA I remains clinically useful for phenotype-driven genetic testing triage, but definitive diagnosis is genetic. (whaley2011autosomaldominantcerebellar pages 1-2, whaley2011autosomaldominantcerebellar pages 7-8, rudaks2024anupdateon pages 1-2)

**Evidence limitations (important for knowledge base ingestion):** This tool session did not retrieve OMIM/Orphanet/ICD/MeSH/MONDO identifier records directly; therefore, identifiers are reported as *not available from retrieved sources* (not as absent in reality). 

---

## 1. Disease information
### 1.1 Definition and current understanding
ADCA I refers to autosomal dominant cerebellar ataxias with **cerebellar ataxia plus other neurologic signs**, including oculomotor disturbance, cognitive deficits, pyramidal and extrapyramidal dysfunction, and bulbar/spinal/peripheral nervous system involvement. (whaley2011autosomaldominantcerebellar pages 1-2)

**Synonyms / alternative names used in practice**
- Autosomal dominant cerebellar ataxia type I (ADCA I) 
- Autosomal dominant cerebellar ataxias (ADCAs) with extracerebellar features 
- Spinocerebellar ataxia (SCA) spectrum disorders (umbrella term increasingly used) (schols2004autosomaldominantcerebellar pages 1-2, durr2010autosomaldominantcerebellar pages 1-2)

### 1.2 Key identifiers
- **MONDO/OMIM/Orphanet/MeSH/ICD-10/ICD-11:** Not retrievable in the current evidence set (see Evidence limitations). 

### 1.3 Evidence source type
The ADCA I concept is derived primarily from **aggregated disease-level resources** (clinical classification + genotype–phenotype studies and reviews), not from EHR-only sources. (whaley2011autosomaldominantcerebellar pages 1-2, durr2010autosomaldominantcerebellar pages 3-4, schols2004autosomaldominantcerebellar pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors
ADCA I is predominantly **genetic**. It spans multiple molecular mechanisms:
- **Coding CAG repeat expansions → polyglutamine (polyQ) proteins** (e.g., SCA1/ATXN1, SCA2/ATXN2, SCA3/ATXN3, SCA17/TBP, DRPLA/ATN1). (whaley2011autosomaldominantcerebellar pages 1-2, schols2004autosomaldominantcerebellar pages 1-2, durr2010autosomaldominantcerebellar pages 1-2)
- **Noncoding repeat expansions** (e.g., SCA8, SCA10, SCA12) and, in the modern adult-onset ataxia landscape, newly recognized expansions such as **FGF14-GAA (SCA27B)** and **ZFHX3 expansion (SCA4)**. (rudaks2024anupdateon pages 2-4, rudaks2024anupdateon pages 14-15)
- **Conventional variants (SNVs/indels/CNVs)** in genes associated with ADCA phenotypes (e.g., KCNC3/SCA13, PRKCG/SCA14, ITPR1/SCA15/16, FGF14/SCA27, AFG3L2/SCA28). (whaley2011autosomaldominantcerebellar pages 1-2, durr2010autosomaldominantcerebellar pages 1-2)

### 2.2 Risk factors
- **Family history / autosomal dominant inheritance** is the primary risk factor.
- For polyQ SCAs, **longer CAG repeat length** is associated with **earlier onset** and in some settings faster progression. (schols2004autosomaldominantcerebellar pages 1-2, rudaks2024anupdateon pages 1-2, durr2010autosomaldominantcerebellar pages 1-2)

### 2.3 Protective factors and gene–environment interactions
No specific protective alleles, protective environmental factors, or quantified gene–environment interactions were identified in the retrieved evidence set.

---

## 3. Phenotypes
### 3.1 Core phenotype spectrum (ADCA I)
ADCA I has a cerebellar syndrome plus multisystem neurologic involvement. Core cerebellar manifestations include gait/truncal/limb ataxia, nystagmus and saccadic abnormalities, and dysarthria. (whaley2011autosomaldominantcerebellar pages 1-2)

Extracerebellar features reported across ADCA I/SCA subtypes include:
- Oculomotor abnormalities: slowed saccades, ophthalmoplegia (whaley2011autosomaldominantcerebellar pages 2-3, durr2010autosomaldominantcerebellar pages 3-4)
- Pyramidal signs: spasticity, hyperreflexia, extensor plantar responses (schols2004autosomaldominantcerebellar pages 5-6)
- Extrapyramidal signs: dystonia, parkinsonism (durr2010autosomaldominantcerebellar pages 3-4)
- Peripheral neuropathy (notably prominent in SCA2) (durr2010autosomaldominantcerebellar pages 3-4)
- Cognitive/neuropsychiatric features (whaley2011autosomaldominantcerebellar pages 1-2)
- Seizures/epilepsy in selected subtypes (e.g., SCA10) (whaley2011autosomaldominantcerebellar pages 3-5)

### 3.2 Quantitative phenotype frequencies (example cohort)
In an Italian ADCA I cohort study (36 families), reported frequencies included:
- Gait ataxia: **100%**
- Dysarthria: **93%**
- Finger-to-nose dysmetria: **83%**
- Slow/absent saccades: **72%**
- Dysphagia: **55%**
- Sphincter disturbances: **66%**
These findings illustrate substantial bulbar/autonomic/oculomotor involvement with direct quality-of-life consequences. (filla1996autosomaldominantcerebellar pages 3-5)

Subtype-enriched frequencies from a large review of ADCAs:
- SCA1: pyramidal signs **67%**, brainstem oculomotor signs **74%**
- SCA2: peripheral nerve involvement **68%**
- SCA3: dystonia **24%**
- SCA7: visual loss **83%**, auditory loss **24%**
(durr2010autosomaldominantcerebellar pages 3-4)

### 3.3 Age of onset and course
- Typical onset is adult (often **3rd–4th decade**) but can range from childhood to older age depending on subtype. (whaley2011autosomaldominantcerebellar pages 1-2, durr2010autosomaldominantcerebellar pages 1-2)
- Example subtype statements: SCA1 often presents in the **4th decade**; SCA6 is often late onset (onset after age 50 in ~60% in one review). (whaley2011autosomaldominantcerebellar pages 2-3, schols2004autosomaldominantcerebellar pages 5-6)
- Course is progressive; one review states: **“These disorders are unrelentingly progressive and can shorten length of life.”** (whaley2011autosomaldominantcerebellar pages 2-3)

### 3.4 Quality of life (QoL) impact
QoL is affected by progressive gait instability (falls risk), dysarthria, dysphagia/aspiration risk, and eventual loss of independent ambulation and need for constant care in some patients. (filla1996autosomaldominantcerebellar pages 3-5, whaley2011autosomaldominantcerebellar pages 2-3)

### 3.5 Suggested HPO terms (non-exhaustive; ontology suggestions)
- Cerebellar ataxia (HP:0001251)
- Gait ataxia (HP:0002066)
- Dysarthria (HP:0001260)
- Nystagmus (HP:0000639)
- Slow saccades (HP:0000644)
- Ophthalmoplegia (HP:0000602)
- Pyramidal signs / spasticity (HP:0001257)
- Peripheral neuropathy (HP:0009830)
- Dystonia (HP:0001332)
- Dysphagia (HP:0002015)
- Cognitive impairment (HP:0100543)
- Seizures (HP:0001250)

---

## 4. Genetic / molecular information
### 4.1 Causal genes and variant classes (representative)
ADCA I is not a single-gene disorder; it is a **clinical umbrella** spanning multiple SCA genes and mechanisms. Key genes include ATXN1 (SCA1), ATXN2 (SCA2), ATXN3 (SCA3/MJD), TBP (SCA17), ATN1 (DRPLA), among others; mechanisms include CAG expansions, noncoding repeats, and conventional variants. (whaley2011autosomaldominantcerebellar pages 1-2, durr2010autosomaldominantcerebellar pages 1-2)

### 4.2 Anticipation and repeat-length effects
Anticipation is characteristic of polyQ SCAs; repeat length inversely correlates with age at onset, and juvenile onset is linked to large expansions often paternally transmitted. (durr2010autosomaldominantcerebellar pages 1-2, durr2010autosomaldominantcerebellar pages 3-4)

### 4.3 Modifier genes / epigenetics
Not identified in retrieved evidence set.

---

## 5. Environmental information
No robust non-genetic environmental causal factors were identified in the retrieved evidence set for ADCA I.

---

## 6. Mechanism / pathophysiology
### 6.1 Convergent mechanisms across polyQ ADCA-I SCAs
Recent synthesis emphasizes three broad mechanistic classes depending on mutation type: **proteotoxicity, RNA toxicity, and protein loss-of-function**, with polyQ SCAs strongly represented by proteotoxicity. (cui2024spinocerebellarataxiasfrom pages 1-2)

Common downstream disturbed processes include:
- Impaired protein quality control (ubiquitin–proteasome system, chaperones, autophagy)
- Transcriptional dysregulation and aberrant protein interactions
- Ion channel dysfunction, mitochondrial dysfunction, impaired DNA repair, and loss of nuclear integrity
(cui2024spinocerebellarataxiasfrom pages 1-2)

### 6.2 ATXN2 (SCA2) mechanisms (2024 update)
ATXN2 has roles in RNA metabolism/translation and stress granules, endocytosis, calcium signaling, and circadian regulation; CAG overexpansion can produce toxic gain and partial loss-of-function effects and is linked to autophagy impairment, oxidative stress, RNA-mediated toxicity, and disrupted calcium homeostasis. (costa2024thepolyglutamineprotein pages 1-2, costa2024thepolyglutamineprotein pages 6-7)

### 6.3 ATXN3 (SCA3/MJD) mechanisms (2024 update)
ATXN3 is a ubiquitin hydrolase (deubiquitinase) with ubiquitin-interacting motifs and connections to p97/VCP, positioning it in proteostasis pathways; mutant ATXN3 is implicated in perturbing protein quality control and autophagy regulation. (hernandezcarralero2024atxn3amultifunctional pages 1-2, cui2024spinocerebellarataxiasfrom pages 2-3)

### 6.4 Suggested GO biological process terms (examples)
- Protein ubiquitination / deubiquitination (GO:0016567; GO:0016579)
- Autophagy (GO:0006914)
- Protein folding / chaperone-mediated protein folding (GO:0006457)
- RNA metabolic process (GO:0016070)
- Cellular response to oxidative stress (GO:0034599)

### 6.5 Suggested CL cell types and UBERON structures (examples)
- Purkinje cell (CL:0000121)
- Cerebellar granule cell (CL:0000120)
- Oligodendrocyte (CL:0000128)
- Cerebellum (UBERON:0002037)
- Brainstem (UBERON:0002298)
- Spinal cord (UBERON:0002240)

---

## 7. Anatomical structures affected
Primary affected system is the **central nervous system**, particularly cerebellum and cerebellar connections; brainstem and spinal pathways may be involved, consistent with imaging (cerebellar/brainstem atrophy) and clinical pyramidal/bulbar features. (durr2010autosomaldominantcerebellar pages 1-2, burk1996autosomaldominantcerebellar pages 1-2)

---

## 8. Temporal development
- **Onset:** typically insidious adult onset, but broad range (childhood to elderly) depending on genotype. (durr2010autosomaldominantcerebellar pages 1-2)
- **Progression:** progressive neurodegenerative course; disability can progress to needing walking support or wheelchair in some cohorts. (filla1996autosomaldominantcerebellar pages 3-5)

---

## 9. Inheritance and population
### 9.1 Inheritance
Autosomal dominant inheritance by definition; for polyQ SCAs, anticipation is common with repeat instability. (durr2010autosomaldominantcerebellar pages 1-2, durr2010autosomaldominantcerebellar pages 3-4)

### 9.2 Epidemiology (recent synthesis prioritized)
- Global SCA prevalence in the 2024 European epidemiology review: **0 to 5.6 per 100,000**. (mattei2024epidemiologyofspinocerebellar pages 1-2)
- 2024 hereditary ataxia review: AD hereditary cerebellar ataxia prevalence reported up to **5.6/100,000** with estimated global average **2.7/100,000**. (rudaks2024anupdateon pages 1-2)
- European ADCA prevalence cited in a major review: **~1–3 per 100,000**. (durr2010autosomaldominantcerebellar pages 1-2)

### 9.3 Geographic heterogeneity and founder effects (Europe)
SCA3 is the most frequent dominant SCA in Europe, with high clustering in Portugal/Azores and other regions; one Portuguese context is reported with very high local prevalence approximating **~1/1,000**. (mattei2024epidemiologyofspinocerebellar pages 4-5)

The 2024 European review reports marked country/subregion heterogeneity in relative frequencies for SCA1/SCA2/SCA3/SCA6/SCA7/SCA8. Examples include EUROSCA relative frequency estimates: **SCA6 ~13%**, **SCA7 ~4.7%**, and SCA3 overall the most frequent. (mattei2024epidemiologyofspinocerebellar pages 4-5, mattei2024epidemiologyofspinocerebellar pages 5-6)

---

## 10. Diagnostics
### 10.1 Clinical evaluation and differential
Diagnosis uses history/exam and exclusion of secondary ataxias; differential includes toxic/drug, nutritional, endocrine, infectious/post-infectious, structural, paraneoplastic and other neurodegenerative causes. (whaley2011autosomaldominantcerebellar pages 1-2)

### 10.2 Genetic testing approach (2024–2025 practice direction)
A contemporary approach emphasizes:
1) **First-tier repeat-expansion testing** for common SCA expansions and other repeat disorders (including newly recognized expansions, where available). (rudaks2024anupdateon pages 1-2, rudaks2024anupdateon pages 10-12)
2) If negative, **NGS panels / WES / WGS** for conventional variants; reported diagnostic yield varies widely (**28.8–70.5%** across cohorts). (rudaks2024anupdateon pages 1-2)
3) Increasing use of **long-read sequencing** to detect STR expansions, deep intronic variants and structural variants; adaptive long-read sequencing has enabled discovery of expansions such as ZFHX3/SCA4. (rudaks2024anupdateon pages 14-15)

A single-center (2025) workflow combining repeat-expansion testing then WES reported:
- Pathogenic/likely pathogenic yield: **40% (28/70)**
- VUS: **20% (14/70)**
- Pathogenic repeat expansions: **14.3% (10/70)**
(bregant2025themolecularlandscape pages 1-2)

### 10.3 Imaging and neurophysiology
- MRI patterns can be subtype-informative: SCA2 may show severe OPCA-like changes, while SCA3 can have milder cerebellar/brainstem atrophy; SCA1 may overlap both. (burk1996autosomaldominantcerebellar pages 1-2)
- Eye movement testing: reduced saccade velocity was observed in **all SCA2**, **56% SCA1**, and **~30% SCA3** patients in one cohort study. (burk1996autosomaldominantcerebellar pages 1-2)

### 10.4 Biomarkers (fluid and digital)
**SCA3 fluid biomarkers (systematic review 2024):**
- NfL: an “**Optimal cut-off: 16.04 pg/mL**” was reported; example values show separation of controls (~5–8 pg/mL), preataxic (~15–22 pg/mL), and ataxic (~31–37 pg/mL) groups in plasma/serum cohorts; CSF NfL can be far higher (reported as “**CSF was 102X higher than serum**”). (sotopina2024specificbiomarkersin pages 5-6, sotopina2024specificbiomarkersin pages 5-5)
- PolyQ-ATXN3: CSF polyQ-ATXN3 “**perfectly discriminated** between controls and ataxic carriers” in one study summarized by the review. (sotopina2024specificbiomarkersin pages 5-5)

**Clinical scale context:** SARA is a standard clinical outcome measure in ataxia research and is also used for stage definitions (e.g., SARA <3 vs ≥3 in SCA3 biomarker studies). (sotopina2024specificbiomarkersin pages 2-5)

---

## 11. Outcome / prognosis
Prognosis varies by molecular subtype and family. Progressive disability can include transition to walking support or wheelchair and complications such as dysphagia/aspiration. (filla1996autosomaldominantcerebellar pages 3-5, whaley2011autosomaldominantcerebellar pages 1-2)

---

## 12. Treatment
### 12.1 Current standard of care (supportive/symptomatic)
There are no established disease-modifying therapies for ADCA I/SCAs; one authoritative review states these disorders **“can only be treated symptomatically.”** (schols2004autosomaldominantcerebellar pages 1-2)

Another ADCA I review states: **“supportive care remains the mainstay of management”** and explicitly: **“there are no known cures for the ADCA Type I.”** Recommended interventions include physical/occupational therapy, speech therapy, mobility aids (cane/walker/wheelchair), and treatment of depression and other symptoms to improve function and quality of life. (whaley2011autosomaldominantcerebellar pages 2-3)

### 12.2 Recent developments (prioritize 2023–2024)
#### Emerging disease-modifying approaches (pipeline)
- 2024 diagnostic review highlights rapid expansion of STR-discovery and improved testing platforms (including long-read sequencing), which is enabling better trial-ready stratification for targeted therapies. (rudaks2024anupdateon pages 14-15, rudaks2024anupdateon pages 1-2)

#### Clinical trials (selected, 2023–2024)
| Therapy | Modality | Target/gene | Indication | Trial phase/design | Status | Primary endpoints | Key quantitative results (if published) | Safety notes | URL and publication date |
|---|---|---|---|---|---|---|---|---|---|
| VO659 | Antisense oligonucleotide; lumbar intrathecal bolus | Expanded CAG-repeat RNA transcripts; SCA1 (**ATXN1**), SCA3 (**ATXN3**), and HD-associated transcript | Dominant polyQ SCAs relevant to ADCA I: SCA1 and SCA3 (plus early HD in basket trial) | Phase 1/2a, first-in-human, open-label, multiple ascending dose study; estimated enrollment 68 (NCT05822908 chunk 1, NCT05822908 chunk 2) | Recruiting (NCT05822908 chunk 1, NCT05822908 chunk 2) | Safety/tolerability; treatment-related AEs/SAEs/AESIs; PK in CSF and plasma; exploratory PD (NCT05822908 chunk 1, NCT05822908 chunk 2) | No efficacy results published in the registry excerpts; dose-escalation cohorts include 10 mg ×4, 20 mg, 40 mg ×4, and single 60 mg dose cohorts (NCT05822908 chunk 1) | Safety monitoring includes vitals, ECG, blood labs, CSF WBC/protein, MRI review, C-SSRS; no published outcome data in excerpt (NCT05822908 chunk 1, NCT05822908 chunk 2) | https://clinicaltrials.gov/study/NCT05822908 ; registry year 2023 (NCT05822908 chunk 1, NCT05822908 chunk 2) |
| ARO-ATXN2 Injection | Intrathecal injection; investigational oligonucleotide-based precision therapy (mechanism not stated in registry excerpt) | **ATXN2** | SCA2, a dominant ADCA I-related polyQ ataxia | Phase 1, randomized, placebo-controlled, dose-escalating, parallel, quadruple-masked; single IT dose; estimated enrollment 36 (NCT06672445 chunk 1) | Recruiting; actual start 2024-12-17; estimated primary completion 2026-12 (NCT06672445 chunk 1, NCT06672445 chunk 2) | Primary: number of participants with TEAEs through Day 253; secondary PK endpoints (Cmax, Tmax, AUCs, t1/2, CL/F, urinary recovery) and CSF safety/biomarker measures (protein, glucose, cell count) (NCT06672445 chunk 1) | No published efficacy results yet; genetically confirmed SCA2 with ≥33 CAG repeats required (NCT06672445 chunk 1) | Early-phase safety/PK study; no published adverse-event results yet in excerpt (NCT06672445 chunk 1) | https://clinicaltrials.gov/study/NCT06672445 ; registry year 2024 (NCT06672445 chunk 1, NCT06672445 chunk 2) |
| L-arginine | Small-molecule/amino-acid pharmacologic therapy; oral | Not gene-specific; tested in **CACNA1A**-related SCA6 clinical population | SCA6, a dominant spinocerebellar ataxia historically outside classic ADCA I but relevant to dominant SCA therapeutic landscape | Multicentre, randomized, double-blind, placebo-controlled phase 2 trial; 40 randomized, 1:1, 48-week treatment (ishihara2024larginineinpatients pages 1-2, ishihara2024larginineinpatients pages 3-4) | Completed/published 2024 (ishihara2024larginineinpatients pages 6-7, ishihara2024larginineinpatients pages 1-2) | Primary: change in total SARA score at 48 weeks (ishihara2024larginineinpatients pages 6-7, ishihara2024larginineinpatients pages 3-4) | Adjusted LS mean change in SARA at 48 weeks: -0.96 (95% CI -2.07 to 0.15) for L-arginine vs 0.56 (95% CI -0.55 to 1.67) for placebo; between-group difference -1.52 (95% CI -3.10 to 0.06), *P*=0.0582; 37/40 completed; adherence 97.2% in active arm (ishihara2024larginineinpatients pages 6-7, ishihara2024larginineinpatients pages 1-2, ishihara2024larginineinpatients pages 7-8) | AEs in 17/20 (85%) in both groups; serious AEs 2/20 (10%) active vs 5/20 (25%) placebo; adverse reactions 8/20 (40%) active vs 5/20 (25%) placebo; one severe pneumonia death and one reversible abnormal liver function in active arm (ishihara2024larginineinpatients pages 6-7, ishihara2024larginineinpatients pages 1-2, ishihara2024larginineinpatients pages 4-6) | https://doi.org/10.1016/j.eclinm.2024.102952 ; published Dec 2024 (ishihara2024larginineinpatients pages 6-7, ishihara2024larginineinpatients pages 1-2) |


*Table: This table summarizes recent 2023-2024 therapeutic developments and interventional studies relevant to dominant spinocerebellar ataxias linked to the legacy ADCA framework. It highlights modality, target, design, endpoints, published quantitative findings, and safety information for the most directly retrieved examples.*

Key examples:
- **VO659 (antisense oligonucleotide; intrathecal)** targeting expanded CAG-repeat RNA in SCA1/SCA3 (basket trial with early HD), Phase 1/2a, recruiting: **NCT05822908**. (NCT05822908 chunk 1, NCT05822908 chunk 2)
- **ARO-ATXN2 (intrathecal injection)** for SCA2, Phase 1 randomized placebo-controlled recruiting: **NCT06672445** (start 2024-12-17). (NCT06672445 chunk 1)
- **L-arginine in SCA6 (published Dec 2024):** multicentre RCT (n=40) with primary endpoint change in SARA at 48 weeks; between-group difference **−1.52 SARA points** (95% CI −3.10 to 0.06; P=0.0582) trending toward benefit; AEs in 85% in both arms; serious AEs 10% vs 25%; one pneumonia death in active group. (ishihara2024larginineinpatients pages 6-7, ishihara2024larginineinpatients pages 1-2, ishihara2024larginineinpatients media dcc962d8)

### 12.3 Suggested MAXO terms (examples)
- Physical therapy (MAXO:0000011)
- Occupational therapy (MAXO:0000012)
- Speech therapy (MAXO:0000015)
- Genetic counseling (MAXO:0000077)
- Assistive device (wheelchair/walker) use (MAXO:0001017)

---

## 13. Prevention
Primary prevention is not currently feasible for monogenic ADCA I disorders. Prevention-oriented actions focus on:
- Genetic counseling and cascade testing in families (whaley2011autosomaldominantcerebellar pages 1-2)
- Anticipation-aware counseling for repeat-expansion subtypes (whaley2011autosomaldominantcerebellar pages 1-2)
- Symptom/complication prevention (falls precautions, dysphagia management) through rehabilitation and supportive care (whaley2011autosomaldominantcerebellar pages 2-3, filla1996autosomaldominantcerebellar pages 3-5)

---

## 14. Other species / natural disease
Not addressed in retrieved evidence set.

---

## 15. Model organisms
Not addressed in retrieved evidence set. Mechanistic reviews note use of cellular and animal models for polyQ SCAs in general, but specific curated model organism details were not retrieved in this session. (cui2024spinocerebellarataxiasfrom pages 1-2)

---

## Key concepts table: ADCA I → modern SCA mapping
| Legacy term/definition | Major SCA subtypes included | Causal gene(s) | Variant class (CAG polyQ, noncoding repeat, SNV/CNV) | Key extracerebellar features | Typical onset range | Key citations with year/URL |
|---|---|---|---|---|---|---|
| **ADCA type I (Harding)**: dominantly inherited cerebellar ataxia **with additional neurologic signs** beyond a pure cerebellar syndrome | Historically includes SCA1–SCA4, SCA8, SCA10, SCA12–SCA23, SCA25, SCA27, SCA28, and DRPLA; modern practice usually reclassifies cases by molecular subtype rather than retaining the legacy umbrella term | Multiple genes/loci depending on subtype | Mixed: polyQ CAG expansions, noncoding repeat expansions, and conventional SNV/CNV/indel mechanisms | Oculomotor disturbance, cognitive deficits, pyramidal/extrapyramidal signs, bulbar, spinal, and peripheral nervous system involvement; gait/truncal/limb ataxia, nystagmus, dysarthria | Usually adult onset; childhood cases also reported | Whaley 2011 https://doi.org/10.1186/1750-1172-6-33; Durr 2010 https://doi.org/10.1016/S1474-4422(10)70183-6; Schöls 2004 https://doi.org/10.1016/S1474-4422(04)00737-9 (whaley2011autosomaldominantcerebellar pages 1-2, schols2004autosomaldominantcerebellar pages 1-2, durr2010autosomaldominantcerebellar pages 1-2) |
| **PolyQ / coding repeat ADCA-I subgroup** | SCA1, SCA2, SCA3, SCA17, DRPLA; many clinical series also focus testing on SCA6/SCA7 among dominant ataxias | **ATXN1, ATXN2, ATXN3, TBP, ATN1** | **CAG repeat expansion in coding region → polyglutamine (polyQ)** | Broad ADCA-I pattern; subtype-enriched features include pyramidal and brainstem oculomotor signs in SCA1, peripheral nerve involvement in SCA2, dystonia in SCA3, marked visual loss in SCA7 | Often 3rd–4th decade; juvenile onset can occur with larger expansions; anticipation common | Durr 2010 https://doi.org/10.1016/S1474-4422(10)70183-6; Schöls 2004 https://doi.org/10.1016/S1474-4422(04)00737-9; Rudaks 2024 https://doi.org/10.1007/s12311-024-01703-z (durr2010autosomaldominantcerebellar pages 3-4, schols2004autosomaldominantcerebellar pages 1-2, rudaks2024anupdateon pages 1-2) |
| **SCA1 within ADCA-I** | SCA1 | **ATXN1** | **CAG polyQ expansion** | Dysarthria, handwriting difficulty, limb ataxia; pyramidal tract signs, optic disc pallor, dysphagia relatively more frequent; slow saccades common | Typically 4th decade; earlier onset with longer repeat length | Burk 1996 https://doi.org/10.1093/brain/119.5.1497; Whaley 2011 https://doi.org/10.1186/1750-1172-6-33; Mattei 2024 https://doi.org/10.1007/s12311-023-01600-x (burk1996autosomaldominantcerebellar pages 1-2, whaley2011autosomaldominantcerebellar pages 2-3, mattei2024epidemiologyofspinocerebellar pages 1-2) |
| **SCA2 within ADCA-I** | SCA2 | **ATXN2** | **CAG polyQ expansion** | Slow saccades are especially characteristic; peripheral neuropathy frequent; broader ADCA-I signs may include parkinsonism/cognitive features in some cases | Usually adult onset, commonly 3rd–4th decade | Burk 1996 https://doi.org/10.1093/brain/119.5.1497; Durr 2010 https://doi.org/10.1016/S1474-4422(10)70183-6; Rudaks 2024 https://doi.org/10.1007/s12311-024-01703-z (burk1996autosomaldominantcerebellar pages 1-2, durr2010autosomaldominantcerebellar pages 3-4, rudaks2024anupdateon pages 1-2) |
| **SCA3 / Machado-Joseph disease within ADCA-I** | SCA3 (MJD) | **ATXN3** | **CAG polyQ expansion** | Dystonia common; ophthalmoplegia/oculomotor abnormalities and peripheral neuropathy may occur; mild-to-moderate brainstem/cerebellar atrophy on MRI relative to SCA2 | Usually adult onset; most common ADCA-I subtype worldwide | Whaley 2011 https://doi.org/10.1186/1750-1172-6-33; Burk 1996 https://doi.org/10.1093/brain/119.5.1497; Durr 2010 https://doi.org/10.1016/S1474-4422(10)70183-6; Rudaks 2024 https://doi.org/10.1007/s12311-024-01703-z (whaley2011autosomaldominantcerebellar pages 1-2, burk1996autosomaldominantcerebellar pages 1-2, durr2010autosomaldominantcerebellar pages 3-4, rudaks2024anupdateon pages 1-2) |
| **Noncoding repeat ADCA-I subgroup** | SCA8, SCA10, SCA12; modern expansion of dominant ataxia landscape also includes newer noncoding STR disorders such as SCA27B and ZFHX3-linked SCA4, though these are discussed in updated hereditary ataxia frameworks rather than original Harding-era lists | **ATXN8OS/ATXN8, ATXN10, PPP2R2B**; newer examples **FGF14, ZFHX3** | **Noncoding repeat expansion** | Can still show classic ADCA-I phenotype with cerebellar plus extracerebellar signs; phenotype varies by subtype | Usually adult onset, variable by subtype | Whaley 2011 https://doi.org/10.1186/1750-1172-6-33; Rudaks 2024 https://doi.org/10.1007/s12311-024-01703-z (whaley2011autosomaldominantcerebellar pages 1-2, rudaks2024anupdateon pages 14-15, rudaks2024anupdateon pages 2-4) |
| **Conventional mutation / SNV-CNV ADCA-I subgroup** | SCA13, SCA14, SCA15/16, SCA27, SCA28; additional conventional-mutation SCAs listed in broader ADCA reviews include SCA5, SCA11 and others | **KCNC3, PRKCG, ITPR1, FGF14, AFG3L2**; broader dominant ataxia list also includes **SPTBN2, TTBK2** | **SNV/indel/deletion/CNV (non-repeat) mechanisms** | Tremor, cognitive impairment, parkinsonian signs, slowed saccades, Babinski/hyperreflexia, sensory neuropathy depending on subtype | Variable; some juvenile-onset forms reported (e.g., SCA28 mean onset ~19.5 y in one review) | Whaley 2011 https://doi.org/10.1186/1750-1172-6-33; Durr 2010 https://doi.org/10.1016/S1474-4422(10)70183-6 (whaley2011autosomaldominantcerebellar pages 7-8, durr2010autosomaldominantcerebellar pages 1-2) |
| **Current diagnostic mapping implication** | In contemporary practice, a patient with a Harding ADCA-I phenotype is worked up as **adult-onset hereditary cerebellar ataxia / SCA**, with first-tier targeted STR testing followed by panel/WES/WGS and increasingly long-read sequencing | Depends on phenotype-guided testing; commonly tested dominant repeat genes include **ATXN1, ATXN2, ATXN3, CACNA1A, ATXN7, TBP**, plus newer loci such as **FGF14** and **ZFHX3** where available | Sequential testing for **repeat expansions first**, then **conventional variants**; long-read sequencing improves detection of complex STRs and intronic expansions | Diagnostic phenotype remains useful because syndrome-specific extracerebellar signs can help prioritize molecular testing, but genotype is now definitive | Adult-onset hereditary ataxia framework; variable by genotype | Whaley 2011 https://doi.org/10.1186/1750-1172-6-33; Durr 2010 https://doi.org/10.1016/S1474-4422(10)70183-6; Rudaks 2024 https://doi.org/10.1007/s12311-024-01703-z (whaley2011autosomaldominantcerebellar pages 7-8, durr2010autosomaldominantcerebellar pages 1-2, rudaks2024anupdateon pages 14-15, rudaks2024anupdateon pages 1-2) |


*Table: This table maps the legacy Harding ADCA type I category to modern molecularly defined spinocerebellar ataxia subtypes, genes, and mutation classes. It is useful for translating older clinical terminology into current diagnostic and knowledge-base frameworks.*

---

## Expert opinion synthesis (from authoritative reviews)
- Clinical phenotype is helpful for triaging tests, but **genotype is definitive**; one review emphasizes that genetic testing is the only definitive way to distinguish genotypes and that classification can streamline molecular testing. (whaley2011autosomaldominantcerebellar pages 7-8)
- Prognostic prediction in presymptomatic testing is limited by repeat instability; one Lancet Neurology review states that **“precise prediction for the age at onset cannot be given in presymptomatic testing”** and that prenatal diagnosis requires caution due to instability. (schols2004autosomaldominantcerebellar pages 1-2)

---

## Reference URLs (selected)
- Whaley et al. Orphanet J Rare Dis. 2011-05. https://doi.org/10.1186/1750-1172-6-33 (whaley2011autosomaldominantcerebellar pages 1-2)
- Durr. Lancet Neurol. 2010-09. https://doi.org/10.1016/S1474-4422(10)70183-6 (durr2010autosomaldominantcerebellar pages 1-2)
- Schöls et al. Lancet Neurol. 2004-05. https://doi.org/10.1016/S1474-4422(04)00737-9 (schols2004autosomaldominantcerebellar pages 1-2)
- De Mattei et al. Cerebellum. 2024-09. https://doi.org/10.1007/s12311-023-01600-x (mattei2024epidemiologyofspinocerebellar pages 1-2)
- Rudaks et al. Cerebellum. 2024-05. https://doi.org/10.1007/s12311-024-01703-z (rudaks2024anupdateon pages 1-2)
- Soto-Piña et al. IJMS. 2024-07. https://doi.org/10.3390/ijms25158074 (sotopina2024specificbiomarkersin pages 5-6)
- Ishihara et al. eClinicalMedicine. 2024-12. https://doi.org/10.1016/j.eclinm.2024.102952 (ishihara2024larginineinpatients pages 6-7)
- ClinicalTrials.gov VO659: https://clinicaltrials.gov/study/NCT05822908 (NCT05822908 chunk 1)
- ClinicalTrials.gov ARO-ATXN2: https://clinicaltrials.gov/study/NCT06672445 (NCT06672445 chunk 1)


References

1. (whaley2011autosomaldominantcerebellar pages 1-2): Nathaniel Robb Whaley, Shinsuke Fujioka, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type i: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 6:33-33, May 2011. URL: https://doi.org/10.1186/1750-1172-6-33, doi:10.1186/1750-1172-6-33. This article has 120 citations and is from a peer-reviewed journal.

2. (whaley2011autosomaldominantcerebellar pages 7-8): Nathaniel Robb Whaley, Shinsuke Fujioka, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type i: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 6:33-33, May 2011. URL: https://doi.org/10.1186/1750-1172-6-33, doi:10.1186/1750-1172-6-33. This article has 120 citations and is from a peer-reviewed journal.

3. (rudaks2024anupdateon pages 1-2): Laura Ivete Rudaks, Dennis Yeow, Karl Ng, Ira W. Deveson, Marina L. Kennerson, and Kishore Raj Kumar. An update on the adult-onset hereditary cerebellar ataxias: novel genetic causes and new diagnostic approaches. Cerebellum (London, England), 23:2152-2168, May 2024. URL: https://doi.org/10.1007/s12311-024-01703-z, doi:10.1007/s12311-024-01703-z. This article has 50 citations.

4. (schols2004autosomaldominantcerebellar pages 1-2): Ludger Schöls, Peter Bauer, Thorsten Schmidt, Thorsten Schulte, and Olaf Riess. Autosomal dominant cerebellar ataxias: clinical features, genetics, and pathogenesis. The Lancet Neurology, 3:291-304, May 2004. URL: https://doi.org/10.1016/s1474-4422(04)00737-9, doi:10.1016/s1474-4422(04)00737-9. This article has 1397 citations and is from a highest quality peer-reviewed journal.

5. (durr2010autosomaldominantcerebellar pages 1-2): Alexandra Durr. Autosomal dominant cerebellar ataxias: polyglutamine expansions and beyond. The Lancet Neurology, 9:885-894, Sep 2010. URL: https://doi.org/10.1016/s1474-4422(10)70183-6, doi:10.1016/s1474-4422(10)70183-6. This article has 851 citations and is from a highest quality peer-reviewed journal.

6. (durr2010autosomaldominantcerebellar pages 3-4): Alexandra Durr. Autosomal dominant cerebellar ataxias: polyglutamine expansions and beyond. The Lancet Neurology, 9:885-894, Sep 2010. URL: https://doi.org/10.1016/s1474-4422(10)70183-6, doi:10.1016/s1474-4422(10)70183-6. This article has 851 citations and is from a highest quality peer-reviewed journal.

7. (rudaks2024anupdateon pages 2-4): Laura Ivete Rudaks, Dennis Yeow, Karl Ng, Ira W. Deveson, Marina L. Kennerson, and Kishore Raj Kumar. An update on the adult-onset hereditary cerebellar ataxias: novel genetic causes and new diagnostic approaches. Cerebellum (London, England), 23:2152-2168, May 2024. URL: https://doi.org/10.1007/s12311-024-01703-z, doi:10.1007/s12311-024-01703-z. This article has 50 citations.

8. (rudaks2024anupdateon pages 14-15): Laura Ivete Rudaks, Dennis Yeow, Karl Ng, Ira W. Deveson, Marina L. Kennerson, and Kishore Raj Kumar. An update on the adult-onset hereditary cerebellar ataxias: novel genetic causes and new diagnostic approaches. Cerebellum (London, England), 23:2152-2168, May 2024. URL: https://doi.org/10.1007/s12311-024-01703-z, doi:10.1007/s12311-024-01703-z. This article has 50 citations.

9. (whaley2011autosomaldominantcerebellar pages 2-3): Nathaniel Robb Whaley, Shinsuke Fujioka, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type i: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 6:33-33, May 2011. URL: https://doi.org/10.1186/1750-1172-6-33, doi:10.1186/1750-1172-6-33. This article has 120 citations and is from a peer-reviewed journal.

10. (schols2004autosomaldominantcerebellar pages 5-6): Ludger Schöls, Peter Bauer, Thorsten Schmidt, Thorsten Schulte, and Olaf Riess. Autosomal dominant cerebellar ataxias: clinical features, genetics, and pathogenesis. The Lancet Neurology, 3:291-304, May 2004. URL: https://doi.org/10.1016/s1474-4422(04)00737-9, doi:10.1016/s1474-4422(04)00737-9. This article has 1397 citations and is from a highest quality peer-reviewed journal.

11. (whaley2011autosomaldominantcerebellar pages 3-5): Nathaniel Robb Whaley, Shinsuke Fujioka, and Zbigniew K Wszolek. Autosomal dominant cerebellar ataxia type i: a review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 6:33-33, May 2011. URL: https://doi.org/10.1186/1750-1172-6-33, doi:10.1186/1750-1172-6-33. This article has 120 citations and is from a peer-reviewed journal.

12. (filla1996autosomaldominantcerebellar pages 3-5): Alessandro Filla, Giuseppe De Michele, Giuseppe Campanella, Anna Perretti, Lucio Santoro, Luigi Serlenga, Michele Ragno, Olga Calabrese, Imma Castaldo, Gabriella De Joanna, and Sergio Cocozza. Autosomal dominant cerebellar ataxia type i. clinical and molecular study in 36 italian families including a comparison between sca1 and sca2 phenotypes. Journal of the Neurological Sciences, 142:140-147, Oct 1996. URL: https://doi.org/10.1016/0022-510x(96)00177-3, doi:10.1016/0022-510x(96)00177-3. This article has 40 citations and is from a peer-reviewed journal.

13. (cui2024spinocerebellarataxiasfrom pages 1-2): Zi-Ting Cui, Zong-Tao Mao, Rong Yang, Jia-Jia Li, Shan-Shan Jia, Jian-Li Zhao, Fang-Tian Zhong, Peng Yu, and Ming Dong. Spinocerebellar ataxias: from pathogenesis to recent therapeutic advances. Frontiers in Neuroscience, Jun 2024. URL: https://doi.org/10.3389/fnins.2024.1422442, doi:10.3389/fnins.2024.1422442. This article has 32 citations and is from a peer-reviewed journal.

14. (costa2024thepolyglutamineprotein pages 1-2): Rafael G. Costa, André Conceição, Carlos A. Matos, and Clévio Nóbrega. The polyglutamine protein atxn2: from its molecular functions to its involvement in disease. Cell Death &amp; Disease, Jun 2024. URL: https://doi.org/10.1038/s41419-024-06812-5, doi:10.1038/s41419-024-06812-5. This article has 39 citations and is from a peer-reviewed journal.

15. (costa2024thepolyglutamineprotein pages 6-7): Rafael G. Costa, André Conceição, Carlos A. Matos, and Clévio Nóbrega. The polyglutamine protein atxn2: from its molecular functions to its involvement in disease. Cell Death &amp; Disease, Jun 2024. URL: https://doi.org/10.1038/s41419-024-06812-5, doi:10.1038/s41419-024-06812-5. This article has 39 citations and is from a peer-reviewed journal.

16. (hernandezcarralero2024atxn3amultifunctional pages 1-2): Esperanza Hernández-Carralero, Grégoire Quinet, and Raimundo Freire. Atxn3: a multifunctional protein involved in the polyglutamine disease spinocerebellar ataxia type 3. Expert Reviews in Molecular Medicine, Sep 2024. URL: https://doi.org/10.1017/erm.2024.10, doi:10.1017/erm.2024.10. This article has 18 citations and is from a peer-reviewed journal.

17. (cui2024spinocerebellarataxiasfrom pages 2-3): Zi-Ting Cui, Zong-Tao Mao, Rong Yang, Jia-Jia Li, Shan-Shan Jia, Jian-Li Zhao, Fang-Tian Zhong, Peng Yu, and Ming Dong. Spinocerebellar ataxias: from pathogenesis to recent therapeutic advances. Frontiers in Neuroscience, Jun 2024. URL: https://doi.org/10.3389/fnins.2024.1422442, doi:10.3389/fnins.2024.1422442. This article has 32 citations and is from a peer-reviewed journal.

18. (burk1996autosomaldominantcerebellar pages 1-2): K. Bürk, M. Abele, Michael Fetter, J. Dichgans, M. Skalej, F. Laccone, O. Didierjean, A. Brice, and T. Klockgether. Autosomal dominant cerebellar ataxia type i clinical features and mri in families with sca1, sca2 and sca3. Brain : a journal of neurology, 119 ( Pt 5):1497-505, Oct 1996. URL: https://doi.org/10.1093/brain/119.5.1497, doi:10.1093/brain/119.5.1497. This article has 314 citations.

19. (mattei2024epidemiologyofspinocerebellar pages 1-2): Filippo De Mattei, Fabio Ferrandes, Salvatore Gallone, Antonio Canosa, Andrea Calvo, Adriano Chiò, and Rosario Vasta. Epidemiology of spinocerebellar ataxias in europe. Cerebellum (London, England), 23:1176-1183, Sep 2024. URL: https://doi.org/10.1007/s12311-023-01600-x, doi:10.1007/s12311-023-01600-x. This article has 38 citations.

20. (mattei2024epidemiologyofspinocerebellar pages 4-5): Filippo De Mattei, Fabio Ferrandes, Salvatore Gallone, Antonio Canosa, Andrea Calvo, Adriano Chiò, and Rosario Vasta. Epidemiology of spinocerebellar ataxias in europe. Cerebellum (London, England), 23:1176-1183, Sep 2024. URL: https://doi.org/10.1007/s12311-023-01600-x, doi:10.1007/s12311-023-01600-x. This article has 38 citations.

21. (mattei2024epidemiologyofspinocerebellar pages 5-6): Filippo De Mattei, Fabio Ferrandes, Salvatore Gallone, Antonio Canosa, Andrea Calvo, Adriano Chiò, and Rosario Vasta. Epidemiology of spinocerebellar ataxias in europe. Cerebellum (London, England), 23:1176-1183, Sep 2024. URL: https://doi.org/10.1007/s12311-023-01600-x, doi:10.1007/s12311-023-01600-x. This article has 38 citations.

22. (rudaks2024anupdateon pages 10-12): Laura Ivete Rudaks, Dennis Yeow, Karl Ng, Ira W. Deveson, Marina L. Kennerson, and Kishore Raj Kumar. An update on the adult-onset hereditary cerebellar ataxias: novel genetic causes and new diagnostic approaches. Cerebellum (London, England), 23:2152-2168, May 2024. URL: https://doi.org/10.1007/s12311-024-01703-z, doi:10.1007/s12311-024-01703-z. This article has 50 citations.

23. (bregant2025themolecularlandscape pages 1-2): Elisa Bregant, Elena Betto, Chiara Dal Secco, Jessica Zucco, Federica Baldan, Lorenzo Allegri, Incoronata Renata Lonigro, Flavio Faletra, Lorenzo Verriello, Giuseppe Damante, and Catia Mio. The molecular landscape of hereditary ataxia: a single-center study. Human Genetics, 144:545-557, Apr 2025. URL: https://doi.org/10.1007/s00439-025-02744-y, doi:10.1007/s00439-025-02744-y. This article has 1 citations and is from a peer-reviewed journal.

24. (sotopina2024specificbiomarkersin pages 5-6): Alexandra E. Soto-Piña, Caroline C. Pulido-Alvarado, Jaroslaw Dulski, Zbigniew K. Wszolek, and Jonathan J. Magaña. Specific biomarkers in spinocerebellar ataxia type 3: a systematic review of their potential uses in disease staging and treatment assessment. International Journal of Molecular Sciences, 25:8074, Jul 2024. URL: https://doi.org/10.3390/ijms25158074, doi:10.3390/ijms25158074. This article has 5 citations.

25. (sotopina2024specificbiomarkersin pages 5-5): Alexandra E. Soto-Piña, Caroline C. Pulido-Alvarado, Jaroslaw Dulski, Zbigniew K. Wszolek, and Jonathan J. Magaña. Specific biomarkers in spinocerebellar ataxia type 3: a systematic review of their potential uses in disease staging and treatment assessment. International Journal of Molecular Sciences, 25:8074, Jul 2024. URL: https://doi.org/10.3390/ijms25158074, doi:10.3390/ijms25158074. This article has 5 citations.

26. (sotopina2024specificbiomarkersin pages 2-5): Alexandra E. Soto-Piña, Caroline C. Pulido-Alvarado, Jaroslaw Dulski, Zbigniew K. Wszolek, and Jonathan J. Magaña. Specific biomarkers in spinocerebellar ataxia type 3: a systematic review of their potential uses in disease staging and treatment assessment. International Journal of Molecular Sciences, 25:8074, Jul 2024. URL: https://doi.org/10.3390/ijms25158074, doi:10.3390/ijms25158074. This article has 5 citations.

27. (NCT05822908 chunk 1):  A Safety and Pharmacokinetics Trial of VO659 in SCA1, SCA3 and HD. Vico Therapeutics B. V.. 2023. ClinicalTrials.gov Identifier: NCT05822908

28. (NCT05822908 chunk 2):  A Safety and Pharmacokinetics Trial of VO659 in SCA1, SCA3 and HD. Vico Therapeutics B. V.. 2023. ClinicalTrials.gov Identifier: NCT05822908

29. (NCT06672445 chunk 1):  Study of ARO-ATXN2 Injection in Adults With Spinocerebellar Ataxia Type 2. Arrowhead Pharmaceuticals. 2024. ClinicalTrials.gov Identifier: NCT06672445

30. (NCT06672445 chunk 2):  Study of ARO-ATXN2 Injection in Adults With Spinocerebellar Ataxia Type 2. Arrowhead Pharmaceuticals. 2024. ClinicalTrials.gov Identifier: NCT06672445

31. (ishihara2024larginineinpatients pages 1-2): Tomohiko Ishihara, Masayoshi Tada, Yoshitomi Kanemitsu, Yuji Takahashi, Kinya Ishikawa, Kensuke Ikenaka, Makito Hirano, Takanori Yokota, Eiko N. Minakawa, Katsuhisa Saito, Yoshitaka Nagai, and Osamu Onodera. L-arginine in patients with spinocerebellar ataxia type 6: a multicentre, randomised, double-blind, placebo-controlled, phase 2 trial. eClinicalMedicine, 78:102952, Dec 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102952, doi:10.1016/j.eclinm.2024.102952. This article has 8 citations and is from a peer-reviewed journal.

32. (ishihara2024larginineinpatients pages 3-4): Tomohiko Ishihara, Masayoshi Tada, Yoshitomi Kanemitsu, Yuji Takahashi, Kinya Ishikawa, Kensuke Ikenaka, Makito Hirano, Takanori Yokota, Eiko N. Minakawa, Katsuhisa Saito, Yoshitaka Nagai, and Osamu Onodera. L-arginine in patients with spinocerebellar ataxia type 6: a multicentre, randomised, double-blind, placebo-controlled, phase 2 trial. eClinicalMedicine, 78:102952, Dec 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102952, doi:10.1016/j.eclinm.2024.102952. This article has 8 citations and is from a peer-reviewed journal.

33. (ishihara2024larginineinpatients pages 6-7): Tomohiko Ishihara, Masayoshi Tada, Yoshitomi Kanemitsu, Yuji Takahashi, Kinya Ishikawa, Kensuke Ikenaka, Makito Hirano, Takanori Yokota, Eiko N. Minakawa, Katsuhisa Saito, Yoshitaka Nagai, and Osamu Onodera. L-arginine in patients with spinocerebellar ataxia type 6: a multicentre, randomised, double-blind, placebo-controlled, phase 2 trial. eClinicalMedicine, 78:102952, Dec 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102952, doi:10.1016/j.eclinm.2024.102952. This article has 8 citations and is from a peer-reviewed journal.

34. (ishihara2024larginineinpatients pages 7-8): Tomohiko Ishihara, Masayoshi Tada, Yoshitomi Kanemitsu, Yuji Takahashi, Kinya Ishikawa, Kensuke Ikenaka, Makito Hirano, Takanori Yokota, Eiko N. Minakawa, Katsuhisa Saito, Yoshitaka Nagai, and Osamu Onodera. L-arginine in patients with spinocerebellar ataxia type 6: a multicentre, randomised, double-blind, placebo-controlled, phase 2 trial. eClinicalMedicine, 78:102952, Dec 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102952, doi:10.1016/j.eclinm.2024.102952. This article has 8 citations and is from a peer-reviewed journal.

35. (ishihara2024larginineinpatients pages 4-6): Tomohiko Ishihara, Masayoshi Tada, Yoshitomi Kanemitsu, Yuji Takahashi, Kinya Ishikawa, Kensuke Ikenaka, Makito Hirano, Takanori Yokota, Eiko N. Minakawa, Katsuhisa Saito, Yoshitaka Nagai, and Osamu Onodera. L-arginine in patients with spinocerebellar ataxia type 6: a multicentre, randomised, double-blind, placebo-controlled, phase 2 trial. eClinicalMedicine, 78:102952, Dec 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102952, doi:10.1016/j.eclinm.2024.102952. This article has 8 citations and is from a peer-reviewed journal.

36. (ishihara2024larginineinpatients media dcc962d8): Tomohiko Ishihara, Masayoshi Tada, Yoshitomi Kanemitsu, Yuji Takahashi, Kinya Ishikawa, Kensuke Ikenaka, Makito Hirano, Takanori Yokota, Eiko N. Minakawa, Katsuhisa Saito, Yoshitaka Nagai, and Osamu Onodera. L-arginine in patients with spinocerebellar ataxia type 6: a multicentre, randomised, double-blind, placebo-controlled, phase 2 trial. eClinicalMedicine, 78:102952, Dec 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102952, doi:10.1016/j.eclinm.2024.102952. This article has 8 citations and is from a peer-reviewed journal.