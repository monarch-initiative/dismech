---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T15:02:14.058632'
end_time: '2026-05-06T15:25:09.491201'
duration_seconds: 1375.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Retinal Arterial Tortuosity
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Retinal Arterial Tortuosity
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Retinal Arterial Tortuosity** covering all of the
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
- **Disease Name:** Retinal Arterial Tortuosity
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Retinal Arterial Tortuosity** covering all of the
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


# Retinal Arterial Tortuosity (Familial Retinal Arteriolar Tortuosity; FRAT/RATOR): Disease Characteristics Research Report

## 1. Disease Information

### 1.1 Overview (current understanding)
Retinal arterial tortuosity (often discussed clinically as **familial retinal arteriolar tortuosity**, FRAT; also termed **retinal arterial tortuosity**, RATOR) is a rare, typically autosomal-dominant retinal vasculopathy characterized by **marked tortuosity/contortion of second- and third-order retinal arterioles**, with **relative sparing of first-order arterioles and the venous system**; this funduscopic pattern is repeatedly described as **pathognomonic** in familial forms. (zenteno2014nextgenerationsequencing pages 1-2, vilimelis2015newgenesinvolved pages 65-72, gasparini2024multiorganmanifestationsof pages 2-2)

A typical clinical issue is **episodic retinal hemorrhage** (intraretinal, preretinal/subhyaloid, sub-internal limiting membrane [sub-ILM], and occasionally subretinal/vitreous), causing **transient visual impairment** often triggered by minor stress, exertion, or Valsalva-like maneuvers; many episodes resolve spontaneously with good visual recovery. (gasparini2024multiorganmanifestationsof pages 2-2, chen2020bilateralandmultiple pages 1-3, saraf2019familialretinalarteriolar pages 3-5)

### 1.2 Key identifiers and nomenclature
- **MONDO (disease ontology)**: **MONDO_0008373** (“retinal arterial tortuosity”). (OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1)
- **OMIM**: **OMIM %180000** for familial retinal arteriolar/arterial tortuosity (historically “%” denoted unknown molecular basis). (vilimelis2015newgenesinvolveda pages 65-72, zenteno2014nextgenerationsequencing pages 1-2, vilimelis2015newgenesinvolveda pages 84-91)
- **Related MONDO entry**: **MONDO_0012726** (“autosomal dominant familial hematuria–retinal arteriolar tortuosity–contractures syndrome”)—a COL4A1/2-associated phenotype class in Open Targets. (OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1)

**Synonyms / alternative names** (as used in the literature retrieved here):
- Familial retinal arteriolar tortuosity (FRAT)
- Familial retinal arterial tortuosity
- Retinal arterial tortuosity (RATOR)
- fRAT (abbreviation used in some sources) (zenteno2014nextgenerationsequencing pages 1-2, vilimelis2015newgenesinvolveda pages 84-91, gasparini2024multiorganmanifestationsof pages 2-2)

**ICD-10/ICD-11 / MeSH / Orphanet IDs**: Not explicitly provided in the retrieved full-text excerpts; Open Targets indicates Orphanet as a source but did not return an Orphanet disease identifier in the retrieved evidence. (OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1)

### 1.3 Evidence source type
The disease knowledge in this report derives primarily from:
- **Human case reports/series** (FRAT clinical phenotype and hemorrhage triggers/outcomes). (chen2020bilateralandmultiple pages 1-3, obayashi2021acaseseries pages 2-4)
- **Human genetics studies** (segregating COL4A1 variant for FRAT). (zenteno2014nextgenerationsequencing pages 4-5)
- **Model organism mechanistic work** (Col4a1 mutant mice with retinal vascular pathology). (alavi2016col4a1mutationscause pages 2-3)
- **Aggregated disease-level evidence / protocols** from a 2024 systematic review + cohort-based management protocol for COL4A1/2-related disease (in which retinal arterial tortuosity is a component feature). (gasparini2024multiorganmanifestationsof pages 19-19)


## 2. Etiology

### 2.1 Primary causal factors
**Genetic (major)**: Familial retinal arteriolar/arterial tortuosity is strongly linked to **monoallelic pathogenic variants in COL4A1** (and more broadly retinal arterial tortuosity is associated with **COL4A1/COL4A2**). (zenteno2014nextgenerationsequencing pages 4-5, gasparini2024multiorganmanifestationsof pages 2-2, OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1)

**Mechanistic concept**: COL4A1 encodes the type IV collagen α1 chain, a core component of vascular basement membranes. Glycine substitutions in the collagenous domain can disrupt collagen IV assembly and secretion (see Mechanism section). (zenteno2014nextgenerationsequencing pages 4-5)

### 2.2 Risk factors (clinical/episode-level)
While disease susceptibility is genetic, **episodic hemorrhages** are frequently reported to be precipitated by:
- **Physical exertion / minor trauma** (gasparini2024multiorganmanifestationsof pages 2-2, zenteno2014nextgenerationsequencing pages 1-2)
- **Valsalva-like maneuvers/straining** (e.g., running) (chen2020bilateralandmultiple pages 1-3)

In a 13-year-old FRAT patient, hemorrhages occurred after running 800 m, consistent with a Valsalva-like trigger. (chen2020bilateralandmultiple pages 1-3)

### 2.3 Protective factors / gene–environment interactions
No specific protective factors (genetic or environmental) were identified in the retrieved sources.

Gene–environment interactions are implied by variable expressivity and hemorrhage triggers (exertion/trauma), and by explicit suggestions that environmental factors and/or genetic modifiers influence phenotype (ocular-only FRAT vs multisystem COL4A1 disease). (zenteno2014nextgenerationsequencing pages 4-5, vilimelis2015newgenesinvolveda pages 95-96)


## 3. Phenotypes (clinical features; HPO suggestions)

A structured phenotype summary is provided in the table artifact below.

| Phenotype feature | Suggested HPO term(s) | Typical onset / course | Triggers / modifiers | Complications / QoL impact | Quantitative data | Key notes / citations |
|---|---|---|---|---|---|---|
| Retinal arteriolar tortuosity distribution in familial disease (FRAT/RATOR) | Retinal vascular tortuosity [suggest HP term: retinal arteriolar tortuosity if curated]; Abnormality of retinal vasculature (suggested) | Often recognized in childhood or early adulthood; usually chronic/stable between hemorrhagic episodes | May become clinically relevant during exertion or minor trauma because hemorrhage can occur despite otherwise stable vessel morphology | Can predispose to recurrent retinal hemorrhage and transient visual disturbance; funduscopic pattern is considered highly characteristic/pathognomonic | Classic pattern: marked tortuosity of **second- and third-order retinal arterioles** with **normal first-order arteries and venous sparing** | Core diagnostic description repeated across FRAT/COL4A1 literature (zenteno2014nextgenerationsequencing pages 1-2, vilimelis2015newgenesinvolved pages 65-72, vilimelis2015newgenesinvolveda pages 84-91, gasparini2024multiorganmanifestationsof pages 2-2, saraf2019familialretinalarteriolar pages 1-2) |
| EDS-associated retinal arterial tortuosity phenotype | Abnormal retinal vasculature; Retinal vascular tortuosity (suggested) | Adult cohort described; variable severity from mild to severe | Not clearly linked to hypertension or diabetes in the cohort studied | Usually an imaging finding; establishes that tortuosity also occurs outside FRAT and may broaden differential diagnosis | In 142 EDS patients, **37.3% definite RAT**, **10.6% possible RAT**, **52.1% no RAT**; among definite RAT eyes: **39.2% mild**, **40.2% moderate**, **20.6% severe**; vessel involvement: **84.9% first-order arterioles**, **35.8% macular arterioles**, **1.9% arteriovenous** | Important differential: unlike FRAT, EDS-associated RAT commonly involved **first-order arterioles** (ghoraba2023retinalarterialtortuosity pages 2-5, ghoraba2023retinalarterialtortuosity pages 1-2, ghoraba2023retinalarterialtortuosity pages 5-5) |
| Retinal hemorrhages: intraretinal / subretinal / premacular-sub-ILM | Retinal hemorrhage; Intraretinal hemorrhage; Subretinal hemorrhage; Preretinal hemorrhage / Premacular hemorrhage (suggested) | Episodic; often sudden onset with spontaneous resolution over weeks to months | Exercise, minor trauma, Valsalva-like maneuvers/straining; running has been reported as a trigger | Acute visual loss, central scotoma; occasional ERM after intervention; anxiety/functional limitation during episodes | FRAT family reports describe recurrent perifoveal/foveal hemorrhages; in one 13-year-old case: **6 sub-ILM hemorrhages OD** (largest **~1.5 DD**) and **2 OS** (largest **5.5 DD**) | Hemorrhage is the main vision-threatening event in FRAT; sub-ILM/premacular hemorrhage well documented by fundus/OCT/FFA (vilimelis2015newgenesinvolveda pages 93-95, vilimelis2015newgenesinvolved pages 93-95, chen2020bilateralandmultiple pages 1-3, chen2020bilateralandmultiple pages 3-5, chen2020bilateralandmultiple media c2e15b79) |
| Transient vision loss / blurred vision / central scotoma | Transient visual loss; Blurred vision; Central scotoma (suggested) | Usually episodic and linked to hemorrhage rather than progressive neuroretinal degeneration | Often precipitated by hemorrhage after exertion or minor trauma | Temporary loss of reading/central vision; can be bilateral in severe premacular hemorrhage; long-term prognosis often good if hemorrhage clears | Visual acuity in the 2020 case improved from **20/100 OD, 20/160 OS** to **20/16 OD, 20/20 OS** after combined treatment/observation | Most affected individuals are asymptomatic between episodes, but hemorrhage can cause transient marked impairment (saraf2019familialretinalarteriolar pages 1-2, gasparini2024multiorganmanifestationsof pages 2-2, chen2020bilateralandmultiple pages 1-3, chen2020bilateralandmultiple pages 3-5) |
| Nailbed capillary tortuosity | Capillary tortuosity (suggested) | Chronic accompanying microvascular finding when present | No specific trigger established | May indicate extra-retinal microvascular involvement; little direct QoL impact but useful diagnostically | Historical reports note marked nailbed capillary tortuosity; one thesis notes abnormal capillary tortuosity threshold **>~20%**, with one family showing **>30%** loops affected | Supports systemic small-vessel involvement beyond the retina in some families (vilimelis2015newgenesinvolved pages 65-72, vilimelis2015newgenesinvolveda pages 65-72) |
| Systemic associations: HANAC-spectrum COL4A1 disease | Hematuria; Cerebral aneurysm; Muscle cramps; Leukoencephalopathy; Raynaud phenomenon; Arrhythmia (suggested HPO mappings) | Variable; penetrance and expressivity are highly heterogeneous, including asymptomatic/oligosymptomatic carriers | Likely modified by genotype plus environmental/genetic modifiers | Renal disease, aneurysm risk, muscle symptoms, neurologic disease; requires multidisciplinary surveillance | In aggregated COL4A1/2 data: **retinal arterial tortuosity 58/685 (8.5%)**; among asymptomatic/oligosymptomatic carriers undergoing ophthalmic workup, retinal vascular tortuosity detected in **5/13 (38.5%)** | Same COL4A1 p.Gly510Arg variant can present as isolated FRAT or multisystem HANAC-like disease, demonstrating variable expressivity (vilimelis2015newgenesinvolved pages 95-96, gasparini2024multiorganmanifestationsof pages 2-2, gasparini2024multiorganmanifestationsof pages 19-19, vilimelis2015newgenesinvolveda pages 95-96, zenteno2014nextgenerationsequencing pages 4-5) |
| Brain small-vessel disease / intracerebral hemorrhage / ischemic lesions in COL4A1/2-related disease | Intracerebral hemorrhage; Cerebral small vessel disease; Lacunar stroke; Leukoencephalopathy (suggested) | Can occur from childhood to adulthood; chronic vasculopathy with risk of hemorrhagic and ischemic events | Blood-pressure burden and trauma likely relevant modifiers; monogenic background is primary | Major morbidity from stroke, seizures, cognitive/neurologic impairment; retinal arteriolar tortuosity can be a valuable diagnostic clue | Literature aggregation in COL4A1/2 disease: **stroke 203/685 (29.6%)**, **seizures/epilepsy 199/685 (29.0%)**, **porencephaly/schizencephaly 168/685 (24.5%)**; case reports include hippocampal infarction and ICH with tortuous retinal arterioles | Retinal arteriolar tortuosity is emphasized as a clue that should prompt evaluation for monogenic COL4A1/2 vasculopathy (kim2017familialretinalarteriolar pages 2-4, bouchart2024clinicalreasoninga pages 3-5, gasparini2024multiorganmanifestationsof pages 2-2, gasparini2024multiorganmanifestationsof pages 19-19) |
| Course and intervention-associated sequelae after premacular hemorrhage | Epiretinal membrane; Wrinkling of retinal internal limiting membrane (suggested) | Usually recovery after spontaneous resorption or drainage; sequelae may follow laser membranotomy | Procedure-related risk with Nd:YAG membranotomy | ERM, ILM wrinkling, rarely other iatrogenic macular complications; affects metamorphopsia risk and follow-up needs | In the 2020 bilateral case, ERM developed in the left eye despite excellent acuity recovery | Supports careful individualized management; observation alone is reasonable for smaller hemorrhages, laser may accelerate recovery in selected large premacular bleeds (chen2020bilateralandmultiple pages 5-5, chen2020bilateralandmultiple pages 1-3, chen2020bilateralandmultiple pages 3-5) |


*Table: This table summarizes the main clinical phenotype features reported for familial retinal arterial/arteriolar tortuosity and related COL4A1/2-associated presentations, including suggested HPO mappings, course, triggers, complications, and quantitative findings. It is useful for structured knowledge-base curation and differential diagnosis, including comparison with EDS-associated retinal arterial tortuosity.*

### 3.1 Core ocular phenotype (familial FRAT/RATOR)
**Definition/diagnostic pattern**: “marked contortion of the second- and third-order retinal arteries with no impact on the first-order arteries and the venous system.” (gasparini2024multiorganmanifestationsof pages 2-2)

**Hemorrhages and transient visual symptoms**: Most affected individuals experience “episodes of transient vision impairment caused by retinal hemorrhage prompted by minor stress or trauma.” (gasparini2024multiorganmanifestationsof pages 2-2)

### 3.2 Notable differential diagnosis and phenotypic overlap
- **Ehlers–Danlos syndromes (EDS)**: A 2023 retrospective cohort study found **retinal arterial tortuosity (RAT)** was common in EDS, with **37.3% definite RAT** and **10.6% possible RAT** among 142 imaged EDS patients; importantly, EDS-associated RAT frequently involved **first-order arterioles (84.9%)**, which contrasts with classic FRAT affecting second/third-order arterioles. (ghoraba2023retinalarterialtortuosity pages 1-2, ghoraba2023retinalarterialtortuosity pages 5-5)


## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **COL4A1** (primary gene for familial FRAT in multiple pedigrees; strong evidence). (zenteno2014nextgenerationsequencing pages 4-5)
- **COL4A2** (associated with retinal arterial tortuosity within the broader COL4A1/2 disease spectrum in aggregated databases). (OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1)

### 4.2 Pathogenic variants (examples)
**COL4A1 c.1528G>A (p.Gly510Arg), heterozygous missense**:
- Identified by WES and confirmed by Sanger in affected family members with FRAT; absent in unaffected daughter and in multiple control datasets. (zenteno2014nextgenerationsequencing pages 1-2, zenteno2014nextgenerationsequencing pages 4-5)
- Population data in one study: absent from **200 ethnically matched control alleles** and **~8,600 exomes** in the NHLBI Exome Variant Server. (zenteno2014nextgenerationsequencing pages 4-5)
- Genotype–phenotype variability: the same p.Gly510Arg variant previously reported in HANAC syndrome, while in the FRAT pedigree no extra-ocular features were found, supporting variable expressivity. (zenteno2014nextgenerationsequencing pages 4-5)

**Variant localization and domain concept**:
- The p.Gly510Arg substitution lies within a “critical region (residues 498–528) that includes integrin binding sites” in the collagenous domain. (zenteno2014nextgenerationsequencing pages 4-5)

### 4.3 Functional consequences (molecular)
Glycine substitutions in the collagenous domain are described as disrupting collagen biology: “perturb triple helix assembly, impair secretion of collagen heterotrimers, and cause intracellular accumulation of misfolded proteins.” (zenteno2014nextgenerationsequencing pages 4-5, vilimelis2015newgenesinvolveda pages 95-96)

### 4.4 Modifier genes / variable expressivity
Multiple sources emphasize that identical COL4A1 mutations can yield ocular-only FRAT vs multisystem disease (HANAC), consistent with modifier effects (genetic background, environment). (vilimelis2015newgenesinvolveda pages 95-96, zenteno2014nextgenerationsequencing pages 4-5)

### 4.5 Epigenetics / chromosomal abnormalities
No disease-specific epigenetic or chromosomal abnormality evidence was identified in the retrieved texts.


## 5. Environmental Information
No specific environmental toxins, lifestyle factors, or infectious agents were identified as causal. The major “environmental” role described is **episode triggering** (exertion/trauma/Valsalva-like stress) for hemorrhage in genetically susceptible individuals. (chen2020bilateralandmultiple pages 1-3, saraf2019familialretinalarteriolar pages 3-5)


## 6. Mechanism / Pathophysiology

### 6.1 Mechanistic causal chain (COL4A1/2-related small-vessel fragility)
A unifying model supported by human genetics and mouse data is:
1) **COL4A1 pathogenic variant** → abnormal type IV collagen network in vascular basement membranes (zenteno2014nextgenerationsequencing pages 4-5)
2) **Primary retinal vascular defects** (vessel instability/tortuosity, permeability, hemorrhage) (alavi2016col4a1mutationscause pages 7-8, alavi2016col4a1mutationscause pages 2-3)
3) **Secondary retinal responses** (reactive Müller glia activation; pro-angiogenic factor upregulation; possible neovascular complications in some COL4A1 contexts) (alavi2016col4a1mutationscause pages 7-8)
4) Clinical manifestation as **arteriolar tortuosity + hemorrhagic episodes** with transient vision loss. (gasparini2024multiorganmanifestationsof pages 2-2, chen2020bilateralandmultiple pages 1-3)

### 6.2 Evidence from model organisms (mechanistic depth)
In Col4a1 mutant mice, retinal pathology included hemorrhage and angiogenic lesions. Key quantitative findings include:
- Retinal pathology (serous chorioretinopathy, hemorrhages, fibrosis or pathogenic angiogenesis) occurred in **up to ~90%** of mutant eyes depending on age and allele. (alavi2016col4a1mutationscause pages 1-2)
- In a large cohort, penetrance increased with age (estimated **36–43% by P21** and **68–88% after 1 month** in one line), and “all mutant eyes exhibited abnormal vascular branching and vascular tortuosity” on fluorescein angiography. (alavi2016col4a1mutationscause pages 2-3)
- Cell-type dissection: “Conditional expression of mutant Col4a1 in vascular endothelium, but not RPE, phenocopies the retinal defects.” (alavi2016col4a1mutationscause pages 7-8)
- Lesion-associated glial response: Müller cell activation (GFAP/vimentin) and elevated pro-angiogenic factors (Vegfa, Pdgfb, Pgf). (alavi2016col4a1mutationscause pages 7-8)

### 6.3 Pathways / ontology suggestions
**GO Biological Process (suggested)**
- extracellular matrix organization
- basement membrane organization
- angiogenesis / regulation of VEGF signaling
- blood vessel morphogenesis
- response to oxidative stress / wound healing (secondary)

**Cell types (CL suggestions)**
- vascular endothelial cell
- pericyte (retinal microvasculature)
- Müller glial cell (reactive gliosis noted) (alavi2016col4a1mutationscause pages 7-8)


## 7. Anatomical Structures Affected

### 7.1 Primary anatomical site
- **Retina – arteriolar vasculature** (especially second- and third-order arterioles in classic FRAT/RATOR). (gasparini2024multiorganmanifestationsof pages 2-2)

**UBERON suggestions**
- retina (UBERON:0000966)
- retinal blood vessel (UBERON term as applicable)

### 7.2 Secondary / systemic involvement (context-dependent)
Although FRAT is often described as primarily ocular, retinal arteriolar tortuosity can be a clue to broader COL4A1/2 vasculopathy, including cerebral small vessel disease and hemorrhage risk. (bouchart2024clinicalreasoninga pages 3-5)


## 8. Temporal Development

### 8.1 Onset
Onset is often described in **childhood or early adulthood** in familial FRAT. (zenteno2014nextgenerationsequencing pages 1-2)

### 8.2 Course
- Baseline vascular tortuosity is chronic.
- Hemorrhage episodes are intermittent; visual prognosis is usually good with recovery after hemorrhage clearance. (saraf2019familialretinalarteriolar pages 1-2)
- Tortuosity may increase with age over decades in some individuals. (saraf2019familialretinalarteriolar pages 3-5)


## 9. Inheritance and Population

### 9.1 Inheritance
Familial FRAT is generally **autosomal dominant**; one pedigree includes male-to-male transmission and vertical inheritance consistent with AD. (zenteno2014nextgenerationsequencing pages 1-2)

Open Targets annotations for retinal arterial tortuosity and related entries list **monoallelic autosomal** allelic requirements. (OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1)

### 9.2 Epidemiology / prevalence
Robust population prevalence estimates were not found in the retrieved evidence. A historical estimate notes “approximately 100 cases described” (as of the cited older literature compilation), reflecting rarity and likely underdiagnosis. (vilimelis2015newgenesinvolved pages 65-72)

### 9.3 Penetrance / expressivity
Penetrance and expressivity in COL4A1/2-related disease are explicitly described as highly variable, with asymptomatic/oligosymptomatic carriers detectable by protocolized screening. (gasparini2024multiorganmanifestationsof pages 19-19)


## 10. Diagnostics

### 10.1 Clinical diagnosis (ophthalmic)
Diagnosis is commonly made via:
- Dilated fundus examination / color fundus photography identifying the characteristic arteriolar pattern (vilimelis2015newgenesinvolved pages 65-72)
- Fluorescein angiography (FA) to document vessel anatomy and hemorrhage-related blocked fluorescence and to exclude leakage in some cases (chen2020bilateralandmultiple media c2e15b79, obayashi2021acaseseries pages 2-4)
- Optical coherence tomography (OCT) to localize premacular hemorrhage (subhyaloid vs sub-ILM) and follow resolution (chen2020bilateralandmultiple pages 1-3)
- OCT angiography (OCTA), including swept-source OCTA, increasingly used to delineate tortuosity and quantify it objectively (saraf2019familialretinalarteriolar pages 1-2, obayashi2021acaseseries pages 4-5)

**Real-world imaging example (figure evidence)**: In a FRAT patient with bilateral premacular hemorrhages, Figure 1 demonstrates tortuous arterioles on fundus photographs and corresponding SD-OCT evidence of dome-shaped sub-ILM hemorrhage. (chen2020bilateralandmultiple media c2e15b79)

### 10.2 Genetic testing
- **Single-gene testing / targeted panels** including COL4A1 can be used; WES identified COL4A1 p.Gly510Arg in one FRAT pedigree. (zenteno2014nextgenerationsequencing pages 4-5)
- Diagnostic caveat: FRAT-like families can be negative on panels. In one family case series, a targeted NGS panel of 328 genes “found no pathogenic variants … including COL4A1,” and the family declined further testing, suggesting locus heterogeneity, undetected variant types, or limitations of panels. (obayashi2021acaseseries pages 4-5)

### 10.3 Differential diagnosis (examples)
In the neurologic setting, retinal arteriolar tortuosity is highlighted as a clue to COL4A1/2-related disorders and helps distinguish from other hereditary CSVDs (e.g., CADASIL, CARASIL, Fabry). (bouchart2024clinicalreasoninga pages 3-5)


## 11. Outcome / Prognosis

### 11.1 Visual prognosis
Visual prognosis is generally favorable. A case series documented spontaneous resolution of hemorrhage with recovery to **20/20** by 1 year in a teenager, and good outcomes overall with observation. (obayashi2021acaseseries pages 1-2)

A 2019 OCTA-based FRAT report states prognosis is “excellent” with most patients recovering normal acuity after hemorrhage clearance, though some may have mild irreversible impairment due to macular pigment changes. (saraf2019familialretinalarteriolar pages 3-5)

### 11.2 Systemic prognosis considerations (COL4A1/2 context)
When retinal arteriolar tortuosity occurs in COL4A1/2 vasculopathy, neurologic risks (ICH, cerebral microbleeds, seizures) can dominate morbidity, warranting multidisciplinary evaluation. (bouchart2024clinicalreasoninga pages 3-5)


## 12. Treatment / Management

### 12.1 Acute hemorrhage management
- **Observation** is standard for many hemorrhages, with spontaneous reabsorption and visual recovery. (saraf2019familialretinalarteriolar pages 1-2, obayashi2021acaseseries pages 1-2)
- **Nd:YAG laser membranotomy** can be considered for large premacular sub-ILM hemorrhage when rapid visual recovery is needed; a bilateral FRAT case achieved improvement from **20/100 and 20/160** to **20/16 and 20/20**, but developed an **epiretinal membrane (ERM)** in one eye, and the authors caution about long-term safety/placement considerations. (chen2020bilateralandmultiple pages 1-3, chen2020bilateralandmultiple pages 5-5)

**MAXO suggestions**
- Observation / watchful waiting
- Laser membranotomy (Nd:YAG)
- Patient education / avoidance counseling

### 12.2 Prevention of hemorrhage episodes
Avoidance of triggering activities (straining/Valsalva-like maneuvers) is commonly recommended in case management. (saraf2019familialretinalarteriolar pages 1-2)

### 12.3 Multiorgan management (COL4A1/2 carriers)
A 2024 expert protocol proposes baseline and follow-up screening in COL4A1/2 variant carriers, including brain MRI with angiographic sequences, baseline labs (blood count, CK, coagulation indices), and ophthalmologic evaluation with OCT-based monitoring depending on initial severity; prenatal imaging is suggested for pregnancy risk counseling. (gasparini2024multiorganmanifestationsof pages 19-19)


## 13. Prevention

Primary prevention is not established (genetic). Key prevention concepts are:
- **Secondary prevention / surveillance** for COL4A1/2 carriers via periodic multi-organ evaluation (brain imaging, ophthalmology, lab screening). (gasparini2024multiorganmanifestationsof pages 19-19)
- **Tertiary prevention**: avoid triggers for hemorrhage; control modifiable vascular risks (e.g., blood pressure) in those with COL4A1/2 vasculopathy. (bouchart2024clinicalreasoninga pages 3-5)


## 14. Other Species / Natural Disease
No naturally occurring veterinary analogs were identified in the retrieved evidence.


## 15. Model Organisms
A well-developed mechanistic model exists in **Col4a1 mutant mice**, which recapitulate retinal vascular tortuosity, hemorrhage, and progressive retinopathy; endothelial expression of mutant Col4a1 is sufficient to induce the phenotype. (alavi2016col4a1mutationscause pages 7-8, alavi2016col4a1mutationscause pages 2-3)


## 16. Recent developments and real-world implementations (prioritizing 2023–2024)

### 16.1 2023: EDS association study (real-world EHR + imaging repository)
A 2023 Eye study used a large institutional repository (STARR) and multimodal imaging to systematically grade RAT in EDS, providing practical prevalence estimates and a grading framework with intergrader agreement (kappa). It reported **37.3% definite RAT** and subclassified severity and vessel distributions. (ghoraba2023retinalarterialtortuosity pages 1-2, ghoraba2023retinalarterialtortuosity pages 2-5)

### 16.2 2024: Clinical reasoning and diagnostic positioning in Neurology
A 2024 Neurology “Clinical Reasoning” article emphasizes that “retinal arteriolar tortuosity, while not always present, is an important finding that strongly suggests the diagnosis of COL4A1/2-related disorders,” integrating ophthalmic findings into monogenic CSVD workups and highlighting management implications (blood pressure control; avoiding head trauma). (bouchart2024clinicalreasoninga pages 3-5)

### 16.3 2024: Management protocol for COL4A1/2 disease
A 2024 AJMG Seminars paper proposes an explicit screening/management protocol (brain MRI/MRA, baseline labs, ophthalmology/OCT monitoring, prenatal imaging, genetic counseling). This is a concrete step toward standard-of-care harmonization for COL4A1/2 carriers in which retinal arterial tortuosity is a recognized phenotype component. (gasparini2024multiorganmanifestationsof pages 19-19)

### 16.4 Clinical trials / prospective implementation
An actively recruiting ClinicalTrials.gov study (NCT07374913; sponsor: Meyer Children’s Hospital IRCCS; posted 2021, currently recruiting) operationalizes multi-organ screening for COL4A1/2 variant carriers in routine care settings with standardized ophthalmological OCT assessments, cardiology testing, and exploratory plasma biomarkers (MMP2/MMP9). (NCT07374913 chunk 1)


## Key limitations of the current evidence base
- FRAT/RATOR remains rare; much evidence comes from case reports/series, limiting precise penetrance and population prevalence estimates. (vilimelis2015newgenesinvolved pages 65-72)
- Database identifiers (Orphanet/ICD/MeSH) were not recoverable from the retrieved excerpts; additional targeted database queries (OMIM/Orphanet directly) would be needed for full code normalization. (OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1)
- COL4A2-specific variant-to-FRAT evidence was limited in the retrieved full texts; associations appear in aggregated resources. (OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1)


# Identifier normalization artifact
| Preferred name | Key synonyms / alternative names | MONDO ID(s) | OMIM identifier | Associated gene(s) | Typical inheritance | Key defining diagnostic description |
|---|---|---|---|---|---|---|
| Retinal arterial tortuosity | Retinal arteriolar tortuosity; familial retinal arteriolar tortuosity (FRAT); familial retinal arterial tortuosity; fRAT; retinal arterial tortuosity (RATOR) (zenteno2014nextgenerationsequencing pages 1-2, vilimelis2015newgenesinvolveda pages 84-91, gasparini2024multiorganmanifestationsof pages 2-2) | MONDO:0008373 = retinal arterial tortuosity; MONDO:0012726 = autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome (OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1) | OMIM %180000 for familial retinal arteriolar/arterial tortuosity (vilimelis2015newgenesinvolveda pages 65-72, zenteno2014nextgenerationsequencing pages 1-2, vilimelis2015newgenesinvolveda pages 84-91) | COL4A1 strongly supported; COL4A2 also associated in Open Targets evidence for retinal arterial tortuosity / related syndrome (OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1, vilimelis2015newgenesinvolveda pages 84-91, gasparini2024multiorganmanifestationsof pages 2-2) | Usually autosomal dominant / monoallelic; vertical transmission and male-to-male transmission reported in families (OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1, zenteno2014nextgenerationsequencing pages 1-2, vilimelis2015newgenesinvolveda pages 84-91) | Marked tortuosity/contortion of second- and third-order retinal arteries/arterioles, typically with normal first-order arteries and sparing of the venous system; funduscopic appearance described as pathognomonic (vilimelis2015newgenesinvolveda pages 65-72, zenteno2014nextgenerationsequencing pages 1-2, vilimelis2015newgenesinvolved pages 65-72, gasparini2024multiorganmanifestationsof pages 2-2) |


*Table: This table summarizes the principal disease names, identifiers, genes, inheritance, and defining diagnostic features for retinal arterial/arteriolar tortuosity. It is useful as a compact normalization reference for disease knowledge-base curation.*

References

1. (zenteno2014nextgenerationsequencing pages 1-2): Juan C. Zenteno, Jaume Crespí, Beatriz Buentello-Volante, Jose A. Buil, Francisca Bassaganyas, Jose I. Vela-Segarra, Jesus Diaz-Cascajosa, and Maria T. Marieges. Next generation sequencing uncovers a missense mutation in col4a1 as the cause of familial retinal arteriolar tortuosity. Graefe's Archive for Clinical and Experimental Ophthalmology, 252:1789-1794, Sep 2014. URL: https://doi.org/10.1007/s00417-014-2800-6, doi:10.1007/s00417-014-2800-6. This article has 55 citations.

2. (vilimelis2015newgenesinvolved pages 65-72): J Crespí Vilimelis. New genes involved in rare diseases in ophthalmology. Unknown journal, 2015.

3. (gasparini2024multiorganmanifestationsof pages 2-2): Simone Gasparini, Simona Balestrini, Luigi Francesco Saccaro, Giacomo Bacci, Giorgia Panichella, Martino Montomoli, Gaetano Cantalupo, Stefania Bigoni, Giorgia Mancano, Simona Pellacani, Vincenzo Leuzzi, Nila Volpi, Francesco Mari, Federico Melani, Mara Cavallin, Tiziana Pisano, Giulio Porcedda, Augusto Vaglio, Davide Mei, Carmen Barba, Elena Parrini, and Renzo Guerrini. Multiorgan manifestations of col4a1 and col4a2 variants and proposal for a clinical management protocol. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, Jul 2024. URL: https://doi.org/10.1002/ajmg.c.32099, doi:10.1002/ajmg.c.32099. This article has 21 citations.

4. (chen2020bilateralandmultiple pages 1-3): Ting Chen, Hongmei Zheng, Yunyun Wang, Junyi Hu, and Changzheng Chen. Bilateral and multiple sub-internal limiting membrane hemorrhages in a familial retinal arteriolar tortuosity patient by valsalva-like mechanism: an observational case report. BMC Ophthalmology, Apr 2020. URL: https://doi.org/10.1186/s12886-020-01413-0, doi:10.1186/s12886-020-01413-0. This article has 8 citations and is from a peer-reviewed journal.

5. (saraf2019familialretinalarteriolar pages 3-5): Steven S. Saraf, Ariel J. Tyring, Chieh-Li Chen, Thao Phuong Le, Robert E. Kalina, Ruikang K. Wang, and Jennifer R. Chao. Familial retinal arteriolar tortuosity and quantification of vascular tortuosity using swept-source optical coherence tomography angiography. American Journal of Ophthalmology Case Reports, 14:74-78, Jun 2019. URL: https://doi.org/10.1016/j.ajoc.2019.03.001, doi:10.1016/j.ajoc.2019.03.001. This article has 24 citations.

6. (OpenTargets Search: retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1): Open Targets Query (retinal arterial tortuosity,familial retinal arterial tortuosity-COL4A1, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (vilimelis2015newgenesinvolveda pages 65-72): J Crespí Vilimelis. New genes involved in rare diseases in ophthalmology. Unknown journal, 2015.

8. (vilimelis2015newgenesinvolveda pages 84-91): J Crespí Vilimelis. New genes involved in rare diseases in ophthalmology. Unknown journal, 2015.

9. (obayashi2021acaseseries pages 2-4): Tomohiro Obayashi, Aki Kato, Harumitsu Suzuki, Kei Ohashi, Munenori Yoshida, Yu Shibata, Yuichiro Ogura, and Tsutomu Yasukawa. A case series from a single family of familial retinal arteriolar tortuosity with common history of sudden visual loss. American Journal of Ophthalmology Case Reports, 24:101230, Dec 2021. URL: https://doi.org/10.1016/j.ajoc.2021.101230, doi:10.1016/j.ajoc.2021.101230. This article has 2 citations.

10. (zenteno2014nextgenerationsequencing pages 4-5): Juan C. Zenteno, Jaume Crespí, Beatriz Buentello-Volante, Jose A. Buil, Francisca Bassaganyas, Jose I. Vela-Segarra, Jesus Diaz-Cascajosa, and Maria T. Marieges. Next generation sequencing uncovers a missense mutation in col4a1 as the cause of familial retinal arteriolar tortuosity. Graefe's Archive for Clinical and Experimental Ophthalmology, 252:1789-1794, Sep 2014. URL: https://doi.org/10.1007/s00417-014-2800-6, doi:10.1007/s00417-014-2800-6. This article has 55 citations.

11. (alavi2016col4a1mutationscause pages 2-3): Marcel V. Alavi, Mao Mao, Bradley T. Pawlikowski, Manana Kvezereli, Jacque L. Duncan, Richard T. Libby, Simon W. M. John, and Douglas B. Gould. Col4a1 mutations cause progressive retinal neovascular defects and retinopathy. Scientific Reports, Jan 2016. URL: https://doi.org/10.1038/srep18602, doi:10.1038/srep18602. This article has 58 citations and is from a peer-reviewed journal.

12. (gasparini2024multiorganmanifestationsof pages 19-19): Simone Gasparini, Simona Balestrini, Luigi Francesco Saccaro, Giacomo Bacci, Giorgia Panichella, Martino Montomoli, Gaetano Cantalupo, Stefania Bigoni, Giorgia Mancano, Simona Pellacani, Vincenzo Leuzzi, Nila Volpi, Francesco Mari, Federico Melani, Mara Cavallin, Tiziana Pisano, Giulio Porcedda, Augusto Vaglio, Davide Mei, Carmen Barba, Elena Parrini, and Renzo Guerrini. Multiorgan manifestations of col4a1 and col4a2 variants and proposal for a clinical management protocol. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, Jul 2024. URL: https://doi.org/10.1002/ajmg.c.32099, doi:10.1002/ajmg.c.32099. This article has 21 citations.

13. (vilimelis2015newgenesinvolveda pages 95-96): J Crespí Vilimelis. New genes involved in rare diseases in ophthalmology. Unknown journal, 2015.

14. (saraf2019familialretinalarteriolar pages 1-2): Steven S. Saraf, Ariel J. Tyring, Chieh-Li Chen, Thao Phuong Le, Robert E. Kalina, Ruikang K. Wang, and Jennifer R. Chao. Familial retinal arteriolar tortuosity and quantification of vascular tortuosity using swept-source optical coherence tomography angiography. American Journal of Ophthalmology Case Reports, 14:74-78, Jun 2019. URL: https://doi.org/10.1016/j.ajoc.2019.03.001, doi:10.1016/j.ajoc.2019.03.001. This article has 24 citations.

15. (ghoraba2023retinalarterialtortuosity pages 2-5): Hashem H. Ghoraba and Darius M. Moshfeghi. Retinal arterial tortuosity in ehlers–danlos syndromes. Eye, 37:1936-1941, Oct 2023. URL: https://doi.org/10.1038/s41433-022-02278-x, doi:10.1038/s41433-022-02278-x. This article has 4 citations and is from a peer-reviewed journal.

16. (ghoraba2023retinalarterialtortuosity pages 1-2): Hashem H. Ghoraba and Darius M. Moshfeghi. Retinal arterial tortuosity in ehlers–danlos syndromes. Eye, 37:1936-1941, Oct 2023. URL: https://doi.org/10.1038/s41433-022-02278-x, doi:10.1038/s41433-022-02278-x. This article has 4 citations and is from a peer-reviewed journal.

17. (ghoraba2023retinalarterialtortuosity pages 5-5): Hashem H. Ghoraba and Darius M. Moshfeghi. Retinal arterial tortuosity in ehlers–danlos syndromes. Eye, 37:1936-1941, Oct 2023. URL: https://doi.org/10.1038/s41433-022-02278-x, doi:10.1038/s41433-022-02278-x. This article has 4 citations and is from a peer-reviewed journal.

18. (vilimelis2015newgenesinvolveda pages 93-95): J Crespí Vilimelis. New genes involved in rare diseases in ophthalmology. Unknown journal, 2015.

19. (vilimelis2015newgenesinvolved pages 93-95): J Crespí Vilimelis. New genes involved in rare diseases in ophthalmology. Unknown journal, 2015.

20. (chen2020bilateralandmultiple pages 3-5): Ting Chen, Hongmei Zheng, Yunyun Wang, Junyi Hu, and Changzheng Chen. Bilateral and multiple sub-internal limiting membrane hemorrhages in a familial retinal arteriolar tortuosity patient by valsalva-like mechanism: an observational case report. BMC Ophthalmology, Apr 2020. URL: https://doi.org/10.1186/s12886-020-01413-0, doi:10.1186/s12886-020-01413-0. This article has 8 citations and is from a peer-reviewed journal.

21. (chen2020bilateralandmultiple media c2e15b79): Ting Chen, Hongmei Zheng, Yunyun Wang, Junyi Hu, and Changzheng Chen. Bilateral and multiple sub-internal limiting membrane hemorrhages in a familial retinal arteriolar tortuosity patient by valsalva-like mechanism: an observational case report. BMC Ophthalmology, Apr 2020. URL: https://doi.org/10.1186/s12886-020-01413-0, doi:10.1186/s12886-020-01413-0. This article has 8 citations and is from a peer-reviewed journal.

22. (vilimelis2015newgenesinvolved pages 95-96): J Crespí Vilimelis. New genes involved in rare diseases in ophthalmology. Unknown journal, 2015.

23. (kim2017familialretinalarteriolar pages 2-4): Tae Hee Kim, Sonia Lee, and Su Jin Lim. Familial retinal arteriolar tortuosity with acute hippocampal infarction. Case Reports in Ophthalmology, 8:185-189, Mar 2017. URL: https://doi.org/10.1159/000456069, doi:10.1159/000456069. This article has 5 citations and is from a peer-reviewed journal.

24. (bouchart2024clinicalreasoninga pages 3-5): Jean Bouchart, Sacha Weber, Thibault Coste, Marie-Alice Laville, Margaux Loisel, and Ahmad Nehme. Clinical reasoning: a 50-year-old man with intracerebral hemorrhage and tortuous retinal arterioles. Neurology, Sep 2024. URL: https://doi.org/10.1212/wnl.0000000000209796, doi:10.1212/wnl.0000000000209796. This article has 1 citations and is from a highest quality peer-reviewed journal.

25. (chen2020bilateralandmultiple pages 5-5): Ting Chen, Hongmei Zheng, Yunyun Wang, Junyi Hu, and Changzheng Chen. Bilateral and multiple sub-internal limiting membrane hemorrhages in a familial retinal arteriolar tortuosity patient by valsalva-like mechanism: an observational case report. BMC Ophthalmology, Apr 2020. URL: https://doi.org/10.1186/s12886-020-01413-0, doi:10.1186/s12886-020-01413-0. This article has 8 citations and is from a peer-reviewed journal.

26. (alavi2016col4a1mutationscause pages 7-8): Marcel V. Alavi, Mao Mao, Bradley T. Pawlikowski, Manana Kvezereli, Jacque L. Duncan, Richard T. Libby, Simon W. M. John, and Douglas B. Gould. Col4a1 mutations cause progressive retinal neovascular defects and retinopathy. Scientific Reports, Jan 2016. URL: https://doi.org/10.1038/srep18602, doi:10.1038/srep18602. This article has 58 citations and is from a peer-reviewed journal.

27. (alavi2016col4a1mutationscause pages 1-2): Marcel V. Alavi, Mao Mao, Bradley T. Pawlikowski, Manana Kvezereli, Jacque L. Duncan, Richard T. Libby, Simon W. M. John, and Douglas B. Gould. Col4a1 mutations cause progressive retinal neovascular defects and retinopathy. Scientific Reports, Jan 2016. URL: https://doi.org/10.1038/srep18602, doi:10.1038/srep18602. This article has 58 citations and is from a peer-reviewed journal.

28. (obayashi2021acaseseries pages 4-5): Tomohiro Obayashi, Aki Kato, Harumitsu Suzuki, Kei Ohashi, Munenori Yoshida, Yu Shibata, Yuichiro Ogura, and Tsutomu Yasukawa. A case series from a single family of familial retinal arteriolar tortuosity with common history of sudden visual loss. American Journal of Ophthalmology Case Reports, 24:101230, Dec 2021. URL: https://doi.org/10.1016/j.ajoc.2021.101230, doi:10.1016/j.ajoc.2021.101230. This article has 2 citations.

29. (obayashi2021acaseseries pages 1-2): Tomohiro Obayashi, Aki Kato, Harumitsu Suzuki, Kei Ohashi, Munenori Yoshida, Yu Shibata, Yuichiro Ogura, and Tsutomu Yasukawa. A case series from a single family of familial retinal arteriolar tortuosity with common history of sudden visual loss. American Journal of Ophthalmology Case Reports, 24:101230, Dec 2021. URL: https://doi.org/10.1016/j.ajoc.2021.101230, doi:10.1016/j.ajoc.2021.101230. This article has 2 citations.

30. (NCT07374913 chunk 1): Simona Balestrini. COL4A1COL4A2: Study of Pathological Conditions Involving Multiple Organs Caused by Mutations in the COL4A1 and COL4A2 Genes. Meyer Children's Hospital IRCCS. 2021. ClinicalTrials.gov Identifier: NCT07374913