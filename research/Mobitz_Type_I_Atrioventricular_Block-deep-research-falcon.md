---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T23:20:40.829526'
end_time: '2026-05-05T23:48:28.675419'
duration_seconds: 1667.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mobitz Type I Atrioventricular Block
  mondo_id: ''
  category: Heart Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mobitz Type I Atrioventricular Block
- **MONDO ID:**  (if available)
- **Category:** Heart Disorder

## Research Objectives

Please provide a comprehensive research report on **Mobitz Type I Atrioventricular Block** covering all of the
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
- **Disease Name:** Mobitz Type I Atrioventricular Block
- **MONDO ID:**  (if available)
- **Category:** Heart Disorder

## Research Objectives

Please provide a comprehensive research report on **Mobitz Type I Atrioventricular Block** covering all of the
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


# Comprehensive Disease Characteristics Research Report: Mobitz Type I Atrioventricular Block (Wenckebach)

## Executive summary
Mobitz type I atrioventricular (AV) block (Wenckebach) is a second-degree AV conduction pattern characterized by progressive PR prolongation followed by a non-conducted P wave, most commonly due to AV nodal (often vagally mediated) conduction delay. Contemporary guidance emphasizes (i) avoiding misdiagnosis with Mobitz II and pseudo–AV block, (ii) determining whether the block is nodal vs infranodal and whether symptoms temporally correlate, and (iii) reserving permanent pacing for persistent symptomatic cases or confirmed infranodal disease; asymptomatic vagally mediated/nodal Wenckebach should generally not be paced. (kusumoto20192018accahahrsguideline pages 48-49, kusumoto20192018accahahrsguideline pages 49-50, kusumoto20192018accahahrsguideline pages 45-48, canoy2024mobitztypeii pages 2-3, canoy2024mobitztypeii pages 3-5)

## Key synthesis tables
The following tables summarize core definitions/guideline points and quantitative statistics.

| Item | Evidence summary | Source (citation id) | Publication year | URL |
|---|---|---|---|---|
| Disease name and synonyms | Mobitz type I atrioventricular block is also called Wenckebach second-degree AV block or Wenckebach periodicity. It is a second-degree AV block pattern characterized by cyclical PR prolongation followed by a non-conducted P wave. (morita2025longtermmanagementof pages 1-3, barold2018typeiwenckebach pages 2-3) | (morita2025longtermmanagementof pages 1-3, barold2018typeiwenckebach pages 2-3) | 2025; 2018 | https://doi.org/10.1292/jvms.24-0521; https://doi.org/10.1002/clc.22874 |
| Key diagnostic definition / ECG criteria | ECG definition: repeated cycles of gradually lengthening PR intervals followed by a dropped QRS complex/non-conducted P wave. A shortening of the PR interval of the first conducted beat after the block supports Wenckebach. Vagal Wenckebach may show sinus slowing and can occasionally have an unchanged post-block PR, creating diagnostic confusion. (morita2025longtermmanagementof pages 1-3, canoy2024mobitztypeii pages 3-5, canoy2024mobitztypeii pages 2-3) | (morita2025longtermmanagementof pages 1-3, canoy2024mobitztypeii pages 3-5, canoy2024mobitztypeii pages 2-3) | 2025; 2024 | https://doi.org/10.1292/jvms.24-0521; https://doi.org/10.3389/fcvm.2024.1450705 |
| Typical anatomic level | Mobitz I is usually an AV nodal block and is often vagally mediated; narrow-QRS Mobitz I is almost always AV nodal. Broad-QRS Mobitz I can still be nodal but is more often His–Purkinje/infranodal. In inferior STEMI, Wenckebach commonly reflects AV nodal ischemia because the AV nodal artery arises from the RCA in about 90% of patients. (kusumoto20192018accahahrsguideline pages 48-49, barold2018typeiwenckebach pages 2-3, karaman2026…clinicaldeterioration pages 110-115) | (kusumoto20192018accahahrsguideline pages 48-49, barold2018typeiwenckebach pages 2-3, karaman2026…clinicaldeterioration pages 110-115) | 2019; 2018; 2026 | https://doi.org/10.1016/j.jacc.2018.10.044; https://doi.org/10.1002/clc.22874 |
| Distinguishing features vs Mobitz II | Differentiation matters because prognosis differs. Mobitz II requires a stable sinus rate and constant PR intervals before and after a blocked beat; correctly identified Mobitz II is typically His–Purkinje disease and generally indicates pacemaker therapy. In contrast, vagally mediated Wenckebach shows sinus slowing; ignoring sinus slowing can mislabel vagal Wenckebach as Mobitz II. A 2:1 AV block cannot be classified as type I or II from ECG alone. (kusumoto20192018accahahrsguideline pages 49-50, canoy2024mobitztypeii pages 2-3, canoy2024mobitztypeii pages 1-2) | (kusumoto20192018accahahrsguideline pages 49-50, canoy2024mobitztypeii pages 2-3, canoy2024mobitztypeii pages 1-2) | 2019; 2024 | https://doi.org/10.1016/j.jacc.2018.10.044; https://doi.org/10.3389/fcvm.2024.1450705 |
| Reversible causes / provoking factors | Common reversible or provoking factors include increased vagal tone, inferior myocardial ischemia/infarction, and AV nodal–depressing drugs such as beta-blockers, non-dihydropyridine calcium-channel blockers, digoxin, and some antiarrhythmics. The guideline also lists reversible AV block causes such as Lyme carditis, electrolyte disturbances, drug toxicity, and obstructive sleep apnea. A 2024 pediatric case showed remifentanil exposure producing sinus bradycardia, Wenckebach-type block, then complete AV block, reversing after stopping the drug and giving atropine/adrenaline. (karaman2026…clinicaldeterioration pages 110-115, sfairopoulos2025clinicalsignificanceand pages 1-2, kusumoto20192018accahahrsguideline pages 48-49, ura2024repeatedcompleteatrioventricular pages 1-3, ura2024repeatedcompleteatrioventricular pages 3-5) | (karaman2026…clinicaldeterioration pages 110-115, sfairopoulos2025clinicalsignificanceand pages 1-2, kusumoto20192018accahahrsguideline pages 48-49, ura2024repeatedcompleteatrioventricular pages 1-3, ura2024repeatedcompleteatrioventricular pages 3-5) | 2026; 2025; 2019; 2024 | https://doi.org/10.1111/jce.16697; https://doi.org/10.1016/j.jacc.2018.10.044; https://doi.org/10.1186/s12871-024-02593-8 |
| Guideline points on pacing | 2018 ACC/AHA/HRS: permanent pacing is symptom-driven for Mobitz I. Permanent pacing should not be performed in asymptomatic patients when the block is believed to be at the AV node, or when symptoms do not temporally correspond to the AV block (Class III: Harm). If symptomatic AV block due to a reversible cause does not resolve after treatment, permanent pacing is recommended; if acute reversible, nonrecurrent AV block fully resolves, permanent pacing should not be performed. Ambulatory ECG monitoring and exercise testing are reasonable to correlate symptoms and assess nodal vs infranodal block. (kusumoto20192018accahahrsguideline pages 48-49, kusumoto20192018accahahrsguideline pages 49-50, kusumoto20192018accahahrsguideline pages 45-48, salim2020mobitztypeii pages 5-6) | (kusumoto20192018accahahrsguideline pages 48-49, kusumoto20192018accahahrsguideline pages 49-50, kusumoto20192018accahahrsguideline pages 45-48, salim2020mobitztypeii pages 5-6) | 2019; 2020 | https://doi.org/10.1016/j.jacc.2018.10.044; https://doi.org/10.30701/ijc.950 |
| Acute management pearls | AV nodal Wenckebach is often atropine-responsive. In inferior STEMI, Wenckebach is generally transient, often resolving within 3–7 days, with favorable prognosis; temporary/transvenous pacing is reserved for hemodynamically unstable patients or those not responding to medical therapy. Atropine is less useful for infranodal block and may worsen intra-His/distal disease. (karaman2026…clinicaldeterioration pages 110-115, kusumoto20192018accahahrsguideline pages 49-50) | (karaman2026…clinicaldeterioration pages 110-115, kusumoto20192018accahahrsguideline pages 49-50) | 2026; 2019 | https://doi.org/10.1016/j.jacc.2018.10.044 |
| Benign physiologic context | In trained athletes, first-degree AV block and Mobitz I are considered normal/physiologic findings related to increased vagal tone and typically normalize with exercise; by contrast, Mobitz II and complete AV block are abnormal and warrant specialist assessment. (rakhmanov2024ecginathletes pages 5-8, rakhmanov2024ecginathletes pages 16-19, rakhmanov2024ecginathletes pages 1-5) | (rakhmanov2024ecginathletes pages 5-8, rakhmanov2024ecginathletes pages 16-19, rakhmanov2024ecginathletes pages 1-5) | 2024 | https://doi.org/10.5772/intechopen.1004231 |


*Table: This table summarizes the core definitional, diagnostic, anatomic, and guideline-management evidence for Mobitz type I (Wenckebach) AV block using only the cited context sources. It is useful as a compact reference for distinguishing benign AV nodal Wenckebach from higher-risk conduction disease and for capturing pacing/reversibility guidance.*

| Study (year) | Population | Outcome/statistic | Numeric value(s) | Notes | URL | Citation id |
|---|---|---|---|---|---|---|
| Kerola et al. (2019) | Mini-Finland community cohort | Cohort size and AV block events | n=6,146; hospitalized with 2nd- or 3rd-degree AV block: 58 (0.9%) | Population-based risk-factor study of incident AV block | https://doi.org/10.1001/jamanetworkopen.2019.4176 | (kerola2019riskfactorsassociated pages 1-2) |
| Kerola et al. (2019) | Same cohort | Risk per systolic blood pressure increase | HR 1.22 per 10 mm Hg increase (95% CI 1.10-1.34; P=.005) | Association remained significant after adjustment in sensitivity analyses | https://doi.org/10.1001/jamanetworkopen.2019.4176 | (kerola2019riskfactorsassociated pages 1-2, kerola2019riskfactorsassociated pages 4-5) |
| Kerola et al. (2019) | Same cohort | Risk per fasting glucose increase | HR 1.22 per 20 mg/dL increase (95% CI 1.08-1.35; P=.001) | Adjusted HR reported as 1.22 (95% CI 1.04-1.43; P=.01) after accounting for major adverse coronary events | https://doi.org/10.1001/jamanetworkopen.2019.4176 | (kerola2019riskfactorsassociated pages 1-2) |
| Kerola et al. (2019) | Same cohort | Population-attributable risk (PAR) | SBP PAR 47% (95% CI 8%-67%); fasting glucose PAR 11% (95% CI 2%-21%) | Suggests modifiable BP and glucose may explain a substantial fraction of AV block burden | https://doi.org/10.1001/jamanetworkopen.2019.4176 | (kerola2019riskfactorsassociated pages 1-2) |
| Kerola et al. (2019) | Same cohort | Third-degree AV block events and risks | Third-degree AV block cases: 40; SBP HR 1.27 (95% CI 1.08-1.47; P=.002); fasting glucose HR 1.20 (95% CI 1.02-1.18; P=.02) | Event subset from total AV block analyses | https://doi.org/10.1001/jamanetworkopen.2019.4176 | (kerola2019riskfactorsassociated pages 6-7) |
| Dideriksen et al. (2021) | Danish patients <50 years with AV block of unknown aetiology treated with first pacemaker, plus matched controls | Cohort size and follow-up | Patients: 517; controls: 5,170; median age 41.3 years; median follow-up 9.8 years | Young-onset AV block of unknown cause; not specific to Mobitz I but highly relevant to prognosis of AV block phenotypes requiring pacing | https://doi.org/10.1093/eurheartj/ehab060 | (sfairopoulos2025clinicalsignificanceand pages 4-4) |
| Dideriksen et al. (2021) | Same cohort | Primary composite outcome occurrence | 14.9% in patients vs 3.2% in controls | Composite: death, heart failure hospitalization, ventricular tachyarrhythmia, or resuscitated cardiac arrest | https://doi.org/10.1093/eurheartj/ehab060 | (sfairopoulos2025clinicalsignificanceand pages 4-4) |
| Dideriksen et al. (2021) | Same cohort | Relative risk of adverse outcome | HR 3.8 (95% CI 2.9-5.1; P<0.001) | AV block of unknown aetiology associated with 3- to 4-fold higher event rate vs controls | https://doi.org/10.1093/eurheartj/ehab060 | (sfairopoulos2025clinicalsignificanceand pages 4-4) |
| Dideriksen et al. (2021) | Same cohort | Higher-risk subgroup and early follow-up risk | Persistent AV block HR 10.6 (95% CI 5.7-20.0; P<0.001); 0-5 year follow-up HR 6.8 (95% CI 4.6-10.0; P<0.001) | Persistent block at diagnosis conveyed especially high risk | https://doi.org/10.1093/eurheartj/ehab060 | (sfairopoulos2025clinicalsignificanceand pages 4-4) |
| Andersen et al. (2013) | 52,755 long-distance cross-country skiers | Cohort size | n=52,755 | Endurance athlete cohort examining arrhythmia risk | https://doi.org/10.1093/eurheartj/eht188 | (andersen2013riskofarrhythmias pages 4-5) |
| Andersen et al. (2013) | Same athlete cohort | Bradyarrhythmia diagnosis counts | Total bradyarrhythmias 122; second-degree AV block 31; complete AV block 34; sick sinus syndrome 49 | Study notes Mobitz I/Wenckebach, sinus bradycardia, and first-degree AV block are usually considered normal findings in athletes | https://doi.org/10.1093/eurheartj/eht188 | (andersen2013riskofarrhythmias pages 4-5) |
| Andersen et al. (2013) | Same athlete cohort | Performance-category trend for bradyarrhythmias | Hazard ratio per category 1.16 (95% CI 0.95-1.40) | Non-significant trend across performance/finishing-time groups | https://doi.org/10.1093/eurheartj/eht188 | (andersen2013riskofarrhythmias pages 4-5) |
| MI-related Wenckebach excerpt (2026 source) | Inferior STEMI / AV nodal ischemia context | AV nodal artery origin from RCA | ~90% | Supports why Wenckebach in inferior MI is commonly AV nodal | Not available in excerpt | (karaman2026…clinicaldeterioration pages 110-115) |
| MI-related Wenckebach excerpt (2026 source) | Inferior STEMI / AV nodal ischemia context | Typical resolution time of Wenckebach | Resolves within 3-7 days | Transient, atropine-responsive, generally favorable prognosis in inferior MI | Not available in excerpt | (karaman2026…clinicaldeterioration pages 110-115) |
| MI-related Wenckebach excerpt (2026 source) | Inferior STEMI / RV infarction context | RV infarction complicating inferior STEMI | 30%-50% | Included as additional quantitative context in inferior MI with conduction disturbance | Not available in excerpt | (karaman2026…clinicaldeterioration pages 110-115) |


*Table: This table compiles key numeric findings from the available evidence relevant to Mobitz type I/Wenckebach and closely related AV block outcomes, including risk factors, prognosis, athlete data, and MI-associated transient Wenckebach. It is useful for quickly locating cohort sizes, hazard ratios, attributable risks, and clinically relevant time-course statistics.*

---

## 1. Disease information
### 1.1 Overview / definition (current understanding)
Mobitz type I (Wenckebach) AV block is a second-degree AV block pattern in which the PR interval progressively lengthens over consecutive beats until a P wave fails to conduct (dropped QRS), often repeating in cycles (“grouped beating”). (morita2025longtermmanagementof pages 1-3)

A key discriminator in typical Wenckebach is that the first conducted beat after the dropped beat has a shorter PR interval than the preceding conducted PR interval(s). (canoy2024mobitztypeii pages 3-5)

Mobitz I is commonly AV nodal in origin and frequently associated with vagal surges (sinus slowing with concomitant AV nodal conduction depression). (kusumoto20192018accahahrsguideline pages 48-49, canoy2024mobitztypeii pages 2-3)

### 1.2 Key identifiers (ICD/MeSH/MONDO)
* **ICD-9 evidence in retrieved literature:** ICD-9 code **I44.1** was used to identify second-degree AV block hospitalizations in a population cohort study of incident AV block risk factors. (kerola2019riskfactorsassociated pages 2-4)
* **ICD-10 / ICD-11 / MeSH / MONDO:** Not available from the retrieved full-text evidence in this run; therefore not asserted.

### 1.3 Synonyms / alternative names
* Mobitz type I AV block
* Wenckebach AV block
* Wenckebach periodicity
* Luciani–Wenckebach (used in sports cardiology guidance)
(morita2025longtermmanagementof pages 1-3, zeppilli2024italiancardiologicalguidelines pages 7-8)

### 1.4 Evidence sources in this report
This entry is derived from **aggregated disease-level resources** (ACC/AHA/HRS guideline; reviews) plus **case reports** illustrating reversible causes and management decisions. (kusumoto20192018accahahrsguideline pages 48-49, ura2024repeatedcompleteatrioventricular pages 1-3, ura2024repeatedcompleteatrioventricular pages 3-5)

---

## 2. Etiology
### 2.1 Disease causal factors (common causes / contexts)
Mobitz I is most often AV nodal and frequently reflects **vagal hypertonicity** (physiologic in sleep and in trained athletes) or **transient AV nodal depression**. (kusumoto20192018accahahrsguideline pages 48-49, rakhmanov2024ecginathletes pages 5-8, zeppilli2024italiancardiologicalguidelines pages 8-10)

Other clinically important causes/contexts include:
* **Inferior myocardial infarction / AV nodal ischemia:** Wenckebach in inferior STEMI is commonly AV nodal because the AV nodal artery arises from the RCA in ~90% of patients; it is typically transient and “resolving within 3–7 days.” (karaman2026…clinicaldeterioration pages 110-115)
* **Drug/toxin-related AV nodal depression:** beta-blockers, non-dihydropyridine calcium channel blockers, digoxin, and antiarrhythmics are commonly implicated reversible contributors to AV block. (sfairopoulos2025clinicalsignificanceand pages 1-2, kusumoto20192018accahahrsguideline pages 48-49)
* **Other reversible causes noted in guideline:** metabolic derangements (e.g., hyperkalemia), infections (e.g., Lyme), obstructive sleep apnea, and drug toxicity/overdose. (kusumoto20192018accahahrsguideline pages 48-49)

### 2.2 Risk factors (population-level)
In a community-based cohort (Mini-Finland), elevated systolic blood pressure and fasting glucose were associated with hospitalization for second- or third-degree AV block (not subtype-specific to Mobitz I, but relevant to conduction disease burden). (kerola2019riskfactorsassociated pages 1-2)

Key quantitative results (see artifact-01):
* n=6,146; AV block events=58 (0.9%). (kerola2019riskfactorsassociated pages 1-2)
* HR 1.22 per 10 mmHg systolic BP increase; HR 1.22 per 20 mg/dL fasting glucose increase; population-attributable risk (PAR) estimates: 47% (BP) and 11% (fasting glucose). (kerola2019riskfactorsassociated pages 1-2)

### 2.3 Protective factors
Direct protective factors specific to Mobitz I were not identified in the retrieved evidence. A practical “protective” clinical feature is **normalization with exercise** (suggesting physiologic/vagal nodal delay rather than fixed infranodal disease), which is used in athlete eligibility evaluations. (zeppilli2024italiancardiologicalguidelines pages 7-8, zeppilli2024italiancardiologicalguidelines pages 8-10)

### 2.4 Gene–environment interactions
The retrieved evidence supports interaction between genetic predisposition to conduction disease (ion-channel/gap-junction/nuclear envelope genes) and acquired modifiers such as inflammation, autoimmunity, or autonomic tone, but specific gene–environment interaction studies for Mobitz I were not available in the retrieved texts. (li2024cardiacconductiondiseases pages 9-11, li2024cardiacconductiondiseases pages 23-28)

---

## 3. Phenotypes
### 3.1 Core clinical phenotypes
Mobitz I may be asymptomatic or manifest with:
* Dizziness/lightheadedness
* Presyncope/syncope
* Exertional chest pain or shortness of breath (when conduction worsens or rate response inadequate)
(kusumoto20192018accahahrsguideline pages 45-48, kusumoto20192018accahahrsguideline pages 48-49)

In vagally mediated cases, episodes often occur during sleep or reflex neural surges and may show sinus slowing with onset of AV block. (kusumoto20192018accahahrsguideline pages 48-49, canoy2024mobitztypeii pages 2-3)

### 3.2 Phenotype characteristics (onset, severity, progression)
* **Onset:** can be incidental and intermittent; may be nocturnal (athletes) or triggered by acute illness/drugs. (kusumoto20192018accahahrsguideline pages 48-49, zeppilli2024italiancardiologicalguidelines pages 8-10)
* **Severity:** typically benign when nodal/vagal; can be clinically significant if infranodal or associated with prolonged pauses/syncope. (kusumoto20192018accahahrsguideline pages 45-48, salim2020mobitztypeii pages 5-6)
* **Progression:** nodal Wenckebach “is typically benign and does not commonly progress suddenly to complete heart block.” (kusumoto20192018accahahrsguideline pages 45-48)

### 3.3 Suggested HPO terms (examples)
(ontology suggestions; not exhaustively validated in retrieved sources)
* Second-degree atrioventricular block (HP term suggestion)
* Bradycardia (HP term suggestion)
* Syncope (HP term suggestion)
* Presyncope/dizziness (HP term suggestion)
* Exercise intolerance / dyspnea on exertion (HP term suggestion)

### 3.4 Quality-of-life impact
The guideline emphasizes that pacemaker therapy (when used) is generally reserved for “significant symptoms that affect quality of life,” indicating symptom burden drives intervention decisions. (kusumoto20192018accahahrsguideline pages 45-48)

---

## 4. Genetic / molecular information
### 4.1 Causal genes and molecular contributors (evidence-based candidates)
Mobitz I itself is often functional/vagal; however, Wenckebach-like AV nodal conduction phenotypes can appear within broader cardiac conduction system disease. A 2024 mechanistic review enumerates genes and molecular classes implicated in AV nodal conduction disease and AV block, including:
* **Ion channels:** SCN5A, SCN1B, CACNA1C, CACNA1G, KCNH2, KCNJ2, KCNQ1, HCN4, TRPM4. (li2024cardiacconductiondiseases pages 8-9)
* **Gap junction / connexins:** multiple connexin genes are implicated (e.g., GJA5/Cx40, GJC1/Cx45), and scaffolding interactions (ZO-1) regulate connexin and Nav1.5 localization. (li2024cardiacconductiondiseases pages 9-11, li2024cardiacconductiondiseases pages 19-20)
* **Nuclear envelope / structural:** lamin A/C (LMNA) and EMD are linked to conduction disease phenotypes including AV block. (li2024cardiacconductiondiseases pages 19-20, li2024cardiacconductiondiseases pages 30-32)

### 4.2 Mechanistic examples linking to Wenckebach phenotype
* **Inflammatory cytokine mechanism:** TNF-α overexpression was associated with “prolonged PR interval, AVN Wenckebach, and extended effective and functional refractory periods,” supporting inflammation-driven AV nodal refractoriness changes as a mechanistic route to Wenckebach. (li2024cardiacconductiondiseases pages 9-11)
* **Autonomic (vagal) mechanism:** A vagal surge can produce simultaneous sinus slowing and AV nodal conduction depression, generating vagally mediated Wenckebach patterns. (canoy2024mobitztypeii pages 2-3)

### 4.3 Variant-level, allele frequency, and ClinVar/gnomAD information
Specific pathogenic variants, ACMG classifications, and population allele frequencies were not present in retrieved evidence; thus not asserted.

### 4.4 Suggested GO biological process / cellular component terms (examples)
* Cardiac conduction (GO term suggestion)
* Regulation of heart rate by autonomic nervous system (GO term suggestion)
* Cell–cell junction organization / gap junction assembly (GO term suggestion)
* Inflammatory response / cytokine-mediated signaling (GO term suggestion)

### 4.5 Suggested Cell Ontology (CL) terms (examples)
* Cardiac muscle cell / cardiomyocyte (CL term suggestion)
* Atrioventricular node cell / conduction system cell (CL term suggestion)
* Macrophage (re: macrophage–connexin conduction concept discussed in conduction disease review) (li2024cardiacconductiondiseases pages 9-11)

---

## 5. Environmental information
Key non-genetic contributors are largely clinical/iatrogenic and physiologic:
* **High vagal tone** (sleep, athletic training). (rakhmanov2024ecginathletes pages 5-8, zeppilli2024italiancardiologicalguidelines pages 8-10)
* **Medication exposures** that depress AV nodal conduction (beta-blockers, non-DHP CCBs, digoxin, antiarrhythmics). (sfairopoulos2025clinicalsignificanceand pages 1-2, kusumoto20192018accahahrsguideline pages 48-49)
* **Anesthesia/opioid exposure example:** Remifentanil can trigger bradycardia progressing through Wenckebach-type block to complete AV block, reversing with drug cessation and atropine/adrenaline. (ura2024repeatedcompleteatrioventricular pages 1-3, ura2024repeatedcompleteatrioventricular pages 3-5)

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (nodal/vagal Wenckebach – typical)
**Trigger** (vagal surge during sleep/training; vagomimetic drugs; autonomic reflex) → **AV nodal refractoriness increases / conduction slows** (often with sinus slowing) → **progressive PR prolongation** → **non-conducted P wave (dropped QRS)** → symptoms may occur if ventricular pauses reduce cerebral perfusion (presyncope/syncope). (canoy2024mobitztypeii pages 2-3, kusumoto20192018accahahrsguideline pages 48-49)

### 6.2 Ischemic Wenckebach (inferior MI context)
Inferior MI (often RCA) → AV nodal ischemia (AV nodal artery RCA origin ~90%) → AV nodal Wenckebach with narrow-QRS escape → typically transient (3–7 days) and atropine responsive; pacing reserved for instability. (karaman2026…clinicaldeterioration pages 110-115)

### 6.3 Distinguishing pathophysiology: nodal vs infranodal Wenckebach
Although Wenckebach is usually nodal, it can be infranodal in a subset, particularly with wide QRS or in the presence of His–Purkinje disease; infranodal disease has different prognosis and may prompt pacing even without symptoms. (kusumoto20192018accahahrsguideline pages 45-48, barold2018typeiwenckebach pages 2-3)

### 6.4 Differential mechanisms / pseudo–AV block
Pseudo–AV block can arise from concealed extrasystoles (junctional/His–Purkinje), non-conducted atrial premature beats, or interpolated PVCs with concealed retrograde conduction, creating patterns that mimic Wenckebach or Mobitz II. (canoy2024mobitztypeii pages 3-5, canoy2024mobitztypeii pages 5-7)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
* **Primary system:** cardiovascular system—cardiac conduction system. (kusumoto20192018accahahrsguideline pages 48-49, li2024cardiacconductiondiseases pages 8-9)

### 7.2 Key structures (UBERON suggestions)
* Heart (UBERON term suggestion)
* Atrioventricular node (UBERON term suggestion)
* His bundle / His–Purkinje system (UBERON term suggestion)

### 7.3 Subcellular/structural correlates
Conduction disease mechanisms emphasize membrane ion channels (Na+, Ca2+), gap junctions/connexins, and scaffolding proteins regulating channel localization. (li2024cardiacconductiondiseases pages 9-11, li2024cardiacconductiondiseases pages 19-20)

---

## 8. Temporal development
### 8.1 Onset
Mobitz I may present intermittently, often during sleep or in specific physiological states (athletes), or acutely after exposures (e.g., drug effect) or ischemia (inferior MI). (ura2024repeatedcompleteatrioventricular pages 1-3, ura2024repeatedcompleteatrioventricular pages 3-5, zeppilli2024italiancardiologicalguidelines pages 8-10)

### 8.2 Progression and course
* Nodal/vagal Mobitz I is generally benign and not commonly progressing suddenly to complete heart block. (kusumoto20192018accahahrsguideline pages 45-48)
* In inferior MI, Wenckebach is often transient (3–7 days). (karaman2026…clinicaldeterioration pages 110-115)

---

## 9. Inheritance and population
### 9.1 Epidemiology
Mobitz I–specific population prevalence was not identified in the retrieved evidence. However, AV block hospitalizations (second/third degree) were 0.9% over long follow-up in a 6,146-person community cohort. (kerola2019riskfactorsassociated pages 1-2)

### 9.2 Athlete populations
Sports cardiology guidance characterizes Mobitz I (Luciani–Wenckebach) as common in highly trained athletes (often nocturnal) and compatible with eligibility when it normalizes with increased heart rate and there is no structural heart disease or concerning pauses. (zeppilli2024italiancardiologicalguidelines pages 7-8, zeppilli2024italiancardiologicalguidelines pages 8-10)

---

## 10. Diagnostics
### 10.1 Core diagnostic test: ECG
Diagnostic criterion: progressive PR lengthening with a dropped beat in repeated cycles. (morita2025longtermmanagementof pages 1-3)

### 10.2 Diagnostic strategy in practice (ACC/AHA/HRS)
Because symptoms may be intermittent, the guideline recommends establishing symptom–rhythm correlation, often requiring longer-term monitoring:
* **Ambulatory ECG monitoring:** 30–90 day event monitors or implanted devices have greater yield than 24–48h monitoring. (kusumoto20192018accahahrsguideline pages 49-50)
* **Exercise treadmill testing:** reasonable in exertional symptoms to assess benefit from pacing and to help localize nodal vs infranodal block (nodal improves with exercise; infranodal typically does not). (kusumoto20192018accahahrsguideline pages 49-50, kusumoto20192018accahahrsguideline pages 45-48)
* **EPS (His recordings):** may be used to localize block and evaluate mimics (His extrasystoles). (kusumoto20192018accahahrsguideline pages 49-50)

### 10.3 Differential diagnosis considerations (misinterpretation risks)
* **Do not classify 2:1 AV block as Mobitz I or II by ECG alone** (classification may require further evaluation). (canoy2024mobitztypeii pages 1-2)
* **Vagal Wenckebach may mimic Mobitz II** when PR intervals appear constant; sinus slowing (P–P lengthening) is a critical clue and argues against true Mobitz II. (canoy2024mobitztypeii pages 2-3, canoy2024mobitztypeii pages 5-7)
* **Pseudo–AV block** due to concealed extrasystoles or poor P-wave visibility can mislead and may require EPS to prevent unnecessary pacing. (canoy2024mobitztypeii pages 5-7)

---

## 11. Outcome / prognosis
### 11.1 Prognosis of nodal/vagal Wenckebach
Guideline perspective: Mobitz I (especially nodal) is typically benign; pacing is symptom-driven, and asymptomatic nodal/vagal AV block should not be paced (Class III: Harm). (kusumoto20192018accahahrsguideline pages 45-48, kusumoto20192018accahahrsguideline pages 48-49)

### 11.2 Contextual prognosis: MI-related Wenckebach
In inferior MI, Wenckebach is generally transient with favorable prognosis and typically resolves within 3–7 days. (karaman2026…clinicaldeterioration pages 110-115)

### 11.3 Broader AV block outcomes (not Mobitz I–specific)
Young patients (<50) requiring pacing for AV block of unknown aetiology had higher long-term adverse outcomes than matched controls (composite endpoint 14.9% vs 3.2%; HR 3.8) over median 9.8 years, emphasizing that some conduction disease presentations in younger patients are not benign. (sfairopoulos2025clinicalsignificanceand pages 4-4)

---

## 12. Treatment
### 12.1 General management principles (ACC/AHA/HRS 2018 guideline; published 2019)
* **Symptom correlation is central:** pacemaker need is “symptom driven.” (kusumoto20192018accahahrsguideline pages 49-50)
* **Avoid unnecessary pacing:** permanent pacing should not be performed in asymptomatic patients when block is believed nodal, and should not be performed when symptoms do not temporally correspond (Class III: Harm). (kusumoto20192018accahahrsguideline pages 45-48)
* **Reversible causes:** if symptomatic AV block is due to a reversible cause and does not resolve after treatment, permanent pacing is recommended (Class I); if acute AV block from a reversible, nonrecurrent cause resolves completely, permanent pacing should not be performed (Class III: Harm). (kusumoto20192018accahahrsguideline pages 48-49)

### 12.2 Acute/urgent management (real-world implementation)
In AV nodal Wenckebach with hemodynamic compromise:
* **Atropine** is first-line for AV nodal block; infranodal block responds poorly and may worsen with atropine. (karaman2026…clinicaldeterioration pages 110-115, kusumoto20192018accahahrsguideline pages 49-50)
* **Pacing (temporary/transvenous or transcutaneous)** is reserved for unstable patients unresponsive to medication. (karaman2026…clinicaldeterioration pages 110-115)

### 12.3 Athlete-specific implementation
Italian COCIS 2024 guidance: Mobitz I is generally compatible with competitive sport if it normalizes with increased heart rate (exercise testing/monitoring) and there are no symptoms or structural heart disease; nocturnal advanced AV block due to vagal hypertonicity may be compatible if it disappears after detraining and does not include pauses >3 seconds. (zeppilli2024italiancardiologicalguidelines pages 7-8, zeppilli2024italiancardiologicalguidelines pages 8-10)

### 12.4 Emerging/advanced therapeutic approaches: cardioneuroablation (CNA)
A 2024 Frontiers review describes CNA as a strategy for recurrent vasovagal syncope and vagally mediated advanced AV block/Wenckebach in young patients by ablating cardiac parasympathetic ganglionated plexi near the SA and AV nodes. It highlights limited evidence, lack of guideline consensus, variable techniques, and the goal of avoiding pacemakers in selected young patients. (francia2024cardioneuroablationtheknown pages 1-2, francia2024cardioneuroablationtheknown pages 2-4)

### 12.5 MAXO term suggestions (examples)
* Permanent cardiac pacing / pacemaker implantation (MAXO suggestion)
* Temporary cardiac pacing (MAXO suggestion)
* Ambulatory electrocardiographic monitoring (MAXO suggestion)
* Exercise stress testing (MAXO suggestion)
* Atropine administration (MAXO suggestion)
* Cardioneuroablation / ganglionated plexus ablation (MAXO suggestion)

---

## 13. Prevention
Primary prevention specific to Mobitz I is not well-defined in the retrieved evidence, but population-level prevention of clinically relevant AV block may be supported by controlling modifiable cardiometabolic risks (blood pressure and glucose), which were associated with incident AV block and accounted for large PAR estimates in a community cohort. (kerola2019riskfactorsassociated pages 1-2)

Secondary prevention includes recognition of physiologic (vagal/athletic) vs pathologic patterns using exercise testing and monitoring to avoid misclassification and unnecessary device therapy. (kusumoto20192018accahahrsguideline pages 49-50, zeppilli2024italiancardiologicalguidelines pages 7-8)

---

## 14. Other species / natural disease
A naturally occurring Wenckebach/paroxysmal AV block phenotype has been reported in a dog (Shiba Inu) with syncope and Holter-documented Wenckebach cycles; atropine response and absence of conduction-system histopathology suggested vagal mediation. The dog had durable clinical benefit from epicardial pacemaker implantation with long-term survival (13 years 3 months post-implant). (morita2025longtermmanagementof pages 1-3, morita2025longtermmanagementof pages 3-4)

---

## 15. Model organisms
No dedicated engineered model organism studies for Mobitz I were retrieved in this run. However, the 2024 conduction-disease review includes animal-model annotations in gene tables (e.g., mouse phenotypes “AVB” for connexin-related genes), indicating that murine genetic models are commonly used to study AV block mechanisms broadly. (li2024cardiacconductiondiseases pages 30-32)

---

## Expert opinions / analysis (authoritative sources)
1. **ACC/AHA/HRS guideline stance:** Mobitz I is typically benign and management is symptom-driven; avoid permanent pacing in asymptomatic nodal/vagal block and when symptoms do not correlate (Class III: Harm). (kusumoto20192018accahahrsguideline pages 45-48, kusumoto20192018accahahrsguideline pages 48-49)
2. **Diagnostic caution (Frontiers 2024):** Misdiagnosis between Wenckebach/vagal AV block and Mobitz II is common; careful attention to sinus slowing and PR behavior, plus prolonged monitoring and EPS in atypical cases, is essential to avoid unnecessary pacemakers. (canoy2024mobitztypeii pages 2-3, canoy2024mobitztypeii pages 5-7)
3. **Sports cardiology perspective (COCIS 2024):** Mobitz I that normalizes with increased heart rate is generally compatible with competitive sport, reinforcing physiologic vagal Wenckebach as a normal variant in trained athletes. (zeppilli2024italiancardiologicalguidelines pages 7-8)

---

## Notes on evidence gaps in this run
* MONDO, MeSH, ICD-10/ICD-11 identifiers were not present in retrieved evidence; they should be added from ontology databases (MONDO, MeSH, ICD).
* Mobitz I–specific prevalence/incidence and large modern cohorts focused exclusively on Wenckebach were not retrieved; most quantitative data available here pertain to AV block broadly. (kerola2019riskfactorsassociated pages 1-2)



References

1. (kusumoto20192018accahahrsguideline pages 48-49): F. Kusumoto, M. Schoenfeld, Coletta Barrett, J. Edgerton, K. Ellenbogen, M. Gold, N. Goldschlager, R. Hamilton, J. Joglar, Robert J. Kim, Richard Lee, J. Marine, Christopher J. McLeod, K. Oken, K. Patton, Cara N. Pellegrini, Kimberly A. Selzman, Annemarie Thompson, and P. Varosy. 2018 acc/aha/hrs guideline on the evaluation and management of patients with bradycardia and cardiac conduction delay: a report of the american college of cardiology/american heart association task force on clinical practice guidelines and the heart rhythm society. Journal of the American College of Cardiology, Aug 2019. URL: https://doi.org/10.1016/j.jacc.2018.10.044, doi:10.1016/j.jacc.2018.10.044. This article has 1695 citations and is from a highest quality peer-reviewed journal.

2. (kusumoto20192018accahahrsguideline pages 49-50): F. Kusumoto, M. Schoenfeld, Coletta Barrett, J. Edgerton, K. Ellenbogen, M. Gold, N. Goldschlager, R. Hamilton, J. Joglar, Robert J. Kim, Richard Lee, J. Marine, Christopher J. McLeod, K. Oken, K. Patton, Cara N. Pellegrini, Kimberly A. Selzman, Annemarie Thompson, and P. Varosy. 2018 acc/aha/hrs guideline on the evaluation and management of patients with bradycardia and cardiac conduction delay: a report of the american college of cardiology/american heart association task force on clinical practice guidelines and the heart rhythm society. Journal of the American College of Cardiology, Aug 2019. URL: https://doi.org/10.1016/j.jacc.2018.10.044, doi:10.1016/j.jacc.2018.10.044. This article has 1695 citations and is from a highest quality peer-reviewed journal.

3. (kusumoto20192018accahahrsguideline pages 45-48): F. Kusumoto, M. Schoenfeld, Coletta Barrett, J. Edgerton, K. Ellenbogen, M. Gold, N. Goldschlager, R. Hamilton, J. Joglar, Robert J. Kim, Richard Lee, J. Marine, Christopher J. McLeod, K. Oken, K. Patton, Cara N. Pellegrini, Kimberly A. Selzman, Annemarie Thompson, and P. Varosy. 2018 acc/aha/hrs guideline on the evaluation and management of patients with bradycardia and cardiac conduction delay: a report of the american college of cardiology/american heart association task force on clinical practice guidelines and the heart rhythm society. Journal of the American College of Cardiology, Aug 2019. URL: https://doi.org/10.1016/j.jacc.2018.10.044, doi:10.1016/j.jacc.2018.10.044. This article has 1695 citations and is from a highest quality peer-reviewed journal.

4. (canoy2024mobitztypeii pages 2-3): D. Canoy, Pasquale Crea, Diego Chemello, S. S. Barold, and B. Herweg. Mobitz type ii second-degree atrioventricular block: a commonly overdiagnosed and misinterpreted arrhythmia. Frontiers in Cardiovascular Medicine, Aug 2024. URL: https://doi.org/10.3389/fcvm.2024.1450705, doi:10.3389/fcvm.2024.1450705. This article has 3 citations and is from a peer-reviewed journal.

5. (canoy2024mobitztypeii pages 3-5): D. Canoy, Pasquale Crea, Diego Chemello, S. S. Barold, and B. Herweg. Mobitz type ii second-degree atrioventricular block: a commonly overdiagnosed and misinterpreted arrhythmia. Frontiers in Cardiovascular Medicine, Aug 2024. URL: https://doi.org/10.3389/fcvm.2024.1450705, doi:10.3389/fcvm.2024.1450705. This article has 3 citations and is from a peer-reviewed journal.

6. (morita2025longtermmanagementof pages 1-3): Shohei MORITA, Shiho TAGUCHI, Takahiro KONDO, Aritada YOSHIMURA, Shiori IKOMA, Takahiro OHMORI, Daiki HIRAO, Noboru MACHIDA, Hisashi HIROSE, and Ryuji FUKUSHIMA. Long-term management of paroxysmal atrioventricular block with wenckebach cycles in a dog. The Journal of Veterinary Medical Science, 87:454-457, Mar 2025. URL: https://doi.org/10.1292/jvms.24-0521, doi:10.1292/jvms.24-0521. This article has 0 citations.

7. (barold2018typeiwenckebach pages 2-3): S. Serge Barold. Type i wenckebach second‐degree av block: a matter of definition. Clinical Cardiology, 41:282-284, Feb 2018. URL: https://doi.org/10.1002/clc.22874, doi:10.1002/clc.22874. This article has 16 citations and is from a peer-reviewed journal.

8. (karaman2026…clinicaldeterioration pages 110-115): K KARAMAN. … clinical deterioration tachyarrhythmias requiring cardioversion and bradycardia syndromes requiring intervention in …. Unknown journal, 2026.

9. (canoy2024mobitztypeii pages 1-2): D. Canoy, Pasquale Crea, Diego Chemello, S. S. Barold, and B. Herweg. Mobitz type ii second-degree atrioventricular block: a commonly overdiagnosed and misinterpreted arrhythmia. Frontiers in Cardiovascular Medicine, Aug 2024. URL: https://doi.org/10.3389/fcvm.2024.1450705, doi:10.3389/fcvm.2024.1450705. This article has 3 citations and is from a peer-reviewed journal.

10. (sfairopoulos2025clinicalsignificanceand pages 1-2): Dimitrios Sfairopoulos, George Bazoukis, Skevos Sideris, Nikolaos Fragakis, Konstantinos Letsas, Konstantinos Zekios, Tong Liu, and Panagiotis Korantzopoulos. Clinical significance and management of atrioventricular block associated with bradycardic/antiarrhythmic drug therapy: drug‐induced or drug‐revealed? Journal of Cardiovascular Electrophysiology, 36:1643-1653, Apr 2025. URL: https://doi.org/10.1111/jce.16697, doi:10.1111/jce.16697. This article has 2 citations and is from a peer-reviewed journal.

11. (ura2024repeatedcompleteatrioventricular pages 1-3): Akihiro Ura, Keisuke Fujii, Tadashi Tanioku, and Tomoyuki Kawamata. Repeated complete atrioventricular block during remifentanil administration in a pediatric patient with brain tumor and acute hydrocephalus: a case report. BMC Anesthesiology, Aug 2024. URL: https://doi.org/10.1186/s12871-024-02593-8, doi:10.1186/s12871-024-02593-8. This article has 1 citations and is from a peer-reviewed journal.

12. (ura2024repeatedcompleteatrioventricular pages 3-5): Akihiro Ura, Keisuke Fujii, Tadashi Tanioku, and Tomoyuki Kawamata. Repeated complete atrioventricular block during remifentanil administration in a pediatric patient with brain tumor and acute hydrocephalus: a case report. BMC Anesthesiology, Aug 2024. URL: https://doi.org/10.1186/s12871-024-02593-8, doi:10.1186/s12871-024-02593-8. This article has 1 citations and is from a peer-reviewed journal.

13. (salim2020mobitztypeii pages 5-6): Stephanie Salim, Sunu Budhi Raharjo, Dony Yugo Hermanto, Dicky Armein Hanafy, Yoga Yuniadi, Stephanie Salim, Sunu Budhi Raharjo, Dony Yugo Hermanto, Dicky Armein Hanafy, and Yoga Yuniadi. Mobitz type ii second-degree atrioventricular block in a pilot : to pace or not to pace? Indonesian Journal of Cardiology, 41:25-31, Aug 2020. URL: https://doi.org/10.30701/ijc.950, doi:10.30701/ijc.950. This article has 1 citations.

14. (rakhmanov2024ecginathletes pages 5-8): Yeltay Rakhmanov, Bauyrzhan Toktarbay, Zaukiya Khamitova, and Alessandro Salustri. Ecg in athletes. Technology in Sports - Recent Advances, New Perspectives and Application [Working Title], Mar 2024. URL: https://doi.org/10.5772/intechopen.1004231, doi:10.5772/intechopen.1004231. This article has 1 citations.

15. (rakhmanov2024ecginathletes pages 16-19): Yeltay Rakhmanov, Bauyrzhan Toktarbay, Zaukiya Khamitova, and Alessandro Salustri. Ecg in athletes. Technology in Sports - Recent Advances, New Perspectives and Application [Working Title], Mar 2024. URL: https://doi.org/10.5772/intechopen.1004231, doi:10.5772/intechopen.1004231. This article has 1 citations.

16. (rakhmanov2024ecginathletes pages 1-5): Yeltay Rakhmanov, Bauyrzhan Toktarbay, Zaukiya Khamitova, and Alessandro Salustri. Ecg in athletes. Technology in Sports - Recent Advances, New Perspectives and Application [Working Title], Mar 2024. URL: https://doi.org/10.5772/intechopen.1004231, doi:10.5772/intechopen.1004231. This article has 1 citations.

17. (kerola2019riskfactorsassociated pages 1-2): Tuomas Kerola, Antti Eranti, Aapo L. Aro, M. Anette Haukilahti, Arttu Holkeri, M. Juhani Junttila, Tuomas V. Kenttä, Harri Rissanen, Eric Vittinghoff, Paul Knekt, Markku Heliövaara, Heikki V. Huikuri, and Gregory M. Marcus. Risk factors associated with atrioventricular block. JAMA Network Open, 2:e194176, May 2019. URL: https://doi.org/10.1001/jamanetworkopen.2019.4176, doi:10.1001/jamanetworkopen.2019.4176. This article has 146 citations and is from a peer-reviewed journal.

18. (kerola2019riskfactorsassociated pages 4-5): Tuomas Kerola, Antti Eranti, Aapo L. Aro, M. Anette Haukilahti, Arttu Holkeri, M. Juhani Junttila, Tuomas V. Kenttä, Harri Rissanen, Eric Vittinghoff, Paul Knekt, Markku Heliövaara, Heikki V. Huikuri, and Gregory M. Marcus. Risk factors associated with atrioventricular block. JAMA Network Open, 2:e194176, May 2019. URL: https://doi.org/10.1001/jamanetworkopen.2019.4176, doi:10.1001/jamanetworkopen.2019.4176. This article has 146 citations and is from a peer-reviewed journal.

19. (kerola2019riskfactorsassociated pages 6-7): Tuomas Kerola, Antti Eranti, Aapo L. Aro, M. Anette Haukilahti, Arttu Holkeri, M. Juhani Junttila, Tuomas V. Kenttä, Harri Rissanen, Eric Vittinghoff, Paul Knekt, Markku Heliövaara, Heikki V. Huikuri, and Gregory M. Marcus. Risk factors associated with atrioventricular block. JAMA Network Open, 2:e194176, May 2019. URL: https://doi.org/10.1001/jamanetworkopen.2019.4176, doi:10.1001/jamanetworkopen.2019.4176. This article has 146 citations and is from a peer-reviewed journal.

20. (sfairopoulos2025clinicalsignificanceand pages 4-4): Dimitrios Sfairopoulos, George Bazoukis, Skevos Sideris, Nikolaos Fragakis, Konstantinos Letsas, Konstantinos Zekios, Tong Liu, and Panagiotis Korantzopoulos. Clinical significance and management of atrioventricular block associated with bradycardic/antiarrhythmic drug therapy: drug‐induced or drug‐revealed? Journal of Cardiovascular Electrophysiology, 36:1643-1653, Apr 2025. URL: https://doi.org/10.1111/jce.16697, doi:10.1111/jce.16697. This article has 2 citations and is from a peer-reviewed journal.

21. (andersen2013riskofarrhythmias pages 4-5): Kasper Andersen, Bahman Farahmand, Anders Ahlbom, Claes Held, Sverker Ljunghall, Karl Michaëlsson, and Johan Sundström. Risk of arrhythmias in 52 755 long-distance cross-country skiers: a cohort study. European heart journal, 34 47:3624-31, Dec 2013. URL: https://doi.org/10.1093/eurheartj/eht188, doi:10.1093/eurheartj/eht188. This article has 538 citations and is from a highest quality peer-reviewed journal.

22. (kerola2019riskfactorsassociated pages 2-4): Tuomas Kerola, Antti Eranti, Aapo L. Aro, M. Anette Haukilahti, Arttu Holkeri, M. Juhani Junttila, Tuomas V. Kenttä, Harri Rissanen, Eric Vittinghoff, Paul Knekt, Markku Heliövaara, Heikki V. Huikuri, and Gregory M. Marcus. Risk factors associated with atrioventricular block. JAMA Network Open, 2:e194176, May 2019. URL: https://doi.org/10.1001/jamanetworkopen.2019.4176, doi:10.1001/jamanetworkopen.2019.4176. This article has 146 citations and is from a peer-reviewed journal.

23. (zeppilli2024italiancardiologicalguidelines pages 7-8): Paolo ZEPPILLI, Alessandro BIFFI, Michela CAMMARANO, Silvia CASTELLETTI, Elena CAVARRETTA, Franco CECCHI, Furio COLIVICCHI, Maurizio CONTURSI, Domenico CORRADO, Antonello D’ANDREA, Francesco DEFERRARI, Pietro DELISE, Antonio DELLO RUSSO, Domenico GABRIELLI, Franco GIADA, Ciro INDOLFI, Viviana MAESTRINI, Giuseppe MASCIA, Lucio MOS, Fabrizio OLIVA, Zefferino PALAMÀ, Stefano PALERMI, Vincenzo PALMIERI, Giampiero PATRIZI, Antonio PELLICCIA, Pasquale PERRONE FILARDI, Italo PORTO, Peter J. SCHWARTZ, Marco SCORCU, Fabrizio SOLLAZZO, Andrea SPAMPINATO, Andrea VERZELETTI, Alessandro ZORZI, Flavio D’ASCENZI, Maurizio CASASCO, and Luigi SCIARRA. Italian cardiological guidelines (cocis) for competitive sport eligibility in athletes with heart disease: update 2024. Minerva medica, 115 5:533-564, Oct 2024. URL: https://doi.org/10.23736/s0026-4806.24.09519-3, doi:10.23736/s0026-4806.24.09519-3. This article has 56 citations and is from a peer-reviewed journal.

24. (zeppilli2024italiancardiologicalguidelines pages 8-10): Paolo ZEPPILLI, Alessandro BIFFI, Michela CAMMARANO, Silvia CASTELLETTI, Elena CAVARRETTA, Franco CECCHI, Furio COLIVICCHI, Maurizio CONTURSI, Domenico CORRADO, Antonello D’ANDREA, Francesco DEFERRARI, Pietro DELISE, Antonio DELLO RUSSO, Domenico GABRIELLI, Franco GIADA, Ciro INDOLFI, Viviana MAESTRINI, Giuseppe MASCIA, Lucio MOS, Fabrizio OLIVA, Zefferino PALAMÀ, Stefano PALERMI, Vincenzo PALMIERI, Giampiero PATRIZI, Antonio PELLICCIA, Pasquale PERRONE FILARDI, Italo PORTO, Peter J. SCHWARTZ, Marco SCORCU, Fabrizio SOLLAZZO, Andrea SPAMPINATO, Andrea VERZELETTI, Alessandro ZORZI, Flavio D’ASCENZI, Maurizio CASASCO, and Luigi SCIARRA. Italian cardiological guidelines (cocis) for competitive sport eligibility in athletes with heart disease: update 2024. Minerva medica, 115 5:533-564, Oct 2024. URL: https://doi.org/10.23736/s0026-4806.24.09519-3, doi:10.23736/s0026-4806.24.09519-3. This article has 56 citations and is from a peer-reviewed journal.

25. (li2024cardiacconductiondiseases pages 9-11): Tingting Li, Qussay Marashly, Jitae A. Kim, Na Li, and Mihail G. Chelu. Cardiac conduction diseases: understanding the molecular mechanisms to uncover targets for future treatments. Expert Opinion on Therapeutic Targets, 28:385-400, May 2024. URL: https://doi.org/10.1080/14728222.2024.2351501, doi:10.1080/14728222.2024.2351501. This article has 5 citations and is from a peer-reviewed journal.

26. (li2024cardiacconductiondiseases pages 23-28): Tingting Li, Qussay Marashly, Jitae A. Kim, Na Li, and Mihail G. Chelu. Cardiac conduction diseases: understanding the molecular mechanisms to uncover targets for future treatments. Expert Opinion on Therapeutic Targets, 28:385-400, May 2024. URL: https://doi.org/10.1080/14728222.2024.2351501, doi:10.1080/14728222.2024.2351501. This article has 5 citations and is from a peer-reviewed journal.

27. (li2024cardiacconductiondiseases pages 8-9): Tingting Li, Qussay Marashly, Jitae A. Kim, Na Li, and Mihail G. Chelu. Cardiac conduction diseases: understanding the molecular mechanisms to uncover targets for future treatments. Expert Opinion on Therapeutic Targets, 28:385-400, May 2024. URL: https://doi.org/10.1080/14728222.2024.2351501, doi:10.1080/14728222.2024.2351501. This article has 5 citations and is from a peer-reviewed journal.

28. (li2024cardiacconductiondiseases pages 19-20): Tingting Li, Qussay Marashly, Jitae A. Kim, Na Li, and Mihail G. Chelu. Cardiac conduction diseases: understanding the molecular mechanisms to uncover targets for future treatments. Expert Opinion on Therapeutic Targets, 28:385-400, May 2024. URL: https://doi.org/10.1080/14728222.2024.2351501, doi:10.1080/14728222.2024.2351501. This article has 5 citations and is from a peer-reviewed journal.

29. (li2024cardiacconductiondiseases pages 30-32): Tingting Li, Qussay Marashly, Jitae A. Kim, Na Li, and Mihail G. Chelu. Cardiac conduction diseases: understanding the molecular mechanisms to uncover targets for future treatments. Expert Opinion on Therapeutic Targets, 28:385-400, May 2024. URL: https://doi.org/10.1080/14728222.2024.2351501, doi:10.1080/14728222.2024.2351501. This article has 5 citations and is from a peer-reviewed journal.

30. (canoy2024mobitztypeii pages 5-7): D. Canoy, Pasquale Crea, Diego Chemello, S. S. Barold, and B. Herweg. Mobitz type ii second-degree atrioventricular block: a commonly overdiagnosed and misinterpreted arrhythmia. Frontiers in Cardiovascular Medicine, Aug 2024. URL: https://doi.org/10.3389/fcvm.2024.1450705, doi:10.3389/fcvm.2024.1450705. This article has 3 citations and is from a peer-reviewed journal.

31. (francia2024cardioneuroablationtheknown pages 1-2): Pietro Francia, J. P. D. Waroux, A. Marrese, R. Persico, E. Parlato, D. Faccenda, A. Salucci, G. Comparone, V. Pergola, G. Ammirati, L. Addeo, C. Fonderico, L. Cocchiara, A. Volpe, P. Visconti, A. Rapacciuolo, and T. Strisciuglio. Cardioneuroablation: the known and the unknown. Frontiers in Cardiovascular Medicine, Jul 2024. URL: https://doi.org/10.3389/fcvm.2024.1412195, doi:10.3389/fcvm.2024.1412195. This article has 4 citations and is from a peer-reviewed journal.

32. (francia2024cardioneuroablationtheknown pages 2-4): Pietro Francia, J. P. D. Waroux, A. Marrese, R. Persico, E. Parlato, D. Faccenda, A. Salucci, G. Comparone, V. Pergola, G. Ammirati, L. Addeo, C. Fonderico, L. Cocchiara, A. Volpe, P. Visconti, A. Rapacciuolo, and T. Strisciuglio. Cardioneuroablation: the known and the unknown. Frontiers in Cardiovascular Medicine, Jul 2024. URL: https://doi.org/10.3389/fcvm.2024.1412195, doi:10.3389/fcvm.2024.1412195. This article has 4 citations and is from a peer-reviewed journal.

33. (morita2025longtermmanagementof pages 3-4): Shohei MORITA, Shiho TAGUCHI, Takahiro KONDO, Aritada YOSHIMURA, Shiori IKOMA, Takahiro OHMORI, Daiki HIRAO, Noboru MACHIDA, Hisashi HIROSE, and Ryuji FUKUSHIMA. Long-term management of paroxysmal atrioventricular block with wenckebach cycles in a dog. The Journal of Veterinary Medical Science, 87:454-457, Mar 2025. URL: https://doi.org/10.1292/jvms.24-0521, doi:10.1292/jvms.24-0521. This article has 0 citations.
