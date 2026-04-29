---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-26T20:02:17.137998'
end_time: '2026-04-26T20:13:58.309383'
duration_seconds: 701.17
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sarcoidosis
  mondo_id: ''
  category: Immune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 62
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sarcoidosis
- **MONDO ID:**  (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Sarcoidosis** covering all of the
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
- **Disease Name:** Sarcoidosis
- **MONDO ID:**  (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Sarcoidosis** covering all of the
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


## Sarcoidosis — Comprehensive Disease Characteristics Report (Immune)

**Target disease:** Sarcoidosis (immune-mediated granulomatous disease) (vagts2025immunopathogenesisofsarcoidosis pages 1-2, starshinova2024chronicsarcoidosisdiagnostic pages 2-3)  
**MONDO ID:** **MONDO:0019338** (Open Targets mapping) (he2025globalburdenof pages 1-2)  
**Category:** Immune / inflammatory

### Executive summary (current understanding)
Sarcoidosis is a multisystem inflammatory disease characterized pathologically by well-formed **non-caseating / non-necrotizing granulomas** that can involve virtually any organ, most often the lungs and intrathoracic lymph nodes (kim2024advancesincellular pages 1-5, vagts2025immunopathogenesisofsarcoidosis pages 1-2). The prevailing model is that **genetically susceptible** individuals mount an exaggerated immune response to **unidentified (exogenous or endogenous) antigen(s)**, producing Th1/Th17-skewed inflammation and macrophage-driven granuloma formation, with variable outcomes ranging from spontaneous resolution to chronic inflammation, organ damage, and fibrosis (vagts2025immunopathogenesisofsarcoidosis pages 1-2, papanikolaou2025phenotypesandendotypes pages 4-6).

### Key structured reference
The following table consolidates identifiers, diagnostic criteria, epidemiology, mechanisms, biomarkers/imaging, and treatment/trial evidence.

| Domain | Key points | Recent evidence/data | Source (DOI/PMID/NCT) | URL | Citation ID |
|---|---|---|---|---|---|
| Identifiers | Disease entity: **sarcoidosis**; MONDO: **MONDO:0019338**. Common coding systems referenced in recent epidemiology work include **ICD-10 D86–D86.2, D86.9** for pulmonary sarcoidosis/related coding. | Open Targets disease mapping identifies sarcoidosis as MONDO_0019338; GBD-based epidemiology study used ICD-10 **D86–D86.2, D86.9** for case definition. MeSH/ICD-11 were not explicitly provided in the retrieved evidence set. | MONDO_0019338; ICD-10 D86–D86.2, D86.9 | https://platform.opentargets.org/disease/MONDO_0019338 ; https://doi.org/10.1186/s40001-025-03141-x | (he2025globalburdenof pages 1-2) |
| Definition & diagnostic criteria | Multisystem inflammatory/granulomatous disease with **non-caseating/non-necrotizing granulomas**; diagnosis is clinicoradiologic-pathologic and requires exclusion of mimics. | Recent review states diagnosis is based on **three main criteria**: clinical presentation, histologic detection of non-caseating granulomas in ≥1 tissue sample, and exclusion of alternative granulomatous diseases. Meta-analysis reiterates accepted approach: compatible clinical picture + radiologic evidence + histologic demonstration of non-necrotising granulomatous disease. | doi:10.3390/jcm13226974; doi:10.1007/s00330-024-10949-4 | https://doi.org/10.3390/jcm13226974 ; https://doi.org/10.1007/s00330-024-10949-4 | (starshinova2024chronicsarcoidosisdiagnostic pages 2-3, donnelly2025metaanalysisof[18f]fdgpetct pages 1-2, starshinova2024chronicsarcoidosisdiagnostic pages 14-15) |
| Organ involvement | Lung and intrathoracic lymph nodes are the dominant sites; extrapulmonary disease is common and clinically important. | Lung involvement reported in **up to 90–95%** of cases; extrapulmonary disease occurs in **~30–50%**. Example frequencies from review: cutaneous **15.9%**, ocular **11.8%**, neurologic **4.6%**. | doi:10.1152/ajpcell.00507.2023; doi:10.3390/jcm13226974; doi:10.1055/a-2716-5737 | https://doi.org/10.1152/ajpcell.00507.2023 ; https://doi.org/10.3390/jcm13226974 ; https://doi.org/10.1055/a-2716-5737 | (kim2024advancesincellular pages 1-5, starshinova2024chronicsarcoidosisdiagnostic pages 2-3, vagts2025immunopathogenesisofsarcoidosis pages 1-2) |
| Epidemiology: population ranges | Sarcoidosis frequency varies markedly by ancestry/geography. | Reported prevalence range **~4.7–64/100,000** and incidence **~1–35.5/100,000/year**; other review-level estimates note incidence worldwide roughly **1–15/100,000/year**. Highest incidence examples in retrieved evidence: Scandinavia/UK **~64/100,000**; African American populations **~39/100,000**; South Korea **4.67/100,000** and Japan **3.7/100,000**. | doi:10.1038/s41598-025-93708-9; doi:10.1152/ajpcell.00507.2023 | https://doi.org/10.1038/s41598-025-93708-9 ; https://doi.org/10.1152/ajpcell.00507.2023 | (guttmannducke2025firstinsightsand pages 1-2, kim2024advancesincellular pages 1-5) |
| Epidemiology: example registry/cohort data | Recent real-world registries provide contemporary demographics and stage distributions. | Vienna registry (n=199): mean age **52 ± 13 y**, women **57.5%**; chest X-ray stage **1: 34.5%**, **2: 46%**, **3: 9.5%**, **4: 6%**; **37.5%** received oral corticosteroids; median OCS duration **5 years** (IQR 3–7.5). | doi:10.1038/s41598-025-93708-9 | https://doi.org/10.1038/s41598-025-93708-9 | (guttmannducke2025firstinsightsand pages 1-2, guttmannducke2025firstinsightsand pages 2-3) |
| Outcomes & mortality | Mortality risk is elevated overall and is highest soon after diagnosis. | Population-based cohort: mortality **17.7%** in sarcoidosis vs **10.6%** controls; adjusted all-cause mortality **HR 1.79** (95% CI 1.64–1.96). First year after diagnosis had highest risk; one analysis reported first-year multivariable **HR 2.99** (95% CI 2.39–3.75). Male sex and older age/comorbidity increased risk. | doi:10.3390/medicina60111787 | https://doi.org/10.3390/medicina60111787 | (patt2024elevatedmortalityrisk pages 1-2, patt2024elevatedmortalityrisk pages 8-9, patt2024elevatedmortalityrisk pages 9-11) |
| Pathophysiology | Current model: antigen-driven, immune-mediated granulomatous inflammation with macrophage core and lymphocyte rim. | Sarcoidosis is described as a T-cell-mediated disorder with **IFN-γ** signature driven by **Th1, Th17, Th17.1** cells; granulomas contain macrophages/epithelioid cells/multinucleated giant cells plus surrounding lymphocytes and fibroblasts. APC antigen presentation via **MHC-II**, innate signaling via **TLRs**, and pathways including **JAK-STAT**, **mTORC1**, and dysregulated autophagy are implicated. | doi:10.1172/jci175264; doi:10.1055/a-2716-5737; doi:10.3390/biomedicines13020287 | https://doi.org/10.1172/jci175264 ; https://doi.org/10.1055/a-2716-5737 ; https://doi.org/10.3390/biomedicines13020287 | (weeratunga2024immunemechanismsof pages 1-2, vagts2025immunopathogenesisofsarcoidosis pages 1-2, papanikolaou2025phenotypesandendotypes pages 4-6) |
| Cell types & molecular findings | Recent omics highlight macrophage metabolic reprogramming and tissue-level immune architecture. | Single-cell RNA-seq study found increased **TREM2+ macrophages** expressing **ACE** and lysozyme in cutaneous sarcoid granulomas; macrophages were hypermetabolic with activation of the **pentose phosphate pathway (PPP)**, and PPP inhibition attenuated granuloma formation in vitro/in vivo. Spatial transcriptomics in muscular sarcoidosis showed granuloma/perigranuloma enrichment for **T-cell and monocyte/macrophage cytokine programs**, **extracellular matrix**, and **TGF-β** signaling with profibrotic signatures near granulomas. | doi:10.1172/jci171088; doi:10.3390/cells12232747 | https://doi.org/10.1172/jci171088 ; https://doi.org/10.3390/cells12232747 | (dhanani2025immunosuppressivetherapiesin pages 10-12, starshinova2024chronicsarcoidosisdiagnostic pages 26-27) |
| Biomarkers & lab support | No single disease-specific biomarker; supportive markers reflect granuloma burden and immune activation. | Review-level evidence supports **serum ACE** elevation correlating with granuloma burden/stages II–III and extrathoracic involvement; **sIL-2R** reflects **Th1 activation** and may predict progression/relapse. BAL may show lymphocytosis **>15%** and **CD4/CD8 ≥3.5**, but these findings are not specific. Hypercalcemia with low PTH and normal/low 25-hydroxyvitamin D can occur. | doi:10.3390/jcm13226974 | https://doi.org/10.3390/jcm13226974 | (starshinova2024chronicsarcoidosisdiagnostic pages 15-17, starshinova2024chronicsarcoidosisdiagnostic pages 14-15) |
| Imaging & diagnostic performance | Imaging is central: CXR/Scadding, HRCT, PET/CT; biopsy remains gold standard. | HRCT is more sensitive than chest radiography for parenchymal disease. Meta-analysis of **18F-FDG PET/CT** in suspected pulmonary sarcoidosis: pooled sensitivity **0.971** and specificity **0.873**; post-treatment SUVmax reduction correlated with FVC (**r=0.644**) and DLCO (**r=0.582**) improvement. PET/CT also helps detect occult extrapulmonary disease and inflammatory activity. | doi:10.1007/s00330-024-10949-4; doi:10.3390/medicina61122094 | https://doi.org/10.1007/s00330-024-10949-4 ; https://doi.org/10.3390/medicina61122094 | (donnelly2025metaanalysisof[18f]fdgpetct pages 1-2, baratella2025ctimagingfeatures pages 3-4, baratella2025ctimagingfeatures pages 1-3) |
| Standard treatment approach | First-line therapy remains glucocorticoids for symptomatic/progressive disease; steroid-sparing therapy often needed. | Recent evidence-based review: prednisone **20–40 mg/day** with slow taper over **6–18 months** is standard first-line for symptomatic pulmonary disease. **Methotrexate** is the preferred steroid-sparing/second-line agent and is increasingly considered as an alternative first-line option; other options include **azathioprine, leflunomide, mycophenolate**. Refractory disease: **infliximab/adalimumab**; emerging options include **JAK inhibitors**, **rituximab**, **RCI**. | doi:10.3390/jcm14196828 | https://doi.org/10.3390/jcm14196828 | (dhanani2025immunosuppressivetherapiesin pages 12-13, dhanani2025immunosuppressivetherapiesin pages 3-4, dhanani2025immunosuppressivetherapiesin pages 1-3) |
| Recent trial result: PREDMETH | First-line methotrexate vs prednisone in treatment-naïve pulmonary sarcoidosis. | NEJM 2025 PREDMETH trial (n=138): mean change in % predicted FVC at week 24 was **+6.75** points with prednisone vs **+6.11** with methotrexate; adjusted between-group difference **−1.17** (95% CI −4.27 to 1.93), meeting noninferiority. AE profile differed: prednisone commonly caused **weight gain, insomnia, increased appetite**; methotrexate caused **nausea, fatigue, abnormal LFTs**. | doi:10.1056/NEJMoa2501443; NCT04314193 | https://doi.org/10.1056/NEJMoa2501443 ; https://clinicaltrials.gov/study/NCT04314193 | (kahlmann2025firstlinetreatmentof pages 1-2) |
| Anti-TNF trial evidence | Infliximab has trial evidence for pulmonary sarcoidosis; adalimumab studied in smaller cohorts. | **NCT00073437**: multicenter randomized double-blind placebo-controlled Phase 3 infliximab trial, enrollment **139**; doses **3 mg/kg** or **5 mg/kg** at weeks 0, 2, 6, 12, 18, 24; primary endpoint was change in **% predicted FVC at week 24**. **NCT00311246**: adalimumab single-group study, enrollment **11**, 40 mg SC weekly for 45 weeks; primary endpoint change in **FVC from screening to week 24**. | NCT00073437; PMID 16840744; PMID 18256069; NCT00311246 | https://clinicaltrials.gov/study/NCT00073437 ; https://pubmed.ncbi.nlm.nih.gov/16840744/ ; https://pubmed.ncbi.nlm.nih.gov/18256069/ ; https://clinicaltrials.gov/study/NCT00311246 | (NCT00073437 chunk 1, NCT00311246 chunk 2) |
| Emerging/ongoing trials | New agents target steroid-sparing immunomodulation or fibrosis progression. | **Efzofitimod/ATYR1923**: **NCT03824392** completed Phase 1/2 study; **NCT05415137** ongoing Phase 3, active-not-recruiting, planned enrollment **268**. **Pirfenidone**: **NCT03260556** Phase 4 randomized triple-masked placebo-controlled study, enrollment **60**, primary endpoint **time until clinical worsening** over 2 years. **Nintedanib**: **NCT06479603** recruiting Phase 4 RCT in fibrotic sarcoidosis, enrollment **120** (from registry metadata), interventions nintedanib + standard care. **Tofacitinib**: **NCT03793439** completed pilot in corticosteroid-dependent sarcoidosis, Phase 1, enrollment **5**. | NCT03824392; NCT05415137; NCT03260556; NCT06479603; NCT03793439 | https://clinicaltrials.gov/study/NCT03824392 ; https://clinicaltrials.gov/study/NCT05415137 ; https://clinicaltrials.gov/study/NCT03260556 ; https://clinicaltrials.gov/study/NCT06479603 ; https://clinicaltrials.gov/study/NCT03793439 | (NCT03824392 chunk 2, NCT03260556 chunk 1, NCT06479603 chunk 2) |


*Table: This table condenses the key identifiers, diagnostic criteria, epidemiology, mechanisms, biomarkers, imaging performance, and treatment/trial evidence for sarcoidosis using only the retrieved evidence. It is designed as a high-density reference for rapid knowledge base population and citation tracking.*

---

## 1. Disease Information

### 1.1 Definition and overview
Sarcoidosis is described as a complex multisystem immune-mediated disorder in which inflammatory cells accumulate and organize into **non-caseous granulomas** within affected organs (kim2024advancesincellular pages 1-5). A recent immunopathogenesis review defines it as “**a granulomatous disease of unknown cause, triggered by an unidentified antigen**,” with the histopathologic hallmark being “**discrete, well-formed, non-necrotizing granulomas** composed of epithelioid histiocytes and multinucleated giant cells surrounded by lymphocytes, plasma cells, and fibroblasts” (vagts2025immunopathogenesisofsarcoidosis pages 1-2).

### 1.2 Key identifiers (with availability in retrieved sources)
* **MONDO:** MONDO:0019338 (Open Targets disease object) (he2025globalburdenof pages 1-2).
* **ICD-10:** D86–D86.2, D86.9 (used in GBD-based epidemiologic analysis for case definition) (he2025globalburdenof pages 1-2).
* **MeSH / ICD-11 / Orphanet / OMIM (disease entry):** Not directly retrievable from the current evidence set; additional database-specific queries (MeSH Browser, ICD-11, Orphanet, OMIM) would be required for authoritative IDs.

### 1.3 Synonyms / alternative names
The retrieved sources primarily use “sarcoidosis” and organ qualifiers (pulmonary sarcoidosis, extrapulmonary sarcoidosis, muscular sarcoidosis). Formal synonym lists were not present in the extracted texts; common clinical variants highlighted include **Löfgren syndrome** (acute presentation) (weeratunga2024immunemechanismsof pages 1-2, vagts2025immunopathogenesisofsarcoidosis pages 1-2).

### 1.4 Evidence provenance
This report synthesizes **aggregated disease-level resources** (reviews, meta-analyses, registry cohorts, and clinical trial registries), not individual EHR case notes, except where cohorts explicitly derive from health-system databases (e.g., Clalit) (patt2024elevatedmortalityrisk pages 1-2, patt2024elevatedmortalityrisk pages 2-3).

---

## 2. Etiology

### 2.1 Causal factors (current consensus)
Sarcoidosis etiology remains unknown; leading models invoke a **triggering antigen** in a genetically predisposed host leading to persistent immune activation and granuloma formation (vagts2025immunopathogenesisofsarcoidosis pages 1-2, papanikolaou2025phenotypesandendotypes pages 4-6).

### 2.2 Genetic risk factors (susceptibility/severity loci)
A 2023 integrated GWAS–eQTL approach (European and African ancestry cohorts) reported that dysregulated innate immunity and MHC-related pathways are implicated in sarcoidosis risk/severity and validated loci including **NOTCH4, IL27RA, BTNL2, ANXA11, and HLA-DRB1** (doi:10.31488/ejrm.137) (casanova2023examinationofeqtl pages 1-3). This supports a polygenic architecture with strong immunogenetic involvement.

**Ontology (gene) suggestions:** HGNC symbols: **BTNL2, ANXA11, HLA-DRB1, NOTCH4, IL27RA** (casanova2023examinationofeqtl pages 1-3).  
**Mechanism linkage:** antigen presentation / MHC class II and innate immune response pathways (casanova2023examinationofeqtl pages 1-3, papanikolaou2025phenotypesandendotypes pages 4-6).

### 2.3 Environmental and infectious risk factors
The retrieved mechanistic phenotype/endotype review notes infectious agents such as **Mycobacterium species** and **Propionibacterium acnes** as implicated candidates and describes innate immune sensing via TLR pathways in antigen presentation contexts (papanikolaou2025phenotypesandendotypes pages 4-6). (This reflects hypothesized triggers; causal proof is not established.)

### 2.4 Protective factors
A protective-factor evidence base was not directly extractable from the retrieved documents.

### 2.5 Gene–environment interactions
Direct GxE effect sizes were not provided in the retrieved evidence set.

---

## 3. Phenotypes (clinical manifestations)

### 3.1 Core clinical phenotype domain
Sarcoidosis has heterogeneous organ involvement. The lungs dominate clinical burden, with pulmonary/intrathoracic involvement reported up to ~90–95% across sources (kim2024advancesincellular pages 1-5, vagts2025immunopathogenesisofsarcoidosis pages 1-2, baratella2025ctimagingfeatures pages 1-3). Extrapulmonary involvement is common, with review-level estimates of ~30–50% (starshinova2024chronicsarcoidosisdiagnostic pages 2-3).

### 3.2 Example organ involvement frequencies (from retrieved sources)
From a 2024 chronic sarcoidosis review: extrapulmonary disease ~30–50%, with reported organ frequencies including **cutaneous 15.9%**, **ocular 11.8%**, and **neurologic 4.6%** (starshinova2024chronicsarcoidosisdiagnostic pages 2-3). Ocular complications include posterior uveitis (5–28% of ocular cases), panuveitis (up to 48%), retinal vasculitis (18%), and retinal neovascularization (1–5%) (starshinova2024chronicsarcoidosisdiagnostic pages 14-15).

### 3.3 Onset and course (high-level)
Löfgren syndrome is emphasized as an acute presentation that often resolves: about **80% resolution within 2 years** in one review (weeratunga2024immunemechanismsof pages 1-2). Chronic/progressive disease is described in “approximately **10 to 40%**” in an immunopathogenesis review excerpt (vagts2025immunopathogenesisofsarcoidosis pages 1-2).

### 3.4 Quality of life
Quality-of-life measures are explicitly emphasized in modern care frameworks (e.g., fatigue and health status instruments appear as key outcomes in treatment considerations) (dhanani2025immunosuppressivetherapiesin pages 3-4, dhanani2025immunosuppressivetherapiesin pages 10-12). Disease-associated fatigue is a major patient-reported concern; however, standardized QoL effect sizes were not extractable from the retrieved passages.

### 3.5 HPO term suggestions (non-exhaustive; mapped to retrieved phenotype domains)
* Pulmonary involvement: **HP:0002094 (Dyspnea)**, **HP:0002104 (Pulmonary fibrosis)**, **HP:0006510 (Restrictive ventilatory defect)**.
* Lymphadenopathy: **HP:0002716 (Lymphadenopathy)**.
* Skin: **HP:0000988 (Skin rash)**; granulomatous dermatitis-related terms.
* Eye: **HP:0000554 (Uveitis)**, **HP:0000602 (Retinal vasculitis)**.
* Hypercalcemia: **HP:0003072 (Hypercalcemia)**.

(These are ontology suggestions; frequency and exact mapping should be validated against HPO definitions and organ-specific sarcoidosis cohorts.)

---

## 4. Genetic/Molecular Information

### 4.1 “Causal genes” vs susceptibility genes
Sarcoidosis is generally treated as complex/polygenic rather than a classic monogenic disorder. The retrieved evidence supports **susceptibility and severity loci** (e.g., HLA region, BTNL2, ANXA11, NOTCH4, IL27RA) rather than single-gene causality (casanova2023examinationofeqtl pages 1-3).

### 4.2 Pathogenic variants (status in retrieved evidence)
Specific variant nomenclature (HGVS) and ClinVar classifications were not present in extracted content; therefore, variant-level curation (pathogenic/likely pathogenic/VUS) cannot be completed from this evidence set.

### 4.3 Modifier genes / severity genetics
The integrated eQTL/GWAS severity analysis suggests multiple loci and pathways associated with complicated/progressive disease, emphasizing **innate immunity and MHC class II** involvement (casanova2023examinationofeqtl pages 1-3).

### 4.4 Epigenetic information
No direct methylation/histone modification datasets were extractable from the retrieved excerpts.

---

## 5. Environmental Information

The retrieved sources emphasize possible environmental/occupational and infectious triggers at a conceptual level, but do not provide a curated list of exposures with quantitative risk estimates in the available passages (papanikolaou2025phenotypesandendotypes pages 4-6).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (trigger → granuloma → organ dysfunction)
A coherent mechanistic chain described across sources is:
1) **Triggering antigen/exposure** in a susceptible host →  
2) **Antigen presentation** by macrophages/dendritic cells via **MHC-II** and innate sensing (e.g., TLR-related pathways) →  
3) **CD4+ T-cell polarization and cytokine production** (classically IFN-γ; Th1/Th17/Th17.1) →  
4) **Macrophage differentiation** into epithelioid cells and multinucleated giant cells, organizing granulomas →  
5) Either **resolution** or persistence with **tissue remodeling/fibrosis** and organ impairment (lung restriction, DLCO decline), with potential extrapulmonary damage (vagts2025immunopathogenesisofsarcoidosis pages 1-2, papanikolaou2025phenotypesandendotypes pages 4-6).

### 6.2 Key immune pathways and cell types (with ontology suggestions)
**Dominant immune phenotype:** IFN-γ/Th1 with Th17/Th17.1 contributions (vagts2025immunopathogenesisofsarcoidosis pages 1-2, papanikolaou2025phenotypesandendotypes pages 4-6).

**Granuloma cellular composition:** macrophages/epithelioid cells/giant cells with surrounding lymphocytes; monocytes/neutrophils/fibroblasts can contribute (weeratunga2024immunemechanismsof pages 1-2, kim2024advancesincellular pages 1-5).

**Ontology suggestions:**
* **GO (biological processes):** antigen processing and presentation (MHC class II), T cell activation, cytokine-mediated signaling pathway, granuloma formation, extracellular matrix organization, fibrosis.
* **CL (cell types):** **CL:0000540 (macrophage)**, **CL:0000624 (CD4-positive, alpha-beta T cell)**, fibroblast, dendritic cell.

### 6.3 Recent developments (2023–2024 priority): single-cell / spatial / metabolic mechanisms
**(a) Macrophage metabolic reprogramming and PPP (JCI 2023):** A 2023 JCI study using **single-cell RNA-seq** in sarcoidosis reported an increase of **TREM2-positive macrophages expressing ACE and lysozyme** in cutaneous sarcoidosis granulomas and found macrophages to be “hypermetabolic,” particularly with activation of the **pentose phosphate pathway (PPP)**; PPP enzyme expression (e.g., **FBP1**) was elevated in lesions and serum, and PPP inhibitors attenuated granuloma formation in in vitro and murine models—supporting PPP as a potential therapeutic target (doi:10.1172/jci171088) (dhanani2025immunosuppressivetherapiesin pages 10-12).

**(b) Spatial transcriptomics in muscular sarcoidosis (Cells 2023):** Spatial transcriptomics of two muscular sarcoidosis patients identified transcriptomic clusters spanning granuloma/perigranuloma and surrounding muscle. Granuloma regions showed immune activation (T-lymphocyte and monocyte/macrophage cytokines), while perigranuloma showed extracellular matrix and **TGF-β signaling** signatures. Proximity to granuloma correlated with stronger interferon/TNF/IL-1/IL-4/IL-6 response signatures and fibrotic replacement signals (doi:10.3390/cells12232747) (starshinova2024chronicsarcoidosisdiagnostic pages 26-27).

**(c) High-resolution granuloma interrogation (JCI Review 2024):** A 2024 JCI review highlights that “recent high-resolution studies of the granuloma in situ” using single-cell and spatial methods are clarifying plausible mechanisms in sarcoidosis and enabling comparative analysis with tuberculosis granulomas (doi:10.1172/jci175264) (weeratunga2024immunemechanismsof pages 1-2).

### 6.4 Imaging/biopsy advances linked to mechanism
A 2024 review of imaging and tissue-based methods emphasizes advanced approaches such as **spatial transcriptomics** and MALDI mass spectrometry imaging to map granuloma biochemistry and spatial organization (doi:10.1152/ajpcell.00507.2023) (kim2024advancesincellular pages 1-5).

---

## 7. Anatomical Structures Affected

### 7.1 Organ-level involvement
Most commonly affected: lungs and intrathoracic lymph nodes (up to ~90–95%) (kim2024advancesincellular pages 1-5, baratella2025ctimagingfeatures pages 1-3). Common extrapulmonary targets include skin, eyes, and heart, with neurologic and renal involvement less frequent but clinically high impact (kim2024advancesincellular pages 1-5, starshinova2024chronicsarcoidosisdiagnostic pages 2-3).

### 7.2 UBERON suggestions (non-exhaustive)
* Lung (**UBERON:0002048**)  
* Mediastinal/hilar lymph nodes (regional lymph node structures)  
* Skin (**UBERON:0002097**)  
* Eye (**UBERON:0000970**)  
* Heart (**UBERON:0000948**)  
* Skeletal muscle (**UBERON:0001134**) (muscular sarcoidosis study) (starshinova2024chronicsarcoidosisdiagnostic pages 26-27)

---

## 8. Temporal Development

* **Typical onset:** peaks reported in young adults (20–39 years) in one epidemiology overview (kim2024advancesincellular pages 1-5).  
* **Course patterns:** acute (e.g., Löfgren syndrome) with high spontaneous resolution vs chronic/progressive disease (weeratunga2024immunemechanismsof pages 1-2, vagts2025immunopathogenesisofsarcoidosis pages 1-2).  
* **Fibrosis progression:** a minority develop fibrotic lung disease; CT fibrosis extent is linked to prognosis and thresholds of functional decline are used clinically (baratella2025ctimagingfeatures pages 3-4).

---

## 9. Inheritance and Population

### 9.1 Epidemiology (incidence, prevalence, demographics)
**Population ranges and geographic variation:**
* Reported prevalence ~**4.7–64 per 100,000** and incidence ~**1–35.5 per 100,000/year** in a recent registry paper’s contextual epidemiology discussion (guttmannducke2025firstinsightsand pages 1-2).  
* Marked geographic differences: Scandinavia/UK ~**64 per 100,000** and African American populations ~**39 per 100,000**, compared with South Korea **4.67** and Japan **3.7 per 100,000** (kim2024advancesincellular pages 1-5).

**Example real-world registry demographics:**
* Vienna registry (2022–2023; n=199): mean age 52±13, women 57.5%; chest X-ray stage distribution 1:34.5%, 2:46%, 3:9.5%, 4:6% (guttmannducke2025firstinsightsand pages 1-2).

### 9.2 Genetic architecture / inheritance
Evidence supports **polygenic susceptibility** (HLA and non-HLA loci), rather than Mendelian inheritance, consistent with multifactorial disease (casanova2023examinationofeqtl pages 1-3).

---

## 10. Diagnostics

### 10.1 Diagnostic criteria (core consensus)
A 2024 review explicitly states diagnosis is based on **three main criteria**: (1) clinical presentation, (2) **histologic detection of non-caseating granulomas** in ≥1 tissue sample, and (3) **exclusion** of alternative granulomatous diseases (starshinova2024chronicsarcoidosisdiagnostic pages 2-3). A 2025 PET/CT meta-analysis similarly describes accepted diagnosis requiring compatible clinical picture, radiologic evidence, and histologic demonstration of non-necrotising granulomatous disease (donnelly2025metaanalysisof[18f]fdgpetct pages 1-2).

### 10.2 Histopathology
Granulomas are composed largely of macrophage-derived epithelioid and giant cells with surrounding lymphocytes (kim2024advancesincellular pages 1-5, starshinova2024chronicsarcoidosisdiagnostic pages 14-15).

### 10.3 Laboratory tests / biomarkers
Supportive biomarkers include:
* **Serum ACE** (produced by monocytes/macrophages/epithelioid cells) reported to correlate with granuloma burden and radiologic stages II–III and may reflect activity/extrathoracic involvement (starshinova2024chronicsarcoidosisdiagnostic pages 15-17, starshinova2024chronicsarcoidosisdiagnostic pages 14-15).  
* **Soluble IL-2 receptor (sIL-2R)** as a marker of Th1 activation; may predict progression/relapse (starshinova2024chronicsarcoidosisdiagnostic pages 15-17).  
* Hypercalcemia with low PTH and normal/low 25-hydroxyvitamin D can occur (starshinova2024chronicsarcoidosisdiagnostic pages 15-17, starshinova2024chronicsarcoidosisdiagnostic pages 14-15).

BAL findings may show lymphocytosis (>15%) and **CD4/CD8 ≥3.5** but are not specific (starshinova2024chronicsarcoidosisdiagnostic pages 15-17).

### 10.4 Imaging
**HRCT:** preferred over CXR for sensitivity and evaluation of complications (baratella2025ctimagingfeatures pages 3-4, baratella2025ctimagingfeatures pages 1-3).  
**FDG-PET/CT:** a 2025 meta-analysis (search through Sep 2023) reported pooled sensitivity **0.971** and specificity **0.873** for suspected pulmonary sarcoidosis; SUVmax reduction correlated with improved FVC and DLCO and may help guide immunosuppression decisions (doi:10.1007/s00330-024-10949-4) (donnelly2025metaanalysisof[18f]fdgpetct pages 1-2).  

### 10.5 Differential diagnosis
Imaging reviews stress differentiation from tuberculosis, silicosis, malignancy, organizing pneumonia, hypersensitivity pneumonitis, etc., and emphasize integrating clinical/radiologic/pathologic evidence with exclusion of alternatives (baratella2025ctimagingfeatures pages 1-3).

---

## 11. Outcome / Prognosis

### 11.1 Mortality and survival (recent real-world estimates)
A 2024 population-based cohort study (Clalit Health Services; incident cases 2000–2016) reported higher mortality in sarcoidosis than controls (**17.7% vs 10.6%**), with adjusted all-cause mortality **HR 1.79** (95% CI 1.64–1.96) and the highest hazard in the **first year post-diagnosis** (patt2024elevatedmortalityrisk pages 1-2). Another excerpt reports first-year multivariable HR **2.99** (95% CI 2.39–3.75), and persistent but lower hazards thereafter (patt2024elevatedmortalityrisk pages 8-9). Predictors included age at diagnosis, male sex, and comorbidity burden (patt2024elevatedmortalityrisk pages 1-2, patt2024elevatedmortalityrisk pages 8-9).

### 11.2 Prognostic functional markers
Imaging-focused reviews highlight functional thresholds associated with progression/response such as ≥5% decline in FVC and ≥10% decline in DLCO, and note that fibrosis extent (e.g., >20% parenchymal fibrosis on CT) correlates with worse outcomes (baratella2025ctimagingfeatures pages 3-4).

---

## 12. Treatment

### 12.1 Current standard pharmacotherapy (guideline-aligned approach)
A practical evidence-based review states oral glucocorticoids remain first-line for symptomatic pulmonary sarcoidosis (typical starting prednisone **20–40 mg/day**) with tapering over **6–18 months** guided by response; steroid-sparing agents are often required due to toxicity (doi:10.3390/jcm14196828) (dhanani2025immunosuppressivetherapiesin pages 1-3). Second-line agents include **methotrexate** (preferred), azathioprine, leflunomide, and mycophenolate; refractory disease options include anti-TNF agents (infliximab, adalimumab) and emerging approaches such as JAK inhibitors, rituximab, and repository corticotropin injection (RCI) (dhanani2025immunosuppressivetherapiesin pages 3-4, dhanani2025immunosuppressivetherapiesin pages 10-12).

**MAXO suggestions (non-exhaustive):** glucocorticoid therapy; methotrexate therapy; TNF inhibitor therapy; antifibrotic therapy; immunosuppressive therapy; JAK inhibitor therapy.

### 12.2 Recent developments (high-priority evidence)
**Methotrexate as first-line alternative (NEJM 2025):** In the PREDMETH noninferiority trial (NCT04314193), methotrexate was **noninferior** to prednisone for 24-week improvement in % predicted FVC (+6.11 vs +6.75 points); adverse event profiles differed (doi:10.1056/NEJMoa2501443) (kahlmann2025firstlinetreatmentof pages 1-2). This is a major development supporting steroid-minimizing strategies.

### 12.3 Biologics and advanced immunomodulators
**Infliximab (anti-TNF):** ClinicalTrials.gov record NCT00073437 describes a multicenter Phase 3 randomized, double-blind, placebo-controlled trial (n=139) assessing infliximab (3 or 5 mg/kg) with primary endpoint change in % predicted FVC at week 24, and cites associated publications including **PMID 16840744** and **PMID 18256069** (NCT00073437 chunk 1).  
**Adalimumab:** NCT00311246 (progressive sarcoidosis; n=11) used adalimumab 40 mg SC weekly; primary endpoint was change in FVC from screening to week 24 (NCT00311246 chunk 2).

### 12.4 Antifibrotics / progressive fibrotic sarcoidosis trials
**Pirfenidone:** NCT03260556 is a Phase 4 randomized, triple-masked placebo-controlled trial (estimated n=60) in progressive fibrotic sarcoidosis; primary endpoint “time until clinical worsening” over two years (NCT03260556 chunk 1).  
**Nintedanib:** NCT06479603 is recruiting and compares nintedanib vs standard of care in fibrotic sarcoidosis; the provided chunk includes fibrosis-based inclusion criteria but does not show endpoints/phase/enrollment in that excerpt (NCT06479603 chunk 2).

### 12.5 Efzofitimod (ATYR1923) — steroid-sparing investigational therapy
NCT03824392 is a completed early study of IV ATYR1923/efzofitimod; registry chunk cites related publications including **PMID 37854715** and **PMID 36356657** (NCT03824392 chunk 2). (Detailed endpoints/phase are not present in the extracted chunk.)

---

## 13. Prevention

No disease-specific primary prevention strategies were identified in the retrieved sources. Prevention in practice centers on (i) avoiding unnecessary immunosuppression in self-limited disease, (ii) monitoring and mitigating treatment complications, and (iii) addressing exposure hypotheses where relevant, but quantitative prevention evidence was not extractable from the provided texts.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary sarcoidosis analogs were identified in the retrieved evidence set.

---

## 15. Model Organisms

The PPP/macrophage study reports both **in vitro giant cell** and **in vivo murine granuloma models** in which PPP inhibitors attenuated granuloma formation, supporting tractable experimental models for granulomatous inflammation and therapeutic targeting (dhanani2025immunosuppressivetherapiesin pages 10-12). Additional organism-specific model catalogs (MGI/IMPC) were not retrieved in this run.

---

## Expert opinions and authoritative analysis (from high-authority sources)
* The JCI 2024 review frames sarcoidosis as a “complex immune-mediated disease characterized by clusters of immune cells called granulomas” and emphasizes insights emerging from high-resolution single-cell/spatial studies (doi:10.1172/jci175264) (weeratunga2024immunemechanismsof pages 1-2).  
* The immunopathogenesis review emphasizes an IFN-γ/Th1–Th17 axis and dysregulated innate–adaptive crosstalk as central drivers of granuloma persistence and fibrotic progression (doi:10.1055/a-2716-5737) (vagts2025immunopathogenesisofsarcoidosis pages 1-2).  
* The NEJM 2025 PREDMETH trial provides the strongest recent clinical evidence supporting methotrexate as an initial therapy option with comparable short-term lung function improvement to prednisone (doi:10.1056/NEJMoa2501443) (kahlmann2025firstlinetreatmentof pages 1-2).

---

## Key gaps and limitations of this evidence set
* Several requested identifier systems (MeSH, ICD-11, Orphanet, OMIM disease entry) were not present in the retrieved texts and cannot be reliably asserted without dedicated database queries.  
* Variant-level (ClinVar/ACMG) pathogenic variant curation is not possible from the extracted passages.  
* Some trial details for efzofitimod Phase 3 (NCT05415137), tofacitinib trials, and the nintedanib record endpoints were not contained in the retrieved chunks; additional ClinicalTrials.gov sections would be required for full endpoint extraction.


References

1. (vagts2025immunopathogenesisofsarcoidosis pages 1-2): Christen Vagts, Christian Ascoli, and Jeffrey R. Jacobson. Immunopathogenesis of sarcoidosis. Seminars in Respiratory and Critical Care Medicine, 46:543-556, Nov 2025. URL: https://doi.org/10.1055/a-2716-5737, doi:10.1055/a-2716-5737. This article has 1 citations and is from a peer-reviewed journal.

2. (starshinova2024chronicsarcoidosisdiagnostic pages 2-3): Anna Starshinova, Elizaveta Berg, Artem Rubinstein, Anastasia Kulpina, Igor Kudryavtsev, and Dmitry Kudlay. Chronic sarcoidosis: diagnostic difficulties and search for new criteria of inflammatory activity (a case report and literature review). Journal of Clinical Medicine, 13:6974, Nov 2024. URL: https://doi.org/10.3390/jcm13226974, doi:10.3390/jcm13226974. This article has 5 citations.

3. (he2025globalburdenof pages 1-2): Xiaoshuang He, Lu Wang, Yu Zhao, Yuanyuan Qu, Wenyan Xin, Lina Xu, Wanyu Li, and Chao Wu. Global burden of disease of interstitial lung disease and pulmonary sarcoidosis in adolescents and young adults (1990–2019), and projections for the next 30 years. European Journal of Medical Research, Sep 2025. URL: https://doi.org/10.1186/s40001-025-03141-x, doi:10.1186/s40001-025-03141-x. This article has 1 citations and is from a peer-reviewed journal.

4. (kim2024advancesincellular pages 1-5): Junwoo Kim, Girish Dwivedi, Berin A. Boughton, Ankur Sharma, and Silvia Lee. Advances in cellular and tissue-based imaging techniques for sarcoid granulomas. American Journal of Physiology-Cell Physiology, 326:C10-C26, Jan 2024. URL: https://doi.org/10.1152/ajpcell.00507.2023, doi:10.1152/ajpcell.00507.2023. This article has 8 citations.

5. (papanikolaou2025phenotypesandendotypes pages 4-6): Ilias C. Papanikolaou, Konstantinos Chytopoulos, Dimitrios Kaitatzis, Nikolaos Kostakis, Anastasios Bogiatzis, Paschalis Steiropoulos, and Fotios Drakopanagiotakis. Phenotypes and endotypes in sarcoidosis: unraveling prognosis and disease course. Biomedicines, 13:287, Jan 2025. URL: https://doi.org/10.3390/biomedicines13020287, doi:10.3390/biomedicines13020287. This article has 6 citations.

6. (donnelly2025metaanalysisof[18f]fdgpetct pages 1-2): Ryan Donnelly, Michael McDermott, Gerry McManus, Alessandro N. Franciosi, Michael P. Keane, Emmet E. McGrath, Cormac McCarthy, and David J. Murphy. Meta-analysis of [18f]fdg-pet/ct in pulmonary sarcoidosis. European Radiology, 35:2222-2232, Jul 2025. URL: https://doi.org/10.1007/s00330-024-10949-4, doi:10.1007/s00330-024-10949-4. This article has 25 citations and is from a domain leading peer-reviewed journal.

7. (starshinova2024chronicsarcoidosisdiagnostic pages 14-15): Anna Starshinova, Elizaveta Berg, Artem Rubinstein, Anastasia Kulpina, Igor Kudryavtsev, and Dmitry Kudlay. Chronic sarcoidosis: diagnostic difficulties and search for new criteria of inflammatory activity (a case report and literature review). Journal of Clinical Medicine, 13:6974, Nov 2024. URL: https://doi.org/10.3390/jcm13226974, doi:10.3390/jcm13226974. This article has 5 citations.

8. (guttmannducke2025firstinsightsand pages 1-2): Claudia Guttmann-Ducke, Martin Lutnik, Maximilian Robert Gysan, Pavla Sarova, Christopher Milacek, Christina Bal, Wolfgang Graninger, Helmut Prosch, Daniela Gompelmann, and Marco Idzko. First insights and future research perspectives from the sarcoidosis registry at the medical university of vienna. Scientific Reports, Mar 2025. URL: https://doi.org/10.1038/s41598-025-93708-9, doi:10.1038/s41598-025-93708-9. This article has 1 citations and is from a peer-reviewed journal.

9. (guttmannducke2025firstinsightsand pages 2-3): Claudia Guttmann-Ducke, Martin Lutnik, Maximilian Robert Gysan, Pavla Sarova, Christopher Milacek, Christina Bal, Wolfgang Graninger, Helmut Prosch, Daniela Gompelmann, and Marco Idzko. First insights and future research perspectives from the sarcoidosis registry at the medical university of vienna. Scientific Reports, Mar 2025. URL: https://doi.org/10.1038/s41598-025-93708-9, doi:10.1038/s41598-025-93708-9. This article has 1 citations and is from a peer-reviewed journal.

10. (patt2024elevatedmortalityrisk pages 1-2): Yonatan Shneor Patt, Kassem Sharif, Paula David, Or Hen, Omer Gendelman, Yoav Elizur, Basel Ahmaro, Orly Weinstein, Abdulla Watad, Howard Amital, and Niv Ben-Shabat. Elevated mortality risk in the first year post-diagnosis of sarcoidosis: a comprehensive population-based cohort study. Medicina, 60:1787, Nov 2024. URL: https://doi.org/10.3390/medicina60111787, doi:10.3390/medicina60111787. This article has 3 citations.

11. (patt2024elevatedmortalityrisk pages 8-9): Yonatan Shneor Patt, Kassem Sharif, Paula David, Or Hen, Omer Gendelman, Yoav Elizur, Basel Ahmaro, Orly Weinstein, Abdulla Watad, Howard Amital, and Niv Ben-Shabat. Elevated mortality risk in the first year post-diagnosis of sarcoidosis: a comprehensive population-based cohort study. Medicina, 60:1787, Nov 2024. URL: https://doi.org/10.3390/medicina60111787, doi:10.3390/medicina60111787. This article has 3 citations.

12. (patt2024elevatedmortalityrisk pages 9-11): Yonatan Shneor Patt, Kassem Sharif, Paula David, Or Hen, Omer Gendelman, Yoav Elizur, Basel Ahmaro, Orly Weinstein, Abdulla Watad, Howard Amital, and Niv Ben-Shabat. Elevated mortality risk in the first year post-diagnosis of sarcoidosis: a comprehensive population-based cohort study. Medicina, 60:1787, Nov 2024. URL: https://doi.org/10.3390/medicina60111787, doi:10.3390/medicina60111787. This article has 3 citations.

13. (weeratunga2024immunemechanismsof pages 1-2): Praveen Weeratunga, David R. Moller, and Ling-Pei Ho. Immune mechanisms of granuloma formation in sarcoidosis and tuberculosis. The Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci175264, doi:10.1172/jci175264. This article has 84 citations.

14. (dhanani2025immunosuppressivetherapiesin pages 10-12): Zehra Dhanani and Rohit Gupta. Immunosuppressive therapies in pulmonary sarcoidosis: a practical, evidence-based review. Journal of Clinical Medicine, 14:6828, Sep 2025. URL: https://doi.org/10.3390/jcm14196828, doi:10.3390/jcm14196828. This article has 2 citations.

15. (starshinova2024chronicsarcoidosisdiagnostic pages 26-27): Anna Starshinova, Elizaveta Berg, Artem Rubinstein, Anastasia Kulpina, Igor Kudryavtsev, and Dmitry Kudlay. Chronic sarcoidosis: diagnostic difficulties and search for new criteria of inflammatory activity (a case report and literature review). Journal of Clinical Medicine, 13:6974, Nov 2024. URL: https://doi.org/10.3390/jcm13226974, doi:10.3390/jcm13226974. This article has 5 citations.

16. (starshinova2024chronicsarcoidosisdiagnostic pages 15-17): Anna Starshinova, Elizaveta Berg, Artem Rubinstein, Anastasia Kulpina, Igor Kudryavtsev, and Dmitry Kudlay. Chronic sarcoidosis: diagnostic difficulties and search for new criteria of inflammatory activity (a case report and literature review). Journal of Clinical Medicine, 13:6974, Nov 2024. URL: https://doi.org/10.3390/jcm13226974, doi:10.3390/jcm13226974. This article has 5 citations.

17. (baratella2025ctimagingfeatures pages 3-4): Elisa Baratella, Valeria di Luca, Alessandra Oliva, Ilaria Fiorese, Antonio Segalotti, Marina Troian, Stefano Lovadina, Barbara Ruaro, Francesco Salton, Roberta Polverosi, and Maria Assunta Cova. Ct imaging features of pulmonary sarcoidosis: typical and atypical radiological features and their differential diagnosis. Medicina, 61:2094, Nov 2025. URL: https://doi.org/10.3390/medicina61122094, doi:10.3390/medicina61122094. This article has 1 citations.

18. (baratella2025ctimagingfeatures pages 1-3): Elisa Baratella, Valeria di Luca, Alessandra Oliva, Ilaria Fiorese, Antonio Segalotti, Marina Troian, Stefano Lovadina, Barbara Ruaro, Francesco Salton, Roberta Polverosi, and Maria Assunta Cova. Ct imaging features of pulmonary sarcoidosis: typical and atypical radiological features and their differential diagnosis. Medicina, 61:2094, Nov 2025. URL: https://doi.org/10.3390/medicina61122094, doi:10.3390/medicina61122094. This article has 1 citations.

19. (dhanani2025immunosuppressivetherapiesin pages 12-13): Zehra Dhanani and Rohit Gupta. Immunosuppressive therapies in pulmonary sarcoidosis: a practical, evidence-based review. Journal of Clinical Medicine, 14:6828, Sep 2025. URL: https://doi.org/10.3390/jcm14196828, doi:10.3390/jcm14196828. This article has 2 citations.

20. (dhanani2025immunosuppressivetherapiesin pages 3-4): Zehra Dhanani and Rohit Gupta. Immunosuppressive therapies in pulmonary sarcoidosis: a practical, evidence-based review. Journal of Clinical Medicine, 14:6828, Sep 2025. URL: https://doi.org/10.3390/jcm14196828, doi:10.3390/jcm14196828. This article has 2 citations.

21. (dhanani2025immunosuppressivetherapiesin pages 1-3): Zehra Dhanani and Rohit Gupta. Immunosuppressive therapies in pulmonary sarcoidosis: a practical, evidence-based review. Journal of Clinical Medicine, 14:6828, Sep 2025. URL: https://doi.org/10.3390/jcm14196828, doi:10.3390/jcm14196828. This article has 2 citations.

22. (kahlmann2025firstlinetreatmentof pages 1-2): Vivienne Kahlmann, Montse Janssen Bonás, Catharina C. Moor, Jan C. Grutters, Rémy L.M. Mostard, Henricus N.A.J. van Rijswijk, Jan van der Maten, Emiel R. Marges, Linda A.A. Moonen, Maria J. Overbeek, Bart Koopman, Daan W. Loth, Esther J. Nossent, Michiel Wagenaar, Henk Kramer, Pascal L.M.L. Wielders, Peter I. Bonta, Stefan Walen, Brigitte A.H.A. Bogaarts, René Kerstens, Mayka Overgaauw, Marcel Veltkamp, and Marlies S. Wijsenbeek. First-line treatment of pulmonary sarcoidosis with prednisone or methotrexate. New England Journal of Medicine, 393:231-242, Jul 2025. URL: https://doi.org/10.1056/nejmoa2501443, doi:10.1056/nejmoa2501443. This article has 53 citations and is from a highest quality peer-reviewed journal.

23. (NCT00073437 chunk 1):  A Study of Infliximab in Patients With Sarcoidosis. Centocor, Inc.. 2003. ClinicalTrials.gov Identifier: NCT00073437

24. (NCT00311246 chunk 2):  Trial of Adalimumab in Progressive Sarcoidosis. University of Chicago. 2006. ClinicalTrials.gov Identifier: NCT00311246

25. (NCT03824392 chunk 2):  Study of Intravenous ATYR1923 (Efzofitimod) for Pulmonary Sarcoidosis. aTyr Pharma, Inc.. 2019. ClinicalTrials.gov Identifier: NCT03824392

26. (NCT03260556 chunk 1): Robert P Baughman. Pirfenidone for Progressive Fibrotic Sarcoidosis. University of Cincinnati. 2017. ClinicalTrials.gov Identifier: NCT03260556

27. (NCT06479603 chunk 2): Sahajal Dhooria. RCT of Nintedanib in Fibrotic Sarcoidosis. Post Graduate Institute of Medical Education and Research, Chandigarh. 2024. ClinicalTrials.gov Identifier: NCT06479603

28. (patt2024elevatedmortalityrisk pages 2-3): Yonatan Shneor Patt, Kassem Sharif, Paula David, Or Hen, Omer Gendelman, Yoav Elizur, Basel Ahmaro, Orly Weinstein, Abdulla Watad, Howard Amital, and Niv Ben-Shabat. Elevated mortality risk in the first year post-diagnosis of sarcoidosis: a comprehensive population-based cohort study. Medicina, 60:1787, Nov 2024. URL: https://doi.org/10.3390/medicina60111787, doi:10.3390/medicina60111787. This article has 3 citations.

29. (casanova2023examinationofeqtl pages 1-3): Nancy G Casanova, S. Camp, Manuel L Gonzalez-Garay, Ken Batai, Lori Garman, Courtney G Montgomery, Nathan Ellis, Rick A. Kittles, C. Bime, Amy P. Hsu, Steven M. Holland, Yves A. Lussier, J. Karnes, N. Sweiss, Lisa A Maier, L. Koth, David R Moller, N. Kaminski, and Joe G. N. Garcia. Examination of eqtl polymorphisms associated with increased risk of progressive complicated sarcoidosis in european and african descent subjects. European journal of respiratory medicine, 5:359-371, Dec 2023. URL: https://doi.org/10.31488/ejrm.137, doi:10.31488/ejrm.137. This article has 2 citations.