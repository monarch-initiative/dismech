---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T07:43:50.892626'
end_time: '2026-05-05T08:13:33.034613'
duration_seconds: 1782.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fibrocartilaginous Embolism
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fibrocartilaginous Embolism
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Fibrocartilaginous Embolism** covering all of the
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
- **Disease Name:** Fibrocartilaginous Embolism
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Fibrocartilaginous Embolism** covering all of the
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


## Fibrocartilaginous Embolism (FCE) — Comprehensive Disease Characteristics Report

### Scope note
Fibrocartilaginous embolism (FCE) is rare in humans and is often discussed as a mechanism within the broader entity of spontaneous spinal cord infarction (SCI). Consequently, many statistics come from SCI cohorts where FCE is one etiologic subgroup, or from clinically suspected FCE case series and systematic reviews; definitive diagnosis generally requires histopathology/autopsy. (cuello2014acutecervicalmyelopathy pages 1-2, mateen2011clinicallysuspectedfibrocartilaginous pages 6-7, abdelrazek2016fibrocartilaginousembolisma pages 5-6)

| Domain | Key points | Quantitative data | Key sources (year, journal, URL) |
|---|---|---|---|
| Disease synonyms / definition | Fibrocartilaginous embolism (FCE), also called fibrocartilaginous embolization; in veterinary literature often termed fibrocartilaginous embolic myelopathy. It is an ischemic myelopathy / spinal cord infarction caused by embolization of fibrocartilaginous material, presumed to originate from nucleus pulposus of the intervertebral disc; in humans it is usually a diagnosis of exclusion (cuello2014acutecervicalmyelopathy pages 1-2, taous2023spinalcordinfarction pages 1-2, alfarsi2023spinalcordinfarct pages 2-4). | Systematic review identified 52 reported human cases: 39 biopsy-proven and 13 clinically diagnosed (cuello2014acutecervicalmyelopathy pages 1-2). | Cuello et al. 2014, *Journal of Spinal Disorders & Techniques*, https://doi.org/10.1097/bsd.0000000000000115 (cuello2014acutecervicalmyelopathy pages 1-2); Taous et al. 2023, *SAS Journal of Medicine*, https://doi.org/10.36347/sasjm.2023.v09i11.015 (taous2023spinalcordinfarction pages 1-2); Al-Farsi et al. 2023, *Cureus*, https://doi.org/10.7759/cureus.37319 (alfarsi2023spinalcordinfarct pages 2-4) |
| Key clinical features and onset | Typical presentation is sudden back/neck pain followed by rapid neurologic deficit over minutes to hours, with weakness/paralysis, asymmetric deficits, spinothalamic sensory loss, possible bowel/bladder dysfunction, and occasionally respiratory compromise if high cervical cord is involved; often follows minor trauma, heavy lifting, exertion, bending, or Valsalva-like events (alfarsi2023spinalcordinfarct pages 2-4, mateen2011clinicallysuspectedfibrocartilaginous pages 1-2, mateen2011clinicallysuspectedfibrocartilaginous pages 2-3, cuello2014acutecervicalmyelopathy pages 1-2). | In Mayo series, 7/9 (78%) had a precipitating event within 24 h; 8/9 reached maximal weakness within 4 h and all within <12 h (mateen2011clinicallysuspectedfibrocartilaginous pages 2-3). In systematic review, median progression was 6 h (IQR 5–60 h); median age 37 y and 56% female (cuello2014acutecervicalmyelopathy pages 1-2). Review cited ~45% of reported cases were <20 y and 55% female (alfarsi2023spinalcordinfarct pages 2-4). | Mateen et al. 2011, *European Journal of Neurology*, https://doi.org/10.1111/j.1468-1331.2010.03200.x (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7, mateen2011clinicallysuspectedfibrocartilaginous pages 1-2, mateen2011clinicallysuspectedfibrocartilaginous pages 2-3, mateen2011clinicallysuspectedfibrocartilaginous pages 7-8); Cuello et al. 2014, *Journal of Spinal Disorders & Techniques*, https://doi.org/10.1097/bsd.0000000000000115 (cuello2014acutecervicalmyelopathy pages 1-2); Al-Farsi et al. 2023, *Cureus*, https://doi.org/10.7759/cureus.37319 (alfarsi2023spinalcordinfarct pages 2-4) |
| Diagnostic findings (MRI / DWI / STIR, CSF, exclusion workup) | MRI is the main antemortem test. Typical findings: focal or longitudinal T2 cord hyperintensity, often in anterior spinal artery territory with gray-matter predominance; “owl’s eyes” on axial imaging; early scans can be normal. DWI/ADC can show restricted diffusion within hours and help distinguish ischemia from inflammatory myelitis. STIR may show adjacent disc abnormalities (loss of normal T2 signal, disc collapse/desiccation, Schmorl nodes), supporting disc-origin embolism. CSF is often normal but may show mild pleocytosis/protein elevation; diagnosis depends on excluding compressive, inflammatory, infectious, vascular-malformation, embolic, and hypercoagulable causes (risio2010fibrocartilaginousembolicmyelopathy pages 6-8, alfarsi2023spinalcordinfarct pages 2-4, manara2010spinalcordinfarction pages 1-3, manara2010spinalcordinfarction pages 3-4, yamaguchi2019fibrocartilaginousembolismof pages 5-8, cuello2014acutecervicalmyelopathy pages 1-2). | DWI restriction seen in 10/12 spinal cord infarction patients who underwent DWI in a 2023 series (not FCE-specific) (castello2023spinalcordinfarction pages 1-2). Myelography shows intramedullary swelling in ~39–47% of histologically confirmed veterinary FCEM cases; CSF abnormalities reported in up to 44–75% of antemortem veterinary cases (risio2010fibrocartilaginousembolicmyelopathy pages 6-8). | Manara et al. 2010, *Journal of Child Neurology*, https://doi.org/10.1177/0883073809355822 (manara2010spinalcordinfarction pages 1-3, manara2010spinalcordinfarction pages 3-4, manara2010spinalcordinfarction pages 4-5); Yamaguchi et al. 2019, *Pediatric Neurology*, https://doi.org/10.1016/j.pediatrneurol.2019.04.013 (yamaguchi2019fibrocartilaginousembolismof pages 5-8); Cuello et al. 2014, *Journal of Spinal Disorders & Techniques*, https://doi.org/10.1097/bsd.0000000000000115 (cuello2014acutecervicalmyelopathy pages 1-2); Al-Farsi et al. 2023, *Cureus*, https://doi.org/10.7759/cureus.37319 (alfarsi2023spinalcordinfarct pages 2-4); De Risio & Platt 2010, *Vet Clin North Am Small Anim Pract*, https://doi.org/10.1016/j.cvsm.2010.05.003 (risio2010fibrocartilaginousembolicmyelopathy pages 6-8) |
| Epidemiology / proportion among spinal cord infarction | FCE is rare and true incidence is unknown. Within spinal cord infarction cohorts, it represents a minority but recognized etiologic subgroup; substantial fractions of spinal cord infarction remain cryptogenic, complicating attribution (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7, castello2023spinalcordinfarction pages 1-2, castello2023spinalcordinfarction pages 5-7). | Mayo cohort: 9/164 acute spinal cord infarctions = 5.5% (95% CI 2.5–10.2%) clinically suspected FCE (mateen2011clinicallysuspectedfibrocartilaginous pages 1-2). 2023 41-patient series: 6/41 = 14.6% attributed to FCE; 29.3% had no determined etiology (castello2023spinalcordinfarction pages 1-2, castello2023spinalcordinfarction pages 5-7). Broader reviews cited unclear etiology in 24–74% of spinal cord infarction cases (mcbride2024nonsurgicalspinalcord pages 3-4). | Mateen et al. 2011, *European Journal of Neurology*, https://doi.org/10.1111/j.1468-1331.2010.03200.x (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7, mateen2011clinicallysuspectedfibrocartilaginous pages 1-2); Ros Castelló et al. 2023, *Neurología (English Edition)*, https://doi.org/10.1016/j.nrleng.2020.11.004 (castello2023spinalcordinfarction pages 1-2, castello2023spinalcordinfarction pages 5-7); McBride et al. 2024, *Spinal Cord Series and Cases*, https://doi.org/10.1038/s41394-024-00665-y (mcbride2024nonsurgicalspinalcord pages 3-4) |
| Treatments tried and outcomes | No therapy has proven efficacy specifically for FCE. Reported acute treatments include corticosteroids, plasma exchange, IVIG, heparin/antiplatelet therapy, analgesia, decompressive surgery in selected cases, permissive mean arterial pressure augmentation, cerebrospinal fluid drainage, and intensive neurorehabilitation; most reports emphasize supportive care and rehabilitation rather than disease-specific therapy (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7, mateen2011clinicallysuspectedfibrocartilaginous pages 1-2, alfarsi2023spinalcordinfarct pages 2-4, NCT04372758 chunk 1). | In Mayo series, IV steroids, plasma exchange, IV heparin, IVIG, and decompressive surgery did not produce meaningful acute improvement; median follow-up disability was severe (median mRS 4, Barthel index 45), with no deaths or recurrences in that cohort (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7). In 2023 spinal cord infarction series, after median 24 months only 29.2% walked unaided; 3-month mortality 9.8% and overall mortality at follow-up 36.6% for the whole SCI cohort (not FCE-specific) (castello2023spinalcordinfarction pages 1-2, castello2023spinalcordinfarction pages 5-7). A pediatric case report described substantial improvement after CSF drainage + MAP augmentation + steroids, but evidence remains anecdotal (NCT04372758 chunk 1). | Mateen et al. 2011, *European Journal of Neurology*, https://doi.org/10.1111/j.1468-1331.2010.03200.x (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7, mateen2011clinicallysuspectedfibrocartilaginous pages 1-2); Al-Farsi et al. 2023, *Cureus*, https://doi.org/10.7759/cureus.37319 (alfarsi2023spinalcordinfarct pages 2-4); Ros Castelló et al. 2023, *Neurología (English Edition)*, https://doi.org/10.1016/j.nrleng.2020.11.004 (castello2023spinalcordinfarction pages 1-2, castello2023spinalcordinfarction pages 5-7); ClinicalTrials.gov NCT04372758, 2020, https://clinicaltrials.gov/study/NCT04372758 (NCT04372758 chunk 1) |


*Table: This table condenses the most clinically relevant evidence on fibrocartilaginous embolism, including definition, presentation, diagnostics, epidemiology, and treatment/outcome data. It is useful as a quick reference for building a disease knowledge base entry from the cited primary and recent sources.*

---

## 1. Disease Information

### 1.1 Concise overview / definition
Fibrocartilaginous embolism (FCE) is an ischemic myelopathy (spinal cord infarction) caused by embolization of fibrocartilaginous material, presumed to originate from the nucleus pulposus of the intervertebral disc, into vessels supplying the spinal cord. In clinical practice it is typically a diagnosis of exclusion because definitive confirmation is usually postmortem or via biopsy/histopathology. (cuello2014acutecervicalmyelopathy pages 1-2, taous2023spinalcordinfarction pages 1-2, abdelrazek2016fibrocartilaginousembolisma pages 5-6)

### 1.2 Synonyms / alternative names
- **Fibrocartilaginous embolization** (human literature) (manara2010spinalcordinfarction pages 1-3, abdelrazek2016fibrocartilaginousembolisma pages 1-2)
- **Fibrocartilaginous embolic myelopathy (FCEM)** (common in veterinary literature; used as a close naturally occurring analog) (risio2010fibrocartilaginousembolicmyelopathy pages 6-8)

### 1.3 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
Within the retrieved full-text evidence, explicit ontology identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH, MONDO) were **not stated**. Therefore, this report cannot provide validated identifier mappings from the present evidence set. (cuello2014acutecervicalmyelopathy pages 1-2, abdelrazek2016fibrocartilaginousembolisma pages 5-6)

### 1.4 Evidence source type
Evidence is primarily:
- **Human clinical**: case reports, systematic reviews, and SCI cohorts with FCE as a subgroup (cuello2014acutecervicalmyelopathy pages 1-2, castello2023spinalcordinfarction pages 1-2, mateen2011clinicallysuspectedfibrocartilaginous pages 6-7)
- **Veterinary clinical/pathology**: naturally occurring FCEM in dogs/cats with histologic confirmation and MRI phenotype (risio2010fibrocartilaginousembolicmyelopathy pages 6-8, togawa2024outcomeinparaplegic pages 1-2)
- **Clinical registry/trial record**: observational SCI cohort explicitly including FCE criteria (NCT04372758 chunk 1)

---

## 2. Etiology

### 2.1 Primary causal factors
**Mechanistic cause (current understanding):** migration/embolization of nucleus pulposus–derived fibrocartilaginous material into spinal cord vasculature causing arterial occlusion and infarction. (taous2023spinalcordinfarction pages 1-2, abdelrazek2016fibrocartilaginousembolisma pages 5-6, abdelrazek2016fibrocartilaginousembolisma pages 1-2)

### 2.2 Risk factors
FCE often follows **minor trauma or mechanical/pressure events** that plausibly increase intradiscal or intra-vertebral pressure (e.g., heavy lifting, physical exertion, bending, Valsalva-like maneuvers). (mateen2011clinicallysuspectedfibrocartilaginous pages 2-3, zalewski2019characteristicsofspontaneous pages 3-4, abdelrazek2016fibrocartilaginousembolisma pages 5-6)

Quantitative examples:
- In a Mayo clinically suspected FCE cohort, **7/9 (78%)** had a precipitating event within 24 hours (motor vehicle accident, heavy lifting, exertion, bending). (mateen2011clinicallysuspectedfibrocartilaginous pages 2-3)
- In spontaneous SCI more broadly, **33/133 (25%)** reported a precipitating physical maneuver (e.g., lifting/Valsalva). (zalewski2019characteristicsofspontaneous pages 3-4)

**Vascular risk factors:** Many patients with spontaneous SCI have vascular risk factors, but FCE is considered particularly in patients with fewer traditional vascular risk factors and supportive disc/vertebral imaging changes; some proposed criteria exclude patients with >2 vascular risk factors. (mateen2011clinicallysuspectedfibrocartilaginous pages 7-8, zalewski2019characteristicsofspontaneous pages 1-2)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence. (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7, abdelrazek2016fibrocartilaginousembolisma pages 5-6)

### 2.4 Gene–environment interactions
No validated gene–environment interactions were identified for human FCE in the retrieved evidence. (abdelrazek2016fibrocartilaginousembolisma pages 5-6)

---

## 3. Phenotypes (clinical presentation)

### 3.1 Core phenotype spectrum
Typical presentation involves:
- **Acute back/neck pain** followed by rapid neurological deficit (mateen2011clinicallysuspectedfibrocartilaginous pages 2-3, cuello2014acutecervicalmyelopathy pages 1-2)
- **Acute paresis/paralysis** (paraparesis/paraplegia or quadriparesis/quadriplegia), often initially flaccid with hyporeflexia (alfarsi2023spinalcordinfarct pages 2-4, chukwudelunzu2025fibrocartilaginousembolismspinala pages 2-3)
- **Sensory level**; commonly selective impairment of pain/temperature (spinothalamic) with relative dorsal column sparing in anterior spinal artery territory presentations (alfarsi2023spinalcordinfarct pages 2-4, zalewski2019characteristicsofspontaneous pages 3-4)
- **Autonomic dysfunction** (neurogenic bladder/bowel) (alfarsi2023spinalcordinfarct pages 2-4)

### 3.2 Age of onset and temporal profile
- FCE is described across ages; reported human cases include **adolescents** and **middle-aged adults** (alfarsi2023spinalcordinfarct pages 2-4, cuello2014acutecervicalmyelopathy pages 1-2)
- Time course is often hyperacute-to-acute.
  - In the Mayo suspected-FCE cohort: **time to maximal weakness ≤4 h in 8/9** and **<12 h in all** (range minutes to 11 h). (mateen2011clinicallysuspectedfibrocartilaginous pages 2-3)
  - In spontaneous SCI cohort (not limited to FCE): **nadir within 12 h in 77%**. (zalewski2019characteristicsofspontaneous pages 1-2)

### 3.3 Severity/progression
Deficits typically progress over minutes to hours to a nadir and then stabilize; severe disability is common, but recovery varies depending on lesion extent and level and access to rehabilitation. (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7, shah2018fibrocartilaginousemboliin pages 4-4)

### 3.4 Suggested HPO terms (non-exhaustive)
Based on the above clinical features:
- Acute pain: **Back pain (HP:0003418)**; **Neck pain (HP:0000467)**
- Motor deficits: **Paraplegia (HP:0003401)**; **Quadriplegia (HP:0003293)**; **Muscle weakness (HP:0001324)**
- Sensory deficits: **Loss of pain sensation (HP:0007012)**; **Sensory level (HP:0033725)** (term availability may vary across HPO releases)
- Autonomic: **Neurogenic bladder (HP:0000010)**; **Urinary retention (HP:0000016)**

(These HPO suggestions are ontology-mapping aids; the retrieved papers describe the phenotypes but do not provide HPO codes.) (alfarsi2023spinalcordinfarct pages 2-4, mateen2011clinicallysuspectedfibrocartilaginous pages 2-3, zalewski2019characteristicsofspontaneous pages 3-4)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes / variants
No causal genes, pathogenic germline variants, or inherited pattern are supported by the retrieved evidence. Human FCE is primarily treated as a **mechanical/vascular phenomenon** rather than a monogenic disease. (abdelrazek2016fibrocartilaginousembolisma pages 5-6)

### 4.2 Molecular profiling / omics
No transcriptomic/proteomic/metabolomic signatures specific to human FCE were identified in the retrieved evidence. (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7)

---

## 5. Environmental Information

### 5.1 Environmental/lifestyle triggers
The most consistently reported environmental/behavioral correlates are **activities increasing spinal load/pressure**, including heavy lifting and physical exertion, and other minor traumatic or Valsalva-like events. (mateen2011clinicallysuspectedfibrocartilaginous pages 2-3, zalewski2019characteristicsofspontaneous pages 3-4)

### 5.2 Infectious agents
No infectious etiology is supported; infectious/inflammatory causes are part of the differential diagnosis to be excluded. (mateen2011clinicallysuspectedfibrocartilaginous pages 2-3, abdelrazek2016fibrocartilaginousembolisma pages 5-6)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (trigger → lesion → symptoms)
1. **Trigger** (often minor exertion/trauma/pressure event) temporally associated with symptom onset (mateen2011clinicallysuspectedfibrocartilaginous pages 2-3, abdelrazek2016fibrocartilaginousembolisma pages 5-6)
2. **Disc-derived fibrocartilage enters vasculature** (nucleus pulposus material migration/embolization) (taous2023spinalcordinfarction pages 1-2, abdelrazek2016fibrocartilaginousembolisma pages 1-2)
3. **Vascular occlusion** (often radicular/anterior spinal artery territory) → **spinal cord ischemia and infarction** (manara2010spinalcordinfarction pages 3-4, cuello2014acutecervicalmyelopathy pages 1-2)
4. **Clinical syndrome** of acute myelopathy: pain, rapid paralysis/weakness, sensory level, autonomic dysfunction (alfarsi2023spinalcordinfarct pages 2-4, mateen2011clinicallysuspectedfibrocartilaginous pages 2-3)

### 6.2 Upstream vs downstream processes
- Upstream: mechanical/disc event leading to embolization (taous2023spinalcordinfarction pages 1-2, abdelrazek2016fibrocartilaginousembolisma pages 5-6)
- Downstream: ischemic cytotoxic edema and infarction, which is detectable by diffusion restriction on MRI and leads to neurologic deficit (manara2010spinalcordinfarction pages 3-4, zalewski2019characteristicsofspontaneous pages 3-4)

### 6.3 Suggested GO biological process terms (conceptual mapping)
- **Ischemic process** / response to hypoxia (e.g., “response to hypoxia”, “cell death”) consistent with infarction biology (supported indirectly via DWI evidence of cytotoxic edema rather than specific molecular assays). (manara2010spinalcordinfarction pages 3-4)

### 6.4 Suggested Cell Ontology (CL) cell types
Primary tissue affected is spinal cord gray/white matter; cell types implicated in ischemic injury include:
- **Spinal cord neuron** populations (especially anterior horn motor neurons in ASA territory) (manara2010spinalcordinfarction pages 3-4)
- **Glial cells** involved in infarct evolution (inferred from ischemic myelopathy context; not directly profiled here). (manara2010spinalcordinfarction pages 3-4)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- **Primary**: spinal cord (central nervous system). (cuello2014acutecervicalmyelopathy pages 1-2, abdelrazek2016fibrocartilaginousembolisma pages 1-2)

### 7.2 Localization patterns
- Human systematic review: cervical cord frequently involved (**48%** in one review) (cuello2014acutecervicalmyelopathy pages 1-2)
- In a 2023 SCI cohort: thoracic region most often affected overall (**68.2%**) (not FCE-specific) (castello2023spinalcordinfarction pages 1-2)

### 7.3 Suggested UBERON terms (conceptual mapping)
- **Spinal cord (UBERON:0002240)**
- Segmental localization (cervical/thoracic/lumbar spinal cord)

---

## 8. Temporal Development

### 8.1 Onset
Hyperacute/acute onset is characteristic.
- Mayo suspected-FCE cohort: maximal deficits within **<12 h** in all cases (mateen2011clinicallysuspectedfibrocartilaginous pages 2-3)
- Spontaneous SCI cohort: nadir within **12 h in 77%** (zalewski2019characteristicsofspontaneous pages 1-2)

### 8.2 Course
Often stabilizes after reaching nadir; longer-term course depends on infarct size/level and rehabilitation. (shah2018fibrocartilaginousemboliin pages 4-4)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
Population incidence/prevalence for human FCE remains poorly defined; however, proportions within SCI cohorts are reported:
- Mayo SCI cohort: **9/164 (5.5%; 95% CI 2.5–10.2%)** clinically suspected FCE among acute spinal cord infarctions. (mateen2011clinicallysuspectedfibrocartilaginous pages 1-2)
- 2023 single-center 41-patient SCI series: **fibrocartilaginous embolism 14.6%** (6 cases); **etiology undetermined 29.3%**. (castello2023spinalcordinfarction pages 1-2, castello2023spinalcordinfarction pages 5-7)

### 9.2 Sex and age distribution
- Systematic review of reported FCE cases: median age 37 years; **56% female**. (cuello2014acutecervicalmyelopathy pages 1-2)
- Mayo suspected-FCE cohort: 6 men and 3 women (median age 46). (mateen2011clinicallysuspectedfibrocartilaginous pages 2-3)

---

## 10. Diagnostics

### 10.1 Key clinical/imaging tests
**MRI spine (core test):**
- T2 patterns typical for SCI include “owl eyes” and “pencil-like” hyperintensity (SCI data; also leveraged in FCE suspicion). (zalewski2019characteristicsofspontaneous pages 3-4, zalewski2019characteristicsofspontaneous pages 1-2)
- FCE case reports emphasize cord swelling and T2 hyperintensity, often without early enhancement; adjacent disc pathology or Schmorl nodes can support FCE mechanism. (yamaguchi2019fibrocartilaginousembolismof pages 5-8, alfarsi2023spinalcordinfarct pages 2-4)

**Diffusion-weighted imaging (DWI/ADC):**
- Helps distinguish cytotoxic (ischemic) from vasogenic (inflammatory) edema; recommended for acute myelopathy workups. (manara2010spinalcordinfarction pages 3-4, manara2010spinalcordinfarction pages 4-5)
- In spontaneous SCI cohort: DWI/ADC restriction in **19/29 (67%)**. (zalewski2019characteristicsofspontaneous pages 3-4)

**CSF:** usually normal or mild nonspecific abnormalities; used to exclude inflammation.
- In spontaneous SCI: mild inflammation in **7/89 (8%)** (elevated nucleated cells). (zalewski2019characteristicsofspontaneous pages 1-2)

### 10.2 Proposed diagnostic criteria / algorithms (expert consensus-level)
- **Spontaneous SCI diagnostic criteria** were proposed and validated in a large JAMA Neurology cohort; hallmark clinical discriminator includes rapid time-to-nadir (<12 h typical) with supportive MRI patterns and confirmatory DWI/vertebral infarction findings. (zalewski2019characteristicsofspontaneous pages 1-2, zalewski2019characteristicsofspontaneous pages 3-4)
- **FCE-focused stepwise approach** (review-based): establish myelopathy; exclude trauma/compression by imaging; exclude inflammatory myelopathies using CSF (no pleocytosis/IgG index elevation) and lack of gadolinium enhancement; interpret vascular distribution and supportive adjacent disc/vertebral findings as increasing likelihood. (abdelrazek2016fibrocartilaginousembolisma pages 5-6, chukwudelunzu2025fibrocartilaginousembolismspinala pages 2-3)

### 10.3 Differential diagnosis
Frequently confounded with inflammatory myelopathies (e.g., transverse myelitis) and other acute myelopathies; multiple reports note misdiagnosis risk and delay. (alfarsi2023spinalcordinfarct pages 2-4, zalewski2019characteristicsofspontaneous pages 1-2)

### 10.4 Pathology
Definitive diagnosis is histopathologic identification of fibrocartilaginous material within spinal cord vessels (often autopsy). (risio2010fibrocartilaginousembolicmyelopathy pages 6-8, abdelrazek2016fibrocartilaginousembolisma pages 1-2)

---

## 11. Outcome / Prognosis

### 11.1 Human prognosis
- In Mayo clinically suspected FCE series: median **mRS 4 (range 3–5)** and Barthel index median **45** among 7, reflecting substantial disability; no deaths or recurrences at mean 2.90-year follow-up. (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7)
- In a 2023 SCI cohort (all-cause SCI, not FCE-specific): after median 24 months, **29.2% walked unaided**; 3-month mortality **9.8%** and mortality at end of follow-up **36.6%**. (castello2023spinalcordinfarction pages 5-7)

### 11.2 Prognostic factors (general SCI / FCE-inferred)
Severity at onset and lesion extent influence recovery; SCI literature identifies older age, vascular risk factors, and anterior spinal artery watershed involvement as worse prognostic indicators. (mcbride2024nonsurgicalspinalcord pages 3-4)

---

## 12. Treatment

### 12.1 Pharmacotherapy and acute interventions
Evidence does not support a specific proven acute therapy for FCE.
- In Mayo suspected-FCE series, **IV steroids, plasma exchange, IV heparin, IVIG, and decompressive surgery** did **not** yield meaningful acute improvement. (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7)
- Some cases are treated with antiplatelet therapy (e.g., aspirin) after excluding inflammatory etiologies; this is largely extrapolated rather than evidence-based for FCE specifically. (alfarsi2023spinalcordinfarct pages 2-4, castello2023spinalcordinfarction pages 5-7)

### 12.2 Neurocritical care / neuroprotection (case-based)
A pediatric illustrative case applied **continuous CSF drainage** plus **mean arterial pressure augmentation** (permissive hypertension) and steroids with substantial neurological improvement; this is hypothesis-generating and extrapolated from aortic surgery spinal cord protection principles. (fedaravicius2021successfulmanagementof pages 1-2)

### 12.3 Rehabilitation (real-world implementation)
Rehabilitation is consistently emphasized.
- Pediatric rehabilitation case literature reports substantial functional gains after intensive inpatient rehabilitation and advocates early initiation of comprehensive rehab. (shah2018fibrocartilaginousemboliin pages 4-4)
- In an inpatient rehab cohort of probable FCEM (31 patients), functional scores improved (motor FIM increased from 36 to 69 during rehab), though many still used wheelchairs as primary mobility at discharge. (moore2018fibrocartilaginousembolicmyelopathy pages 1-2)

### 12.4 MAXO term suggestions (conceptual mapping)
- **Rehabilitation therapy** (e.g., physical therapy/occupational therapy) (shah2018fibrocartilaginousemboliin pages 4-4)
- **Antiplatelet therapy** (aspirin in some cases) (alfarsi2023spinalcordinfarct pages 2-4)
- **Cerebrospinal fluid drainage** (case-based neuroprotection) (fedaravicius2021successfulmanagementof pages 1-2)
- **Blood pressure augmentation / hemodynamic support** (fedaravicius2021successfulmanagementof pages 1-2)

---

## 13. Prevention
No validated primary prevention strategy exists because FCE is rare, unpredictable, and typically associated with nonspecific mechanical triggers. Practical prevention is therefore limited to general spine safety and vascular-risk management when appropriate, but this is not evidence-based for FCE prevention specifically in the retrieved literature. (abdelrazek2016fibrocartilaginousembolisma pages 5-6)

---

## 14. Other Species / Natural Disease

### 14.1 Naturally occurring veterinary analogs
In veterinary neurology, **fibrocartilaginous embolic myelopathy (FCEM)** is a well-recognized cause of peracute noncompressive myelopathy in dogs/cats, with diagnosis definitively confirmed by histology showing fibrocartilaginous material in spinal vessels. (risio2010fibrocartilaginousembolicmyelopathy pages 6-8)

### 14.2 Veterinary outcome statistics (useful for comparative prognosis biology)
In a 2024 cohort of paraplegic dogs with thoracolumbar FCEM/ANNPE:
- **Deep pain positive**: 9/14 (64.3%) regained independent ambulation
- **Deep pain negative**: 1/12 (8.3%) regained independent ambulation
- Deep pain negative status strongly predicted poor recovery (OR 47.40). (togawa2024outcomeinparaplegic pages 1-2)

These naturally occurring datasets support the central prognostic role of initial neurologic severity and can inform translational hypotheses, but they are not direct human clinical evidence. (togawa2024outcomeinparaplegic pages 1-2, risio2010fibrocartilaginousembolicmyelopathy pages 6-8)

---

## 15. Model Organisms
No engineered genetic model organism systems were identified in the retrieved evidence. The most relevant “models” are **naturally occurring veterinary FCEM cases** and imaging/clinical cohorts, which provide translationally relevant ischemic myelopathy phenotypes and opportunities for biomarker and neuroprotection research. (risio2010fibrocartilaginousembolicmyelopathy pages 6-8, togawa2024outcomeinparaplegic pages 1-2)

---

## Recent developments and latest research emphasis (2023–2024)
- **Human cohort-level update (2023):** a 41-patient spinal cord infarction series reported fibrocartilaginous embolism as **14.6%** of etiologies and documented major long-term disability (only **29.2% walking unaided** at median 24 months) and substantial mortality, underscoring persistent unmet needs in diagnosis and post-acute care. (castello2023spinalcordinfarction pages 1-2, castello2023spinalcordinfarction pages 5-7)
- **Prognosis synthesis (2024):** a long-term follow-up case series/review context emphasizes that a large fraction of SCI remains of unclear etiology in published studies (24–74%) and that long-term disability is common, with prognosis linked to initial severity and risk factors. (mcbride2024nonsurgicalspinalcord pages 3-4)
- **Veterinary prognosis (2024):** robust prognostic discrimination using deep pain sensation in severe FCEM/ANNPE provides an example of clinically actionable predictors in a natural disease analog. (togawa2024outcomeinparaplegic pages 1-2)

---

## Clinical trials / registries
- **ClinicalTrials.gov NCT04372758 (EDMIAS)**: completed retrospective observational cohort (n=60) aimed at characterizing acute spontaneous SCI (2010–2020) and explicitly includes evaluation/application of **fibrocartilaginous embolism criteria (2015)** as a secondary outcome, reflecting ongoing efforts to operationalize FCE diagnosis within SCI research frameworks. URL: https://clinicaltrials.gov/study/NCT04372758 (NCT04372758 chunk 1)

---

## Key limitations / data gaps
- Ontology identifier mappings (MONDO/MeSH/ICD/Orphanet) were not available in retrieved evidence texts.
- Human FCE evidence remains dominated by case reports and small series; many treatment strategies are extrapolated from SCI or neuroprotection principles rather than validated by controlled studies. (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7, fedaravicius2021successfulmanagementof pages 1-2)


References

1. (cuello2014acutecervicalmyelopathy pages 1-2): Juan P. Cuello, Santiago Ortega-Gutierrez, Guillermo Linares, Sachin Agarwal, Alyson Cunningham, Jay P. Mohr, Stephan A. Mayer, Randolph S. Marshall, Jan Claassen, Neeraj Badjatia, Mitchel S.V. Elkind, and Kiwon Lee. Acute cervical myelopathy due to presumed fibrocartilaginous embolism: a case report and systematic review of the literature. Journal of Spinal Disorders and Techniques, 27:E276–E281, Dec 2014. URL: https://doi.org/10.1097/bsd.0000000000000115, doi:10.1097/bsd.0000000000000115. This article has 18 citations.

2. (mateen2011clinicallysuspectedfibrocartilaginous pages 6-7): F. Mateen, F. Mateen, Priya Monrad, A. L. Hunderfund, Carrie E. Robertson, and E. J. Sorenson. Clinically suspected fibrocartilaginous embolism: clinical characteristics, treatments, and outcomes. European Journal of Neurology, 18:218-225, Feb 2011. URL: https://doi.org/10.1111/j.1468-1331.2010.03200.x, doi:10.1111/j.1468-1331.2010.03200.x. This article has 93 citations and is from a domain leading peer-reviewed journal.

3. (abdelrazek2016fibrocartilaginousembolisma pages 5-6): Mahmoud A. AbdelRazek, Ashkan Mowla, Salman Farooq, Nicholas Silvestri, Robert Sawyer, and Gil Wolfe. Fibrocartilaginous embolism: a comprehensive review of an under-studied cause of spinal cord infarction and proposed diagnostic criteria. The Journal of Spinal Cord Medicine, 39:146-154, Feb 2016. URL: https://doi.org/10.1080/10790268.2015.1116726, doi:10.1080/10790268.2015.1116726. This article has 116 citations.

4. (taous2023spinalcordinfarction pages 1-2): Abdellah Taous, Taoufik Boubga, Tarik Boulahri, Soufiane Belabbes, Taoufik Africha, Omar Boulahroud, and Maha Ait Berri. Spinal cord infarction owing to likely fibrocartilaginous embolism. SAS Journal of Medicine, 9:1207-1209, Nov 2023. URL: https://doi.org/10.36347/sasjm.2023.v09i11.015, doi:10.36347/sasjm.2023.v09i11.015. This article has 0 citations.

5. (alfarsi2023spinalcordinfarct pages 2-4): Said A Al-Farsi, Haifa Al-Abri, Eiman Al-Ajmi, and Abdullah Al-Asmi. Spinal cord infarct due to fibrocartilaginous embolism in an adolescent boy: a case report and literature review. Cureus, Apr 2023. URL: https://doi.org/10.7759/cureus.37319, doi:10.7759/cureus.37319. This article has 7 citations.

6. (mateen2011clinicallysuspectedfibrocartilaginous pages 1-2): F. Mateen, F. Mateen, Priya Monrad, A. L. Hunderfund, Carrie E. Robertson, and E. J. Sorenson. Clinically suspected fibrocartilaginous embolism: clinical characteristics, treatments, and outcomes. European Journal of Neurology, 18:218-225, Feb 2011. URL: https://doi.org/10.1111/j.1468-1331.2010.03200.x, doi:10.1111/j.1468-1331.2010.03200.x. This article has 93 citations and is from a domain leading peer-reviewed journal.

7. (mateen2011clinicallysuspectedfibrocartilaginous pages 2-3): F. Mateen, F. Mateen, Priya Monrad, A. L. Hunderfund, Carrie E. Robertson, and E. J. Sorenson. Clinically suspected fibrocartilaginous embolism: clinical characteristics, treatments, and outcomes. European Journal of Neurology, 18:218-225, Feb 2011. URL: https://doi.org/10.1111/j.1468-1331.2010.03200.x, doi:10.1111/j.1468-1331.2010.03200.x. This article has 93 citations and is from a domain leading peer-reviewed journal.

8. (mateen2011clinicallysuspectedfibrocartilaginous pages 7-8): F. Mateen, F. Mateen, Priya Monrad, A. L. Hunderfund, Carrie E. Robertson, and E. J. Sorenson. Clinically suspected fibrocartilaginous embolism: clinical characteristics, treatments, and outcomes. European Journal of Neurology, 18:218-225, Feb 2011. URL: https://doi.org/10.1111/j.1468-1331.2010.03200.x, doi:10.1111/j.1468-1331.2010.03200.x. This article has 93 citations and is from a domain leading peer-reviewed journal.

9. (risio2010fibrocartilaginousembolicmyelopathy pages 6-8): Luisa De Risio and Simon R. Platt. Fibrocartilaginous embolic myelopathy in small animals. The Veterinary clinics of North America. Small animal practice, 40 5:859-69, Sep 2010. URL: https://doi.org/10.1016/j.cvsm.2010.05.003, doi:10.1016/j.cvsm.2010.05.003. This article has 121 citations.

10. (manara2010spinalcordinfarction pages 1-3): Renzo Manara, Milena Calderone, Maria Savina Severino, Valentina Citton, Irene Toldo, Anna Maria Laverda, and Stefano Sartori. Spinal cord infarction due to fibrocartilaginous embolization: the role of diffusion weighted imaging and short-tau inversion recovery sequences. Journal of Child Neurology, 25:1024-1028, Mar 2010. URL: https://doi.org/10.1177/0883073809355822, doi:10.1177/0883073809355822. This article has 34 citations and is from a peer-reviewed journal.

11. (manara2010spinalcordinfarction pages 3-4): Renzo Manara, Milena Calderone, Maria Savina Severino, Valentina Citton, Irene Toldo, Anna Maria Laverda, and Stefano Sartori. Spinal cord infarction due to fibrocartilaginous embolization: the role of diffusion weighted imaging and short-tau inversion recovery sequences. Journal of Child Neurology, 25:1024-1028, Mar 2010. URL: https://doi.org/10.1177/0883073809355822, doi:10.1177/0883073809355822. This article has 34 citations and is from a peer-reviewed journal.

12. (yamaguchi2019fibrocartilaginousembolismof pages 5-8): Hiroshi Yamaguchi, Hiroaki Nagase, Masahiro Nishiyama, Shoichi Tokumoto, Daisaku Toyoshima, Yoshinobu Akasaka, Azusa Maruyama, and Kazumoto Iijima. Fibrocartilaginous embolism of the spinal cord in children: a case report and review of literature. Pediatric neurology, 99:3-6, Oct 2019. URL: https://doi.org/10.1016/j.pediatrneurol.2019.04.013, doi:10.1016/j.pediatrneurol.2019.04.013. This article has 29 citations and is from a peer-reviewed journal.

13. (castello2023spinalcordinfarction pages 1-2): V. Ros Castelló, A. Sánchez Sánchez, E. Natera Villalba, A. Gómez López, P. Parra, F. Rodríguez Jorge, J. Buisán Catevilla, N. García Barragán, J. Masjuán, and Í. Corral. Spinal cord infarction: aetiology, imaging findings, and prognostic factors in a series of 41 patients. Neurología (English Edition), 38:391-398, Jul 2023. URL: https://doi.org/10.1016/j.nrleng.2020.11.004, doi:10.1016/j.nrleng.2020.11.004. This article has 20 citations.

14. (manara2010spinalcordinfarction pages 4-5): Renzo Manara, Milena Calderone, Maria Savina Severino, Valentina Citton, Irene Toldo, Anna Maria Laverda, and Stefano Sartori. Spinal cord infarction due to fibrocartilaginous embolization: the role of diffusion weighted imaging and short-tau inversion recovery sequences. Journal of Child Neurology, 25:1024-1028, Mar 2010. URL: https://doi.org/10.1177/0883073809355822, doi:10.1177/0883073809355822. This article has 34 citations and is from a peer-reviewed journal.

15. (castello2023spinalcordinfarction pages 5-7): V. Ros Castelló, A. Sánchez Sánchez, E. Natera Villalba, A. Gómez López, P. Parra, F. Rodríguez Jorge, J. Buisán Catevilla, N. García Barragán, J. Masjuán, and Í. Corral. Spinal cord infarction: aetiology, imaging findings, and prognostic factors in a series of 41 patients. Neurología (English Edition), 38:391-398, Jul 2023. URL: https://doi.org/10.1016/j.nrleng.2020.11.004, doi:10.1016/j.nrleng.2020.11.004. This article has 20 citations.

16. (mcbride2024nonsurgicalspinalcord pages 3-4): Fionán McBride, Jane Anketell, Gavin V. McDonnell, Suzanne Maguire, and Karen M. Doherty. Non-surgical spinal cord infarction: case series & long-term follow-up of functional outcome. Spinal Cord Series and Cases, Oct 2024. URL: https://doi.org/10.1038/s41394-024-00665-y, doi:10.1038/s41394-024-00665-y. This article has 1 citations and is from a peer-reviewed journal.

17. (NCT04372758 chunk 1):  Descriptive Study of Acute Spontaneous Spinal Cord Infarction. University Hospital, Montpellier. 2020. ClinicalTrials.gov Identifier: NCT04372758

18. (abdelrazek2016fibrocartilaginousembolisma pages 1-2): Mahmoud A. AbdelRazek, Ashkan Mowla, Salman Farooq, Nicholas Silvestri, Robert Sawyer, and Gil Wolfe. Fibrocartilaginous embolism: a comprehensive review of an under-studied cause of spinal cord infarction and proposed diagnostic criteria. The Journal of Spinal Cord Medicine, 39:146-154, Feb 2016. URL: https://doi.org/10.1080/10790268.2015.1116726, doi:10.1080/10790268.2015.1116726. This article has 116 citations.

19. (togawa2024outcomeinparaplegic pages 1-2): Go Togawa, Melissa J. Lewis, and Dillon Devathasan. Outcome in paraplegic dogs with or without pain perception due to thoracolumbar fibrocartilaginous embolic myelopathy or acute non-compressive nucleus pulposus extrusion. Frontiers in Veterinary Science, May 2024. URL: https://doi.org/10.3389/fvets.2024.1406843, doi:10.3389/fvets.2024.1406843. This article has 7 citations and is from a peer-reviewed journal.

20. (zalewski2019characteristicsofspontaneous pages 3-4): Nicholas L. Zalewski, Alejandro A. Rabinstein, Karl N. Krecke, Robert D. Brown, Eelco F. M. Wijdicks, Brian G. Weinshenker, Timothy J. Kaufmann, Jonathan M. Morris, Allen J. Aksamit, J. D. Bartleson, Giuseppe Lanzino, Melissa M. Blessing, and Eoin P. Flanagan. Characteristics of spontaneous spinal cord infarction and proposed diagnostic criteria. JAMA Neurology, 76:56–63, Jan 2019. URL: https://doi.org/10.1001/jamaneurol.2018.2734, doi:10.1001/jamaneurol.2018.2734. This article has 249 citations and is from a highest quality peer-reviewed journal.

21. (zalewski2019characteristicsofspontaneous pages 1-2): Nicholas L. Zalewski, Alejandro A. Rabinstein, Karl N. Krecke, Robert D. Brown, Eelco F. M. Wijdicks, Brian G. Weinshenker, Timothy J. Kaufmann, Jonathan M. Morris, Allen J. Aksamit, J. D. Bartleson, Giuseppe Lanzino, Melissa M. Blessing, and Eoin P. Flanagan. Characteristics of spontaneous spinal cord infarction and proposed diagnostic criteria. JAMA Neurology, 76:56–63, Jan 2019. URL: https://doi.org/10.1001/jamaneurol.2018.2734, doi:10.1001/jamaneurol.2018.2734. This article has 249 citations and is from a highest quality peer-reviewed journal.

22. (chukwudelunzu2025fibrocartilaginousembolismspinala pages 2-3): FE Chukwudelunzu and T Young. Fibrocartilaginous embolism spinal cord infarction, mistaken for glial fibrillary acidic protein autoimmune transverse myelitis: a case report. Unknown journal, 2025.

23. (shah2018fibrocartilaginousemboliin pages 4-4): Supriya Shah and Phillip Bryant. Fibrocartilaginous emboli in the pediatric population: the role of rehabilitation in facilitating functional recovery. Journal of Pediatric Rehabilitation Medicine, 11:53-56, Mar 2018. URL: https://doi.org/10.3233/prm-170502, doi:10.3233/prm-170502. This article has 11 citations.

24. (fedaravicius2021successfulmanagementof pages 1-2): Augustinas Fedaravičius, Yael Feinstein, Isaac Lazar, Micky Gidon, Ilan Shelef, Elad Avraham, Arimantas Tamašauskas, and Israel Melamed. Successful management of spinal cord ischemia in a pediatric patient with fibrocartilaginous embolism: illustrative case. Journal of Neurosurgery: Case Lessons, Sep 2021. URL: https://doi.org/10.3171/case21380, doi:10.3171/case21380. This article has 5 citations.

25. (moore2018fibrocartilaginousembolicmyelopathy pages 1-2): Brittany J. Moore, Anna M. Batterson, Marianne T. Luetmer, and Ronald K. Reeves. Fibrocartilaginous embolic myelopathy: demographics, clinical presentation, and functional outcomes. Spinal Cord, 56:1144-1150, May 2018. URL: https://doi.org/10.1038/s41393-018-0159-y, doi:10.1038/s41393-018-0159-y. This article has 12 citations and is from a peer-reviewed journal.