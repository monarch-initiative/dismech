---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T18:16:20.714731'
end_time: '2026-04-24T18:25:03.703417'
duration_seconds: 522.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: UNC13A-Related Congenital NDD with Epilepsy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** UNC13A-Related Congenital NDD with Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **UNC13A-Related Congenital NDD with Epilepsy** covering all of the
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
- **Disease Name:** UNC13A-Related Congenital NDD with Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **UNC13A-Related Congenital NDD with Epilepsy** covering all of the
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


# UNC13A-Related Congenital Neurodevelopmental Disorder (NDD) with Epilepsy — Research Report

## Executive summary
Biallelic loss-of-function (LoF) variants in **UNC13A** (encoding the presynaptic priming factor **Munc13-1**) cause a severe, congenital-onset disorder characterized by profound neurodevelopmental impairment (congenital encephalopathy), epileptiform EEG activity/epileptic encephalopathy, and a prominent **presynaptic neuromuscular transmission defect** (a “LEMS-like” congenital myasthenic syndrome phenotype) often complicated by respiratory failure and early death (engel2016lossofmunc131 pages 1-2, mullins2022homozygousunc13avariant pages 2-4). Published human evidence in this run includes (i) a 2016 Neurology Genetics case (Engel et al.) and (ii) a 2022 Cureus case with detailed neuropathology (Mullins et al.), both with biallelic truncating/frameshift variants (engel2016lossofmunc131 pages 1-2, mullins2022homozygousunc13avariant pages 2-4). Recent (2023–2024) sources retrieved here are **reviews** providing current understanding of presynaptic/synaptic disorders and clinical context (not new UNC13A congenital case expansions) (scorrano2024exploringthelandscape pages 1-2, ohno2023clinicalandpathologic pages 1-3, pugliese2023presynapticcongenitalmyasthenic pages 1-3).

*Important limitation:* In the retrieved full texts/snippets for this run, **no OMIM/Orphanet/MONDO/ICD identifiers** were explicitly stated for this specific entity, and therefore cannot be reliably reported without additional database retrieval beyond the provided tools/evidence (asadollahi2025pathogenicunc13avariants pages 1-2, engel2016lossofmunc131 pages 1-2, mullins2022homozygousunc13avariant pages 2-4).

---

## 1. Disease information
### 1.1 Overview (what is the disease?)
**UNC13A-related congenital NDD with epilepsy** is best supported (from available primary reports) as an **autosomal recessive** disorder due to **biallelic truncating/LoF** UNC13A variants, presenting with:
- **Congenital encephalopathy** / severe global neurodevelopmental impairment
- **Cortical hyperexcitability** (epileptiform EEG and/or epileptic encephalopathy)
- **Severe presynaptic neuromuscular transmission failure** (congenital myasthenic syndrome-like), with respiratory complications and high mortality (engel2016lossofmunc131 pages 1-2, mullins2022homozygousunc13avariant pages 2-4).

**Primary literature abstract support (direct quote):** Engel et al. report a “*fatal syndrome of microcephaly, cortical hyperexcitability, and myasthenia*” due to “*a homozygous nonsense mutation … of MUNC13-1 (UNC13A)*” (engel2016lossofmunc131 pages 1-2).

### 1.2 Synonyms / alternative names (as used in the retrieved literature)
The primary reports used descriptive labels rather than a standardized disease name:
- “**Loss of MUNC13-1 function**” syndrome; “**fatal syndrome of microcephaly, cortical hyperexcitability, and myasthenia**” (Engel 2016) (engel2016lossofmunc131 pages 1-2)
- “**Congenital encephalopathy and severe neuromuscular phenotype**” with epileptic encephalopathy (Mullins 2022) (mullins2022homozygousunc13avariant pages 2-4)
- In broader mechanistic/clinical reviews, UNC13A is listed among genes relevant to **SNARE machinery** and **congenital myasthenic syndromes (CMS)** (cali2022epilepticphenotypesassociated pages 1-2, ohno2023clinicalandpathologic pages 1-3).

### 1.3 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
No OMIM/Orphanet/MONDO/ICD/MeSH identifiers were present in the retrieved excerpts for the congenital UNC13A condition (asadollahi2025pathogenicunc13avariants pages 1-2, engel2016lossofmunc131 pages 1-2, mullins2022homozygousunc13avariant pages 2-4). 

**Ontology suggestion:** If a MONDO term is required for a knowledge base, it will likely need to be created/mapped by curators from primary reports (Engel 2016; Mullins 2022) rather than extracted from the current retrieved texts.

### 1.4 Evidence source type
- **Human primary evidence:** single-patient case report with extensive NMJ physiology/ultrastructure (2016) and single-patient case report with detailed neuropathology (2022) (engel2016lossofmunc131 pages 1-2, mullins2022homozygousunc13avariant pages 2-4).
- **Aggregated/secondary evidence:** 2023 CMS comprehensive review, 2023 presynaptic CMS review, and 2024 synaptopathy review (ohno2023clinicalandpathologic pages 1-3, pugliese2023presynapticcongenitalmyasthenic pages 1-3, scorrano2024exploringthelandscape pages 1-2).

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** germline **loss-of-function** UNC13A variants disrupting synaptic vesicle priming and neurotransmitter release at both the **neuromuscular junction** and CNS synapses.
- Engel et al. identified a **homozygous nonsense** variant **c.304C>T (p.Gln102*)** truncating Munc13-1 to 101/1703 amino acids (engel2016lossofmunc131 pages 3-5).
- Mullins et al. report a **homozygous frameshift** **c.1188delC (p.Asp397Thrfs*107)** (mullins2022homozygousunc13avariant pages 2-4).

**Mechanistic framing (direct quote from Engel abstract):** “*Loss of Munc13-1 function predicts that syntaxin 1B is consigned to a nonfunctional closed state; this inhibits cholinergic transmission at the neuromuscular junction and glutamatergic transmission in the brain.*” (engel2016lossofmunc131 pages 1-2).

### 2.2 Risk factors
- **Genetic risk:** parental consanguinity increases the likelihood of homozygosity for rare UNC13A LoF alleles; the 2022 case explicitly reports parents as distant cousins (mullins2022homozygousunc13avariant pages 1-2).
- No environmental, infectious, or lifestyle risk factors were described in the retrieved primary reports.

### 2.3 Protective factors / gene–environment interactions
No protective factors or gene–environment interactions were reported in the retrieved evidence.

---

## 3. Phenotypes
### 3.1 Core phenotype spectrum (from primary cases)
Below is a consolidated phenotype list supported by the two biallelic LoF cases in this run.

#### Neurologic / developmental
- **Congenital hypotonia** and severe developmental impairment (Engel: hypotonic at birth; later unable to sit; limited speech) (engel2016lossofmunc131 pages 1-2, engel2016lossofmunc131 pages 2-3).
- **Microcephaly** (Engel) (engel2016lossofmunc131 pages 2-3).
- **Epileptiform EEG / cortical hyperexcitability**: Engel described EEG abnormalities with multifocal sharp waves and periodic sharp-wave trains without overt seizures (engel2016lossofmunc131 pages 2-3); Mullins described **infantile spasms** with **burst-suppression** pattern (mullins2022homozygousunc13avariant pages 2-4).

#### Neuromuscular / respiratory
- **LEMS-like presynaptic transmission defect** with low CMAP amplitudes, decrement on stimulation, and marked facilitation with rapid stimulation (engel2016lossofmunc131 pages 2-3).
- Feeding difficulties (weak suck/gag in Mullins; gastrostomy/gastric tube/Nissen fundoplasty in Engel) (mullins2022homozygousunc13avariant pages 1-2, engel2016lossofmunc131 pages 2-3).
- Respiratory compromise, aspiration pneumonia; eventual ventilator dependence in Engel (engel2016lossofmunc131 pages 2-3).

#### Neuroimaging / neuropathology
- Engel MRI showed **thin corpus callosum** (engel2016lossofmunc131 pages 2-3, engel2016lossofmunc131 media ceed3256).
- Mullins autopsy brain findings included open Sylvian fissures, blunted lobes, vertical hippocampus, absent subcortical U-fibers, and synuclein-positive axonal spheroids (mullins2022homozygousunc13avariant pages 2-4, mullins2022homozygousunc13avariant pages 4-5).

### 3.2 Phenotype characteristics (onset, severity, course)
- **Onset:** congenital/neonatal (Engel: symptomatic from birth; Mullins: congenital encephalopathy) (engel2016lossofmunc131 pages 1-2, mullins2022homozygousunc13avariant pages 1-2).
- **Severity:** severe/profound.
- **Course:** complicated by infections/respiratory failure; death in infancy or early childhood in both reports (8 months in Mullins; 50 months in Engel) (mullins2022homozygousunc13avariant pages 2-4, engel2016lossofmunc131 pages 2-3).

### 3.3 Quantitative data (recent studies)
While case counts are very small in the congenital biallelic LoF form in this run, Engel provides quantitative electrophysiology demonstrating profound presynaptic failure:
- MEPP frequency in 5 mM K+ (patient): **0.23/min** vs controls **10.7/min**
- MEPP frequency in 20 mM K+ (patient): **0.48/min** vs controls **173/min**
- Quantal content of EPP at 1 Hz (patient): **0.89** vs 6-month control **14.7**
- Readily releasable quanta n (patient): **7.5** vs 6-month control **72**
- Probability of release p: **normal (0.14)** (engel2016lossofmunc131 pages 3-5, engel2016lossofmunc131 media ceed3256).

### 3.4 Suggested HPO terms
(ontology suggestions; not explicitly listed in sources)
- Seizures: **Infantile spasms** (HP:0012469), **Epileptic encephalopathy** (HP:0200134)
- EEG burst suppression: **Burst suppression** (HP:0010855)
- Abnormal EEG: **Abnormality of EEG** (HP:0002353)
- Microcephaly: **Microcephaly** (HP:0000252)
- Hypotonia: **Hypotonia** (HP:0001252)
- Feeding difficulty: **Feeding difficulties** (HP:0011968)
- Respiratory failure: **Respiratory insufficiency** (HP:0002093)
- Myasthenic symptoms: **Abnormality of neuromuscular junction** (HP:0003201) (broad)
- Thin corpus callosum: **Thin corpus callosum** (HP:0033725) (if available in HPO; otherwise “Abnormal corpus callosum morphology” HP:0001273)

---

## 4. Genetic / molecular information
### 4.1 Causal gene
- **UNC13A** (encodes Munc13-1), a key presynaptic protein required for **synaptic vesicle docking/priming** and SNARE complex function (engel2016lossofmunc131 pages 1-2).

### 4.2 Pathogenic variants (from primary reports in this run)
- **UNC13A c.304C>T (p.Gln102*)**, homozygous nonsense; truncates after 101 aa; not listed in ExAC at time of report; parents heterozygous (engel2016lossofmunc131 pages 3-5).
- **UNC13A c.1188delC (p.Asp397Thrfs*107)**, homozygous frameshift; parents distant cousins (mullins2022homozygousunc13avariant pages 2-4).

**Variant type/class:** truncating LoF (nonsense/frameshift) consistent with **autosomal recessive** inheritance in these congenital, severe cases (engel2016lossofmunc131 pages 3-5, mullins2022homozygousunc13avariant pages 2-4).

### 4.3 Functional consequences
Engel et al. emphasize that Munc13-1 interacts with syntaxin 1B to promote an open conformation needed for primed SNARE complexes and exocytosis (engel2016lossofmunc131 pages 1-2). Their conclusion links LoF to impaired CNS and NMJ transmission (engel2016lossofmunc131 pages 1-2).

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes, epigenetic signatures, or chromosomal abnormalities were reported for this congenital condition in the retrieved evidence.

---

## 5. Environmental information
No disease-specific environmental/lifestyle/infectious triggers or modifiers were described in the primary congenital UNC13A LoF cases retrieved here.

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (UNC13A LoF → synaptic failure → clinical phenotype)
**Upstream trigger:** biallelic UNC13A truncating variants → marked loss of functional Munc13-1.

**Molecular/cellular mechanism:** impaired Munc13-1 function disrupts opening of syntaxin 1B and assembly/priming of SNARE complexes required for vesicle exocytosis; physiologically this manifests as profound depletion of the readily releasable vesicle pool (engel2016lossofmunc131 pages 1-2, engel2016lossofmunc131 pages 3-5).

**System-level consequences:**
- NMJ: markedly reduced MEPP frequency and quantal content with normal release probability → severe neuromuscular weakness and LEMS-like electrophysiology (engel2016lossofmunc131 pages 3-5, engel2016lossofmunc131 media ceed3256).
- CNS: abnormal cortical electrical activity/epileptiform EEG and structural brain findings (microcephaly; thin corpus callosum; neuropathologic malformations) (engel2016lossofmunc131 pages 2-3, mullins2022homozygousunc13avariant pages 2-4).

### 6.2 Pathways / ontology suggestions
- **Pathway/complex:** SNARE-mediated synaptic vesicle exocytosis (contextualized in “SNAREopathies” review) (cali2022epilepticphenotypesassociated pages 1-2).
- **Suggested GO Biological Process terms:** neurotransmitter secretion; synaptic vesicle priming; regulated exocytosis; synaptic transmission.
- **Suggested CL (cell types):** motor neuron (CL:0000100), cortical glutamatergic neuron (broad), cerebellar Purkinje cell (CL:0000121).

### 6.3 Expert synthesis from authoritative reviews (2023–2024)
- CMS review (Ohno et al., 2023) frames CMS as NMJ transmission disorders due to germline variants, noting that diagnosis requires electrophysiology and genetic testing, and discusses therapeutic classes used across CMS (ohno2023clinicalandpathologic pages 1-3).
- Presynaptic CMS review (Pugliese et al., 2023) notes presynaptic CMS can present prenatally/neonatally with severe phenotypes including developmental delay and apnoeic crises and that animal models are used to study mechanisms and treatment testing (pugliese2023presynapticcongenitalmyasthenic pages 1-3).
- Synaptopathy review (Scorrano et al., 2024) summarizes NGS-driven discovery of synaptic gene variants and uses UNC13A as an example among presynaptic genes in pediatric epilepsy/NDD contexts (scorrano2024exploringthelandscape pages 1-2).

---

## 7. Anatomical structures affected
### 7.1 Primary organs/systems
- **Nervous system** (central) (EEG abnormalities; microcephaly; brain malformations/pathology) (engel2016lossofmunc131 pages 2-3, mullins2022homozygousunc13avariant pages 4-5).
- **Neuromuscular junction / peripheral motor system** (presynaptic transmission defect; severe weakness) (engel2016lossofmunc131 pages 2-3, engel2016lossofmunc131 media ceed3256).
- Secondary complications: **respiratory system** (aspiration pneumonia; ventilator dependence) (engel2016lossofmunc131 pages 2-3).

### 7.2 Suggested UBERON terms
- Brain (UBERON:0000955)
- Corpus callosum (UBERON:0002285)
- Neuromuscular junction (UBERON:0001250)
- Spinal cord (UBERON:0002240)

### 7.3 Subcellular localization (suggested)
Munc13-1 is a presynaptic active zone-associated protein; relevant GO Cellular Component suggestions include presynaptic active zone and synaptic vesicle-related compartments.

---

## 8. Temporal development
- **Onset:** congenital/neonatal (engel2016lossofmunc131 pages 1-2, mullins2022homozygousunc13avariant pages 1-2).
- **Progression/course:** severe early course with feeding/respiratory complications; death in infancy/early childhood has been observed in the two biallelic LoF cases retrieved here (mullins2022homozygousunc13avariant pages 2-4, engel2016lossofmunc131 pages 2-3).

---

## 9. Inheritance and population
### 9.1 Inheritance
- Evidence from the congenital severe cases supports **autosomal recessive inheritance** with homozygous truncating/frameshift UNC13A variants and heterozygous carrier parents (engel2016lossofmunc131 pages 3-5, mullins2022homozygousunc13avariant pages 2-4).

### 9.2 Epidemiology / prevalence
No disease-specific prevalence/incidence estimates were reported in the retrieved evidence. (The presynaptic CMS review provides a general CMS prevalence estimate—**1.8 to 14.8 per million under age 18**—but this is not UNC13A-specific and should not be used as the prevalence of UNC13A-related disease) (pugliese2023presynapticcongenitalmyasthenic pages 1-3).

### 9.3 Consanguinity
Parental consanguinity is reported in the 2022 case (parents distant cousins), consistent with recessive inheritance (mullins2022homozygousunc13avariant pages 1-2).

---

## 10. Diagnostics
### 10.1 Clinical and electrophysiologic testing
Evidence-based diagnostic features from Engel include:
- Low baseline CMAP amplitudes with **decrement** on low-frequency stimulation and **facilitation** (>100% increase) with rapid stimulation, consistent with a presynaptic defect (engel2016lossofmunc131 pages 2-3).
- In vitro microelectrode studies demonstrating profoundly reduced MEPP frequency and readily releasable pool with normal release probability (engel2016lossofmunc131 pages 3-5, engel2016lossofmunc131 media ceed3256).

### 10.2 Neuroimaging
- Brain MRI: **thin corpus callosum** in Engel (engel2016lossofmunc131 pages 2-3, engel2016lossofmunc131 media ceed3256).
- In Mullins, MRI was largely unremarkable aside from non-occlusive venous sinus thrombosis (mullins2022homozygousunc13avariant pages 2-4).

### 10.3 Genetic testing approach (real-world implementation)
- In the primary congenital cases, diagnosis was achieved via **exome sequencing** identifying homozygous UNC13A truncating variants (engel2016lossofmunc131 pages 1-2, mullins2022homozygousunc13avariant pages 2-4).
- The 2022 case noted an “epileptic encephalopathy panel” that was negative before UNC13A was found (mullins2022homozygousunc13avariant pages 2-4), supporting real-world escalation from panel testing to broader sequencing.

### 10.4 Differential diagnosis
Given the overlap with presynaptic CMS/LEMS-like physiology and severe early encephalopathy, differential diagnosis should include other **SNARE complex and presynaptic CMS genes** (e.g., SNAP25, VAMP1, SYT2, STXBP1), as discussed in CMS and SNAREopathy reviews (ohno2023clinicalandpathologic pages 1-3, cali2022epilepticphenotypesassociated pages 1-2).

---

## 11. Outcome / prognosis
- High morbidity from severe weakness, feeding and respiratory complications.
- Mortality in reported biallelic LoF cases: death at **8 months** (Mullins) and **50 months** (Engel) (mullins2022homozygousunc13avariant pages 2-4, engel2016lossofmunc131 pages 2-3).

No formal survival curves or prognostic biomarkers were available in the retrieved evidence.

---

## 12. Treatment
### 12.1 Pharmacotherapy used in reported UNC13A biallelic LoF case
In Engel 2016:
- **Pyridostigmine** increased CMAP amplitude but did not improve strength and caused “copious secretions” (engel2016lossofmunc131 pages 2-3).
- **3,4-diaminopyridine** increased ulnar CMAP and improved cough/cry with only slight limb strength improvement (engel2016lossofmunc131 pages 2-3).

**Suggested MAXO terms (ontology suggestions):**
- Acetylcholinesterase inhibitor therapy (pyridostigmine)
- Potassium channel blocker therapy / amifampridine-class therapy (3,4-diaminopyridine)
- Mechanical ventilation
- Gastrostomy tube feeding

### 12.2 Supportive care
Supportive interventions reported include ventilatory support and enteral feeding (gastric tube; fundoplication; gastrojejunostomy) (engel2016lossofmunc131 pages 2-3, mullins2022homozygousunc13avariant pages 1-2).

### 12.3 Clinical trials
A ClinicalTrials.gov search for “UNC13A” in this run primarily retrieved ALS-related studies (not congenital NDD with epilepsy) (NCT05193994; NCT06681610). These should not be interpreted as trials for the congenital UNC13A disorder.

---

## 13. Prevention
No primary prevention strategies are described for this ultra-rare genetic disorder. Prevention is primarily via **genetic counseling**, carrier testing in at-risk families, and reproductive options.

---

## 14. Other species / natural disease
No naturally occurring veterinary disease analogs were retrieved in this run.

---

## 15. Model organisms (supporting mechanism)
Although not a disease-model paper per se in this run, Engel links human findings to Munc13-1 knockout mouse observations and to SNARE/syntaxin biology (engel2016lossofmunc131 pages 3-5, engel2016lossofmunc131 pages 5-6). Mechanistic reviews emphasize that presynaptic genes are conserved and can be modeled in zebrafish, mouse, and C. elegans (pugliese2023presynapticcongenitalmyasthenic pages 1-3).

---

# Evidence tables
A structured summary of human evidence is provided below.

| Publication (first author, year, journal) | URL/DOI | Evidence type (human case report/series) | Inheritance/variant(s) | Key neurologic features (development, seizures/EEG) | Key neuromuscular features | Neuroimaging/neuropathology | Outcome | Notes (e.g., treatments tried) |
|---|---|---|---|---|---|---|---|---|
| Engel, 2016, *Neurology Genetics* | https://doi.org/10.1212/NXG.0000000000000105 | Single human case report with clinical, electrophysiologic, ultrastructural, and genetic analysis | Homozygous nonsense UNC13A variant c.304C>T, p.Gln102*; parents heterozygous; autosomal recessive pattern (engel2016lossofmunc131 pages 1-2, engel2016lossofmunc131 pages 3-5) | Premature infant with hypotonia at birth; microcephaly by 4 months; EEG showed 2–4 Hz posterior background activity, nearly continuous multifocal sharp waves centrally, and periodic trains of sharp waves in both hemispheres without overt seizures; at 21 months unable to sit, babbled but could not speak (engel2016lossofmunc131 pages 1-2, engel2016lossofmunc131 pages 2-3) | Severe presynaptic neuromuscular transmission defect: low-amplitude CMAPs, 20–40% decrement on repetitive stimulation, >100% facilitation with rapid stimulation; marked hypotonia/hyporeflexia, barely moved, ptosis, no voluntary/tracking eye movements, intermittent squint, thoracic kyphoscoliosis, flexion contractures; in vitro studies showed markedly reduced MEPP frequency and readily releasable quanta with normal release probability (engel2016lossofmunc131 pages 2-3, engel2016lossofmunc131 pages 3-5, engel2016lossofmunc131 pages 5-6) | Brain MRI: thin corpus callosum; muscle/endplate studies showed preserved junctional architecture and normal AChR/AChE localization despite physiologic presynaptic failure (engel2016lossofmunc131 pages 2-3, engel2016lossofmunc131 pages 3-5) | Became ventilator dependent after prolonged respiratory arrest during pneumonia at 10–11 months; died of respiratory failure at age 50 months (engel2016lossofmunc131 pages 2-3) | Pyridostigmine increased CMAP amplitude but not strength and caused copious secretions; 3,4-diaminopyridine increased CMAP amplitude and modestly improved cough/cry with only slight limb-strength benefit (engel2016lossofmunc131 pages 2-3) |
| Mullins, 2022, *Cureus* | https://doi.org/10.7759/cureus.30774 | Single human case report with detailed CNS neuropathology | Homozygous UNC13A frameshift variant c.1188delC, p.Asp397Thrfs*107; parents distant cousins; autosomal recessive pattern (mullins2022homozygousunc13avariant pages 2-4, mullins2022homozygousunc13avariant pages 1-2) | Congenital encephalopathy with severe neuromuscular phenotype; infantile spasms; EEG with burst-suppression pattern; alternating hypertonia and hypotonia, decreased consciousness, weak suck and gag; small optic nerves (mullins2022homozygousunc13avariant pages 2-4, mullins2022homozygousunc13avariant pages 1-2) | Extreme generalized muscle weakness; feeding dependence via gastrojejunostomy; severe kyphoscoliosis; diaphragmatic and umbilical hernias (mullins2022homozygousunc13avariant pages 1-2) | MRI largely unremarkable aside from non-occlusive venous sinus thrombosis; autopsy brain showed open Sylvian fissures, blunted frontal and left temporal lobes, vertical hippocampus, absent lines of Gennari, absent subcortical U-fibers; microscopy showed synuclein-positive axonal spheroids in septum pellucidum, cerebellar Purkinje-layer gliosis without Purkinje-cell loss, spinal cord atrophy, and small optic nerves; skin EM showed fingerprint/lamellar inclusions; faint PAS-positive hepatocyte inclusions (mullins2022homozygousunc13avariant pages 2-4, mullins2022homozygousunc13avariant pages 4-5) | Died at 8 months, with bronchopneumonia in the setting of severe neurologic disease (mullins2022homozygousunc13avariant pages 2-4) | Report framed as first detailed CNS neuropathologic report of homozygous UNC13A loss; excerpt did not specify a disease-targeted treatment regimen (mullins2022homozygousunc13avariant pages 1-2, mullins2022homozygousunc13avariant pages 4-5) |
| Su, 2025, *Genes & Diseases* | https://doi.org/10.1016/j.gendis.2024.101315 | Human case series of 3 unrelated probands | Three de novo heterozygous missense UNC13A variants: c.1892T>A/p.Met631Lys, c.1945T>C/p.Phe649Leu, c.2441C>T/p.Pro814Leu; absent from population databases (su2025denovomissense pages 1-3) | Epileptic encephalopathies/intellectual disability; seizure onset at 1y6m, 1y8m, and 7y; focal-onset seizures in febrile and afebrile states; history of status epilepticus; EEG showed focal discharges in the Rolandic region; one had ADHD; dysmorphism and café-au-lait spot noted in one (su2025denovomissense pages 1-3) | Not specifically described in the available excerpt (su2025denovomissense pages 1-3) | Neuroimaging normal in 2 patients; 1 had bilateral lateral ventricle trigone signal abnormalities and abnormal local gyral structure (su2025denovomissense pages 1-3) | Long-term outcome not detailed in available excerpt (su2025denovomissense pages 1-3) | Functional assays in zebrafish/cell systems supported pathogenicity via increased epileptiform activity and calcium fluctuations; no specific antiseizure treatment details available in excerpt (su2025denovomissense pages 1-3) |
| Asadollahi, 2025, *Nature Genetics* | https://doi.org/10.1038/s41588-025-02361-5 | Large human series / syndrome-defining study, 48 index patients | Germline coding or splice-site UNC13A variants; mixed inheritance: autosomal recessive biallelic loss-of-function variants (type A), de novo heterozygous missense gain-of-function variants (type B), and familial heterozygous regulatory missense variant C587F (type C) (asadollahi2025pathogenicunc13avariants pages 1-2) | UNC13A-related neurodevelopmental syndrome with variable global developmental delay/intellectual disability, seizures of different types, hypotonia, tremor, ataxia, dyskinetic movements; severe type A had profound GDD and early-onset seizures; type B seizures mainly refractory to treatment (asadollahi2025pathogenicunc13avariants pages 1-2) | Hypotonia reported among core features; additional neuromuscular-specific phenotype details not provided in excerpt (asadollahi2025pathogenicunc13avariants pages 1-2) | EEG and neuroimaging not detailed in available excerpt (asadollahi2025pathogenicunc13avariants pages 1-2) | Some patients died in early childhood (asadollahi2025pathogenicunc13avariants pages 1-2) | Provides three subtype framework (A–C) linked to distinct mechanisms: reduced protein expression, gain-of-function increased neurotransmission, and impaired second-messenger regulation; 48 index patients total, including 13 in heterozygous de novo missense group and one affected family with at least 4 members (asadollahi2025pathogenicunc13avariants pages 1-2) |


*Table: This table summarizes published human case reports and series relevant to UNC13A-related congenital neurodevelopmental disorder with epilepsy, including congenital encephalopathy with neuromuscular involvement. It highlights inheritance, phenotype, imaging/pathology, outcomes, and treatment notes using only evidence explicitly available in the retrieved snippets and read text.*

---

# Key URLs and publication dates (from retrieved sources)
- Engel et al. “Loss of MUNC13-1 function causes microcephaly, cortical hyperexcitability, and fatal myasthenia.” *Neurology Genetics*. **Oct 2016**. https://doi.org/10.1212/NXG.0000000000000105 (engel2016lossofmunc131 pages 1-2)
- Mullins et al. “Homozygous UNC13A Variant in an Infant With Congenital Encephalopathy and Severe Neuromuscular Phenotype…” *Cureus*. **Oct 2022**. https://doi.org/10.7759/cureus.30774 (mullins2022homozygousunc13avariant pages 2-4)
- Ohno et al. “Clinical and Pathologic Features of Congenital Myasthenic Syndromes Caused by 35 Genes—A Comprehensive Review.” *Int. J. Mol. Sci.* **13 Feb 2023**. https://doi.org/10.3390/ijms24043730 (ohno2023clinicalandpathologic pages 1-3)
- Pugliese et al. “Presynaptic Congenital Myasthenic Syndromes…” *Journal of Neuromuscular Diseases*. **8 Sep 2023**. https://doi.org/10.3233/jnd-221646 (pugliese2023presynapticcongenitalmyasthenic pages 1-3)
- Scorrano et al. “Exploring the Landscape of Pre- and Post-Synaptic Pediatric Disorders with Epilepsy…” *Int. J. Mol. Sci.* **7 Nov 2024**. https://doi.org/10.3390/ijms252211982 (scorrano2024exploringthelandscape pages 1-2)

# Figures/tables examined
- Engel 2016 Table 1 (microelectrode studies) and Figure 2 (thin corpus callosum MRI) were inspected directly (engel2016lossofmunc131 media ceed3256).

References

1. (engel2016lossofmunc131 pages 1-2): Andrew G. Engel, Duygu Selcen, Xin-Ming Shen, Margherita Milone, and C. Michel Harper. Loss of munc13-1 function causes microcephaly, cortical hyperexcitability, and fatal myasthenia. Neurology Genetics, Oct 2016. URL: https://doi.org/10.1212/nxg.0000000000000105, doi:10.1212/nxg.0000000000000105. This article has 81 citations.

2. (mullins2022homozygousunc13avariant pages 2-4): Jordyn R Mullins, Kathryn McFadden, Nicole Snow, and Angelica Oviedo. Homozygous unc13a variant in an infant with congenital encephalopathy and severe neuromuscular phenotype: a case report with detailed central nervous system neuropathologic findings. Cureus, Oct 2022. URL: https://doi.org/10.7759/cureus.30774, doi:10.7759/cureus.30774. This article has 4 citations.

3. (scorrano2024exploringthelandscape pages 1-2): Giovanna Scorrano, Ludovica Di Francesco, Armando Di Ludovico, Francesco Chiarelli, and Sara Matricardi. Exploring the landscape of pre- and post-synaptic pediatric disorders with epilepsy: a narrative review on molecular mechanisms involved. International Journal of Molecular Sciences, 25:11982, Nov 2024. URL: https://doi.org/10.3390/ijms252211982, doi:10.3390/ijms252211982. This article has 10 citations.

4. (ohno2023clinicalandpathologic pages 1-3): K. Ohno, B. Ohkawara, Xinming Shen, D. Selcen, and A. Engel. Clinical and pathologic features of congenital myasthenic syndromes caused by 35 genes—a comprehensive review. International Journal of Molecular Sciences, Feb 2023. URL: https://doi.org/10.3390/ijms24043730, doi:10.3390/ijms24043730. This article has 111 citations.

5. (pugliese2023presynapticcongenitalmyasthenic pages 1-3): Alessia Pugliese, Stephen H. Holland, Carmelo Rodolico, Hanns Lochmüller, and Sally Spendiff. Presynaptic congenital myasthenic syndromes: understanding clinical phenotypes through in vivo models. Journal of Neuromuscular Diseases, 10:731-759, Sep 2023. URL: https://doi.org/10.3233/jnd-221646, doi:10.3233/jnd-221646. This article has 17 citations and is from a peer-reviewed journal.

6. (asadollahi2025pathogenicunc13avariants pages 1-2): Reza Asadollahi, Aisha Ahmad, Paranchai Boonsawat, Jasmine Shahanoor Hinzen, Mareike Lohse, Boris Bouazza-Arostegui, Siqi Sun, Tillmann Utesch, Jonas D. Sommer, Dragana Ilic, Murugesh Padmanarayana, Kati Fischermanns, Mrinalini Ranjan, Moritz Boll, Chandran Ka, Amélie Piton, Francesca Mattioli, Bertrand Isidor, Katrin Õunap, Karit Reinson, Monica H. Wojcik, Christian R. Marshall, Saadet Mercimek-Andrews, Naomichi Matsumoto, Noriko Miyake, Bruno de Oliveira Stephan, Rachel Sayuri Honjo, Debora R. Bertola, Chong Ae Kim, Roman Yusupov, Heather C. Mefford, John Christodoulou, Joy Lee, Oliver Heath, Natasha J. Brown, Naomi Baker, Zornitza Stark, Martin Delatycki, Nicole J. Lake, Shimriet Zeidler, Linda Zuurbier, Saskia M. Maas, Chris C. de Kruiff, Farrah Rajabi, Lance H. Rodan, Stephanie A. Coury, Konrad Platzer, Henry Oppermann, Rami Abou Jamra, Skadi Beblo, Caroline Maxton, Robert Śmigiel, Hunter Underhill, Holly Dubbs, Alyssa Rosen, Katherine L. Helbig, Ingo Helbig, Sarah McKeown Ruggiero, Mark P. Fitzgerald, Dennis Kraemer, Carlos E. Prada, Jeffrey Tenney, Parul Jayakar, Sylvia Redon, Jérémie Lefranc, Kevin Uguen, Simone Race, Stephanie Efthymiou, Reza Maroofian, Henry Houlden, Sandra Coppens, Nicolas Deconinck, Balasubramaniem Ashokkumar, Perumal Varalakshmi, Vykunta Raju Gowda K, Fatemeh Eghbal, Ehsan Ghayoor Karimiani, Morteza Heidari, John Neidhardt, Marta Owczarek-Lipska, G. Christoph Korenke, Michael J. Bamshad, Philippe M. Campeau, Anna Lehman, Laura G. Hendon, Ingrid M. Wentzensen, Kristin G. Monaghan, Yanmin Chen, Anna Szuto, Ronald D. Cohn, Ping Yee Billie Au, Christoph Hübner, Felix Boschann, Kandamurugu Manickam, Daniel C. Koboldt, Aboulfazl Rad, Gabriela Oprea, Kristine K. Bachman, Andrea H. Seeley, Emanuele Agolini, Alessandra Terracciano, Piscopo Carmelo, Caleb Bupp, Bethany Grysko, Annick Rein-Rothschild, Bruria Ben Zeev, Amy Margolin, Jennifer Morrison, Aditi Dagli, Elliot Stolerman, Raymond J. Louie, Camerun Washington, Servi J. C. Stevens, Malou Heijligers, Fowzan S. Alkuraya, Jasmin Lisfeld, Axel Neu, Fabíola Paoli Monteiro, André Luiz Santos Pessoa, Antonio Edvan Camelo-Filho, Fernando Kok, Dwight Koeberl, Kacie Riley, Lydie Burglen, Diane Doummar, Bénédicte Héron, Cyril Mignot, Boris Keren, Perrine Charles, Caroline Nava, Felix P. Bernhard, Andrea A. Kühn, Sven Thoms, Ryan D. Morrie, Shila Mekhoubad, Eric M. Green, Sami J. Barmada, Aaron D. Gitler, Olaf Jahn, Jeong Seop Rhee, Christian Rosenmund, Mišo Mitkovski, Heinrich Sticht, Han Sun, Gerald Le Gac, Holger Taschenberger, Nils Brose, Jeremy S. Dittman, Anita Rauch, and Noa Lipstein. Pathogenic unc13a variants cause a neurodevelopmental syndrome by impairing synaptic function. Nature Genetics, 57:2691-2704, Oct 2025. URL: https://doi.org/10.1038/s41588-025-02361-5, doi:10.1038/s41588-025-02361-5. This article has 3 citations and is from a highest quality peer-reviewed journal.

7. (cali2022epilepticphenotypesassociated pages 1-2): Elisa Cali, Clarissa Rocca, Vincenzo Salpietro, and Henry Houlden. Epileptic phenotypes associated with snares and related synaptic vesicle exocytosis machinery. Frontiers in Neurology, Jan 2022. URL: https://doi.org/10.3389/fneur.2021.806506, doi:10.3389/fneur.2021.806506. This article has 30 citations and is from a peer-reviewed journal.

8. (engel2016lossofmunc131 pages 3-5): Andrew G. Engel, Duygu Selcen, Xin-Ming Shen, Margherita Milone, and C. Michel Harper. Loss of munc13-1 function causes microcephaly, cortical hyperexcitability, and fatal myasthenia. Neurology Genetics, Oct 2016. URL: https://doi.org/10.1212/nxg.0000000000000105, doi:10.1212/nxg.0000000000000105. This article has 81 citations.

9. (mullins2022homozygousunc13avariant pages 1-2): Jordyn R Mullins, Kathryn McFadden, Nicole Snow, and Angelica Oviedo. Homozygous unc13a variant in an infant with congenital encephalopathy and severe neuromuscular phenotype: a case report with detailed central nervous system neuropathologic findings. Cureus, Oct 2022. URL: https://doi.org/10.7759/cureus.30774, doi:10.7759/cureus.30774. This article has 4 citations.

10. (engel2016lossofmunc131 pages 2-3): Andrew G. Engel, Duygu Selcen, Xin-Ming Shen, Margherita Milone, and C. Michel Harper. Loss of munc13-1 function causes microcephaly, cortical hyperexcitability, and fatal myasthenia. Neurology Genetics, Oct 2016. URL: https://doi.org/10.1212/nxg.0000000000000105, doi:10.1212/nxg.0000000000000105. This article has 81 citations.

11. (engel2016lossofmunc131 media ceed3256): Andrew G. Engel, Duygu Selcen, Xin-Ming Shen, Margherita Milone, and C. Michel Harper. Loss of munc13-1 function causes microcephaly, cortical hyperexcitability, and fatal myasthenia. Neurology Genetics, Oct 2016. URL: https://doi.org/10.1212/nxg.0000000000000105, doi:10.1212/nxg.0000000000000105. This article has 81 citations.

12. (mullins2022homozygousunc13avariant pages 4-5): Jordyn R Mullins, Kathryn McFadden, Nicole Snow, and Angelica Oviedo. Homozygous unc13a variant in an infant with congenital encephalopathy and severe neuromuscular phenotype: a case report with detailed central nervous system neuropathologic findings. Cureus, Oct 2022. URL: https://doi.org/10.7759/cureus.30774, doi:10.7759/cureus.30774. This article has 4 citations.

13. (engel2016lossofmunc131 pages 5-6): Andrew G. Engel, Duygu Selcen, Xin-Ming Shen, Margherita Milone, and C. Michel Harper. Loss of munc13-1 function causes microcephaly, cortical hyperexcitability, and fatal myasthenia. Neurology Genetics, Oct 2016. URL: https://doi.org/10.1212/nxg.0000000000000105, doi:10.1212/nxg.0000000000000105. This article has 81 citations.

14. (su2025denovomissense pages 1-3): Ke Su, Yu Ma, Mingshan Zhou, Yihan Liu, Chengjie Li, Yonghui Jiang, Qihui Wu, Gang Peng, Yi Wang, and Shaohua Fan. De novo missense variants of unc13a are implicated in epileptic encephalopathies and neurodevelopmental disorders. Genes &amp; Diseases, 12:101315, Mar 2025. URL: https://doi.org/10.1016/j.gendis.2024.101315, doi:10.1016/j.gendis.2024.101315. This article has 5 citations.