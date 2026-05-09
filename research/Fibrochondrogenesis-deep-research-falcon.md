---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T15:26:18.137957'
end_time: '2026-05-08T15:56:13.123493'
duration_seconds: 1794.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fibrochondrogenesis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fibrochondrogenesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Fibrochondrogenesis** covering all of the
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
- **Disease Name:** Fibrochondrogenesis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Fibrochondrogenesis** covering all of the
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


## Comprehensive Research Report: Fibrochondrogenesis (Mendelian skeletal dysplasia)

### Target disease
- **Disease name:** Fibrochondrogenesis
- **Category:** Mendelian skeletal dysplasia / type XI collagenopathy
- **MONDO ID:** Not evidenced in retrieved full-text sources (see “Evidence gaps”).

---

## 1. Disease Information

### 1.1 Overview (what is the disease?)
Fibrochondrogenesis is a **severe short-limbed skeletal dysplasia** that classically presents **prenatally** with characteristic craniofacial, thoracic, and radiographic findings and is frequently **perinatally lethal** due to thoracic insufficiency/respiratory compromise (tompson2010fibrochondrogenesisresultsfrom pages 1-2, tompson2012dominantandrecessive pages 1-3). In the landmark genetic study, Tompson et al. describe it as “**a severe, autosomal-recessive, short-limbed skeletal dysplasia**” and provide detailed clinical-radiographic-pathologic characterization (tompson2010fibrochondrogenesisresultsfrom pages 1-2).

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
- **OMIM/MIM:** **228520** (“Fibrochondrogenesis (MIM 228520)”) (tompson2010fibrochondrogenesisresultsfrom pages 1-2)
- **Orphanet, ICD-10/ICD-11, MeSH, MONDO:** Not present in the retrieved full-text excerpts (tompson2010fibrochondrogenesisresultsfrom pages 5-5, jeon2024anovelcompound pages 1-3).

### 1.3 Synonyms / alternative names in retrieved sources
- **Fibrochondrogenesis type 1** / **FBCG1** (jeon2024anovelcompound pages 1-3)

### 1.4 Evidence source types
The retrieved evidence is largely from:
- **Human clinical genetics and fetal/neonatal radiology/pathology** (case reports and molecular studies) (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3, tompson2012dominantandrecessive pages 1-3)
- **Aggregated radiology review** (type II and type XI collagenopathies) (handa2021radiologicfeaturesof pages 11-14)
- **Model organism studies** (zebrafish and mouse) supporting mechanism (lawrence2018themechanicalimpact pages 1-2, reeck2022theshapeof pages 9-11, hafez2015col11a1regulatesbone pages 1-3)

A compact identifiers/nomenclature summary is provided here:

| Disease name / label in source | Synonyms / alternative names in retrieved texts | OMIM / MIM | Described inheritance in retrieved texts | Causal gene(s) mentioned in retrieved texts | Key source (URL; publication date) | Notes on identifiers not found in retrieved texts |
|---|---|---|---|---|---|---|
| Fibrochondrogenesis | — | MIM 228520 | Severe, autosomal recessive short-limbed skeletal dysplasia (tompson2010fibrochondrogenesisresultsfrom pages 1-2) | COL11A1 identified as a disease locus (tompson2010fibrochondrogenesisresultsfrom pages 1-2) | Tompson et al., *Am J Hum Genet*; https://doi.org/10.1016/j.ajhg.2010.10.009; Nov 2010 (tompson2010fibrochondrogenesisresultsfrom pages 1-2) | Orphanet, MONDO, MeSH, and ICD identifiers were not reported in the retrieved text excerpts (tompson2010fibrochondrogenesisresultsfrom pages 5-5) |
| Fibrochondrogenesis type 1 | FBCG1; “fibrochondrogenesis type I” (jeon2024anovelcompound pages 1-3) | OMIM #228520 | Rare lethal autosomal recessive form (jeon2024anovelcompound pages 1-3) | COL11A1 (jeon2024anovelcompound pages 1-3) | Jeon et al., *Ann Pediatr Endocrinol Metab*; https://doi.org/10.6065/apem.2346150.075; Apr 2024 (jeon2024anovelcompound pages 1-3) | Orphanet, MONDO, MeSH, and ICD identifiers were not reported in the retrieved text excerpts (jeon2024anovelcompound pages 1-3) |
| Fibrochondrogenesis | — | OMIM 228520 | Both recessive and dominant forms described at a second locus; de novo dominant case reported (tompson2012dominantandrecessive pages 1-3, tompson2012dominantandrecessive pages 4-6) | COL11A2 as a second locus (tompson2012dominantandrecessive pages 1-3, tompson2012dominantandrecessive pages 12-13) | Tompson et al., *Am J Med Genet A*; https://doi.org/10.1002/ajmg.a.34406; Feb 2012 (tompson2012dominantandrecessive pages 1-3, tompson2012dominantandrecessive pages 4-6) | Orphanet, MONDO, MeSH, and ICD identifiers were not reported in the retrieved text excerpts (tompson2012dominantandrecessive pages 7-12, tompson2012dominantandrecessive pages 4-6, tompson2012dominantandrecessive pages 12-13) |
| Fibrochondrogenesis | Included among type XI collagenopathies; described alongside otospondylomegaepiphyseal dysplasia (handa2021radiologicfeaturesof pages 11-14) | — | Variably fatal; lethal autosomal recessive chondrodysplasia attributed to COL11A1 in review text (handa2021radiologicfeaturesof pages 11-14, handa2021radiologicfeaturesof pages 16-17) | COL11A1; related type XI collagenopathy context also includes COL11A2 (handa2021radiologicfeaturesof pages 16-17, handa2021radiologicfeaturesof pages 11-14) | Handa et al., *RadioGraphics*; https://doi.org/10.1148/rg.2021200075; Jan 2021 (handa2021radiologicfeaturesof pages 11-14) | OMIM/Orphanet/ICD/MeSH/MONDO identifiers were not provided in the cited review excerpts (handa2021radiologicfeaturesof pages 16-17, handa2021radiologicfeaturesof pages 11-14) |


*Table: This table summarizes the disease names, synonyms, OMIM/MIM identifiers, inheritance patterns, and causal genes for fibrochondrogenesis using only the retrieved evidence. It also flags which standard identifiers were not found in the available source excerpts.*

---

## 2. Etiology

### 2.1 Disease causal factors
Fibrochondrogenesis is primarily a **genetic disorder** caused by pathogenic variants affecting **type XI collagen**:
- **COL11A1**: established disease locus for classic autosomal recessive fibrochondrogenesis (tompson2010fibrochondrogenesisresultsfrom pages 1-2)
- **COL11A2**: identified as a **second locus**, with both recessive and **de novo dominant** fibrochondrogenesis reported (tompson2012dominantandrecessive pages 1-3, tompson2012dominantandrecessive pages 4-6)

#### Key primary-literature abstract quote (genetic causality)
Tompson et al. (2010) report: “**Fibrochondrogenesis results from mutations in the COL11A1 type XI collagen gene**” and note affected individuals were compound heterozygotes for a loss-of-function allele and a glycine-substitution triple-helical allele (tompson2010fibrochondrogenesisresultsfrom pages 1-2).

### 2.2 Risk factors
- **Genetic risk factor:** biallelic pathogenic variants in COL11A1 (AR) (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3).
- **Consanguinity/autozygosity:** a case had “unknown ancestral consanguinity” inferred from autozygous regions by SNP genotyping (tompson2010fibrochondrogenesisresultsfrom pages 1-2).

Environmental/lifestyle risk factors are **not established** in the retrieved sources.

### 2.3 Protective factors / gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved evidence for fibrochondrogenesis.

---

## 3. Phenotypes

### 3.1 Core clinical and radiographic phenotype (current understanding)
Tompson et al. describe the classic phenotype including:
- Craniofacial: **flat midface**, small nose, **anteverted nares** (tompson2010fibrochondrogenesisresultsfrom pages 1-2)
- Limbs: **significant shortening of all limb segments** with relatively normal hands/feet (tompson2010fibrochondrogenesisresultsfrom pages 1-2)
- Thorax: **small bell-shaped thorax** (tompson2010fibrochondrogenesisresultsfrom pages 1-2)
- Radiographs: **short long bones with broad metaphyseal ends (“dumb-bell shape”)**, short ribs with metaphyseal cupping, and **flat vertebral bodies with “pinched” appearance** (hypoplastic posterior end; rounded anterior end) (tompson2010fibrochondrogenesisresultsfrom pages 1-2)
- Histopathology: growth plate with **fibroblastic chondrocytes** and **fibrous cartilage extracellular matrix**; collagen fibrils appear “frayed and irregular” on EM (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3)

The 2024 Korean survivor case (COL11A1 compound heterozygote) highlights that **phenotypic severity can vary** by genotype and can include short stature and dysmorphism with survivorship into childhood (jeon2024anovelcompound pages 1-3).

### 3.2 Phenotype ontology mapping (HPO) and anatomical structures (UBERON)
A structured mapping of major features to suggested **HPO** and **UBERON** terms is provided here:

| Phenotype description (as in sources) | Suggested HPO term (name + HP:ID) | Typical onset | Notes on frequency/severity | Key anatomic structure (with UBERON if known) | Supporting citation context IDs |
|---|---|---|---|---|---|
| Severe short-limbed skeletal dysplasia / significant shortening of all limb segments | Short limb (HP:0009826); Micromelia (HP:0002983) | Prenatal | Core, severe feature; often detected on prenatal imaging | Limb skeleton (UBERON:0001032); long bone of lower limb (UBERON:0000981) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3) |
| Flat midface with small nose and anteverted nares / severe midface hypoplasia | Midface retrusion (HP:0011800); Anteverted nares (HP:0000463); Flat face (HP:0000276) | Prenatal / neonatal | Characteristic craniofacial gestalt | Face (UBERON:0001456); middle face region (UBERON:0011822) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3, handa2021radiologicfeaturesof pages 11-14) |
| Small bell-shaped thorax | Bell-shaped thorax (HP:0001591); Narrow chest (HP:0000774) | Prenatal / neonatal | Major severity marker; contributes to respiratory compromise/perinatal lethality | Thoracic cage (UBERON:0000915) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, tompson2012dominantandrecessive pages 1-3, jeon2024anovelcompound pages 1-3) |
| Protuberant abdomen | Protuberant abdomen (HP:0001538) | Prenatal / neonatal | Reported in classic clinical description | Abdomen (UBERON:0000916) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2) |
| Long bones severely short, broad metaphyseal ends, dumbbell-shaped with metaphyseal widening/flaring | Metaphyseal widening (HP:0003026); Dumbbell-shaped long bone (HP:0003305) | Prenatal / neonatal | Hallmark radiographic feature; severe | Long bone metaphysis (UBERON:0006374); long bone (UBERON:0002495) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, tompson2012dominantandrecessive pages 4-6, handa2021radiologicfeaturesof pages 11-14) |
| Short ribs with metaphyseal cupping / anterior rib cupping | Short rib (HP:0000885); Cupped ribs (suggested HPO if used locally; exact HP uncertain) | Prenatal / neonatal | Frequent radiographic clue in severe cases | Rib (UBERON:0000974) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, tompson2012dominantandrecessive pages 1-3, tompson2012dominantandrecessive pages 4-6) |
| Flat vertebral bodies / platyspondyly / pear-shaped vertebral bodies | Platyspondyly (HP:0000926); Pear-shaped vertebrae (HP:0002938) | Prenatal / neonatal | Hallmark axial skeletal finding; often severe | Vertebral body (UBERON:0002415); vertebral column (UBERON:0001130) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3, handa2021radiologicfeaturesof pages 11-14) |
| Vertebral bodies with hypoplastic posterior and rounded anterior ends producing a pinched appearance | Vertebral body hypoplasia (HP:0002650); Abnormal vertebral body morphology (HP:0003312) | Prenatal / neonatal | Distinctive lateral radiographic appearance | Vertebral body (UBERON:0002415) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, tompson2012dominantandrecessive pages 1-3, rebello2023col11a2asa pages 1-2) |
| Multilevel coronal clefts / dorsally wedged vertebral bodies | Coronal cleft vertebrae (HP:0004602); Vertebral wedging (HP:0004586) | Prenatal / neonatal | Distinguishes fibrochondrogenesis from some related dysplasias | Vertebral body (UBERON:0002415); lumbar vertebra (UBERON:0002414) | (handa2021radiologicfeaturesof pages 11-14) |
| Delayed vertebral ossification / delayed ossification of cervical vertebral bodies | Delayed skeletal ossification (HP:0002750); Delayed ossification of vertebral bodies (suggested) | Prenatal | Seen in severe fetal cases | Vertebral column (UBERON:0001130); cervical vertebra (UBERON:0002413) | (tompson2012dominantandrecessive pages 7-12, handa2021radiologicfeaturesof pages 11-14) |
| Small ilia with hypoplastic ischia and pubis / pelvic hypoplasia | Hypoplastic ilia (HP:0008818); Ischiopubic hypoplasia (suggested) | Prenatal / neonatal | Supports radiographic diagnosis in severe cases | Ilium (UBERON:0001137); ischium (UBERON:0001274); pubis (UBERON:0001275) | (tompson2012dominantandrecessive pages 7-12, tompson2012dominantandrecessive pages 12-13) |
| Relatively normal hands and feet | Normal hands and feet / absence of major acromelic shortening (no direct HPO disease term) | Prenatal / neonatal | Helpful negative discriminator in classic description | Hand (UBERON:0002398); foot (UBERON:0002399) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2) |
| Short stature | Short stature (HP:0004322) | Prenatal to childhood | Common among survivors; severity variable by genotype | Whole body (UBERON:0000468) | (jeon2024anovelcompound pages 1-3, handa2021radiologicfeaturesof pages 11-14) |
| Myopia | Myopia (HP:0000545) | Childhood / later in survivors; also mild in some carriers | Reported in affected individuals and some heterozygous carriers | Eye (UBERON:0000970) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3) |
| Cataracts | Cataract (HP:0000518) | Childhood / later in survivors | Reported in clinical spectrum of FBCG1 | Lens of eye (UBERON:0001769) | (jeon2024anovelcompound pages 1-3) |
| Sensorineural hearing loss / early-onset hearing loss | Sensorineural hearing impairment (HP:0000407) | Childhood / early onset | Reported in survivors; mild/early-onset in some carriers | Inner ear (UBERON:0002517); cochlea (UBERON:0002245) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3) |
| Micrognathia | Micrognathia (HP:0000347) | Prenatal / neonatal | Recurrent craniofacial feature | Mandible (UBERON:0001684) | (reeck2022theshapeof pages 9-11, jeon2024anovelcompound pages 1-3) |
| Clinodactyly of fifth digits | Clinodactyly (HP:0030084); Fifth finger clinodactyly (HP:0004209) | Childhood | Observed in surviving 2024 case | Fifth finger (UBERON:0006048) | (jeon2024anovelcompound pages 1-3) |
| Webbed neck | Webbed neck (HP:0000465) | Childhood | Reported in surviving 2024 case; not clearly known as common | Neck (UBERON:0000974) | (jeon2024anovelcompound pages 1-3) |
| Straight spine / abnormal spinal curvature reported in disease spectrum | Abnormality of the vertebral column (HP:0000925); Kyphosis/Scoliosis if present (HP:0002808/HP:0002650 as applicable) | Prenatal to childhood | Spinal curvature abnormalities mentioned across reports/models; variable | Vertebral column (UBERON:0001130) | (reeck2022theshapeof pages 9-11, jeon2024anovelcompound pages 1-3) |
| Fibroblastic appearance of chondrocytes and fibrous cartilage extracellular matrix on growth-plate histology | Abnormal cartilage histology (HP:0031843); Fibrous cartilage matrix (suggested descriptive annotation) | Prenatal / fetal pathology | Defining pathologic feature underlying disease name | Growth plate cartilage (UBERON:0001485); cartilage tissue (UBERON:0002418) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3, handa2021radiologicfeaturesof pages 11-14) |


*Table: This table maps major clinical, radiographic, and histopathologic features reported for fibrochondrogenesis to suggested HPO and anatomic UBERON terms. It is designed to support structured disease knowledge-base curation and phenotype annotation from the cited source contexts.*

### 3.3 Quality-of-life impact
Direct quality-of-life instrument data (e.g., EQ-5D/SF-36) were not identified in retrieved texts. However, for survivors, the condition can involve chronic skeletal dysplasia with potential ophthalmic and auditory complications requiring ongoing surveillance (jeon2024anovelcompound pages 1-3).

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **COL11A1** (type XI collagen α1 chain) is a key causal gene; Tompson et al. identify COL11A1 as the cartilage-selective candidate and report compound heterozygous pathogenic variants (tompson2010fibrochondrogenesisresultsfrom pages 1-2).
- **COL11A2** (type XI collagen α2 chain) is a second locus; Tompson et al. report both recessive and dominant fibrochondrogenesis due to COL11A2 variants (tompson2012dominantandrecessive pages 1-3, tompson2012dominantandrecessive pages 4-6).

### 4.2 Pathogenic variants (representative examples from retrieved sources)
A structured gene/variant table is provided here:

| Gene | Disorder context | Inheritance | Variant(s) with HGVS as reported | Variant type | Evidence notes | Source with URL and publication month/year |
|---|---|---|---|---|---|---|
| **COL11A1** | Fibrochondrogenesis / FBCG1 | Autosomal recessive | Specific HGVS not fully shown in excerpt; two independent cases each had one **loss-of-function** allele plus one **glycine-substitution missense** allele in **COL11A1** | LoF + missense | Landmark study establishing **COL11A1** as a fibrochondrogenesis locus; affected individuals were **compound heterozygotes**; carrier parents had myopia or early-onset hearing loss (tompson2010fibrochondrogenesisresultsfrom pages 1-2) | Tompson et al. *Am J Hum Genet* (Nov 2010), https://doi.org/10.1016/j.ajhg.2010.10.009 (tompson2010fibrochondrogenesisresultsfrom pages 1-2) |
| **COL11A1** | Fibrochondrogenesis type 1 (FBCG1) | Autosomal recessive | **c.3478C>G (p.Pro1160Ala)**; **c.2771C>T (p.Pro924Leu)** | Missense + missense | Korean case; **compound heterozygous** variants confirmed **in trans** from father and mother; **p.Pro1160Ala** was novel and reclassified from VUS to likely pathogenic after segregation analysis (jeon2024anovelcompound pages 1-3) | Jeon et al. *Ann Pediatr Endocrinol Metab* (Apr 2024), https://doi.org/10.6065/apem.2346150.075 (jeon2024anovelcompound pages 1-3) |
| **COL11A2** | Fibrochondrogenesis | Autosomal recessive | **IVS18+3insG**; predicted protein effect **p.556_573del18** | Splice-site leading to in-frame exon-skipping deletion | Recessive case at second locus; splice donor change caused **exon 18 skipping** and predicted deletion of 18 amino acids in the triple-helical domain (tompson2012dominantandrecessive pages 1-3, tompson2012dominantandrecessive pages 12-13) | Tompson et al. *Am J Med Genet A* (Feb 2012), https://doi.org/10.1002/ajmg.a.34406 (tompson2012dominantandrecessive pages 1-3, tompson2012dominantandrecessive pages 12-13) |
| **COL11A2** | Fibrochondrogenesis | Autosomal dominant | **c.2899_2907del9**; predicted protein effect **p.967_969del3** | In-frame deletion | Dominant case at second locus; variant was **de novo**, providing evidence for an **autosomal dominant form** of fibrochondrogenesis (tompson2012dominantandrecessive pages 1-3, tompson2012dominantandrecessive pages 12-13, tompson2012dominantandrecessive pages 4-6) | Tompson et al. *Am J Med Genet A* (Feb 2012), https://doi.org/10.1002/ajmg.a.34406 (tompson2012dominantandrecessive pages 1-3, tompson2012dominantandrecessive pages 4-6) |
| **COL11A1** | Fibrochondrogenesis (expanded molecular spectrum) | Autosomal recessive | “**homozygous null mutations**” (exact HGVS not provided in retrieved excerpt) | LoF / null | Review-style citation trail notes UAE patients with **two COL11A1 homozygous null mutations**, supporting recessive severe disease; exact variant strings were not present in the available excerpt (reeck2022theshapeof pages 11-13, hall2024fetalandperinatal pages 61-63) | Referenced within Reeck et al. *J Dev Biol* (Sep 2022), https://doi.org/10.3390/jdb10040040; and Hall et al. cited in excerpt (reeck2022theshapeof pages 11-13, hall2024fetalandperinatal pages 61-63) |


*Table: This table summarizes causal genes and representative pathogenic variants reported for fibrochondrogenesis in the retrieved sources, including inheritance pattern, variant class, and the evidence context. It is useful for quickly mapping the molecular heterogeneity of COL11A1- and COL11A2-related fibrochondrogenesis.*

Key 2023–2024 update (prioritized):
- **2024 (Jeon et al.)** report a Korean case of FBCG1 with compound heterozygous **COL11A1** missense variants **c.3478C>G (p.Pro1160Ala)** (novel; absent from gnomAD v2.1.1/v3 in the report; REVEL 0.649) and **c.2771C>T (p.Pro924Leu)**, with segregation demonstrating the variants are in trans (jeon2024anovelcompound pages 1-3).

### 4.3 Variant functional consequences (high-level)
The primary mechanism is **extracellular matrix (ECM) structural failure** from impaired type XI collagen, affecting cartilage collagen fibril organization and downstream endochondral skeletal development (tompson2012dominantandrecessive pages 4-6, lawrence2018themechanicalimpact pages 1-2).

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities specific to fibrochondrogenesis were identified in the retrieved sources.

---

## 5. Environmental Information
No specific environmental, lifestyle, or infectious contributors were identified in the retrieved evidence; fibrochondrogenesis is treated as a primarily genetic disorder in these sources (tompson2010fibrochondrogenesisresultsfrom pages 1-2, tompson2012dominantandrecessive pages 1-3).

---

## 6. Mechanism / Pathophysiology

### 6.1 Current mechanistic model (genotype → phenotype causal chain)
Evidence across human pathology and animal models supports:
1) **COL11A1/COL11A2 variants** disrupt type XI collagen in cartilage (tompson2010fibrochondrogenesisresultsfrom pages 1-2, tompson2012dominantandrecessive pages 4-6).
2) Disruption of type XI collagen destabilizes the collagen network; in zebrafish **col11a2** mutants, **type II collagen is made but prematurely degraded** in maturing cartilage (lawrence2018themechanicalimpact pages 1-2).
3) The abnormal ECM is linked to altered chondrocyte organization and tissue-level biomechanics; zebrafish mutants show altered joint morphology and increased stiffness measured by AFM (lawrence2018themechanicalimpact pages 1-2).
4) These disruptions manifest as the characteristic fetal skeletal dysplasia pattern (short, flared long bones; platyspondyly; small thorax), often with perinatal respiratory compromise (tompson2010fibrochondrogenesisresultsfrom pages 1-2, tompson2012dominantandrecessive pages 1-3).

#### Direct abstract quotes supporting mechanism (model organism)
- Lawrence et al. (2018) state: “**in col11a2 mutants, type II collagen is made but is prematurely degraded** in maturing cartilage” and that these changes correlate with increased stiffness of bone and cartilage (lawrence2018themechanicalimpact pages 1-2).

### 6.2 Ontology suggestions (GO, CL)
A structured mechanism table with suggested **GO biological process** and **CL cell type** terms is provided here:

| Level | Mechanistic statement (genotype→phenotype causal chain) | Evidence type (human/model) | Suggested GO biological process terms and CL terms | Supporting context IDs |
|---|---|---|---|---|
| Molecular | Pathogenic variants in **COL11A1** or **COL11A2** disrupt type XI collagen, a minor but structurally critical cartilage collagen that helps organize and stabilize the type II/XI heterotypic fibril network; abnormal triple-helical chains or loss of chain production impair fibril assembly and matrix integrity, initiating fibrochondrogenesis/type XI collagenopathy phenotypes. | Human genetics + model-organism mechanistic inference | GO: collagen fibril organization (GO:0030199); extracellular matrix organization (GO:0030198); skeletal system development (GO:0001501). CL: chondrocyte (CL:0000138) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, tompson2012dominantandrecessive pages 4-6, lawrence2018themechanicalimpact pages 1-2, hafez2015col11a1regulatesbone pages 1-3) |
| Molecular | In zebrafish **col11a2** mutants, type II collagen is still synthesized but becomes **prematurely degraded** in maturing cartilage and ectopically localized in the joint, indicating that type XI collagen is required upstream for type II collagen stability and correct matrix distribution. | Model organism (zebrafish) | GO: collagen catabolic process (GO:0030574); protein-containing complex assembly / extracellular matrix assembly (GO:0065003, GO:0030198); cartilage development (GO:0051216). CL: chondrocyte (CL:0000138) | (lawrence2018themechanicalimpact pages 1-2, lawrence2018themechanicalimpact pages 12-12) |
| Cellular | Loss of **col11a1a** disrupts chondrocyte organization in Meckel’s cartilage: cells fail to intercalate and stack into normal columnar arrays, consistent with altered cell-matrix interactions during cartilage morphogenesis. This cellular disorganization plausibly contributes to shortened, misshapen skeletal elements. | Model organism (zebrafish) | GO: chondrocyte differentiation (GO:0002063); cartilage morphogenesis (GO:0060536); cell-matrix adhesion (GO:0007160); regulation of cell shape (GO:0008360). CL: chondrocyte (CL:0000138); fibroblast-like cell / mesenchymal cell (CL:0000057) | (reeck2022theshapeof pages 9-11, reeck2017theroleof pages 40-45) |
| Cellular | Human fetal pathology shows **fibroblastic-appearing chondrocytes** and fibrous cartilage extracellular matrix; ultrastructurally, collagen fibrils are frayed and irregular. This links mutant collagen XI directly to abnormal chondrocyte phenotype and aberrant matrix ultrastructure. | Human clinical pathology | GO: cartilage development (GO:0051216); extracellular matrix organization (GO:0030198); endochondral bone morphogenesis (GO:0060350). CL: chondrocyte (CL:0000138); fibroblast (CL:0000057) | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3) |
| Tissue | Matrix-level defects alter the **mechanical properties** of cartilage and bone: zebrafish **col11a2** mutants show increased stiffness and altered joint shape/material behavior, indicating that ECM disorganization is translated into abnormal tissue biomechanics. | Model organism (zebrafish) | GO: extracellular matrix organization (GO:0030198); cartilage development (GO:0051216); ossification (GO:0001503). CL: chondrocyte (CL:0000138); osteoblast (CL:0000062) | (lawrence2018themechanicalimpact pages 1-2, lawrence2018themechanicalimpact pages 12-12) |
| Tissue | In mouse **Col11a1** deficiency, absent Col11a1 cannot be functionally compensated by alternate triple-helical assemblies, leading to defects in epiphyseal cartilage, periosteal/bone collar formation, vertebral body formation, and trabecular/cortical bone microarchitecture. | Model organism (mouse) | GO: collagen fibril organization (GO:0030199); endochondral ossification (GO:0001958); bone mineralization (GO:0030282); osteoblast differentiation (GO:0001649). CL: chondrocyte (CL:0000138); osteoblast (CL:0000062); osteocyte (CL:0000638) | (hafez2015col11a1regulatesbone pages 1-3) |
| Organ | In the developing spine, **COL11A2** loss-of-function causes vertebral fusions due to mineralization across intervertebral segments; patient missense variants fail to rescue this phenotype in zebrafish, supporting a causal chain from collagen XI dysfunction to abnormal vertebral segmentation and “pinched”/fused vertebral phenotypes. | Human genetics + zebrafish functional validation | GO: vertebral development (broadly skeletal system development, GO:0001501); biomineral tissue development (GO:0031214); regulation of ossification (GO:0030278). CL: chondrocyte (CL:0000138); notochord-associated mesenchymal derivatives not specifically resolved in source | (rebello2023col11a2asa pages 1-2) |
| Organ | Craniofacial abnormalities (midface hypoplasia, micrognathia, altered jaw cartilage shape) can be explained by impaired collagen XI-dependent craniofacial cartilage morphogenesis and abnormal adjacent mineralization, demonstrated in zebrafish **col11a1a** models and reflected in human fibrochondrogenesis. | Human clinical + model organism | GO: craniofacial cartilage development (related cartilage development, GO:0051216); biomineral tissue development (GO:0031214); skeletal system morphogenesis (GO:0048705). CL: chondrocyte (CL:0000138); osteoblast (CL:0000062) | (reeck2022theshapeof pages 9-11, reeck2022theshapeof pages 11-13) |
| Organ | Small thorax and severe long-bone/vertebral dysplasia likely represent downstream consequences of generalized cartilage matrix failure during prenatal endochondral skeletal development, explaining frequent **perinatal lethality** from thoracic insufficiency/respiratory compromise in severe cases. | Human clinical/radiographic inference | GO: endochondral ossification (GO:0001958); skeletal system development (GO:0001501); cartilage development (GO:0051216). CL: chondrocyte (CL:0000138); osteoblast (CL:0000062) | (tompson2012dominantandrecessive pages 1-3, tompson2010fibrochondrogenesisresultsfrom pages 1-2, handa2021radiologicfeaturesof pages 11-14, tompson2012dominantandrecessive pages 4-6) |
| Pathway hypothesis | Source authors propose that some downstream effects of **col11a1a** loss may involve disrupted **non-canonical Wnt/planar cell polarity**, integrin-matrix interactions, and possibly BMP/Wnt signaling, but these remain mechanistic hypotheses rather than established disease pathways in fibrochondrogenesis. | Model-organism hypothesis / interpretive | GO: planar cell polarity pathway involved in axis elongation (related PCP processes; exact GO uncertain); cell-matrix adhesion (GO:0007160); Wnt signaling pathway (GO:0016055); BMP signaling pathway (GO:0030509). CL: chondrocyte (CL:0000138) | (reeck2022theshapeof pages 9-11) |


*Table: This table summarizes the main mechanistic links from COL11A1/COL11A2 variation to cartilage matrix dysfunction, abnormal skeletal morphogenesis, and organ-level phenotypes in fibrochondrogenesis and related type XI collagenopathies. It integrates human pathology/genetics with zebrafish and mouse model evidence and suggests ontology terms useful for structured annotation.*

---

## 7. Anatomical Structures Affected
Primary affected systems are the **skeletal system** (appendicular and axial skeleton) and **cartilage growth plates**, with frequent involvement of the **thoracic cage** and **vertebral bodies** (tompson2010fibrochondrogenesisresultsfrom pages 1-2, handa2021radiologicfeaturesof pages 11-14). The phenotypic mapping table provides suggested UBERON terms for major sites (artifact-02).

---

## 8. Temporal Development

- **Onset:** typically **prenatal**, with suspicion often beginning when limb shortening is seen on screening ultrasound (nishimura2023prenataldiagnosisof pages 1-2, tompson2010fibrochondrogenesisresultsfrom pages 1-2).
- **Course:** severe cases are often **perinatal lethal**; survivorship into childhood is possible in milder genotypes (e.g., 2024 case) (jeon2024anovelcompound pages 1-3).

Formal staging systems are not described in the retrieved sources.

---

## 9. Inheritance and Population

### 9.1 Inheritance
- Classic fibrochondrogenesis/FBCG1 is **autosomal recessive** with biallelic COL11A1 variants (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3).
- **COL11A2** can cause **recessive** disease (splice-associated in-frame deletion) and also **autosomal dominant** fibrochondrogenesis via **de novo** in-frame deletion; counseling should consider **parental germline mosaicism** (tompson2012dominantandrecessive pages 4-6).

### 9.2 Epidemiology and rarity
Quantitative population incidence/prevalence specifically for fibrochondrogenesis is sparse in the retrieved texts. Available estimates include:
- Tompson et al. (2012) suggest: “**perhaps less than 1 in 1,000,000 births in outbred populations**,” implying a **carrier frequency of ~1 in 500** under Hardy–Weinberg assumptions (tompson2012dominantandrecessive pages 4-6).
- Jeon et al. (2024) note: “**About 22 cases have been reported worldwide**” (case-report-based count) (jeon2024anovelcompound pages 1-3).

For context on skeletal dysplasias more broadly (not fibrochondrogenesis-specific):
- Nishimura et al. (2023) report prenatal bone dysplasias have prevalence **2.1–2.4 per 10,000**, and lethal bone dysplasias about **1.1 per 10,000**, contributing about **1 out of 100 perinatal deaths** (nishimura2023prenataldiagnosisof pages 1-2).

### 9.3 Risk/protective factors beyond genetics
No environmental or lifestyle risk modifiers were established for fibrochondrogenesis in the retrieved evidence.

---

## 10. Diagnostics

### 10.1 Imaging and diagnostic workflow
A current, real-world prenatal skeletal dysplasia workflow emphasizes that:
- Limb shortening on screening ultrasound prompts more detailed evaluation.
- Additional imaging (detailed US, **MRI**, **CT**) can refine diagnosis.
- **Imaging remains critical** because genetic testing identifies variants but not necessarily pathogenicity without phenotypic correlation (nishimura2023prenataldiagnosisof pages 1-2).

Radiographic hallmarks specific to fibrochondrogenesis include dumbbell long bones with metaphyseal widening, platyspondyly and distinctive vertebral body changes, rib cupping, and severe thoracic narrowing in lethal cases (tompson2010fibrochondrogenesisresultsfrom pages 1-2, tompson2012dominantandrecessive pages 4-6, handa2021radiologicfeaturesof pages 11-14).

### 10.2 Genetic testing
Demonstrated approaches include:
- Targeted sequencing of all coding exons/splice junctions in **COL11A1** (Tompson et al.) (tompson2010fibrochondrogenesisresultsfrom pages 1-2)
- Whole-exome sequencing with parental segregation testing (Jeon et al. 2024) (jeon2024anovelcompound pages 1-3)
- SNP genotyping for autozygosity mapping in recessive suspicion (tompson2010fibrochondrogenesisresultsfrom pages 1-2)

### 10.3 Pathology
The diagnosis is supported by characteristic cartilage histology (“fibroblastic” chondrocytes; fibrous matrix) and EM findings (frayed collagen fibrils) (tompson2010fibrochondrogenesisresultsfrom pages 1-2).

### 10.4 Differential diagnosis
Fibrochondrogenesis overlaps with other collagenopathies (e.g., Kniest dysplasia) but can be distinguished by severity and vertebral changes (e.g., multilevel coronal clefts and dorsally wedged vertebral bodies in type XI collagenopathies) (handa2021radiologicfeaturesof pages 11-14).

A structured diagnostics/management summary is provided here:

| Domain | Key findings/approach | Real-world implementation notes | Treatment/management options | Sources |
|---|---|---|---|---|
| Prenatal suspicion | Fibrochondrogenesis is typically suspected when fetal limb shortening is detected on screening ultrasound; lethal skeletal dysplasia workup should then assess thoracic size, vertebral abnormalities, and overall pattern of shortening. Prenatal diagnosis of skeletal dysplasias generally proceeds from detailed US to MRI and/or CT when needed. | In practice, obstetric screening US is the entry point; multidisciplinary fetal imaging is emphasized because molecular findings require imaging correlation for pathogenic interpretation. Postmortem radiography/autopsy remains valuable when pregnancy is terminated or fetal demise occurs. | No disease-specific prenatal therapy identified; management is diagnostic/prognostic counseling, delivery planning, and family counseling regarding lethality and recurrence risk. (nishimura2023prenataldiagnosisof pages 1-2, hall2024fetalandperinatal pages 61-63) | (nishimura2023prenataldiagnosisof pages 1-2, hall2024fetalandperinatal pages 61-63) |
| Imaging modalities | Radiographic hallmarks include severely short dumbbell-shaped long bones with metaphyseal widening/flaring, short ribs with cupping, platyspondyly/flat vertebral bodies, pear-shaped or "pinched" vertebrae, and in some cases multilevel coronal clefts. | Real-world diagnosis uses prenatal ultrasound first, with fetal/postnatal radiographs to refine differential diagnosis against other lethal dysplasias such as achondrogenesis, Kniest dysplasia, and otospondylomegaepiphyseal dysplasia. Example radiographs were reported at 21 and 32 weeks' gestation. | Imaging primarily guides prognosis and differential diagnosis; no imaging-directed intervention was identified. Small thorax on imaging implies risk of perinatal respiratory compromise and need for anticipatory counseling. | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, handa2021radiologicfeaturesof pages 11-14, tompson2012dominantandrecessive pages 7-12, tompson2012dominantandrecessive pages 1-3) |
| Genetic testing | Confirmatory diagnosis is achieved by molecular testing of COL11A1 and COL11A2. Reported successful approaches include whole-exome sequencing, targeted sequencing of all coding exons/splice junctions, SNP genotyping for autozygosity/homozygosity mapping, and parental segregation testing. | Current implementation includes WES in undiagnosed skeletal dysplasia and trio/segregation testing to establish variants in trans or de novo status. In the 2024 Korean case, WES identified compound heterozygous COL11A1 variants and segregation upgraded one novel variant from VUS to likely pathogenic. | Genetic confirmation enables family testing, recurrence-risk counseling, and targeted surveillance of relatives/carriers where appropriate. Counseling must consider autosomal recessive disease, de novo dominant COL11A2 cases, and possible parental germline mosaicism. | (jeon2024anovelcompound pages 1-3, tompson2010fibrochondrogenesisresultsfrom pages 1-2, tompson2012dominantandrecessive pages 4-6) |
| Pathology / histology | The disorder name derives from growth-plate pathology: chondrocytes have a fibroblastic appearance and there are regions of fibrous cartilage extracellular matrix; electron microscopy shows frayed, irregular collagen fibrils. | Histopathology is most relevant in fetal pathology/postmortem confirmation and in difficult differential diagnosis when imaging is suggestive but not definitive. | No pathology-directed treatment identified; pathology mainly supports definitive diagnosis and disease classification. | (tompson2010fibrochondrogenesisresultsfrom pages 1-2, jeon2024anovelcompound pages 1-3) |
| Supportive clinical management | Surviving patients may require longitudinal orthopedic, audiologic, and ophthalmologic assessment because reported phenotypes can include short stature, hearing loss, myopia, and cataracts. | A 2024 survivor case underwent ophthalmologic and audiometric assessments after genetic diagnosis, illustrating real-world surveillance after diagnosis. | No specific therapy exists for FBCG1 according to the 2024 case report. Supportive care consists of surveillance for ophthalmic/hearing complications and standard multidisciplinary skeletal dysplasia management. | (jeon2024anovelcompound pages 1-3) |
| Growth-related treatment | Evidence is extremely limited. A prior small report cited in the 2024 case noted growth hormone use in three COL11A1 cases. | This is not established standard of care for fibrochondrogenesis; evidence appears anecdotal/case-based rather than trial-based. No fibrochondrogenesis-specific clinical trials were identified in retrieved records. | Growth hormone was reported to increase growth velocity to 9.1 cm/year and height by +1.5 SDS during the first treatment year in three COL11A1 cases, but this should be interpreted cautiously due to sparse evidence. | (jeon2024anovelcompound pages 1-3) |


*Table: This table summarizes how fibrochondrogenesis is recognized and confirmed in practice, from prenatal suspicion through imaging, genetics, and pathology. It also condenses the limited current management evidence, highlighting that care is mainly supportive and surveillance-based, with only sparse anecdotal treatment data.*

---

## 11. Outcome / Prognosis
Most cases are described as **perinatal lethal** or **variably fatal** with lethality linked to thoracic hypoplasia/respiratory compromise (tompson2012dominantandrecessive pages 1-3, handa2021radiologicfeaturesof pages 11-14). Quantitative survival rates (e.g., 1-year survival) were not available in the retrieved excerpts.

Survivors can have persistent skeletal dysplasia with potential ophthalmic/audiologic complications, illustrated by the 2024 survivor case under ongoing surveillance (jeon2024anovelcompound pages 1-3).

---

## 12. Treatment

### 12.1 Standard of care
No disease-modifying therapy was identified in the retrieved evidence. The 2024 case report explicitly states: “**there is no specific treatment for FBCG1**” (jeon2024anovelcompound pages 1-3).

### 12.2 Supportive care and surveillance
After genetic diagnosis, surveillance for **ophthalmic and hearing** complications is emphasized (jeon2024anovelcompound pages 1-3).

### 12.3 Growth hormone (limited evidence)
Jeon et al. cite a small prior report that “treatment of three cases with COL11A1 mutations with growth hormone was effective,” increasing growth velocity to **9.1 cm/year** and improving height by **+1.5 SDS** in the first year (jeon2024anovelcompound pages 1-3). This is anecdotal/case-based and not supported by trial evidence in the retrieved material.

### 12.4 Clinical trials
A clinical-trial search did not retrieve fibrochondrogenesis-specific interventional trials in the current tool run (no relevant NCT evidence in context).

**MAXO suggestions (supportive, not evidence-validated here):** genetic counseling; prenatal diagnostic imaging; molecular genetic testing; audiologic evaluation; ophthalmologic surveillance (supported conceptually by sources but not encoded as MAXO IDs in retrieved texts).

---

## 13. Prevention
Because fibrochondrogenesis is genetic, prevention is primarily via **reproductive/genetic counseling**:
- **Carrier testing** and family studies after molecular diagnosis (jeon2024anovelcompound pages 1-3)
- **Prenatal diagnosis** using imaging plus molecular testing where appropriate (nishimura2023prenataldiagnosisof pages 1-2)
- Counseling must consider **autosomal recessive recurrence risk** for COL11A1-related disease and also the possibility of **parental germline mosaicism** in dominant COL11A2-related cases (tompson2012dominantandrecessive pages 4-6).

---

## 14. Other Species / Natural Disease
No naturally occurring fibrochondrogenesis in non-human species was identified in the retrieved evidence.

---

## 15. Model Organisms
Evidence supports multiple models relevant to type XI collagenopathy mechanisms:
- **Zebrafish col11a2 mutants**: cartilage matrix defects, type II collagen premature degradation, altered stiffness, and joint pathology (lawrence2018themechanicalimpact pages 1-2).
- **Zebrafish col11a1a knockdown/LOF**: disrupted Meckel’s cartilage organization and mineralization (reeck2022theshapeof pages 9-11).
- **Mouse Col11a1 deficiency (cho/Col11a1−/−)**: defects in chondrogenesis and vertebral body formation and altered bone microarchitecture (hafez2015col11a1regulatesbone pages 1-3).

---

## Real-world implementation snapshot (applications)
- **Prenatal care:** screening ultrasound identifies limb shortening; expert fetal imaging (US/MRI/CT) and multidisciplinary interpretation guide prognosis and decisions; imaging-genetics correlation is critical because variant pathogenicity is not guaranteed by sequence alone (nishimura2023prenataldiagnosisof pages 1-2).
- **Clinical genetics:** WES and segregation analysis are used in contemporary practice to resolve diagnoses in atypical/surviving cases and to reclassify novel variants (jeon2024anovelcompound pages 1-3).

---

## Key visual evidence
Radiographs from Tompson et al. (2010) show the classic fetal radiographic appearance (short long bones with broad metaphyses; rib and vertebral abnormalities) (tompson2010fibrochondrogenesisresultsfrom media 1bd9e7f7).

---

## Evidence gaps / limitations (important for knowledge-base curation)
- No Orphanet/ICD/MeSH/MONDO identifiers were available in the retrieved full-text excerpts; these should be added by direct lookup in the respective databases.
- No robust survival statistics, standardized diagnostic criteria statements (ICD/consensus criteria), or QoL instrument outcomes were found in the retrieved excerpts.
- Environmental risk factors, protective factors, and GxE interactions were not supported in this evidence set.

---

## URLs and publication dates (most relevant, prioritized recent)
- Jeon et al. **Apr 2024**. *Ann Pediatr Endocrinol Metab.* “A novel compound heterozygous variant of the COL11A1 gene…” https://doi.org/10.6065/apem.2346150.075 (jeon2024anovelcompound pages 1-3)
- Nishimura et al. **Jul 2023**. *Br J Radiol.* “Prenatal diagnosis of bone dysplasias.” https://doi.org/10.1259/bjr.20221025 (nishimura2023prenataldiagnosisof pages 1-2)
- Rebello et al. **Jul 2023**. *Hum Mol Genet.* “COL11A2 as a candidate gene for vertebral malformations…” https://doi.org/10.1093/hmg/ddad117 (rebello2023col11a2asa pages 1-2)
- Handa et al. **Jan 2021**. *RadioGraphics.* “Radiologic features of type II and type XI collagenopathies.” https://doi.org/10.1148/rg.2021200075 (handa2021radiologicfeaturesof pages 11-14)
- Tompson et al. **Feb 2012**. *Am J Med Genet A.* “Dominant and recessive forms of fibrochondrogenesis…” https://doi.org/10.1002/ajmg.a.34406 (tompson2012dominantandrecessive pages 1-3)
- Tompson et al. **Nov 2010**. *Am J Hum Genet.* “Fibrochondrogenesis results from mutations in the COL11A1 type XI collagen gene.” https://doi.org/10.1016/j.ajhg.2010.10.009 (tompson2010fibrochondrogenesisresultsfrom pages 1-2)
- Lawrence et al. **Sep 2018**. *Phil Trans R Soc B.* “The mechanical impact of col11a2 loss on joints…” https://doi.org/10.1098/rstb.2017.0335 (lawrence2018themechanicalimpact pages 1-2)

---

### Appendix: quick-reference tables
(Embedded above)
- Disease identifiers/nomenclature: artifact-00
- Causal genes and representative variants: artifact-01
- Phenotype → HPO/UBERON mapping: artifact-02
- Diagnostics & management: artifact-03
- Mechanisms with GO/CL suggestions: artifact-04


References

1. (tompson2010fibrochondrogenesisresultsfrom pages 1-2): Stuart W. Tompson, Carlos A. Bacino, Nicole P. Safina, Michael B. Bober, Virginia K. Proud, Tara Funari, Michael F. Wangler, Lisette Nevarez, Leena Ala-Kokko, William R. Wilcox, David R. Eyre, Deborah Krakow, and Daniel H. Cohn. Fibrochondrogenesis results from mutations in the col11a1 type xi collagen gene. American journal of human genetics, 87 5:708-12, Nov 2010. URL: https://doi.org/10.1016/j.ajhg.2010.10.009, doi:10.1016/j.ajhg.2010.10.009. This article has 96 citations and is from a highest quality peer-reviewed journal.

2. (tompson2012dominantandrecessive pages 1-3): Stuart W. Tompson, Eissa Ali Faqeih, Leena Ala‐Kokko, Jacqueline T. Hecht, Rika Miki, Tara Funari, Vincent A. Funari, Lisette Nevarez, Deborah Krakow, and Daniel H. Cohn. Dominant and recessive forms of fibrochondrogenesis resulting from mutations at a second locus, col11a2. American Journal of Medical Genetics Part A, 158A:309-314, Feb 2012. URL: https://doi.org/10.1002/ajmg.a.34406, doi:10.1002/ajmg.a.34406. This article has 23 citations.

3. (tompson2010fibrochondrogenesisresultsfrom pages 5-5): Stuart W. Tompson, Carlos A. Bacino, Nicole P. Safina, Michael B. Bober, Virginia K. Proud, Tara Funari, Michael F. Wangler, Lisette Nevarez, Leena Ala-Kokko, William R. Wilcox, David R. Eyre, Deborah Krakow, and Daniel H. Cohn. Fibrochondrogenesis results from mutations in the col11a1 type xi collagen gene. American journal of human genetics, 87 5:708-12, Nov 2010. URL: https://doi.org/10.1016/j.ajhg.2010.10.009, doi:10.1016/j.ajhg.2010.10.009. This article has 96 citations and is from a highest quality peer-reviewed journal.

4. (jeon2024anovelcompound pages 1-3): Jaesung Jeon, Minji Kim, Sukdong Yoo, Yoomi Kim, and Chong Kun Cheon. A novel compound heterozygous variant of the col11a1 gene in a patient with fibrochondrogenesis type i: the first case in korea. Annals of Pediatric Endocrinology &amp; Metabolism, 29:135-137, Apr 2024. URL: https://doi.org/10.6065/apem.2346150.075, doi:10.6065/apem.2346150.075. This article has 0 citations.

5. (handa2021radiologicfeaturesof pages 11-14): Atsuhiko Handa, Giedre Grigelioniene, and Gen Nishimura. Radiologic features of type ii and type xi collagenopathies. RadioGraphics, 41:192-209, Jan 2021. URL: https://doi.org/10.1148/rg.2021200075, doi:10.1148/rg.2021200075. This article has 20 citations and is from a domain leading peer-reviewed journal.

6. (lawrence2018themechanicalimpact pages 1-2): Elizabeth A. Lawrence, Erika Kague, Jessye A. Aggleton, Robert L. Harniman, Karen A. Roddy, and Chrissy L. Hammond. The mechanical impact of <i>col11a2</i> loss on joints; <i>col11a2</i> mutant zebrafish show changes to joint development and function, which leads to early-onset osteoarthritis. Philosophical Transactions of the Royal Society B: Biological Sciences, 373:20170335, Sep 2018. URL: https://doi.org/10.1098/rstb.2017.0335, doi:10.1098/rstb.2017.0335. This article has 73 citations and is from a domain leading peer-reviewed journal.

7. (reeck2022theshapeof pages 9-11): Jonathon C. Reeck and Julia Thom Oxford. The shape of the jaw—zebrafish col11a1a regulates meckel’s cartilage morphogenesis and mineralization. Journal of Developmental Biology, 10:40, Sep 2022. URL: https://doi.org/10.3390/jdb10040040, doi:10.3390/jdb10040040. This article has 12 citations.

8. (hafez2015col11a1regulatesbone pages 1-3): Anthony Hafez, Ryan Squires, Amber Pedracini, Alark Joshi, Robert Seegmiller, and Julia Oxford. Col11a1 regulates bone microarchitecture during embryonic development. Journal of developmental biology, 3:158-176, Dec 2015. URL: https://doi.org/10.3390/jdb3040158, doi:10.3390/jdb3040158. This article has 49 citations.

9. (tompson2012dominantandrecessive pages 4-6): Stuart W. Tompson, Eissa Ali Faqeih, Leena Ala‐Kokko, Jacqueline T. Hecht, Rika Miki, Tara Funari, Vincent A. Funari, Lisette Nevarez, Deborah Krakow, and Daniel H. Cohn. Dominant and recessive forms of fibrochondrogenesis resulting from mutations at a second locus, col11a2. American Journal of Medical Genetics Part A, 158A:309-314, Feb 2012. URL: https://doi.org/10.1002/ajmg.a.34406, doi:10.1002/ajmg.a.34406. This article has 23 citations.

10. (tompson2012dominantandrecessive pages 12-13): Stuart W. Tompson, Eissa Ali Faqeih, Leena Ala‐Kokko, Jacqueline T. Hecht, Rika Miki, Tara Funari, Vincent A. Funari, Lisette Nevarez, Deborah Krakow, and Daniel H. Cohn. Dominant and recessive forms of fibrochondrogenesis resulting from mutations at a second locus, col11a2. American Journal of Medical Genetics Part A, 158A:309-314, Feb 2012. URL: https://doi.org/10.1002/ajmg.a.34406, doi:10.1002/ajmg.a.34406. This article has 23 citations.

11. (tompson2012dominantandrecessive pages 7-12): Stuart W. Tompson, Eissa Ali Faqeih, Leena Ala‐Kokko, Jacqueline T. Hecht, Rika Miki, Tara Funari, Vincent A. Funari, Lisette Nevarez, Deborah Krakow, and Daniel H. Cohn. Dominant and recessive forms of fibrochondrogenesis resulting from mutations at a second locus, col11a2. American Journal of Medical Genetics Part A, 158A:309-314, Feb 2012. URL: https://doi.org/10.1002/ajmg.a.34406, doi:10.1002/ajmg.a.34406. This article has 23 citations.

12. (handa2021radiologicfeaturesof pages 16-17): Atsuhiko Handa, Giedre Grigelioniene, and Gen Nishimura. Radiologic features of type ii and type xi collagenopathies. RadioGraphics, 41:192-209, Jan 2021. URL: https://doi.org/10.1148/rg.2021200075, doi:10.1148/rg.2021200075. This article has 20 citations and is from a domain leading peer-reviewed journal.

13. (rebello2023col11a2asa pages 1-2): Denise Rebello, Elizabeth Wohler, Vida Erfani, Guozhuang Li, Alexya N Aguilera, Alberto Santiago-Cornier, Sen Zhao, Steven W Hwang, Robert D Steiner, Terry Jianguo Zhang, Christina A Gurnett, Cathleen Raggio, Nan Wu, Nara Sobreira, Philip F Giampietro, and Brian Ciruna. Col11a2 as a candidate gene for vertebral malformations and congenital scoliosis. Human molecular genetics, 32:2913-2928, Jul 2023. URL: https://doi.org/10.1093/hmg/ddad117, doi:10.1093/hmg/ddad117. This article has 19 citations and is from a domain leading peer-reviewed journal.

14. (reeck2022theshapeof pages 11-13): Jonathon C. Reeck and Julia Thom Oxford. The shape of the jaw—zebrafish col11a1a regulates meckel’s cartilage morphogenesis and mineralization. Journal of Developmental Biology, 10:40, Sep 2022. URL: https://doi.org/10.3390/jdb10040040, doi:10.3390/jdb10040040. This article has 12 citations.

15. (hall2024fetalandperinatal pages 61-63): Christine M Hall, Amaka C Offiah, Francesca Forzano, Mario Lituania, Gen Nishimura, and Valerie Cormier-Daire. Fetal and perinatal skeletal dysplasias. ArXiv, Mar 2024. URL: https://doi.org/10.1201/9781003166948, doi:10.1201/9781003166948. This article has 26 citations.

16. (lawrence2018themechanicalimpact pages 12-12): Elizabeth A. Lawrence, Erika Kague, Jessye A. Aggleton, Robert L. Harniman, Karen A. Roddy, and Chrissy L. Hammond. The mechanical impact of <i>col11a2</i> loss on joints; <i>col11a2</i> mutant zebrafish show changes to joint development and function, which leads to early-onset osteoarthritis. Philosophical Transactions of the Royal Society B: Biological Sciences, 373:20170335, Sep 2018. URL: https://doi.org/10.1098/rstb.2017.0335, doi:10.1098/rstb.2017.0335. This article has 73 citations and is from a domain leading peer-reviewed journal.

17. (reeck2017theroleof pages 40-45): Jonathon Charles Reeck. The role of col11a1 expression during cartilage development. ArXiv, 2017. URL: https://doi.org/10.18122/b2dq43, doi:10.18122/b2dq43. This article has 1 citations.

18. (nishimura2023prenataldiagnosisof pages 1-2): Gen Nishimura, Atsuhiko Handa, Osamu Miyazaki, Yuko Tsujioka, Jun Murotsuki, Hideaki Sawai, Takahiro Yamada, Yutaka Kozuma, Yuichiro Takahashi, Katsunori Ozawa, Ritusuko Pooh, and Masakatsu Sase. Prenatal diagnosis of bone dysplasias. The British journal of radiology, 96 1147:20221025, Jul 2023. URL: https://doi.org/10.1259/bjr.20221025, doi:10.1259/bjr.20221025. This article has 20 citations.

19. (tompson2010fibrochondrogenesisresultsfrom media 1bd9e7f7): Stuart W. Tompson, Carlos A. Bacino, Nicole P. Safina, Michael B. Bober, Virginia K. Proud, Tara Funari, Michael F. Wangler, Lisette Nevarez, Leena Ala-Kokko, William R. Wilcox, David R. Eyre, Deborah Krakow, and Daniel H. Cohn. Fibrochondrogenesis results from mutations in the col11a1 type xi collagen gene. American journal of human genetics, 87 5:708-12, Nov 2010. URL: https://doi.org/10.1016/j.ajhg.2010.10.009, doi:10.1016/j.ajhg.2010.10.009. This article has 96 citations and is from a highest quality peer-reviewed journal.
