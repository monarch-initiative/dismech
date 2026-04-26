---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:24.155206'
end_time: '2026-04-25T22:28:16.701230'
duration_seconds: 772.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lafora Disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lafora Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lafora Disease** covering all of the
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
- **Disease Name:** Lafora Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lafora Disease** covering all of the
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


## Lafora Disease (LD) — Comprehensive Disease Characteristics Report (Mendelian)

### Target disease
- **Disease:** Lafora disease
- **Category:** Mendelian (autosomal recessive progressive myoclonus epilepsy / glycogen storage disorder) (turnbull2016laforadisease. pages 1-2, pondrelli2021naturalhistoryof pages 1-2)
- **MONDO ID:** not retrieved from the available sources in this run (see identifiers table below) (pondrelli2021naturalhistoryof pages 1-2, turnbull2016laforadisease. pages 1-2)

### Evidence note (source types)
This report synthesizes: (i) peer‑reviewed reviews and primary studies (2012–2024, emphasizing 2023–2024), (ii) systematic reviews/meta-analyses with individual participant data, and (iii) ClinicalTrials.gov records for real‑world clinical implementation and trial readiness. ClinicalTrials.gov records provide MeSH terms and operational definitions for outcomes/biomarkers but do not substitute for peer‑reviewed efficacy evidence. (NCT03876522 chunk 1, NCT06609889 chunk 1)

| Disease name | MONDO ID | OMIM | Orphanet | MeSH | ICD | Synonyms / alternate names | Inheritance | Causal genes |
|---|---|---|---|---|---|---|---|---|
| Lafora disease |  (not retrieved) | OMIM #254780 (turnbull2016laforadisease. pages 1-2, pondrelli2023prognosticvalueof pages 1-2, duran2023roleofastrocytes pages 1-2, pondrelli2021naturalhistoryof pages 1-2, burgos2023earlytreatmentwith pages 1-2) | ORPHA:501 (burgos2023earlytreatmentwith pages 1-2) | MeSH: D020192 “Lafora Disease” (NCT03876522 chunk 1, NCT00007124 chunk 1) | ICD-10/ICD-11: not retrieved in current context | Lafora body disease; progressive myoclonus epilepsy; progressive myoclonus epilepsy type 2 / EPM2; Lafora progressive myoclonus epilepsy (turnbull2016laforadisease. pages 1-2, pondrelli2021naturalhistoryof pages 1-2, imbrici2024sodiumglucosecotransporter2inhibitors pages 1-3) | Autosomal recessive (turnbull2016laforadisease. pages 1-2, pondrelli2023prognosticvalueof pages 1-2, skurat2024impairedmalinexpression pages 1-2, pondrelli2021naturalhistoryof pages 1-2, burgos2023earlytreatmentwith pages 1-2) | EPM2A (laforin) and NHLRC1 / EPM2B (malin); PRDM8 tentatively linked in one early-onset family, not confirmed as a major cause (turnbull2016laforadisease. pages 1-2, pondrelli2023prognosticvalueof pages 1-2, duran2023roleofastrocytes pages 1-2, pondrelli2021naturalhistoryof pages 1-2, burgos2023earlytreatmentwith pages 1-2) |


*Table: This table compiles the core identifiers, nomenclature, inheritance pattern, and causal genes for Lafora disease from the retrieved literature and clinical-trial metadata. It is useful as a compact knowledge-base starter for standardized disease naming and cross-references.*

## 1. Disease Information

### 1.1 What is Lafora disease?
Lafora disease is an **ultra‑rare, fatal, autosomal recessive** form of **progressive myoclonus epilepsy** characterized pathologically by **intracellular polyglucosan (abnormal glycogen) inclusions** called **Lafora bodies** that accumulate in brain and other tissues. (turnbull2016laforadisease. pages 1-2, duran2023roleofastrocytes pages 1-2, pondrelli2021naturalhistoryof pages 1-2)

**Current clinical understanding** is that affected individuals are typically previously healthy and develop seizures and myoclonus in late childhood/adolescence, followed by rapid neurodegeneration (cognitive/psychiatric decline, ataxia, dysarthria) and death often within ~10 years of onset. (turnbull2016laforadisease. pages 3-4, pondrelli2021naturalhistoryof pages 1-2)

### 1.2 Key identifiers, synonyms, and data provenance
- **OMIM:** #254780 (turnbull2016laforadisease. pages 1-2, pondrelli2021naturalhistoryof pages 1-2)
- **Orphanet:** ORPHA:501 (burgos2023earlytreatmentwith pages 1-2)
- **MeSH:** “Lafora Disease” (MeSH **D020192** appears in ClinicalTrials.gov metadata) (NCT03876522 chunk 1)
- **ICD‑10/ICD‑11:** not retrieved in the available sources for this run (turnbull2016laforadisease. pages 1-2)
- **Synonyms/alternate names:** “Lafora body disease,” “progressive myoclonus epilepsy type 2 (EPM2),” “Lafora progressive myoclonus epilepsy.” (turnbull2016laforadisease. pages 1-2, imbrici2024sodiumglucosecotransporter2inhibitors pages 1-3)

**Data sources:** largely **aggregated disease-level resources** (systematic reviews/meta‑analyses; clinical trial registries; reviews) plus individual **case reports** used for genotype–phenotype and diagnostic nuance. (pondrelli2021naturalhistoryof pages 1-2, pondrelli2023prognosticvalueof pages 1-2, aggradi2023laforadiseasea pages 1-2)

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** biallelic pathogenic variants in **EPM2A** or **NHLRC1 (EPM2B)** leading to loss of function of **laforin** (glucan phosphatase) or **malin** (E3 ubiquitin ligase), respectively, and consequent disruption of glycogen structure/solubility with Lafora body formation. (pondrelli2023prognosticvalueof pages 1-2, skurat2024impairedmalinexpression pages 1-2, turnbull2016laforadisease. pages 1-2)

**Abstract quote (mechanism + fatal course):** Duran (2023) states that LD is caused by “loss of function mutations in either the EPM2A or NHLRC1 gene” and that the hallmark is “accumulation of poorly branched glycogen in the form of aggregates known as Lafora bodies.” (duran2023roleofastrocytes pages 1-2)

### 2.2 Risk factors
- **Genetic risk factor:** autosomal recessive inheritance; **consanguinity** increases frequency and LD is more frequent in regions/populations with higher consanguinity rates. (turnbull2016laforadisease. pages 1-2, pondrelli2021naturalhistoryof pages 1-2)
- **Geographic association:** relatively higher frequency in Mediterranean countries, North Africa, Middle East, and some regions of Southern India. (turnbull2016laforadisease. pages 1-2, pondrelli2021naturalhistoryof pages 1-2)

### 2.3 Protective factors
No established genetic or environmental protective factors were identified in the retrieved evidence set. The best available “protective” signals in current evidence are **prognostic modifiers** (below) rather than preventive factors. (pondrelli2023prognosticvalueof pages 1-2, pondrelli2021naturalhistoryof pages 1-2)

### 2.4 Gene–environment interactions
No clear gene–environment interaction evidence was retrieved in the available corpus; the major risk architecture is Mendelian biallelic loss-of-function with possible population/founder effects. (turnbull2016laforadisease. pages 1-2, pondrelli2021naturalhistoryof pages 1-2)

## 3. Phenotypes (clinical features)

### 3.1 Core neurological phenotype (with suggested HPO)
Lafora disease is clinically described as relatively homogeneous (except for rare atypical forms), with onset usually in adolescence and rapid progression. (turnbull2016laforadisease. pages 1-2, turnbull2016laforadisease. pages 3-4)

Key phenotypes include:
- **Progressive myoclonic epilepsy**: action- and stimulus‑sensitive myoclonus and generalized seizures including tonic–clonic, absence, atonic, and **visual seizures**; **photosensitivity** can be prominent. (turnbull2016laforadisease. pages 1-2, turnbull2016laforadisease. pages 3-4)
  - Suggested HPO: **Myoclonus (HP:0001336)**; **Generalized tonic-clonic seizure (HP:0002069)**; **Absence seizures (HP:0002121)**; **Photosensitivity (HP:0001338)**; **Visual seizures (HP:0001121)**
- **Neuropsychiatric symptoms** (behavioral change, depression/apathy; hallucinations/psychosis reported): (turnbull2016laforadisease. pages 1-2, aggradi2023laforadiseasea pages 2-4)
  - Suggested HPO: **Behavioral abnormality (HP:0000708)**; **Depression (HP:0000716)**; **Hallucinations (HP:0000738)**; **Psychosis (HP:0000709)**
- **Cognitive decline / dementia** progressing to severe disability and vegetative state: (turnbull2016laforadisease. pages 3-4, pondrelli2021naturalhistoryof pages 1-2)
  - Suggested HPO: **Cognitive impairment (HP:0100543)**; **Dementia (HP:0000726)**; **Loss of ambulation (HP:0002505)**
- **Cerebellar and bulbar dysfunction**: ataxia, dysarthria, mutism, dysphagia in advanced disease. (turnbull2016laforadisease. pages 3-4, aggradi2023laforadiseasea pages 2-4)
  - Suggested HPO: **Ataxia (HP:0001251)**; **Dysarthria (HP:0001260)**; **Dysphagia (HP:0002015)**; **Mutism (HP:0002317)**

### 3.2 EEG and electrophysiology phenotype (diagnostic signature)
A key real‑world clinical discriminator is the progression of EEG abnormalities:
- Early EEG may be near normal or slightly slowed; **occipital discharges** on a slowed posterior dominant rhythm are described as highly suggestive in context. (turnbull2016laforadisease. pages 1-2)
- Over time, EEG progresses to frequent diffuse epileptic discharges, long bursts of spike‑waves/polyspikes with major myoclonic jerks, and marked **photic stimulation enhancement**. (turnbull2016laforadisease. pages 3-4)

### 3.3 Laboratory/pathology phenotypes
- **Lafora bodies** (PAS‑positive glycogen‑like inclusions) can be found in multiple tissues (brain, liver, muscle, sweat glands). (turnbull2016laforadisease. pages 1-2)
- Atypical pathology can occur: a 2023 case report found increased lipid droplets and mild intermyofibrillar glycogen with **PAS‑D negative for Lafora bodies**, illustrating that biopsy sensitivity can be limited. (aggradi2023laforadiseasea pages 2-4)

### 3.4 Frequency/penetrance and QoL impact
Quantitative phenotype frequencies were not directly enumerated in the retrieved excerpts. However, severe QoL impact is implicit from the high probability of loss of autonomy and the use of epilepsy QoL instruments in longitudinal studies/trials. (pondrelli2021naturalhistoryof pages 1-2, NCT06609889 chunk 1)

QoL instruments used in current trial infrastructure include **QOLCE‑55**, **QOLIE‑AD48**, and **QOLIE‑31P**. (NCT06609889 chunk 1)

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **EPM2A** encodes **laforin**, described as a protein with an N‑terminal carbohydrate‑binding domain and a C‑terminal dual‑specificity phosphatase domain. (pondrelli2023prognosticvalueof pages 1-2, skurat2024impairedmalinexpression pages 1-2)
- **NHLRC1 / EPM2B** encodes **malin**, an E3 ubiquitin ligase with a RING finger domain and NHL repeats/domains. (pondrelli2023prognosticvalueof pages 1-2, skurat2024impairedmalinexpression pages 1-2)

**Third gene claim:** **PRDM8** has been reported in a single early‑onset family and remains tentative/not confirmed as a common cause in systematic summaries. (pondrelli2021naturalhistoryof pages 1-2, turnbull2012earlyonsetlaforabody pages 4-5)

### 4.2 Pathogenic variants and genotype–phenotype modifiers (recent quantitative synthesis)
A 2023 systematic review/meta‑analysis of genetically confirmed cases analyzed variant classes:
- In 250 cases, mutated gene was **NHLRC1 in 56%** and **EPM2A in 44%**, with **114 distinct pathogenic variants** identified (67 EPM2A; 47 NHLRC1). (pondrelli2023prognosticvalueof pages 1-2)
- **NHLRC1 PT/PT** (biallelic truncating) genotype associated with **shorter survival** (HR **2.88**, 95% CI 1.23–6.78). (pondrelli2023prognosticvalueof pages 6-9)
- A specific homozygous missense variant **p.Asp146Asn (NHLRC1)** was confirmed to have a **more favorable prognosis** (disease duration >15 years in the described subgroup). (pondrelli2023prognosticvalueof pages 6-9)

### 4.3 Functional consequences and protein dysfunction
Mechanistically, loss of laforin/malin function yields glycogen molecules with abnormal structure (poor branching, long chains; often hyperphosphorylated) that become insoluble and aggregate into Lafora bodies, driving neuroinflammation and neurodegeneration. (donohue2023gys1antisensetherapy pages 1-2, duran2023roleofastrocytes pages 1-2)

**Abstract quote (polyglucosan → neuroinflammation/degeneration):** Mitra et al. describe LD as “continuous formation of glycogen molecules with overlong and overphosphorylated branches called polyglucosans, which precipitate and gradually aggregate… [Lafora bodies]. These drive escalating neuroinflammation and neurodegeneration… and death within 10 years of onset.” (mitra2023laforintargetsmalin pages 1-2)

### 4.4 Modifier genes, epigenetics, chromosomal abnormalities
No robust modifier genes or epigenetic signatures were identified in the available evidence set for this run.

## 5. Environmental Information
No specific toxin/lifestyle/infectious environmental causes were identified; LD is primarily Mendelian. (pondrelli2021naturalhistoryof pages 1-2, turnbull2016laforadisease. pages 1-2)

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (upstream → downstream)
**Upstream trigger:** biallelic LOF in **EPM2A** or **NHLRC1/EPM2B** → dysfunctional laforin/malin complex (pondrelli2023prognosticvalueof pages 1-2, aggradi2023laforadiseasea pages 1-2)

**Primary molecular defect:** abnormal glycogen structure (poor branching; long chains; often hyperphosphorylation) → insoluble polyglucosan → **Lafora bodies** (duran2023roleofastrocytes pages 1-2, skurat2024impairedmalinexpression pages 1-2)

**Cellular/tissue response:** Lafora bodies and abnormal glycogen associate with neuroinflammation and neurodegeneration; increasing seizure burden and cognitive decline. (mitra2023laforintargetsmalin pages 1-2, donohue2023gys1antisensetherapy pages 1-2)

### 6.2 Cell type involvement — astrocytes as a key recent concept (2023)
A major shift in “current understanding” is the cell type distribution of Lafora bodies:
- Historically thought to be neuronal; now evidence indicates **most glycogen aggregates are present in astrocytes** and that **astrocytic Lafora bodies contribute to pathology**. (duran2023roleofastrocytes pages 1-2)

**Suggested Cell Ontology (CL) terms (candidate):** astrocyte (CL:0000127); neuron (CL:0000540).

### 6.3 Protein interaction and localization (2023–2024 mechanistic advances)
- **Laforin targets malin to glycogen**: Mitra et al. generated a FLAG-tagged malin mouse and showed that malin localizes to glycogen and its presence at glycogen depends on laforin. (mitra2023laforintargetsmalin pages 1-2)
- **Malin stabilization and interactome requires laforin**: Skurat et al. report that malin interacts with laforin and multiple glycogen-metabolizing enzymes; “interaction of malin with partner proteins requires laforin” (not dependent on laforin catalytic activity). (skurat2024impairedmalinexpression pages 1-2)

### 6.4 Pathways and ontology suggestions
**Candidate GO Biological Process terms (suggested):**
- Glycogen metabolic process (GO:0005977)
- Glycogen biosynthetic process (GO:0005978)
- Protein ubiquitination (GO:0016567)
- Inflammatory response (GO:0006954)
- Neuroinflammatory response (candidate; map to inflammatory response + CNS context)

**Candidate GO Cellular Component terms (suggested):** cytosol (GO:0005829); glycogen granule (GO:0042587); lysosome (GO:0005764).

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue distribution
Pathology includes Lafora bodies in:
- **Brain** (major driver of clinical manifestations),
- **Liver**, **skeletal muscle**, **cardiac muscle**, and **sweat gland cells** (eccrine/apocrine). (turnbull2016laforadisease. pages 1-2)

**Suggested UBERON terms (candidate):** brain (UBERON:0000955); liver (UBERON:0002107); skeletal muscle tissue (UBERON:0001134); heart (UBERON:0000948); skin (UBERON:0002097).

## 8. Temporal Development

### 8.1 Onset
Natural history meta-analysis reports:
- **Mean onset age 13.4 years (SD 3.7)**; **9.1%** with onset ≥18 years. (pondrelli2021naturalhistoryof pages 1-2)
- Reviews commonly state onset in adolescence; some cases are late-onset. (turnbull2016laforadisease. pages 1-2, pondrelli2021naturalhistoryof pages 1-2)

### 8.2 Progression pattern and staging
LD course is progressive with escalating seizures and neurodegeneration leading to severe disability. (turnbull2016laforadisease. pages 3-4)

A 2025 cohort analysis described three stages (presenting symptoms → progressive neurodegeneration → terminal stage) with increasing seizure emergencies and medical complications; included here as an example of operational clinical staging (though not 2023–2024). (d’orsi2025clinicalcourseand pages 1-2)

## 9. Inheritance and Population

### 9.1 Inheritance
- **Autosomal recessive** (biallelic pathogenic variants). (turnbull2016laforadisease. pages 1-2, pondrelli2023prognosticvalueof pages 1-2)

### 9.2 Epidemiology (statistics)
- **Worldwide prevalence ~4 cases per million**. (pondrelli2021naturalhistoryof pages 1-2, aggradi2023laforadiseasea pages 1-2)
- Higher frequency in Mediterranean countries/North Africa/Middle East/Southern India; association with consanguinity. (turnbull2016laforadisease. pages 1-2, pondrelli2021naturalhistoryof pages 1-2)

### 9.3 Population/prognostic demographic factors
- In pooled survival analyses, **Asian origin** and onset <18 years were negative prognostic factors. (pondrelli2021naturalhistoryof pages 1-2, pondrelli2023prognosticvalueof pages 6-9)

## 10. Diagnostics

### 10.1 Clinical tests and biomarkers used in practice/research
- **EEG**: progressive abnormalities including occipital discharges early and later diffuse spike‑waves/polyspikes with photic sensitivity. (turnbull2016laforadisease. pages 3-4, turnbull2016laforadisease. pages 1-2)
- **MRI**: often unremarkable at onset. (turnbull2016laforadisease. pages 1-2, aggradi2023laforadiseasea pages 2-4)

### 10.2 Biopsy/pathology
- **Skin biopsy** can demonstrate PAS‑positive inclusions (Lafora bodies) in sweat gland myoepithelial cells; however, systematic natural history review cautions about **false positives/false negatives** and positions **genetic testing as reference standard**. (turnbull2016laforadisease. pages 1-2, pondrelli2021naturalhistoryof pages 1-2)

### 10.3 Genetic testing (recommended approach)
- **Targeted genetic testing for biallelic EPM2A or EPM2B/NHLRC1 variants** is the current reference standard for confirmation. (pondrelli2021naturalhistoryof pages 1-2)
- Example implementation (2023 case): targeted next-generation sequencing (clinical exome) + Sanger confirmation identified homozygous **c.137G>A, p.(Cys46Tyr)** in EPM2B. (aggradi2023laforadiseasea pages 2-4)

### 10.4 Differential diagnosis
Differentials for progressive myoclonic epilepsies include Unverricht–Lundborg disease (EPM1), neuronal ceroid lipofuscinoses, MERRF, and sialidosis. (turnbull2016laforadisease. pages 3-4)

## 11. Outcome / Prognosis

### 11.1 Survival and disability (quantitative natural history)
Individual participant data meta-analysis (2021) provides key statistics:
- **Survival:** 93% at 5 years; 62% at 10 years; 57% at 15 years; **median survival 11 years**. (pondrelli2021naturalhistoryof pages 1-2)
- **Loss of autonomy:** 45% at 5 years; 75% at 10 years; 83% at 15 years; **median time to loss of autonomy 6 years**. (pondrelli2021naturalhistoryof pages 1-2)

### 11.2 Genotype-informed prognosis (2023)
- NHLRC1 truncating/truncating genotype (PT/PT) confers higher hazard of death (HR 2.88) and possible increased risk for loss of autonomy. (pondrelli2023prognosticvalueof pages 6-9)

## 12. Treatment

### 12.1 Current standard of care (real-world implementation)
- **Antiseizure medications (ASMs)** are used symptomatically but do not stop the neurodegenerative process; drug resistance develops. (imbrici2024sodiumglucosecotransporter2inhibitors pages 1-3, turnbull2016laforadisease. pages 1-2)
- **Supportive care** becomes critical in advanced stages (preventing/handling status epilepticus, aspiration pneumonia, respiratory compromise). (turnbull2016laforadisease. pages 3-4, d’orsi2025clinicalcourseand pages 1-2)

**Suggested MAXO terms (candidate):** antiseizure therapy (MAXO:0001298, candidate); supportive care (MAXO:0000747, candidate); ketogenic diet therapy (MAXO:0000088, candidate).

### 12.2 Disease-modifying and emerging therapies (2023–2024 prioritized)

| Approach | Target/mechanism | Evidence type | Key findings | Source (citation) | Publication date | URL | ClinicalTrials.gov NCT |
|---|---|---|---|---|---|---|---|
| Disease-modifying | **Gys1-ASO** lowers brain glycogen synthase 1 to reduce glycogen synthesis, Lafora body formation, and network hyperexcitability | Mouse model (Epm2b-/-) | Intracerebroventricular dosing at 4, 7, and 10 months led to **decreased Gys1 protein**, **decreased glycogen aggregation**, and **reduced epileptiform discharges**; prior genetic work cited in the paper suggested ~**50% reduction** in glycogen synthesis strongly suppresses pathology | Donohue et al., *Neurotherapeutics* (donohue2023gys1antisensetherapy pages 1-2) | 2023-09-12 | https://doi.org/10.1007/s13311-023-01434-9 | — |
| Disease-modifying / repurposed | **Metformin**; AMPK activation with downstream effects on oxidative stress, neuroinflammation, mitochondrial dysfunction, and neuronal hyperexcitability | Mouse models + human observational follow-up | In Epm2a-/- and Epm2b-/- mice, **early treatment from conception to adulthood** improved PTZ sensitivity, motor/memory outcomes, neurodegeneration, astrogliosis, and decreased Lafora bodies; human follow-up included **18 patients** (**8 treated**, **10 untreated**), with treated patients showing **slower disease progression** and slower decline in daily living activities | Burgos et al., *Neurotherapeutics* (burgos2023earlytreatmentwith pages 1-2) | 2022-10-27 / 2023 issue | https://doi.org/10.1007/s13311-022-01304-w | — |
| Disease-modifying / hypothesis-generating repurposing | **SGLT2 inhibitors (gliflozins)** proposed to reduce neuronal/astrocytic glucose entry, lower glycogen storage/polyglucosan formation, reduce sodium-dependent excitability, and promote ketogenesis | Review / mechanistic hypothesis | No efficacy data in LD patients yet; article argues these drugs may reduce glucose available for glycogen accumulation and could mimic some antiepileptic/metabolic benefits; emphasizes LD prevalence **<4 per 1,000,000**, onset around **10–11 years**, life expectancy about **10 years from diagnosis** | Imbrici et al., *Pharmacological Research* (imbrici2024sodiumglucosecotransporter2inhibitors pages 1-3) | 2024-01 | https://doi.org/10.1016/j.phrs.2023.107012 | — |
| Disease-modifying | **ION283** intrathecal antisense oligonucleotide for Lafora disease | Phase 1/2 open-label clinical trial | Recruiting **10** participants; **15 mg intrathecal every 12 weeks** for 24 months; primary endpoint safety (treatment-related AEs); efficacy endpoints include Lafora Disease Performance Scale, PEDI, global impression scales, seizure frequency, and EEG measures | ClinicalTrials.gov trial record (NCT06609889 chunk 1) | First posted 2024-09-24; updated 2025-12-18 | https://clinicaltrials.gov/study/NCT06609889 | **NCT06609889** |
| Disease-modifying / expanded access | **VAL-1221** intravenous investigational therapy; expanded-access program for genetically confirmed mid-stage LD | Expanded access program | Protocol allows up to **10** patients; dosing **20 mg/kg IV every other week**; eligibility includes genetically confirmed LD with pathogenic/likely pathogenic variants in **EPM2A** or **EPM2B** and age **12–28 years** | ClinicalTrials.gov expanded access record (NCT05930223 chunk 1) | First posted 2023-07-05 | https://clinicaltrials.gov/study/NCT05930223 | **NCT05930223** |
| Symptomatic / possibly disease-modifying | **Ketogenic diet**; restrictive minimum-carbohydrate diet aimed at altering substrate availability and seizure burden | NIH open-label clinical study | Planned enrollment **15**; 6-month protocol in patients ≥10 years with relatively advanced LD; outcomes included standardized clinical scales plus MRI/MRS, CSF, EEG, EMG, evoked potentials, and metabolic testing; designed to assess acute and potential disease-modifying effects | ClinicalTrials.gov trial record (NCT00007124 chunk 1) | First posted 2000-12-08; completed 2002-11 | https://clinicaltrials.gov/study/NCT00007124 | **NCT00007124** |
| Natural history / trial-readiness / biomarker platform | Prospective natural history and functional status study to define clinical course, biomarkers, and outcome measures for future intervention trials | Prospective observational cohort | Completed study with **33** participants over **24 months**; collected blood and CSF for biomarker work and longitudinal assessments including Lafora Disease Performance Scale, seizure diary, video-EEG, cognitive/motor testing, caregiver burden, ataxia scales, and QoL instruments | ClinicalTrials.gov observational study record (NCT03876522 chunk 1) | First posted 2019-03-15; completed 2022-04-01 | https://clinicaltrials.gov/study/NCT03876522 | **NCT03876522** |


*Table: This table summarizes the current Lafora disease therapeutic landscape, emphasizing 2023-2024 developments while also including key older clinical studies that support trial readiness. It is useful for quickly comparing mechanisms, evidence levels, and active/available clinical programs.*

Key developments:
- **GYS1 reduction strategies (ASO)**: 2023 preclinical work demonstrates that a brain‑delivered Gys1-ASO reduces glycogen aggregation and epileptiform discharges in LD mouse models. (donohue2023gys1antisensetherapy pages 1-2)
- **Clinical translation to ASO trials:** a Phase 1/2 intrathecal ASO program (ION283) is recruiting (NCT06609889). (NCT06609889 chunk 1)
- **Metformin repurposing:** metformin shows improved outcomes in LD mouse models and is associated with slower progression in a small human observational cohort (8 treated vs 10 untreated). (burgos2023earlytreatmentwith pages 1-2)
- **SGLT2 inhibitor repurposing hypothesis (2024):** proposed mechanism includes limiting neuronal/astrocytic glucose entry (reducing glycogen substrate), reducing sodium-driven excitability, and promoting ketogenesis; currently hypothesis‑generating. (imbrici2024sodiumglucosecotransporter2inhibitors pages 1-3)

### 12.3 Visual evidence (preclinical application)
Figures in Donohue et al. (2023) provide a schematic for the glycogen/metabolic rationale and show reductions in Lafora body burden and epileptiform discharges after Gys1-ASO treatment in a mouse model, supporting the mechanistic application of glycogen synthase lowering. (donohue2023gys1antisensetherapy media 599505f0, donohue2023gys1antisensetherapy media 63d9a679)

## 13. Prevention
No primary prevention strategies exist beyond genetic counseling and reproductive planning for at-risk families; LD is Mendelian with autosomal recessive inheritance. (turnbull2016laforadisease. pages 1-2, pondrelli2021naturalhistoryof pages 1-2)

## 14. Other Species / Natural Disease
Animal models are referenced as recapitulating pathology/phenotype in reviews; detailed natural disease in non-human species was not retrieved in the evidence set for this run. (turnbull2016laforadisease. pages 1-2)

## 15. Model Organisms
- **Mouse knockout models (Epm2a−/−, Epm2b−/−)** recapitulate key neurological and histopathological features and are used for therapeutic testing (metformin, Gys1-ASO). (burgos2023earlytreatmentwith pages 1-2, donohue2023gys1antisensetherapy pages 1-2)
- A 2023 mechanistic study generated a **FLAG-tagged malin (Nhlrc1) mouse** to localize and study endogenous malin. (mitra2023laforintargetsmalin pages 1-2)

## Expert opinions / analysis (authoritative perspectives)
- **Astrocyte primacy:** Duran (2023) argues that identifying astrocytic Lafora bodies as a major aggregate pool “identify a primary role of astrocytes in the pathophysiology,” shifting target cell assumptions for therapy design. (duran2023roleofastrocytes pages 1-2)
- **Trial design implication:** The 2023 patient-level meta-analysis explicitly notes that genotype-defined functional impact (e.g., NHLRC1 PT/PT) should be considered when launching disease-modifying trials to interpret outcomes appropriately. (pondrelli2023prognosticvalueof pages 1-2, pondrelli2023prognosticvalueof pages 6-9)

## Key gaps / not available in this run
- MONDO ID and ICD-10/ICD-11 mappings were not retrieved from the available sources.
- Population carrier frequency estimates and gnomAD-based allele frequencies were not retrieved.
- Detailed per-phenotype frequency percentages (beyond survival/disability) were not captured in available excerpts.



References

1. (turnbull2016laforadisease. pages 1-2): Julie Turnbull, Erica Tiberia, Pasquale Striano, Pierre Genton, Stirling Carpenter, Cameron A. Ackerley, and Berge A. Minassian. Lafora disease. Epileptic disorders : international epilepsy journal with videotape, 18 S2:38-62, Sep 2016. URL: https://doi.org/10.1684/epd.2016.0842, doi:10.1684/epd.2016.0842. This article has 195 citations.

2. (pondrelli2021naturalhistoryof pages 1-2): Federica Pondrelli, Lorenzo Muccioli, Laura Licchetta, Barbara Mostacci, Corrado Zenesini, Paolo Tinuper, Luca Vignatelli, and Francesca Bisulli. Natural history of lafora disease: a prognostic systematic review and individual participant data meta-analysis. Orphanet Journal of Rare Diseases, Aug 2021. URL: https://doi.org/10.1186/s13023-021-01989-w, doi:10.1186/s13023-021-01989-w. This article has 62 citations and is from a peer-reviewed journal.

3. (NCT03876522 chunk 1):  Natural History and Functional Status Study of Patients With Lafora Disease. Ionis Pharmaceuticals, Inc.. 2019. ClinicalTrials.gov Identifier: NCT03876522

4. (NCT06609889 chunk 1): Berge Minassian. A Safety and Efficacy of Intrathecally Administered ION283 in Patients With Lafora Disease. Berge Minassian. 2024. ClinicalTrials.gov Identifier: NCT06609889

5. (pondrelli2023prognosticvalueof pages 1-2): Federica Pondrelli, Raffaella Minardi, Lorenzo Muccioli, Corrado Zenesini, Luca Vignatelli, Laura Licchetta, Barbara Mostacci, Paolo Tinuper, Craig W. Vander Kooi, Matthew S. Gentry, and Francesca Bisulli. Prognostic value of pathogenic variants in lafora disease: systematic review and meta-analysis of patient-level data. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02880-6, doi:10.1186/s13023-023-02880-6. This article has 16 citations and is from a peer-reviewed journal.

6. (duran2023roleofastrocytes pages 1-2): Jordi Duran. Role of astrocytes in the pathophysiology of lafora disease and other glycogen storage disorders. Cells, 12:722, Feb 2023. URL: https://doi.org/10.3390/cells12050722, doi:10.3390/cells12050722. This article has 9 citations.

7. (burgos2023earlytreatmentwith pages 1-2): Daniel F. Burgos, María Machío-Castello, Nerea Iglesias-Cabeza, Beatriz G. Giráldez, Juan González-Fernández, Gema Sánchez-Martín, Marina P. Sánchez, and José M. Serratosa. Early treatment with metformin improves neurological outcomes in lafora disease. Neurotherapeutics, 20:230-244, Jan 2023. URL: https://doi.org/10.1007/s13311-022-01304-w, doi:10.1007/s13311-022-01304-w. This article has 32 citations and is from a peer-reviewed journal.

8. (NCT00007124 chunk 1):  Ketogenic Diet in Lafora Disease. National Institute of Neurological Disorders and Stroke (NINDS). 2000. ClinicalTrials.gov Identifier: NCT00007124

9. (imbrici2024sodiumglucosecotransporter2inhibitors pages 1-3): Paola Imbrici, Giuseppe d’Orsi, Massimo Carella, Orazio Nicolotti, Annamaria De Luca, Cosimo Damiano Altomare, and Antonella Liantonio. Sodium-glucose cotransporter-2 inhibitors: a potential novel treatment for lafora disease? Pharmacological Research, 199:107012, Jan 2024. URL: https://doi.org/10.1016/j.phrs.2023.107012, doi:10.1016/j.phrs.2023.107012. This article has 5 citations and is from a highest quality peer-reviewed journal.

10. (skurat2024impairedmalinexpression pages 1-2): Alexander V. Skurat, Dyann M. Segvich, Christopher J. Contreras, Yueh-Chiang Hu, Thomas D. Hurley, Anna A. DePaoli-Roach, and Peter J. Roach. Impaired malin expression and interaction with partner proteins in lafora disease. Journal of Biological Chemistry, 300:107271, May 2024. URL: https://doi.org/10.1016/j.jbc.2024.107271, doi:10.1016/j.jbc.2024.107271. This article has 10 citations and is from a domain leading peer-reviewed journal.

11. (turnbull2016laforadisease. pages 3-4): Julie Turnbull, Erica Tiberia, Pasquale Striano, Pierre Genton, Stirling Carpenter, Cameron A. Ackerley, and Berge A. Minassian. Lafora disease. Epileptic disorders : international epilepsy journal with videotape, 18 S2:38-62, Sep 2016. URL: https://doi.org/10.1684/epd.2016.0842, doi:10.1684/epd.2016.0842. This article has 195 citations.

12. (aggradi2023laforadiseasea pages 1-2): Carola Rita Ferrari Aggradi, Martina Rimoldi, Gloria Romagnoli, Daniele Velardo, Megi Meneri, Davide Iacobucci, Michela Ripolone, Laura Napoli, Patrizia Ciscato, Maurizio Moggio, Giacomo Pietro Comi, Dario Ronchi, Stefania Corti, and Elena Abati. Lafora disease: a case report and evolving treatment advancements. Brain Sciences, 13:1679, Dec 2023. URL: https://doi.org/10.3390/brainsci13121679, doi:10.3390/brainsci13121679. This article has 8 citations.

13. (aggradi2023laforadiseasea pages 2-4): Carola Rita Ferrari Aggradi, Martina Rimoldi, Gloria Romagnoli, Daniele Velardo, Megi Meneri, Davide Iacobucci, Michela Ripolone, Laura Napoli, Patrizia Ciscato, Maurizio Moggio, Giacomo Pietro Comi, Dario Ronchi, Stefania Corti, and Elena Abati. Lafora disease: a case report and evolving treatment advancements. Brain Sciences, 13:1679, Dec 2023. URL: https://doi.org/10.3390/brainsci13121679, doi:10.3390/brainsci13121679. This article has 8 citations.

14. (turnbull2012earlyonsetlaforabody pages 4-5): Julie Turnbull, Jean-Marie Girard, Hannes Lohi, Elayne M. Chan, Peixiang Wang, Erica Tiberia, Salah Omer, Mushtaq Ahmed, Christopher Bennett, Aruna Chakrabarty, Atul Tyagi, Yan Liu, Nela Pencea, XiaoChu Zhao, Stephen W. Scherer, Cameron A. Ackerley, and Berge A. Minassian. Early-onset lafora body disease. Brain, 135:2684-2698, Aug 2012. URL: https://doi.org/10.1093/brain/aws205, doi:10.1093/brain/aws205. This article has 113 citations and is from a highest quality peer-reviewed journal.

15. (pondrelli2023prognosticvalueof pages 6-9): Federica Pondrelli, Raffaella Minardi, Lorenzo Muccioli, Corrado Zenesini, Luca Vignatelli, Laura Licchetta, Barbara Mostacci, Paolo Tinuper, Craig W. Vander Kooi, Matthew S. Gentry, and Francesca Bisulli. Prognostic value of pathogenic variants in lafora disease: systematic review and meta-analysis of patient-level data. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02880-6, doi:10.1186/s13023-023-02880-6. This article has 16 citations and is from a peer-reviewed journal.

16. (donohue2023gys1antisensetherapy pages 1-2): Katherine J. Donohue, Bethany Fitzsimmons, Ronald C. Bruntz, Kia H. Markussen, Lyndsay E.A. Young, Harrison A. Clarke, Peyton T. Coburn, Laiken E. Griffith, William Sanders, Jack Klier, Sara N. Burke, Andrew P. Maurer, Berge A. Minassian, Ramon C. Sun, Holly B. Kordasiewisz, and Matthew S. Gentry. Gys1 antisense therapy prevents disease-driving aggregates and epileptiform discharges in a lafora disease mouse model. Neurotherapeutics, 20:1808-1819, Oct 2023. URL: https://doi.org/10.1007/s13311-023-01434-9, doi:10.1007/s13311-023-01434-9. This article has 18 citations and is from a peer-reviewed journal.

17. (mitra2023laforintargetsmalin pages 1-2): Sharmistha Mitra, Baozhi Chen, Peixiang Wang, Erin E. Chown, Mathew Dear, Dikran R. Guisso, Ummay Mariam, Jun Wu, Emrah Gumusgoz, and Berge A. Minassian. Laforin targets malin to glycogen in lafora progressive myoclonus epilepsy. Disease Models &amp; Mechanisms, Jan 2023. URL: https://doi.org/10.1242/dmm.049802, doi:10.1242/dmm.049802. This article has 19 citations and is from a domain leading peer-reviewed journal.

18. (d’orsi2025clinicalcourseand pages 1-2): G. d’Orsi, Maria Teresa Di Claudio, A. Liantonio, P. Imbrici, C. Altomare, O. Palumbo, P. Palumbo, Mario Benvenuto, Nicola Gambacorta, G. Lolli, Francesca Cinzia Giuseppe Lidia Valentina Laura Raffaele Lor Bisulli Costa Damante Di Vito Imperatore Licchetta, F. Bisulli, Cinzia Costa, Giuseppe Damante, L. Di Vito, Valentina Imperatore, L. Licchetta, Raffaele Lodi, L. Muccioli, P. Mantuano, Serena Mazzone, Roberto Michelucci, E. Pasini, Paolo Prontera, M. Tappatà, L. Vignatelli, C. Zenesini, and M. Carella. Clinical course and management challenges in lafora disease: a narrative analysis in an apulian cohort. Orphanet Journal of Rare Diseases, Aug 2025. URL: https://doi.org/10.1186/s13023-025-03976-x, doi:10.1186/s13023-025-03976-x. This article has 0 citations and is from a peer-reviewed journal.

19. (NCT05930223 chunk 1):  Intravenous VAL-1221 Lafora Expanded Access Protocol. Parasail, LLC. ClinicalTrials.gov Identifier: NCT05930223

20. (donohue2023gys1antisensetherapy media 599505f0): Katherine J. Donohue, Bethany Fitzsimmons, Ronald C. Bruntz, Kia H. Markussen, Lyndsay E.A. Young, Harrison A. Clarke, Peyton T. Coburn, Laiken E. Griffith, William Sanders, Jack Klier, Sara N. Burke, Andrew P. Maurer, Berge A. Minassian, Ramon C. Sun, Holly B. Kordasiewisz, and Matthew S. Gentry. Gys1 antisense therapy prevents disease-driving aggregates and epileptiform discharges in a lafora disease mouse model. Neurotherapeutics, 20:1808-1819, Oct 2023. URL: https://doi.org/10.1007/s13311-023-01434-9, doi:10.1007/s13311-023-01434-9. This article has 18 citations and is from a peer-reviewed journal.

21. (donohue2023gys1antisensetherapy media 63d9a679): Katherine J. Donohue, Bethany Fitzsimmons, Ronald C. Bruntz, Kia H. Markussen, Lyndsay E.A. Young, Harrison A. Clarke, Peyton T. Coburn, Laiken E. Griffith, William Sanders, Jack Klier, Sara N. Burke, Andrew P. Maurer, Berge A. Minassian, Ramon C. Sun, Holly B. Kordasiewisz, and Matthew S. Gentry. Gys1 antisense therapy prevents disease-driving aggregates and epileptiform discharges in a lafora disease mouse model. Neurotherapeutics, 20:1808-1819, Oct 2023. URL: https://doi.org/10.1007/s13311-023-01434-9, doi:10.1007/s13311-023-01434-9. This article has 18 citations and is from a peer-reviewed journal.
