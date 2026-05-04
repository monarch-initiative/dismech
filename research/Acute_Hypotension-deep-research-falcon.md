---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T15:41:53.839822'
end_time: '2026-05-04T16:01:05.920712'
duration_seconds: 1152.08
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Hypotension
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Hypotension
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Hypotension** covering all of the
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
- **Disease Name:** Acute Hypotension
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Hypotension** covering all of the
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


# Acute Hypotension — Disease Characteristics Research Report (2023–2024 prioritized)

## Target disease
**Disease name:** Acute hypotension (acute abnormally low blood pressure causing or risking tissue hypoperfusion)  
**MONDO ID:** Not identified in the retrieved corpus (needs direct lookup in MONDO/OLS).  
**Category:** Complex syndrome / clinical sign, not a single etiologic disease entity (cause-dependent).  

## 1. Disease Information
### 1.1 Overview (what is the disease?)
Acute hypotension is an abrupt fall in arterial blood pressure that may be transient or sustained and can lead to inadequate organ perfusion (shock physiology) and downstream organ injury depending on severity and duration. In ICU literature, hypotension definitions are highly heterogeneous—one recent systematic review identified **140 distinct definitions**—but **MAP <65 mmHg** is the most frequently used ICU threshold. (schuurmans2024hypotensionduringintensive pages 1-2)

A practical clinical framing used in bedside shock literature is that **shock is circulatory failure causing insufficient oxygen delivery to meet tissue demands**, with a “pre-shock” phase in which tissue hypoperfusion may occur even before hypotension develops. (oliveira2024uncomplicatedcirculatoryshock pages 1-2)

### 1.2 Key identifiers and coding systems
* **ICD-10:** Hypotension is coded under the I95.* family (subcodes vary by context). In US mortality administrative data, hypotension may be captured as **I95.9 (hypotension, unspecified)**, but authors caution this code may represent a terminal physiologic state rather than a primary disease entity. (asghar2026hypotensionunspecifieduncharted pages 1-3)
* **MeSH / OMIM / Orphanet / MONDO:** Not established from the retrieved sources; acute hypotension is commonly treated as a sign/syndrome rather than a monogenic disorder. (schuurmans2024hypotensionduringintensive pages 1-2, oliveira2024uncomplicatedcirculatoryshock pages 1-2)

### 1.3 Synonyms / alternative names
Common alternative labels in the retrieved literature include:
* **“Hypotension”** during ICU stay (schuurmans2024hypotensionduringintensive pages 1-2)
* **“Circulatory shock”** (syndrome-level framing) (oliveira2024uncomplicatedcirculatoryshock pages 1-2)
* **“Intraoperative hypotension (IOH)”** and **“post-induction hypotension (PIH)”** (perioperative) (maleczek2024definitionofclinically pages 7-8, ripollesmelchor2023hypotensionpredictionindex pages 2-3)
* **“Post-intubation hypotension (PIH)”** (airway/procedural) (pan2024recentadvancesin pages 1-2, anand2024impactofresuscitation pages 1-7)

### 1.4 Source type
Most information here is derived from **aggregated disease-level resources** (systematic reviews, narrative reviews, clinical cohorts, and trials), not from single-patient case series. (schuurmans2024hypotensionduringintensive pages 1-2, oliveira2024uncomplicatedcirculatoryshock pages 1-2, mohamed2024theeffectof pages 1-2)

## 2. Etiology
Acute hypotension is best handled as a **final common hemodynamic phenotype** with multiple etiologies.

### 2.1 Primary causal factors (clinical categories)
A bedside shock taxonomy remains in common use:
* **Cardiogenic:** pump failure
* **Hypovolemic (including hemorrhagic):** inadequate circulating volume
* **Obstructive:** mechanical impediment to inflow/outflow
* **Vasoplegic/distributive:** failure of peripheral vascular tone (includes sepsis and anaphylaxis)  
This classification is explicitly described in a 2024 shock narrative review. (oliveira2024uncomplicatedcirculatoryshock pages 1-2)

### 2.2 Major risk factors (examples with evidence)
**Procedure-related hypotension (peri-intubation):**
* In trauma patients undergoing prehospital emergency anesthesia, PIH (new SBP <90 mmHg within 10 min, or relative drop if baseline <90) occurred in **21.8%** (218/998). Risk associations included older age (>55 years), pre-intubation tachycardia, multisystem injury, and pre-arrival crystalloid. (anand2024impactofresuscitation pages 1-7)
* In isolated TBI requiring emergent intubation, PIH defined as SBP fall ≥20% or SBP ≤80 mmHg or MAP ≤60 mmHg occurred in **62%** (304/490). (anand2024impactofresuscitation pages 1-7)

**Anaphylaxis severity / treatment-response modifiers:**
A 2024 overview of refractory anaphylaxis guidelines notes that genetic factors may modulate severity/response, including “deficiency in platelet activating factor-acetyl hydrolase” and “hereditary alpha-tryptasaemia,” as well as mastocytosis. (pauw2024frequencyofcardiotoxicity pages 1-2)

**Sepsis-related hypotension / shock:**
Surviving Sepsis Campaign (SSC) Research Priorities 2023 identify key gaps directly tied to acute hypotension in sepsis, including: “**what is the best vasopressor approach for treating the different phases of septic shock?**” and how genetics/epigenetics influence sepsis development and treatment response. (backer2024survivingsepsiscampaign pages 1-2, backer2024survivingsepsiscampaign pages 18-20)

### 2.3 Protective factors
The retrieved corpus did not provide robust, quantified protective factors specific to “acute hypotension” as a syndrome. Some peri-intubation and hemorrhagic shock studies suggest modifiable protective interventions (e.g., pre-intubation vasopressors/HTS; early low-dose norepinephrine), which function as **preventive strategies for iatrogenic or progression-related hypotension** rather than intrinsic protective factors. (anand2024impactofresuscitation pages 1-7, mohamed2024theeffectof pages 1-2)

### 2.4 Gene–environment interactions
Direct gene–environment interaction evidence for acute hypotension was not retrieved. SSC priorities emphasize that genetics/epigenetics likely influence sepsis susceptibility, severity, and treatment response, indicating a major open research area relevant to hypotension in sepsis. (backer2024survivingsepsiscampaign pages 18-20)

## 3. Phenotypes (clinical features)
### 3.1 Core clinical phenotype
In shock physiology, skin and perfusion findings are emphasized: **cold/pale/moist/mottled skin** and prolonged **capillary refill time (CRT)**, with possible **hyperlactatemia** even before hypotension (pre-shock). (oliveira2024uncomplicatedcirculatoryshock pages 1-2)

### 3.2 Quantitative hypotension thresholds used in recent literature
Because thresholds are context-dependent, clinical research commonly operationalizes hypotension using SBP and/or MAP cutoffs and sometimes relative drops.

* **ICU (general):** MAP <65 mmHg is “most frequently used” despite heterogeneity. (schuurmans2024hypotensionduringintensive pages 1-2)
* **Sepsis trials/targets:** MAP <65 mmHg used for inclusion and MAP ≥65 mmHg used as a resuscitation target; shock control definitions often include perfusion markers (urine output and lactate change). (antonucci2024hemodynamicsupportin pages 4-5)
* **Post-intubation hypotension:** definitions include SBP <90 mmHg and/or MAP <65 mmHg and/or >20% drop from baseline; incidence reported as **19–52%** across studies. (pan2024recentadvancesin pages 1-2)
* **TBI peri-intubation (2024 cohort):** PIH defined as SBP decrease ≥20% or SBP ≤80 mmHg or MAP ≤60 mmHg. (anand2024impactofresuscitation pages 1-7)

A consolidated table of thresholds and outcome links is provided below.

| Setting/Context | Hypotension definition/threshold | Study (first author, journal, year) | Key quantitative outcome/statistic | URL/DOI |
|---|---|---|---|---|
| ICU, general critical care | Heterogeneous definitions; MAP <65 mmHg most frequently used in ICU literature; outcome associations especially pronounced when MAP <60 mmHg and SBP <90 mmHg for mortality | Schuurmans, *Intensive Care Medicine*, 2024 (schuurmans2024hypotensionduringintensive pages 1-2) | Systematic review/meta-analysis of 122 studies (176,329 patients): hypotension associated with mortality OR 1.45 (95% CI 1.12–1.88); majority of studies also linked greater hypotension severity with AKI risk | https://doi.org/10.1007/s00134-023-07304-4 |
| Sepsis / septic shock (ED-ICU transition) | MAP <65 mmHg in adults with suspected infection/sepsis; shock control target MAP >65 mmHg with urine output >0.5 mL/kg/h for 2 h or lactate decrease >10% | Antonucci summarizing CENSER, *Anesthesiology*, 2024 (antonucci2024hemodynamicsupportin pages 4-5) | Early norepinephrine trial: shock control by 6 h in 76.1% vs 48.4% with control (118/155 vs 75/155; P<0.001); lower cardiogenic pulmonary edema 14.4% vs 27.7% and new arrhythmia 11% vs 20% | https://doi.org/10.1097/ALN.0000000000004958 |
| Perioperative intraoperative hypotension (IOH) | Common algorithmic target MAP ≥65 mmHg; risk rises with deeper hypotension, especially MAP <55 mmHg; one cited IOH definition included MAP 55–59 mmHg for <10 min | Ripollés-Melchor, *Frontiers in Anesthesiology*, 2023 (ripollesmelchor2023hypotensionpredictionindex pages 2-3) | Review notes MAP <55 mmHg associated with increased AKI and postoperative myocardial infarction risk; >20 min with MAP <55 mmHg associated with higher 30-day mortality | https://doi.org/10.3389/fanes.2023.1138175 |
| Perioperative IOH, data-driven thresholds | Absolute MAP-based IOH exposure; reported median time under thresholds: <65 mmHg 4.2 min, <70 mmHg 16.2 min, <75 mmHg 33.0 min, <80 mmHg 49.2 min | Maleczek, *PLOS ONE*, 2024 (maleczek2024definitionofclinically pages 7-8) | In 65,454 patients, adverse outcome risk increased continuously with decreasing MAP; PACU length of stay was substantially influenced by IOH burden | https://doi.org/10.1371/journal.pone.0312966 |
| Post-intubation hypotension (trauma/prehospital emergency anesthesia) | New SBP <90 mmHg within 10 min of induction, or >10% SBP reduction if pre-induction SBP <90 mmHg | Price, *Scandinavian Journal of Trauma, Resuscitation and Emergency Medicine*, 2023 (anand2024impactofresuscitation pages 1-7) | 218/998 trauma patients (21.8%) had PIH; older age >55 y, tachycardia, multisystem injury, and pre-HEMS crystalloid use were associated with PIH | https://doi.org/10.1186/s13049-023-01091-z |
| Post-intubation hypotension in isolated TBI | SBP decrease ≥20% from baseline or to <80 mmHg, or any MAP decrease to ≤60 mmHg | Anand, *Journal of Trauma and Acute Care Surgery*, 2024 (anand2024impactofresuscitation pages 1-7) | 304/490 patients (62%) developed PIH; pre-intubation vasopressors and hypertonic saline were independently associated with lower odds of PIH | https://doi.org/10.1097/TA.0000000000004306 |
| Post-intubation hypotension, broad critical care literature | Commonly defined as SBP <90 mmHg, MAP <65 mmHg, or >20% drop from baseline; some definitions also include new vasopressor initiation | Pan, *Asploro Journal of Biomedical and Clinical Case Reports*, 2024 (pan2024recentadvancesin pages 1-2) | Review reports PIH incidence varies from 19% to 52% and is associated with acute myocardial infarction, renal failure, longer hospitalization, and poor overall outcomes | https://doi.org/10.36502/2024/asjbccr.6384 |
| Postoperative ICU after non-cardiac surgery | POH assessed at MAP thresholds ≤75, ≤65, and ≤55 mmHg in ICU after surgery | Smischney, *Critical Care*, 2020 (smischney2020postoperativehypotensionin pages 1-2) | MAP ≤65 mmHg: 30-day MACCE HR 1.52 and 30-day mortality HR 1.56; MAP ≤55 mmHg: 30-day MACCE HR 2.02, 30-day mortality HR 1.97, 90-day mortality HR 1.78, AKI stage II/III HR 1.68 | https://doi.org/10.1186/s13054-020-03412-5 |


*Table: This table compares commonly used acute hypotension definitions across ICU, sepsis, perioperative, peri-intubation, and postoperative settings, alongside key quantitative outcomes from the gathered evidence. It is useful for harmonizing thresholds and linking them to clinically important morbidity and mortality data.*

### 3.3 Suggested phenotype ontology mappings (HPO suggestions)
Direct ontology IDs were not present in the retrieved sources; below are **suggestions** for knowledge-base normalization:
* Hypotension (HPO: *Hypotension*)
* Shock (HPO: *Shock*)
* Decreased capillary refill time (HPO: *Abnormality of capillary refill* / prolonged CRT)
* Oliguria (HPO: *Oliguria*)
* Hyperlactatemia (HPO: *Lactic acidosis* / *Increased blood lactate*)

## 4. Genetic / Molecular Information
### 4.1 Causal genes
Acute hypotension is not typically monogenic. No causal-gene evidence for “acute hypotension” as a standalone entity was retrieved.

### 4.2 Genetic modifiers and epigenetics (most relevant in sepsis)
SSC 2023 Research Priorities explicitly identify genetics and epigenetics as an underexplored but important domain in sepsis, stating that the link between genetic factors and “susceptibility, severity and evolution of sepsis” is not fully understood. (backer2024survivingsepsiscampaign pages 18-20)

For anaphylaxis-related hypotension severity/response, guideline overviews cite candidate genetic factors such as platelet-activating-factor acetylhydrolase deficiency and hereditary alpha-tryptasemia as potential modifiers. (pauw2024frequencyofcardiotoxicity pages 1-2)

### 4.3 Molecular profiling
Not established for “acute hypotension” broadly in the retrieved evidence. For sepsis, the SSC priorities and related reviews frame precision approaches (including biology-driven stratification) as research needs rather than routine care. (backer2024survivingsepsiscampaign pages 1-2)

## 5. Environmental Information
Environmental precipitants of acute hypotension are largely **contextual exposures** (e.g., infection leading to sepsis, allergens leading to anaphylaxis, trauma/hemorrhage, anesthetic/induction drugs). The retrieved sources emphasize the need for rapid bedside differentiation rather than isolating specific toxins. (oliveira2024uncomplicatedcirculatoryshock pages 1-2, pan2024recentadvancesin pages 1-2)

## 6. Mechanism / Pathophysiology
### 6.1 Causal chain (syndrome-level)
A general mechanistic chain is: **trigger (infection/trauma/allergen/procedure) → hemodynamic disturbance (pump failure, volume loss, vasodilation/vasoplegia, obstruction) → tissue hypoperfusion and cellular hypoxia → organ dysfunction and multi-organ failure if not reversed**. (oliveira2024uncomplicatedcirculatoryshock pages 1-2)

### 6.2 Sepsis-associated mechanisms (selected)
A 2024 sepsis hemodynamics review notes that sepsis-induced organ injury can result from **microvascular dysfunction, immune and autonomic dysfunction, apoptosis, mitochondrial damage, and coagulation disorders**, framing hypotension as one component of a broader pathobiology. (antonucci2024hemodynamicsupportin pages 1-2)

### 6.3 Intubation-related hypotension mechanisms
A 2024 PIH review attributes mechanisms to **sympathetic suppression**, **vagal activation**, effects of **positive-pressure ventilation** on venous return/cardiac output, and **direct hemodynamic effects of induction drugs**, while emphasizing inconsistent diagnostic criteria across studies. (pan2024recentadvancesin pages 1-2)

### 6.4 Suggested GO / CL / UBERON mappings (high-level suggestions)
Because explicit pathway annotations were not provided in the retrieved corpus, the following are **high-level suggestions** consistent with shock biology:
* GO biological processes: regulation of blood pressure; response to hypoxia; inflammatory response; coagulation; regulation of vascular tone.
* CL cell types: vascular endothelial cell; vascular smooth muscle cell; monocyte/macrophage; cardiomyocyte.
* UBERON organs/structures: systemic arterial circulation; heart; kidney; brain; microvasculature.

## 7. Anatomical Structures Affected
Acute hypotension/shock is systemic but clinically important organ targets include:
* **Brain** (risk of hypoperfusion, especially in TBI where hypotension can exacerbate injury) (anand2024impactofresuscitation pages 1-7)
* **Kidney** (hypotension exposure associated with AKI in many observational studies; postoperative ICU hypotension at MAP ≤55 mmHg associated with AKI stage II/III) (smischney2020postoperativehypotensionin pages 1-2, schuurmans2024hypotensionduringintensive pages 1-2)
* **Heart** (major adverse cardiac/cerebrovascular events associated with postoperative ICU hypotension) (smischney2020postoperativehypotensionin pages 1-2)

## 8. Temporal Development
Acute hypotension typically has **acute onset** (minutes–hours) and may evolve through shock phases:
* **Pre-shock (compensated):** hypoperfusion may precede hypotension
* **Shock phase:** hypotension becomes manifest
* **Organ injury phase:** prolonged hypoperfusion causes organ damage/failure  
This phase framing is explicitly described in the 2024 shock narrative review. (oliveira2024uncomplicatedcirculatoryshock pages 1-2)

## 9. Inheritance and Population
Because acute hypotension is not a single inherited disorder, classic inheritance patterns are not applicable.

Epidemiology is cause- and setting-dependent; however, peri-intubation hypotension incidence estimates and ICU associations are available:
* PIH incidence **19–52%** across studies (review). (pan2024recentadvancesin pages 1-2)
* PIH incidence **62%** in isolated TBI cohort (2019–2022). (anand2024impactofresuscitation pages 1-7)

Administrative mortality analyses based on I95.9 exist but may be difficult to interpret as disease burden due to coding non-specificity. (asghar2026hypotensionunspecifieduncharted pages 1-3)

## 10. Diagnostics
### 10.1 Clinical assessment and bedside testing
A shock review recommends joint analysis of clinical data and routine tests to infer cause; **point-of-care ultrasonography and echocardiography** are described as “the most valuable non-invasive diagnostic tools.” (oliveira2024uncomplicatedcirculatoryshock pages 1-2)

Common perfusion/organ markers used in shock resuscitation frameworks include:
* **Lactate** (e.g., rising or >2 mM in one sepsis hemodynamic summary table) (antonucci2024hemodynamicsupportin pages 4-5)
* **Urine output** (e.g., >0.5 mL/kg/h targets used in shock control endpoints) (antonucci2024hemodynamicsupportin pages 4-5)
* **Capillary refill time** (e.g., >3 s referenced) (antonucci2024hemodynamicsupportin pages 4-5)

### 10.2 Dynamic assessment of fluid responsiveness (recent practical synthesis)
In shock management, dynamic tests are emphasized to avoid indiscriminate fluids:
* Passive leg raising (PLR) described as equivalent to ~300 mL fluid challenge (oliveira2024uncomplicatedcirculatoryshock pages 6-7)
* Reported diagnostic performance in one summary: PLR increase in CO ≥11% sensitivity 88%, specificity 92%; end-expiratory occlusion test cardiac index increase ≥5% sensitivity 91%, specificity 100% (oliveira2024uncomplicatedcirculatoryshock pages 6-7)

### 10.3 Differential diagnosis (etiologic workup)
Core differentials align with cardiogenic/hypovolemic/obstructive/vasoplegic shock categories and should be guided by history/exam plus ECG, radiography, labs (including troponin, BNP, D-dimer, gases, lactate), and ultrasound/echo. (oliveira2024uncomplicatedcirculatoryshock pages 1-2)

### 10.4 Coding-based ascertainment caveat
Claims databases may lack physiologic BP measurements and therefore identify hypotension using diagnosis codes, limiting severity phenotyping and mechanistic inference. (holtz2022economicoutcomesand pages 7-8)

## 11. Outcomes / Prognosis
### 11.1 ICU outcomes (2024 synthesis)
A 2024 systematic review/meta-analysis of ICU hypotension (122 studies; 176,329 patients) found hypotension associated with mortality (meta-analysis OR **1.45**, 95% CI 1.12–1.88). (schuurmans2024hypotensionduringintensive pages 1-2)

### 11.2 Postoperative ICU outcomes (reference thresholds)
In a large multi-center retrospective ICU postoperative cohort (non-cardiac surgery), postoperative hypotension at **MAP ≤65** and **≤55 mmHg** was associated with higher 30- and 90-day mortality and MACCE; MAP ≤55 was also associated with AKI stage II/III. (smischney2020postoperativehypotensionin pages 1-2)

### 11.3 Anaphylaxis treatment safety outcome statistic (2024)
Among 338 adult ED anaphylaxis patients receiving IM epinephrine, cardiotoxicity (composite definition) occurred in **4.7%** (16/338). (pauw2024frequencyofcardiotoxicity pages 1-2)

## 12. Treatment
Treatment is **cause-directed** but shares common hemodynamic stabilization principles.

### 12.1 Immediate stabilization / implementation (shock physiology)
Bedside shock care emphasizes rapid restoration of venous return and cardiac output and avoidance of delay in cause identification; POCUS/echo is central. (oliveira2024uncomplicatedcirculatoryshock pages 1-2)

### 12.2 Sepsis-associated acute hypotension: early vasopressors and MAP targets (2024 review synthesis)
A 2024 sepsis hemodynamics review describes an early resuscitation approach with **MAP target ~65 mmHg** and **norepinephrine as first-line vasopressor**, noting early vasopressors may be considered (including peripheral infusion in some contexts). (antonucci2024hemodynamicsupportin media 3450bcbc)

In the ED sepsis trial summarized in that review (CENSER), early norepinephrine increased shock control by 6 hours (**76.1% vs 48.4%**) and reduced cardiogenic pulmonary edema and new arrhythmia. (antonucci2024hemodynamicsupportin pages 4-5)

### 12.3 Hemorrhagic shock (2024 RCT)
A 2024 randomized trial in severely traumatized hemorrhagic shock patients (inclusion MAP 65–75 mmHg) reported that early low-dose norepinephrine plus fluids reduced **24-hour mortality (3% vs 13%)** and in-hospital mortality (9% vs 21%), with lower fluid requirement and improved lactate/creatinine trajectories. (mohamed2024theeffectof pages 1-2)

### 12.4 Peri-intubation hypotension prevention/mitigation (2024 TBI cohort)
In isolated TBI intubations, pre-intubation vasopressors and hypertonic saline were associated with reduced odds of PIH. (anand2024impactofresuscitation pages 1-7)

### 12.5 Anaphylaxis (guideline-aligned key points and refractory cases)
Anaphylaxis is characterized by systemic reactions that may include hypotension, and epinephrine is the core acute treatment; the 2023 practice parameter update is referenced as emphasizing that meeting diagnostic criteria is not required to treat severe reactions and that epinephrine is first-line (reviewed in 2024). (shaker2024anaphylaxisdefinitionand pages 1-2)

For **refractory anaphylaxis**, a 2024 guideline overview notes recommendations for timely aggressive fluids and IV adrenaline; the preferred second-line vasopressor is uncertain, and IV glucagon is commonly recommended for patients on beta-blockers despite limited evidence; rescue therapies include methylene blue or extracorporeal life support. (pauw2024frequencyofcardiotoxicity pages 1-2)

### 12.6 MAXO treatment ontology suggestions (high-level)
* Vasopressor therapy (e.g., norepinephrine infusion)
* Intravenous fluid therapy (balanced crystalloids)
* Point-of-care ultrasonography
* Endotracheal intubation with hemodynamic optimization/prevention of peri-intubation hypotension
* Epinephrine administration (intramuscular; intravenous infusion for refractory anaphylaxis)

## 13. Prevention
Prevention is primarily **secondary/tertiary**: preventing progression to organ injury by avoiding delays and iatrogenic hypotension.

### 13.1 Predictive/proactive hemodynamic management (perioperative)
A 2023 perioperative review describes the shift from reactive to predictive hemodynamic management (e.g., algorithms with MAP targets and vasopressors to maintain perfusion), with emphasis that deeper hypotension exposures (e.g., MAP <55 mmHg) are linked to adverse outcomes. (ripollesmelchor2023hypotensionpredictionindex pages 2-3)

## 14. Other Species / Natural Disease
No naturally occurring comparative-animal epidemiology for “acute hypotension” was retrieved. The most relevant cross-species content in the corpus pertains to **sepsis research**, where translation from animal models to humans is highlighted as a major limitation and research target. (backer2024survivingsepsiscampaign pages 18-20)

## 15. Model Organisms
SSC Research Priorities explicitly call to improve animal models so they better resemble human sepsis and to align outcome variables between animals and humans; this is directly relevant to modeling hypotension/shock mechanisms in sepsis. (backer2024survivingsepsiscampaign pages 1-2, backer2024survivingsepsiscampaign pages 18-20)

## Recent developments and expert analysis (2023–2024 highlights)
1. **Harmonization remains unresolved**: ICU hypotension remains defined in many ways (140 definitions), yet MAP <65 mmHg is still the dominant operational threshold; observational associations are consistent and severity-dependent. (schuurmans2024hypotensionduringintensive pages 1-2)
2. **Earlier vasopressor strategies** are increasingly supported in sepsis resuscitation syntheses; early norepinephrine improves short-term shock control and may reduce cardiopulmonary complications, aligning with algorithmic care maps. (antonucci2024hemodynamicsupportin pages 4-5, antonucci2024hemodynamicsupportin media 3450bcbc)
3. **Cause- and phase-specific BP targets** are emphasized as research priorities; SSC Research Priorities 2023 explicitly target improved vasopressor strategy definition across septic shock phases and deeper mechanistic understanding (including genetics/epigenetics). (backer2024survivingsepsiscampaign pages 1-2, backer2024survivingsepsiscampaign pages 18-20)
4. **Safety quantification in anaphylaxis care**: recent ED data quantify IM epinephrine cardiotoxicity at ~5%, contextualizing clinician hesitancy against life-saving benefit. (pauw2024frequencyofcardiotoxicity pages 1-2)

## Visual evidence (recent algorithm)
A 2024 sepsis hemodynamics review figure depicts early resuscitation/optimization phases and a MAP 65 mmHg target with norepinephrine as first-line vasopressor. (antonucci2024hemodynamicsupportin media 3450bcbc)

## Limitations of this report (evidence gaps)
* MONDO/MeSH/OMIM identifiers were not recoverable from the retrieved papers; direct ontology database lookup is required. (schuurmans2024hypotensionduringintensive pages 1-2, oliveira2024uncomplicatedcirculatoryshock pages 1-2)
* Many key claims about acute hypotension are intrinsically **setting- and etiology-dependent**; the strongest quantitative evidence is in ICU/sepsis/perioperative/peri-intubation contexts rather than a unified “acute hypotension” cohort. (schuurmans2024hypotensionduringintensive pages 1-2, pan2024recentadvancesin pages 1-2)

## Key cited sources (with publication dates and URLs)
* Schuurmans J. et al. **Hypotension during intensive care stay and mortality and morbidity**. *Intensive Care Medicine*. **Jan 2024**. https://doi.org/10.1007/s00134-023-07304-4 (schuurmans2024hypotensionduringintensive pages 1-2)
* Antonucci E. et al. **Hemodynamic Support in Sepsis**. *Anesthesiology*. **May 2024**. https://doi.org/10.1097/ALN.0000000000004958 (antonucci2024hemodynamicsupportin pages 1-2)
* de Oliveira M.D.C. et al. **Uncomplicated circulatory shock: a narrative review**. *einstein (São Paulo)*. **Oct 2024**. https://doi.org/10.31744/einstein_journal/2024rw0775 (oliveira2024uncomplicatedcirculatoryshock pages 1-2)
* Anand T. et al. **Impact of resuscitation adjuncts on postintubation hypotension in isolated TBI**. *J Trauma Acute Care Surg*. **Mar 2024**. https://doi.org/10.1097/TA.0000000000004306 (anand2024impactofresuscitation pages 1-7)
* Mohamed R.M. et al. **Low-dose norepinephrine before hypotensive resuscitation in hemorrhagic shock (RCT)**. *Anaesthesia, Pain & Intensive Care*. **Oct 2024**. https://doi.org/10.35975/apic.v28i5.2560 (mohamed2024theeffectof pages 1-2)
* Pauw E.K. et al. **Cardiotoxicity after IM epinephrine for anaphylaxis**. *JACEP Open*. **Feb 2024** (Accepted Dec 13, 2023). https://doi.org/10.1002/emp2.13095 (pauw2024frequencyofcardiotoxicity pages 1-2)
* De Backer D. et al. **Surviving Sepsis Campaign Research Priorities 2023**. *Critical Care Medicine*. **Jan 2024**. https://doi.org/10.1097/CCM.0000000000006135 (backer2024survivingsepsiscampaign pages 1-2)


References

1. (schuurmans2024hypotensionduringintensive pages 1-2): Jaap Schuurmans, Benthe T. B. van Rossem, Santino R. Rellum, Johan T. M. Tol, Vincent C. Kurucz, Niels van Mourik, Ward H. van der Ven, Denise P. Veelo, Jimmy Schenk, and Alexander P. J. Vlaar. Hypotension during intensive care stay and mortality and morbidity: a systematic review and meta-analysis. Intensive Care Medicine, 50:516-525, Jan 2024. URL: https://doi.org/10.1007/s00134-023-07304-4, doi:10.1007/s00134-023-07304-4. This article has 37 citations and is from a highest quality peer-reviewed journal.

2. (oliveira2024uncomplicatedcirculatoryshock pages 1-2): Mauro Dirlando Conte de Oliveira, Oscar Fernando Pavão dos Santos, Giancarlo Colombo, Thiago Domingos Corrêa, and Miguel Cendoroglo. Uncomplicated circulatory shock: a narrative review. Einstein, Oct 2024. URL: https://doi.org/10.31744/einstein\_journal/2024rw0775, doi:10.31744/einstein\_journal/2024rw0775. This article has 0 citations.

3. (asghar2026hypotensionunspecifieduncharted pages 1-3): Palwasha Asghar, Muhammad Bilal Masood, Sahla Waqas, Wajeeha Iftikhar Shah, Fatima Fazal, and Raghabendra Kumar Mahato. Hypotension, unspecified: uncharted mortality trends and disparities in the united states, a cdc wonder analysis (1999-2025). Unknown journal, Apr 2026. URL: https://doi.org/10.21203/rs.3.rs-9541628/v1, doi:10.21203/rs.3.rs-9541628/v1.

4. (maleczek2024definitionofclinically pages 7-8): Mathias Maleczek, Daniel Laxar, Angelika Geroldinger, Andreas Gleiss, Paul Lichtenegger, and Oliver Kimberger. Definition of clinically relevant intraoperative hypotension: a data-driven approach. PLOS ONE, 19:e0312966, Nov 2024. URL: https://doi.org/10.1371/journal.pone.0312966, doi:10.1371/journal.pone.0312966. This article has 7 citations and is from a peer-reviewed journal.

5. (ripollesmelchor2023hypotensionpredictionindex pages 2-3): Javier Ripollés-Melchor, Alicia Ruiz-Escobar, Paula Fernández-Valdes-Bango, Juan V. Lorente, Ignacio Jiménez-López, Alfredo Abad-Gurumeta, Laura Carrasco-Sánchez, and M. Ignacio Monge-García. Hypotension prediction index: from reactive to predictive hemodynamic management, the key to maintaining hemodynamic stability. Frontiers in Anesthesiology, Apr 2023. URL: https://doi.org/10.3389/fanes.2023.1138175, doi:10.3389/fanes.2023.1138175. This article has 28 citations.

6. (pan2024recentadvancesin pages 1-2): E. Pan and Yao Chen. Recent advances in understanding the pathophysiology and risk stratification of post-intubation hypotension. Asploro Journal of Biomedical and Clinical Case Reports, 8:20-29, Dec 2024. URL: https://doi.org/10.36502/2024/asjbccr.6384, doi:10.36502/2024/asjbccr.6384. This article has 0 citations.

7. (anand2024impactofresuscitation pages 1-7): Tanya Anand, Omar Hejazi, Madolyn Conant, Dylan Joule, Megan Lundy, Christina Colosimo, Audrey Spencer, Adam Nelson, Lou Magnotti, and Bellal Joseph. Impact of resuscitation adjuncts on postintubation hypotension in patients with isolated traumatic brain injury. Journal of Trauma and Acute Care Surgery, 97:112-118, Mar 2024. URL: https://doi.org/10.1097/ta.0000000000004306, doi:10.1097/ta.0000000000004306. This article has 3 citations and is from a peer-reviewed journal.

8. (mohamed2024theeffectof pages 1-2): Rabab Mohamed Mohamed, Atia Gad Anwar, and Ahmed Aboelhasan Eid. The effect of using low dose norepinephrine before hypotensive resuscitation in hemorrhagic shock; a randomized controlled trial. Anaesthesia, Pain &amp; Intensive Care, 28:914-921, Oct 2024. URL: https://doi.org/10.35975/apic.v28i5.2560, doi:10.35975/apic.v28i5.2560. This article has 2 citations.

9. (pauw2024frequencyofcardiotoxicity pages 1-2): Emily K. Pauw, William B. Stubblefield, Jesse O. Wrenn, Sarah K. Brown, Millie S. Cosse, Zoe S. Curry, Terence P. Darcy, Tia'Asia E. James, Paige E. Koetter, Caitlin E. Nicholson, Frank N. Parisi, Laura G. Shepherd, Savannah L. Soppet, Michael D. Stocker, Bernard M. Walston, Wesley H. Self, Jin H. Han, and Michael J. Ward. Frequency of cardiotoxicity following intramuscular administration of epinephrine in emergency department patients with anaphylaxis. JACEP Open, 5:e13095, Feb 2024. URL: https://doi.org/10.1002/emp2.13095, doi:10.1002/emp2.13095. This article has 10 citations.

10. (backer2024survivingsepsiscampaign pages 1-2): Daniel De Backer, Clifford S. Deutschman, Judith Hellman, Sheila Nainan Myatra, Marlies Ostermann, Hallie C. Prescott, Daniel Talmor, Massimo Antonelli, Luciano Cesar Pontes Azevedo, Seth R. Bauer, Niranjan Kissoon, Ignacio-Martin Loeches, Mark Nunnally, Pierre Tissieres, Antoine Vieillard-Baron, and Craig M. Coopersmith. Surviving sepsis campaign research priorities 2023. Critical Care Medicine, 52:268-296, Jan 2024. URL: https://doi.org/10.1097/ccm.0000000000006135, doi:10.1097/ccm.0000000000006135. This article has 162 citations and is from a domain leading peer-reviewed journal.

11. (backer2024survivingsepsiscampaign pages 18-20): Daniel De Backer, Clifford S. Deutschman, Judith Hellman, Sheila Nainan Myatra, Marlies Ostermann, Hallie C. Prescott, Daniel Talmor, Massimo Antonelli, Luciano Cesar Pontes Azevedo, Seth R. Bauer, Niranjan Kissoon, Ignacio-Martin Loeches, Mark Nunnally, Pierre Tissieres, Antoine Vieillard-Baron, and Craig M. Coopersmith. Surviving sepsis campaign research priorities 2023. Critical Care Medicine, 52:268-296, Jan 2024. URL: https://doi.org/10.1097/ccm.0000000000006135, doi:10.1097/ccm.0000000000006135. This article has 162 citations and is from a domain leading peer-reviewed journal.

12. (antonucci2024hemodynamicsupportin pages 4-5): Edoardo Antonucci, Bruno Garcia, and Matthieu Legrand. Hemodynamic support in sepsis. Anesthesiology, 140:1205-1220, May 2024. URL: https://doi.org/10.1097/aln.0000000000004958, doi:10.1097/aln.0000000000004958. This article has 5 citations and is from a domain leading peer-reviewed journal.

13. (smischney2020postoperativehypotensionin pages 1-2): Nathan J. Smischney, Andrew D. Shaw, Wolf H. Stapelfeldt, Isabel J. Boero, Qinyu Chen, Mitali Stevens, and Ashish K. Khanna. Postoperative hypotension in patients discharged to the intensive care unit after non-cardiac surgery is associated with adverse clinical outcomes. Critical Care, Dec 2020. URL: https://doi.org/10.1186/s13054-020-03412-5, doi:10.1186/s13054-020-03412-5. This article has 75 citations and is from a highest quality peer-reviewed journal.

14. (antonucci2024hemodynamicsupportin pages 1-2): Edoardo Antonucci, Bruno Garcia, and Matthieu Legrand. Hemodynamic support in sepsis. Anesthesiology, 140:1205-1220, May 2024. URL: https://doi.org/10.1097/aln.0000000000004958, doi:10.1097/aln.0000000000004958. This article has 5 citations and is from a domain leading peer-reviewed journal.

15. (oliveira2024uncomplicatedcirculatoryshock pages 6-7): Mauro Dirlando Conte de Oliveira, Oscar Fernando Pavão dos Santos, Giancarlo Colombo, Thiago Domingos Corrêa, and Miguel Cendoroglo. Uncomplicated circulatory shock: a narrative review. Einstein, Oct 2024. URL: https://doi.org/10.31744/einstein\_journal/2024rw0775, doi:10.31744/einstein\_journal/2024rw0775. This article has 0 citations.

16. (holtz2022economicoutcomesand pages 7-8): Margaret Holtz, Nick Liao, Jennifer H. Lin, and Carl V. Asche. Economic outcomes and incidence of postsurgical hypotension with liposomal bupivacaine vs epidural analgesia in abdominal surgeries. Journal of Health Economics and Outcomes Research, Sep 2022. URL: https://doi.org/10.36469/001c.37739, doi:10.36469/001c.37739. This article has 5 citations.

17. (antonucci2024hemodynamicsupportin media 3450bcbc): Edoardo Antonucci, Bruno Garcia, and Matthieu Legrand. Hemodynamic support in sepsis. Anesthesiology, 140:1205-1220, May 2024. URL: https://doi.org/10.1097/aln.0000000000004958, doi:10.1097/aln.0000000000004958. This article has 5 citations and is from a domain leading peer-reviewed journal.

18. (shaker2024anaphylaxisdefinitionand pages 1-2): Marcus S. Shaker. Anaphylaxis: definition and criteria. Journal of Food Allergy, 6:26-31, Jul 2024. URL: https://doi.org/10.2500/jfa.2024.6.240002, doi:10.2500/jfa.2024.6.240002. This article has 8 citations.