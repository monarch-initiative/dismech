---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T18:55:37.358054'
end_time: '2026-05-08T19:03:33.178844'
duration_seconds: 475.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hand-Foot-Genital Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hand-Foot-Genital Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hand-Foot-Genital Syndrome** covering all of the
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
- **Disease Name:** Hand-Foot-Genital Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hand-Foot-Genital Syndrome** covering all of the
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


# Hand-Foot-Genital Syndrome (HFGS) — Comprehensive Disease Characteristics Report

## Executive summary
Hand-Foot-Genital Syndrome (HFGS) is a rare, autosomal dominant developmental malformation syndrome caused by pathogenic variation in **HOXA13**, a homeobox transcription factor essential for distal limb and urogenital tract development (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6). The core phenotype is **highly penetrant distal limb malformations** (notably first-digit hypoplasia) with **variably penetrant genitourinary anomalies** (hypospadias in males; Müllerian fusion anomalies and/or urinary tract abnormalities in females) (goodman2000novelhoxa13mutations pages 1-2, utsch2002anovelstable pages 1-2). Recent (2023–2024) genomics literature emphasizes that **structural variants (SVs) such as inversions** can be under-ascertained by standard tests and may contribute to unresolved Mendelian phenotypes, supporting broader use of genome sequencing and SV-aware interpretation (pagnamenta2024theimpactof pages 1-2).

---

## 1. Disease information

### 1.1 Definition / overview (current understanding)
HFGS is “a rare, dominantly inherited condition characterized by distal limb and distal genitourinary tract malformations” (Goodman et al., 2000; published online 2000-06-05; https://doi.org/10.1086/302961) (goodman2000novelhoxa13mutations pages 1-2). Classic limb findings are typically bilateral and symmetric and include first-digit hypoplasia (thumb and hallux) with carpal/tarsal anomalies, while genitourinary findings show incomplete penetrance and variable severity (goodman2000novelhoxa13mutations pages 1-2, utsch2002anovelstable pages 1-2).

**Abstract quote (primary literature):** “Hand-foot-genital syndrome (HFGS) is a rare, dominantly inherited condition affecting the distal limbs and genitourinary tract.” (Goodman et al., 2000) (goodman2000novelhoxa13mutations pages 1-2).

### 1.2 Key identifiers
- **OMIM:** **140000** (HFGS) (goodman2000novelhoxa13mutations pages 1-2, jaouadi2023geneticandphenotypic pages 1-2).
- **Gene:** **HOXA13** (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6).
- **Other identifiers (MONDO, Orphanet, ICD-10/ICD-11, MeSH):** Not directly retrievable from the currently ingested sources; requires external database lookup (gap).

### 1.3 Synonyms / alternative names
- “Hand-foot-genital syndrome”
- “HFGS” (common abbreviation)
- Older abbreviations in some literature include “HFG/HFU” context (as cited in a 2002 Human Genetics paper) (utsch2002anovelstable pages 1-2).

### 1.4 Evidence source types
The current evidence base is predominantly:
- **Aggregated disease-level descriptions** (review-style synthesis and multi-family genetic reports) (goodman2002limbmalformationsand pages 5-6, utsch2002anovelstable pages 1-2).
- **Individual/family-based primary reports** (case reports/series and family studies with segregation) (goodman2000novelhoxa13mutations pages 1-2, owens2013analysisofde pages 2-3).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline pathogenic variants affecting **HOXA13** function (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6).

**Variant classes reported across the core literature include:**
- **Nonsense/truncating variants** (predicted loss of function) (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6).
- **Missense variants** (often in the DNA-binding homeodomain; can associate with unusually severe limb phenotypes) (goodman2000novelhoxa13mutations pages 1-2, imagawa2014severemanifestationsof pages 4-5).
- **In-frame polyalanine tract expansions** in the N-terminus (goodman2000novelhoxa13mutations pages 1-2, innis2004polyalanineexpansionin pages 1-2).
- **Duplications** affecting HOXA13 (reported in atypical HFGS) (frisen2003anovelduplication pages 1-1, frisen2003anovelduplication pages 5-5).
- **Larger structural changes** including deletions affecting the HOXA cluster (discussed as part of mutational spectrum) (utsch2002anovelstable pages 1-2, frisen2003anovelduplication pages 1-1).

### 2.2 Risk factors
- **Genetic:** having a pathogenic **HOXA13** variant (autosomal dominant inheritance) is the principal risk factor (goodman2000novelhoxa13mutations pages 1-2, utsch2002anovelstable pages 1-2).
- **De novo variation:** de novo polyalanine expansions and point mutations have been documented (owens2013analysisofde pages 2-3, goodman2000novelhoxa13mutations pages 1-2).

**Recent development (genomics diagnostics):** structural variants such as inversions can underlie rare disease and may be missed by copy-number-focused pipelines, supporting the use of genome sequencing for unsolved cases (Pagnamenta et al., 2024-06-06, AJHG; https://doi.org/10.1016/j.ajhg.2024.04.018) (pagnamenta2024theimpactof pages 1-2).

### 2.3 Protective factors
No evidence for genetic/environmental protective factors specific to HFGS was identified in the ingested sources (gap).

### 2.4 Gene–environment interactions
No direct gene–environment interaction evidence specific to HFGS was identified in the ingested sources (gap).

---

## 3. Phenotypes

### 3.1 Phenotype spectrum and characteristics

#### Distal limb phenotype (high penetrance)
Commonly described findings include:
- **First-digit hypoplasia**: short, proximally placed thumbs and short, medially deviated halluces; hypoplastic thenar eminences (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6, utsch2002anovelstable pages 1-2).
- **Carpal/tarsal ossification anomalies**: delayed ossification, fusion, shortening of carpals and tarsals (goodman2000novelhoxa13mutations pages 1-2, utsch2002anovelstable pages 1-2).
- Additional digital findings: ulnar deviation of second fingers, clinodactyly/brachydactyly (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6, utsch2002anovelstable pages 1-2).

Penetrance statement: limb abnormalities are described as **fully penetrant / highly penetrant** in reported series (utsch2002anovelstable pages 1-2, frisen2003anovelduplication pages 1-1).

**Suggested HPO terms (examples):**
- First digit hypoplasia: **HP:0005864** (Thumb hypoplasia; approximate mapping)
- Hypoplastic thenar eminence: **HP:0030438** (Thenar hypoplasia; approximate)
- Hallux deviation/varus/valgus: **HP:0001847** (Hallux varus) / **HP:0001838** (Hallux valgus; approximate)
- Carpal/tarsal coalition/fusion: **HP:0009702** (Carpal fusion) / **HP:0008367** (Tarsal coalition; approximate)

(Exact HPO IDs should be verified during curation; the phenotype concepts are strongly supported by primary descriptions.) (goodman2000novelhoxa13mutations pages 1-2, utsch2002anovelstable pages 1-2).

#### Genitourinary phenotype (variable expressivity / incomplete penetrance)
- **Males:** hypospadias and other penile anomalies (goodman2000novelhoxa13mutations pages 1-2, utsch2002anovelstable pages 1-2).
- **Females:** Müllerian duct fusion anomalies ranging from longitudinal vaginal septum to double uterus with double cervix; bicornuate uterus described in recent cases (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6, jaouadi2023geneticandphenotypic pages 1-2).
- **Urinary tract anomalies:** ectopic ureteric orifices, vesicoureteric reflux, pelvi-ureteric junction obstruction, recurrent UTIs; renal complications can occur (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6, owens2013analysisofde pages 2-3).

**Statistics (reported in a major review):**
- Müllerian duct fusion defects in females are described as occurring in **~50% of affected females** (Goodman 2002) (goodman2002limbmalformationsand pages 5-6).
- Urinary tract anomalies were described as occurring in **<20%** in that summary (with potential for chronic pyelonephritis and renal insufficiency) (goodman2002limbmalformationsand pages 5-6).

**Suggested HPO terms (examples):**
- Hypospadias: **HP:0000047**
- Uterine didelphys / double uterus: **HP:0000135** (Uterus didelphys; approximate)
- Longitudinal vaginal septum: **HP:0100644** (Vaginal septum; approximate)
- Vesicoureteral reflux: **HP:0000076**
- Recurrent urinary tract infections: **HP:0000010**

### 3.2 Age of onset, progression, and natural history
HFGS is a **congenital** malformation syndrome with abnormalities typically evident at birth or early in life (limb phenotype), while genitourinary manifestations may be discovered during childhood/adolescence/adulthood (e.g., evaluation for UTIs, imaging of Müllerian anomalies, fertility workup) (goodman2000novelhoxa13mutations pages 1-2, owens2013analysisofde pages 2-3, jaouadi2023geneticandphenotypic pages 1-2).

### 3.3 Quality-of-life impact
Primary evidence indicates potential impact via:
- Functional and orthopedic consequences of limb malformations (hand/foot anatomy) (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6).
- Urologic morbidity (recurrent UTIs, urinary leakage, renal impairment risk) and reproductive outcomes (fetal loss/neonatal death reported in at least three families in early literature) (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6, owens2013analysisofde pages 2-3).

---

## 4. Genetic / molecular information

### 4.1 Causal gene
- **HOXA13** (homeobox transcription factor) is the established causal gene (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6).

### 4.2 Pathogenic variant spectrum (types and interpreted effects)
Evidence supports at least two broad mechanistic categories:
1) **Loss-of-function / haploinsufficiency-like outcomes** (notably truncating variants; and some polyalanine expansions with reduced protein abundance) (innis2004polyalanineexpansionin pages 1-2, goodman2000novelhoxa13mutations pages 1-2).
2) **Dominant-negative and/or gain-of-function possibilities** for certain missense variants and some polyalanine expansions, discussed as explaining unusually severe phenotypes compared with null alleles (utsch2002anovelstable pages 6-7, imagawa2014severemanifestationsof pages 4-5, frisen2003anovelduplication pages 5-5).

Key variant categories documented in the ingested primary literature:
- **Truncating/nonsense variants** leading to truncated proteins (Goodman 2000) (goodman2000novelhoxa13mutations pages 1-2).
- **Polyalanine expansions** in HOXA13 (Innis 2004; Utsch 2002) (innis2004polyalanineexpansionin pages 1-2, utsch2002anovelstable pages 1-2).
  - **Abstract quote (Innis 2004):** “Polyalanine expansions … can cause HFGS.” and “Mutant limb buds had … reduced levels of steady-state protein… loss of function is secondary to a reduction in the in vivo abundance of the expanded protein likely due to degradation.” (Innis et al., 2004-11; https://doi.org/10.1093/hmg/ddh306) (innis2004polyalanineexpansionin pages 1-2).
- **Duplications** (including “novel HOXA13 duplication” associated with atypical HFGS) (frisen2003anovelduplication pages 1-1, frisen2003anovelduplication pages 5-5).
- **De novo polyalanine expansions** with molecular evidence consistent with replication slippage (Owens 2013) (owens2013analysisofde pages 2-3).

### 4.3 Inheritance, penetrance, expressivity
- **Inheritance:** autosomal dominant (goodman2000novelhoxa13mutations pages 1-2, utsch2002anovelstable pages 1-2).
- **Penetrance:** limb findings are described as fully/highly penetrant; genitourinary anomalies are incompletely/partially penetrant with variable expressivity (utsch2002anovelstable pages 1-2, frisen2003anovelduplication pages 1-1, jaouadi2023geneticandphenotypic pages 1-2).

### 4.4 Modifier genes / dual diagnoses
The phenotype can be complicated by additional variants in other genes in some individuals, consistent with “phenotypic blending” / multiple diagnoses in modern genomics (concept supported by rare disease genome sequencing studies and reported dual diagnoses including HOXA13 plus another gene in case literature) (wallis2016dualgeneticdiagnoses pages 6-7, pagnamenta2024theimpactof pages 1-2).

### 4.5 Epigenetic information
No disease-specific epigenetic mechanisms for HFGS were identified in the ingested sources (gap).

### 4.6 Chromosomal abnormalities
The mutational spectrum discussed in the HFGS literature includes HOXA cluster deletions and other SV mechanisms (utsch2002anovelstable pages 1-2, frisen2003anovelduplication pages 1-1). Separately, recent large-cohort genome sequencing indicates inversions are an under-recognized disease mechanism in general and can act via gene disruption or altered regulatory landscapes (pagnamenta2024theimpactof pages 1-2).

---

## 5. Environmental information
No established non-genetic environmental or infectious contributors were identified for HFGS in the ingested sources; HFGS is treated as a Mendelian developmental disorder (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6).

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (from gene defect to phenotype)
1) **Upstream trigger:** germline pathogenic variant affecting HOXA13 (goodman2000novelhoxa13mutations pages 1-2).
2) **Molecular consequence:** altered transcription factor function (via reduced protein abundance/degradation for some polyalanine expansions; altered DNA-binding for homeodomain missense; truncation removing key domains) (innis2004polyalanineexpansionin pages 1-2, imagawa2014severemanifestationsof pages 4-5, goodman2002limbmalformationsand pages 5-6).
3) **Developmental pathway disruption:** impaired patterning and morphogenesis of distal limbs and urogenital tract derivatives (goodman2002limbmalformationsand pages 5-6, utsch2002anovelstable pages 1-2).
4) **Organ-level manifestations:** first-digit hypoplasia/carpal-tarsal defects and hypospadias/Müllerian anomalies/urinary anomalies (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6).

### 6.2 Pathways, processes, and targets (evidence-based highlights)
- Polyalanine expansion mechanism: evidence indicates decreased steady-state HOXA13 protein with expanded tract, with inferred degradation leading to functional loss (mouse model and molecular assays) (innis2004polyalanineexpansionin pages 1-2).
- Homeodomain missense and developmental processes: HOXA13 is reported to bind targets such as **Bmp2** and **Bmp7** and to regulate “interdigital programmed cell death, digit mesenchymal condensation, and digit chondrogenesis” (Imagawa 2014) (imagawa2014severemanifestationsof pages 4-5).
- De novo expansion mechanism: evidence supports replication slippage/unequal sister chromatid exchange as plausible mechanisms rather than unequal crossing-over in at least one de novo expansion analysis (owens2013analysisofde pages 2-3).

### 6.3 Ontology suggestions
**GO biological process (examples to curate/validate):**
- Pattern specification process (GO:0007389)
- Limb development / appendage development (e.g., GO:0060173 / GO:0048736)
- Urogenital system development (GO:0001655)
- Regulation of programmed cell death (for interdigital apoptosis; GO:0043067)

**Cell types (CL) likely involved (developmental):**
- Limb bud mesenchymal cell (CL term requires curator selection)
- Urogenital sinus / genital tubercle mesenchyme (developmental CL terms require curator selection)

These ontology mappings are consistent with the mechanistic descriptions but require formal term validation during curation (imagawa2014severemanifestationsof pages 4-5, innis2004polyalanineexpansionin pages 1-2).

---

## 7. Anatomical structures affected

### 7.1 Organ and system level
- **Skeletal system (distal appendicular skeleton):** thumbs, halluces, carpals, tarsals (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6).
- **Urogenital system:** distal genitourinary tract; in males (penis/urethra), in females (Müllerian-derived uterus/cervix/vagina), and urinary tract (ureters/bladder) (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6, owens2013analysisofde pages 2-3).

**Suggested UBERON terms (examples):**
- UBERON:0002398 (hand), UBERON:0002108 (foot)
- UBERON:0000945 (uterus), UBERON:0000996 (vagina)
- UBERON:0001255 (urinary bladder), UBERON:0000056 (ureter)

### 7.2 Subcellular level
HOXA13 is a transcription factor (nuclear localization implied), and polyalanine expansions can alter protein abundance; specific organelle-level pathology beyond this is not described in the ingested sources (innis2004polyalanineexpansionin pages 1-2).

---

## 8. Temporal development
- **Onset:** congenital, with limb anomalies typically apparent early; genitourinary anomalies may be detected later depending on severity and clinical pathway (goodman2000novelhoxa13mutations pages 1-2, owens2013analysisofde pages 2-3).
- **Course:** generally lifelong anatomical differences; complications relate mainly to urologic sequelae (UTIs/reflux/renal impairment) and reproductive outcomes (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6).

---

## 9. Inheritance and population

### 9.1 Epidemiology (available statistics)
Robust population prevalence/incidence estimates were not found in the ingested sources (gap).

A frequently cited early aggregation reported: “nine families and three sporadic cases” totaling “52 affected individuals (34 males, 18 females)” (Utsch et al., 2002-04; https://doi.org/10.1007/s00439-002-0712-8) (utsch2002anovelstable pages 1-2). This is not a prevalence estimate but provides early ascertainment scale.

### 9.2 Inheritance pattern
- **Autosomal dominant** inheritance is consistently reported (goodman2000novelhoxa13mutations pages 1-2, utsch2002anovelstable pages 1-2, jaouadi2023geneticandphenotypic pages 1-2).
- **Variable expressivity** and **incomplete penetrance for genitourinary anomalies** are repeatedly emphasized (goodman2000novelhoxa13mutations pages 1-2, frisen2003anovelduplication pages 1-1, jaouadi2023geneticandphenotypic pages 1-2).

Founder effects, consanguinity, carrier frequency: not identified in ingested sources (gap).

---

## 10. Diagnostics

### 10.1 Clinical recognition
Suspicion is based on the combination of:
- Typical bilateral distal limb pattern (thumb/hallux hypoplasia, carpal/tarsal anomalies) (goodman2000novelhoxa13mutations pages 1-2, utsch2002anovelstable pages 1-2).
- Genitourinary anomalies (hypospadias; Müllerian fusion anomalies; urinary anomalies) with variable penetrance (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6).

### 10.2 Imaging and clinical tests
- **Urogenital imaging** (e.g., evaluation for vesicoureteric reflux; pelvic imaging for uterine anomalies) is supported by reported clinical follow-up and case descriptions (goodman2000novelhoxa13mutations pages 1-2, jaouadi2023geneticandphenotypic pages 1-2).

### 10.3 Genetic testing (current practice implications)
Evidence across time supports a tiered approach:
- **Targeted HOXA13 sequencing (PCR/Sanger validation)** has been used in classic families (goodman2000novelhoxa13mutations pages 1-2, imagawa2014severemanifestationsof pages 4-5, owens2013analysisofde pages 2-3).
- **WES** can identify novel HOXA13 missense variants in syndromic presentations (Jaouadi 2023; received 2022-10-04; accepted 2022-11-30; https://doi.org/10.3892/mmr.2023.12946) (jaouadi2023geneticandphenotypic pages 1-2).
- **Genome sequencing with SV-aware analysis** is increasingly important because inversion and other complex SV classes can be missed by copy-number-focused pipelines; large rare disease cohort work shows inversions are a “small but notable” contributor and can resolve prolonged diagnostic odysseys (Pagnamenta 2024) (pagnamenta2024theimpactof pages 1-2).

### 10.4 Differential diagnosis (examples mentioned in primary literature)
In severe limb phenotypes due to HOXA13 missense, differential diagnoses discussed include **brachydactyly type B1** and **Cook syndrome** (imagawa2014severemanifestationsof pages 4-5).

### 10.5 Screening
No newborn screening or population screening programs were identified for HFGS in the ingested sources; however, family-based cascade testing is implied by autosomal dominant inheritance and de novo possibility (goodman2000novelhoxa13mutations pages 1-2, owens2013analysisofde pages 2-3).

---

## 11. Outcome / prognosis
HFGS is not presented as a life-shortening disorder per se in the ingested sources; morbidity primarily reflects urogenital complications (reflux, UTIs, renal insufficiency) and reproductive outcomes in affected females (goodman2002limbmalformationsand pages 5-6, goodman2000novelhoxa13mutations pages 1-2). Severe urologic dysfunction can require major reconstructive interventions in some cases (owens2013analysisofde pages 2-3).

---

## 12. Treatment

### 12.1 Current applications and real-world implementations (management)
Management is individualized and typically includes:
- **Urologic evaluation and treatment** of reflux/obstruction/UTIs; in severe cases, reconstructive procedures.
  - Example of high-intensity management reported: bladder augmentation and creation of a Mitrofanoff channel for urinary leakage and small bladder, in a patient with HOXA13 polyalanine expansion (Owens 2013) (owens2013analysisofde pages 2-3).
- **Surgical repair** of hypospadias when indicated (not quantified in ingested sources, but repeatedly listed as a key manifestation) (goodman2000novelhoxa13mutations pages 1-2, innis2004polyalanineexpansionin pages 1-2).
- **Orthopedic/hand-foot care** as needed for function and footwear (not detailed quantitatively in ingested sources) (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6).

### 12.2 Pharmacotherapy
No disease-specific pharmacologic therapy targeting HOXA13 mechanisms was identified (gap).

### 12.3 Experimental / clinical trials
ClinicalTrials.gov searches retrieved observational studies related to hypospadias and other conditions, but **no HFGS-specific interventional clinical trials** were identified in the retrieved trial set (gap; based on current tool results).

### 12.4 MAXO term suggestions (examples)
- **Genetic counseling** (MAXO term to curate)
- **Surgical repair of hypospadias** (MAXO)
- **Urologic reconstructive surgery** (e.g., urinary diversion, bladder augmentation) (MAXO)
- **Renal/urinary tract surveillance** (MAXO)

---

## 13. Prevention
Primary prevention is not applicable for inherited HFGS beyond reproductive planning.

### 13.1 Genetic counseling and reproductive options
Autosomal dominant inheritance supports:
- **Cascade testing** of at-risk relatives once a familial HOXA13 variant is known (goodman2000novelhoxa13mutations pages 1-2).
- **Prenatal diagnosis** or **preimplantation genetic testing** may be considered for known familial variants (not directly described in ingested sources, but standard for AD Mendelian disorders; should be treated as an implementation inference).

### 13.2 Secondary/tertiary prevention
- Early identification and management of **vesicoureteric reflux/UTIs** to reduce risk of chronic pyelonephritis and renal impairment (goodman2002limbmalformationsand pages 5-6).

---

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in the ingested sources (gap).

---

## 15. Model organisms
Mouse models provide functional evidence linking HOXA13 disruptions to the phenotype:
- A mouse HOXA13 polyalanine expansion model showed phenotypes indistinguishable from null mice and demonstrated that loss of function can arise from reduced in vivo abundance of the expanded protein (Innis 2004) (innis2004polyalanineexpansionin pages 1-2).
- Review-level summaries note that homozygous loss of Hoxa13 is lethal and produces severe urinary/genital tract malformations, supporting developmental essentiality (Goodman 2002) (goodman2002limbmalformationsand pages 5-6).

---

## 2023–2024 “latest research” highlights (prioritized)
1) **Expanded syndromic context and penetrance framing (2023):** A 2023 case-based paper reiterates HFGS (OMIM 140000) as a HOXA13-related autosomal dominant disorder with fully penetrant limb defects and partially penetrant genitourinary anomalies, and emphasizes variable fertility implications (Jaouadi 2023; https://doi.org/10.3892/mmr.2023.12946) (jaouadi2023geneticandphenotypic pages 1-2).
2) **Structural variants and diagnostic implementation (2024):** A large rare disease genome sequencing analysis highlights how inversions and complex SVs contribute to Mendelian diagnoses and can be missed by routine approaches, supporting broader implementation of WGS/SV detection for unresolved phenotypes (Pagnamenta 2024-06-06; https://doi.org/10.1016/j.ajhg.2024.04.018) (pagnamenta2024theimpactof pages 1-2).

---

## Structured identifiers/nomenclature artifact
| Disease name | Synonyms / alternative names | OMIM number | Causal gene | Inheritance | Key phenotypic hallmarks: hands/feet | Key phenotypic hallmarks: genitourinary | Key references (year; DOI / URL) |
|---|---|---|---|---|---|---|---|
| Hand-Foot-Genital Syndrome | HFGS; hand-foot-genital syndrome; hand–foot–genital syndrome | OMIM 140000 | **HOXA13** | Autosomal dominant | Distal limb malformations with first-digit hypoplasia; short, proximally placed thumbs; hypoplastic thenar eminences; short, medially deviated halluces; delayed ossification/fusion/shortening of carpals and tarsals; clinodactyly/brachydactyly may occur (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6, utsch2002anovelstable pages 1-2, jaouadi2023geneticandphenotypic pages 1-2, innis2004polyalanineexpansionin pages 1-2) | Distal genitourinary tract malformations with variable expressivity; hypospadias in males; Müllerian duct fusion defects in females (e.g., vaginal septum, double uterus with double cervix, bicornuate uterus); urinary anomalies can include vesicoureteric reflux, ectopic ureteric orifices, pelvi-ureteric/ureteropelvic junction obstruction, recurrent UTIs, and risk of renal insufficiency (goodman2000novelhoxa13mutations pages 1-2, goodman2002limbmalformationsand pages 5-6, utsch2002anovelstable pages 1-2, jaouadi2023geneticandphenotypic pages 1-2, innis2004polyalanineexpansionin pages 1-2) | Goodman 2000; doi:10.1086/302961; https://doi.org/10.1086/302961 (goodman2000novelhoxa13mutations pages 1-2) |
| Hand-Foot-Genital Syndrome | HFGS; HFG syndrome / HFU syndrome (older abbreviation in literature) | OMIM 140000; OMIM 142959 also cited in older literature context | **HOXA13** | Autosomal dominant | Limb defects are described as fully penetrant / highly penetrant in reported series; bilateral and symmetrical in typical cases (utsch2002anovelstable pages 1-2, jaouadi2023geneticandphenotypic pages 1-2) | Genitourinary anomalies are incompletely penetrant / partially penetrant and variably severe, with fertility implications in some affected females (goodman2000novelhoxa13mutations pages 1-2, utsch2002anovelstable pages 1-2, jaouadi2023geneticandphenotypic pages 1-2) | Goodman 2002; doi:10.1002/ajmg.10776; https://doi.org/10.1002/ajmg.10776 (goodman2002limbmalformationsand pages 5-6) |
| Hand-Foot-Genital Syndrome | HFGS | OMIM 140000 | **HOXA13** | Autosomal dominant | Typical phenotype can result from nonsense mutations and polyalanine tract expansions; missense variants may produce more severe limb phenotypes (goodman2000novelhoxa13mutations pages 1-2, imagawa2014severemanifestationsof pages 4-5) | Typical phenotype includes hypospadias, Müllerian anomalies, and urinary tract abnormalities; severity is variable across families (goodman2000novelhoxa13mutations pages 1-2, imagawa2014severemanifestationsof pages 4-5) | Utsch 2002; doi:10.1007/s00439-002-0712-8; https://doi.org/10.1007/s00439-002-0712-8 (utsch2002anovelstable pages 1-2, utsch2002anovelstable pages 6-7) |
| Hand-Foot-Genital Syndrome | HFGS | OMIM 140000 | **HOXA13** | Autosomal dominant | Polyalanine expansions in all three major HOXA13 polyalanine repeats can cause HFGS; common phenotype includes bilaterally symmetrical shortening of thumbs and halluces with clinobrachydactyly (innis2004polyalanineexpansionin pages 1-2) | Genitourinary anomalies may include hypospadias, ureteral reflux, and incomplete Müllerian fusion (innis2004polyalanineexpansionin pages 1-2) | Innis 2004; doi:10.1093/hmg/ddh306; https://doi.org/10.1093/hmg/ddh306 (innis2004polyalanineexpansionin pages 1-2) |
| Hand-Foot-Genital Syndrome | HFGS | OMIM 140000 | **HOXA13** | Autosomal dominant | Recent review/case literature reiterates bilateral, symmetrical distal limb anomalies centered on first-digit hypoplasia and wrist/foot ossification defects (jaouadi2023geneticandphenotypic pages 1-2) | Recent review/case literature reiterates genitourinary malformations with variable penetrance; females do not necessarily have infertility (jaouadi2023geneticandphenotypic pages 1-2) | Jaouadi 2023; doi:10.3892/mmr.2023.12946; https://doi.org/10.3892/mmr.2023.12946 (jaouadi2023geneticandphenotypic pages 1-2) |
| Hand-Foot-Genital Syndrome | HFGS | OMIM 140000 | **HOXA13** | Autosomal dominant | Structural variant studies expand the mutational spectrum affecting HOXA13-related disease; inversions can contribute to rare disease diagnosis where targeted prior testing was negative (pagnamenta2024theimpactof pages 1-2) | Structural rearrangements near/disrupting developmental genes such as **HOXA13** may alter regulatory landscape and contribute to disease phenotypes, relevant to unresolved HFGS-like presentations (pagnamenta2024theimpactof pages 1-2) | Pagnamenta 2024; doi:10.1016/j.ajhg.2024.04.018; https://doi.org/10.1016/j.ajhg.2024.04.018 (pagnamenta2024theimpactof pages 1-2) |


*Table: This table summarizes the core identifiers, naming, inheritance, causal gene, and hallmark clinical features of Hand-Foot-Genital Syndrome using only the specified evidence sources. It is useful as a compact disease knowledge base seed for nomenclature and phenotype curation.*

---

## Evidence limitations and curation gaps
- MONDO, Orphanet, ICD-10/ICD-11, and MeSH identifiers were not extractable from the currently ingested texts; this report therefore anchors coding primarily to OMIM and primary literature (gap).
- Population prevalence/incidence estimates were not found; available numeric data are from early aggregated case counts and phenotype-frequency statements in review summaries (utsch2002anovelstable pages 1-2, goodman2002limbmalformationsand pages 5-6).
- HPO/GO/CL/UBERON/MAXO term IDs listed are partially inferential and require curator verification; however, the underlying phenotype/process/anatomy concepts are strongly supported by cited sources.


References

1. (goodman2000novelhoxa13mutations pages 1-2): Frances R. Goodman, Chiara Bacchelli, Angela F. Brady, Louise A. Brueton, Jean-Pierre Fryns, Douglas P. Mortlock, Jeffrey W. Innis, Lewis B. Holmes, Alan E. Donnenfeld, Murray Feingold, Frits A. Beemer, Raoul C.M. Hennekam, and Peter J. Scambler. Novel hoxa13 mutations and the phenotypic spectrum of hand-foot-genital syndrome. The American Journal of Human Genetics, 67:197-202, Jul 2000. URL: https://doi.org/10.1086/302961, doi:10.1086/302961. This article has 288 citations.

2. (goodman2002limbmalformationsand pages 5-6): Frances R. Goodman. Limb malformations and the human hox genes. American journal of medical genetics, 112 3:256-65, Oct 2002. URL: https://doi.org/10.1002/ajmg.10776, doi:10.1002/ajmg.10776. This article has 294 citations.

3. (utsch2002anovelstable pages 1-2): Boris Utsch, Karl Becker, Detlef Brock, Michael J. Lentze, Frank Bidlingmaier, and Michael Ludwig. A novel stable polyalanine [poly(a)] expansion in the hoxa13 gene associated with hand-foot-genital syndrome: proper function of poly(a)-harbouring transcription factors depends on a critical repeat length? Human Genetics, 110:488-494, Apr 2002. URL: https://doi.org/10.1007/s00439-002-0712-8, doi:10.1007/s00439-002-0712-8. This article has 74 citations and is from a peer-reviewed journal.

4. (pagnamenta2024theimpactof pages 1-2): Alistair T. Pagnamenta, Jing Yu, Susan Walker, Alexandra J. Noble, Jenny Lord, Prasun Dutta, Mona Hashim, Carme Camps, Hannah Green, Smrithi Devaiah, Lina Nashef, Jason Parr, Carl Fratter, Rana Ibnouf Hussein, Sarah J. Lindsay, Fiona Lalloo, Benito Banos-Pinero, David Evans, Lucy Mallin, Adrian Waite, Julie Evans, Andrew Newman, Zoe Allen, Cristina Perez-Becerril, Gavin Ryan, Rachel Hart, John Taylor, Tina Bedenham, Emma Clement, Ed Blair, Eleanor Hay, Francesca Forzano, Jenny Higgs, Natalie Canham, Anirban Majumdar, Meriel McEntagart, Nayana Lahiri, Helen Stewart, Sarah Smithson, Eduardo Calpena, Adam Jackson, Siddharth Banka, Hannah Titheradge, Ruth McGowan, Julia Rankin, Charles Shaw-Smith, D. Gareth Evans, George J. Burghel, Miriam J. Smith, Emily Anderson, Rajesh Madhu, Helen Firth, Sian Ellard, Paul Brennan, Claire Anderson, Doug Taupin, Mark T. Rogers, Jackie A. Cook, Miranda Durkie, James E. East, Darren Fowler, Louise Wilson, Rebecca Igbokwe, Alice Gardham, Ian Tomlinson, Diana Baralle, Holm H. Uhlig, and Jenny C. Taylor. The impact of inversions across 33,924 families with rare disease from a national genome sequencing project. The American Journal of Human Genetics, 111:1140-1164, Jun 2024. URL: https://doi.org/10.1016/j.ajhg.2024.04.018, doi:10.1016/j.ajhg.2024.04.018. This article has 36 citations.

5. (jaouadi2023geneticandphenotypic pages 1-2): Hager Jaouadi, Alexis Theron, Giulia Norscini, Jean-François Avierinos, and Stéphane Zaffran. Genetic and phenotypic continuum of hoxa genes: a case with double hoxa9/hoxa13 mutations. Molecular Medicine Reports, Jan 2023. URL: https://doi.org/10.3892/mmr.2023.12946, doi:10.3892/mmr.2023.12946. This article has 3 citations and is from a peer-reviewed journal.

6. (owens2013analysisofde pages 2-3): Kailey M. Owens, Shane C. Quinonez, Peedikayil E. Thomas, Catherine E. Keegan, Nanci Lefebvre, Diane Roulston, Christine A. Larsen, H. Scott Stadler, and Jeffrey W. Innis. Analysis of de novo hoxa13 polyalanine expansions supports replication slippage without repair in their generation. American Journal of Medical Genetics Part A, 161:1019-1027, May 2013. URL: https://doi.org/10.1002/ajmg.a.35843, doi:10.1002/ajmg.a.35843. This article has 11 citations.

7. (imagawa2014severemanifestationsof pages 4-5): Eri Imagawa, Hülya Kayserili, Gen Nishimura, Mitsuko Nakashima, Yoshinori Tsurusaki, Hirotomo Saitsu, Shiro Ikegawa, Naomichi Matsumoto, and Noriko Miyake. Severe manifestations of hand‐foot‐genital syndrome associated with a novel hoxa13 mutation. American Journal of Medical Genetics Part A, 164:2398-2402, Sep 2014. URL: https://doi.org/10.1002/ajmg.a.36648, doi:10.1002/ajmg.a.36648. This article has 26 citations.

8. (innis2004polyalanineexpansionin pages 1-2): Jeffrey W. Innis, Douglas Mortlock, Zhi Chen, Michael Ludwig, Melissa E. Williams, Thomas M. Williams, Colleen D. Doyle, Zhihong Shao, Michael Glynn, Davor Mikulic, Katarina Lehmann, Stefan Mundlos, and Boris Utsch. Polyalanine expansion in hoxa13: three new affected families and the molecular consequences in a mouse model. Human molecular genetics, 13 22:2841-51, Nov 2004. URL: https://doi.org/10.1093/hmg/ddh306, doi:10.1093/hmg/ddh306. This article has 59 citations and is from a domain leading peer-reviewed journal.

9. (frisen2003anovelduplication pages 1-1): L. Frisén, K. Lagerstedt, M. Tapper-Persson, Ingrid Kockum, and A. Nordenskjöld. A novel duplication in the hoxa13 gene in a family with atypical hand-foot-genital syndrome. Journal of Medical Genetics, 40:e49-e49, Apr 2003. URL: https://doi.org/10.1136/jmg.40.4.e49, doi:10.1136/jmg.40.4.e49. This article has 37 citations and is from a domain leading peer-reviewed journal.

10. (frisen2003anovelduplication pages 5-5): L. Frisén, K. Lagerstedt, M. Tapper-Persson, Ingrid Kockum, and A. Nordenskjöld. A novel duplication in the hoxa13 gene in a family with atypical hand-foot-genital syndrome. Journal of Medical Genetics, 40:e49-e49, Apr 2003. URL: https://doi.org/10.1136/jmg.40.4.e49, doi:10.1136/jmg.40.4.e49. This article has 37 citations and is from a domain leading peer-reviewed journal.

11. (utsch2002anovelstable pages 6-7): Boris Utsch, Karl Becker, Detlef Brock, Michael J. Lentze, Frank Bidlingmaier, and Michael Ludwig. A novel stable polyalanine [poly(a)] expansion in the hoxa13 gene associated with hand-foot-genital syndrome: proper function of poly(a)-harbouring transcription factors depends on a critical repeat length? Human Genetics, 110:488-494, Apr 2002. URL: https://doi.org/10.1007/s00439-002-0712-8, doi:10.1007/s00439-002-0712-8. This article has 74 citations and is from a peer-reviewed journal.

12. (wallis2016dualgeneticdiagnoses pages 6-7): Mathew Wallis, Yoshinori Tsurusaki, Trent Burgess, Peter Borzi, Naomichi Matsumoto, Noriko Miyake, Deanna True, and Chirag Patel. Dual genetic diagnoses: atypical hand‐foot‐genital syndrome and developmental delay due to de novo mutations in hoxa13 and nrxn1. American Journal of Medical Genetics Part A, 170:717-724, Mar 2016. URL: https://doi.org/10.1002/ajmg.a.37478, doi:10.1002/ajmg.a.37478. This article has 15 citations.
