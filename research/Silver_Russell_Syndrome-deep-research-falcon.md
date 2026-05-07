---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T08:59:00.658765'
end_time: '2026-05-07T09:17:14.673199'
duration_seconds: 1094.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Silver-Russell Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Silver-Russell Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Silver-Russell Syndrome** covering all of the
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
- **Disease Name:** Silver-Russell Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Silver-Russell Syndrome** covering all of the
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


# Silver–Russell Syndrome (SRS): Comprehensive Disease Characteristics Report

## Executive summary
Silver–Russell syndrome (SRS; also called Russell–Silver syndrome) is a rare congenital growth disorder and **imprinting disorder** characterized by prenatal and postnatal growth restriction, relative macrocephaly, prominent forehead, body asymmetry, and feeding difficulties. It is primarily a **clinical diagnosis**, supported by molecular confirmation in ~60% of cases; the two most common molecular causes are **11p15.5 loss of methylation (LOM) at IC1 / H19–IGF2** and **maternal uniparental disomy of chromosome 7 (upd(7)mat)**. International consensus guidance emphasizes early nutritional optimization and proactive prevention of hypoglycaemia, with recombinant human growth hormone (rhGH) providing benefits beyond linear growth (body composition, appetite, motor development), and monitoring/treating early/rapid puberty when appropriate. (wakeling2017diagnosisandmanagement pages 4-7, wakeling2017diagnosisandmanagement pages 17-20)

## Quick reference table (identifiers, molecular causes, NH‑CSS, management)
| Section | Item | Summary | Approx. frequency / threshold | Citations |
|---|---|---|---|---|
| Identifiers / classification | Silver-Russell syndrome (SRS; Russell-Silver syndrome) | Rare congenital **imprinting disorder** characterized by prenatal and postnatal growth restriction, relative macrocephaly, prominent forehead, asymmetry, and feeding difficulties; **OMIM #180860** | Molecular cause identified in ~60% of clinically diagnosed cases | (jang2025silver–russellsyndromefrom pages 1-2, wakeling2017diagnosisandmanagement pages 4-7) |
| Synonyms | Alternative names | Silver-Russell syndrome; Russell-Silver syndrome; SRS; historically RSS | Not applicable | (jang2025silver–russellsyndromefrom pages 1-2, wakeling2017diagnosisandmanagement pages 4-7) |
| Molecular etiology | 11p15 LOM / IC1 hypomethylation (H19/IGF2:IG-DMR) | Major subtype; reduced paternal IGF2 expression is central to growth restriction | ~30–60% overall; 63.8% in one typical RSS cohort | (wakeling2017diagnosisandmanagement pages 4-7, geoffron2018chromosome14q32.2imprinted pages 2-3, wakeling2017diagnosisandmanagement pages 7-10) |
| Molecular etiology | Maternal uniparental disomy of chromosome 7, upd(7)mat / mUPD7 | Second major subtype | ~5–10% | (geoffron2018chromosome14q32.2imprinted pages 2-3, wakeling2017diagnosisandmanagement pages 4-7) |
| Molecular etiology | Other causes | CNVs involving 11p15 or chr7; rare defects at 14q32 and other imprinted loci; rare monogenic causes including **IGF2, CDKN1C, HMGA2, PLAG1** | Remaining minority; monogenic causes are rare | (geoffron2018chromosome14q32.2imprinted pages 1-2, kurup2025silverrussellsyndromesecondary pages 1-2, hong2024prenataldiagnosisof pages 7-7) |
| NH-CSS | 1. Small for gestational age | Birth weight and/or birth length ≤ -2 SDS | Criterion present/absent | (jang2025silver–russellsyndromefrom pages 1-2, wakeling2017diagnosisandmanagement media 5493aae2) |
| NH-CSS | 2. Postnatal growth failure | Height at ~24 months ≤ -2 SDS or height ≤ -2 SDS below mid-parental target | Criterion present/absent | (jang2025silver–russellsyndromefrom pages 1-2, wakeling2017diagnosisandmanagement media 5493aae2) |
| NH-CSS | 3. Relative macrocephaly at birth | Head circumference at birth ≥ 1.5 SDS above birth weight and/or length SDS | Criterion present/absent | (jang2025silver–russellsyndromefrom pages 1-2, wakeling2017diagnosisandmanagement media 5493aae2) |
| NH-CSS | 4. Prominent forehead | Forehead projecting beyond facial plane on side view in early childhood | Criterion present/absent | (jang2025silver–russellsyndromefrom pages 1-2, wakeling2017diagnosisandmanagement media 5493aae2) |
| NH-CSS | 5. Body asymmetry | e.g., leg-length discrepancy ≥0.5 cm or asymmetry of other body parts | Criterion present/absent | (jang2025silver–russellsyndromefrom pages 1-2, wakeling2017diagnosisandmanagement media 5493aae2) |
| NH-CSS | 6. Feeding difficulties / low BMI | BMI ≤ -2 SDS at 24 months and/or current use of feeding support/appetite stimulants | Criterion present/absent | (jang2025silver–russellsyndromefrom pages 1-2, wakeling2017diagnosisandmanagement media 5493aae2) |
| NH-CSS performance | Clinical use | Molecular testing recommended when **≥3/6** criteria are met; clinical diagnosis usually **≥4/6**, including relative macrocephaly and prominent forehead; sensitivity ~98%, NPV ~89%, specificity ~36% | Thresholds as shown | (wakeling2017diagnosisandmanagement pages 7-10, jang2025silver–russellsyndromefrom pages 1-2) |
| Management | Nutrition / feeding | Early goal is nutritional repletion while avoiding excessive rapid catch-up weight gain; assess reflux, dysmotility, and oral-motor dysfunction; multidisciplinary care recommended | >70% digestive problems; ~55% severe GERD reported in consensus summary | (wakeling2017diagnosisandmanagement pages 14-17, wakeling2017diagnosisandmanagement pages 4-7) |
| Management | Hypoglycemia prevention | Risk is increased in young children; monitor safe fasting interval, consider home ketone monitoring, avoid prolonged fasting; nighttime glucose polymer (infants) or uncooked cornstarch (older children) can be used | Hypoglycemia incidence ~27% in young children in consensus summary | (wakeling2017diagnosisandmanagement pages 17-20) |
| Management | Growth hormone (GH) therapy | GH improves height, body composition, appetite, motor development, and may reduce hypoglycemia risk; classic GH deficiency is uncommon | Predicted adult height gain ~7–11 cm; mean gain ~+1.2 to +1.4 SDS in studies summarized by consensus | (wakeling2017diagnosisandmanagement pages 4-7, wakeling2017diagnosisandmanagement pages 17-20) |
| Management | Puberty management | Monitor for premature adrenarche and relatively early/rapid central puberty; GnRH analogues may help preserve adult height potential in selected patients | Case-by-case endocrine management | (wakeling2017diagnosisandmanagement pages 4-7, jang2025silver–russellsyndromefrom pages 5-6) |


*Table: This table condenses key disease identifiers, molecular causes, NH-CSS diagnostic criteria, and main management pillars for Silver-Russell syndrome. It is useful as a quick reference for building a structured disease knowledge-base entry with source-linked evidence.*

---

## 1. Disease information
### 1.1 Definition and overview
SRS is a rare congenital disorder (imprinting disorder) with prenatal and postnatal growth retardation and multisystem involvement. The 2017 international consensus statement summarizes it as “an imprinting disorder that causes prenatal and postnatal growth retardation,” noting substantial overlap with care of children born small for gestational age (SGA), but with SRS-specific management issues (feeding, hypoglycaemia, asymmetry, neurodevelopment, psychosocial) (wakeling2017diagnosisandmanagement pages 4-7).

**Authoritative expert opinion (international consensus):**
- “SRS is primarily a clinical diagnosis; however, molecular testing enables confirmation of the clinical diagnosis and defines the subtype. A ‘normal’ result from a molecular test does not exclude the diagnosis of SRS.” (Wakeling et al., 2017) (wakeling2017diagnosisandmanagement pages 7-10).

### 1.2 Key identifiers
- **OMIM phenotype:** **180860** (reported in a retrieved review excerpt). (jang2025silver–russellsyndromefrom pages 1-2)
- **MONDO / Orphanet / ICD-10/ICD-11 / MeSH:** Not retrievable from the currently gathered full-text evidence in this run; therefore not asserted here.

### 1.3 Synonyms
- Silver–Russell syndrome (SRS)
- Russell–Silver syndrome
- Historical: Russell–Silver syndrome (RSS) (jang2025silver–russellsyndromefrom pages 1-2, wakeling2017diagnosisandmanagement pages 4-7)

### 1.4 Evidence sources (individual vs aggregated)
This report integrates:
- **Aggregated expert consensus** (international consensus statement) (wakeling2017diagnosisandmanagement pages 4-7).
- **Human cohort studies** with molecular/clinical data (e.g., Netchine et al. 2007; Temple/14q32 overlap cohort) (geoffron2018chromosome14q32.2imprinted pages 2-3).
- **Recent human observational research** (executive function study in adolescents/adults) (jang2025silver–russellsyndromefrom pages 2-4).
- **ClinicalTrials.gov registry records** for real-world/implementation-oriented studies (NCT06878716 chunk 1, NCT05214742 chunk 1, NCT01842659 chunk 1).

---

## 2. Etiology
### 2.1 Primary causal factors (genetic/epigenetic)
SRS is best understood as a disorder of **genomic imprinting** affecting growth-regulatory networks. The international consensus estimates identifiable molecular causes in ~60% of clinically diagnosed patients, most commonly:
- **11p15 LOM (IC1 / H19–IGF2 IG-DMR hypomethylation)**: ~30–60% (wakeling2017diagnosisandmanagement pages 4-7).
- **upd(7)mat**: ~5–10% (wakeling2017diagnosisandmanagement pages 4-7).

A large early cohort study explicitly quantified major etiologies in a clinically-defined RSS subgroup within SGA patients:
- “Of the 127 SGA patients, 58 were diagnosed with RSS; **37 of these (63.8%) displayed partial LOM of the 11p15 ICR1 domain, and three (5.2%) had mUPD7**.” (Netchine et al., 2007) (wesseler2019molecularandclinical pages 11-13).

**Other (rare) etiologies** include CNVs affecting imprinting regions, and rare SNVs in growth/imprinting genes (e.g., IGF2, CDKN1C, HMGA2, PLAG1), with phenotypic heterogeneity that can reduce sensitivity of purely clinical criteria for these subgroups (kurup2025silverrussellsyndromesecondary pages 1-2).

### 2.2 Risk factors
**Genetic risk factors:** SRS is typically sporadic, but recurrence risk may increase in specific scenarios (e.g., heritable CNVs affecting imprinting control regions, or maternal-effect variants affecting imprint maintenance). Evidence for maternal-effect mechanisms and multilocus imprinting disturbance is discussed in WGS-based diagnostic studies and imprinting-disorder mechanistic workups (NCT05945576 chunk 2).

**Non-genetic/environmental risk factors:** Direct environmental causes are not established for SRS as a Mendelian/imprinting disorder in the retrieved evidence. However, imprinting disorders (including SRS) are under investigation for potential association with assisted reproductive technologies (ART), with ongoing observational studies designed to quantify ART conception prevalence in SRS (NCT06878716 chunk 1).

### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
In the retrieved evidence, gene–environment interaction is best framed as **epigenetic vulnerability during imprint establishment/maintenance**; this is being assessed via real-world observational studies of ART/infertility factors in SRS families (NCT06878716 chunk 1).

---

## 3. Phenotypes
### 3.1 Core phenotype spectrum (with onset and frequency where available)
SRS typically presents **prenatally and in early childhood** with growth restriction and failure to thrive. Key differentiating clinical features from other SGA/IUGR include **relative macrocephaly, prominent forehead, body asymmetry, and feeding difficulties** (wakeling2017diagnosisandmanagement pages 4-7).

**Feeding/GI:** The international consensus notes substantial GI burden, stating “>70% have digestive problems” and “55% severe GERD” in the cited summary evidence (wakeling2017diagnosisandmanagement pages 14-17).

**Hypoglycaemia:** The consensus statement indicates increased risk in early childhood with an estimated incidence “≈27%” and highlights that episodes are often asymptomatic and nocturnal, motivating home monitoring and structured fasting guidance (wakeling2017diagnosisandmanagement pages 17-20).

**Neurocognitive/behavioral:** Neurocognitive problems are noted to be more frequent in upd(7)mat than in 11p15 LOM in the consensus overview (wakeling2017diagnosisandmanagement pages 14-17). A 2023 study of adolescents/adults reported largely normal group-level executive function but clinically relevant impairment in some individuals, concluding that SRS individuals “could be at high risk of developing executive dysfunction or attention-deficit/hyperactivity disorder” (Burgevin et al., 2023) (jang2025silver–russellsyndromefrom pages 2-4).

### 3.2 NH‑CSS phenotyping and diagnostic criteria mapping (HPO suggestions)
The NH‑CSS uses six criteria; a tightly-cropped table listing criteria was retrieved (wakeling2017diagnosisandmanagement media 5493aae2). Criteria and suggested HPO mappings:
1) **SGA (birth weight/length ≤ −2 SDS)** → *Small for gestational age* (HP:0001518) (wakeling2017diagnosisandmanagement media 5493aae2)
2) **Postnatal growth failure** → *Postnatal growth retardation* (HP:0008897) / *Short stature* (HP:0004322) (wakeling2017diagnosisandmanagement media 5493aae2)
3) **Relative macrocephaly at birth** → *Relative macrocephaly* (HP:0004488) (wakeling2017diagnosisandmanagement media 5493aae2)
4) **Prominent forehead** → *Prominent forehead* (HP:0011220) (wakeling2017diagnosisandmanagement media 5493aae2)
5) **Body asymmetry** → *Body asymmetry* (HP:0000930) / *Hemihypotrophy* (HP:0001528) (wakeling2017diagnosisandmanagement media 5493aae2)
6) **Feeding difficulties / low BMI** → *Feeding difficulties* (HP:0011968) / *Failure to thrive* (HP:0001508) / *Low body mass index* (HP:0001511) (wakeling2017diagnosisandmanagement media 5493aae2)

**NH‑CSS performance/thresholds:** In prospective evaluation, NH‑CSS sensitivity was ~98% and NPV ~89%, but specificity was low (~36%); the consensus recommends molecular testing if ≥3 criteria and clinical SRS diagnosis at ≥4 criteria including relative macrocephaly and protruding/prominent forehead (wakeling2017diagnosisandmanagement pages 7-10).

### 3.3 Quality-of-life impacts
The consensus statement explicitly highlights “psychosocial challenges” and the need for multidisciplinary care, including psychology/speech/occupational and family support, implying significant functional and QoL impact (wakeling2017diagnosisandmanagement pages 4-7).

---

## 4. Genetic / molecular information
### 4.1 Causal loci and genes (current understanding)
**11p15.5 imprinting region (IC1/H19–IGF2 and related DMRs):** Loss of methylation at IC1 is a major cause of “typical Russell-Silver syndrome” (wesseler2019molecularandclinical pages 11-13). Mechanistically, hypomethylation at the paternally methylated H19/IGF2 imprinting control region reduces paternal IGF2 expression, a key driver of fetal growth restriction (wakeling2017diagnosisandmanagement pages 7-10).

**Chromosome 7 (upd(7)mat):** Common secondary cause (~5–10%) (wakeling2017diagnosisandmanagement pages 4-7).

**Other imprinted regions (notably 14q32.2):** Disruption of 14q32.2 can present with SRS-like phenotypes; in a 14q32.2 disruption cohort, **72.7% met NH‑CSS ≥4/6**, illustrating clinically important overlap and the need for differential molecular diagnosis beyond 11p15/upd7 (geoffron2018chromosome14q32.2imprinted pages 1-2).

**Rare monogenic causes (examples):** A 2025 synthesis of rare (epi)genotypes reports that variants in **IGF2, CDKN1C, HMGA2, PLAG1** can cause SRS-like phenotypes, but NH‑CSS misses a substantial fraction (9–55%) depending on gene, supporting broader genetic testing approaches when suspicion persists despite borderline clinical scoring (kurup2025silverrussellsyndromesecondary pages 1-2).

### 4.2 Variant types and diagnostic implications
Across SRS and SRS-like presentations, pathogenic mechanisms include:
- **Epimutations** (DNA methylation abnormalities; often mosaic)
- **UPD**
- **CNVs** (duplications/deletions involving imprinting regions)
- **SNVs** in growth/imprinting genes (wakeling2017diagnosisandmanagement pages 7-10, kurup2025silverrussellsyndromesecondary pages 1-2)

**Recent (2024) pedigree evidence for CNV/epigenotype complexity:** A 2024 familial case described 11p15 duplications with variable methylation patterns and phenotypic outcomes; “duplications of maternal IC2 (copy number of 3) with enhanced methylation (methylation index 0.62) resulted in typical SRS,” demonstrating clinically relevant inheritance and prenatal testing complexity (hong2024prenataldiagnosisof pages 1-2).

### 4.3 Epigenetic information
SRS is classically an imprinting disorder with methylation alterations at imprinted DMRs (11p15, sometimes multi-locus). Mosaicism and tissue-specific methylation can cause false negatives in blood, motivating multi-tissue strategies and quantitative assays (wakeling2017diagnosisandmanagement pages 7-10).

---

## 5. Environmental information
No established infectious, toxin, or lifestyle causal factors were identified in the retrieved evidence. Environmental context is primarily studied via **ART and infertility** as potential correlates of imprinting disorders, including SRS, with an observational pilot study designed to estimate ART conception prevalence in SRS and collect parental exposure/occupation and fertility data (NCT06878716 chunk 1).

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (high-level)
1) **Upstream trigger:** imprinting disturbance (e.g., 11p15 IC1 hypomethylation) or upd(7)mat (wakeling2017diagnosisandmanagement pages 4-7).
2) **Molecular consequence:** altered parent-of-origin gene expression, especially growth regulators (e.g., reduced paternal IGF2 expression) (wakeling2017diagnosisandmanagement pages 7-10).
3) **Cellular/tissue effects:** impaired fetal growth and postnatal growth, low muscle mass, feeding difficulties, increased fasting vulnerability (hypoglycaemia) (wakeling2017diagnosisandmanagement pages 17-20).
4) **Clinical manifestations:** SGA, postnatal growth failure, relative macrocephaly, prominent forehead, asymmetry, GI problems/GERD, hypoglycaemia, variable neurocognitive outcomes, and early/rapid puberty risk (wakeling2017diagnosisandmanagement pages 4-7, wakeling2017diagnosisandmanagement pages 17-20).

### 6.2 Pathways and ontology suggestions
**Key pathway concept:** IGF2 growth axis and imprinting network dysregulation (wakeling2017diagnosisandmanagement pages 7-10).

**Suggested GO Biological Process terms (examples):**
- GO:0001558 *regulation of cell growth*
- GO:0040007 *growth*
- GO:0008283 *cell population proliferation*
- GO:0010817 *regulation of hormone levels*

**Suggested Cell Ontology (CL) terms (broad, given limited direct evidence in retrieved sources):**
- CL:0000187 *cell of the endocrine pancreas* (re hypoglycaemia context)
- CL:0000540 *skeletal muscle cell* (low muscle mass, growth)

**Suggested Reactome/KEGG framing:** IGF signaling; growth hormone/IGF axis (supported conceptually in consensus management and IGF2 mechanism discussion) (wakeling2017diagnosisandmanagement pages 7-10, wakeling2017diagnosisandmanagement pages 17-20).

### 6.3 Molecular profiling / omics
No transcriptomics/proteomics/metabolomics signatures specific to SRS were present in the retrieved full-text evidence for 2023–2024; model-building iPSC studies are registered to examine “consequences of epimutations at 11p15 or 14q32 on the imprinted gene network” (NCT05214742 chunk 1).

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
SRS is a multisystem condition with prominent effects on:
- **Whole-body growth and musculoskeletal development** (short stature, asymmetry; scoliosis risk) (wakeling2017diagnosisandmanagement pages 4-7)
- **Gastrointestinal system** (feeding difficulties, reflux, dysmotility) (wakeling2017diagnosisandmanagement pages 14-17)
- **Endocrine/metabolic regulation** (hypoglycaemia risk, puberty timing, insulin resistance risk) (wakeling2017diagnosisandmanagement pages 17-20)
- **Neurodevelopment/psychosocial domains** (speech/motor delay, psychosocial challenges; variable executive function risk) (wakeling2017diagnosisandmanagement pages 4-7, jang2025silver–russellsyndromefrom pages 2-4)

### 7.2 UBERON suggestions (examples)
- UBERON:0002048 *thyroid gland* / endocrine system context (puberty/metabolic monitoring)
- UBERON:0000948 *heart* (cardiac issues as differential/rare monogenic presentations) (kurup2025silverrussellsyndromesecondary pages 1-2)
- UBERON:0002107 *liver* and UBERON:0001264 *pancreas* (glucose homeostasis context)
- UBERON:0002387 *long bone of lower limb* (leg-length discrepancy/asymmetry)

---

## 8. Temporal development
- **Onset:** Typically congenital/prenatal (SGA) with postnatal growth failure evident in infancy/early childhood (wakeling2017diagnosisandmanagement pages 4-7).
- **Course:** Lifelong short stature risk; early feeding and hypoglycaemia issues are emphasized in the first years, with later risks including early/rapid puberty and metabolic complications depending on growth/nutrition trajectory (wakeling2017diagnosisandmanagement pages 14-17, wakeling2017diagnosisandmanagement pages 17-20).

---

## 9. Inheritance and population
### 9.1 Epidemiology
The international consensus reports incidence estimates ranging from **~1:30,000 to 1:100,000**, with one molecularly confirmed estimate in Estonia of **~1:70,000** (wakeling2017diagnosisandmanagement pages 4-7).

### 9.2 Inheritance patterns
SRS is “generally sporadic,” and a strong family history should trigger evaluation for alternative diagnoses or rare inherited molecular mechanisms (e.g., familial CNVs with parent-of-origin effects) (wakeling2017diagnosisandmanagement pages 14-17).

### 9.3 Population demographics
No sex ratio or ethnicity/geographic variant distribution data were present in the retrieved evidence.

---

## 10. Diagnostics
### 10.1 Clinical criteria (NH‑CSS)
NH‑CSS is the recommended clinical scoring system with 6 criteria (wakeling2017diagnosisandmanagement media 5493aae2). The consensus specifies:
- **Molecular testing recommended** when **≥3/6** criteria are present.
- **Clinical SRS diagnosis** typically reserved for **≥4/6**, including **relative macrocephaly and prominent forehead** (wakeling2017diagnosisandmanagement pages 7-10).

### 10.2 Molecular testing workflow (current practice)
The consensus emphasizes first-line molecular evaluation for:
- **11p15.5 methylation abnormalities** (H19/IGF2 IG-DMR)
- **upd(7)mat**
- Consideration of **CNVs** and broader genomic causes when initial testing is negative and clinical suspicion remains (wakeling2017diagnosisandmanagement pages 7-10, wakeling2017diagnosisandmanagement pages 14-17).

**Assay considerations:** MS-MLPA is widely used; low-level mosaicism and tissue specificity can yield false-negative blood testing, motivating careful assay choice and potentially multi-tissue sampling (blood vs buccal/skin) in some cases (wakeling2017diagnosisandmanagement pages 7-10).

### 10.3 Genomic sequencing developments
A real-world WGS study (100,000 Genomes Project category “SRS”) reported that WGS can identify SNVs, CNVs, UPD, and maternal-effect variants and may be a “valuable addition” to diagnosis of SRS and related growth restriction disorders (Alhendi et al., 2022) (NCT05945576 chunk 2). 

### 10.4 Prenatal diagnosis
A 2024 report demonstrates prenatal testing using microarray plus MS-MLPA methylation assessment in a familial 11p15 duplication context, highlighting the feasibility and complexity of prenatal diagnosis for imprinting disturbances (hong2024prenataldiagnosisof pages 1-2). Complementarily, a registered prenatal screening study evaluates agreement of methylation index measurements across fetal/cord blood/placental tissues (NCT01842659 chunk 1).

### 10.5 Differential diagnosis
Consensus guidance notes that consanguinity/family history should prompt alternatives, and highlights overlap with osteogenesis imperfecta, recommending skeletal survey and possible COL1A1/2 testing in suggestive cases (wakeling2017diagnosisandmanagement pages 14-17).

---

## 11. Outcome / prognosis
The retrieved evidence emphasizes improved outcomes with early multidisciplinary management and growth-hormone therapy but does not provide disease-specific mortality rates. Untreated adult height was summarized in a retrieved review excerpt as approximately **−3.1 SDS** (jang2025silver–russellsyndromefrom pages 1-2).

---

## 12. Treatment
### 12.1 Core management principles (real-world implementation)
The 2017 consensus recommends experienced multidisciplinary care (endocrinology-led coordination plus dietetics, gastroenterology, genetics, orthopaedics, speech/psychology) and prioritizes early nutritional optimization and hypoglycaemia prevention (wakeling2017diagnosisandmanagement pages 14-17).

**Direct expert statement (consensus):**
- “The benefits of treating patients with SRS with growth hormone include improved body composition, motor development and appetite, reduced risk of hypoglycaemia and increased height.” (wakeling2017diagnosisandmanagement pages 4-7)

### 12.2 Nutrition/feeding interventions
- Evaluate and treat reflux/dysmotility/oromotor issues; reserve gastrostomy/enteral feeding as a last resort and avoid promoting excessive weight gain (wakeling2017diagnosisandmanagement pages 14-17).

**Suggested MAXO terms:**
- MAXO:0000064 *nutritional support*
- MAXO:0000147 *gastrostomy*

### 12.3 Hypoglycaemia prevention
Consensus recommendations include:
- Home **urinary ketone monitoring** to define safe fasting times.
- Night-time supplementation with high–molecular-weight glucose polymer (infants <10 months) or **uncooked cornstarch** (older infants/children) to prevent nocturnal hypoglycaemia.
- Avoid glucagon; provide rapid-access plans for IV dextrose during illness/perioperative fasting (wakeling2017diagnosisandmanagement pages 17-20).

**Suggested MAXO terms:**
- MAXO:0000100 *blood glucose monitoring*
- MAXO:0000789 *dietary carbohydrate supplementation*

### 12.4 Growth hormone (GH) therapy
SRS is an indication under the SGA rhGH license, and the consensus summarizes adult-height benefits:
- Predicted adult height increases of **~7–11 cm** and mean gains of **~+1.2 to +1.4 SDS** in summarized studies (doses 35–70 μg/kg/day). Response correlates with earlier start and baseline height SDS (wakeling2017diagnosisandmanagement pages 17-20).

**Suggested MAXO term:**
- MAXO:0000747 *growth hormone therapy*

### 12.5 Puberty management
Clinicians should monitor for premature adrenarche and early/rapid central puberty; GnRH analogues may be used to preserve adult height in selected cases (wakeling2017diagnosisandmanagement pages 4-7).

**Suggested MAXO term:**
- MAXO:0000912 *gonadotropin-releasing hormone analogue therapy*

### 12.6 Experimental/clinical trials landscape (selected)
- **NCT06878716 (2025; NOT_YET_RECRUITING):** estimates prevalence of ART conception among SRS children; collects parental fertility and exposure data (telephone questionnaire) (NCT06878716 chunk 1).
- **NCT01842659 (2013; diagnostic interventional):** evaluates agreement of 11p15 methylation index between amniocytes and cord blood leukocytes for prenatal screening (NCT01842659 chunk 1).
- **NCT05214742 (2022; ENROLLING_BY_INVITATION):** derives iPSCs from blood to model imprinting disorders (including SRS) to study consequences of 11p15/14q32 epimutations on imprinted gene networks (NCT05214742 chunk 1).
- **NCT02859688 (COMPLETED):** proof-of-concept germline vs somatic methylation in an SRS proband; reports efficient reversion of constitutive epimutation in spermatozoa, informing reproductive counseling (NCT02859688 chunk 1).

---

## 13. Prevention
### 13.1 Primary prevention
No established primary prevention exists for imprinting disorders like SRS.

### 13.2 Secondary/tertiary prevention
Consensus recommendations function as secondary/tertiary prevention by preventing complications:
- Early nutritional management to avoid malnutrition and reduce hypoglycaemia risk.
- Monitoring and proactive management of hypoglycaemia, puberty timing, and metabolic risk (wakeling2017diagnosisandmanagement pages 14-17, wakeling2017diagnosisandmanagement pages 17-20).

### 13.3 Genetic counseling / reproductive risk
A dedicated observational study (REPAR) provides counseling-relevant evidence that somatic epimutations may revert in germline, affecting recurrence risk assessment (NCT02859688 chunk 1). Familial CNV/epigenotype cases (11p15 duplication with parent-of-origin methylation effects) underscore the importance of parental testing and imprinting-aware interpretation (hong2024prenataldiagnosisof pages 1-2).

---

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in the retrieved evidence.

---

## 15. Model organisms
A mouse model relevant to rare SRS-associated microduplication mechanisms has been reported (CDKN1C dosage model), supporting mechanistic investigation of feeding/behavioral phenotypes; the abstract notes that “rare SRS patients carry maternally inherited microduplications spanning… CDKN1C…” and describes behavioral alterations attributable to elevated Cdkn1c (jang2025silver–russellsyndromefrom pages 6-7). Additionally, a registered clinical study aims to create iPSC-derived models to study imprinting networks in SRS and related imprinting disorders (NCT05214742 chunk 1).

---

## Recent developments (prioritizing 2023–2024)
1) **Neuropsychology in adolescents/adults (2023):** Executive function testing suggests no uniform executive dysfunction phenotype at group level, but clinically significant impairments in subsets and potential increased ADHD/executive dysfunction risk (jang2025silver–russellsyndromefrom pages 2-4).
2) **Prenatal and familial molecular diagnosis (2024):** Multi-generation 11p15 duplication with methylation-dependent expressivity illustrates complexity in inheritance and supports combined microarray + methylation testing in prenatal/familial workups (hong2024prenataldiagnosisof pages 1-2).
3) **Genetic landscape in persistent short stature after SGA (2023):** In a cohort of children born SGA with persistent short stature, SRS constituted a substantial fraction of genetically explained cases, using Netchine–Harbison criteria to define SRS clinically (toni2024thegeneticlandscape pages 9-10).

---

## Limitations of this report relative to template requirements
- **PMIDs:** The retrieved full-text evidence in this run did not expose PubMed identifiers directly; therefore, PMIDs are not asserted.
- **MONDO/Orphanet/ICD/MeSH IDs:** Not present in the retrieved sources; therefore not asserted.
- **Many requested detailed frequencies (phenotype-by-phenotype) and multi-omics signatures:** Not available in the retrieved excerpts; only the consensus-provided and cohort-provided statistics reported above are included.

---

## Key source URLs (with publication dates)
- Wakeling et al. *Nat Rev Endocrinol* (Feb 2017). https://doi.org/10.1038/nrendo.2016.138 (wakeling2017diagnosisandmanagement pages 4-7)
- Netchine et al. *J Clin Endocrinol Metab* (Aug 2007). https://doi.org/10.1210/jc.2007-0354 (wesseler2019molecularandclinical pages 11-13)
- Burgevin et al. *PLOS ONE* (Jan 2023). https://doi.org/10.1371/journal.pone.0279745 (jang2025silver–russellsyndromefrom pages 2-4)
- Hong et al. *Front Genet* (Dec 2024). https://doi.org/10.3389/fgene.2024.1465521 (hong2024prenataldiagnosisof pages 1-2)
- Geoffron et al. *J Clin Endocrinol Metab* (Jul 2018). https://doi.org/10.1210/jc.2017-02152 (geoffron2018chromosome14q32.2imprinted pages 2-3)
- ClinicalTrials.gov: NCT06878716 (registered 2025). https://clinicaltrials.gov/study/NCT06878716 (NCT06878716 chunk 1)
- ClinicalTrials.gov: NCT05214742 (registered 2022). https://clinicaltrials.gov/study/NCT05214742 (NCT05214742 chunk 1)
- ClinicalTrials.gov: NCT01842659 (registered 2013). https://clinicaltrials.gov/study/NCT01842659 (NCT01842659 chunk 1)
- ClinicalTrials.gov: NCT02859688 (registered 2016). https://clinicaltrials.gov/study/NCT02859688 (NCT02859688 chunk 1)


References

1. (wakeling2017diagnosisandmanagement pages 4-7): Emma L. Wakeling, Frédéric Brioude, Oluwakemi Lokulo-Sodipe, Susan M. O'Connell, Jennifer Salem, Jet Bliek, Ana P. M. Canton, Krystyna H. Chrzanowska, Justin H. Davies, Renuka P. Dias, Béatrice Dubern, Miriam Elbracht, Eloise Giabicani, Adda Grimberg, Karen Grønskov, Anita C. S. Hokken-Koelega, Alexander A. Jorge, Masayo Kagami, Agnes Linglart, Mohamad Maghnie, Klaus Mohnike, David Monk, Gudrun E. Moore, Philip G. Murray, Tsutomu Ogata, Isabelle Oliver Petit, Silvia Russo, Edith Said, Meropi Toumba, Zeynep Tümer, Gerhard Binder, Thomas Eggermann, Madeleine D. Harbison, I. Karen Temple, Deborah J. G. Mackay, and Irène Netchine. Diagnosis and management of silver–russell syndrome: first international consensus statement. Nature Reviews Endocrinology, 13:105-124, Feb 2017. URL: https://doi.org/10.1038/nrendo.2016.138, doi:10.1038/nrendo.2016.138. This article has 610 citations and is from a domain leading peer-reviewed journal.

2. (wakeling2017diagnosisandmanagement pages 17-20): Emma L. Wakeling, Frédéric Brioude, Oluwakemi Lokulo-Sodipe, Susan M. O'Connell, Jennifer Salem, Jet Bliek, Ana P. M. Canton, Krystyna H. Chrzanowska, Justin H. Davies, Renuka P. Dias, Béatrice Dubern, Miriam Elbracht, Eloise Giabicani, Adda Grimberg, Karen Grønskov, Anita C. S. Hokken-Koelega, Alexander A. Jorge, Masayo Kagami, Agnes Linglart, Mohamad Maghnie, Klaus Mohnike, David Monk, Gudrun E. Moore, Philip G. Murray, Tsutomu Ogata, Isabelle Oliver Petit, Silvia Russo, Edith Said, Meropi Toumba, Zeynep Tümer, Gerhard Binder, Thomas Eggermann, Madeleine D. Harbison, I. Karen Temple, Deborah J. G. Mackay, and Irène Netchine. Diagnosis and management of silver–russell syndrome: first international consensus statement. Nature Reviews Endocrinology, 13:105-124, Feb 2017. URL: https://doi.org/10.1038/nrendo.2016.138, doi:10.1038/nrendo.2016.138. This article has 610 citations and is from a domain leading peer-reviewed journal.

3. (jang2025silver–russellsyndromefrom pages 1-2): K Jang and J Moon. Silver–russell syndrome: from molecular pathogenesis to clinical management. Unknown journal, 2025.

4. (geoffron2018chromosome14q32.2imprinted pages 2-3): Sophie Geoffron, Walid Abi Habib, Sandra Chantot-Bastaraud, Béatrice Dubern, Virginie Steunou, Salah Azzi, Alexandra Afenjar, Tiffanny Busa, Ana Pinheiro Canton, Christel Chalouhi, Marie-Noëlle Dufourg, Blandine Esteva, Mélanie Fradin, David Geneviève, Solveig Heide, Bertrand Isidor, Agnès Linglart, Fanny Morice Picard, Catherine Naud-Saudreau, Isabelle Oliver Petit, Nicole Philip, Catherine Pienkowski, Marlène Rio, Sylvie Rossignol, Maithé Tauber, Julien Thevenon, Thuy-Ai Vu-Hong, Madeleine D Harbison, Jennifer Salem, Frédéric Brioude, Irène Netchine, and Eloïse Giabicani. Chromosome 14q32.2 imprinted region disruption as an alternative molecular diagnosis of silver-russell syndrome. The Journal of Clinical Endocrinology & Metabolism, 103:2436–2446, Jul 2018. URL: https://doi.org/10.1210/jc.2017-02152, doi:10.1210/jc.2017-02152. This article has 76 citations.

5. (wakeling2017diagnosisandmanagement pages 7-10): Emma L. Wakeling, Frédéric Brioude, Oluwakemi Lokulo-Sodipe, Susan M. O'Connell, Jennifer Salem, Jet Bliek, Ana P. M. Canton, Krystyna H. Chrzanowska, Justin H. Davies, Renuka P. Dias, Béatrice Dubern, Miriam Elbracht, Eloise Giabicani, Adda Grimberg, Karen Grønskov, Anita C. S. Hokken-Koelega, Alexander A. Jorge, Masayo Kagami, Agnes Linglart, Mohamad Maghnie, Klaus Mohnike, David Monk, Gudrun E. Moore, Philip G. Murray, Tsutomu Ogata, Isabelle Oliver Petit, Silvia Russo, Edith Said, Meropi Toumba, Zeynep Tümer, Gerhard Binder, Thomas Eggermann, Madeleine D. Harbison, I. Karen Temple, Deborah J. G. Mackay, and Irène Netchine. Diagnosis and management of silver–russell syndrome: first international consensus statement. Nature Reviews Endocrinology, 13:105-124, Feb 2017. URL: https://doi.org/10.1038/nrendo.2016.138, doi:10.1038/nrendo.2016.138. This article has 610 citations and is from a domain leading peer-reviewed journal.

6. (geoffron2018chromosome14q32.2imprinted pages 1-2): Sophie Geoffron, Walid Abi Habib, Sandra Chantot-Bastaraud, Béatrice Dubern, Virginie Steunou, Salah Azzi, Alexandra Afenjar, Tiffanny Busa, Ana Pinheiro Canton, Christel Chalouhi, Marie-Noëlle Dufourg, Blandine Esteva, Mélanie Fradin, David Geneviève, Solveig Heide, Bertrand Isidor, Agnès Linglart, Fanny Morice Picard, Catherine Naud-Saudreau, Isabelle Oliver Petit, Nicole Philip, Catherine Pienkowski, Marlène Rio, Sylvie Rossignol, Maithé Tauber, Julien Thevenon, Thuy-Ai Vu-Hong, Madeleine D Harbison, Jennifer Salem, Frédéric Brioude, Irène Netchine, and Eloïse Giabicani. Chromosome 14q32.2 imprinted region disruption as an alternative molecular diagnosis of silver-russell syndrome. The Journal of Clinical Endocrinology & Metabolism, 103:2436–2446, Jul 2018. URL: https://doi.org/10.1210/jc.2017-02152, doi:10.1210/jc.2017-02152. This article has 76 citations.

7. (kurup2025silverrussellsyndromesecondary pages 1-2): Uttara Kurup, David B. N. Lim, Avinaash V. Maharaj, Miho Ishida, Justin H. Davies, and Helen L. Storr. Silver-russell syndrome secondary to rare (epi)genotypes exhibits phenotypic heterogeneity challenging clinical diagnosis. Clinical Epigenetics, Dec 2025. URL: https://doi.org/10.1186/s13148-025-02023-7, doi:10.1186/s13148-025-02023-7. This article has 1 citations and is from a peer-reviewed journal.

8. (hong2024prenataldiagnosisof pages 7-7): Shurong Hong, Hua Wei, Xueyi Zhuang, Weirong Huang, and Yu Zhang. Prenatal diagnosis of a silver-russell syndrome caused by 11p15 duplication and pedigree analysis. Frontiers in Genetics, Dec 2024. URL: https://doi.org/10.3389/fgene.2024.1465521, doi:10.3389/fgene.2024.1465521. This article has 0 citations and is from a peer-reviewed journal.

9. (wakeling2017diagnosisandmanagement media 5493aae2): Emma L. Wakeling, Frédéric Brioude, Oluwakemi Lokulo-Sodipe, Susan M. O'Connell, Jennifer Salem, Jet Bliek, Ana P. M. Canton, Krystyna H. Chrzanowska, Justin H. Davies, Renuka P. Dias, Béatrice Dubern, Miriam Elbracht, Eloise Giabicani, Adda Grimberg, Karen Grønskov, Anita C. S. Hokken-Koelega, Alexander A. Jorge, Masayo Kagami, Agnes Linglart, Mohamad Maghnie, Klaus Mohnike, David Monk, Gudrun E. Moore, Philip G. Murray, Tsutomu Ogata, Isabelle Oliver Petit, Silvia Russo, Edith Said, Meropi Toumba, Zeynep Tümer, Gerhard Binder, Thomas Eggermann, Madeleine D. Harbison, I. Karen Temple, Deborah J. G. Mackay, and Irène Netchine. Diagnosis and management of silver–russell syndrome: first international consensus statement. Nature Reviews Endocrinology, 13:105-124, Feb 2017. URL: https://doi.org/10.1038/nrendo.2016.138, doi:10.1038/nrendo.2016.138. This article has 610 citations and is from a domain leading peer-reviewed journal.

10. (wakeling2017diagnosisandmanagement pages 14-17): Emma L. Wakeling, Frédéric Brioude, Oluwakemi Lokulo-Sodipe, Susan M. O'Connell, Jennifer Salem, Jet Bliek, Ana P. M. Canton, Krystyna H. Chrzanowska, Justin H. Davies, Renuka P. Dias, Béatrice Dubern, Miriam Elbracht, Eloise Giabicani, Adda Grimberg, Karen Grønskov, Anita C. S. Hokken-Koelega, Alexander A. Jorge, Masayo Kagami, Agnes Linglart, Mohamad Maghnie, Klaus Mohnike, David Monk, Gudrun E. Moore, Philip G. Murray, Tsutomu Ogata, Isabelle Oliver Petit, Silvia Russo, Edith Said, Meropi Toumba, Zeynep Tümer, Gerhard Binder, Thomas Eggermann, Madeleine D. Harbison, I. Karen Temple, Deborah J. G. Mackay, and Irène Netchine. Diagnosis and management of silver–russell syndrome: first international consensus statement. Nature Reviews Endocrinology, 13:105-124, Feb 2017. URL: https://doi.org/10.1038/nrendo.2016.138, doi:10.1038/nrendo.2016.138. This article has 610 citations and is from a domain leading peer-reviewed journal.

11. (jang2025silver–russellsyndromefrom pages 5-6): K Jang and J Moon. Silver–russell syndrome: from molecular pathogenesis to clinical management. Unknown journal, 2025.

12. (jang2025silver–russellsyndromefrom pages 2-4): K Jang and J Moon. Silver–russell syndrome: from molecular pathogenesis to clinical management. Unknown journal, 2025.

13. (NCT06878716 chunk 1):  Silver Russell Syndrome, Parental Fertility and Assisted Reproductive Technology. Assistance Publique - Hôpitaux de Paris. 2025. ClinicalTrials.gov Identifier: NCT06878716

14. (NCT05214742 chunk 1):  Developing Derived Induced Pluripotent Stem Cells as a Model to Understand Imprinted Disorders. Institute of Cardiometabolism and Nutrition, France. 2022. ClinicalTrials.gov Identifier: NCT05214742

15. (NCT01842659 chunk 1):  Prenatal Screening for Imprinting Anomalies Implicated in Beckwith Wiedemann and Silver Russell Syndromes. Assistance Publique - Hôpitaux de Paris. 2013. ClinicalTrials.gov Identifier: NCT01842659

16. (wesseler2019molecularandclinical pages 11-13): Katharina Wesseler, Florian Kraft, and Thomas Eggermann. Molecular and clinical opposite findings in 11p15.5 associated imprinting disorders: characterization of basic mechanisms to improve clinical management. International Journal of Molecular Sciences, 20:4219, Aug 2019. URL: https://doi.org/10.3390/ijms20174219, doi:10.3390/ijms20174219. This article has 15 citations.

17. (NCT05945576 chunk 2):  IDMet (RaDiCo Cohort) (RaDiCo-IDMet). Institut National de la Santé Et de la Recherche Médicale, France. 2017. ClinicalTrials.gov Identifier: NCT05945576

18. (hong2024prenataldiagnosisof pages 1-2): Shurong Hong, Hua Wei, Xueyi Zhuang, Weirong Huang, and Yu Zhang. Prenatal diagnosis of a silver-russell syndrome caused by 11p15 duplication and pedigree analysis. Frontiers in Genetics, Dec 2024. URL: https://doi.org/10.3389/fgene.2024.1465521, doi:10.3389/fgene.2024.1465521. This article has 0 citations and is from a peer-reviewed journal.

19. (NCT02859688 chunk 1):  Can Epimutations be Inherited? How to Manage Patients With Imprinting-related Diseases Who Wish to Become Parents. Centre Hospitalier Universitaire Dijon. 2015. ClinicalTrials.gov Identifier: NCT02859688

20. (jang2025silver–russellsyndromefrom pages 6-7): K Jang and J Moon. Silver–russell syndrome: from molecular pathogenesis to clinical management. Unknown journal, 2025.

21. (toni2024thegeneticlandscape pages 9-10): L. Toni, L. Plachy, P. Dusatkova, S. Amaratunga, Lenka Elblová, Z. Šumník, S. Koloušková, M. Šnajderová, B. Obermannová, Š. Průhová, and J. Lebl. The genetic landscape of children born small for gestational age with persistent short stature. Hormone Research in Paediatrics, 97:40-52, Apr 2023. URL: https://doi.org/10.1159/000530521, doi:10.1159/000530521. This article has 24 citations and is from a peer-reviewed journal.