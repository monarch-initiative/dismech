---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T07:43:45.839985'
end_time: '2026-05-05T07:58:58.696757'
duration_seconds: 912.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Polyarteritis Nodosa
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Polyarteritis Nodosa
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Primary Polyarteritis Nodosa** covering all of the
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
- **Disease Name:** Primary Polyarteritis Nodosa
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Primary Polyarteritis Nodosa** covering all of the
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


# Primary Polyarteritis Nodosa (Primary PAN): Comprehensive Disease Characteristics Report

## Executive summary (current understanding)
Primary polyarteritis nodosa (PAN) is a rare, systemic necrotizing vasculitis that predominantly targets medium-sized arteries and is classically distinguished from ANCA-associated vasculitis by *absence of glomerulonephritis* and typical *ANCA negativity*, with pathology showing *segmental, transmural necrotizing arteritis with fibrinoid necrosis and without granulomas*. (wolff2023polyarteritisnodosaold pages 1-2, chung20212021americancollegea pages 1-2, puechal2022polyarteritisnodosastate pages 1-2)

A major 2023–2024 development is the ongoing “re-framing” of what was historically called idiopathic PAN into (i) truly primary/idiopathic disease and (ii) PAN phenotypes driven by identifiable causes or mimics (e.g., HBV-associated PAN, monogenic ADA2 deficiency/DADA2, VEXAS), with important treatment implications (etiology-directed therapy rather than uniform immunosuppression). (wolff2023polyarteritisnodosaold pages 2-3, wolff2023polyarteritisnodosareviewed pages 8-9)


## Evidence map table
The following table consolidates key evidence items and quantitative data for rapid curation.

| Domain | Key points | Quantitative data | Key sources (with year, DOI/URL if known) |
|---|---|---|---|
| Identifiers / definitions | Primary polyarteritis nodosa (PAN) is a systemic necrotizing vasculitis of predominantly medium-sized arteries; diagnosis/classification emphasizes absence of glomerulonephritis, granulomas, and usually ANCA. CHCC 2012/overview definitions separate PAN from microscopic polyangiitis and other small-vessel vasculitides. ACR/VF 2021 guideline focuses on systemic, non-HBV PAN. | CHCC wording summarized as necrotizing inflammation of medium/small arteries without glomerulonephritis or vasculitis in arterioles, capillaries, venules; ACR/VF guideline issued 16 recommendations + 1 ungraded statement. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668; Jennette, 2013, https://doi.org/10.1007/s10157-013-0869-6; Chung et al., 2021, https://doi.org/10.1002/acr.24633 (wolff2023polyarteritisnodosaold pages 1-2, chung20212021americancollegea pages 1-2, hocevar2021clinicalapproachto pages 1-2) |
| Key distinguishing features | Distinguished from AAV/MPA by lack of pauci-immune glomerulonephritis and usual ANCA negativity; histology shows segmental, transmural necrotizing arteritis with fibrinoid necrosis and no granulomas; angiography may show aneurysms/stenoses of mesenteric, hepatic, and renal arteries. | ACR 1990 criteria require >=3/10 items for classification. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668; Hočevar et al., 2021, https://doi.org/10.1007/s11926-021-00983-2; Puéchal, 2022, https://doi.org/10.1016/j.jbspin.2021.105320 (wolff2023polyarteritisnodosaold pages 2-3, chung20212021americancollegea pages 1-2, hocevar2021clinicalapproachto pages 5-6, puechal2022polyarteritisnodosastate pages 1-2) |
| Epidemiology | PAN is rare in Europe and has become less common since reduction of HBV-related disease; contemporary idiopathic PAN is considered uncommon. Adult cohorts show middle age at onset and male predominance. | Prevalence in Europe about 2-31 per million; mean age ~51-54 years (one cohort 53.6 ± 18 years); male:female ratio ~1.5-1.7. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668; Walter et al., 2024, https://doi.org/10.1186/s12872-024-03841-y (wolff2023polyarteritisnodosaold pages 1-2, wolff2023polyarteritisnodosaold pages 2-3, walter2024shiftingperspectivesin pages 7-9) |
| Etiologies / associations: HBV | Historically a major cause; pathogenesis linked to HBsAg-containing immune complexes. Modern vaccination/public-health measures markedly reduced HBV-PAN frequency. HBV-associated PAN is treated differently from primary PAN. | Historical importance high; no current pooled rate given in extracted evidence. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668; Hočevar et al., 2021, https://doi.org/10.1007/s11926-021-00983-2; Puéchal, 2022, https://doi.org/10.1016/j.jbspin.2021.105320 (wolff2023polyarteritisnodosaold pages 2-3, wolff2023polyarteritisnodosareviewed pages 8-9, hocevar2021clinicalapproachto pages 1-2, puechal2022polyarteritisnodosastate pages 1-2) |
| Etiologies / associations: HCV, HIV, parvovirus B19 | HCV has been reported but is uncommon in PAN; HIV has occasional associations; parvovirus B19 has been investigated without convincing enrichment versus controls in one PCR-based study. | HCV association estimated at ~5% of PAN patients in reviewed evidence. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668 (wolff2023polyarteritisnodosaold pages 2-3) |
| Etiologies / associations: drugs / vaccines | Drug-induced PAN-like disease reported, including minocycline; post-COVID-19 vaccination PAN/cPAN-like cases have been reported, but causal inference remains limited. | No robust incidence estimate available in extracted evidence. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668 (wolff2023polyarteritisnodosaold pages 2-3) |
| Etiologies / associations: malignancy | PAN can occur as a paraneoplastic/associated vasculitis, especially with hematologic disease including myelodysplastic syndrome (MDS); this is important in “secondary” PAN differential diagnosis. | In one series of 70 patients with MDS and vasculitis, 9% had PAN. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668 (wolff2023polyarteritisnodosaold pages 2-3) |
| Etiologies / associations: DADA2 / ADA2 | Deficiency of ADA2 (CECR1/ADA2) is a key monogenic PAN mimic/cause, especially in early-onset disease; testing is important in childhood and young-adult PAN or unusual phenotypes. Anti-TNF therapy is favored in DADA2. | >300 cases reported since 2014; 4.3% of 118 adults with idiopathic PAN had biallelic ADA2 pathogenic variants; in DADA2, ~85% manifest before age 12, mucocutaneous involvement ~75%, livedo reticularis ~50%, neurologic involvement ~51%, ischemic stroke ~27%. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668; Hočevar et al., 2021, https://doi.org/10.1007/s11926-021-00983-2 (wolff2023polyarteritisnodosaold pages 1-2, wolff2023polyarteritisnodosaold pages 2-3, wolff2023polyarteritisnodosaold pages 7-8, hocevar2021clinicalapproachto pages 5-6, hocevar2021clinicalapproachto pages 1-2) |
| Etiologies / associations: VEXAS, FMF, SAVI | VEXAS (UBA1 somatic mutations), FMF-associated PAN, and SAVI/interferonopathy-related PAN-like disease broaden PAN nosology and are key differentials in “primary” PAN workup. | VEXAS inaugural cohort: 3/12 met PAN criteria; FMF-associated PAN prevalence ~0.9%. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668 (wolff2023polyarteritisnodosaold pages 2-3) |
| Clinical phenotypes | Heterogeneous multisystem disease with constitutional symptoms plus skin, peripheral nerve, GI, renal vascular, musculoskeletal, cardiac, CNS, and gonadal involvement. Orchitis/testicular pain is uncommon but relatively specific; coronary involvement may occur. | >90% systemic symptoms in meta-analysis; fever ~52%, myalgia ~53%, cutaneous involvement ~56%; muscle biopsy diagnostic in up to 50%; cutaneous and myalgia common among relapsers. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668; Taprantzis et al., 2026, https://doi.org/10.1007/s00296-026-06082-8; Walter et al., 2024, https://doi.org/10.1186/s12872-024-03841-y (wolff2023polyarteritisnodosaold pages 1-2, wolff2023polyarteritisnodosareviewed pages 7-8, taprantzis2026clinicalmanifestationsprognostic pages 1-2, walter2024shiftingperspectivesin pages 7-9) |
| Diagnostics: biopsy | Tissue biopsy is the diagnostic gold standard when feasible. Recommended targets are symptomatic tissues (deep skin/subcutis, muscle, sural nerve; combined nerve+muscle biopsy if neuropathy). Deep skin biopsy is preferred over superficial punch because medium-sized vessels lie deeper. | Histology: segmental necrotizing transmural inflammation with fibrinoid necrosis; muscle biopsy positive in up to 50% of cases. | Chung et al., 2021, https://doi.org/10.1002/acr.24633; Hočevar et al., 2021, https://doi.org/10.1007/s11926-021-00983-2; Wolff et al., 2023, https://doi.org/10.3390/ijms242316668 (chung20212021americancollegea pages 5-6, chung20212021americancollegea pages 1-2, hocevar2021clinicalapproachto pages 5-6, wolff2023polyarteritisnodosareviewed pages 7-8) |
| Diagnostics: angiography / imaging | Angiography is used when biopsy is not available or unsafe. Conventional angiography remains highest-resolution standard; CTA may better visualize distal mesenteric branches; MRA is an alternative when iodinated contrast is undesirable. Angiography can also define disease extent and detect aneurysms. | Typical findings: saccular/fusiform aneurysms and stenotic lesions in mesenteric, hepatic, renal arteries. | Chung et al., 2021, https://doi.org/10.1002/acr.24633; Hočevar et al., 2021, https://doi.org/10.1007/s11926-021-00983-2; Puéchal, 2022, https://doi.org/10.1016/j.jbspin.2021.105320 (chung20212021americancollegea pages 5-6, chung20212021americancollegea pages 1-2, hocevar2021clinicalapproachto pages 5-6, puechal2022polyarteritisnodosastate pages 1-2) |
| Diagnostics: labs / classification criteria | No specific serologic biomarker exists for primary PAN. ANCA is typically absent and its presence should prompt reconsideration of AAV/MPA. ACR 1990 criteria remain widely cited but were developed before MPA separation; EMA algorithm plus CHCC definition improves classification. | ACR 1990 sensitivity 82.2%, specificity 86.6%; later performance lower after MPA separation (sensitivity reportedly fell to 40.6% in re-evaluation). | Lin et al., 2021, https://doi.org/10.1002/acr2.11189; Hočevar et al., 2021, https://doi.org/10.1007/s11926-021-00983-2; Puéchal, 2022, https://doi.org/10.1016/j.jbspin.2021.105320; Walter et al., 2024, https://doi.org/10.1186/s12872-024-03841-y (lin2021polyarteritisnodosaa pages 1-2, hocevar2021clinicalapproachto pages 5-6, puechal2022polyarteritisnodosastate pages 2-3, walter2024shiftingperspectivesin pages 7-9) |
| Prognosis / Five-Factor Score | Prognosis is commonly stratified using the Five-Factor Score (FFS), which informs intensity of induction therapy. Poor-prognosis organ involvement drives morbidity and mortality. | FFS items: proteinuria >1 g/day, creatinine >140 µmol/L, cardiomyopathy, severe GI involvement, CNS involvement (1 point each). Meta-analysis: relapse ~27%, mortality ~13%, remission ~65%. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668; Taprantzis et al., 2026, https://doi.org/10.1007/s00296-026-06082-8 (wolff2023polyarteritisnodosareviewed pages 7-8, wolff2023polyarteritisnodosaold pages 7-8, taprantzis2026clinicalmanifestationsprognostic pages 1-2) |
| Treatment by severity: mild / FFS 0 | For newly diagnosed nonsevere PAN, glucocorticoids are often effective, but guidelines and reviews increasingly favor adding a nonglucocorticoid immunosuppressant (AZA or MTX) to reduce relapse/steroid exposure. | GC monotherapy associated with relapse concern; review cites ~40% relapse rate for mild PAN treated with GC alone. ACR/VF suggests AZA 2-3 mg/kg/day or MTX 0.3 mg/kg/week as options. | Chung et al., 2021, https://doi.org/10.1002/acr.24633; Wolff et al., 2023, https://doi.org/10.3390/ijms242316668 (chung20212021americancollegea pages 5-6, wolff2023polyarteritisnodosareviewed pages 7-8, wolff2023polyarteritisnodosaold pages 7-8) |
| Treatment by severity: severe / FFS >0 | Severe or organ-/life-threatening PAN is treated with pulse IV glucocorticoids or high-dose oral glucocorticoids plus cyclophosphamide; rituximab is not preferred first-line because evidence is sparse. If cyclophosphamide cannot be used, AZA/MTX may be combined with glucocorticoids rather than GC alone. | Induction typically 3-6 months; prednisone about 1 mg/kg/day (max 60 mg/day); cyclophosphamide usually limited to <=6 months. One cited comparison found 12 monthly cyclophosphamide doses superior to a shorter 6-dose strategy for survival (HR 0.44) and sustained remission (HR 0.34) at 32 months. | Chung et al., 2021, https://doi.org/10.1002/acr.24633; Walter et al., 2024, https://doi.org/10.1186/s12872-024-03841-y; Wolff et al., 2023, https://doi.org/10.3390/ijms242316668 (chung20212021americancollegea pages 5-6, walter2024shiftingperspectivesin pages 7-9, wolff2023polyarteritisnodosareviewed pages 7-8, wolff2023polyarteritisnodosaold pages 7-8) |
| Maintenance therapy | After remission induction, cyclophosphamide should be transitioned to a less toxic maintenance agent such as azathioprine or methotrexate; maintenance generally continues 12-18 months, with some guidance allowing discontinuation after ~18 months of sustained remission. | Maintenance duration commonly 12-18 months; French recommendations for systemic necrotizing vasculitides describe maintenance 12-48 months depending on context. | Chung et al., 2021, https://doi.org/10.1002/acr.24633; Terrier et al., 2020, https://doi.org/10.1186/s13023-020-01621-3; Wolff et al., 2023, https://doi.org/10.3390/ijms242316668 (chung20212021americancollegea pages 5-6, wolff2023polyarteritisnodosareviewed pages 8-9, wolff2023polyarteritisnodosaold pages 7-8) |
| Refractory / relapsing disease | Biologics are reserved for refractory/relapsing PAN or specific molecular subtypes. Evidence is limited to retrospective cohorts and case reports; etiology-directed therapy is increasingly emphasized (anti-TNF for DADA2; JAK inhibition/tocilizumab in selected VEXAS; disease-specific therapy for malignancy-associated PAN). | European retrospective series complete remission: tocilizumab 50%, TNF inhibitors 40%, rituximab 33%. | Wolff et al., 2023, https://doi.org/10.3390/ijms242316668 (wolff2023polyarteritisnodosareviewed pages 7-8, wolff2023polyarteritisnodosareviewed pages 8-9, wolff2023polyarteritisnodosaold pages 7-8) |
| HBV-PAN treatment | HBV-associated PAN is managed differently from primary PAN: antiviral therapy is central, with short-course glucocorticoids and plasma exchange used in severe disease. Classic older trial data did not show benefit of plasma exchange added to steroids alone in non-HBV PAN/CSS, underscoring etiology-specific use. | Older randomized trial in PAN/CSS: no superiority of steroids + plasma exchange over steroids alone; HBV-PAN recommendations are based largely on uncontrolled studies/guidelines rather than modern RCTs. | Guillevin et al., 1992, https://doi.org/10.1002/art.1780350214; Hočevar et al., 2021, https://doi.org/10.1007/s11926-021-00983-2; Puéchal, 2022, https://doi.org/10.1016/j.jbspin.2021.105320 (hocevar2021clinicalapproachto pages 1-2, puechal2022polyarteritisnodosastate pages 1-2) |


*Table: This table consolidates core disease-characteristic evidence for primary polyarteritis nodosa, including definition, epidemiology, etiologic associations, phenotypes, diagnostic criteria, prognosis, and treatment. It is designed as a compact evidence map for knowledge-base curation and report drafting.*


## 1. Disease information

### 1.1 What is the disease?
**Definition (CHCC concept and modern reviews):** PAN is defined as necrotizing inflammation of medium-sized (and sometimes small muscular) arteries, *without* glomerulonephritis and *without* vasculitis of arterioles/capillaries/venules. (puechal2022polyarteritisnodosastate pages 1-2)

**Guideline clinical framing (ACR/Vasculitis Foundation 2021):** PAN is a systemic necrotizing vasculitis of medium-sized vessels; typical clinical patterns include constitutional symptoms plus cutaneous, neurologic (peripheral neuropathy/mononeuritis multiplex), gastrointestinal, and renovascular manifestations; diagnosis is generally confirmed by biopsy of an affected organ or by angiography when biopsy cannot be obtained. (chung20212021americancollegea pages 1-2)

### 1.2 Key identifiers (ontology/coding)
**ICD-10:** Polyarteritis nodosa is commonly coded as **M30.0** (standard clinical coding; not directly extracted from retrieved texts).

**MeSH / MONDO / Orphanet:** A specific MONDO ID and ORPHAcode for “primary/idiopathic systemic PAN” were **not retrievable from the tool-accessible corpus** in this run; knowledge base ingestion should pull these directly from MONDO and Orphanet inventories. (Evidence gap; see “Limitations”.)

### 1.3 Common synonyms / alternative names
- **Polyarteritis nodosa (PAN)**
- **Panarteritis nodosa** (wolff2023polyarteritisnodosaold pages 1-2)
- “Classic” or “systemic” PAN are used variably in clinical literature to separate from cutaneous arteritis/cutaneous PAN. (hocevar2021clinicalapproachto pages 1-2)

### 1.4 Source types (patient-level vs aggregated)
Current understanding is derived from a mixture of (i) cohort/registry experience and guideline syntheses (ACR/VF 2021; French recommendations), (ii) older randomized trials in systemic necrotizing vasculitides, (iii) observational studies and case series in refractory disease, and (iv) increasingly, *genotype-first* studies that identify monogenic causes/mimics in “idiopathic” cohorts. (chung20212021americancollegea pages 5-6, wolff2023polyarteritisnodosaold pages 2-3)


## 2. Etiology

### 2.1 Disease causal factors (primary vs secondary)
**Primary (idiopathic) PAN** is diagnosed after excluding secondary causes (notably HBV) and important mimics/phenocopies (e.g., DADA2/ADA2 deficiency; VEXAS). Modern reviews emphasize that PAN is now better viewed as a spectrum where identifying an underlying driver changes management. (wolff2023polyarteritisnodosaold pages 2-3, wolff2023polyarteritisnodosareviewed pages 8-9)

### 2.2 Risk factors and associated conditions

#### Infectious associations
- **HBV:** Historically a major cause; pathogenesis linked to immune complexes containing hepatitis B surface antigen; the association has decreased markedly in many settings with improved HBV control. (wolff2023polyarteritisnodosaold pages 2-3, wolff2023polyarteritisnodosaold pages 1-2)
- **HCV:** In a 2023 review, HCV association is stated to concern **~5%** of patients with PAN. (wolff2023polyarteritisnodosaold pages 2-3)
- **HIV:** Reported association (rare; largely case-based). (wolff2023polyarteritisnodosaold pages 2-3)
- **Parvovirus B19:** Investigated; one PCR-based analysis found no higher parvovirus prevalence in PAN than controls (supporting uncertainty for causality). (wolff2023polyarteritisnodosaold pages 2-3)

#### Drug-/vaccine-associated reports
Drug-induced PAN-like cases (e.g., **minocycline**) and post–COVID-19 vaccination temporal associations have been reported, but population-level causality is not established in the extracted evidence. (wolff2023polyarteritisnodosaold pages 2-3)

#### Malignancy associations
PAN may occur in association with hematologic malignancy, including myelodysplastic syndrome (MDS); in one referenced series, among **70** patients with MDS and vasculitis, **9%** presented with PAN. (wolff2023polyarteritisnodosaold pages 2-3)

#### Genetic/monogenic causes and mimics (high priority in “primary PAN” workup)
- **ADA2 deficiency (DADA2; gene: ADA2/CECR1):** Since 2014, >300 DADA2 cases with PAN-like vasculitis have been reported. (wolff2023polyarteritisnodosaold pages 1-2)
  - In a study of **118** adults with “idiopathic adult PAN,” **4.3%** had biallelic pathogenic ADA2 variants, implying clinically meaningful reclassification potential. (wolff2023polyarteritisnodosaold pages 2-3)
- **VEXAS (UBA1 somatic variants):** In an early cohort, **3/12** met criteria for PAN, illustrating diagnostic overlap. (wolff2023polyarteritisnodosaold pages 2-3)
- **Familial Mediterranean fever (FMF; MEFV):** PAN prevalence reported at **0.9%** in FMF in a referenced study. (wolff2023polyarteritisnodosaold pages 2-3)
- **Interferonopathies (e.g., SAVI):** Reported as part of expanding etiologic spectrum. (wolff2023polyarteritisnodosaold pages 2-3)

### 2.3 Protective factors
No robust protective genetic or environmental factors were identified in the tool-accessible evidence.

### 2.4 Gene–environment interactions
Not specifically established in the retrieved evidence; a plausible interaction is genetic predisposition (e.g., ADA2 deficiency) plus infectious triggers, but this remains incompletely defined here. (wolff2023polyarteritisnodosaold pages 2-3)


## 3. Phenotypes (clinical features)

### 3.1 Core phenotype domains (with suggested HPO terms)
PAN can involve virtually any organ, with preferential involvement of skin, peripheral nervous system, and GI tract in many series/reviews. (wolff2023polyarteritisnodosaold pages 1-2)

**Constitutional/systemic**
- Fever, asthenia/fatigue, weight loss (e.g., **HP:0001945** Fever; **HP:0001254** Lethargy/fatigue; **HP:0001824** Weight loss). (wolff2023polyarteritisnodosaold pages 1-2, taprantzis2026clinicalmanifestationsprognostic pages 1-2)

**Cutaneous**
- Livedo reticularis/racemosa (**HP:0000973**), subcutaneous nodules (**HP:0001480**), skin ulcers (**HP:0001053**), palpable purpura (**HP:0000964**). (chung20212021americancollegea pages 1-2, taprantzis2026clinicalmanifestationsprognostic pages 1-2)

**Peripheral nervous system**
- Peripheral neuropathy and mononeuritis multiplex (**HP:0009830** Peripheral neuropathy; **HP:0001305** Mononeuritis multiplex). (chung20212021americancollegea pages 1-2, taprantzis2026clinicalmanifestationsprognostic pages 1-2)

**Gastrointestinal/mesenteric ischemia**
- Abdominal pain (**HP:0002027**), bowel ischemia/perforation/bleeding (**HP:0031944** Intestinal ischemia; **HP:0004395** Gastrointestinal hemorrhage). (taprantzis2026clinicalmanifestationsprognostic pages 1-2)

**Renovascular**
- Hypertension (**HP:0000822**), renal artery stenosis/aneurysm with hematuria/proteinuria (**HP:0000790** Hematuria; **HP:0000093** Proteinuria). (taprantzis2026clinicalmanifestationsprognostic pages 1-2)

**Musculoskeletal**
- Myalgia (**HP:0003326**), arthralgia (**HP:0002829**). (taprantzis2026clinicalmanifestationsprognostic pages 1-2)

**Cardiac**
- Coronary arteritis/stenosis/aneurysm leading to myocardial ischemia or heart failure (e.g., **HP:0001658** Myocardial infarction; **HP:0001635** Congestive heart failure). (wolff2023polyarteritisnodosaold pages 1-2, walter2024shiftingperspectivesin pages 7-9)

**Genitourinary**
- Orchitis/testicular pain (**HP:0000035** Orchitis; **HP:0030547** Testicular pain). Orchitis is described as rare but relatively specific for PAN. (wolff2023polyarteritisnodosaold pages 1-2, wolff2023polyarteritisnodosareviewed pages 7-8)

### 3.2 Frequency/statistics from recent syntheses
A 2026 systematic review/meta-analysis (not within 2023–2024 but recent and quantitative) reported: fever ~**52%**, myalgia ~**53%**, cutaneous involvement ~**56%**, relapse ~**27%**, mortality ~**13%**, remission ~**65%**, and >90% with systemic manifestations. (taprantzis2026clinicalmanifestationsprognostic pages 1-2)

### 3.3 Quality-of-life impact
Direct validated QoL instruments (SF-36/EQ-5D) were not extractable from the retrieved texts; however, PAN is consistently framed as potentially disabling due to neuropathy, ischemic complications, and treatment toxicity. (chung20212021americancollegea pages 1-2)


## 4. Genetic/molecular information

### 4.1 Causal genes
**Primary/idiopathic PAN** is generally not monogenic, but a major modern development is recognition that a subset of cases labeled “idiopathic PAN” actually reflect **monogenic vasculitis/vasculopathy**, especially **ADA2 (CECR1/ADA2)** deficiency. (wolff2023polyarteritisnodosaold pages 2-3)

### 4.2 Pathogenic variants and molecular testing implications
- **ADA2 (CECR1/ADA2) biallelic pathogenic variants**: detected in **4.3%** of a 118-patient idiopathic adult PAN cohort; this supports routine consideration of ADA2 testing in early-onset/atypical or familial PAN-like disease. (wolff2023polyarteritisnodosaold pages 2-3)

**Suggested molecular diagnostic actions (MAXO-style actions, illustrative):**
- ADA2 enzyme activity assay (MAXO:0000115 “enzyme activity measurement”)
- CECR1/ADA2 sequencing (MAXO:0000127 “gene sequencing”) (hocevar2021clinicalapproachto pages 5-6)

### 4.3 Epigenetics / omics
No PAN-specific epigenetic or multi-omics profiling signatures were identified in the retrieved evidence.


## 5. Environmental information
No robust toxin/pollution/occupational exposures were identified. The dominant “environmental” component supported here is infectious association (HBV; occasional HCV/HIV reports). (wolff2023polyarteritisnodosaold pages 2-3)


## 6. Mechanism / pathophysiology

### 6.1 Core vascular lesion and inflammatory biology
Histopathology features emphasized in modern reviews include segmental, necrotizing, transmural arteritis with fibrinoid necrosis, microaneurysms, and mixed inflammatory infiltrates, typically without granulomas. (wolff2023polyarteritisnodosaold pages 2-3, chung20212021americancollegea pages 1-2)

Cytokine elevations and immune cell infiltrates reported in a 2023 review include IFN-α, IL-2, TNFα, and IL-1β, with macrophage and T-cell involvement in lesions. (wolff2023polyarteritisnodosaold pages 2-3)

### 6.2 Causal chain (generalized)
Upstream trigger (often unknown in primary PAN; or immune complexes in HBV-PAN; or intrinsic immune dysregulation in monogenic phenocopies) → medium-artery wall inflammation and fibrinoid necrosis → stenosis, thrombosis, aneurysm formation → tissue ischemia/hemorrhage in affected vascular territories → organ-specific manifestations (neuropathy, GI ischemia, renal ischemia/hypertension, skin ulcers/nodules, coronary events). (chung20212021americancollegea pages 1-2, wolff2023polyarteritisnodosaold pages 1-2)

### 6.3 Ontology suggestions
**GO biological process (suggested):**
- GO:0006954 inflammatory response
- GO:0002682 regulation of immune system process
- GO:0001525 angiogenesis (aneurysm/repair context)
- GO:0007596 blood coagulation (thrombosis complications)

**Cell Ontology (CL) (suggested):**
- Macrophage (CL:0000235)
- T cell (CL:0000084)
- Endothelial cell (CL:0000115)
- Vascular smooth muscle cell (CL:0000192)

**UBERON anatomy (suggested):**
- Medium-sized artery / muscular artery (e.g., UBERON:0001637 artery; more specific vessel terms should be selected per organ)
- Mesenteric artery, renal artery, hepatic artery

(These ontology mappings are proposed based on described biology; no ontology IDs were explicitly enumerated in the retrieved texts.)


## 7. Anatomical structures affected
**Primary:** medium-sized arteries, especially visceral arterial branches (mesenteric, hepatic, renal) with aneurysms/stenoses; skin and peripheral nerve involvement are common. (chung20212021americancollegea pages 1-2, wolff2023polyarteritisnodosaold pages 1-2)

**Secondary/complications:** mesenteric infarction/hemorrhage, cardiac ischemia, cerebrovascular events, renal ischemia/hypertension. (wolff2023polyarteritisnodosaold pages 1-2, walter2024shiftingperspectivesin pages 7-9)


## 8. Temporal development
Typical presentation is adult-onset in many cohorts (mean ~early 50s) with male predominance, though monogenic mimics (DADA2) often present in childhood. (wolff2023polyarteritisnodosaold pages 1-2, wolff2023polyarteritisnodosaold pages 7-8)

Disease course may be relapsing, with relapse estimates around ~27% in pooled data. (taprantzis2026clinicalmanifestationsprognostic pages 1-2)


## 9. Inheritance and population

### 9.1 Epidemiology
Reported European prevalence range in modern reviews is **~2–31 per million**. (wolff2023polyarteritisnodosaold pages 1-2)

Demographics in a contemporary cohort cited in a 2023 review: mean age **53.6 ± 18 years**, male predominance with sex ratio **~1.5**. (wolff2023polyarteritisnodosaold pages 2-3)

### 9.2 Genetic etiologies and inheritance (for mimics)
- **DADA2 (ADA2/CECR1):** autosomal recessive (biallelic pathogenic variants), often pediatric onset with mucocutaneous and neurologic features. (wolff2023polyarteritisnodosaold pages 7-8)
- **VEXAS (UBA1):** somatic, X-linked gene in hematopoietic lineages; late-onset inflammatory syndrome that can meet PAN criteria. (wolff2023polyarteritisnodosaold pages 2-3)


## 10. Diagnostics

### 10.1 Clinical criteria/classification
**ACR 1990 PAN classification criteria:** ≥3 of 10 items yields sensitivity **82.2%** and specificity **86.6%** for classification; limitations recognized because criteria predate separation of microscopic polyangiitis. (walter2024shiftingperspectivesin pages 7-9, puechal2022polyarteritisnodosastate pages 2-3)

**CHCC definition (quoted in a 2022 state-of-the-art review):** “Necrotising inflammation of medium-sized or small arteries without glomerulonephritis or vasculitis in arterioles, capillaries, or venules.” (puechal2022polyarteritisnodosastate pages 1-2)

### 10.2 Laboratory testing
There is no specific serologic biomarker for primary PAN; ANCA negativity supports PAN classification, and ANCA positivity should raise suspicion for AAV/MPA rather than PAN. (lin2021polyarteritisnodosaa pages 1-2, puechal2022polyarteritisnodosastate pages 1-2)

### 10.3 Imaging
Angiography may show saccular/fusiform aneurysms and stenoses in mesenteric/hepatic/renal arteries. Conventional angiography remains highest resolution; CTA and MRA are useful alternatives in specific contexts. (chung20212021americancollegea pages 5-6, chung20212021americancollegea pages 1-2)

### 10.4 Biopsy
Biopsy remains the diagnostic gold standard when feasible; deep skin biopsy is recommended over superficial punch when evaluating cutaneous disease, and combined nerve+muscle biopsy is recommended over nerve alone for suspected vasculitic neuropathy. (chung20212021americancollegea pages 5-6)

### 10.5 Differential diagnosis (high-yield)
- ANCA-associated vasculitides (MPA/GPA/EGPA)
- Cryoglobulinemic vasculitis
- DADA2 (ADA2 deficiency)
- VEXAS syndrome
- Malignancy-associated vasculitis (esp. MDS)
- Infection-associated vasculitis (HBV) (wolff2023polyarteritisnodosaold pages 2-3, puechal2022polyarteritisnodosastate pages 1-2)

### 10.6 Visual evidence (table/algorithm)
A treatment algorithm and classification/criteria table are shown in Puéchal (2022), including ACR criteria, CHCC definition, and the EMA classification approach, plus a clinical treatment flowchart stratified by subtype and severity. (puechal2022polyarteritisnodosastate media 85b1bd4a, puechal2022polyarteritisnodosastate media 858e4031)


## 11. Outcome / prognosis

### 11.1 Prognostic factors
The **Five-Factor Score (FFS)** assigns 1 point each for **proteinuria >1 g/day**, **creatinine >140 µmol/L**, **cardiomyopathy**, **severe GI involvement**, and **CNS involvement** to stratify risk and guide treatment intensity. (wolff2023polyarteritisnodosareviewed pages 7-8)

### 11.2 Relapse, remission, mortality (recent quantitative synthesis)
A recent meta-analysis estimated **relapse ~27%**, **mortality ~13%**, and **remission ~65%** across included PAN studies (heterogeneous definitions and eras). (taprantzis2026clinicalmanifestationsprognostic pages 1-2)


## 12. Treatment (current practice + evidence)

### 12.1 First-line treatment (primary non-HBV PAN)
**ACR/VF 2021 guideline (real-world implementation in rheumatology practice):**
- **Severe PAN:** cyclophosphamide + glucocorticoids preferred over glucocorticoids alone and over rituximab + glucocorticoids; IV pulse glucocorticoids are conditionally preferred over high-dose oral glucocorticoids for newly diagnosed severe disease. (chung20212021americancollegea pages 5-6)
- **Nonsevere PAN:** glucocorticoids plus a non-glucocorticoid immunosuppressant (e.g., azathioprine or methotrexate) are conditionally preferred over glucocorticoids alone. (chung20212021americancollegea pages 5-6, walter2024shiftingperspectivesin pages 7-9)

**Dose/duration patterns reported in a 2023 review:** induction for moderate–severe PAN commonly uses prednisone ~1 mg/kg/day (max 60 mg/day) and cyclophosphamide for ~3–6 months, with cyclophosphamide generally limited to ≤6 months, followed by maintenance azathioprine or methotrexate for ~12–18 months. (wolff2023polyarteritisnodosareviewed pages 7-8)

### 12.2 Evidence and statistics
- A referenced comparison in PAN reported that **12 monthly cyclophosphamide doses + glucocorticoids** were superior to a shorter strategy for survival (HR **0.44**, p=0.02) and sustained remission (HR **0.34**, p=0.02) at 32 months. (walter2024shiftingperspectivesin pages 7-9)
- For “mild” PAN (FFS=0), relapse risk with glucocorticoids alone is highlighted as high (reported **~40% relapse rate** in a 2023 review), motivating steroid-sparing strategies. (wolff2023polyarteritisnodosareviewed pages 7-8)

### 12.3 Refractory/relapsing PAN and biologics
Evidence remains limited (mostly retrospective cohorts/case series). A European retrospective series cited in a 2023 review reported complete remission rates of **50%** (tocilizumab), **40%** (TNF inhibitors), and **33%** (rituximab) in relapsing/refractory PAN. (wolff2023polyarteritisnodosareviewed pages 7-8)

### 12.4 Etiology-directed therapy
- **HBV-associated PAN:** requires antiviral therapy; a 2021 review states HBV-PAN “primarily requires antiviral therapy combined with plasma exchange.” (hocevar2021clinicalapproachto pages 1-2)
- **DADA2:** anti-TNF therapy is a key targeted approach (not primary idiopathic PAN). (lin2021polyarteritisnodosaa pages 1-2)
- **VEXAS/MDS-associated cases:** may require hematology-directed therapy; immunosuppression alone may be insufficient. (wolff2023polyarteritisnodosaold pages 8-9)

### 12.5 Clinical trials / trials infrastructure (ClinicalTrials.gov)
- **Biomarker/natural history:** NCT00315406 (completed; observational; n=107) collected blood/urine/DNA longitudinally to identify disease activity biomarkers and excluded ANCA-positive disease, glomerulonephritis, HBV/HCV/HIV, and isolated cutaneous PAN—reflecting operational criteria for “primary systemic PAN” research cohorts. (NCT00315406 chunk 1)
- **Steroid-sparing trial in systemic necrotizing vasculitides (FFS=0):** NCT00647166 (CHUSPAN-2; completed; n=114) randomized adults with newly diagnosed PAN/MPA/EGPA without poor-prognosis factors to glucocorticoids plus azathioprine vs placebo; primary outcome was combined remission failures and relapses at 24 months; linked publication **PMID: 28678392**. (NCT00647166 chunk 1, NCT00647166 chunk 2)

**MAXO suggestions (treatments/actions; illustrative):**
- Glucocorticoid therapy (MAXO:0000747)
- Cyclophosphamide therapy (MAXO:0001024)
- Azathioprine therapy (MAXO:0000724)
- Methotrexate therapy (MAXO:0001008)
- Plasma exchange (MAXO:0000411)


## 13. Prevention
Primary prevention of idiopathic PAN is not established. For secondary PAN risk reduction, HBV vaccination and HBV control plausibly reduce HBV-associated PAN burden; this is consistent with the reported historical decline in HBV-PAN. (lin2021polyarteritisnodosaa pages 1-2)


## 14. Other species / natural disease
No naturally occurring PAN analogs in other species were identified in the retrieved evidence.


## 15. Model organisms
No validated animal models were identified in the retrieved evidence set.


## Recent developments (2023–2024 priority highlights)
1. **Nosology shift (“old disease, new etiologies”):** 2023 reviews emphasize declining HBV-driven PAN and increasing recognition of genetic syndromes (ADA2 deficiency) and hematologic/inflammatory syndromes (VEXAS) that can meet PAN criteria, making etiology workup central to management. (wolff2023polyarteritisnodosaold pages 2-3)
2. **Refractory treatment landscape:** 2023 synthesis notes off-label biologic use (tocilizumab, TNF inhibitors, rituximab) with modest complete remission rates in retrospective data, reflecting the need for better trials in non-ANCA medium-vessel vasculitis. (wolff2023polyarteritisnodosareviewed pages 7-8)
3. **Coronary involvement awareness:** 2024 review emphasizes coronary artery disease can occur in PAN and may require combined immunosuppression plus revascularization approaches in selected cases. (walter2024shiftingperspectivesin pages 7-9)


## Limitations / evidence gaps for knowledge base completion
- **Ontology identifiers (MONDO, ORPHAcode, MeSH unique ID)** were not extractable from the retrieved papers in this run; these should be pulled directly from MONDO/Orphanet/MeSH resources.
- Some key quantitative epidemiology/outcome estimates for *primary* (non-HBV, non-monogenic) PAN are limited by heterogeneity, older cohorts, and inclusion of secondary/monogenic cases in aggregate analyses.
- Several statements about HBV-PAN treatment rely on reviews and uncontrolled study traditions; high-quality modern RCT evidence specific to HBV-PAN is limited in the extracted corpus.


## Key sources (URLs and publication dates)
- Wolff L, et al. *Polyarteritis Nodosa: Old Disease, New Etiologies.* Int J Mol Sci. **2023-11**. https://doi.org/10.3390/ijms242316668 (wolff2023polyarteritisnodosaold pages 2-3)
- Chung SA, et al. *2021 ACR/VF Guideline for the Management of Polyarteritis Nodosa.* Arthritis Care Res. **2021-07**. https://doi.org/10.1002/acr.24633 (chung20212021americancollegea pages 1-2)
- Puéchal X. *Polyarteritis Nodosa: State of the art.* Joint Bone Spine. **2022-07**. https://doi.org/10.1016/j.jbspin.2021.105320 (puechal2022polyarteritisnodosastate pages 1-2)
- Hočevar A, et al. *Clinical Approach to Diagnosis and Therapy of Polyarteritis Nodosa.* Curr Rheumatol Rep. **2021-02**. https://doi.org/10.1007/s11926-021-00983-2 (hocevar2021clinicalapproachto pages 5-6)
- Walter DJ, et al. *Shifting perspectives in coronary involvement of PAN.* BMC Cardiovasc Disord. **2024-04**. https://doi.org/10.1186/s12872-024-03841-y (walter2024shiftingperspectivesin pages 7-9)
- ClinicalTrials.gov NCT00315406 (Merkel P). **2006; completed 2019**. https://clinicaltrials.gov/study/NCT00315406 (NCT00315406 chunk 1)
- ClinicalTrials.gov NCT00647166 (CHUSPAN-2). **2008; completed**; linked publication **PMID: 28678392**. https://clinicaltrials.gov/study/NCT00647166 (NCT00647166 chunk 1)


References

1. (wolff2023polyarteritisnodosaold pages 1-2): Louis Wolff, Alice Horisberger, Laura Moi, Maria P. Karampetsou, and Denis Comte. Polyarteritis nodosa: old disease, new etiologies. International Journal of Molecular Sciences, 24:16668, Nov 2023. URL: https://doi.org/10.3390/ijms242316668, doi:10.3390/ijms242316668. This article has 50 citations.

2. (chung20212021americancollegea pages 1-2): Sharon A. Chung, Mark Gorelik, Carol A. Langford, Mehrdad Maz, Andy Abril, Gordon Guyatt, Amy M. Archer, Doyt L. Conn, Kathy A. Full, Peter C. Grayson, Maria F. Ibarra, Lisa F. Imundo, Susan Kim, Peter A. Merkel, Rennie L. Rhee, Philip Seo, John H. Stone, Sangeeta Sule, Robert P. Sundel, Omar I. Vitobaldi, Ann Warner, Kevin Byram, Anisha B. Dua, Nedaa Husainat, Karen E. James, Mohamad Kalot, Yih Chang Lin, Jason M. Springer, Marat Turgunbaev, Alexandra Villa‐Forte, Amy S. Turner, and Reem A. Mustafa. 2021 american college of rheumatology/vasculitis foundation guideline for the management of polyarteritis nodosa. Arthritis Care & Research, 73:1061-1070, Jul 2021. URL: https://doi.org/10.1002/acr.24633, doi:10.1002/acr.24633. This article has 137 citations and is from a domain leading peer-reviewed journal.

3. (puechal2022polyarteritisnodosastate pages 1-2): Xavier Puéchal. Polyarteritis nodosa: state of the art. Joint Bone Spine, 89:105320, Jul 2022. URL: https://doi.org/10.1016/j.jbspin.2021.105320, doi:10.1016/j.jbspin.2021.105320. This article has 16 citations and is from a peer-reviewed journal.

4. (wolff2023polyarteritisnodosaold pages 2-3): Louis Wolff, Alice Horisberger, Laura Moi, Maria P. Karampetsou, and Denis Comte. Polyarteritis nodosa: old disease, new etiologies. International Journal of Molecular Sciences, 24:16668, Nov 2023. URL: https://doi.org/10.3390/ijms242316668, doi:10.3390/ijms242316668. This article has 50 citations.

5. (wolff2023polyarteritisnodosareviewed pages 8-9): Louis Wolff, Alice Horisberger, Laura Moi, Maria P. Karampetsou, and Denis Comte. Polyarteritis nodosa reviewed in 2023: old disease, new etiologies. Oct 2023. URL: https://doi.org/10.20944/preprints202310.0949.v1, doi:10.20944/preprints202310.0949.v1.

6. (hocevar2021clinicalapproachto pages 1-2): Alojzija Hočevar, Matija Tomšič, and Katja Perdan Pirkmajer. Clinical approach to diagnosis and therapy of polyarteritis nodosa. Current Rheumatology Reports, Feb 2021. URL: https://doi.org/10.1007/s11926-021-00983-2, doi:10.1007/s11926-021-00983-2. This article has 58 citations and is from a peer-reviewed journal.

7. (hocevar2021clinicalapproachto pages 5-6): Alojzija Hočevar, Matija Tomšič, and Katja Perdan Pirkmajer. Clinical approach to diagnosis and therapy of polyarteritis nodosa. Current Rheumatology Reports, Feb 2021. URL: https://doi.org/10.1007/s11926-021-00983-2, doi:10.1007/s11926-021-00983-2. This article has 58 citations and is from a peer-reviewed journal.

8. (walter2024shiftingperspectivesin pages 7-9): Dylan J. Walter, Grace E. Bigham, Steven Lahti, and Syed W. Haider. Shifting perspectives in coronary involvement of polyarteritis nodosa: case of 3-vessel occlusion treated with 4-vessel cabg and review of literature. BMC Cardiovascular Disorders, Apr 2024. URL: https://doi.org/10.1186/s12872-024-03841-y, doi:10.1186/s12872-024-03841-y. This article has 3 citations and is from a peer-reviewed journal.

9. (wolff2023polyarteritisnodosaold pages 7-8): Louis Wolff, Alice Horisberger, Laura Moi, Maria P. Karampetsou, and Denis Comte. Polyarteritis nodosa: old disease, new etiologies. International Journal of Molecular Sciences, 24:16668, Nov 2023. URL: https://doi.org/10.3390/ijms242316668, doi:10.3390/ijms242316668. This article has 50 citations.

10. (wolff2023polyarteritisnodosareviewed pages 7-8): Louis Wolff, Alice Horisberger, Laura Moi, Maria P. Karampetsou, and Denis Comte. Polyarteritis nodosa reviewed in 2023: old disease, new etiologies. Oct 2023. URL: https://doi.org/10.20944/preprints202310.0949.v1, doi:10.20944/preprints202310.0949.v1.

11. (taprantzis2026clinicalmanifestationsprognostic pages 1-2): Nikolaos Taprantzis, Maria Eleni Kasimeri, Dimosthenis Chrysikos, Amir Shihada, Alexandros Samolis, George Tsakotos, Martina Liga, and Theodore Troupis. Clinical manifestations, prognostic impact, and relapse in polyarteritis nodosa: a systematic review and meta-analysis. Rheumatology International, Feb 2026. URL: https://doi.org/10.1007/s00296-026-06082-8, doi:10.1007/s00296-026-06082-8. This article has 0 citations and is from a peer-reviewed journal.

12. (chung20212021americancollegea pages 5-6): Sharon A. Chung, Mark Gorelik, Carol A. Langford, Mehrdad Maz, Andy Abril, Gordon Guyatt, Amy M. Archer, Doyt L. Conn, Kathy A. Full, Peter C. Grayson, Maria F. Ibarra, Lisa F. Imundo, Susan Kim, Peter A. Merkel, Rennie L. Rhee, Philip Seo, John H. Stone, Sangeeta Sule, Robert P. Sundel, Omar I. Vitobaldi, Ann Warner, Kevin Byram, Anisha B. Dua, Nedaa Husainat, Karen E. James, Mohamad Kalot, Yih Chang Lin, Jason M. Springer, Marat Turgunbaev, Alexandra Villa‐Forte, Amy S. Turner, and Reem A. Mustafa. 2021 american college of rheumatology/vasculitis foundation guideline for the management of polyarteritis nodosa. Arthritis Care & Research, 73:1061-1070, Jul 2021. URL: https://doi.org/10.1002/acr.24633, doi:10.1002/acr.24633. This article has 137 citations and is from a domain leading peer-reviewed journal.

13. (lin2021polyarteritisnodosaa pages 1-2): Yih Chang Lin, Mohamad A. Kalot, Nedaa M. Husainat, Kevin Byram, Anisha B. Dua, Karen E. James, Jason M. Springer, Marat Turgunbaev, Alexandra Villa‐Forte, Andy Abril, Carol Langford, Mehrdad Maz, Sharon A. Chung, and Reem A. Mustafa. Polyarteritis nodosa: a systematic review of test accuracy and benefits and harms of common treatments. ACR Open Rheumatology, 3:91-100, Jan 2021. URL: https://doi.org/10.1002/acr2.11189, doi:10.1002/acr2.11189. This article has 14 citations and is from a peer-reviewed journal.

14. (puechal2022polyarteritisnodosastate pages 2-3): Xavier Puéchal. Polyarteritis nodosa: state of the art. Joint Bone Spine, 89:105320, Jul 2022. URL: https://doi.org/10.1016/j.jbspin.2021.105320, doi:10.1016/j.jbspin.2021.105320. This article has 16 citations and is from a peer-reviewed journal.

15. (puechal2022polyarteritisnodosastate media 85b1bd4a): Xavier Puéchal. Polyarteritis nodosa: state of the art. Joint Bone Spine, 89:105320, Jul 2022. URL: https://doi.org/10.1016/j.jbspin.2021.105320, doi:10.1016/j.jbspin.2021.105320. This article has 16 citations and is from a peer-reviewed journal.

16. (puechal2022polyarteritisnodosastate media 858e4031): Xavier Puéchal. Polyarteritis nodosa: state of the art. Joint Bone Spine, 89:105320, Jul 2022. URL: https://doi.org/10.1016/j.jbspin.2021.105320, doi:10.1016/j.jbspin.2021.105320. This article has 16 citations and is from a peer-reviewed journal.

17. (wolff2023polyarteritisnodosaold pages 8-9): Louis Wolff, Alice Horisberger, Laura Moi, Maria P. Karampetsou, and Denis Comte. Polyarteritis nodosa: old disease, new etiologies. International Journal of Molecular Sciences, 24:16668, Nov 2023. URL: https://doi.org/10.3390/ijms242316668, doi:10.3390/ijms242316668. This article has 50 citations.

18. (NCT00315406 chunk 1): Peter Merkel. Determining Disease Activity Biomarkers in Individuals With Polyarteritis Nodosa. University of Pennsylvania. 2006. ClinicalTrials.gov Identifier: NCT00315406

19. (NCT00647166 chunk 1):  Association Corticosteroid/Azathioprine in Microscopic Polyangiitis/ Polyarteritis Nodosa or Eosinophilic Granulomatosis With Polyangiitis (Churg Strauss Syndrome). Assistance Publique - Hôpitaux de Paris. 2008. ClinicalTrials.gov Identifier: NCT00647166

20. (NCT00647166 chunk 2):  Association Corticosteroid/Azathioprine in Microscopic Polyangiitis/ Polyarteritis Nodosa or Eosinophilic Granulomatosis With Polyangiitis (Churg Strauss Syndrome). Assistance Publique - Hôpitaux de Paris. 2008. ClinicalTrials.gov Identifier: NCT00647166