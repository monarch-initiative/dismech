---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T17:36:27.145520'
end_time: '2026-05-12T17:46:44.508259'
duration_seconds: 617.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth Disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease** covering all of the
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
- **Disease Name:** Charcot-Marie-Tooth Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease** covering all of the
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


## Comprehensive Disease Characteristics Report: Charcot–Marie–Tooth Disease (CMT)

**Target disease:** Charcot–Marie–Tooth disease (CMT) (hereditary motor and sensory neuropathy spectrum; Mendelian).

**Evidence note / limitations:** The tool-accessible corpus for this run contains high-quality peer‑reviewed clinical genetics, outcomes, and treatment/trial sources (2023–2024 emphasized), but it does **not** include direct pulls from OMIM/Orphanet/MeSH/MONDO authority pages. Therefore, **formal identifiers (OMIM/ORPHA/MeSH/MONDO/ICD)** cannot be reliably populated from this evidence set and are flagged as *not available from retrieved sources*.

---

# 1. Disease Information

### 1.1 Concise overview
Charcot–Marie–Tooth disease (CMT) is among the most common inherited peripheral neuropathies and is **genetically heterogeneous**, with reports of **>130 disease-causing genes** in modern diagnostic series. (record2024wholegenomesequencing pages 1-2)

CMT and related inherited neuropathies are commonly classified clinically/electrophysiologically into demyelinating (CMT1), axonal (CMT2), and intermediate forms, with additional related categories such as hereditary motor neuropathy (HMN), hereditary sensory neuropathy (HSN), and hereditary neuropathy with liability to pressure palsies (HNPP). In a large specialist-center cohort (2009–2023; n=1515), the clinical distribution included **CMT1 41.0%**, **CMT2 19.4%**, **intermediate CMT 13.5%**, **HMN 9.2%**, **HSN 6.1%**, **HNPP 4.8%**, and others. (record2024wholegenomesequencing pages 1-2)

### 1.2 Common synonyms / alternate names
Within this evidence set, CMT is discussed under:
- **Charcot–Marie–Tooth disease (CMT)**
- **CMT1A** (most common genetic subtype; PMP22 duplication)
- **CMTX1** (GJB1)
- **HNPP** (PMP22 deletion)
- **“inherited peripheral neuropathies / inherited neuropathies”** (umbrella term used in therapeutic and modeling literature) (record2024wholegenomesequencing pages 1-2, okamoto2023thecurrentstate pages 1-2, mandarakas2024multicentervalidationof pages 1-2)

### 1.3 Key identifiers (OMIM, Orphanet, ICD, MeSH, MONDO)
Not extractable from the retrieved evidence in this run; requires direct querying of OMIM/Orphanet/MONDO/MeSH/ICD sources.

### 1.4 Evidence source type
Most information in this report is derived from:
- **Aggregated disease-level resources** (large specialty-center series; multicenter validation cohorts; reviews). (record2024wholegenomesequencing pages 1-2, okamoto2023thecurrentstate pages 1-2, mandarakas2024multicentervalidationof pages 1-2)
- **Clinical trial registry records** (ClinicalTrials.gov). (NCT04762758 chunk 1, NCT06328712 chunk 1, NCT02579759 chunk 1, NCT05361031 chunk 2, NCT03023540 chunk 2)

---

# 2. Etiology

## 2.1 Disease causal factors
CMT is primarily a **genetic** disorder caused by pathogenic variants affecting peripheral nerve myelination (Schwann-cell biology) and/or axonal structure/function.

Across modern clinical cohorts, the most common genetic causes are:
- **PMP22 duplication (CMT1A)**
- **GJB1 variants (CMTX1)**
- **PMP22 deletion (HNPP)**
- **MFN2 variants (CMT2A)** (record2024wholegenomesequencing pages 1-2)

In the 1515-patient Brain 2024 specialist series, among solved cases (n=1165), the leading diagnoses were **PMP22 duplication 43.3%**, **GJB1 13.0%**, **PMP22 deletion 6.2%**, **MFN2 3.9%**. (record2024wholegenomesequencing pages 1-2)

## 2.2 Risk factors
### Genetic risk
The dominant “risk factor” is carrying a **pathogenic germline variant** in one of many CMT genes. The contribution of a small number of genes is particularly large: a 2023 diagnostic study emphasizes that **PMP22, GJB1, MFN2, and MPZ** account for “nearly 80%” of genetically inherited CMT in their summary framing. (ceylan2023highdiagnosticyield pages 1-2)

### Environmental / non-genetic risk factors
The available evidence set does not contain robust epidemiologic analyses of environmental contributors to CMT onset; however, CMT severity can be affected by clinical course and management and potentially by exposures that worsen neuropathy (e.g., avoidance of neurotoxic medications is referenced as an exclusion in a long-term PXT3003 extension protocol). (NCT03023540 chunk 2)

## 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence set.

## 2.4 Gene–environment interactions
Direct gene–environment interaction studies were not present in the retrieved evidence.

---

# 3. Phenotypes

## 3.1 Core phenotype spectrum (high-level)
Although phenotype is heterogeneous, commonly highlighted clinical manifestations include distal weakness and sensory impairment with functional limitations. Subtype-specific cohorts demonstrate additional features (e.g., in CMT4J). (record2024wholegenomesequencing pages 1-2)

### Example: CMT4J (FIG4-related) clinical features
A 2024 Neurology cross-sectional cohort (n=19; 14 pediatric, 5 adult) reported:
- Most frequent neuromuscular symptoms: **gross motor delay** and **distal > proximal muscle weakness** (14/19).
- Most common non-neuromuscular symptoms: **cognitive** and **respiratory deficits** (each 8/19).
- Nonuniform slowing of conduction velocities in 6 patients; asymmetric weakness in 2 patients.
- CMTPedS and QoL/adaptive behavior scales affected in most patients; neurofilament light correlated with CMTPedS in pediatrics. (mandarakas2024multicentervalidationof pages 5-6)

## 3.2 Phenotype characteristics (onset, progression, severity)
CMT is typically chronic and slowly progressive; formal onset/progression metrics vary by genotype and are not comprehensively quantified in the extracted evidence set. However, CMT4J demonstrates childhood disease burden with motor delay and multisystem features. (mandarakas2024multicentervalidationof pages 5-6)

## 3.3 Quality of life impact
The CMT functional burden is captured in validated functional measures such as the **CMT-FOM** (adult CMT1A), which discriminates patients by self-reported trips/falls, unsteady ankles, tremor, and hand weakness. (mandarakas2024multicentervalidationof pages 1-2)

## 3.4 Suggested HPO terms (non-exhaustive; ontology mapping suggestions)
The evidence set supports mapping to common CMT manifestations; suggested HPO terms include:
- **Distal muscle weakness** (HP:0002460)
- **Muscle atrophy** (HP:0003202)
- **Pes cavus** (HP:0001761)
- **Areflexia** (HP:0001284)
- **Peripheral neuropathy** (HP:0009830)
- **Gait abnormality** (HP:0001288)
- **Gross motor delay** (HP:0002194) — particularly supported in CMT4J (mandarakas2024multicentervalidationof pages 5-6)
- **Respiratory insufficiency** (HP:0002093) and **Cognitive impairment** (HP:0100543) — supported for CMT4J (mandarakas2024multicentervalidationof pages 5-6)

(These HPO IDs are ontology suggestions; they are not explicitly listed in the retrieved sources and should be verified against HPO.)

---

# 4. Genetic / Molecular Information

## 4.1 Causal genes (high-frequency examples)
Large contemporary diagnostic work shows that a limited set of genes accounts for a substantial fraction of diagnoses:
- **PMP22**: duplication → CMT1A; deletion → HNPP (record2024wholegenomesequencing pages 1-2)
- **GJB1**: CMTX1 (record2024wholegenomesequencing pages 1-2)
- **MFN2**: CMT2A (record2024wholegenomesequencing pages 1-2)

A 2023 review further summarizes that, among positive molecular findings in a large commercial dataset, **PMP22 duplications and deletions dominated**, with next most frequent positives in **GJB1, MPZ, MFN2**, and that **94.9%** of positives were in **PMP22/GJB1/MPZ/MFN2**. (okamoto2023thecurrentstate pages 1-2)

## 4.2 Pathogenic variant classes
Common variant classes implicated in CMT include:
- **Copy-number variants (CNVs)**, particularly **PMP22 duplication** (CMT1A) and **PMP22 deletion** (HNPP), typically detected via MLPA or similar assays. (ceylan2023highdiagnosticyield pages 1-2, ceylan2023highdiagnosticyield pages 2-4, record2024wholegenomesequencing pages 2-3)
- **Single nucleotide variants and small indels** across many genes, increasingly detected by targeted NGS panels, WES, and WGS with ACMG-based classification. (record2024wholegenomesequencing pages 1-2, ceylan2023highdiagnosticyield pages 1-2)

## 4.3 Modifier genes / epigenetics
The retrieved evidence set does not provide definitive modifier-gene or epigenetic mechanisms for CMT at a knowledge-base-ready level.

---

# 5. Environmental Information

No disease-specific environmental causal factors were identified in the retrieved evidence set. Environmental relevance is most clearly implicit through **avoidance of concomitant neurotoxic drugs** in trial protocols and through supportive care/rehabilitation. (NCT03023540 chunk 2)

---

# 6. Mechanism / Pathophysiology

## 6.1 Core mechanistic principles across common subtypes
### PMP22 overexpression (CMT1A)
A major disease mechanism in CMT1A is **increased PMP22 dosage** (duplication), motivating disease-modifying strategies aiming to **downregulate PMP22** (siRNA, ASO, AAV-mediated silencing) and to improve axonal function. (okamoto2023thecurrentstate pages 16-17, NCT02579759 chunk 1)

### MPZ (CMT1B)
A 2024 review focused on CMT1B describes that MPZ mutations can lead to **protein misfolding, UPR activation, ER stress, or mistrafficking**, motivating approaches such as gene therapy and proteostasis modulation (review-level mechanistic framing). (mcculloch2024navigatingthelandscape pages 22-23)

### Inflammation as a potential co-mechanism
A 2024 perspective review notes that inflammation and neurodegeneration may coexist in some CMTs and discusses implications for immunomodulatory approaches in selected patients. (yalcouye2023geneticsofhearing pages 163-166)

## 6.2 Pathways / processes / ontology suggestions
Supported or strongly implied mechanisms include:
- **Myelination / Schwann cell biology** (GO:0042552 myelination; CL:0000218 Schwann cell)
- **Axon maintenance and degeneration** (GO:0007409 axonogenesis; GO:0008050 axon guidance)
- **ER stress / unfolded protein response** for MPZ-related disease (GO:0030968 endoplasmic reticulum unfolded protein response)

(These GO/CL suggestions should be validated against ontology references; not enumerated directly in the retrieved sources.)

---

# 7. Anatomical Structures Affected

Primary system: **peripheral nervous system** (peripheral nerves; motor and sensory fibers). (record2024wholegenomesequencing pages 1-2)

Key tissue/cell types implicated by the genetic targets and mechanistic discussions:
- **Peripheral nerves** (UBERON:0000010 peripheral nerve)
- **Schwann cells** (CL:0000218)
- **Peripheral neurons / axons** (CL:0000540 neuron; GO cellular components such as axon)

---

# 8. Temporal Development

CMT is chronic and typically slowly progressive across many subtypes, creating challenges for detecting change in clinical trials and motivating sensitive outcome measures and biomarkers. (okamoto2023thecurrentstate pages 12-14, mandarakas2024multicentervalidationof pages 1-2)

---

# 9. Inheritance and Population

## 9.1 Epidemiology
Modern sources in this evidence set provide broad prevalence ranges:
- A large specialist diagnostic cohort cites estimated prevalence **1 in 2,500 to 1 in 10,000**. (record2024wholegenomesequencing pages 1-2)
- A 2023 treatment review states incidence on the order of **~10–40 per 100,000** (as reported in that review). (okamoto2023thecurrentstate pages 1-2)

## 9.2 Subtype frequencies (genetic)
In the Brain 2024 specialist cohort, among solved cases (n=1165) the most common diagnoses were:
- **PMP22 duplication (CMT1A): 43.3%**
- **GJB1 (CMTX1): 13.0%**
- **PMP22 deletion (HNPP): 6.2%**
- **MFN2 (CMT2A): 3.9%** (record2024wholegenomesequencing pages 1-2)

---

# 10. Diagnostics

## 10.1 Current understanding: tiered genetic testing is central
A consistent theme across 2023–2024 evidence is the value of an algorithmic, tiered testing strategy:
- **First tier:** targeted **PMP22 CNV detection (e.g., MLPA)** given high prevalence of duplication/deletion.
- **Second tier:** targeted **NGS gene panels**.
- **Escalation:** **WES/WGS** (often via virtual panels) and multidisciplinary review, particularly for unsolved cases. (ceylan2023highdiagnosticyield pages 1-2, record2024wholegenomesequencing pages 2-3)

## 10.2 Diagnostic yield statistics
### MLPA, panel NGS, WES (single-center algorithmic series)
In a 2023 hereditary neuropathy series (n=64 suspected CMT):
- **MLPA** diagnosed **39% (25/64)** (14 duplications, 11 deletions).
- In those proceeding to **targeted NGS panels**, yield was **36% (18/50)**.
- **WES** solved **80% (4/5)** of panel-negative cases. (ceylan2023highdiagnosticyield pages 1-2, ceylan2023highdiagnosticyield pages 2-4)

### Large specialist-center yield and contribution of WGS
In the Brain 2024 specialist cohort (n=1515):
- Overall genetic diagnosis rate **76.9% (1165/1515)**.
- WGS in the UK 100,000 Genomes Project subgroup had a “true” diagnostic rate **19.7% (46/233)**; overall WGS “uplift” for the entire cohort was **3.5%**. (record2024wholegenomesequencing pages 1-2)

## 10.3 Outcome measures in clinical evaluation
The Brain 2024 cohort notes use of validated scales including CMT Examination Score and CMT Neuropathy Score in phenotyping. (record2024wholegenomesequencing pages 1-2)

---

# 11. Outcome / Prognosis

Robust survival and life expectancy statistics were not present in the retrieved evidence set. The disease burden is better captured by validated functional scales and quality-of-life impact.

## 11.1 Validated outcome measures (2024 update)
### CMT-FOM (adult CMT1A)
A 2024 multicenter validation established the **CMT-Functional Outcome Measure (CMT-FOM)** for adult CMT1A (PMP22 duplication):
- Cohort: **n=214**, ages 18–75, 58% female across US/UK/Italy. (mandarakas2024multicentervalidationof pages 1-2)
- Structure: **12-item**, ~30 minutes, **0–100 interval score** (0 unaffected → 100 severe). (mandarakas2024multicentervalidationof pages 1-2, mandarakas2024multicentervalidationof pages 6-9)
- Psychometrics: excellent interrater reliability **ICC 0.992**; convergent validity with **CMTES-R (r=0.643)** and **ONLS (r=0.516)**. (mandarakas2024multicentervalidationof pages 1-2, mandarakas2024multicentervalidationof pages 6-9)

---

# 12. Treatment

## 12.1 Current standard of care (real-world implementation)
No disease-curative pharmacotherapy is established in the evidence set; current management is largely symptomatic/supportive and includes multidisciplinary approaches. Reviews emphasize the absence of definitive pharmacologic treatment and the need for sensitive endpoints due to slow progression. (okamoto2023thecurrentstate pages 12-14)

## 12.2 Disease-modifying and advanced therapeutics (pipeline)
### (A) PXT3003 (fixed-dose combination; oral)
**What it is:** PXT3003 is described in Phase III trials as an oral fixed-dose combination of **(RS)-baclofen, naltrexone HCl, and D-sorbitol** intended to limit PMP22 production and protect/improve axonal function (trial registry description). (NCT04762758 chunk 1, NCT02579759 chunk 1)

**Key trials (ClinicalTrials.gov):**
- **PLEO-CMT (NCT02579759)**: Phase 3, randomized, double-blind, placebo-controlled; **enrollment 323**; **completed**. Primary endpoint: mean ONLS at months 12 and 15; included 10MWT and CMTNS-v2 derived measures among secondary endpoints; a quality issue caused premature discontinuation of one dose arm in 2017. (NCT02579759 chunk 1)
- **PREMIER (NCT04762758)**: Phase 3, randomized, double-blind; planned **~350**; status reported as active not recruiting; primary outcomes include modified ONLS and 10mWT through month 15; estimated primary completion April 2024. (NCT04762758 chunk 1)

**MAXO suggestions:** combination pharmacotherapy (NCIT:C15986 drug therapy), gait rehabilitation adjunct (MAXO:0000011 physical therapy), functional outcome assessment (MAXO:0000745 clinical assessment).

### (B) PMP22 lowering (gene silencing / RNA therapeutics; preclinical)
A 2023 review summarizes multiple preclinical approaches targeting PMP22 overexpression, including siRNA formulations, AAV-mediated silencing, and ASOs that reversed CMT1A features in rodent models (review-level summary with multiple cited studies). (okamoto2023thecurrentstate pages 16-17)

### (C) Gene therapy (examples)
A 2023 gene-therapy advances review notes that proposed approaches include gene replacement/addition, silencing, modification, and editing, with targeting of Schwann cells and/or neurons depending on subtype. (dong2024currenttreatmentmethods pages 2-4)

**Example clinical gene-therapy trial:**
- **scAAV1.tMCK.NTF3 for CMT1A (NCT03520751)**: Phase I/IIa trial record describes AAV1-based NTF3 delivery with detailed eligibility and immune-exclusion criteria (AAV1 antibody titers). Enrollment/status/endpoints were not available from the extracted chunk. (NCT03520751 chunk 2)

### (D) HGF plasmid therapy (VM202 / Engensis)
ClinicalTrials.gov record **NCT05361031** evaluates Engensis (VM202) in genetically confirmed CMT1A, with outcomes including change in nerve conduction velocity and HGF antibody generation over ~270 days; eligibility includes mild-to-moderate disease by CMTNS v2. (NCT05361031 chunk 2)

### (E) Cell therapy (mesenchymal stromal cells)
ClinicalTrials.gov record **NCT06328712** (Phase 1b) evaluates EN001 (allogeneic Wharton’s jelly-derived MSCs) in CMT1A, completed with **n=6**, with primary safety endpoints (DLTs) and multiple secondary exploratory efficacy outcomes including CMTNSv2, CMTES, electrophysiology, MRI, and SF‑36. (NCT06328712 chunk 1)

---

# 13. Prevention

Primary prevention of genetic CMT is not generally applicable in the classical public-health sense; preventive strategy is largely:
- **Genetic counseling** and cascade testing (not directly evidenced in retrieved sources).
- **Avoidance of exposures/medications that could worsen neuropathy**, suggested indirectly by trial exclusion criteria for “neurotoxic drugs” in the PXT3003 extension protocol. (NCT03023540 chunk 2)

---

# 14. Other Species / Natural Disease

The retrieved evidence set did not include a structured discussion of naturally occurring CMT analogs in companion animals (OMIA/VetCompass).

---

# 15. Model Organisms

The retrieved evidence emphasizes that treatment development has been tested largely in **in vitro and rodent models**, with discussion that larger-animal models may help translate dosing/safety. (dong2024currenttreatmentmethods pages 2-4)

A 2024 CMT1B-focused review highlights diverse model systems used for inherited neuropathies, including iPSC-derived organoids and multiple mouse models relevant to myelin disorders and proteostasis pathways. (mcculloch2024navigatingthelandscape pages 22-23)

---

# Consolidated Evidence Tables

| Topic | Key data points (numbers) | Source (first author year, journal) | URL/DOI |
|---|---|---|---|
| Core disease definition and classification | Charcot-Marie-Tooth disease (CMT) is one of the most common inherited peripheral neuropathies; genetically heterogeneous with **>130 disease-causing genes** reported. In a 1,515-patient specialist cohort, subtype distribution was **CMT1 41.0% (621/1515)**, **CMT2 19.4% (294/1515)**, **intermediate CMT 13.5% (205/1515)**, **HMN 9.2% (139/1515)**, **HSN 6.1% (93/1515)**, **sensory ataxic neuropathy 2.5% (38/1515)**, **HNPP 4.8% (72/1515)**, **complex neuropathy 3.5% (53/1515)**. Estimated prevalence reported as **1 in 2,500 to 1 in 10,000**; another review gives **10–40 per 100,000**. (record2024wholegenomesequencing pages 1-2, okamoto2023thecurrentstate pages 1-2) | Record 2024, *Brain*; Okamoto 2023, *Genes* | https://doi.org/10.1093/brain/awae064; https://doi.org/10.3390/genes14071391 |
| Most common genetic causes in contemporary cohort | Among solved cases (**n=1165**), most common diagnoses were **PMP22 duplication/CMT1A 43.3% (505/1165)**, **GJB1/CMTX1 13.0% (151/1165)**, **PMP22 deletion/HNPP 6.2% (72/1165)**, **MFN2/CMT2A 3.9% (46/1165)**. In the full 1,515-case cohort, PMP22 duplication represented **33.3% overall (505/1515)**. (record2024wholegenomesequencing pages 1-2, record2024wholegenomesequencing pages 2-3) | Record 2024, *Brain* | https://doi.org/10.1093/brain/awae064 |
| Most common genetic causes in review cohorts | Review summary of earlier cohorts: **CMT1A/PMP22 55%**, **CMTX1/GJB1 15.2%**, **HNPP 9.2%**, **CMT1B/MPZ 8.5%**, **CMT2A/MFN2 4%**. In a large commercial-lab cohort, genetic anomalies were found in **18.5% (3312/17,880)**; among positives: **PMP22 duplications 56.7%**, **PMP22 deletions 21.9%**, **GJB1 6.7%**, **MPZ 5.3%**, **MFN2 4.3%**; **94.9%** of positives were in **PMP22/GJB1/MPZ/MFN2**. (okamoto2023thecurrentstate pages 1-2) | Okamoto 2023, *Genes* | https://doi.org/10.3390/genes14071391 |
| Diagnostic yield: MLPA first-tier CNV testing | In suspected CMT (**n=64**), **MLPA diagnosed 25/64 (39%)**; specifically **14 PMP22 duplications** and **11 PMP22 deletions**. MLPA remains the preferred test for common **PMP22** CNVs causing CMT1A/HNPP. (ceylan2023highdiagnosticyield pages 1-2, ceylan2023highdiagnosticyield pages 2-4, record2024wholegenomesequencing pages 2-3) | Ceylan 2023, *Rev Assoc Med Bras*; Record 2024, *Brain* | https://doi.org/10.1590/1806-9282.20220929; https://doi.org/10.1093/brain/awae064 |
| Diagnostic yield: targeted NGS panels | After negative PMP22 MLPA, **50** patients underwent targeted NGS; panel diagnostic yield was **36% (18/50)** for pathogenic/likely pathogenic variants. Authors recommend algorithmic testing guided by phenotype, pedigree, and inheritance pattern. (ceylan2023highdiagnosticyield pages 1-2, ceylan2023highdiagnosticyield pages 2-4) | Ceylan 2023, *Rev Assoc Med Bras* | https://doi.org/10.1590/1806-9282.20220929 |
| Diagnostic yield: WES | In the same algorithmic series, **WES diagnosed 4/5 (80%)** panel-negative cases, with higher yield in the childhood group. (ceylan2023highdiagnosticyield pages 1-2) | Ceylan 2023, *Rev Assoc Med Bras* | https://doi.org/10.1590/1806-9282.20220929 |
| Diagnostic yield: contemporary overall genetics and WGS uplift | Single-center specialist cohort overall molecular diagnosis: **76.9% (1165/1515)**; highest in **CMT1 96.8%**, **intermediate CMT 81.0%**, **HSN 69.9%**; **<50%** in CMT2/HMN/complex neuropathies. In UK 100,000 Genomes Project cases (**n=233**), reported WGS diagnoses were **31.8% (74/233)**, but true WGS diagnostic rate after excluding otherwise-diagnosed cases was **19.7% (46/233)**. Overall WGS diagnostic uplift for the full cohort was **3.5%**. (record2024wholegenomesequencing pages 1-2, record2024wholegenomesequencing pages 2-3) | Record 2024, *Brain* | https://doi.org/10.1093/brain/awae064 |
| Outcome measure: CMT-FOM cohort and structure | Multicenter validation in adult CMT1A: **n=214**, age **18–75 years**, **58% female**; recruited from **US 130**, **UK 52**, **Italy 32**. Final instrument is a **12-item** disease-specific measure covering strength, upper/lower limb function, balance, and mobility; transformed to a **0–100** interval scale (**0 = unaffected; 100 = severely affected**). Mean score **47.7 ± 10.2**, range **17–83**. (mandarakas2024multicentervalidationof pages 1-2, mandarakas2024multicentervalidationof pages 5-6, mandarakas2024multicentervalidationof pages 6-9) | Mandarakas 2024, *Neurology* | https://doi.org/10.1212/wnl.0000000000207963 |
| Outcome measure: CMT-FOM psychometrics | Good Rasch model fit (**χ² probability 0.15**), internal consistency **PSI 0.82**, no floor/ceiling effects, excellent inter-rater reliability **ICC 0.992 (95% CI 0.979–0.998)**. Convergent validity: correlation with **CMTES-R r=0.643, p<0.001** and **ONLS r=0.516, p<0.001**; also correlated with gait assessment (**r=0.65, p<0.001**). Initial 13-item version showed **Cronbach α=0.84** before Rasch refinement to 12 items. (mandarakas2024multicentervalidationof pages 1-2, mandarakas2024multicentervalidationof pages 3-5, mandarakas2024multicentervalidationof pages 6-9) | Mandarakas 2024, *Neurology* | https://doi.org/10.1212/wnl.0000000000207963 |
| Other validated/used outcome measures in CMT trials | Established measures referenced for CMT include **CMTNSv1**, **CMTNSv2**, **Rasch-modified CMTNSv2/CMTES-R**, and **ONLS**. Review notes limited sensitivity of older CMTNS versions and increasing use of Rasch-modified scales and biomarkers. (okamoto2023thecurrentstate pages 12-14, mandarakas2024multicentervalidationof pages 2-3) | Okamoto 2023, *Genes*; Mandarakas 2024, *Neurology* | https://doi.org/10.3390/genes14071391; https://doi.org/10.1212/wnl.0000000000207963 |


*Table: This table condenses high-yield facts on Charcot-Marie-Tooth disease classification, major causal genes, diagnostic yields across testing modalities, and validated outcome-measure psychometrics. It is useful as a quick reference for disease knowledge base curation and evidence-backed clinical context.*

---

# Recent Developments (2023–2024 highlights)

1. **Whole-genome sequencing in routine care:** WGS implementation (e.g., via UK NHS/100KGP) provides incremental diagnostic uplift and highlights the value of access to raw WGS for unsolved cases; large single-center yield reached **76.9%** overall. (record2024wholegenomesequencing pages 1-2)
2. **Outcome measures readiness:** The **CMT-FOM** was multicenter-validated in 2024 to support upcoming CMT1A trials, with strong reliability and validity metrics. (mandarakas2024multicentervalidationof pages 1-2, mandarakas2024multicentervalidationof pages 6-9)
3. **Late-stage pharmacologic development:** Multiple Phase III trials of **PXT3003** continue to use functional endpoints (mONLS, 10mWT) and longer follow-up windows consistent with slow progression. (NCT04762758 chunk 1, NCT02579759 chunk 1)
4. **Therapeutic modality expansion:** Reviews in 2023–2024 emphasize gene therapy and gene silencing as a major direction (PMP22 silencing; AAV-based strategies), with translation challenges remaining. (okamoto2023thecurrentstate pages 16-17, dong2024currenttreatmentmethods pages 2-4)

---

# URLs and publication dates (from evidence)

- Record et al., *Brain* (advance access Mar 2024): https://doi.org/10.1093/brain/awae064 (record2024wholegenomesequencing pages 1-2)
- Mandarakas et al., *Neurology* (Feb 2024): https://doi.org/10.1212/wnl.0000000000207963 (mandarakas2024multicentervalidationof pages 1-2)
- Okamoto & Takashima, *Genes* (Jul 2023): https://doi.org/10.3390/genes14071391 (okamoto2023thecurrentstate pages 1-2)
- Ceylan et al., *Rev Assoc Med Bras* (Feb 2023): https://doi.org/10.1590/1806-9282.20220929 (ceylan2023highdiagnosticyield pages 1-2)
- ClinicalTrials.gov: PREMIER NCT04762758 (posted/maintained by sponsor; started 2021-03-30 per record): https://clinicaltrials.gov/study/NCT04762758 (NCT04762758 chunk 1)
- ClinicalTrials.gov: PLEO-CMT NCT02579759: https://clinicaltrials.gov/study/NCT02579759 (NCT02579759 chunk 1)
- ClinicalTrials.gov: EN001 NCT06328712: https://clinicaltrials.gov/study/NCT06328712 (NCT06328712 chunk 1)
- ClinicalTrials.gov: VM202/Engensis NCT05361031: https://clinicaltrials.gov/study/NCT05361031 (NCT05361031 chunk 2)

---

## Appendix: Suggested ontology terms (to be validated)
- **Disease:** CMT (MONDO/OMIM/Orphanet identifiers not retrieved in this run)
- **HPO:** distal muscle weakness; pes cavus; areflexia; gross motor delay (CMT4J); respiratory deficits (CMT4J) (mandarakas2024multicentervalidationof pages 5-6)
- **GO:** myelination; axon maintenance; unfolded protein response
- **CL:** Schwann cell
- **UBERON:** peripheral nerve
- **MAXO:** drug therapy; gene therapy; physical therapy; orthopedic surgery; assistive orthoses (supportive care not directly enumerated in the extracted sources but consistent with review framing)


References

1. (record2024wholegenomesequencing pages 1-2): Christopher J Record, Menelaos Pipis, Mariola Skorupinska, Julian Blake, Roy Poh, James M Polke, Kelly Eggleton, Tina Nanji, Stephan Zuchner, Andrea Cortese, Henry Houlden, Alexander M Rossor, Matilde Laura, and Mary M Reilly. Whole genome sequencing increases the diagnostic rate in charcot-marie-tooth disease. Brain, 147:3144-3156, Mar 2024. URL: https://doi.org/10.1093/brain/awae064, doi:10.1093/brain/awae064. This article has 49 citations and is from a highest quality peer-reviewed journal.

2. (okamoto2023thecurrentstate pages 1-2): Yuji Okamoto and Hiroshi Takashima. The current state of charcot–marie–tooth disease treatment. Genes, 14:1391, Jul 2023. URL: https://doi.org/10.3390/genes14071391, doi:10.3390/genes14071391. This article has 58 citations.

3. (mandarakas2024multicentervalidationof pages 1-2): Melissa R. Mandarakas, Katy J. Eichinger, Paula Bray, Kayla M.D. Cornett, Michael E. Shy, Mary M. Reilly, Gita M. Ramdharry, Steven S. Scherer, Davide Pareyson, Timothy Estilow, Marnee J. McKay, David N. Herrmann, and Joshua Burns. Multicenter validation of the charcot-marie-tooth functional outcome measure. Neurology, Feb 2024. URL: https://doi.org/10.1212/wnl.0000000000207963, doi:10.1212/wnl.0000000000207963. This article has 12 citations and is from a highest quality peer-reviewed journal.

4. (NCT04762758 chunk 1):  Phase III Trial Assessing the Efficacy and Safety of PXT3003 in CMT1A Patients. Pharnext S.C.A.. 2021. ClinicalTrials.gov Identifier: NCT04762758

5. (NCT06328712 chunk 1):  Evaluate the Safety and Efficacy of EN001 in Patients With Charcot-Marie-Tooth Disease Type 1A. ENCell. 2024. ClinicalTrials.gov Identifier: NCT06328712

6. (NCT02579759 chunk 1):  Phase III Trial Assessing the Efficacy and Safety of PXT3003 in CMT1A Patients (PLEO-CMT). Pharnext S.C.A.. 2015. ClinicalTrials.gov Identifier: NCT02579759

7. (NCT05361031 chunk 2):  The Safety and Tolerability of Engensis (VM202) in Patients With Charcot-Marie-Tooth Disease Subtype 1A (CMT1A). Helixmith Co., Ltd.. 2020. ClinicalTrials.gov Identifier: NCT05361031

8. (NCT03023540 chunk 2):  Assessing Long Term Safety and Tolerability of PXT3003 in Patients With Charcot-Marie-Tooth Disease Type 1A. Pharnext S.C.A.. 2017. ClinicalTrials.gov Identifier: NCT03023540

9. (ceylan2023highdiagnosticyield pages 1-2): Gülay Güleç Ceylan, Esra Habiloğlu, Büşranur Çavdarlı, Ebru Tuncez, Sule Bilen, Özlem Yayıcı Köken, and C. Nur Semerci Gündüz. High diagnostic yield with algorithmic molecular approach on hereditary neuropathies. Revista da Associação Médica Brasileira, 69:233-239, Feb 2023. URL: https://doi.org/10.1590/1806-9282.20220929, doi:10.1590/1806-9282.20220929. This article has 5 citations.

10. (mandarakas2024multicentervalidationof pages 5-6): Melissa R. Mandarakas, Katy J. Eichinger, Paula Bray, Kayla M.D. Cornett, Michael E. Shy, Mary M. Reilly, Gita M. Ramdharry, Steven S. Scherer, Davide Pareyson, Timothy Estilow, Marnee J. McKay, David N. Herrmann, and Joshua Burns. Multicenter validation of the charcot-marie-tooth functional outcome measure. Neurology, Feb 2024. URL: https://doi.org/10.1212/wnl.0000000000207963, doi:10.1212/wnl.0000000000207963. This article has 12 citations and is from a highest quality peer-reviewed journal.

11. (ceylan2023highdiagnosticyield pages 2-4): Gülay Güleç Ceylan, Esra Habiloğlu, Büşranur Çavdarlı, Ebru Tuncez, Sule Bilen, Özlem Yayıcı Köken, and C. Nur Semerci Gündüz. High diagnostic yield with algorithmic molecular approach on hereditary neuropathies. Revista da Associação Médica Brasileira, 69:233-239, Feb 2023. URL: https://doi.org/10.1590/1806-9282.20220929, doi:10.1590/1806-9282.20220929. This article has 5 citations.

12. (record2024wholegenomesequencing pages 2-3): Christopher J Record, Menelaos Pipis, Mariola Skorupinska, Julian Blake, Roy Poh, James M Polke, Kelly Eggleton, Tina Nanji, Stephan Zuchner, Andrea Cortese, Henry Houlden, Alexander M Rossor, Matilde Laura, and Mary M Reilly. Whole genome sequencing increases the diagnostic rate in charcot-marie-tooth disease. Brain, 147:3144-3156, Mar 2024. URL: https://doi.org/10.1093/brain/awae064, doi:10.1093/brain/awae064. This article has 49 citations and is from a highest quality peer-reviewed journal.

13. (okamoto2023thecurrentstate pages 16-17): Yuji Okamoto and Hiroshi Takashima. The current state of charcot–marie–tooth disease treatment. Genes, 14:1391, Jul 2023. URL: https://doi.org/10.3390/genes14071391, doi:10.3390/genes14071391. This article has 58 citations.

14. (mcculloch2024navigatingthelandscape pages 22-23): Mary Kate McCulloch, Fatemeh Mehryab, and Afrooz Rashnonejad. Navigating the landscape of cmt1b: understanding genetic pathways, disease models, and potential therapeutic approaches. International Journal of Molecular Sciences, 25:9227, Aug 2024. URL: https://doi.org/10.3390/ijms25179227, doi:10.3390/ijms25179227. This article has 9 citations.

15. (yalcouye2023geneticsofhearing pages 163-166): A Yalcouye. Genetics of hearing impairment and peripheral neuropathy in mali. Unknown journal, 2023.

16. (okamoto2023thecurrentstate pages 12-14): Yuji Okamoto and Hiroshi Takashima. The current state of charcot–marie–tooth disease treatment. Genes, 14:1391, Jul 2023. URL: https://doi.org/10.3390/genes14071391, doi:10.3390/genes14071391. This article has 58 citations.

17. (mandarakas2024multicentervalidationof pages 6-9): Melissa R. Mandarakas, Katy J. Eichinger, Paula Bray, Kayla M.D. Cornett, Michael E. Shy, Mary M. Reilly, Gita M. Ramdharry, Steven S. Scherer, Davide Pareyson, Timothy Estilow, Marnee J. McKay, David N. Herrmann, and Joshua Burns. Multicenter validation of the charcot-marie-tooth functional outcome measure. Neurology, Feb 2024. URL: https://doi.org/10.1212/wnl.0000000000207963, doi:10.1212/wnl.0000000000207963. This article has 12 citations and is from a highest quality peer-reviewed journal.

18. (dong2024currenttreatmentmethods pages 2-4): Hongxian Dong, Boquan Qin, Hui Zhang, Lei Lei, and Shizhou Wu. Current treatment methods for charcot–marie–tooth diseases. Biomolecules, 14:1138, Sep 2024. URL: https://doi.org/10.3390/biom14091138, doi:10.3390/biom14091138. This article has 10 citations.

19. (NCT03520751 chunk 2): Zarife Sahenk. Phase I/IIa Trial of scAAV1.tMCK.NTF3 for Treatment of CMT1A. Nationwide Children's Hospital. 2027. ClinicalTrials.gov Identifier: NCT03520751

20. (mandarakas2024multicentervalidationof pages 3-5): Melissa R. Mandarakas, Katy J. Eichinger, Paula Bray, Kayla M.D. Cornett, Michael E. Shy, Mary M. Reilly, Gita M. Ramdharry, Steven S. Scherer, Davide Pareyson, Timothy Estilow, Marnee J. McKay, David N. Herrmann, and Joshua Burns. Multicenter validation of the charcot-marie-tooth functional outcome measure. Neurology, Feb 2024. URL: https://doi.org/10.1212/wnl.0000000000207963, doi:10.1212/wnl.0000000000207963. This article has 12 citations and is from a highest quality peer-reviewed journal.

21. (mandarakas2024multicentervalidationof pages 2-3): Melissa R. Mandarakas, Katy J. Eichinger, Paula Bray, Kayla M.D. Cornett, Michael E. Shy, Mary M. Reilly, Gita M. Ramdharry, Steven S. Scherer, Davide Pareyson, Timothy Estilow, Marnee J. McKay, David N. Herrmann, and Joshua Burns. Multicenter validation of the charcot-marie-tooth functional outcome measure. Neurology, Feb 2024. URL: https://doi.org/10.1212/wnl.0000000000207963, doi:10.1212/wnl.0000000000207963. This article has 12 citations and is from a highest quality peer-reviewed journal.
