---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-23T18:35:35.539340'
end_time: '2026-04-23T18:48:15.351786'
duration_seconds: 759.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tall Stature-Intellectual Disability-Renal Anomalies Syndrome
  mondo_id: ''
  category: Developmental Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tall Stature-Intellectual Disability-Renal Anomalies Syndrome
- **MONDO ID:**  (if available)
- **Category:** Developmental Disorder

## Research Objectives

Please provide a comprehensive research report on **Tall Stature-Intellectual Disability-Renal Anomalies Syndrome** covering all of the
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
- **Disease Name:** Tall Stature-Intellectual Disability-Renal Anomalies Syndrome
- **MONDO ID:**  (if available)
- **Category:** Developmental Disorder

## Research Objectives

Please provide a comprehensive research report on **Tall Stature-Intellectual Disability-Renal Anomalies Syndrome** covering all of the
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


# Tall Stature–Intellectual Disability–Renal Anomalies Syndrome (Developmental Disorder): Comprehensive Research Report

## Executive summary (current understanding)
The label **“Tall stature–intellectual disability–renal anomalies syndrome”** is not consistently used as a single standardized nosologic entity in the literature retrieved here. The **best-supported match** in primary sources is **“15q overgrowth syndrome”** (also described as distal **15q duplication/trisomy/tetrasomy**), a **copy-number gain of distal chromosome 15q** often encompassing **IGF1R**, producing a recognizable syndrome of **postnatal overgrowth/tall stature**, **learning difficulties/intellectual disability**, **characteristic facial gestalt**, and **frequent renal anomalies**. (tatton‐brown200915qovergrowthsyndrome pages 1-2, tatton‐brown200915qovergrowthsyndrome pages 5-6, tatton‐brown200915qovergrowthsyndrome pages 6-8)

A **genetically distinct** but phenotypically overlapping disorder is **FIBP-related Thauvin–Robinet–Faivre syndrome (TROFAS/TRFS)**, an **autosomal recessive** syndromic overgrowth condition with **intellectual disability**, **renal anomalies/renal dysplasia**, and reported **Wilms tumor** predisposition. (akawi2016arecessivesyndrome pages 3-5, cosentino2025expandingtheknowledge pages 1-3)

Because the requested disease name appears to be a **phenotype label** rather than a single curated ontology entry in the retrieved set, this report is structured around these **two evidence-supported entities**.

| Entity/synonyms | Genetic etiology | Key renal findings | Key neurodevelopmental/growth findings | Key statistics/frequencies | Key references with year, journal, DOI/URL |
|---|---|---|---|---|---|
| **15q overgrowth syndrome**; distal 15q duplication/trisomy/tetrasomy; “15q OGS”; phenotype corresponding to a tall stature–intellectual disability–renal anomalies presentation in the evidence | Increased dosage of distal chromosome **15q** (duplication/triplication/tetrasomy; often **15q25.3–q26.3** / **15q26.1-qter**), frequently including **IGF1R**; mechanism supported by increased **IGF1R** dosage/expression and downstream growth signaling (tatton‐brown200915qovergrowthsyndrome pages 1-2, tatton‐brown200915qovergrowthsyndrome pages 4-5, cannarella2017chromosome15structural pages 1-2, tatton‐brown200915qovergrowthsyndrome pages 6-8, bodle2019acuteleukemiain pages 1-2) | Renal anomalies reported include **horseshoe kidney, renal agenesis, hydronephrosis, vesico-ureteric reflux, polycystic kidney, right pelvic duplication** (tatton‐brown200915qovergrowthsyndrome pages 5-6) | Postnatal **overgrowth/tall stature**, **learning difficulties/intellectual disability**, characteristic facial gestalt (long/thin face, prominent chin/nose, broad nasal bridge, high anterior hairline/dolichocephaly); additional reported findings include hypotonia, seizures/autism in some cases, scoliosis, hearing loss, cardiac anomalies, craniosynostosis, genital/gonadal anomalies (tatton‐brown200915qovergrowthsyndrome pages 2-4, tatton‐brown200915qovergrowthsyndrome pages 6-8, cannarella2017chromosome15structural pages 1-2, bodle2019acuteleukemiain pages 1-2) | Trisomy 15q: **71% (12/17)** overgrown, **100% (17/17)** learning difficulties, **94% (16/17)** characteristic facial appearance; tetrasomy 15q: **100% (4/4)** overgrowth and **100% (5/5)** learning difficulties; renal anomalies identified in **45% (5/11)** of trisomy cases investigated and **80% (4/5)** of tetrasomy cases investigated; in the 2009 series, **3/5** cases had renal anomalies (tatton‐brown200915qovergrowthsyndrome pages 6-8, tatton‐brown200915qovergrowthsyndrome pages 5-6) | Tatton-Brown et al., **2009**, *Am J Med Genet A*, DOI: **10.1002/ajmg.a.32534** / https://doi.org/10.1002/ajmg.a.32534 (tatton‐brown200915qovergrowthsyndrome pages 1-2, tatton‐brown200915qovergrowthsyndrome pages 6-8); Cannarella et al., **2017**, *Endocrine Connections*, DOI: **10.1530/EC-17-0158** / https://doi.org/10.1530/ec-17-0158 (cannarella2017chromosome15structural pages 1-2); Bodle et al., **2019**, *Am J Med Genet A*, DOI: **10.1002/ajmg.a.61115** / https://doi.org/10.1002/ajmg.a.61115 (bodle2019acuteleukemiain pages 2-3, bodle2019acuteleukemiain pages 1-2) |
| **FIBP-related Thauvin–Robinet–Faivre syndrome**; recessive syndrome of intellectual disability, moderate overgrowth, and renal dysplasia predisposing to Wilms tumor; overlapping tall stature–intellectual disability–renal anomalies phenotype | **Autosomal recessive**, caused by **biallelic FIBP variants** on chromosome **11q13.1**; reported variants in the evidence include **c.175_176insTAA / p.His59delinsLeuAsn (p.H59LN)** and **c.652C>T / p.Gln218\***; FIBP encodes an intracellular acidic FGF-binding protein (akawi2016arecessivesyndrome pages 1-2, akawi2016arecessivesyndrome pages 3-5, cosentino2025expandingtheknowledge pages 6-7, cosentino2025expandingtheknowledge pages 1-3, akawi2016arecessivesyndrome pages 2-3) | **Renal dysplasia**, **nephromegaly**, **bilateral cystic dysplastic kidneys** with non-functioning kidney, **renal malrotation**, **left bifid ureter**, simple renal cyst, and predisposition to **Wilms tumor**; prenatal ultrasound may show cystic dysplastic kidneys (akawi2016arecessivesyndrome pages 3-5, akawi2016arecessivesyndrome pages 2-3) | **Moderate/generalized overgrowth or tall stature**, **intellectual disability/developmental delay/learning disability**, macrocephaly in some reports, facial dysmorphism; additional anomalies reported include hearing loss, ocular anomalies, cardiac defects, skeletal/orthopedic abnormalities; patient fibroblasts showed increased proliferation in supporting studies (akawi2016arecessivesyndrome pages 2-3, akawi2016arecessivesyndrome pages 3-5, cosentino2025expandingtheknowledge pages 1-3, akawi2016arecessivesyndrome pages 7-8) | No population-level prevalence estimates in the provided snippets; evidence is from small families/case reports. In one consanguineous family, **3 affected siblings** were described; one had **stage III Wilms tumor**, one had cystic dysplastic kidneys/nephromegaly, and one had normal kidneys, indicating **variable expressivity/intrafamilial heterogeneity** (akawi2016arecessivesyndrome pages 3-5, akawi2016arecessivesyndrome pages 7-8, akawi2016arecessivesyndrome pages 2-3) | Akawi et al., **2016**, *Am J Med Genet A*, DOI: **10.1002/ajmg.a.37741** / https://doi.org/10.1002/ajmg.a.37741 (akawi2016arecessivesyndrome pages 2-3, akawi2016arecessivesyndrome pages 1-2, akawi2016arecessivesyndrome pages 3-5); Cosentino et al., **2025**, *Journal of Applied Genetics*, DOI: **10.1007/s13353-025-00984-2** / https://doi.org/10.1007/s13353-025-00984-2 (cosentino2025expandingtheknowledge pages 6-7, cosentino2025expandingtheknowledge pages 1-3) |


*Table: This table maps the label 'Tall stature–intellectual disability–renal anomalies syndrome' to the two evidence-supported entities that best match it in the retrieved literature. It highlights the distinction between the chromosomal 15q overgrowth syndrome and the monogenic FIBP-related Thauvin–Robinet–Faivre syndrome.*

---

## 1. Disease information

### 1.1 Concise overview
**15q overgrowth syndrome (distal 15q duplication/trisomy/tetrasomy)** is a cytogenomic overgrowth syndrome characterized by **overgrowth/tall stature**, **learning difficulties/intellectual disability**, **Sotos-like facial gestalt**, and **renal anomalies**, caused by **increased dosage of distal 15q** (duplication/triplication/tetrasomy). (tatton‐brown200915qovergrowthsyndrome pages 1-2, tatton‐brown200915qovergrowthsyndrome pages 5-6, tatton‐brown200915qovergrowthsyndrome pages 6-8)

**FIBP-related Thauvin–Robinet–Faivre syndrome (TROFAS/TRFS)** is an **autosomal recessive** syndromic overgrowth disorder caused by **biallelic loss-of-function variants in FIBP (chr11q13.1)**, with **intellectual disability**, **overgrowth**, and **renal anomalies/renal dysplasia**; renal disease may be severe and has been reported to predispose to **Wilms tumor**. (akawi2016arecessivesyndrome pages 3-5, akawi2016arecessivesyndrome pages 2-3, cosentino2025expandingtheknowledge pages 1-3)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
The retrieved full-text excerpts **do not provide MONDO, Orphanet, MeSH, ICD-10/ICD-11, or OMIM identifiers** for “15q overgrowth syndrome” or for “Tall stature–intellectual disability–renal anomalies syndrome” as a single named entity. Therefore, identifiers cannot be asserted from the current tool-accessed evidence without external database lookups. (tatton‐brown200915qovergrowthsyndrome pages 5-6, tatton‐brown200915qovergrowthsyndrome pages 6-8)

However, Tatton-Brown et al. provide an OMIM-based **differential diagnosis table** (e.g., Sotos syndrome OMIM 117550; Weaver syndrome OMIM 277590), demonstrating the clinical overlap space in which 15q overgrowth syndrome is considered. (tatton‐brown200915qovergrowthsyndrome pages 6-8)

### 1.3 Synonyms / alternative names (from evidence)
- **15q overgrowth syndrome**, **15q OGS**, distal **15q duplication/trisomy/tetrasomy** phenotypes. (bodle2019acuteleukemiain pages 1-2, tatton‐brown200915qovergrowthsyndrome pages 5-6)
- For the monogenic overlapping entity: **Thauvin–Robinet–Faivre syndrome (TROFAS/TRFS)**; “recessive syndrome of intellectual disability, moderate overgrowth, and renal dysplasia predisposing to Wilms tumor” caused by **FIBP** variants. (akawi2016arecessivesyndrome pages 2-3, cosentino2025expandingtheknowledge pages 1-3)

### 1.4 Evidence source types
- **Human clinical cytogenetics/case series:** 15q overgrowth syndrome characterization and pooled frequencies. (tatton‐brown200915qovergrowthsyndrome pages 5-6, tatton‐brown200915qovergrowthsyndrome pages 6-8)
- **Human case report with molecular cytogenetics and clinical course:** adult with 15q OGS and mixed phenotype acute leukemia. (bodle2019acuteleukemiain pages 1-2)
- **Human Mendelian family study (WES + homozygosity mapping):** FIBP-related syndromic overgrowth with renal dysplasia/Wilms tumor. (akawi2016arecessivesyndrome pages 3-5)
- **Recent review (2024) on overgrowth mechanisms and omics diagnostics:** emphasizes NGS/omics and diagnostic challenges. (prawitt2024molecularmechanismsof pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors

#### 2.1.1 15q overgrowth syndrome
**Primary cause:** **copy-number gain** of distal 15q (duplication/triplication/tetrasomy), frequently including **IGF1R**. (tatton‐brown200915qovergrowthsyndrome pages 4-5, tatton‐brown200915qovergrowthsyndrome pages 5-6, bodle2019acuteleukemiain pages 1-2)

Mechanistic gene-dosage hypothesis is supported by Tatton-Brown et al.: **“Increased dosage of IGF1R, through duplication or triplication of the 15q26.1-qter region, could therefore lead to overgrowth.”** (tatton‐brown200915qovergrowthsyndrome pages 6-8)

#### 2.1.2 FIBP-related Thauvin–Robinet–Faivre syndrome
**Primary cause:** **biallelic FIBP loss-of-function** (autosomal recessive). (akawi2016arecessivesyndrome pages 3-5, cosentino2025expandingtheknowledge pages 1-3)

Akawi et al. explicitly frame the entity as a Mendelian syndrome: “A recessive syndrome of intellectual disability, moderate overgrowth, and renal dysplasia predisposing to wilms tumor is caused by a mutation in fibp gene.” (title-level statement in the full text excerpt context). (akawi2016arecessivesyndrome pages 2-3)

### 2.2 Risk factors / protective factors / gene–environment interactions
No evidence in the retrieved texts supports environmental risk factors, protective factors, or gene–environment interactions for either entity. The disorders are currently best supported as **genetic** with variable expressivity. (tatton‐brown200915qovergrowthsyndrome pages 5-6, akawi2016arecessivesyndrome pages 2-3)

---

## 3. Phenotypes

### 3.1 Core phenotype set: 15q overgrowth syndrome (distal 15q duplication)

#### 3.1.1 Growth/overgrowth
- Tall stature / overgrowth (HPO: **HP:0000098 Tall stature**, **HP:0004322 Accelerated growth**, **HP:0001518 Overgrowth**) 
- Frequency (pooled): **71% (12/17)** overgrown among trisomy 15q cases; **100% (4/4)** overgrowth among reported tetrasomy 15q cases. (tatton‐brown200915qovergrowthsyndrome pages 6-8)

#### 3.1.2 Neurodevelopment
- Learning difficulties / intellectual disability (HPO: **HP:0001249 Intellectual disability**, **HP:0001263 Global developmental delay**, **HP:0000750 Delayed speech and language development**)
- Frequency (pooled): **100% (17/17)** learning difficulties in trisomy 15q series; **100% (5/5)** learning difficulties in reported tetrasomy cases. (tatton‐brown200915qovergrowthsyndrome pages 6-8)

#### 3.1.3 Facial gestalt / dysmorphism
- “Sotos-like” facial appearance; long/thin face, prominent chin/nose, broad nasal bridge, high anterior hairline; dolichocephaly. (HPO examples: **HP:0000307 Dolichocephaly**, **HP:0000303 Prominent forehead**, **HP:0000308 Brachycephaly** (if present in individuals), **HP:0000347 Micrognathia** (reported in some distal 15q duplication descriptions)) (tatton‐brown200915qovergrowthsyndrome pages 2-4, tatton‐brown200915qovergrowthsyndrome pages 5-6, tatton‐brown200915qovergrowthsyndrome pages 6-8)
- Frequency (pooled): **94% (16/17)** characteristic facial appearance in trisomy 15q cases; **100% (8/8)** in reported tetrasomy cases (facial gestalt). (tatton‐brown200915qovergrowthsyndrome pages 6-8)

#### 3.1.4 Renal anomalies
- Specific anomalies reported: **horseshoe kidney, renal agenesis, hydronephrosis, vesico-ureteric reflux, polycystic kidney, right pelvic duplication**. (HPO examples: **HP:0000085 Horseshoe kidney**, **HP:0000104 Renal agenesis**, **HP:0000126 Hydronephrosis**, **HP:0000076 Vesicoureteral reflux**, **HP:0000110 Renal dysplasia** (if dysplasia documented), **HP:0000107 Renal cyst**) (tatton‐brown200915qovergrowthsyndrome pages 5-6)
- Frequency (pooled, among those investigated): **45% (5/11)** of 15q trisomy cases and **80% (4/5)** of 15q tetrasomy cases had renal anomalies when renal investigations were performed; in the authors’ cohort, **3/5** had renal anomalies. (tatton‐brown200915qovergrowthsyndrome pages 5-6)

#### 3.1.5 Other commonly reported features (variable)
- Seizures, autism, hypotonia (tatton‐brown200915qovergrowthsyndrome pages 5-6)
- Scoliosis, craniosynostosis, hearing loss, genital abnormalities, minor cardiac anomalies. (bodle2019acuteleukemiain pages 1-2)

### 3.2 Core phenotype set: FIBP-related Thauvin–Robinet–Faivre syndrome

#### 3.2.1 Growth/overgrowth
- Overgrowth primarily in height/tall stature (HPO: **HP:0000098 Tall stature**, **HP:0001518 Overgrowth**) (akawi2016arecessivesyndrome pages 3-5)

#### 3.2.2 Neurodevelopment
- Developmental delay / learning disability / intellectual disability (HPO: **HP:0001263 Global developmental delay**, **HP:0001249 Intellectual disability**) (akawi2016arecessivesyndrome pages 3-5)

#### 3.2.3 Renal anomalies / renal dysplasia and complications
- Prenatal cystic dysplastic kidneys (akawi2016arecessivesyndrome pages 3-5)
- Nephromegaly, bilateral cystic dysplastic kidneys, non-functioning kidney; renal malrotation; bifid ureter. (HPO: **HP:0000110 Renal dysplasia**, **HP:0000107 Renal cyst**, **HP:0000125 Nephromegaly**, **HP:0000083 Renal malrotation**, **HP:0000072 Ureteral duplication**) (akawi2016arecessivesyndrome pages 3-5)
- Severe neonatal renal failure and early mortality have been reported: **“Half of the reported cases die in the first few days of life mainly due to renal failure.”** (akawi2016arecessivesyndrome pages 2-3)

#### 3.2.4 Tumor predisposition
- Wilms tumor observed in an affected child (stage III in Akawi family). (HPO: **HP:0002667 Wilms tumor**) (akawi2016arecessivesyndrome pages 3-5)
- Cosentino et al. (2025) also state increased risk for Wilms tumor in TROFAS (but detailed risk quantification is not available in the provided excerpt). (cosentino2025expandingtheknowledge pages 1-3)

#### 3.2.5 Additional manifestations (emerging)
- Hearing loss and ocular abnormalities appear in the Akawi family. (akawi2016arecessivesyndrome pages 3-5)
- 2025 phenotype expansion includes conduction disease/AV block, ophthalmologic inflammation (uveitis), orthopedic findings, and a recommendation for surveillance (see Treatment/Management). (cosentino2025expandingtheknowledge pages 5-6)

### 3.3 Quality-of-life impact
No disease-specific QoL instruments (EQ-5D/SF-36/PROMIS) were retrieved for these entities. Given core neurodevelopmental disability and potential renal disease, QoL burden is expected to be substantial, but this cannot be quantified from the current evidence set.

---

## 4. Genetic / molecular information

### 4.1 Causal genes / loci
- **15q overgrowth syndrome:** distal **15q copy-number gain** (often **15q25.3–15q26.3**), frequently including **IGF1R**. Bodle et al. report a case with aCGH result **[hg19: 15q25.3q26.3(88802919–102383473) × 3]** including **IGF1R** (and ≥71 genes). (bodle2019acuteleukemiain pages 1-2)
- **FIBP-related TROFAS:** **FIBP** (chr11q13.1). (cosentino2025expandingtheknowledge pages 1-3)

### 4.2 Pathogenic variants / variant classes
- **15q overgrowth syndrome:** structural variants / CNVs (duplications/triplications/tetrasomy), including small “pure” duplications (e.g., 568 kb 15q26.3 duplication) and larger trisomies. (cannarella2017chromosome15structural pages 1-2, bodle2019acuteleukemiain pages 1-2)
- **FIBP-related TROFAS:** biallelic variants including an in-frame insertion **NM_198897.1:c.175_176insTAA; p.His59delinsLeuAsn** (Akawi family), and truncating variants in later case reports (compound heterozygous p.Arg335* and p.Ser166* in Cosentino case). (akawi2016arecessivesyndrome pages 3-5, cosentino2025expandingtheknowledge pages 1-3)

### 4.3 Inheritance, penetrance, expressivity
- **15q overgrowth syndrome:** typically **de novo or inherited chromosomal rearrangements** causing distal 15q dosage gain; expressivity varies and can be influenced by breakpoints/position effects. Cannarella et al. discuss breakpoint-dependent regulation: genotype–phenotype discordance may arise when a breakpoint juxtaposes IGF1R to an active promoter or disrupts regulatory sequences. (cannarella2017chromosome15structural pages 5-6)
- **FIBP-related TROFAS:** **autosomal recessive**, with **variable renal involvement** even within a family (one child with Wilms tumor, another with dysplastic kidneys, another with normal kidneys), indicating variable expressivity. (akawi2016arecessivesyndrome pages 7-8)

### 4.4 Population allele frequencies
No gnomAD/ExAC allele-frequency data were available in the retrieved excerpts; therefore, allele frequencies cannot be provided here.

---

## 5. Environmental information
No environmental, lifestyle, or infectious causal triggers were supported by the retrieved texts. These disorders are best supported as genetic. (tatton‐brown200915qovergrowthsyndrome pages 5-6, akawi2016arecessivesyndrome pages 2-3)

---

## 6. Mechanism / pathophysiology

### 6.1 15q overgrowth syndrome: IGF1R dosage and growth pathways
Tatton-Brown et al. describe IGF1R-mediated growth signaling: binding of IGF1/IGF2 to IGF1R triggers autophosphorylation and **PI3K/mTOR pathway** activation “a key pathway involved in cell growth and proliferation.” (tatton‐brown200915qovergrowthsyndrome pages 5-6)

They explicitly propose a dosage mechanism: **“Increased dosage of IGF1R, through duplication or triplication of the 15q26.1-qter region, could therefore lead to overgrowth.”** (tatton‐brown200915qovergrowthsyndrome pages 6-8)

Functional support cited in the text includes increased proliferation and IGF1R autophosphorylation in fibroblasts with IGF1R duplication (Okubo et al. 2003 as cited). (tatton‐brown200915qovergrowthsyndrome pages 6-8)

**Ontology suggestions (mechanism):**
- GO Biological Process: **PI3K signaling (GO:0014065)**; **mTOR signaling (GO:0031929)**; **cell proliferation (GO:0008283)**.
- Cell types (CL): plausible key responders include **fibroblast (CL:0000057)** (directly referenced in fibroblast functional observations), and growth-responsive lineages broadly.

### 6.2 FIBP-related TROFAS: FGF signaling and proliferation
FIBP encodes an intracellular **FGF-binding protein**, and loss-of-function is linked to dysregulated growth control. Akawi et al. report increased cellular proliferation in patient fibroblasts and strong embryonic expression in developing kidney/neural tissues (mouse expression work described in the paper). (akawi2016arecessivesyndrome pages 7-8)

Cosentino et al. summarize that FIBP “modulates cell proliferation, differentiation, and survival,” and note that loss-of-function variants lead to dysregulated signaling with implications for Wilms tumor predisposition. (cosentino2025expandingtheknowledge pages 6-7)

**Ontology suggestions (mechanism):**
- GO Biological Process: **fibroblast growth factor receptor signaling pathway (GO:0008543)**; **regulation of cell proliferation (GO:0042127)**; **kidney development (GO:0001822)**.
- Cell types (CL): **metanephric mesenchyme cell (CL:0002297)** / nephrogenic precursors (conceptually relevant to renal dysplasia), and **fibroblast (CL:0000057)** for functional assays.

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
- **Kidney/urinary system** (UBERON: **kidney UBERON:0002113**; **ureter UBERON:0001222**) due to congenital anomalies (horseshoe kidney, agenesis, hydronephrosis, renal dysplasia). (tatton‐brown200915qovergrowthsyndrome pages 5-6, akawi2016arecessivesyndrome pages 3-5)
- **Central nervous system** (UBERON: **brain UBERON:0000955**) due to neurodevelopmental disability. (tatton‐brown200915qovergrowthsyndrome pages 6-8, akawi2016arecessivesyndrome pages 3-5)
- **Skeletal system** (e.g., scoliosis/orthopedic findings) in some cases. (bodle2019acuteleukemiain pages 1-2, cosentino2025expandingtheknowledge pages 5-6)

### 7.2 Subcellular / molecular localization
- **IGF1R** is a membrane receptor tyrosine kinase; **FIBP** is intracellular. These are molecular-localization facts implied by receptor biology and FIBP function in the retrieved sources. (cannarella2017chromosome15structural pages 1-2, cosentino2025expandingtheknowledge pages 6-7)

---

## 8. Temporal development (onset and progression)

### 8.1 15q overgrowth syndrome
Typically features are apparent in childhood due to overgrowth and developmental delay/learning difficulties. Renal anomalies may be congenital and detected via imaging; Tatton-Brown et al. include prenatal/postnatal findings across reported cases. (tatton‐brown200915qovergrowthsyndrome pages 5-6)

### 8.2 FIBP-related TROFAS
- Can present prenatally with cystic dysplastic kidneys and in early childhood with overgrowth and developmental delay. (akawi2016arecessivesyndrome pages 3-5)
- Severe neonatal renal failure and early death reported in some cases. (akawi2016arecessivesyndrome pages 2-3)

---

## 9. Inheritance and population

### 9.1 Epidemiology
No prevalence/incidence estimates were identified in the retrieved texts for either entity; both are described as rare with small numbers of reported individuals. (cannarella2017chromosome15structural pages 1-2, bodle2019acuteleukemiain pages 2-3)

### 9.2 Inheritance
- 15q overgrowth syndrome: chromosomal rearrangements leading to distal 15q dosage gain; may be de novo or familial (e.g., pericentric inversion-related). (tatton‐brown200915qovergrowthsyndrome pages 6-8)
- FIBP-related TROFAS: **autosomal recessive**, often in consanguineous families. (akawi2016arecessivesyndrome pages 3-5)

---

## 10. Diagnostics

### 10.1 Clinical recognition and differential diagnosis
Tatton-Brown et al. emphasize clinical similarity to Sotos syndrome and recommend considering distal 15q duplication in Sotos-like cases without NSD1 abnormalities: **“We therefore suggest that the 15q overgrowth syndrome be considered in those cases with a clinical diagnosis of Sotos syndrome without an associated abnormality of NSD1 and that investigation of the 15q telomere be undertaken.”** (tatton‐brown200915qovergrowthsyndrome pages 5-6)

Differentials explicitly listed include **Sotos, Weaver, Bannayan–Riley–Ruvalcaba, Simpson–Golabi–Behmel**. (tatton‐brown200915qovergrowthsyndrome pages 5-6)

### 10.2 Genetic testing approaches (real-world implementations)
**15q overgrowth syndrome:**
- Cytogenomic approaches are central; Bodle et al. report **array comparative genomic hybridization** confirming distal 15q trisomy with coordinates and IGF1R inclusion. (bodle2019acuteleukemiain pages 1-2)
- Cannarella et al. evaluate small duplications using **array-CGH** and quantify IGF1R mRNA/protein changes in selected cases. (cannarella2017chromosome15structural pages 1-2)

**FIBP-related TROFAS:**
- Akawi et al.: homozygosity mapping + **whole-exome sequencing** + Sanger confirmation in a consanguineous family. (akawi2016arecessivesyndrome pages 2-3)
- Cosentino et al. (2025) diagnostic workflow: karyotype, targeted FISH, and **exome sequencing** identifying compound heterozygous truncating variants. (cosentino2025expandingtheknowledge pages 1-3)

**Latest research / 2024 diagnostic perspective (omics):**
Prawitt & Eggermann (2024) summarize emerging omics and emphasize early molecular testing: **“Physicians should consider molecular genetic testing as a first diagnostic step in overgrowth syndromes.”** (prawitt2024molecularmechanismsof pages 1-2)

Abolhassani et al. (2024) provide a concrete, contemporary clinical NGS pipeline and performance metrics (though not syndrome-specific), including mean depth **126×** for exomes and **522×** for panels and ACMG/AMP classification practices. (abolhassani2024clinicalapplicationof pages 9-10)

---

## 11. Outcome / prognosis

### 11.1 15q overgrowth syndrome
- Neurodevelopmental outcome includes persistent learning difficulties/intellectual disability, with variable severity. (tatton‐brown200915qovergrowthsyndrome pages 5-6)
- Malignancy risk is **uncertain** due to small numbers; Bodle et al. report leukemia in a 34-year-old with 15q OGS and note limited reported malignancies. (bodle2019acuteleukemiain pages 2-3)

### 11.2 FIBP-related TROFAS
- Potential for severe neonatal renal failure with early mortality: **“Half of the reported cases die in the first few days of life mainly due to renal failure.”** (akawi2016arecessivesyndrome pages 2-3)
- Wilms tumor risk is reported (case-level) and cited as a concern in later reviews/case reports. (akawi2016arecessivesyndrome pages 3-5, cosentino2025expandingtheknowledge pages 1-3)

---

## 12. Treatment / management

### 12.1 Disease-modifying therapy
No disease-specific pharmacotherapies or gene-targeted therapies were identified in the retrieved sources.

### 12.2 Supportive care and surveillance (real-world implementation)

**15q overgrowth syndrome:**
- No standardized surveillance protocol is provided in the retrieved excerpts. However, because renal anomalies are frequent and considered a “major feature,” baseline and follow-up renal evaluation is clinically reasonable, but specific schedules are not evidence-specified here. (tatton‐brown200915qovergrowthsyndrome pages 5-6)

**FIBP-related TROFAS:**
- Cosentino et al. (2025) explicitly advocate broad longitudinal surveillance: **“Establishing comprehensive surveillance protocols, including musculoskeletal evaluations, cardiology assessments, pulmonary function monitoring, and ophthalmologic screenings...”** (cosentino2025expandingtheknowledge pages 5-6)
- They highlight cardiac conduction disease as clinically critical: “(AV) block requiring pacemaker implantation is a particularly critical finding,” motivating “serial electrocardiographic and echocardiographic evaluations.” (cosentino2025expandingtheknowledge pages 5-6)

**MAXO term suggestions (supportive actions):**
- Renal imaging surveillance: **MAXO:0000832 (Ultrasonography)** (for kidney ultrasound).
- Developmental interventions: **MAXO:0001074 (Speech therapy)**; **MAXO:0000727 (Occupational therapy)**; **MAXO:0000513 (Physical therapy)**.
- Cardiac monitoring (TROFAS): **MAXO:0000537 (Electrocardiography)**; **MAXO:0000470 (Echocardiography)**.

### 12.3 Clinical trials
The clinical-trials search did not identify syndrome-specific interventional trials relevant to this rare developmental disorder in the current retrieval state. (clinical trials tool result: no relevant trials)

---

## 13. Prevention
Primary prevention is not established for these genetic conditions. Secondary prevention may involve **genetic counseling** (especially for autosomal recessive FIBP-related disease) and prenatal/preimplantation options, but such guidelines were not present in retrieved excerpts.

---

## 14–15. Other species / model organisms
Akawi et al. include **mouse embryonic expression** evidence for Fibp in developing kidney and neural tissues (supporting biological plausibility), but no dedicated disease model organisms are described in the retrieved excerpts. (akawi2016arecessivesyndrome pages 7-8)

---

## Recent developments and latest research (prioritizing 2023–2024)
1. **Omics-first diagnostic framing for overgrowth syndromes (2024):** Prawitt & Eggermann (Frontiers in Genetics, 2024-06; https://doi.org/10.3389/fgene.2024.1382371) emphasize early molecular genetic testing and integration of NGS and other omics to confirm diagnoses and expand phenotype spectra: **“Physicians should consider molecular genetic testing as a first diagnostic step in overgrowth syndromes.”** (prawitt2024molecularmechanismsof pages 1-2)
2. **Operationalized clinical NGS pipelines (2024):** Abolhassani et al. (NPJ Genomic Medicine, 2024-02; https://doi.org/10.1038/s41525-024-00393-0) describe large-scale real-world ES/panel testing with explicit sequencing depths, variant filtering against gnomAD/Iranome, and ACMG/AMP + ClinGen-guided classification, which is directly applicable to diagnosing monogenic overgrowth/ID syndromes such as FIBP-related TROFAS. (abolhassani2024clinicalapplicationof pages 9-10)
3. **Emerging phenotype expansions in FIBP-related disease (2023–2024 referenced in 2025 review):** Although the key phenotype-expansion case report retrieved is 2025, it explicitly cites 2023–2024 literature reporting additional manifestations (e.g., inflammatory eye disease) and novel variants, indicating rapid ongoing delineation of TROFAS. (cosentino2025expandingtheknowledge pages 6-7)

---

## Key statistics (from recent and classic studies)
- **15q overgrowth syndrome (pooled literature as of 2009):** overgrowth **71% (12/17)**, learning difficulties **100% (17/17)**, characteristic facial appearance **94% (16/17)**; renal anomalies in investigated cases **45% (5/11)** for trisomy and **80% (4/5)** for tetrasomy. (tatton‐brown200915qovergrowthsyndrome pages 5-6)
- **FIBP-related syndrome (case-based):** severe renal outcomes may be common among early reports: **“Half of the reported cases die in the first few days of life mainly due to renal failure.”** (akawi2016arecessivesyndrome pages 2-3)

---

## Limitations of this report
- **Ontology identifiers** (MONDO/Orphanet/MeSH/ICD) for the target disease name were not recoverable from the retrieved literature excerpts and therefore are not provided.
- Some requested elements (population prevalence, formal surveillance schedules, variant population frequencies, ClinVar/ClinGen summaries) require database queries beyond the papers available in the current tool state.

---

## Primary sources (URLs; publication dates)
- Tatton-Brown K. et al. *Am J Med Genet A* (2009-02): “15q overgrowth syndrome...” https://doi.org/10.1002/ajmg.a.32534 (tatton‐brown200915qovergrowthsyndrome pages 1-2, tatton‐brown200915qovergrowthsyndrome pages 5-6, tatton‐brown200915qovergrowthsyndrome pages 6-8)
- Cannarella R. et al. *Endocrine Connections* (2017-10): “Chromosome 15 structural abnormalities: effect on IGF1R gene expression and function” https://doi.org/10.1530/ec-17-0158 (cannarella2017chromosome15structural pages 1-2)
- Bodle E.E. et al. *Am J Med Genet A* (2019-06; accepted 2018-11-05): “Acute leukemia in a patient with 15q overgrowth syndrome” https://doi.org/10.1002/ajmg.a.61115 (bodle2019acuteleukemiain pages 1-2)
- Akawi N. et al. *Am J Med Genet A* (2016-05): FIBP-related recessive overgrowth/ID/renal dysplasia https://doi.org/10.1002/ajmg.a.37741 (akawi2016arecessivesyndrome pages 3-5)
- Prawitt D., Eggermann T. *Frontiers in Genetics* (2024-06): omics diagnostics in overgrowth https://doi.org/10.3389/fgene.2024.1382371 (prawitt2024molecularmechanismsof pages 1-2)
- Abolhassani A. et al. *NPJ Genomic Medicine* (2024-02): clinical NGS implementation https://doi.org/10.1038/s41525-024-00393-0 (abolhassani2024clinicalapplicationof pages 9-10)


References

1. (tatton‐brown200915qovergrowthsyndrome pages 1-2): Katrina Tatton‐Brown, Daniela T. Pilz, Karen Helene Örstavik, Michael Patton, John C.K. Barber, Morag N. Collinson, Vivienne K. Maloney, Shuwen Huang, John A. Crolla, Karen Marks, Eli Ormerod, Peter Thompson, Zafar Nawaz, Christa Lese‐Martin, Susan Tomkins, Paula Waits, Nazneen Rahman, and Meriel McEntagart. 15q overgrowth syndrome: a newly recognized phenotype associated with overgrowth, learning difficulties, characteristic facial appearance, renal anomalies and increased dosage of distal chromosome 15q. American Journal of Medical Genetics Part A, 149A:147-154, Feb 2009. URL: https://doi.org/10.1002/ajmg.a.32534, doi:10.1002/ajmg.a.32534. This article has 68 citations.

2. (tatton‐brown200915qovergrowthsyndrome pages 5-6): Katrina Tatton‐Brown, Daniela T. Pilz, Karen Helene Örstavik, Michael Patton, John C.K. Barber, Morag N. Collinson, Vivienne K. Maloney, Shuwen Huang, John A. Crolla, Karen Marks, Eli Ormerod, Peter Thompson, Zafar Nawaz, Christa Lese‐Martin, Susan Tomkins, Paula Waits, Nazneen Rahman, and Meriel McEntagart. 15q overgrowth syndrome: a newly recognized phenotype associated with overgrowth, learning difficulties, characteristic facial appearance, renal anomalies and increased dosage of distal chromosome 15q. American Journal of Medical Genetics Part A, 149A:147-154, Feb 2009. URL: https://doi.org/10.1002/ajmg.a.32534, doi:10.1002/ajmg.a.32534. This article has 68 citations.

3. (tatton‐brown200915qovergrowthsyndrome pages 6-8): Katrina Tatton‐Brown, Daniela T. Pilz, Karen Helene Örstavik, Michael Patton, John C.K. Barber, Morag N. Collinson, Vivienne K. Maloney, Shuwen Huang, John A. Crolla, Karen Marks, Eli Ormerod, Peter Thompson, Zafar Nawaz, Christa Lese‐Martin, Susan Tomkins, Paula Waits, Nazneen Rahman, and Meriel McEntagart. 15q overgrowth syndrome: a newly recognized phenotype associated with overgrowth, learning difficulties, characteristic facial appearance, renal anomalies and increased dosage of distal chromosome 15q. American Journal of Medical Genetics Part A, 149A:147-154, Feb 2009. URL: https://doi.org/10.1002/ajmg.a.32534, doi:10.1002/ajmg.a.32534. This article has 68 citations.

4. (akawi2016arecessivesyndrome pages 3-5): Nadia Akawi, Salma Ben‐Salem, Laura Lahti, Juha Partanen, Bassam R. Ali, and Lihadh Al‐Gazali. A recessive syndrome of intellectual disability, moderate overgrowth, and renal dysplasia predisposing to wilms tumor is caused by a mutation in fibp gene. American Journal of Medical Genetics Part A, 170:2111-2118, May 2016. URL: https://doi.org/10.1002/ajmg.a.37741, doi:10.1002/ajmg.a.37741. This article has 18 citations.

5. (cosentino2025expandingtheknowledge pages 1-3): Andrea Cosentino, Flavia D’Orazio, Roberto Magnato, and Wilhelm Berger. Expanding the knowledge about thauvin-robinet-faivre syndrome: a case report with novel clinical findings and review of the literature. Journal of applied genetics, Jun 2025. URL: https://doi.org/10.1007/s13353-025-00984-2, doi:10.1007/s13353-025-00984-2. This article has 1 citations and is from a peer-reviewed journal.

6. (tatton‐brown200915qovergrowthsyndrome pages 4-5): Katrina Tatton‐Brown, Daniela T. Pilz, Karen Helene Örstavik, Michael Patton, John C.K. Barber, Morag N. Collinson, Vivienne K. Maloney, Shuwen Huang, John A. Crolla, Karen Marks, Eli Ormerod, Peter Thompson, Zafar Nawaz, Christa Lese‐Martin, Susan Tomkins, Paula Waits, Nazneen Rahman, and Meriel McEntagart. 15q overgrowth syndrome: a newly recognized phenotype associated with overgrowth, learning difficulties, characteristic facial appearance, renal anomalies and increased dosage of distal chromosome 15q. American Journal of Medical Genetics Part A, 149A:147-154, Feb 2009. URL: https://doi.org/10.1002/ajmg.a.32534, doi:10.1002/ajmg.a.32534. This article has 68 citations.

7. (cannarella2017chromosome15structural pages 1-2): Rossella Cannarella, Teresa Mattina, Rosita A Condorelli, Laura M Mongioì, Giuseppe Pandini, Sandro La Vignera, and Aldo E Calogero. Chromosome 15 structural abnormalities: effect on igf1r gene expression and function. Endocrine Connections, 6:528-539, Oct 2017. URL: https://doi.org/10.1530/ec-17-0158, doi:10.1530/ec-17-0158. This article has 34 citations and is from a peer-reviewed journal.

8. (bodle2019acuteleukemiain pages 1-2): Ethan E. Bodle, Ridhi Gupta, Athena M. Cherry, Lori Muffly, and Melanie A. Manning. Acute leukemia in a patient with 15q overgrowth syndrome. American Journal of Medical Genetics Part A, 179:1025-1029, Jun 2019. URL: https://doi.org/10.1002/ajmg.a.61115, doi:10.1002/ajmg.a.61115. This article has 0 citations.

9. (tatton‐brown200915qovergrowthsyndrome pages 2-4): Katrina Tatton‐Brown, Daniela T. Pilz, Karen Helene Örstavik, Michael Patton, John C.K. Barber, Morag N. Collinson, Vivienne K. Maloney, Shuwen Huang, John A. Crolla, Karen Marks, Eli Ormerod, Peter Thompson, Zafar Nawaz, Christa Lese‐Martin, Susan Tomkins, Paula Waits, Nazneen Rahman, and Meriel McEntagart. 15q overgrowth syndrome: a newly recognized phenotype associated with overgrowth, learning difficulties, characteristic facial appearance, renal anomalies and increased dosage of distal chromosome 15q. American Journal of Medical Genetics Part A, 149A:147-154, Feb 2009. URL: https://doi.org/10.1002/ajmg.a.32534, doi:10.1002/ajmg.a.32534. This article has 68 citations.

10. (bodle2019acuteleukemiain pages 2-3): Ethan E. Bodle, Ridhi Gupta, Athena M. Cherry, Lori Muffly, and Melanie A. Manning. Acute leukemia in a patient with 15q overgrowth syndrome. American Journal of Medical Genetics Part A, 179:1025-1029, Jun 2019. URL: https://doi.org/10.1002/ajmg.a.61115, doi:10.1002/ajmg.a.61115. This article has 0 citations.

11. (akawi2016arecessivesyndrome pages 1-2): Nadia Akawi, Salma Ben‐Salem, Laura Lahti, Juha Partanen, Bassam R. Ali, and Lihadh Al‐Gazali. A recessive syndrome of intellectual disability, moderate overgrowth, and renal dysplasia predisposing to wilms tumor is caused by a mutation in fibp gene. American Journal of Medical Genetics Part A, 170:2111-2118, May 2016. URL: https://doi.org/10.1002/ajmg.a.37741, doi:10.1002/ajmg.a.37741. This article has 18 citations.

12. (cosentino2025expandingtheknowledge pages 6-7): Andrea Cosentino, Flavia D’Orazio, Roberto Magnato, and Wilhelm Berger. Expanding the knowledge about thauvin-robinet-faivre syndrome: a case report with novel clinical findings and review of the literature. Journal of applied genetics, Jun 2025. URL: https://doi.org/10.1007/s13353-025-00984-2, doi:10.1007/s13353-025-00984-2. This article has 1 citations and is from a peer-reviewed journal.

13. (akawi2016arecessivesyndrome pages 2-3): Nadia Akawi, Salma Ben‐Salem, Laura Lahti, Juha Partanen, Bassam R. Ali, and Lihadh Al‐Gazali. A recessive syndrome of intellectual disability, moderate overgrowth, and renal dysplasia predisposing to wilms tumor is caused by a mutation in fibp gene. American Journal of Medical Genetics Part A, 170:2111-2118, May 2016. URL: https://doi.org/10.1002/ajmg.a.37741, doi:10.1002/ajmg.a.37741. This article has 18 citations.

14. (akawi2016arecessivesyndrome pages 7-8): Nadia Akawi, Salma Ben‐Salem, Laura Lahti, Juha Partanen, Bassam R. Ali, and Lihadh Al‐Gazali. A recessive syndrome of intellectual disability, moderate overgrowth, and renal dysplasia predisposing to wilms tumor is caused by a mutation in fibp gene. American Journal of Medical Genetics Part A, 170:2111-2118, May 2016. URL: https://doi.org/10.1002/ajmg.a.37741, doi:10.1002/ajmg.a.37741. This article has 18 citations.

15. (prawitt2024molecularmechanismsof pages 1-2): Dirk Prawitt and Thomas Eggermann. Molecular mechanisms of human overgrowth and use of omics in its diagnostics: chances and challenges. Frontiers in Genetics, Jun 2024. URL: https://doi.org/10.3389/fgene.2024.1382371, doi:10.3389/fgene.2024.1382371. This article has 5 citations and is from a peer-reviewed journal.

16. (cosentino2025expandingtheknowledge pages 5-6): Andrea Cosentino, Flavia D’Orazio, Roberto Magnato, and Wilhelm Berger. Expanding the knowledge about thauvin-robinet-faivre syndrome: a case report with novel clinical findings and review of the literature. Journal of applied genetics, Jun 2025. URL: https://doi.org/10.1007/s13353-025-00984-2, doi:10.1007/s13353-025-00984-2. This article has 1 citations and is from a peer-reviewed journal.

17. (cannarella2017chromosome15structural pages 5-6): Rossella Cannarella, Teresa Mattina, Rosita A Condorelli, Laura M Mongioì, Giuseppe Pandini, Sandro La Vignera, and Aldo E Calogero. Chromosome 15 structural abnormalities: effect on igf1r gene expression and function. Endocrine Connections, 6:528-539, Oct 2017. URL: https://doi.org/10.1530/ec-17-0158, doi:10.1530/ec-17-0158. This article has 34 citations and is from a peer-reviewed journal.

18. (abolhassani2024clinicalapplicationof pages 9-10): Ayda Abolhassani, Zohreh Fattahi, Maryam Beheshtian, Mahsa Fadaee, Raheleh Vazehan, Fatemeh Ahangari, Shima Dehdahsi, Mehrshid Faraji Zonooz, Elham Parsimehr, Zahra Kalhor, Fatemeh Peymani, Maryam Mozaffarpour Nouri, Mojgan Babanejad, Khadijeh Noudehi, Fatemeh Fatehi, Shima Zamanian Najafabadi, Fariba Afroozan, Hilda Yazdan, Bita Bozorgmehr, Azita Azarkeivan, Shokouh Sadat Mahdavi, Pooneh Nikuei, Farzad Fatehi, Payman Jamali, Mahmoud Reza Ashrafi, Parvaneh Karimzadeh, Haleh Habibi, Kimia Kahrizi, Shahriar Nafissi, Ariana Kariminejad, and Hossein Najmabadi. Clinical application of next generation sequencing for mendelian disease diagnosis in the iranian population. NPJ Genomic Medicine, Feb 2024. URL: https://doi.org/10.1038/s41525-024-00393-0, doi:10.1038/s41525-024-00393-0. This article has 15 citations and is from a peer-reviewed journal.