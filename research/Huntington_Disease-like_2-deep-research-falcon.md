---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T22:47:20.917774'
end_time: '2026-05-09T23:01:27.119438'
duration_seconds: 846.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Huntington disease-like 2
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Huntington disease-like 2
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Huntington disease-like 2** covering all of the
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
- **Disease Name:** Huntington disease-like 2
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Huntington disease-like 2** covering all of the
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


# Huntington disease-like 2 (HDL2): Disease characteristics research report

## 1. Disease information

### Overview
Huntington disease-like 2 (HDL2) is a rare, adult-onset, progressive neurodegenerative disorder that clinically and pathologically closely resembles Huntington disease (HD) (i.e., an “HD phenocopy/genocopy”). It is caused by a pathogenic trinucleotide repeat expansion at the junctophilin-3 locus (JPH3) and is enriched in individuals with African ancestry. (anderson2025huntingtondiseaselike2 pages 1-3, margolis2003huntingtonsdiseaselike2 pages 1-2, margolis2016pathogenicinsightsfrom pages 1-2)

### Key identifiers (available from retrieved sources)
- **OMIM (disease):** 606438 (HDL2) (anderson2025huntingtondiseaselike2 pages 14-16)
- **OMIM (gene):** 605268 (**JPH3**) (anderson2025huntingtondiseaselike2 pages 14-16)
- **Cytogenetic locus:** 16q24.2 (reported in GeneReviews-style summary) (anderson2025huntingtondiseaselike2 pages 14-16)

**Not available from retrieved full text:** MONDO, Orphanet (ORPHA), MeSH, ICD-10/ICD-11 codes.

### Synonyms / alternative names
- Huntington disease-like 2
- Huntington’s disease–like 2
- HDL2
- HD phenocopy/genocopy due to **JPH3** repeat expansion (anderson2025huntingtondiseaselike2 pages 1-3, margolis2016pathogenicinsightsfrom pages 1-2)

### Evidence provenance
Most information used here is aggregated from gene- and disease-level resources (GeneReviews-style) and peer-reviewed primary literature (human postmortem, cell models, and mouse models), plus large diagnostic/referral cohorts for epidemiology. (anderson2025huntingtondiseaselike2 pages 1-3, krause2015junctophilin3(jph3) pages 4-6, rudnicki2007huntingtonsdisease–like2 pages 6-8, wilburn2011anantisensecag pages 1-2)

## 2. Etiology

### Disease causal factors
**Primary cause (genetic):** a germline heterozygous **CTG/CAG trinucleotide repeat expansion** at the **JPH3** locus. (anderson2025huntingtondiseaselike2 pages 1-3, margolis2016pathogenicinsightsfrom pages 1-2)

**Repeat characteristics / definitions (current working thresholds):**
- Normal: typically **6–28** repeats (anderson2025huntingtondiseaselike2 pages 1-3, margolis2016pathogenicinsightsfrom pages 1-2)
- Intermediate/uncertain: **29–39** repeats (uncertain clinical significance) (anderson2025huntingtondiseaselike2 pages 1-3, anderson2025huntingtondiseaselike2 pages 14-16)
- Pathogenic: generally **≥40 CTG** repeats (“full-penetrance” in GeneReviews-style resource; some ambiguity near the boundary) (anderson2025huntingtondiseaselike2 pages 1-3, anderson2025huntingtondiseaselike2 pages 14-16)
- Reported affected range: commonly ~**40–59** triplets (margolis2016pathogenicinsightsfrom pages 1-2, seixas2012lossofjunctophilin‐3 pages 1-2)
- Largest reported expansion in humans: **63 CTG** repeats (anderson2025huntingtondiseaselike2 pages 3-5)

**Genotype–phenotype:** increasing repeat size correlates with earlier onset, estimated ~**1.2–2.9 years earlier per triplet** (reported in GeneReviews-style summary). (anderson2025huntingtondiseaselike2 pages 3-5)

### Risk factors
- **Ancestry/population risk:** HDL2 is strongly enriched in people with **African ancestry**; referral cohorts in South Africa show high diagnostic yield of JPH3 expansions among patients with an HD phenotype and African ancestry. (krause2015junctophilin3(jph3) pages 4-6, krause2015junctophilin3(jph3) pages 3-4)

### Protective factors
No genetic or environmental protective factors specific to HDL2 were identified in the retrieved sources.

### Gene–environment interactions
No HDL2-specific gene–environment interaction evidence was identified in the retrieved sources.

## 3. Phenotypes

### Core clinical phenotype (symptoms/signs)
HDL2 is typically described as a progressive triad of:
- **Movement disorder:** chorea and/or other hyperkinetic features; parkinsonism can also occur (anderson2025huntingtondiseaselike2 pages 1-3, krause2015junctophilin3(jph3) pages 6-8)
- **Psychiatric/behavioral features:** e.g., irritability, apathy, depression (reported in review) (margolis2016pathogenicinsightsfrom pages 1-2)
- **Cognitive decline progressing to dementia** (anderson2025huntingtondiseaselike2 pages 3-5, anderson2025huntingtondiseaselike2 pages 1-3)

**Age of onset and progression:** mean age at onset reported as **41 years** (SD 11.1; range **12–66**), with progressive course and death typically **10–20 years** after onset. (anderson2025huntingtondiseaselike2 pages 3-5, anderson2025huntingtondiseaselike2 pages 1-3)

**Frequency notes:** In a South African clinical-file subset, parkinsonian features were reported in **5/22 (23%)** HDL2 vs **1/39 (3%)** HD (χ2=6.45, p=0.011), suggesting possible relative enrichment (limited sample size). (krause2015junctophilin3(jph3) pages 6-8)

### Suggested HPO terms (examples)
- Chorea: **HP:0002072**
- Parkinsonism: **HP:0001300**
- Dystonia: **HP:0001332** (as differential motor manifestation)
- Dementia: **HP:0000726**
- Cognitive impairment: **HP:0100543**
- Depression: **HP:0000716**
- Irritability: **HP:0000737**
- Apathy: **HP:0000741**
- Dysarthria: **HP:0001260** (common in HD-like neurodegeneration and addressed in management) (anderson2025huntingtondiseaselike2 pages 10-11)
- Dysphagia: **HP:0002015** (addressed in management/aspiration precautions) (anderson2025huntingtondiseaselike2 pages 10-11)

### Quality-of-life impact
Direct HDL2-specific quality-of-life instrument results were not identified in the retrieved sources. Functional impairment is inferred from progressive motor disability, cognitive decline/dementia, and need for multidisciplinary supportive care (e.g., PT, speech therapy, nutrition, home safety modifications). (anderson2025huntingtondiseaselike2 pages 10-11, anderson2025huntingtondiseaselike2 pages 1-3)

## 4. Genetic / molecular information

### Causal gene
- **Gene:** **JPH3** (junctophilin-3) (OMIM 605268) (anderson2025huntingtondiseaselike2 pages 14-16)

### Pathogenic variant type
- **Variant class:** repeat expansion (trinucleotide CTG/CAG) (anderson2025huntingtondiseaselike2 pages 1-3)
- **Molecular context:** the repeat lies in alternatively spliced exon **2A** on the sense strand (CTG orientation) and is in **CAG** orientation on the antisense strand (JPH3-AS), enabling bidirectional transcription models. (anderson2025huntingtondiseaselike2 pages 14-16, anderson2025huntingtondiseaselike2 pages 16-19)

### Variant classification (ACMG/AMP context)
The retrieved sources treat **≥40 CTG repeats** as pathogenic/diagnostic in a clinically compatible case. (anderson2025huntingtondiseaselike2 pages 1-3, anderson2025huntingtondiseaselike2 pages 14-16)

### Allele frequency
Population allele frequency in gnomAD/1000 Genomes was not available in the retrieved sources.

### Somatic vs germline
HDL2 is described as a germline, inherited autosomal dominant disorder (no somatic-only HDL2 cases in retrieved sources). (anderson2025huntingtondiseaselike2 pages 1-3)

### Functional consequences (mechanism-level, summarized)
Evidence supports a **multimodal** model combining:
1) **RNA gain-of-function** from expanded CUG repeat RNA and RNA-binding protein sequestration;
2) possible **antisense/polyQ-mediated toxicity** (strong in BAC-HDL2 mouse; unproven/undetectable or low in human brain);
3) **loss of JPH3 function** (reduced transcript/protein in patient brain; motor deficits in Jph3 mutant mice). (rudnicki2007huntingtonsdisease–like2 pages 6-8, seixas2012lossofjunctophilin‐3 pages 1-2, margolis2016pathogenicinsightsfrom pages 2-4, wilburn2011anantisensecag pages 1-2)

### Modifier genes
No HDL2-specific modifier genes were identified in the retrieved sources.

### Epigenetic information
No HDL2-specific epigenetic findings were identified in the retrieved sources.

### Chromosomal abnormalities
Not applicable based on retrieved sources (repeat expansion at JPH3 locus rather than large structural variant). (anderson2025huntingtondiseaselike2 pages 1-3)

## 5. Environmental information
No specific environmental, lifestyle, toxin, or infectious triggers for HDL2 were identified in the retrieved sources.

## 6. Mechanism / pathophysiology

### Mechanistic causal chain (integrated)
**Trigger:** inherited JPH3 CTG repeat expansion (≥40) (anderson2025huntingtondiseaselike2 pages 1-3)

**Upstream molecular events (RNA-focused):** expanded **CUG** repeat RNA from JPH3 forms nuclear RNA foci in HDL2 frontal cortex and in cell models. In one study, RNA foci colocalized with **MBNL1**, were RNase-sensitive, and were associated with reduced nuclear MBNL1 and splicing abnormalities. (rudnicki2007huntingtonsdisease–like2 pages 6-8)

**Downstream cellular effects:** in neuronal-like cell models, a nontranslatable expanded CUG construct increased apoptosis/toxicity (e.g., caspase activation and TUNEL signal). (rudnicki2007huntingtonsdisease–like2 pages 6-8)

**RNA processing dysfunction (splicing):** the same study reported MBNL1 depletion (t=8.57, p=0.001) and splicing changes including increased fetal **MAPT** isoforms lacking exon 2 (t=5.71, p=0.0012) and altered **APP** exon 7 utilization (t=5.43, p=0.0016). (rudnicki2007huntingtonsdisease–like2 pages 6-8)

**Loss-of-function component:** JPH3 transcript and full-length protein are decreased in HDL2 frontal cortex, and **Jph3** mutant mice show progressive motor phenotypes and impaired motor learning, supporting that reduced JPH3 contributes to disease. (seixas2012lossofjunctophilin‐3 pages 1-2, seixas2012lossofjunctophilin‐3 pages 9-11)

**Antisense / polyQ component (model vs human):** BAC-HDL2 mice provide evidence for bidirectional transcription and an antisense **HDL2-CAG** transcript encoding expanded polyglutamine with polyQ-positive nuclear inclusions; however, postmortem human data have been inconsistent in detecting expanded antisense transcripts or expanded polyQ proteins, leaving the extent of this mechanism in human HDL2 unresolved. (margolis2016pathogenicinsightsfrom pages 2-4, wilburn2011anantisensecag pages 1-2)

### Key concepts and definitions (repeat expansion pathomechanisms)
HDL2 is often discussed within repeat expansion disorder frameworks that can involve **RNA gain-of-function**, **protein gain-of-function**, and/or **loss of function**. The evidence base for HDL2 supports more than one of these. (seixas2012lossofjunctophilin‐3 pages 1-2, margolis2016pathogenicinsightsfrom pages 2-4)

### Tissue and cell-type involvement
**Primary affected system:** central nervous system, particularly **striatum** and **cerebral cortex** with prominent neuronal loss (anderson2025huntingtondiseaselike2 pages 3-5)

**Cell-type emphasis:** medium spiny neurons (striatal projection neurons) are highlighted by loss patterns (“loss of medium spiny neurons in a dorsal-to-ventral gradient”). (anderson2025huntingtondiseaselike2 pages 3-5)

### Suggested ontology mappings
- **GO biological process (examples):**
  - RNA splicing: **GO:0008380** (supported by MBNL1-associated splicing abnormalities) (rudnicki2007huntingtonsdisease–like2 pages 6-8)
  - Regulation of apoptotic process: **GO:0042981** (expanded RNA induced caspase/TUNEL toxicity in vitro) (rudnicki2007huntingtonsdisease–like2 pages 6-8)
  - Protein ubiquitination / inclusion formation: **GO:0016567** / aggregation-related terms (inclusion pathology described) (anderson2025huntingtondiseaselike2 pages 3-5)
- **CL (Cell Ontology, examples):**
  - Medium spiny neuron: **CL:0002618** (mentioned as major affected striatal neuron type) (anderson2025huntingtondiseaselike2 pages 3-5)
- **UBERON (examples):**
  - Striatum: **UBERON:0002435**
  - Caudate nucleus: **UBERON:0001875** (MRI emphasizes caudate atrophy) (anderson2025huntingtondiseaselike2 pages 1-3)
  - Cerebral cortex: **UBERON:0000956** (anderson2025huntingtondiseaselike2 pages 1-3)

### Visual evidence (bidirectional transcription model)
A schematic of the BAC-HDL2 construct and bidirectional transcription at the JPH3 locus (including the antisense HDL2-CAG transcript model) is shown in Wilburn et al. (Neuron 2011). (wilburn2011anantisensecag media fdbbbc4c, wilburn2011anantisensecag media aa402816)

## 7. Anatomical structures affected

### Organ/body system level
- Central nervous system (movement, psychiatric, cognitive domains) (anderson2025huntingtondiseaselike2 pages 1-3)

### Tissue/anatomical regions
- **Striatum** (including caudate), **cerebral cortex** (anderson2025huntingtondiseaselike2 pages 1-3, anderson2025huntingtondiseaselike2 pages 3-5)
- Thalamus may be relatively more affected vs HD on volumetric MRI comparisons (anderson2025huntingtondiseaselike2 pages 1-3)

### Subcellular localization
- Nuclear RNA foci and nuclear inclusions (RNA foci and polyQ/ubiquitin-positive inclusions described) (rudnicki2007huntingtonsdisease–like2 pages 6-8, anderson2025huntingtondiseaselike2 pages 3-5)

## 8. Temporal development

### Onset
- Typically adult-onset, mean ~**41 years**, range **12–66** (anderson2025huntingtondiseaselike2 pages 3-5)

### Progression
- Progressive neurodegeneration with death typically **10–20 years** after onset (anderson2025huntingtondiseaselike2 pages 1-3)

### Staging
No HDL2-specific validated staging system was identified in retrieved sources; clinical monitoring is modeled on HD scales (e.g., UHDRS). (anderson2025huntingtondiseaselike2 pages 10-11, anderson2025huntingtondiseaselike2 pages 11-14)

## 9. Inheritance and population

### Inheritance
- **Autosomal dominant**; 50% transmission risk to offspring of an affected individual (anderson2025huntingtondiseaselike2 pages 1-3, anderson2025huntingtondiseaselike2 pages 14-16)

### Epidemiology and distribution (statistics)
**Referral/diagnostic cohorts (South Africa):**
- Among black patients referred for an HD phenotype, **20/130 (15%)** had JPH3 expansions; among mixed ancestry **3/14 (21%)**; among white **0/171**. (krause2015junctophilin3(jph3) pages 4-6)
- In the same dataset, among genetically diagnosed black/mixed-ancestry cases, HDL2 accounted for about **23/76 (~30%)** of diagnoses. (krause2015junctophilin3(jph3) pages 4-6)
- As of Dec 2013, one service ascertained **41 individuals** with JPH3 expansions from **34 families** (expansion sizes 40–58). (krause2015junctophilin3(jph3) pages 6-8)

**Genetic-ascertainment frequency estimates (South Africa):**
- A 20-year retrospective review of molecular diagnoses reported combined minimum frequency estimates for **HD+HDL2** of **0.25 (black), 2.10 (mixed ancestry), 5.10 (white) per 100,000**; these were not HDL2-specific prevalence rates and were noted as minimum estimates with substantial under-ascertainment likely. (baine2016thefrequencyof pages 1-2, baine2016thefrequencyof pages 2-3)

**Founder effect / ancestry:** haplotype analyses in multiple families are consistent with a founder mutation with African origin, and the literature emphasizes that HDL2 has been described “exclusively” in individuals with confirmed/likely African ancestry in GeneReviews-style summaries. (krause2015junctophilin3(jph3) pages 1-3, anderson2025huntingtondiseaselike2 pages 3-5)

## 10. Diagnostics

### Clinical recognition
Because HDL2 is clinically indistinguishable from HD, suspicion is highest in individuals with an HD phenotype and African ancestry (or family history consistent with autosomal dominant inheritance) and negative HTT testing. (anderson2025huntingtondiseaselike2 pages 1-3, krause2015junctophilin3(jph3) pages 4-6)

### Genetic testing (recommended approach)
- **Targeted JPH3 CTG repeat analysis** is diagnostic: a heterozygous allele **≥40 CTG repeats** establishes the molecular diagnosis in a compatible phenotype. (anderson2025huntingtondiseaselike2 pages 1-3)
- **Assay notes:** PCR-based repeat sizing is standard and usually detects expanded alleles; however, repeat-expansion testing can yield misleading “single allele” results (e.g., apparent homozygosity) and may require repeat testing with alternative primers and/or additional methods when suspicion remains high. (anderson2025huntingtondiseaselike2 pages 3-5, anderson2025huntingtondiseaselike2 pages 16-19)
- **Predictive and reproductive testing:** predictive testing for at-risk adults, prenatal testing, and preimplantation genetic testing are possible once a family expansion is known. (anderson2025huntingtondiseaselike2 pages 14-16)

### Imaging
MRI findings include **prominent caudate and cortical atrophy** with relative sparing of brainstem and cerebellum; semiautomated volumetry suggested **greater thalamic atrophy** in HDL2 compared with HD despite similar cortical/striatal loss. (anderson2025huntingtondiseaselike2 pages 1-3)

### Biomarkers (research / translational)
Plasma **neurofilament light chain (NfL)** is elevated in manifest HDL2 and discriminated HDL2 from controls with AUC **0.926 (95% CI 0.812–1.000)** in a small cross-sectional study (HDL2 n=12; controls n=9). (anderson2025comparativeanalysisof pages 9-13)

### Differential diagnosis
In the context of “non-HD chorea/HD phenocopies,” HDL2/JPH3 is among the most frequent genetic causes cited in a 2024 practical diagnostic approach preprint, alongside several spinocerebellar ataxia genes and frontotemporal dementia genes. (bates2015huntingtondisease pages 16-19)

## 11. Outcome / prognosis

### Survival and mortality
Typical survival is described as approximately **10–20 years after onset** (and some reviews cite ~15–20 years). (anderson2025huntingtondiseaselike2 pages 1-3, margolis2016pathogenicinsightsfrom pages 1-2)

### Morbidity and functional impact
Progressive motor disability, psychiatric morbidity, and dementia drive increasing care needs; management emphasizes multidisciplinary support, safety evaluation, nutritional support, and psychiatric care. (anderson2025huntingtondiseaselike2 pages 10-11, anderson2025huntingtondiseaselike2 pages 11-14)

### Prognostic factors
Repeat length correlates with age at onset; stronger HDL2-specific prognostic biomarkers beyond repeat size and clinical measures were not identified in the retrieved sources. (anderson2025huntingtondiseaselike2 pages 3-5)

## 12. Treatment

### Current standard of care (real-world implementation)
No disease-modifying therapy for HDL2 was identified in retrieved sources; management is symptomatic and largely extrapolated from HD care.

**Symptomatic pharmacotherapy examples (from GeneReviews-style guidance):**
- Chorea/movement suppression: **tetrabenazine** (and derivatives) and/or low-dose neuroleptics such as **fluphenazine** or **haloperidol** (anderson2025huntingtondiseaselike2 pages 10-11, anderson2025huntingtondiseaselike2 pages 1-3)
- Psychiatric symptoms: antidepressants (e.g., sertraline, nortriptyline), antipsychotics, mood stabilizers (e.g., lithium, valproate, carbamazepine, lamotrigine), and occasionally **ECT** (anderson2025huntingtondiseaselike2 pages 10-11, anderson2025huntingtondiseaselike2 pages 1-3)

**Supportive/rehabilitative care:**
- Physical therapy for mobility and fall prevention; home safety modifications (anderson2025huntingtondiseaselike2 pages 10-11, anderson2025huntingtondiseaselike2 pages 11-14)
- Speech-language pathology for dysarthria/dysphagia; nutrition/feeding modifications to reduce aspiration risk; communication devices (anderson2025huntingtondiseaselike2 pages 10-11)
- Care coordination/social work, legal/financial planning, and palliative care considerations (anderson2025huntingtondiseaselike2 pages 10-11, anderson2025huntingtondiseaselike2 pages 11-14)

### MAXO term suggestions (examples)
- Symptomatic pharmacotherapy: **MAXO:0000058** (drug therapy)
- Physical therapy: **MAXO:0000012**
- Speech therapy: **MAXO:0000129**
- Genetic counseling: **MAXO:0000079**
- Palliative care: **MAXO:0000527**

### Experimental / trials
No HDL2-specific interventional clinical trials were identified in the retrieved sources or in the clinical trial tool state during this run.

## 13. Prevention
No primary prevention is available for an autosomal dominant repeat expansion disorder, but **secondary prevention** in the form of genetic counseling and predictive testing for at-risk adults is feasible when a family expansion is known. (anderson2025huntingtondiseaselike2 pages 14-16)

**Genetic counseling:** recommended to support informed reproductive decision-making (including prenatal and preimplantation genetic testing options) and psychosocial planning. (anderson2025huntingtondiseaselike2 pages 14-16, anderson2025huntingtondiseaselike2 pages 10-11)

## 14. Other species / natural disease
No naturally occurring non-human HDL2 analogs were identified in the retrieved sources.

## 15. Model organisms

### Mouse models
- **BAC-HDL2 model (repeat 120):** supports bidirectional transcription and antisense HDL2-CAG transcript models with polyQ-positive nuclear inclusions and transcriptional dysregulation (CBP involvement). (wilburn2011anantisensecag pages 1-2)
- **Jph3 loss-of-function mice:** exhibit motor dysfunction and impaired motor learning, supporting contribution of JPH3 loss but suggesting loss-of-function alone is insufficient to recapitulate the full inclusion pathology. (seixas2012lossofjunctophilin‐3 pages 9-11, wilburn2011anantisensecag pages 1-2)

### Cell-based models
Expanded CUG-repeat transcripts form nuclear foci and cause toxicity (caspase activation/TUNEL) in neuronal-like cells, supporting RNA gain-of-function. (rudnicki2007huntingtonsdisease–like2 pages 6-8)

## Key knowledge-base summary table

| Topic | Key facts | Citations |
|---|---|---|
| Identifiers | Disease: Huntington disease-like 2 (HDL2); OMIM disease **606438**. Causal gene: **JPH3** (junctophilin-3); OMIM gene **605268**; locus **16q24.2**. HDL2 is an HD phenocopy recognized in aggregated disease-level resources/reviews and molecularly confirmed by repeat testing. | (anderson2025huntingtondiseaselike2 pages 14-16, anderson2025huntingtondiseaselike2 pages 3-5) |
| Gene / variant / threshold | Cause is a **germline heterozygous CTG/CAG trinucleotide repeat expansion** at the **JPH3** locus. Normal alleles are typically **6-28 repeats**; **29-39 repeats** are of uncertain significance; **>=40 CTG repeats** is generally considered pathogenic/full-penetrance, with reported affected alleles usually **40-59** and up to **63** repeats reported. Repeat length inversely correlates with age at onset. | (anderson2025huntingtondiseaselike2 pages 1-3, anderson2025huntingtondiseaselike2 pages 3-5, margolis2016pathogenicinsightsfrom pages 1-2) |
| Inheritance | **Autosomal dominant**; most affected individuals have an affected parent; each child of an affected individual has a **50%** risk of inheriting the expansion. Anticipation is discussed for repeat-length disorders, but penetrance near the lower boundary remains incompletely defined. | (anderson2025huntingtondiseaselike2 pages 1-3, anderson2025huntingtondiseaselike2 pages 14-16, anderson2025huntingtondiseaselike2 pages 3-5) |
| Populations / epidemiology | HDL2 is reported almost exclusively in people with **African ancestry**. In a South African referral cohort, **20/130 black patients (15%)** and **3/14 mixed-ancestry patients (21%)** with an HD phenotype had **JPH3** expansions, versus **0/171 white** patients; among genetically diagnosed black/mixed-ancestry patients, HDL2 accounted for about **23/76 (~30%)**. A nationwide South African molecular-ascertainment study found **52 HDL2** and **384 HD** diagnoses among **436** genetically confirmed HD/HDL2 cases; combined minimum HD/HDL2 frequencies were **0.25, 2.10, and 5.10 per 100,000** in black, mixed-ancestry, and white groups, respectively (not HDL2-specific prevalence). | (krause2015junctophilin3(jph3) pages 4-6, krause2015junctophilin3(jph3) pages 8-10, baine2016thefrequencyof pages 3-4, baine2016thefrequencyof pages 1-2, baine2016thefrequencyof pages 2-3) |
| Core phenotype / onset / prognosis | Progressive triad of **movement, psychiatric/emotional, and cognitive** impairment, often clinically indistinguishable from Huntington disease. Mean age at onset about **41 years** (SD 11.1; range **12-66**). Dementia is described as progressive/universal in advanced disease. Death typically occurs **10-20 years** after onset; some reviews cite **15-20 years** of progression. Parkinsonian features may be relatively enriched in HDL2 (**5/22, 23%**) versus matched HD (**1/39, 3%**) in one South African series. | (anderson2025huntingtondiseaselike2 pages 3-5, anderson2025huntingtondiseaselike2 pages 1-3, margolis2016pathogenicinsightsfrom pages 1-2, krause2015junctophilin3(jph3) pages 6-8) |
| Mechanisms | Evidence supports **multimodal pathogenesis**: (1) **sense-strand expanded CUG RNA** forms **nuclear RNA foci** in HDL2 cortex and cell models; foci colocalize with **MBNL1**, with nuclear MBNL1 depletion and splicing changes including **MAPT exon 2** and **APP exon 7** abnormalities; nontranslatable expanded RNA increases **caspase-3/7** activity and **TUNEL** positivity. (2) **Antisense CAG/polyQ toxicity** is strongly supported in **BAC-HDL2 mice**, where an antisense transcript produces polyQ-positive nuclear inclusions and CBP-related transcriptional dysfunction, but equivalent expanded antisense/polyQ species are not convincingly detected in human HDL2 brain. (3) **JPH3 loss-of-function** also contributes: full-length JPH3 transcript/protein is reduced in HDL2 brain, and **Jph3** mutant mice show motor impairment, but knockout alone does not recapitulate full human inclusion pathology. | (rudnicki2007huntingtonsdisease–like2 pages 6-8, seixas2012lossofjunctophilin‐3 pages 1-2, margolis2016pathogenicinsightsfrom pages 2-4, seixas2012lossofjunctophilin‐3 pages 9-11, wilburn2011anantisensecag pages 1-2) |
| Neuropathology / imaging | Pathology resembles HD, with prominent **striatal and cortical neuronal loss**, loss of **medium spiny neurons** in a dorsal-to-ventral striatal gradient, and cortical intranuclear inclusions staining for **polyglutamine, ubiquitin, torsinA, and TBP**. MRI shows **caudate and cortical atrophy** with relative sparing of brainstem/cerebellum; semiautomated volumetry reported **greater thalamic atrophy** in HDL2 than HD despite similar cortical/striatal volume loss. | (anderson2025huntingtondiseaselike2 pages 3-5, anderson2025huntingtondiseaselike2 pages 1-3, margolis2016pathogenicinsightsfrom pages 1-2) |
| Diagnostics | Diagnosis is established by **targeted molecular testing of the JPH3 CTG repeat**, typically **PCR-based repeat-expansion testing**. Assays detect nearly all expanded alleles but can yield false-negative or misleading single-allele results with very long repeats; if suspicion remains high or apparent homozygosity is seen, **repeat testing with alternate primers / additional methods** and family testing are recommended. Predictive, prenatal, and preimplantation testing are possible once a familial expansion is known. | (anderson2025huntingtondiseaselike2 pages 3-5, anderson2025huntingtondiseaselike2 pages 16-19, anderson2025huntingtondiseaselike2 pages 14-16) |
| Biomarkers | **Plasma neurofilament light chain (NfL)** is elevated in manifest HDL2. In a cross-sectional study (**HDL2 n=12; HD n=9; controls n=9**), mean log NfL was **3.1** in HDL2 vs **2.1** in controls and **3.9** in HD; overall group difference **p=0.0006**. HDL2 vs control ROC AUC was **0.926 (95% CI 0.812-1.000)**, supporting NfL as a promising research biomarker, though correlations with motor/functional scores were weak. | (anderson2025comparativeanalysisof pages 9-13, anderson2025comparativeanalysisof pages 6-9, anderson2025comparativeanalysisof pages 1-6) |
| Current management | No HDL2-specific disease-modifying therapy or formal HDL2 guideline is available; care is extrapolated from **Huntington disease** and is **symptomatic, multidisciplinary, and real-world supportive**. Common measures include **tetrabenazine** (and derivatives) or **low-dose neuroleptics** for chorea/movement symptoms; **physical therapy**, **speech-language therapy**, nutrition/feeding modifications, aspiration precautions, communication devices, home safety and driving assessment; psychiatric treatment with **antidepressants, antipsychotics, mood stabilizers**, and occasionally **ECT**; annual surveillance of motor, cognitive, nutritional, and psychiatric status; social work, palliative care, and genetic counseling. | (anderson2025huntingtondiseaselike2 pages 10-11, anderson2025huntingtondiseaselike2 pages 1-3, anderson2025huntingtondiseaselike2 pages 11-14, anderson2025huntingtondiseaselike2 pages 8-10) |


*Table: This table summarizes the highest-yield knowledge-base facts for Huntington disease-like 2, including identifiers, genetics, epidemiology, clinical course, mechanisms, diagnostics, biomarkers, and management. It is designed for rapid curation and includes citation IDs in every row for traceability.*

## Source list (URLs and publication dates as available from retrieved full text)
- Rudnicki DD, Margolis RL. *Huntington disease-like 2.* (GeneReviews-style “Definitions”). **Feb 2020**. https://doi.org/10.32388/lkfkvq (anderson2025huntingtondiseaselike2 pages 1-3)
- Krause A, et al. *JPH3 expansion mutations causing HDL2 are common in South African patients with African ancestry and an HD phenotype.* **Oct 2015**. https://doi.org/10.1002/ajmg.b.32332 (krause2015junctophilin3(jph3) pages 4-6)
- Baine FK, et al. *The frequency of Huntington disease and Huntington disease-like 2 in the South African population.* **Feb 2016**. https://doi.org/10.1159/000444020 (baine2016thefrequencyof pages 1-2)
- Rudnicki DD, et al. *HDL2 is associated with CUG repeat-containing RNA foci.* **Mar 2007**. https://doi.org/10.1002/ana.21081 (rudnicki2007huntingtonsdisease–like2 pages 6-8)
- Seixas AI, et al. *Loss of junctophilin-3 contributes to HDL2 pathogenesis.* **Feb 2012**. https://doi.org/10.1002/ana.22598 (seixas2012lossofjunctophilin‐3 pages 1-2)
- Wilburn B, et al. *An antisense CAG repeat transcript at JPH3 locus mediates expanded polyglutamine protein toxicity in HDL2 mice.* **May 2011**. https://doi.org/10.1016/j.neuron.2011.03.021 (wilburn2011anantisensecag pages 1-2)
- Margolis RL, Rudnicki DD. *Pathogenic insights from HDL2 and other HD genocopies.* **Dec 2016**. https://doi.org/10.1097/WCO.0000000000000386 (margolis2016pathogenicinsightsfrom pages 1-2)
- Anderson DG, et al. *Plasma neurofilament light chain in HDL2 and HD.* **Nov 2025**. https://doi.org/10.1177/18796397241300141 (anderson2025comparativeanalysisof pages 9-13)

## Limitations of this report
- **Identifiers/codes:** MONDO/Orphanet/MeSH/ICD codes were not retrievable from the available full-text corpus in this run.
- **2023–2024 HDL2-specific reviews:** a major HDL2-focused Nature Reviews Neurology piece (2024) appeared in search results but was unobtainable in this run; consequently, “latest research” synthesis is anchored in primary studies and accessible contextual reviews/preprints.
- **Therapeutics:** HDL2-specific interventional trial evidence was not identified in the retrieved sources.


References

1. (anderson2025huntingtondiseaselike2 pages 1-3): DD Rudnicki and RL Margolis. Huntington disease-like 2. Definitions, Feb 2020. URL: https://doi.org/10.32388/lkfkvq, doi:10.32388/lkfkvq. This article has 11 citations.

2. (margolis2003huntingtonsdiseaselike2 pages 1-2): Russell L Margolis and Susan E Holmes. Huntington's disease-like 2: a clinical, pathological, and molecular comparison to huntington's disease. Clinical Neuroscience Research, 3:187-196, Sep 2003. URL: https://doi.org/10.1016/s1566-2772(03)00061-6, doi:10.1016/s1566-2772(03)00061-6. This article has 14 citations and is from a peer-reviewed journal.

3. (margolis2016pathogenicinsightsfrom pages 1-2): Russell L. Margolis and Dobrila D. Rudnicki. Pathogenic insights from huntington's disease-like 2 and other huntington's disease genocopies. Current Opinion in Neurology, 29:743-748, Dec 2016. URL: https://doi.org/10.1097/wco.0000000000000386, doi:10.1097/wco.0000000000000386. This article has 13 citations and is from a peer-reviewed journal.

4. (anderson2025huntingtondiseaselike2 pages 14-16): DD Rudnicki and RL Margolis. Huntington disease-like 2. Definitions, Feb 2020. URL: https://doi.org/10.32388/lkfkvq, doi:10.32388/lkfkvq. This article has 11 citations.

5. (krause2015junctophilin3(jph3) pages 4-6): Amanda Krause, Claire Mitchell, Fahmida Essop, Susan Tager, James Temlett, Giovanni Stevanin, Christopher Ross, Dobrila Rudnicki, and Russell Margolis. Junctophilin 3 (jph3) expansion mutations causing huntington disease like 2 (hdl2) are common in south african patients with african ancestry and a huntington disease phenotype. American Journal of Medical Genetics Part B: Neuropsychiatric Genetics, 168:573-585, Oct 2015. URL: https://doi.org/10.1002/ajmg.b.32332, doi:10.1002/ajmg.b.32332. This article has 73 citations.

6. (rudnicki2007huntingtonsdisease–like2 pages 6-8): Dobrila D. Rudnicki, Susan E. Holmes, Mark W. Lin, Charles A. Thornton, Christopher A. Ross, and Russell L. Margolis. Huntington's disease–like 2 is associated with cug repeat‐containing rna foci. Annals of Neurology, 61:272-282, Mar 2007. URL: https://doi.org/10.1002/ana.21081, doi:10.1002/ana.21081. This article has 182 citations and is from a highest quality peer-reviewed journal.

7. (wilburn2011anantisensecag pages 1-2): Brian Wilburn, Dobrila D. Rudnicki, Jing Zhao, Tara Murphy Weitz, Yin Cheng, Xiaofeng Gu, Erin Greiner, Chang Sin Park, Nan Wang, Bryce L. Sopher, Albert R. La Spada, Alex Osmand, Russell L. Margolis, Yi E. Sun, and X. William Yang. An antisense cag repeat transcript at jph3 locus mediates expanded polyglutamine protein toxicity in huntington's disease-like 2 mice. Neuron, 70:427-440, May 2011. URL: https://doi.org/10.1016/j.neuron.2011.03.021, doi:10.1016/j.neuron.2011.03.021. This article has 168 citations and is from a highest quality peer-reviewed journal.

8. (seixas2012lossofjunctophilin‐3 pages 1-2): Ana I. Seixas, Susan E. Holmes, Hiroshi Takeshima, Amira Pavlovich, Nancy Sachs, Jennifer L. Pruitt, Isabel Silveira, Christopher A. Ross, Russell L. Margolis, and Dobrila D. Rudnicki. Loss of junctophilin‐3 contributes to huntington disease‐like 2 pathogenesis. Annals of Neurology, 71:245-257, Feb 2012. URL: https://doi.org/10.1002/ana.22598, doi:10.1002/ana.22598. This article has 88 citations and is from a highest quality peer-reviewed journal.

9. (anderson2025huntingtondiseaselike2 pages 3-5): DD Rudnicki and RL Margolis. Huntington disease-like 2. Definitions, Feb 2020. URL: https://doi.org/10.32388/lkfkvq, doi:10.32388/lkfkvq. This article has 11 citations.

10. (krause2015junctophilin3(jph3) pages 3-4): Amanda Krause, Claire Mitchell, Fahmida Essop, Susan Tager, James Temlett, Giovanni Stevanin, Christopher Ross, Dobrila Rudnicki, and Russell Margolis. Junctophilin 3 (jph3) expansion mutations causing huntington disease like 2 (hdl2) are common in south african patients with african ancestry and a huntington disease phenotype. American Journal of Medical Genetics Part B: Neuropsychiatric Genetics, 168:573-585, Oct 2015. URL: https://doi.org/10.1002/ajmg.b.32332, doi:10.1002/ajmg.b.32332. This article has 73 citations.

11. (krause2015junctophilin3(jph3) pages 6-8): Amanda Krause, Claire Mitchell, Fahmida Essop, Susan Tager, James Temlett, Giovanni Stevanin, Christopher Ross, Dobrila Rudnicki, and Russell Margolis. Junctophilin 3 (jph3) expansion mutations causing huntington disease like 2 (hdl2) are common in south african patients with african ancestry and a huntington disease phenotype. American Journal of Medical Genetics Part B: Neuropsychiatric Genetics, 168:573-585, Oct 2015. URL: https://doi.org/10.1002/ajmg.b.32332, doi:10.1002/ajmg.b.32332. This article has 73 citations.

12. (anderson2025huntingtondiseaselike2 pages 10-11): DD Rudnicki and RL Margolis. Huntington disease-like 2. Definitions, Feb 2020. URL: https://doi.org/10.32388/lkfkvq, doi:10.32388/lkfkvq. This article has 11 citations.

13. (anderson2025huntingtondiseaselike2 pages 16-19): DD Rudnicki and RL Margolis. Huntington disease-like 2. Definitions, Feb 2020. URL: https://doi.org/10.32388/lkfkvq, doi:10.32388/lkfkvq. This article has 11 citations.

14. (margolis2016pathogenicinsightsfrom pages 2-4): Russell L. Margolis and Dobrila D. Rudnicki. Pathogenic insights from huntington's disease-like 2 and other huntington's disease genocopies. Current Opinion in Neurology, 29:743-748, Dec 2016. URL: https://doi.org/10.1097/wco.0000000000000386, doi:10.1097/wco.0000000000000386. This article has 13 citations and is from a peer-reviewed journal.

15. (seixas2012lossofjunctophilin‐3 pages 9-11): Ana I. Seixas, Susan E. Holmes, Hiroshi Takeshima, Amira Pavlovich, Nancy Sachs, Jennifer L. Pruitt, Isabel Silveira, Christopher A. Ross, Russell L. Margolis, and Dobrila D. Rudnicki. Loss of junctophilin‐3 contributes to huntington disease‐like 2 pathogenesis. Annals of Neurology, 71:245-257, Feb 2012. URL: https://doi.org/10.1002/ana.22598, doi:10.1002/ana.22598. This article has 88 citations and is from a highest quality peer-reviewed journal.

16. (wilburn2011anantisensecag media fdbbbc4c): Brian Wilburn, Dobrila D. Rudnicki, Jing Zhao, Tara Murphy Weitz, Yin Cheng, Xiaofeng Gu, Erin Greiner, Chang Sin Park, Nan Wang, Bryce L. Sopher, Albert R. La Spada, Alex Osmand, Russell L. Margolis, Yi E. Sun, and X. William Yang. An antisense cag repeat transcript at jph3 locus mediates expanded polyglutamine protein toxicity in huntington's disease-like 2 mice. Neuron, 70:427-440, May 2011. URL: https://doi.org/10.1016/j.neuron.2011.03.021, doi:10.1016/j.neuron.2011.03.021. This article has 168 citations and is from a highest quality peer-reviewed journal.

17. (wilburn2011anantisensecag media aa402816): Brian Wilburn, Dobrila D. Rudnicki, Jing Zhao, Tara Murphy Weitz, Yin Cheng, Xiaofeng Gu, Erin Greiner, Chang Sin Park, Nan Wang, Bryce L. Sopher, Albert R. La Spada, Alex Osmand, Russell L. Margolis, Yi E. Sun, and X. William Yang. An antisense cag repeat transcript at jph3 locus mediates expanded polyglutamine protein toxicity in huntington's disease-like 2 mice. Neuron, 70:427-440, May 2011. URL: https://doi.org/10.1016/j.neuron.2011.03.021, doi:10.1016/j.neuron.2011.03.021. This article has 168 citations and is from a highest quality peer-reviewed journal.

18. (anderson2025huntingtondiseaselike2 pages 11-14): DD Rudnicki and RL Margolis. Huntington disease-like 2. Definitions, Feb 2020. URL: https://doi.org/10.32388/lkfkvq, doi:10.32388/lkfkvq. This article has 11 citations.

19. (baine2016thefrequencyof pages 1-2): Fiona K. Baine, Amanda Krause, and L. Jacquie Greenberg. The frequency of huntington disease and huntington disease-like 2 in the south african population. Neuroepidemiology, 46:198-202, Feb 2016. URL: https://doi.org/10.1159/000444020, doi:10.1159/000444020. This article has 43 citations and is from a peer-reviewed journal.

20. (baine2016thefrequencyof pages 2-3): Fiona K. Baine, Amanda Krause, and L. Jacquie Greenberg. The frequency of huntington disease and huntington disease-like 2 in the south african population. Neuroepidemiology, 46:198-202, Feb 2016. URL: https://doi.org/10.1159/000444020, doi:10.1159/000444020. This article has 43 citations and is from a peer-reviewed journal.

21. (krause2015junctophilin3(jph3) pages 1-3): Amanda Krause, Claire Mitchell, Fahmida Essop, Susan Tager, James Temlett, Giovanni Stevanin, Christopher Ross, Dobrila Rudnicki, and Russell Margolis. Junctophilin 3 (jph3) expansion mutations causing huntington disease like 2 (hdl2) are common in south african patients with african ancestry and a huntington disease phenotype. American Journal of Medical Genetics Part B: Neuropsychiatric Genetics, 168:573-585, Oct 2015. URL: https://doi.org/10.1002/ajmg.b.32332, doi:10.1002/ajmg.b.32332. This article has 73 citations.

22. (anderson2025comparativeanalysisof pages 9-13): David G Anderson, Aline Ferreira-Correia, Filipe B Rodrigues, Lauren M Byrne, Edward J Wild, and Amanda Krause. Comparative analysis of neurofilament light chain in huntington's disease like 2 and huntington's disease. Journal of Huntington's Disease, 14:103-108, Nov 2025. URL: https://doi.org/10.1177/18796397241300141, doi:10.1177/18796397241300141. This article has 0 citations and is from a peer-reviewed journal.

23. (bates2015huntingtondisease pages 16-19): Gillian P. Bates, Ray Dorsey, James F. Gusella, Michael R. Hayden, Chris Kay, Blair R. Leavitt, Martha Nance, Christopher A. Ross, Rachael I. Scahill, Ronald Wetzel, Edward J. Wild, and Sarah J. Tabrizi. Huntington disease. Nature Reviews Disease Primers, Apr 2026. URL: https://doi.org/10.1038/nrdp.2015.5, doi:10.1038/nrdp.2015.5. This article has 1437 citations.

24. (krause2015junctophilin3(jph3) pages 8-10): Amanda Krause, Claire Mitchell, Fahmida Essop, Susan Tager, James Temlett, Giovanni Stevanin, Christopher Ross, Dobrila Rudnicki, and Russell Margolis. Junctophilin 3 (jph3) expansion mutations causing huntington disease like 2 (hdl2) are common in south african patients with african ancestry and a huntington disease phenotype. American Journal of Medical Genetics Part B: Neuropsychiatric Genetics, 168:573-585, Oct 2015. URL: https://doi.org/10.1002/ajmg.b.32332, doi:10.1002/ajmg.b.32332. This article has 73 citations.

25. (baine2016thefrequencyof pages 3-4): Fiona K. Baine, Amanda Krause, and L. Jacquie Greenberg. The frequency of huntington disease and huntington disease-like 2 in the south african population. Neuroepidemiology, 46:198-202, Feb 2016. URL: https://doi.org/10.1159/000444020, doi:10.1159/000444020. This article has 43 citations and is from a peer-reviewed journal.

26. (anderson2025comparativeanalysisof pages 6-9): David G Anderson, Aline Ferreira-Correia, Filipe B Rodrigues, Lauren M Byrne, Edward J Wild, and Amanda Krause. Comparative analysis of neurofilament light chain in huntington's disease like 2 and huntington's disease. Journal of Huntington's Disease, 14:103-108, Nov 2025. URL: https://doi.org/10.1177/18796397241300141, doi:10.1177/18796397241300141. This article has 0 citations and is from a peer-reviewed journal.

27. (anderson2025comparativeanalysisof pages 1-6): David G Anderson, Aline Ferreira-Correia, Filipe B Rodrigues, Lauren M Byrne, Edward J Wild, and Amanda Krause. Comparative analysis of neurofilament light chain in huntington's disease like 2 and huntington's disease. Journal of Huntington's Disease, 14:103-108, Nov 2025. URL: https://doi.org/10.1177/18796397241300141, doi:10.1177/18796397241300141. This article has 0 citations and is from a peer-reviewed journal.

28. (anderson2025huntingtondiseaselike2 pages 8-10): DD Rudnicki and RL Margolis. Huntington disease-like 2. Definitions, Feb 2020. URL: https://doi.org/10.32388/lkfkvq, doi:10.32388/lkfkvq. This article has 11 citations.
